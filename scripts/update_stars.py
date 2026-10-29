#!/usr/bin/env python3
"""Refresh one complete GitHub Stars snapshot and render both README catalogs."""

from __future__ import annotations

import argparse
import copy
import html
import json
import os
import re
import sys
import time
from datetime import datetime, timezone
from http.client import HTTPException
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urlsplit
from urllib.request import HTTPRedirectHandler, Request, build_opener

ROOT = Path(__file__).resolve().parents[1]
BEGIN = "<!-- BEGIN GENERATED PROJECTS -->"
END = "<!-- END GENERATED PROJECTS -->"
REPOSITORY = re.compile(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+\Z")
LANGUAGES = {"en": "README.md", "zh": "README_zh-CN.md"}


class FetchError(Exception):
    """A stable, publishable failure code; raw API responses are never persisted."""

    def __init__(self, status: str):
        super().__init__(status)
        self.status = status


def repository_name(value: str) -> str:
    """Accept owner/repo or a GitHub URL, including a branch-specific entry."""
    if not isinstance(value, str):
        raise TypeError("Repository must be a string")
    if value.startswith("https://"):
        parsed = urlsplit(value)
        if parsed.netloc != "github.com":
            raise ValueError(f"Not a GitHub repository: {value}")
        value = "/".join(parsed.path.strip("/").split("/")[:2])
    if not REPOSITORY.fullmatch(value) or any(
        x in {".", ".."} for x in value.split("/")
    ):
        raise ValueError(f"Invalid repository: {value}")
    return value


def localized(value: dict, field: str) -> None:
    for lang in LANGUAGES:
        text = value.get(lang)
        if not isinstance(text, str) or not text.strip() or "\n" in text:
            raise ValueError(f"{field} requires a single nonempty line in {lang}")


def load_catalog(path: Path) -> dict:
    catalog = json.loads(path.read_text(encoding="utf-8"))
    categories = catalog["categories"]
    ids = [c["id"] for c in categories]
    if not ids or len(set(ids)) != len(ids):
        raise ValueError("Category IDs must be unique and nonempty")
    for category in categories:
        localized(category["title"], "category title")
        localized(category["short_title"], "category short title")
        localized(category["anchor"], "category anchor")
    repos, anchors = set(), set()
    if not catalog["projects"]:
        raise ValueError("The catalog is empty")
    for project in catalog["projects"]:
        repo = repository_name(project["repo"])
        if repo != project["repo"] or repo.casefold() in repos:
            raise ValueError(f"Duplicate or noncanonical repository: {repo}")
        repos.add(repo.casefold())
        if repository_name(project["repository_url"]).casefold() != repo.casefold():
            raise ValueError(f"Repository link mismatch: {repo}")
        if project["category"] not in ids:
            raise ValueError(f"Unknown category: {repo}")
        for field in ("name", "author", "stack", "anchor"):
            if (
                not isinstance(project[field], str)
                or not project[field].strip()
                or "\n" in project[field]
            ):
                raise ValueError(f"Invalid {field}: {repo}")
        for anchor in project["legacy_anchors"]:
            if anchor in anchors or not re.fullmatch(r"[\w-]+", anchor):
                raise ValueError(f"Duplicate or invalid project anchor: {anchor}")
            anchors.add(anchor)
        if project["anchor"] not in project["legacy_anchors"]:
            raise ValueError(f"Missing stable project anchor: {repo}")
        localized(project["highlights"], "highlights")
        if "pick_reason" in project:
            localized(project["pick_reason"], "pick reason")
        datetime.strptime(project["added"]["date"], "%Y-%m-%d")
        if not re.fullmatch(
            r"https://github.com/miao-org/awesome-supermimic/(?:commit/[a-f0-9]{40}|pull/[1-9][0-9]*)",
            project["added"]["source"],
        ):
            raise ValueError(f"Missing catalog-addition evidence: {repo}")
        for lang in LANGUAGES:
            for link in project["links"][lang]:
                if not link["label"] or not link["url"].startswith("https://"):
                    raise ValueError(f"Invalid source link: {repo}")
    return catalog


class GitHubRedirects(HTTPRedirectHandler):
    """Follow GitHub renames without forwarding credentials to another host."""

    def redirect_request(self, req, fp, code, msg, headers, newurl):
        target = urlsplit(newurl)
        if target.scheme != "https" or target.netloc != "api.github.com":
            raise FetchError("unsafe_redirect")
        return super().redirect_request(req, fp, code, msg, headers, newurl)


def fetch_repository(repo: str, previous: dict | None, token: str | None) -> dict:
    # A stable GitHub ID survives renames and prevents a reused old name from
    # silently replacing the originally curated project.
    endpoint = (
        f"repositories/{previous['id']}"
        if previous and previous.get("id")
        else f"repos/{repo}"
    )
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "awesome-supermimic-stars",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"
    request = Request(f"https://api.github.com/{endpoint}", headers=headers)
    opener = build_opener(GitHubRedirects())
    for attempt in range(3):
        try:
            with opener.open(request, timeout=20) as response:
                payload = json.load(response)
            if not isinstance(payload, dict):
                raise ValueError("Expected a repository object")
            if payload.get("private"):
                raise FetchError("not_public")
            repo_id, stars = payload["id"], payload["stargazers_count"]
            canonical = repository_name(payload["full_name"])
            if (
                type(repo_id) is not int
                or repo_id <= 0
                or type(stars) is not int
                or stars < 0
            ):
                raise ValueError("Invalid repository ID or Stars")
            if previous and previous.get("id") and repo_id != previous["id"]:
                raise FetchError("identity_changed")
            return {"id": repo_id, "full_name": canonical, "stars": stars}
        except HTTPError as error:
            if error.code == 429 or (
                error.code == 403
                and (
                    error.headers.get("X-RateLimit-Remaining") == "0"
                    or error.headers.get("Retry-After")
                    or b"rate limit" in error.read().lower()
                )
            ):
                # Do not make another API call this run. A future scheduled/manual
                # run can retry after GitHub's reset/Retry-After window.
                retry = error.headers.get("Retry-After") or error.headers.get(
                    "X-RateLimit-Reset", "later"
                )
                print(f"GitHub rate limit: retry after {retry}", file=sys.stderr)
                raise FetchError("rate_limited") from error
            if error.code in (401, 403):
                raise FetchError("authentication_failed") from error
            if error.code == 404:
                raise FetchError("not_found") from error
            if 500 <= error.code <= 599:
                status = "server_error"
            else:
                raise FetchError(f"http_{error.code}") from error
        except (URLError, TimeoutError, OSError, HTTPException):
            status = "network_error"
        except (ValueError, KeyError, TypeError):
            raise FetchError("invalid_response") from None
        if attempt < 2:
            time.sleep(2**attempt)
    raise FetchError(status)


def validate_snapshot(snapshot: dict, projects: list[dict]) -> None:
    datetime.fromisoformat(snapshot["snapshot_at"])
    records = snapshot["repositories"]
    ids, names = set(), set()
    for project in projects:
        repo = project["repo"]
        record = records.get(repo)
        if record is None:
            raise ValueError(
                f"No valid Stars snapshot for {repo}; run an online update"
            )
        if type(record["stars"]) is not int or record["stars"] < 0:
            raise ValueError(f"Invalid cached Stars: {repo}")
        if type(record["id"]) is not int or record["id"] <= 0:
            raise ValueError(f"Invalid cached repository ID: {repo}")
        name = repository_name(record["full_name"]).casefold()
        if record["id"] in ids or name in names:
            raise ValueError("Multiple catalog entries resolve to the same repository")
        ids.add(record["id"])
        names.add(name)
    if not set(snapshot.get("failures", {})) <= {p["repo"] for p in projects}:
        raise ValueError("Snapshot failure references an unknown project")


def refresh_snapshot(
    projects: list[dict], previous: dict | None, token: str | None
) -> dict:
    records, failures = {}, {}
    cached = previous["repositories"] if previous else {}
    halted = None
    for project in projects:
        repo = project["repo"]
        if halted:
            failures[repo] = halted
            continue
        try:
            records[repo] = fetch_repository(repo, cached.get(repo), token)
        except FetchError as error:
            failures[repo] = error.status
            print(f"{repo}: {error.status}", file=sys.stderr)
            if error.status in {"rate_limited", "authentication_failed"}:
                halted = error.status
    if failures:
        # Freeze the ENTIRE previous snapshot: mixing fresh and stale numbers
        # would create an apparently current but misleading new ranking.
        if not previous:
            raise ValueError(
                "Initial fetch incomplete; no ranking or zero-Star placeholders were written"
            )
        snapshot = copy.deepcopy(previous)
        snapshot["repositories"] = {
            p["repo"]: cached[p["repo"]] for p in projects if p["repo"] in cached
        }
        snapshot["failures"] = failures
    else:
        # The timestamp identifies the last changed data snapshot, not a poll.
        # Identical values produce no daily timestamp-only commit.
        snapshot_at = (
            previous["snapshot_at"]
            if previous and records == cached
            else datetime.now(timezone.utc).isoformat(timespec="seconds")
        )
        snapshot = {"snapshot_at": snapshot_at, "repositories": records, "failures": {}}
    validate_snapshot(snapshot, projects)
    return snapshot


def ranked(projects: list[dict], snapshot: dict) -> list[dict]:
    return sorted(
        projects,
        key=lambda p: (
            -snapshot["repositories"][p["repo"]]["stars"],
            p["repo"].casefold(),
        ),
    )


def cell(text: str) -> str:
    return html.escape(text, quote=False).replace("|", "&#124;")


def badge(project: dict, snapshot: dict) -> str:
    repo = snapshot["repositories"][project["repo"]]["full_name"]
    return (
        f"[![GitHub Stars: {repo}]"
        f"(https://img.shields.io/github/stars/{repo}?style=social)]"
        f"(https://github.com/{repo}/stargazers)"
    )


def repository_url(project: dict, snapshot: dict) -> str:
    canonical = snapshot["repositories"][project["repo"]]["full_name"]
    return project["repository_url"].replace(
        "https://github.com/" + project["repo"], "https://github.com/" + canonical, 1
    )


def details_url(project: dict, lang: str) -> str:
    suffix = "_zh-CN" if lang == "zh" else ""
    return f"docs/community-projects{suffix}.md#{project['anchor']}"


def render_catalog(catalog: dict, snapshot: dict, lang: str) -> str:
    zh = lang == "zh"
    projects = ranked(catalog["projects"], snapshot)
    categories = {c["id"]: c for c in catalog["categories"]}
    lines = [
        f"**{len(projects)} 个项目 · {len(categories)} 个分类**"
        if zh
        else f"**{len(projects)} projects · {len(categories)} categories**",
        "",
        '<a id="most-starred-projects"></a>',
        "",
        "### Most Starred Projects" + (" · Stars 排行榜" if zh else ""),
        "",
    ]
    date = snapshot["snapshot_at"].replace("T", " ").replace("+00:00", " UTC")
    if zh:
        lines += [
            f"排序依据 GitHub API 快照：**{date}** · 每日按 Stars 降序更新，同分按 `owner/repo` 忽略大小写升序。徽章通过实时 Stars 接口更新（有服务缓存），可能暂时与排序快照不同。Stars 计入整个仓库（含更大框架），反映关注度，不代表基准成绩。"
        ]
    else:
        lines += [
            f"Ranked by GitHub API snapshot: **{date}** · Order refreshed daily, Stars descending, ties by case-insensitive `owner/repo`. Badges query live Stars through a cached service and may temporarily differ from the ranking snapshot. Stars cover the whole repository, including broader frameworks; they measure attention, not benchmark quality."
        ]
    if snapshot["failures"]:
        lines += [
            "",
            "> ⚠️ "
            + (
                "排序更新未完成；整份排序保留上次有效快照，徽章由实时接口独立更新。失败状态："
                if zh
                else "Ranking refresh incomplete; the entire last valid ranking snapshot is retained. Live badges update independently. Failure status: "
            ),
            "> "
            + "; ".join(
                f"`{r}`: `{s}`" for r, s in sorted(snapshot["failures"].items())
            ),
        ]
    else:
        lines += [
            "",
            (
                "排序数据状态：完整有效快照。"
                if zh
                else "Ranking data status: complete valid snapshot."
            )
            + " [Update policy](docs/star-rankings.md).",
        ]
    lines += [
        "",
        "| 排名 | 项目 | GitHub&nbsp;Stars | 分类 | 一句话亮点 |"
        if zh
        else "| Rank | Project | GitHub&nbsp;Stars | Category | Highlights |",
        "| ---: | --- | --- | --- | --- |",
    ]
    for rank, p in enumerate(projects, 1):
        cat = categories[p["category"]]
        lines.append(
            f"| {rank} | [{cell(p['name'])}]({repository_url(p, snapshot)}) | {badge(p, snapshot)} | [{cell(cat['short_title'][lang])}](#{cat['anchor'][lang]}) | {cell(p['highlights'][lang])} |"
        )
    lines += [
        "",
        '<a id="browse-by-category"></a>',
        "",
        "### Browse by Category" + (" · 分类浏览" if zh else ""),
        "",
        " · ".join(
            f"[{cell(c['short_title'][lang])} ({sum(p['category'] == c['id'] for p in projects)})](#{c['anchor'][lang]})"
            for c in categories.values()
        ),
        "",
        (
            "分类内同样按 Stars 排序；完整实验、限制与 GIF 见各项目详情。"
            if zh
            else "Each category also follows Stars order. Full experiments, limitations and GIFs live in the linked project details."
        ),
        "",
        '<a id="maintainers-picks"></a>',
        "",
        "### Maintainer’s Picks" + (" · 维护者精选" if zh else ""),
        "",
        (
            "⭐ 延续原有人工精选，理由来自已收录资料，与 Stars 排名独立。"
            if zh
            else "⭐ Retains the existing editorial selections, with reasons from the curated sources. These are independent of the Stars ranking."
        ),
        "",
        "| 项目 | 推荐理由 |" if zh else "| Project | Why read it |",
        "| --- | --- |",
    ]
    for p in catalog["projects"]:
        if "pick_reason" in p:
            lines.append(
                f"| ⭐ [{cell(p['name'])}](#{p['anchor']}) | {cell(p['pick_reason'][lang])} |"
            )
    lines += [
        "",
        '<a id="new--noteworthy"></a>',
        "",
        "### New & Noteworthy" + (" · 新收录项目" if zh else ""),
        "",
        (
            "最近五个收录条目，按本清单 Git 历史中的首次收录日期排序，同日按仓库名排序。日期链接可核查；不是项目发布日期或质量评分，不设 Stars 门槛。"
            if zh
            else "The five most recently added entries, using first inclusion dates from this list’s Git history, then repository name for same-day ties. Dates link to evidence; they are not project release dates or quality scores. No Stars threshold."
        ),
        "",
        "| 收录日期 | 项目 | 看点 |"
        if zh
        else "| Added to this list | Project | What to explore |",
        "| --- | --- | --- |",
    ]
    recent = sorted(projects, key=lambda p: p["repo"].casefold())
    recent.sort(key=lambda p: p["added"]["date"], reverse=True)
    for p in recent[:5]:
        lines.append(
            f"| [{p['added']['date']}]({p['added']['source']}) | [{cell(p['name'])}](#{p['anchor']}) | {cell(p['highlights'][lang])} |"
        )
    for cat in categories.values():
        members = [p for p in projects if p["category"] == cat["id"]]
        lines += [
            "",
            f'<a id="{cat["anchor"][lang]}"></a>',
            "",
            f"### {cat['title'][lang]} ({len(members)})",
            "",
        ]
        for p in members:
            lines += [
                *(f'<a id="{a}"></a>' for a in p["legacy_anchors"]),
                "",
                f"**[{cell(p['name'])}]({repository_url(p, snapshot)})** · {badge(p, snapshot)}"
                + (
                    " · ⭐ " + ("维护者精选" if zh else "Maintainer’s Pick")
                    if "pick_reason" in p
                    else ""
                ),
                "",
                f"**{'技术栈' if zh else 'Stack'}:** {cell(p['stack'])} · **{'作者' if zh else 'By'}:** {cell(p['author'])}<br>",
                cell(p["highlights"][lang]),
                "",
            ]
            links = [
                f"[{'仓库' if zh else 'Repository'}]({repository_url(p, snapshot)})"
            ]
            if p.get("demo"):
                links.append(f"[{'演示' if zh else 'Demo'}]({p['demo']})")
            links += [
                f"[{'实验与详情' if zh else 'Results & details'}]({details_url(p, lang)})"
            ]
            if p["links"][lang]:
                source = p["links"][lang][0]
                links += [f"[{cell(source['label'])}]({source['url']})"]
            lines += [" · ".join(links), ""]
    return "\n".join(lines).rstrip() + "\n"


def replace_generated(readme: str, generated: str) -> str:
    if readme.count(BEGIN) != 1 or readme.count(END) != 1:
        raise ValueError("README must have exactly one generated region")
    start, end = readme.index(BEGIN) + len(BEGIN), readme.index(END)
    if end < start:
        raise ValueError("Reversed generated-region markers")
    return readme[:start] + "\n\n" + generated + "\n" + readme[end:]


def update(root: Path, *, offline: bool = False, check: bool = False) -> bool:
    catalog = load_catalog(root / "data/projects.json")
    cache_path = root / "data/stars.json"
    previous = (
        json.loads(cache_path.read_text(encoding="utf-8"))
        if cache_path.exists()
        else None
    )
    if previous:
        # Validate cached records before using their IDs in API requests. New
        # catalog entries can be fetched online, but cannot be silently ranked.
        existing = [
            p for p in catalog["projects"] if p["repo"] in previous["repositories"]
        ]
        validate_snapshot(
            {
                **previous,
                "failures": {
                    r: s
                    for r, s in previous["failures"].items()
                    if r in {p["repo"] for p in existing}
                },
            },
            existing,
        )
    if offline or check:
        if previous is None:
            raise ValueError("No snapshot; run an online update first")
        snapshot = previous
    else:
        snapshot = refresh_snapshot(
            catalog["projects"], previous, os.environ.get("GITHUB_TOKEN")
        )
    validate_snapshot(snapshot, catalog["projects"])
    outputs = {cache_path: json.dumps(snapshot, ensure_ascii=False, indent=2) + "\n"}
    for lang, filename in LANGUAGES.items():
        path = root / filename
        outputs[path] = replace_generated(
            path.read_text(encoding="utf-8"), render_catalog(catalog, snapshot, lang)
        )
    changed = [
        path
        for path, content in outputs.items()
        if not path.exists() or path.read_text(encoding="utf-8") != content
    ]
    if check:
        if changed:
            raise ValueError(
                "Generated files are outdated: "
                + ", ".join(str(p.relative_to(root)) for p in changed)
            )
    else:
        for path in changed:
            path.parent.mkdir(parents=True, exist_ok=True)
            temporary = path.with_suffix(path.suffix + ".tmp")
            temporary.write_text(outputs[path], encoding="utf-8")
            temporary.replace(path)
    status = "stale snapshot retained" if snapshot["failures"] else "complete snapshot"
    print(
        f"{len(catalog['projects'])} projects; {status}; {len(changed)} changed files"
    )
    return bool(changed)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--offline",
        action="store_true",
        help="render from the saved snapshot without API calls",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="validate metadata and generated files offline, without writing",
    )
    args = parser.parse_args()
    try:
        update(ROOT, offline=args.offline, check=args.check)
    except (ValueError, KeyError, TypeError, OSError) as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
