"""Offline regression tests; synthetic values never enter the published snapshot."""

import copy
import json
import re
import shutil
import tempfile
import unittest
from io import BytesIO
from pathlib import Path
from unittest.mock import patch
from urllib.error import HTTPError, URLError
from urllib.request import Request

from scripts import update_stars as stars


def record(repo, count, repo_id):
    return {"id": repo_id, "full_name": repo, "stars": count}


def snapshot():
    return {
        "snapshot_at": "2026-01-01T00:00:00+00:00",
        "repositories": {
            "alice/alpha": record("alice/alpha", 5, 1),
            "bob/beta": record("bob/beta", 10, 2),
        },
        "failures": {},
    }


class FetchTests(unittest.TestCase):
    def setUp(self):
        self.opener_patch = patch.object(stars, "build_opener")
        self.open = self.opener_patch.start().return_value.open
        self.addCleanup(self.opener_patch.stop)
        self.sleep_patch = patch.object(stars.time, "sleep")
        self.sleep = self.sleep_patch.start()
        self.addCleanup(self.sleep_patch.stop)

    def response(self, **kwargs):
        data = {"id": 1, "full_name": "alice/alpha", "stargazers_count": 5}
        data.update(kwargs)
        return BytesIO(json.dumps(data).encode())

    def error(self, code, headers=None, body=b""):
        return HTTPError(
            "https://api.github.com/repos/alice/alpha",
            code,
            "failure",
            headers or {},
            BytesIO(body),
        )

    def test_real_api_fields_and_token(self):
        self.open.return_value = self.response(stargazers_count=0)
        self.assertEqual(
            stars.fetch_repository("alice/alpha", None, "test-token"),
            record("alice/alpha", 0, 1),
        )
        request = self.open.call_args.args[0]
        self.assertEqual(request.full_url, "https://api.github.com/repos/alice/alpha")
        self.assertEqual(request.get_header("Authorization"), "Bearer test-token")
        self.assertEqual(self.open.call_args.kwargs["timeout"], 20)

    def test_cached_id_survives_rename(self):
        self.open.return_value = self.response(full_name="new-owner/new-name")
        result = stars.fetch_repository(
            "alice/alpha", record("alice/alpha", 5, 1), None
        )
        self.assertEqual(result["full_name"], "new-owner/new-name")
        self.assertEqual(
            self.open.call_args.args[0].full_url,
            "https://api.github.com/repositories/1",
        )

    def test_private_repository_is_not_published_with_a_privileged_token(self):
        self.open.return_value = self.response(private=True)
        with self.assertRaisesRegex(stars.FetchError, "not_public"):
            stars.fetch_repository("alice/alpha", None, "test-token")

    def test_identity_change_is_rejected(self):
        self.open.return_value = self.response(id=99)
        with self.assertRaisesRegex(stars.FetchError, "identity_changed"):
            stars.fetch_repository("alice/alpha", record("alice/alpha", 5, 1), None)

    def test_404_is_not_zero(self):
        self.open.side_effect = self.error(404)
        with self.assertRaisesRegex(stars.FetchError, "not_found"):
            stars.fetch_repository("alice/alpha", None, None)
        self.assertEqual(self.open.call_count, 1)

    def test_rate_limits_stop_without_retrying_early(self):
        for code, headers, body in [
            (429, {"Retry-After": "120"}, b""),
            (403, {"X-RateLimit-Remaining": "0"}, b""),
            (403, {}, b'{"message":"secondary rate limit"}'),
        ]:
            with self.subTest(code=code, headers=headers):
                self.open.reset_mock()
                self.open.side_effect = self.error(code, headers, body)
                with self.assertRaisesRegex(stars.FetchError, "rate_limited"):
                    stars.fetch_repository("alice/alpha", None, None)
                self.assertEqual(self.open.call_count, 1)
                self.sleep.assert_not_called()

    def test_permission_errors(self):
        for code in (401, 403):
            self.open.side_effect = self.error(code)
            with self.assertRaisesRegex(stars.FetchError, "authentication_failed"):
                stars.fetch_repository("alice/alpha", None, None)

    def test_transient_network_failure_recovers(self):
        self.open.side_effect = [URLError("offline"), self.response()]
        self.assertEqual(stars.fetch_repository("alice/alpha", None, None)["stars"], 5)
        self.sleep.assert_called_once_with(1)

    def test_retries_are_bounded(self):
        for error, status in [
            (URLError("offline"), "network_error"),
            (TimeoutError(), "network_error"),
            (self.error(503), "server_error"),
        ]:
            with self.subTest(status=status):
                self.open.reset_mock()
                self.open.side_effect = error
                with self.assertRaisesRegex(stars.FetchError, status):
                    stars.fetch_repository("alice/alpha", None, None)
                self.assertEqual(self.open.call_count, 3)

    def test_malformed_payloads_are_rejected(self):
        for payload in [
            b"not json",
            b"[]",
            b"{}",
            b'{"id":1,"full_name":"alice/alpha","stargazers_count":true}',
            b'{"id":1,"full_name":"alice/alpha","stargazers_count":-1}',
        ]:
            self.open.return_value = BytesIO(payload)
            with self.assertRaisesRegex(stars.FetchError, "invalid_response"):
                stars.fetch_repository("alice/alpha", None, None)

    def test_redirects_stay_on_github_api(self):
        redirect = stars.GitHubRedirects()
        request = Request(
            "https://api.github.com/repos/alice/alpha",
            headers={"Authorization": "Bearer test"},
        )
        renamed = redirect.redirect_request(
            request, None, 301, "", {}, "https://api.github.com/repositories/1"
        )
        self.assertEqual(renamed.full_url, "https://api.github.com/repositories/1")
        for target in [
            "https://example.org/steal",
            "http://api.github.com/repositories/1",
        ]:
            with self.assertRaisesRegex(stars.FetchError, "unsafe_redirect"):
                redirect.redirect_request(request, None, 301, "", {}, target)


