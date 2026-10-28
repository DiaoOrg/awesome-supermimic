# Community media credits

## SuperMimic Mjlab performance figure

Checked on **2026-10-27**, source revision **`23c76cad5bf41110709c7f929b54c1da1be6b248`**.

- **Source / maintainer:** [Breezewrf / supermimic_mjlab](https://github.com/Breezewrf/supermimic_mjlab).
- **Original preview:** [doc/assets/evaluation.png](https://github.com/Breezewrf/supermimic_mjlab/blob/23c76cad5bf41110709c7f929b54c1da1be6b248/doc/assets/evaluation.png). Embedded directly from the pinned source at a display width of 720 pixels, preserving aspect ratio; no copy, excerpt, screenshot preparation or re-encoding.
- **Context:** The figure is the upstream evaluation dashboard showing normalized return, successful motion count, success rate, per-motion return/completion and environment steps. It shows the selected training run; the separate configuration ablation table in the source README reports the progression from input normalization through the orientation anchor, world-model normalization and corrected learning-rate schedule. These are upstream reports, not independent measurements by this collection.

Rights in the original footage remain with its authors; it is excluded from this collection's CC0 dedication.

## ScaleBFM_Plus animated preview

Checked on **2026-10-27**, source revision **`65e4d524bd31fdc4284ba8c6e624fb0b0127da03`**.

- **Source / maintainer:** [Hxxxz0 / ScaleBFM_Plus](https://github.com/Hxxxz0/ScaleBFM_Plus), a community extension of [ScaleBFM](https://github.com/zengweishuai/ScaleBFM).
- **Original preview:** [ScaleTrack/assets/demos/supermimic_vs_official.gif](https://github.com/Hxxxz0/ScaleBFM_Plus/blob/65e4d524bd31fdc4284ba8c6e624fb0b0127da03/ScaleTrack/assets/demos/supermimic_vs_official.gif). Embedded directly through GitHub's LFS media endpoint at a display width of 480 pixels, preserving aspect ratio; no copy, excerpt, screenshot preparation, or re-encoding.
- **Context:** The [source README](https://github.com/Hxxxz0/ScaleBFM_Plus/blob/65e4d524bd31fdc4284ba8c6e624fb0b0127da03/ScaleTrack/README.md#fast-training-with-a-learned-world-model-supermimic) identifies the left policy as official ScaleBFM-M and the right as SuperMimic, tracking an unseen LAFAN dance with the same simulator, motion, seed and camera. This is an upstream simulation demonstration, not an independent evaluation or a real-robot result.

Rights in the original footage remain with its authors; it is excluded from this collection's CC0 dedication.

## In-Hand Rotation mjlab animated preview

Checked on **2026-10-28**, source revision **`0ab03eb2244b4a1a020d94ef38a4823bb9e15ba0`**.

- **Source / maintainer:** [Msornerrrr / in-hand-rotation-mjlab](https://github.com/Msornerrrr/in-hand-rotation-mjlab).
- **Original preview:** [assets/sim_fingertip.gif](https://github.com/Msornerrrr/in-hand-rotation-mjlab/blob/0ab03eb2244b4a1a020d94ef38a4823bb9e15ba0/assets/sim_fingertip.gif). Embedded directly from the pinned source at a display width of 480 pixels, preserving aspect ratio; no copy, excerpt, screenshot preparation or re-encoding.
- **Context:** A simulated rollout of the repository's joints-only world-model policy turning four of its 22 objects (sphere, cube, cylinder, cuboid) palm down at pad friction 0.35; each panel shows a view from below and one up the palm normal. This is an upstream simulation demonstration, not an independent evaluation or a real-robot result.

Rights in the original footage remain with its authors; it is excluded from this collection's CC0 dedication.

## Video previews

These GIFs show demonstrations published by the linked projects. They are converted from the original videos; this collection did not run the experiments.

| Preview | Authors / source project | Original video | Duration |
| --- | --- | --- | --- |
| [morphmimic.gif](morphmimic.gif) | [Lizhi Yang and the MorphMimic authors](https://github.com/lzyang2000/morphmimic) | [MP4](https://lzyang2000.github.io/morphmimic/static/videos/dance_hiphop_shuffle_sequence_v_001_R_003__A306.mp4) | 20.02 s |
| [backflip.gif](backflip.gif) | [liudi159](https://github.com/liudi159/supermimic-backflip-5090) | [MP4](https://raw.githubusercontent.com/liudi159/supermimic-backflip-5090/5b313d75e804cdd2ff1ce9bdcfa899a98eca856b/media/v14_blue_checker.mp4) | 11.44 s |
| [flatworld.gif](flatworld.gif) | [swaggyliu](https://github.com/swaggyliu/FlatWorld) | [MP4](https://raw.githubusercontent.com/swaggyliu/FlatWorld/207e9e9c61ef21b8f145c3e0c4d8b121a03bf45a/supermimic2d/runs/lafan2d/showcase_30s.mp4) | 31.60 s |

Retrieved on 2026-10-26. Each preview preserves the complete selected clip, its framing, frame order and original playback speed. They are scaled to 480 × 270, sampled at 12 fps and quantized to 128 colors, with no added borders, motion interpolation or generated content. GIF timing is rounded to centiseconds.

- **MorphMimic:** the project website’s street-shuffle demonstration of G1, X2 Ultra and T2 using one shared policy; this is the complete 20.02-second clip, not the longer project film.
- **Backflip:** the final V14 policy rollout. The project reports a failed strict evaluation due to non-foot contact; the GIF is not evidence of passing that evaluation.
- **FlatWorld:** the complete upstream 2D motion-tracking showcase.

All rights in the source footage remain with the original authors. These third-party previews are excluded from this collection’s CC0 dedication. Refer to the linked projects for their terms; this collection does not grant new rights to the footage.

Conversion uses FFmpeg:

```sh
ffmpeg -i source.mp4 -filter_complex \
  "fps=12,scale=480:-1:flags=lanczos,setsar=1,split[a][b];[a]palettegen=max_colors=128[p];[b][p]paletteuse=dither=bayer:bayer_scale=4" \
  -loop 0 preview.gif
```

## Static previews

The following previews were checked on 2026-10-26. Each links to a pinned source revision. They show the authors' figures or documented results; this collection did not run the experiments.

### Original project images

These images are embedded directly from their source repositories, without editing. Click a preview in the README for the full-size source.

| Project | Image and source | What it shows |
| --- | --- | --- |
| [InstinctMJ · SuperMimic](https://github.com/project-instinct/InstinctMJ) | [world_model_simple.png](https://github.com/project-instinct/InstinctMJ/blob/7ca851e002980011f24a1664011305d0ba94aefc/src/instinct_mj/rl/supermimic/assets/world_model_simple.png) | Method diagram · robot-state and visual-latent prediction |
| [SuperMimic-perceptive](https://github.com/mode1223345/SuperMimic-perceptive) | [Curves.png](https://github.com/mode1223345/SuperMimic-perceptive/blob/3d38bacbaf5bee7e782bdada6a6da678264d0bfa/results/Curves.png) | Training curves · 2026-10-24 snapshot; control comparisons in progress |
| [Dex SuperMimic](https://github.com/CumulusAlpha/Dex-Supermimic) | [teaser.jpg](https://github.com/CumulusAlpha/Dex-Supermimic/blob/5ca57628af3666a9b2878c00f461f43d6edb5b61/teaser.jpg) | Simulation screenshot · Wuji Hand 2 cube reorientation |

### Source-table screenshots

The eight PNGs below preserve the selected upstream table content. The tables were rendered locally with a dark theme and wrapped cells for legibility, without GitHub navigation. Text and values were not rewritten; the two excerpts are identified below. These are report or code-index screenshots, not simulation frames or new measurements. The original sources remain available as selectable text.

| Screenshot | Pinned source | Selection |
| --- | --- | --- |
| [reproduced-results.png](reproduced-results.png) | [SuperMimic-Reproduced](https://github.com/CuboiLeo/SuperMimic-Reproduced/blob/d9be385b3eeb13a638fb33fb200d3bfd9be9839f/README.md) | Complete experiment summary, including the separate observation settings and BONES-SEED subset evaluation. |
| [vibe-results.png](vibe-results.png) | [supermimic_vibe](https://github.com/dhmbb2/supermimic_vibe/blob/072f0910dadc9d95c720e625b546120e9ce917c9/README.md) | Complete reproduction-status table, including partial, pending, blocked and out-of-scope items. |
| [locomujoco-results.png](locomujoco-results.png) | [SuperMimic on LocoMuJoCo](https://github.com/Alchedata/supermimic-locomujoco/blob/cc1375d48a38bde062d088ffd132122e0cd7b7da/README.md) | Complete Results at 5k table, including the failed seed and recovery branches. |
| [rethinking-comparison.png](rethinking-comparison.png) | [Rethinking SuperMimic](https://github.com/btx0424/rethinking-supermimic/blob/ecdaeb6a916a16cf7eb69b19226c17be31a6bc27/README.md) | Excerpt: header and first three rows — dynamics state, MLP details and world-model loss. |
| [pera-tracking-results.png](pera-tracking-results.png) | [SuperMimic-PERA](https://github.com/shangchaohu718/supermimic-pera/blob/0e89e55187a800341e609129b5d5200a607a467c/README.md) | Complete tracking-checkpoint table. This is the tracker baseline, not the separate skateboarding result. |
| [contact-bptt-results.png](contact-bptt-results.png) | [Ref2Dex · Dex Contact MBRL](https://github.com/hitsz-oyx/Ref2Dex-agent/blob/31cdb9ac759838b83d62bbc0addfd5cf28f3dff4/src/task/dex-contact-mbrl/docs/CONTACT-REFINEMENT-RESULTS-20261026.md) | Complete three-arm native-physics comparison. Higher reference survival accompanies lower mean return. |
| [g05-steering-entry.png](g05-steering-entry.png) | [G0.5 · SuperMimic-style Steering](https://github.com/azizkhadraoui/g05/blob/e3de0de50db7d90068483e2d30f2eacd781300b4/README.md) | Excerpt: code-index header and Noise policies row identifying the SuperMimic-style scripts; not a rollout. |
| [mujoco-evaluation.png](mujoco-evaluation.png) | [SuperMimic-MuJoCo](https://github.com/panhainan2020/SuperMimic-MuJoCo/blob/db045afa9c52458f213e2c66037387e9c109a03a/README.md) | Complete evaluation summary. The external video cover returned HTTP 403 when checked; the README retains the gallery link. |

All rights in the original figures, text and data remain with their respective authors. These third-party previews are excluded from this collection's CC0 dedication; consult the linked sources for their terms. InstinctMJ's source is licensed CC BY-NC 4.0.
