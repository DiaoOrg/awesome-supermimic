# Contributing

We welcome public implementations, extensions, demos, datasets and learning resources directly related to SuperMimic. Check the catalog before adding a repository. Identify the original author and distinguish independent implementations, downstream ports and method extensions from the original paper.

## Add or update a project

1. Add one entry to [`data/projects.json`](data/projects.json), or update its existing entry. Use the GitHub `owner/repo` as `repo`, and preserve a branch URL in `repository_url` when necessary. One repository belongs to one category; aliases must not duplicate an existing repository.
2. Supply its public name, original author, supported stack and a short highlight in **both English and Chinese**. Use the existing categories where possible. Keep the stable `anchor` and all `legacy_anchors` when renaming an entry.
3. Set `added.date` to its first inclusion date in this list and `added.source` to the corresponding inclusion commit or PR. For a new submission, open the PR and then add its link before review. Do not use an assumed upstream release date. Do not change this date when updating results.
4. Add matching entries to [`docs/community-projects.md`](docs/community-projects.md) and [`docs/community-projects_zh-CN.md`](docs/community-projects_zh-CN.md). Keep the stable anchor, repository/branch, author, reviewed source revision and important links. Preserve the task, data, hardware, denominator and protocol for any quoted result. Mark upstream reports accurately; do not describe them as independently verified.
5. Add optional Demo, Results and Documentation links only where supported by sources. Store existing detailed link labels in `links.en` / `links.zh`. Keep long experimental accounts and GIFs in the detail pages, not the generated README cards.
6. Fetch real Stars, regenerate both READMEs and run the checks below. Do not hand-edit counts, ranking rows, category counts or the generated region. The updater validates duplicates and bilingual fields.

```bash
# With GITHUB_TOKEN supplied through your environment when available:
python3 scripts/update_stars.py
python3 -m unittest discover -s tests -v
python3 scripts/update_stars.py --check
git diff --check
```

For a text-only edit to an existing project, `python3 scripts/update_stars.py --offline` regenerates from the saved real snapshot. New projects require a successful API fetch. See [update policy and failure handling](docs/star-rankings.md). Include the catalog, affected detail pages, snapshot and both generated READMEs in your PR as applicable. Check rendered tables, relative links, old anchors and media on GitHub.

A repository returning 404 is not proof that it was never open source: it may be private, deleted or renamed. Keep the previous valid Stars on an automatic refresh. Archive/remove an unavailable entry only in an explicit editorial change, retain the record and reason in [`docs/archived-projects.md`](docs/archived-projects.md), and preserve its old README anchor with a link to the archive.

## Editorial picks and new entries

Stars rank community attention, not incompatible benchmarks. ⭐ Maintainer’s Picks highlight documented technical strengths independently of Stars. Retain complementary choices by use case; do not impose a one-project-per-category quota. To propose a pick, add a concise evidence-based `pick_reason` in both languages and cite its basis in the detail entry. Picks never override Stars ordering.

New & Noteworthy is generated from the five latest catalog addition dates, with repository names breaking same-day ties. It has no Stars threshold and does not assert upstream release dates or unverified quality ratings.

## Technical details and media

Use a level-two category heading and a level-three project heading in the detail pages. Credit the verified author or team in the first bullet. Prefer the organization’s public display name; use the owner’s account name when no separate author is documented. Include only supported links and claims; omit unpublished results rather than borrowing a baseline score. Retain implementation differences, negative results and conditions that affect interpretation.

Place a relevant preview with its source and caption in the detail entry. Prefer task demonstrations; otherwise use a labeled project screenshot, method figure or result plot. Keep report values and evaluation context intact and link the selectable source text. Use 480 pixels for motion previews and up to 720 pixels for detailed figures, preserving aspect ratio. Separate adjacent entries with a single `<br>` and blank lines.

When making a GIF from an accessible source video, retain playback speed, the original video link and attribution. An inherited baseline demo does not establish a downstream project’s results. Record the source revision and any preparation in [`assets/community/README.md`](assets/community/README.md). Omit a preview if relevant material is unavailable. Do not upload media or data without permission to redistribute.

By contributing original text or artwork, you agree to release it under this collection’s [CC0 1.0 license](LICENSE). Third-party material retains its own terms.