class SnapshotTests(unittest.TestCase):
    def setUp(self):
        self.previous = snapshot()
        self.projects = [{"repo": repo} for repo in self.previous["repositories"]]

    @patch.object(stars, "fetch_repository")
    def test_partial_failure_freezes_every_value(self, fetch):
        fetch.side_effect = [
            record("alice/alpha", 999, 1),
            stars.FetchError("not_found"),
        ]
        result = stars.refresh_snapshot(self.projects, self.previous, None)
        self.assertEqual(result["repositories"], self.previous["repositories"])
        self.assertEqual(result["snapshot_at"], self.previous["snapshot_at"])
        self.assertEqual(result["failures"], {"bob/beta": "not_found"})
        self.assertEqual(self.previous, snapshot())

    @patch.object(stars, "fetch_repository")
    def test_initial_failure_writes_no_fake_ranking(self, fetch):
        fetch.side_effect = stars.FetchError("not_found")
        with self.assertRaisesRegex(ValueError, "Initial fetch incomplete"):
            stars.refresh_snapshot(self.projects, None, None)

    @patch.object(stars, "fetch_repository")
    def test_rate_limit_stops_remaining_requests(self, fetch):
        fetch.side_effect = stars.FetchError("rate_limited")
        result = stars.refresh_snapshot(self.projects, self.previous, None)
        fetch.assert_called_once()
        self.assertEqual(set(result["failures"]), {"alice/alpha", "bob/beta"})

    @patch.object(stars, "fetch_repository")
    def test_unchanged_poll_does_not_change_timestamp(self, fetch):
        fetch.side_effect = list(self.previous["repositories"].values())
        self.assertEqual(
            stars.refresh_snapshot(self.projects, self.previous, None), self.previous
        )

    @patch.object(stars, "fetch_repository")
    def test_recovery_clears_failure_and_accepts_new_values(self, fetch):
        self.previous["failures"] = {"bob/beta": "not_found"}
        fetch.side_effect = [record("alice/alpha", 20, 1), record("bob/beta", 8, 2)]
        result = stars.refresh_snapshot(self.projects, self.previous, None)
        self.assertFalse(result["failures"])
        self.assertEqual(result["repositories"]["alice/alpha"]["stars"], 20)
        self.assertNotEqual(result["snapshot_at"], self.previous["snapshot_at"])

    @patch.object(stars, "fetch_repository")
    def test_repeated_failure_is_stable(self, fetch):
        fetch.side_effect = stars.FetchError("network_error")
        first = stars.refresh_snapshot(self.projects, self.previous, None)
        second = stars.refresh_snapshot(self.projects, first, None)
        self.assertEqual(first, second)

    @patch.object(stars, "fetch_repository")
    def test_new_repository_without_cache_fails_closed(self, fetch):
        self.projects.append({"repo": "charlie/new"})
        fetch.side_effect = [
            *self.previous["repositories"].values(),
            stars.FetchError("not_found"),
        ]
        with self.assertRaisesRegex(ValueError, "No valid Stars snapshot"):
            stars.refresh_snapshot(self.projects, self.previous, None)

    def test_stable_tie_order_is_case_insensitive(self):
        projects = [{"repo": r} for r in ["z/z", "Beta/b", "alpha/a"]]
        data = {"repositories": {p["repo"]: {"stars": 5} for p in projects}}
        self.assertEqual(
            [p["repo"] for p in stars.ranked(projects, data)],
            ["alpha/a", "Beta/b", "z/z"],
        )
        self.assertEqual(
            stars.ranked(projects, data), stars.ranked(list(reversed(projects)), data)
        )

    def test_two_names_cannot_resolve_to_one_repository(self):
        self.previous["repositories"]["bob/beta"] = self.previous["repositories"][
            "alice/alpha"
        ]
        with self.assertRaisesRegex(ValueError, "same repository"):
            stars.validate_snapshot(self.previous, self.projects)


