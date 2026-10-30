# Contributing

We welcome implementations, extensions, demos, datasets, and learning resources that directly relate to SuperMimic.

1. Check the existing entries before adding a resource.
2. Link the original repository or publication and identify the author or maintainer. Use an explicit branch URL when the work lives outside the default branch.
3. Explain what the project does and how it relates to the original SuperMimic paper. Distinguish an official release, independent implementation, downstream port, and method extension.
4. For reported results, cite a source and retain the task, dataset size, hardware, metric, and evaluation conditions. Label upstream reports and independent measurements accurately.
5. Attribute previews to their source. Do not upload media or data you do not have permission to redistribute.
6. Update both [English](README.md) and [Chinese](README_zh-CN.md) entries, including the checked date and source snapshot when applicable.
7. Check links, anchors, table rendering, and media loading; run `git diff --check` before submitting a pull request.

Keep descriptions concise. This collection organizes resources; it does not rank incompatible benchmarks or imply endorsement by the original authors.

## Suggested entry

```markdown
### Project name

[Repository](https://github.com/OWNER/REPO) · [Setup](https://github.com/OWNER/REPO/blob/COMMIT/README.md#setup) · [Results](https://github.com/OWNER/REPO/blob/COMMIT/README.md#results)

- **By Author / Organization.** Explain the main contribution, its relationship to SuperMimic, and the framework and robot it uses.
- **Upstream report:** Summarize a published result with its task, metric, denominator and relevant training/evaluation conditions.
- **Useful context:** Explain any branch requirement, implementation difference or limitation that affects interpretation or use. [Source snapshot](https://github.com/OWNER/REPO/blob/COMMIT/README.md).
```

Add the entry to the appropriate topic. Topics use level-two headings with a short scope description; projects use level-three headings, followed by a compact row of relevant links and two or three bullets. Update the topic count in the navigation when adding a project. Credit the verified author or team in the first bullet, together with what they built. Prefer the organization's public display name; use the repository owner's account name when no separate author name is documented.

Include only links and bullets supported by the source. Omit the result bullet when no relevant result is published; a useful description of released tools or current progress can take its place. Do not fill missing results with inherited baseline scores, imply that demonstrations establish general performance, or force every entry into the same number of bullets. Link to the reviewed source revision for factual claims.

Place a visual preview immediately below the description, with a link to its source and a concise caption. Prefer a task demo; otherwise use a project screenshot, method figure or result plot. If only a written report is available, a legible screenshot of its relevant table can serve as a preview. Label report screenshots and excerpts explicitly, preserve their values and evaluation context, and keep a link to selectable source text. Use 480 pixels for motion previews and up to 720 pixels for detailed figures or tables, preserving the original aspect ratio; GitHub scales them down on narrow screens.

When a project publishes an accessible video without an animated preview, convert a representative clip into a GIF instead of leaving only a video link. Preserve playback speed and keep the original video link. If the video is inaccessible, use a relevant static preview and retain the video entry point. Confirm that the media demonstrates the listed work; inherited baseline demos or unrelated experiments do not establish its results. Record the source revision, any excerpt and screenshot preparation in `assets/community/README.md`. Omit a preview if no relevant source material is available.

Separate adjacent projects with a single `<br>` after the description or demo caption, with blank lines on both sides. Reserve heading underlines for topic boundaries; do not repeat horizontal rules between projects.

By contributing original text or artwork, you agree to release that contribution under this collection's [CC0 1.0 license](LICENSE). Third-party material retains its own terms.

## Suggested starting points

The community-project guide highlights distinct strengths by use case, not a performance ranking. Do not impose a one-project-per-category quota: include complementary approaches (for example, arm manipulation, dexterous-hand tasks and controlled method comparisons) when each has a documented reason to read it. Pair each linked project with its own short reason in the guide. Prefix recommended headings with ⭐ without pinning them above other projects. Sort all entries within each category, and recommended picks within each guide row, by descending repository-wide GitHub Stars; break ties by owner/repository name and place unavailable counts last. Refresh both languages together and record the sorting snapshot date in the guide; dynamic badges update independently of the Markdown order. Keep recommendations separate from popularity and retain the previous heading anchor with an explicit HTML anchor so existing links keep working. Keep the guide, category counts and selections aligned in both languages, and summarize only evidence already linked in the entry.
