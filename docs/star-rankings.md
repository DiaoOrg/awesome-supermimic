# Maintaining the Stars rankings

Both READMEs use one catalog, [`data/projects.json`](../data/projects.json), and one real GitHub REST API snapshot, [`data/stars.json`](../data/stars.json). Edit technical summaries and selections in the catalog; edit full experimental records in the bilingual [project details](community-projects.md). The updater changes only the marked `BEGIN/END GENERATED PROJECTS` region in each README, the Stars snapshot and generated SVG badges in `assets/stars/`. It never edits the catalog, technical detail pages, official introduction or footer.

## Update and check

Python 3.10+ and its standard library are sufficient; there are no third-party Python dependencies.

```bash
# GITHUB_TOKEN is optional for public repositories, recommended for API limits.
# Supply it through your shell's secret mechanism, never in a committed file.
python3 scripts/update_stars.py

# Rebuild from the saved real snapshot without API calls.
python3 scripts/update_stars.py --offline

# Validate metadata and both generated regions without writing or API calls.
python3 scripts/update_stars.py --check
python3 -m unittest discover -s tests -v
git diff --check
```

## Ranking and evidence

- Every active project appears in the full ranking and exactly one category. Both use descending `stargazers_count`, then case-insensitive catalog `owner/repo` ascending. A tie receives a distinct position under this documented ordering.
- Badges are **locally generated SVG snapshots** of the fetched count, linked to the corresponding repository’s stargazers. They use a familiar badge style, with a gold star and a blue count. Keeping these small images in `assets/stars/` avoids third-party Shields image failures and keeps visible numbers consistent with ordering. A dynamic badge alone cannot sort Markdown.
- The snapshot stores the numeric repository ID, canonical GitHub name and Stars. After the initial request to `/repos/{owner}/{repo}`, subsequent requests use `/repositories/{id}` so renames/transfers work even if the old name is reused. Branch-specific repository links remain branch-specific. Reviewed source-revision links are retained as authored.
- Stars count the entire repository, which can include a larger framework. They measure attention, not reproduction fidelity, benchmark performance or independent verification.
- ⭐ Maintainer’s Picks retain the existing editorial choices and individually sourced reasons. They do not move projects ahead of higher-Star entries.
- New & Noteworthy shows the five latest **additions to this catalog**, irrespective of Stars. Dates link to the inclusion commit or PR; same-day ties use repository name. These are not upstream release dates or claims of project quality.
- `snapshot_at` identifies the fetched snapshot when its values last changed. It is not a last-poll timestamp. Unchanged daily polls leave all tracked files byte-identical; the latest attempt time is available in the [Actions runs](https://github.com/miao-org/awesome-supermimic/actions/workflows/update-stars.yml).

## Failure policy

A refresh must fetch every active repository successfully before changing **any** Stars value or ranking. On 404, network failure, malformed responses or identity changes, all previous numeric values are preserved together and a visible bilingual warning lists the failures. No failure is converted into zero Stars. Recovery clears the warning and accepts a complete new snapshot.

Without a valid previous value for every catalog entry (initial setup or an unavailable newly added project), the updater fails before writing any file. Resolve the source or explicitly archive/remove the entry in an editorial change, then retry. The updater never automatically removes projects.

Network errors and HTTP 5xx responses get at most three attempts with bounded backoff and a 20-second request timeout. Authentication failures and primary/secondary rate limits stop further API calls for the run; rate-limit reset/Retry-After information is printed, and retry is deferred to a future scheduled or manual run. Redirects must stay on `https://api.github.com`; access tokens and raw error bodies are never written to tracked data. Duplicate canonical names or repository IDs fail validation before writing.

The same failure repeated on later days creates no timestamp-only commit. A changed failure status or recovery can produce a commit because it changes what readers should know.

## GitHub Actions

[The workflow](../.github/workflows/update-stars.yml) validates pull requests and pushes to `main` with `contents: read` and no persisted checkout credentials. The scheduled/manual refresh job has only `contents: write`, uses `GITHUB_TOKEN`, and can mutate only the default branch. No PAT, pull-request write permission or `pull_request_target` event is needed.

The daily schedule is **03:23 UTC / 11:23 Asia/Shanghai**. `workflow_dispatch` is also available after this workflow reaches the default branch. Concurrency serializes runs for the same ref; cancellation is disabled. Only `data/stars.json`, `assets/stars/`, `README.md` and `README_zh-CN.md` are staged, and no commit is made when these files are unchanged. A concurrent human push or branch rule that prevents direct bot commits causes a normal push failure; the workflow never force-pushes or changes protection rules. In that case, a maintainer can run the same update locally and submit the result through the repository’s permitted PR process.

## 中文说明

- `data/projects.json` 是中英文共用的人工项目索引；`data/stars.json` 只保存真实 GitHub API 数值与状态。自动化仅修改 README 指定生成区域、Stars 数据和 `assets/stars/` 的 SVG 徽章，不覆盖人工技术详情。
- 全榜与分类内均按 Stars 降序，同分按索引中的 `owner/repo` 忽略大小写升序。Badge 使用同一份快照生成仓库内 SVG，避免显示数值与排序不一致，也不依赖第三方图片服务。
- 任一已有项目查询失败，整份数值排名冻结在上次有效快照，并显示失败原因；不会将失败值写成 0。首次初始化或新项目没有历史有效数据时，停止写入。归档/移除项目需要人工决定，不由脚本自动执行。
- 首次用仓库路径查询，此后用 GitHub 数字 ID 跟随改名或转移；分支入口和原有核查版本链接保留。限流后停止本轮请求，网络与服务端错误进行有上限的重试。
- 每日北京时间 11:23 运行，也支持手动触发。`snapshot_at` 表示数值快照变化时刻，不是每天的检查时间；数值与状态未变则不提交。最新尝试时间见 Actions。
- “维护者精选”与 Stars 排名分开；“新收录项目”使用本清单首次收录日期和证据链接，不冒充项目发布日期或质量评价。
- 添加或修改项目按 [贡献指南](../CONTRIBUTING.md) 操作，然后运行上面的检查命令。单元测试使用的虚构数值只存在于测试，绝不用于正式排行榜。