class CatalogTests(unittest.TestCase):
    def setUp(self):
        self.catalog = stars.load_catalog(stars.ROOT / "data/projects.json")
        self.snapshot = json.loads((stars.ROOT / "data/stars.json").read_text())

    def test_repository_parsing(self):
        for value in [
            "alice/repo",
            "https://github.com/alice/repo",
            "https://github.com/alice/repo/tree/topic",
        ]:
            self.assertEqual(stars.repository_name(value), "alice/repo")
        for value in ["alice", "https://example.com/alice/repo", "a/../b", "../repo"]:
            with self.assertRaises(ValueError):
                stars.repository_name(value)

    def test_duplicate_repositories_and_missing_translations_rejected(self):
        for kind in ("duplicate", "translation", "link"):
            data = copy.deepcopy(self.catalog)
            if kind == "duplicate":
                duplicate = copy.deepcopy(data["projects"][0])
                duplicate["repo"] = duplicate["repo"].upper()
                data["projects"].append(duplicate)
            elif kind == "translation":
                del data["projects"][0]["highlights"]["zh"]
            else:
                data["projects"][0]["repository_url"] = "https://github.com/wrong/repo"
            with tempfile.TemporaryDirectory() as tmp:
                path = Path(tmp) / "projects.json"
                path.write_text(json.dumps(data))
                with self.assertRaises(ValueError):
                    stars.load_catalog(path)

    def test_every_detail_project_is_in_catalog(self):
        expected = {p["repo"].casefold() for p in self.catalog["projects"]}
        for filename, label in [
            ("community-projects.md", "Repository"),
            ("community-projects_zh-CN.md", "仓库"),
        ]:
            text = (stars.ROOT / "docs" / filename).read_text()
            repos = [
                stars.repository_name(url).casefold()
                for url in re.findall(r"^\[" + label + r"\]\(([^)]+)\)", text, re.M)
            ]
            self.assertEqual(set(repos), expected)
            self.assertEqual(len(repos), len(expected))

    def test_catalog_detail_anchors_resolve(self):
        for filename in ["community-projects.md", "community-projects_zh-CN.md"]:
            text = (stars.ROOT / "docs" / filename).read_text()
            anchors = set(re.findall(r'<a (?:id|name)="([^"]+)"', text))
            for title in re.findall(r"^#{1,6} (.+)$", text, re.M):
                anchors.add(re.sub(r"[^\w\- ]", "", title.lower()).replace(" ", "-"))
            for project in self.catalog["projects"]:
                self.assertIn(project["anchor"], anchors, (filename, project["name"]))

    def test_rankings_badges_and_category_order_match_in_both_languages(self):
        ordered = stars.ranked(self.catalog["projects"], self.snapshot)
        expected = [
            self.snapshot["repositories"][p["repo"]]["full_name"] for p in ordered
        ]
        for lang in stars.LANGUAGES:
            text = stars.render_catalog(self.catalog, self.snapshot, lang)
            ranking = text.split('<a id="browse-by-category">')[0]
            rows = re.findall(r"^\| (\d+) \| (.*)$", ranking, re.M)
            self.assertEqual(
                [int(n) for n, _ in rows], list(range(1, len(expected) + 1))
            )
            self.assertEqual(
                re.findall(r"\]\(https://github.com/([^)]*)/stargazers\)", ranking),
                expected,
            )
            for p in ordered:
                record = self.snapshot["repositories"][p["repo"]]
                self.assertIn(
                    f"/badge/stars-{record['stars']}-blue?",
                    stars.badge(p, self.snapshot),
                )
                self.assertIn(
                    f"https://github.com/{record['full_name']}/stargazers",
                    stars.badge(p, self.snapshot),
                )
            for cat in self.catalog["categories"]:
                section = text.split(f'<a id="{cat["anchor"][lang]}"></a>')[1].split(
                    "\n### ", 1
                )[1]
                members = [p for p in ordered if p["category"] == cat["id"]]
                positions = [section.index(f'<a id="{p["anchor"]}">') for p in members]
                self.assertEqual(positions, sorted(positions))
                self.assertIn(f"({len(members)})", section.splitlines()[0])

    def test_rename_preserves_branch_link(self):
        project = next(
            p for p in self.catalog["projects"] if "/tree/" in p["repository_url"]
        )
        self.snapshot["repositories"][project["repo"]]["full_name"] = "new/renamed"
        self.assertEqual(
            stars.repository_url(project, self.snapshot),
            "https://github.com/new/renamed/tree/supermimic",
        )

    def test_html_and_table_content_is_escaped(self):
        self.assertEqual(stars.cell("a | <tag> & b"), "a &#124; &lt;tag&gt; &amp; b")

    def test_render_preserves_manual_regions(self):
        readme = (
            "Hand-written intro\n"
            + stars.BEGIN
            + "\nold\n"
            + stars.END
            + "\nHand-written science\n"
        )
        result = stars.replace_generated(readme, "new\n")
        self.assertTrue(result.startswith("Hand-written intro\n"))
        self.assertTrue(result.endswith("\nHand-written science\n"))
        for invalid in ["no markers", stars.END + stars.BEGIN, readme + stars.BEGIN]:
            with self.assertRaises(ValueError):
                stars.replace_generated(invalid, "new")

    def test_all_legacy_anchors_and_authors_rendered(self):
        for lang in stars.LANGUAGES:
            rendered = stars.render_catalog(self.catalog, self.snapshot, lang)
            for project in self.catalog["projects"]:
                for anchor in project["legacy_anchors"]:
                    self.assertIn(f'<a id="{anchor}"></a>', rendered)
                self.assertIn(stars.cell(project["author"]), rendered)

    def test_offline_regeneration_is_idempotent(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "data").mkdir()
            for filename in [
                "data/projects.json",
                "data/stars.json",
                "README.md",
                "README_zh-CN.md",
            ]:
                shutil.copy(stars.ROOT / filename, root / filename)
            before = {p: p.read_bytes() for p in root.rglob("*") if p.is_file()}
            self.assertFalse(stars.update(root, offline=True))
            self.assertFalse(stars.update(root, offline=True))
            self.assertFalse(stars.update(root, check=True))
            self.assertEqual(before, {p: p.read_bytes() for p in before})

    def test_invalid_readme_does_not_partially_write_snapshot(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "data").mkdir()
            for filename in [
                "data/projects.json",
                "data/stars.json",
                "README.md",
                "README_zh-CN.md",
            ]:
                shutil.copy(stars.ROOT / filename, root / filename)
            (root / "README_zh-CN.md").write_text("broken markers")
            before = (root / "data/stars.json").read_bytes()
            with patch.object(
                stars,
                "refresh_snapshot",
                return_value={
                    **self.snapshot,
                    "snapshot_at": "2027-01-01T00:00:00+00:00",
                },
            ):
                with self.assertRaisesRegex(ValueError, "generated region"):
                    stars.update(root)
            self.assertEqual((root / "data/stars.json").read_bytes(), before)


if __name__ == "__main__":
    unittest.main()
