<div align="center">

# Awesome SuperMimic

[![Awesome](https://awesome.re/badge.svg)](https://github.com/sindresorhus/awesome) [![Paper](https://img.shields.io/badge/arXiv-2610.28480-b31b1b.svg)](https://arxiv.org/abs/2610.28480) [![License: CC0](https://img.shields.io/badge/License-CC0_1.0-blue.svg)](LICENSE) [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

**A curated collection of SuperMimic implementations, extensions, demos, and resources.**

English · [简体中文](README_zh-CN.md)

[Original paper](https://arxiv.org/abs/2610.28480) · [Official website](https://supermimic.github.io/) · [Interactive demo](https://supermimic.github.io/demo/) · [Community projects](#community-projects)

</div>

Find community implementations by GitHub Stars, task and framework. Stars measure repository attention; ⭐ maintainer picks highlight documented technical strengths. Results are upstream reports, not independently rerun here.

<a id="contents"></a>

[Rankings](#most-starred-projects) · [Categories](#browse-by-category) · [Maintainer’s picks](#maintainers-picks) · [New & noteworthy](#new--noteworthy) · [Original work](#original-supermimic) · [Contributing](#contributing)

## Community projects

<!-- BEGIN GENERATED PROJECTS -->

**38 projects · 9 categories**

<a id="most-starred-projects"></a>

### Most Starred Projects

GitHub API snapshot: **2026-10-29 17:33:46 UTC** · Checked daily · Stars descending, ties by case-insensitive `owner/repo`. Stars cover the whole repository, including broader frameworks; they measure attention, not benchmark quality.

Data status: complete valid snapshot. [Update policy](docs/star-rankings.md).

| Rank | Project | GitHub&nbsp;Stars | Category | Highlights |
| ---: | --- | --- | --- | --- |
| 1 | [HoloMotion · SuperMimic](https://github.com/HorizonRobotics/HoloMotion) | [![750 stars](assets/stars/1028843437.svg)](https://github.com/HorizonRobotics/HoloMotion/stargazers) | [Training Frameworks](#frameworks-and-training-stacks) | Shared G1 tasks for PPO / SuperMimic on MuJoCo Warp and Isaac PhysX. |
| 2 | [supermimic_vibed](https://github.com/zita-ch/supermimic_vibed) | [![724 stars](assets/stars/1428714029.svg)](https://github.com/zita-ch/supermimic_vibed/stargazers) | [Reproductions](#independent-reproductions) | Kit-less Isaac Lab G1 baseline with full-clip evaluation and cached ground assets. |
| 3 | [SuperMimic-Reproduced](https://github.com/CuboiLeo/SuperMimic-Reproduced) | [![315 stars](assets/stars/1429037845.svg)](https://github.com/CuboiLeo/SuperMimic-Reproduced/stargazers) | [Reproductions](#independent-reproductions) | Full BONES-SEED checkpoint and paper-vs-anchor observation experiments. |
| 4 | [InstinctMJ · SuperMimic](https://github.com/project-instinct/InstinctMJ/tree/supermimic) | [![301 stars](assets/stars/1176761185.svg)](https://github.com/project-instinct/InstinctMJ/stargazers) | [Perception &amp; Terrain](#perception-terrain-and-quadrupeds) | G1 terrain tracking with differentiable depth rendering in imagination; supermimic branch. |
| 5 | [UniSuperMimic](https://github.com/Motphys/Uni-SuperMimic) | [![205 stars](assets/stars/1429498465.svg)](https://github.com/Motphys/Uni-SuperMimic/stargazers) | [Training Frameworks](#frameworks-and-training-stacks) | Three-backend G1 training with a 129k-clip BONES-SEED pipeline and full-library evaluation. |
| 6 | [MorphMimic](https://github.com/lzyang2000/morphmimic) | [![152 stars](assets/stars/1430789167.svg)](https://github.com/lzyang2000/morphmimic/stargazers) | [Method Variants](#method-and-morphology-variants) | Morphology-conditioned G1 / X2 / T2 sharing with full-motion and five-point goals. |
| 7 | [Dex SuperMimic](https://github.com/CumulusAlpha/Dex-Supermimic) | [![75 stars](assets/stars/1433804344.svg)](https://github.com/CumulusAlpha/Dex-Supermimic/stargazers) | [Manipulation &amp; Hands](#manipulation-and-dexterous-hands) | Wuji Hand 1 / 2 cube reorientation and Hand 2 pen spin with released weights. |
| 8 | [Go2-SuperMimic](https://github.com/Zhengtianjin/go2-supermimic) | [![69 stars](assets/stars/1431486582.svg)](https://github.com/Zhengtianjin/go2-supermimic/stargazers) | [Perception &amp; Terrain](#perception-terrain-and-quadrupeds) | Simulated Go2 chase / dodge on flat ground and terrain, with released actors. |
| 9 | [InstantTrack](https://github.com/Huy-Quang-Dao/instantTrack) | [![52 stars](assets/stars/1438037302.svg)](https://github.com/Huy-Quang-Dao/instantTrack/stargazers) | [Method Variants](#method-and-morphology-variants) | EMA, fused GPU updates and contact rewards; three-seed LAFAN1 study. |
| 10 | [FlatWorld · SuperMimic-2D](https://github.com/swaggyliu/FlatWorld) | [![43 stars](assets/stars/1284715083.svg)](https://github.com/swaggyliu/FlatWorld/stargazers) | [Learning Examples](#inspired-experiments) | 2D multi-skill humanoid tracking to explore shared world-model learning. |
| 11 | [SuperMimic for Robot Manipulation](https://github.com/emoPointer/supermimic_manipulation) | [![39 stars](assets/stars/1433554854.svg)](https://github.com/emoPointer/supermimic_manipulation/stargazers) | [Manipulation &amp; Hands](#manipulation-and-dexterous-hands) | ARX5 lemon / box / mug tasks with held-out reset banks and released policies. |
| 12 | [SuperMimic-Repro-Sim2Real](https://github.com/NJU-R-L-Group-Embodied-Lab/SuperMimic-Repro-Sim2Real) | [![36 stars](assets/stars/1433556794.svg)](https://github.com/NJU-R-L-Group-Embodied-Lab/SuperMimic-Repro-Sim2Real/stargazers) | [Sim2Real](#real-robot-deployment-and-sim2real) | Clip-specific G1 dances, video-to-motion tools and ONNX deployment. |
| 13 | [In-Hand Rotation mjlab](https://github.com/Msornerrrr/in-hand-rotation-mjlab) | [![34 stars](assets/stars/1162247047.svg)](https://github.com/Msornerrrr/in-hand-rotation-mjlab/stargazers) | [Manipulation &amp; Hands](#manipulation-and-dexterous-hands) | LEAP yaw and 22-object fingertip world-model / PPO comparisons; real demos use PPO. |
| 14 | [Muscle SuperMimic](https://github.com/kaibohex/muscle-supermimic) | [![33 stars](assets/stars/1434932501.svg)](https://github.com/kaibohex/muscle-supermimic/stargazers) | [Muscles &amp; Interaction](#muscle-interaction-and-diagnostics) | 700 / 354-muscle body tracking with differentiable muscles and held-out KIT evaluation. |
| 15 | [allmimic](https://github.com/Shimingyi/allmimic) | [![31 stars](assets/stars/1431958748.svg)](https://github.com/Shimingyi/allmimic/stargazers) | [Method Variants](#method-and-morphology-variants) | Residual actions and balanced sampling, with hard-motion and held-out BONES-SEED reports. |
| 16 | [Rethinking SuperMimic](https://github.com/btx0424/rethinking-supermimic) | [![27 stars](assets/stars/1429359559.svg)](https://github.com/btx0424/rethinking-supermimic/stargazers) | [Method Variants](#method-and-morphology-variants) | FiLM goal conditioning, SAC baseline, policy EMA and gradient diagnostics. |
| 17 | [Standing MBRL vs PPO](https://github.com/JackMin7/supermimic_whole_body_tracking) | [![20 stars](assets/stars/1429495052.svg)](https://github.com/JackMin7/supermimic_whole_body_tracking/stargazers) | [Method Variants](#method-and-morphology-variants) | Matched G1 standing-task inputs and budget for MBRL / PPO comparisons. |
| 18 | [ScaleBFM_Plus · SuperMimic](https://github.com/Hxxxz0/ScaleBFM_Plus) | [![19 stars](assets/stars/1431877986.svg)](https://github.com/Hxxxz0/ScaleBFM_Plus/stargazers) | [Training Frameworks](#frameworks-and-training-stacks) | SuperMimic updates for ScaleTrack's humanoid transformer, with held-out motion reports. |
| 19 | [SuperMimic-MuJoCo](https://github.com/panhainan2020/SuperMimic-MuJoCo) | [![15 stars](assets/stars/1430957174.svg)](https://github.com/panhainan2020/SuperMimic-MuJoCo/stargazers) | [Robot Porting](#robot-porting-and-retargeting) | G1 mjlab / CPU MuJoCo port with 3,573 held-out 100STYLE clips and policy weights. |
| 20 | [TrackerLab SuperMimic](https://github.com/Renforce-Dynamics/trackerlab-supermimic) | [![13 stars](assets/stars/1430222310.svg)](https://github.com/Renforce-Dynamics/trackerlab-supermimic/stargazers) | [Training Frameworks](#frameworks-and-training-stacks) | Multi-robot PhysX stack plus optional G1 Warp training; new CUDA qualification pending. |
| 21 | [SuperMimic Parkour](https://github.com/yhx1203/supermimic_parkour) | [![12 stars](assets/stars/1430513100.svg)](https://github.com/yhx1203/supermimic_parkour/stargazers) | [Perception &amp; Terrain](#perception-terrain-and-quadrupeds) | G1 five-skill parkour using PHP motion bundles and a released checkpoint. |
| 22 | [SuperMimic Retargeted](https://github.com/tianshuwu/supermimic-retargeted) | [![9 stars](assets/stars/1430469940.svg)](https://github.com/tianshuwu/supermimic-retargeted/stargazers) | [Robot Porting](#robot-porting-and-retargeting) | G1 / A3 / X2 Ultra ports with SOMA retargeting and per-robot experiment records. |
| 23 | [SuperMimic Mjlab](https://github.com/Breezewrf/supermimic_mjlab) | [![8 stars](assets/stars/1429560578.svg)](https://github.com/Breezewrf/supermimic_mjlab/stargazers) | [Reproductions](#independent-reproductions) | 40-motion G1 tracking, velocity training and normalization / learning-rate ablations. |
| 24 | [SuperMimic G1 Deployment](https://github.com/KyrieYoung926/supermimic_deploy) | [![8 stars](assets/stars/1430946541.svg)](https://github.com/KyrieYoung926/supermimic_deploy/stargazers) | [Sim2Real](#real-robot-deployment-and-sim2real) | ONNX playback for 29-DoF G1 in MuJoCo and on hardware. |
| 25 | [Humanoid Mimic · SuperMimic](https://github.com/shuayyy/humanoid-amp-ppo) | [![8 stars](assets/stars/1285577591.svg)](https://github.com/shuayyy/humanoid-amp-ppo/stargazers) | [Manipulation &amp; Hands](#manipulation-and-dexterous-hands) | G1 walk / squat / box-lift comparisons; SuperMimic scores use clean observations. |
| 26 | [SuperMimic Wheel-Legged (wheelbipe)](https://github.com/RadiantForever/supermimic_wheelbipe) | [![7 stars](assets/stars/1437090261.svg)](https://github.com/RadiantForever/supermimic_wheelbipe/stargazers) | [Robot Porting](#robot-porting-and-retargeting) | Wheelbipe forward / yaw / leg-height control learned through world-model rollouts. |
| 27 | [SuperMimic-perceptive](https://github.com/mode1223345/SuperMimic-perceptive) | [![6 stars](assets/stars/1432125557.svg)](https://github.com/mode1223345/SuperMimic-perceptive/stargazers) | [Perception &amp; Terrain](#perception-terrain-and-quadrupeds) | Frozen shared heightmap AE for actor, critic and world model; controlled runs in progress. |
| 28 | [SuperMimic on LocoMuJoCo](https://github.com/Alchedata/supermimic-locomujoco) | [![5 stars](assets/stars/1432664861.svg)](https://github.com/Alchedata/supermimic-locomujoco/stargazers) | [Method Variants](#method-and-morphology-variants) | H1 full-state ODE dynamics and three-seed anti-saturation comparisons. |
| 29 | [supermimic_vibe](https://github.com/dhmbb2/supermimic_vibe) | [![5 stars](assets/stars/1429888171.svg)](https://github.com/dhmbb2/supermimic_vibe/stargazers) | [Reproductions](#independent-reproductions) | Full BONES-SEED evaluation, SONIC / PPO comparisons and training-collapse ablations. |
| 30 | [SuperMimic E1](https://github.com/wenconggan/SuperMimic_e1) | [![5 stars](assets/stars/1430480272.svg)](https://github.com/wenconggan/SuperMimic_e1/stargazers) | [Robot Porting](#robot-porting-and-retargeting) | 21-DoF E1 tracking with native MuJoCo playback and separate full-clip metrics. |
| 31 | [SuperMimicKit](https://github.com/OMEGA-i/SuperMimicKit) | [![4 stars](assets/stars/1431562951.svg)](https://github.com/OMEGA-i/SuperMimicKit/stargazers) | [Training Frameworks](#frameworks-and-training-stacks) | G1 / H2 train40 / val37 metrics and G1 / H2 / A3 ONNX / WebGPU previews. |
| 32 | [SuperMimic Oli](https://github.com/liuskywalkerjskd/supermimic_oli) | [![3 stars](assets/stars/1431102076.svg)](https://github.com/liuskywalkerjskd/supermimic_oli/stargazers) | [Robot Porting](#robot-porting-and-retargeting) | 31-DoF Oli adaptation with 40-clip metrics and full-motion videos. |
| 33 | [SuperMimic Lab](https://github.com/chu-fa/isaaclab-supermimic) | [![2 stars](assets/stars/1431327517.svg)](https://github.com/chu-fa/isaaclab-supermimic/stargazers) | [Training Frameworks](#frameworks-and-training-stacks) | Isaac Lab learner / task contracts with a separately installable A3 example. |
| 34 | [SuperMimic Backflip Diagnostics](https://github.com/liudi159/supermimic-backflip-5090) | [![2 stars](assets/stars/1432819468.svg)](https://github.com/liudi159/supermimic-backflip-5090/stargazers) | [Muscles &amp; Interaction](#muscle-interaction-and-diagnostics) | G1 backflip symmetry and landing diagnostics; strict contact checks still fail. |
| 35 | [SuperMimic on RTX 5080](https://github.com/rzc156/supermimic-rtx5080) | [![2 stars](assets/stars/1434000857.svg)](https://github.com/rzc156/supermimic-rtx5080/stargazers) | [Reproductions](#independent-reproductions) | 16 GB RTX 5080 adaptation with anchor observations and full LAFAN1 evaluation. |
| 36 | [SuperMimic on Apple M5](https://github.com/WXyuany/supermimic-m5) | [![1 stars](assets/stars/1430927278.svg)](https://github.com/WXyuany/supermimic-m5/stargazers) | [Robot Porting](#robot-porting-and-retargeting) | Apple M5: MPS learning, CPU MuJoCo physics and released G1 weights. |
| 37 | [G0.5 · SuperMimic-style Steering](https://github.com/azizkhadraoui/g05) | [![0 stars](assets/stars/1425368329.svg)](https://github.com/azizkhadraoui/g05/stargazers) | [Learning Examples](#inspired-experiments) | SuperMimic-style VLA steering and direct-policy fine-tuning failures on LIBERO. |
| 38 | [SuperMimic-PERA](https://github.com/shangchaohu718/supermimic-pera) | [![0 stars](assets/stars/1430576677.svg)](https://github.com/shangchaohu718/supermimic-pera/stargazers) | [Muscles &amp; Interaction](#muscle-interaction-and-diagnostics) | Frozen G1 tracker plus a separate simulated skateboarding policy. |

<a id="browse-by-category"></a>

### Browse by Category

[Sim2Real (2)](#real-robot-deployment-and-sim2real) · [Reproductions (5)](#independent-reproductions) · [Method Variants (6)](#method-and-morphology-variants) · [Perception &amp; Terrain (4)](#perception-terrain-and-quadrupeds) · [Manipulation &amp; Hands (4)](#manipulation-and-dexterous-hands) · [Muscles &amp; Interaction (3)](#muscle-interaction-and-diagnostics) · [Training Frameworks (6)](#frameworks-and-training-stacks) · [Robot Porting (6)](#robot-porting-and-retargeting) · [Learning Examples (2)](#inspired-experiments)

Each category also follows Stars order. Full experiments, limitations and GIFs live in the linked project details.

<a id="maintainers-picks"></a>

### Maintainer’s Picks

⭐ Retains the existing editorial selections, with reasons from the curated sources. These are independent of the Stars ranking.

| Project | Why read it |
| --- | --- |
| ⭐ [SuperMimic-Repro-Sim2Real](#supermimic-repro-sim2real) | G1 hardware demos and deployment notes |
| ⭐ [supermimic_vibed](#supermimic_vibed) | LAFAN1 training baseline |
| ⭐ [SuperMimic-Reproduced](#supermimic-reproduced) | BONES-SEED experiment logs and weights |
| ⭐ [SuperMimic Mjlab](#supermimic-mjlab) | step-by-step ablations and released checkpoints |
| ⭐ [InstantTrack](#instanttrack) | 15-minute LAFAN1 target on one RTX 5090, three seeds |
| ⭐ [MorphMimic](#morphmimic) | world-model / policy sharing across G1, X2 Ultra and T2 |
| ⭐ [InstinctMJ · SuperMimic](#instinctmj--supermimic) | Differentiable depth rendering for perceptive terrain tracking |
| ⭐ [Go2-SuperMimic](#go2-supermimic) | quadruped chase / dodge with released actors |
| ⭐ [SuperMimic for Robot Manipulation](#supermimic-for-robot-manipulation) | three ARX5 arm tasks, weights and reset banks |
| ⭐ [Dex SuperMimic](#dex-supermimic) | Wuji hands: cube reorientation, pen spinning and weights |
| ⭐ [In-Hand Rotation mjlab](#in-hand-rotation-mjlab) | LEAP hand: world-model / PPO simulation comparisons |
| ⭐ [Muscle SuperMimic](#muscle-supermimic) | two muscle-driven bodies, held-out KIT evaluation |
| ⭐ [UniSuperMimic](#unisupermimic) | Three backends, full-library evaluation and EMA / no-sync training |
| ⭐ [ScaleBFM_Plus · SuperMimic](#scalebfm_plus--supermimic) | humanoid transformer integration and held-out evaluation |
| ⭐ [SuperMimic Retargeted](#supermimic-retargeted) | G1 / A3 / X2 Ultra retargeting and coordinate checks |
| ⭐ [FlatWorld · SuperMimic-2D](#flatworld--supermimic-2d) | see the learning loop in a 2D multi-skill demo |

<a id="new--noteworthy"></a>

### New & Noteworthy

The five most recently added entries, using first inclusion dates from this list’s Git history, then repository name for same-day ties. Dates link to evidence; they are not project release dates or quality scores. No Stars threshold.

| Added to this list | Project | What to explore |
| --- | --- | --- |
| [2026-10-29](https://github.com/miao-org/awesome-supermimic/commit/4ec2021a76c389760c79cf8149fa5a20e998fe98) | [InstantTrack](#instanttrack) | EMA, fused GPU updates and contact rewards; three-seed LAFAN1 study. |
| [2026-10-28](https://github.com/miao-org/awesome-supermimic/commit/0035f0d90c1fae44cf2ecbf6fb8584bee6f1f415) | [Standing MBRL vs PPO](#standing-mbrl-vs-ppo) | Matched G1 standing-task inputs and budget for MBRL / PPO comparisons. |
| [2026-10-28](https://github.com/miao-org/awesome-supermimic/commit/f03b1b9e0a24b3ca65f6da06ec3f12aa8eced02c) | [In-Hand Rotation mjlab](#in-hand-rotation-mjlab) | LEAP yaw and 22-object fingertip world-model / PPO comparisons; real demos use PPO. |
| [2026-10-28](https://github.com/miao-org/awesome-supermimic/commit/9706213a5c3eee8ea16e0e53fdc3d589eab23441) | [SuperMimic Wheel-Legged (wheelbipe)](#supermimic-wheel-legged-wheelbipe) | Wheelbipe forward / yaw / leg-height control learned through world-model rollouts. |
| [2026-10-28](https://github.com/miao-org/awesome-supermimic/commit/0035f0d90c1fae44cf2ecbf6fb8584bee6f1f415) | [SuperMimic on RTX 5080](#supermimic-on-rtx-5080) | 16 GB RTX 5080 adaptation with anchor observations and full LAFAN1 evaluation. |

<a id="real-robot-deployment-and-sim2real"></a>

### Real-robot deployment and Sim2Real (2)

<a id="supermimic-repro-sim2real"></a>
<a id="-supermimic-repro-sim2real"></a>

**[SuperMimic-Repro-Sim2Real](https://github.com/NJU-R-L-Group-Embodied-Lab/SuperMimic-Repro-Sim2Real)** · [![36 stars](assets/stars/1433556794.svg)](https://github.com/NJU-R-L-Group-Embodied-Lab/SuperMimic-Repro-Sim2Real/stargazers) · ⭐ Maintainer’s Pick

**Stack:** mjlab / MuJoCo / Unitree SDK · **By:** NJU R&amp;L Group Embodied Lab<br>
Clip-specific G1 dances, video-to-motion tools and ONNX deployment.

[Repository](https://github.com/NJU-R-L-Group-Embodied-Lab/SuperMimic-Repro-Sim2Real) · [Demo](https://github.com/NJU-R-L-Group-Embodied-Lab/SuperMimic-Repro-Sim2Real/releases/download/v1.1/shanshenbu_pro_real_robot.mp4) · [Results & details](docs/community-projects.md#supermimic-repro-sim2real) · [Quickstart](https://github.com/NJU-R-L-Group-Embodied-Lab/SuperMimic-Repro-Sim2Real/blob/f8f60d7bbdba68468c050ef100af02d752ca238e/README.md#快速开始)

<a id="supermimic-g1-deployment"></a>

**[SuperMimic G1 Deployment](https://github.com/KyrieYoung926/supermimic_deploy)** · [![8 stars](assets/stars/1430946541.svg)](https://github.com/KyrieYoung926/supermimic_deploy/stargazers)

**Stack:** ONNX Runtime / MuJoCo / Unitree SDK2 · **By:** KyrieYoung926<br>
ONNX playback for 29-DoF G1 in MuJoCo and on hardware.

[Repository](https://github.com/KyrieYoung926/supermimic_deploy) · [Demo](https://github.com/KyrieYoung926/supermimic_deploy) · [Results & details](docs/community-projects.md#supermimic-g1-deployment) · [MuJoCo guide](https://github.com/KyrieYoung926/supermimic_deploy/blob/7e63e3bbd5150d55afbdece28278781800f3ed21/README.md#3-run-in-mujoco)


<a id="independent-reproductions"></a>

### Independent reproductions (5)

<a id="supermimic_vibed"></a>
<a id="-supermimic_vibed"></a>

**[supermimic_vibed](https://github.com/zita-ch/supermimic_vibed)** · [![724 stars](assets/stars/1428714029.svg)](https://github.com/zita-ch/supermimic_vibed/stargazers) · ⭐ Maintainer’s Pick

**Stack:** Isaac Lab 3 · **By:** Chong Zhang<br>
Kit-less Isaac Lab G1 baseline with full-clip evaluation and cached ground assets.

[Repository](https://github.com/zita-ch/supermimic_vibed) · [Demo](https://github.com/zita-ch/supermimic_vibed) · [Results & details](docs/community-projects.md#supermimic_vibed) · [Setup and usage](https://github.com/zita-ch/supermimic_vibed/blob/8bfc1158bd968f729fcc65d5e897a05b05ea3d36/README.md#setup)

<a id="supermimic-reproduced"></a>
<a id="-supermimic-reproduced"></a>

**[SuperMimic-Reproduced](https://github.com/CuboiLeo/SuperMimic-Reproduced)** · [![315 stars](assets/stars/1429037845.svg)](https://github.com/CuboiLeo/SuperMimic-Reproduced/stargazers) · ⭐ Maintainer’s Pick

**Stack:** mjlab · **By:** CuboiLeo<br>
Full BONES-SEED checkpoint and paper-vs-anchor observation experiments.

[Repository](https://github.com/CuboiLeo/SuperMimic-Reproduced) · [Demo](https://github.com/CuboiLeo/SuperMimic-Reproduced/releases/tag/e8-boneseed-100k) · [Results & details](docs/community-projects.md#supermimic-reproduced) · [Setup](https://github.com/CuboiLeo/SuperMimic-Reproduced/blob/ba6105349069bf040f1fdad60873d13138d505a2/README.md#setup)

<a id="supermimic-mjlab"></a>
<a id="-supermimic-mjlab"></a>

**[SuperMimic Mjlab](https://github.com/Breezewrf/supermimic_mjlab)** · [![8 stars](assets/stars/1429560578.svg)](https://github.com/Breezewrf/supermimic_mjlab/stargazers) · ⭐ Maintainer’s Pick

**Stack:** mjlab · **By:** Breezewrf<br>
40-motion G1 tracking, velocity training and normalization / learning-rate ablations.

[Repository](https://github.com/Breezewrf/supermimic_mjlab) · [Demo](https://github.com/Breezewrf/supermimic_mjlab/blob/77183062eb92026bfbee2daf276f87cad36fd957/doc/assets/demo_v0.gif) · [Results & details](docs/community-projects.md#supermimic-mjlab) · [Setup](https://github.com/Breezewrf/supermimic_mjlab/blob/77183062eb92026bfbee2daf276f87cad36fd957/doc/setup_en.md)

<a id="supermimic_vibe"></a>

**[supermimic_vibe](https://github.com/dhmbb2/supermimic_vibe)** · [![5 stars](assets/stars/1429888171.svg)](https://github.com/dhmbb2/supermimic_vibe/stargazers)

**Stack:** mjlab · **By:** dhmbb2<br>
Full BONES-SEED evaluation, SONIC / PPO comparisons and training-collapse ablations.

[Repository](https://github.com/dhmbb2/supermimic_vibe) · [Demo](https://github.com/dhmbb2/supermimic_vibe/blob/d0934d069207ee745be8489d9631a8314c94c1f3/README.md#results) · [Results & details](docs/community-projects.md#supermimic_vibe) · [Setup](https://github.com/dhmbb2/supermimic_vibe/blob/d0934d069207ee745be8489d9631a8314c94c1f3/README.md#setup)

<a id="supermimic-on-rtx-5080"></a>

**[SuperMimic on RTX 5080](https://github.com/rzc156/supermimic-rtx5080)** · [![2 stars](assets/stars/1434000857.svg)](https://github.com/rzc156/supermimic-rtx5080/stargazers)

**Stack:** mjlab · **By:** rzc156<br>
16 GB RTX 5080 adaptation with anchor observations and full LAFAN1 evaluation.

[Repository](https://github.com/rzc156/supermimic-rtx5080) · [Demo](https://github.com/rzc156/supermimic-rtx5080/blob/df967c61c29a2ed9ba6b188e1607ba59225fe8a7/results/lafan1_anchor/videos/index.html) · [Results & details](docs/community-projects.md#supermimic-on-rtx-5080) · [Reproduction analysis](https://github.com/rzc156/supermimic-rtx5080/blob/df967c61c29a2ed9ba6b188e1607ba59225fe8a7/REPRODUCTION_ANALYSIS.md)


<a id="method-and-morphology-variants"></a>

### Method and morphology variants (6)

<a id="morphmimic"></a>
<a id="-morphmimic"></a>

**[MorphMimic](https://github.com/lzyang2000/morphmimic)** · [![152 stars](assets/stars/1430789167.svg)](https://github.com/lzyang2000/morphmimic/stargazers) · ⭐ Maintainer’s Pick

**Stack:** mjlab · **By:** Lizhi Yang et al<br>
Morphology-conditioned G1 / X2 / T2 sharing with full-motion and five-point goals.

[Repository](https://github.com/lzyang2000/morphmimic) · [Demo](https://lzyang2000.github.io/morphmimic/static/videos/dance_hiphop_shuffle_sequence_v_001_R_003__A306.mp4) · [Results & details](docs/community-projects.md#morphmimic) · [Setup](https://github.com/lzyang2000/morphmimic/blob/aa40fe46a7fa995ba7a7354ad065a2c8ad64a302/README.md#setup)

<a id="instanttrack"></a>
<a id="-instanttrack"></a>

**[InstantTrack](https://github.com/Huy-Quang-Dao/instantTrack)** · [![52 stars](assets/stars/1438037302.svg)](https://github.com/Huy-Quang-Dao/instantTrack/stargazers) · ⭐ Maintainer’s Pick

**Stack:** mjlab · **By:** Huy-Quang-Dao<br>
EMA, fused GPU updates and contact rewards; three-seed LAFAN1 study.

[Repository](https://github.com/Huy-Quang-Dao/instantTrack) · [Demo](https://github.com/Huy-Quang-Dao/instantTrack/blob/a33691a08bca8802d9d2985f62e2567479735a8e/media/equal_time_15min.gif) · [Results & details](docs/community-projects.md#instanttrack) · [Setup](https://github.com/Huy-Quang-Dao/instantTrack/blob/a33691a08bca8802d9d2985f62e2567479735a8e/README.md#setup)

<a id="allmimic"></a>

**[allmimic](https://github.com/Shimingyi/allmimic)** · [![31 stars](assets/stars/1431958748.svg)](https://github.com/Shimingyi/allmimic/stargazers)

**Stack:** mjlab · **By:** Shimingyi<br>
Residual actions and balanced sampling, with hard-motion and held-out BONES-SEED reports.

[Repository](https://github.com/Shimingyi/allmimic) · [Demo](https://github.com/Shimingyi/allmimic) · [Results & details](docs/community-projects.md#allmimic) · [Install](https://github.com/Shimingyi/allmimic/blob/cb334ff674b2f57248f33f8c21b7fb526fbdf8cc/README.md#install)

<a id="rethinking-supermimic"></a>

**[Rethinking SuperMimic](https://github.com/btx0424/rethinking-supermimic)** · [![27 stars](assets/stars/1429359559.svg)](https://github.com/btx0424/rethinking-supermimic/stargazers)

**Stack:** mjlab · **By:** btx0424<br>
FiLM goal conditioning, SAC baseline, policy EMA and gradient diagnostics.

[Repository](https://github.com/btx0424/rethinking-supermimic) · [Demo](https://github.com/btx0424/rethinking-supermimic/blob/ecdaeb6a916a16cf7eb69b19226c17be31a6bc27/README.md) · [Results & details](docs/community-projects.md#rethinking-supermimic) · [Installation](https://github.com/btx0424/rethinking-supermimic/blob/2cbbd1278bfb8bd59c31fe48d7413c46ae205e32/README.md#installation)

<a id="standing-mbrl-vs-ppo"></a>

**[Standing MBRL vs PPO](https://github.com/JackMin7/supermimic_whole_body_tracking)** · [![20 stars](assets/stars/1429495052.svg)](https://github.com/JackMin7/supermimic_whole_body_tracking/stargazers)

**Stack:** RSL-RL / G1 · **By:** JackMin7<br>
Matched G1 standing-task inputs and budget for MBRL / PPO comparisons.

[Repository](https://github.com/JackMin7/supermimic_whole_body_tracking) · [Demo](https://github.com/JackMin7/supermimic_whole_body_tracking/blob/553a7d32dc5fc00cbe6de5ee46479af2fcceeda8/media/ppo_vs_mbrl_60s.mp4) · [Results & details](docs/community-projects.md#standing-mbrl-vs-ppo) · [Experiment details](https://github.com/JackMin7/supermimic_whole_body_tracking/blob/553a7d32dc5fc00cbe6de5ee46479af2fcceeda8/docs/EXPERIMENTS.md)

<a id="supermimic-on-locomujoco"></a>

**[SuperMimic on LocoMuJoCo](https://github.com/Alchedata/supermimic-locomujoco)** · [![5 stars](assets/stars/1432664861.svg)](https://github.com/Alchedata/supermimic-locomujoco/stargazers)

**Stack:** JAX / LocoMuJoCo · **By:** Alchedata<br>
H1 full-state ODE dynamics and three-seed anti-saturation comparisons.

[Repository](https://github.com/Alchedata/supermimic-locomujoco) · [Demo](https://github.com/Alchedata/supermimic-locomujoco/blob/de9f39191b9e8b87ff1afd2b0129dd93d4795e8c/docs/figures/return_vs_step.png) · [Results & details](docs/community-projects.md#supermimic-on-locomujoco) · [Setup](https://github.com/Alchedata/supermimic-locomujoco/blob/de9f39191b9e8b87ff1afd2b0129dd93d4795e8c/README.md#setup)


<a id="perception-terrain-and-quadrupeds"></a>

### Perception, terrain and quadrupeds (4)

<a id="instinctmj--supermimic"></a>
<a id="-instinctmj--supermimic"></a>

**[InstinctMJ · SuperMimic](https://github.com/project-instinct/InstinctMJ/tree/supermimic)** · [![301 stars](assets/stars/1176761185.svg)](https://github.com/project-instinct/InstinctMJ/stargazers) · ⭐ Maintainer’s Pick

**Stack:** mjlab / instinct_rl · **By:** Project Instinct<br>
G1 terrain tracking with differentiable depth rendering in imagination; supermimic branch.

[Repository](https://github.com/project-instinct/InstinctMJ/tree/supermimic) · [Demo](https://github.com/project-instinct/InstinctMJ/blob/3f0952d36268c6aad299e256d27cc65d3bcc1434/src/instinct_mj/rl/supermimic/assets/method.png) · [Results & details](docs/community-projects.md#instinctmj--supermimic) · [Method and results](https://github.com/project-instinct/InstinctMJ/blob/3f0952d36268c6aad299e256d27cc65d3bcc1434/src/instinct_mj/rl/supermimic/README.md#results)

<a id="go2-supermimic"></a>
<a id="-go2-supermimic"></a>

**[Go2-SuperMimic](https://github.com/Zhengtianjin/go2-supermimic)** · [![69 stars](assets/stars/1431486582.svg)](https://github.com/Zhengtianjin/go2-supermimic/stargazers) · ⭐ Maintainer’s Pick

**Stack:** mjlab · **By:** Zhengtianjin<br>
Simulated Go2 chase / dodge on flat ground and terrain, with released actors.

[Repository](https://github.com/Zhengtianjin/go2-supermimic) · [Demo](https://github.com/Zhengtianjin/go2-supermimic) · [Results & details](docs/community-projects.md#go2-supermimic) · [Quickstart](https://github.com/Zhengtianjin/go2-supermimic/blob/d9eee9b3f248e5300e636c433255db2c1c3e086a/README.md#-quickstart)

<a id="supermimic-parkour"></a>

**[SuperMimic Parkour](https://github.com/yhx1203/supermimic_parkour)** · [![12 stars](assets/stars/1430513100.svg)](https://github.com/yhx1203/supermimic_parkour/stargazers)

**Stack:** mjlab / PHP Parkour · **By:** yhx1203<br>
G1 five-skill parkour using PHP motion bundles and a released checkpoint.

[Repository](https://github.com/yhx1203/supermimic_parkour) · [Demo](https://github.com/yhx1203/supermimic_parkour/blob/f398519453a25b3f10722626b7356266d8b7f875/doc/%E5%BD%95%E5%B1%8F%202026%E5%B9%B410%E6%9C%8826%E6%97%A5%2016%E6%97%B641%E5%88%8626%E7%A7%92.gif) · [Results & details](docs/community-projects.md#supermimic-parkour) · [Data setup](https://github.com/yhx1203/supermimic_parkour/blob/f398519453a25b3f10722626b7356266d8b7f875/README.md#motion-data)

<a id="supermimic-perceptive"></a>

**[SuperMimic-perceptive](https://github.com/mode1223345/SuperMimic-perceptive)** · [![6 stars](assets/stars/1432125557.svg)](https://github.com/mode1223345/SuperMimic-perceptive/stargazers)

**Stack:** Isaac Lab 3 · **By:** mode1223345<br>
Frozen shared heightmap AE for actor, critic and world model; controlled runs in progress.

[Repository](https://github.com/mode1223345/SuperMimic-perceptive) · [Demo](https://github.com/mode1223345/SuperMimic-perceptive/blob/3d38bacbaf5bee7e782bdada6a6da678264d0bfa/results/Curves.png) · [Results & details](docs/community-projects.md#supermimic-perceptive) · [Method](https://github.com/mode1223345/SuperMimic-perceptive/blob/3d38bacbaf5bee7e782bdada6a6da678264d0bfa/Ae.md)


<a id="manipulation-and-dexterous-hands"></a>

### Manipulation and dexterous hands (4)

<a id="dex-supermimic"></a>
<a id="-dex-supermimic"></a>

**[Dex SuperMimic](https://github.com/CumulusAlpha/Dex-Supermimic)** · [![75 stars](assets/stars/1433804344.svg)](https://github.com/CumulusAlpha/Dex-Supermimic/stargazers) · ⭐ Maintainer’s Pick

**Stack:** mjlab / MuJoCo Warp / InstinctMJ · **By:** CumulusAlpha<br>
Wuji Hand 1 / 2 cube reorientation and Hand 2 pen spin with released weights.

[Repository](https://github.com/CumulusAlpha/Dex-Supermimic) · [Demo](https://github.com/CumulusAlpha/Dex-Supermimic/blob/3a7c1a33fd8e5c6cc047e381ea9309da96553c27/docs/demos/hand1_reorient.gif) · [Results & details](docs/community-projects.md#dex-supermimic) · [Installation](https://github.com/CumulusAlpha/Dex-Supermimic/blob/3a7c1a33fd8e5c6cc047e381ea9309da96553c27/README.md#installation)

<a id="supermimic-for-robot-manipulation"></a>
<a id="-supermimic-for-robot-manipulation"></a>

**[SuperMimic for Robot Manipulation](https://github.com/emoPointer/supermimic_manipulation)** · [![39 stars](assets/stars/1433554854.svg)](https://github.com/emoPointer/supermimic_manipulation/stargazers) · ⭐ Maintainer’s Pick

**Stack:** mjlab / MuJoCo Warp · **By:** Zhiqiang Zhou (emoPointer)<br>
ARX5 lemon / box / mug tasks with held-out reset banks and released policies.

[Repository](https://github.com/emoPointer/supermimic_manipulation) · [Demo](https://github.com/emoPointer/supermimic_manipulation) · [Results & details](docs/community-projects.md#supermimic-for-robot-manipulation) · [Setup](https://github.com/emoPointer/supermimic_manipulation/blob/810e5768c50117d2fec75f20f9e643a11cd0882b/README.md#install)

<a id="in-hand-rotation-mjlab"></a>
<a id="-in-hand-rotation-mjlab"></a>

**[In-Hand Rotation mjlab](https://github.com/Msornerrrr/in-hand-rotation-mjlab)** · [![34 stars](assets/stars/1162247047.svg)](https://github.com/Msornerrrr/in-hand-rotation-mjlab/stargazers) · ⭐ Maintainer’s Pick

**Stack:** mjlab / MuJoCo Warp · **By:** Msornerrrr<br>
LEAP yaw and 22-object fingertip world-model / PPO comparisons; real demos use PPO.

[Repository](https://github.com/Msornerrrr/in-hand-rotation-mjlab) · [Demo](https://github.com/Msornerrrr/in-hand-rotation-mjlab) · [Results & details](docs/community-projects.md#in-hand-rotation-mjlab) · [Install](https://github.com/Msornerrrr/in-hand-rotation-mjlab/blob/0ab03eb2244b4a1a020d94ef38a4823bb9e15ba0/README.md#install)

<a id="humanoid-mimic--supermimic"></a>

**[Humanoid Mimic · SuperMimic](https://github.com/shuayyy/humanoid-amp-ppo)** · [![8 stars](assets/stars/1285577591.svg)](https://github.com/shuayyy/humanoid-amp-ppo/stargazers)

**Stack:** mjlab · **By:** shuayyy<br>
G1 walk / squat / box-lift comparisons; SuperMimic scores use clean observations.

[Repository](https://github.com/shuayyy/humanoid-amp-ppo) · [Demo](https://github.com/shuayyy/humanoid-amp-ppo/blob/4889389118e0c88d3945dff54d2cd3f992ed815e/assets/supermimic_vs_ppo_lift.mp4) · [Results & details](docs/community-projects.md#humanoid-mimic--supermimic) · [Quickstart](https://github.com/shuayyy/humanoid-amp-ppo/blob/681874bab20273ba9211cb92d5ff108900ce3490/README.md#quickstart)


<a id="muscle-interaction-and-diagnostics"></a>

### Muscle, interaction and diagnostics (3)

<a id="muscle-supermimic"></a>
<a id="-muscle-supermimic"></a>

**[Muscle SuperMimic](https://github.com/kaibohex/muscle-supermimic)** · [![33 stars](assets/stars/1434932501.svg)](https://github.com/kaibohex/muscle-supermimic/stargazers) · ⭐ Maintainer’s Pick

**Stack:** mjlab / MuJoCo Warp · **By:** Kaibo He (kaibohex)<br>
700 / 354-muscle body tracking with differentiable muscles and held-out KIT evaluation.

[Repository](https://github.com/kaibohex/muscle-supermimic) · [Demo](https://github.com/kaibohex/muscle-supermimic) · [Results & details](docs/community-projects.md#muscle-supermimic) · [Setup](https://github.com/kaibohex/muscle-supermimic/blob/932ac22ca720b1c4db40c4323a3b67bf3c1eaa99/README.md#install)

<a id="supermimic-backflip-diagnostics"></a>

**[SuperMimic Backflip Diagnostics](https://github.com/liudi159/supermimic-backflip-5090)** · [![2 stars](assets/stars/1432819468.svg)](https://github.com/liudi159/supermimic-backflip-5090/stargazers)

**Stack:** Isaac Lab 3 · **By:** liudi159<br>
G1 backflip symmetry and landing diagnostics; strict contact checks still fail.

[Repository](https://github.com/liudi159/supermimic-backflip-5090) · [Demo](https://github.com/liudi159/supermimic-backflip-5090/blob/5b313d75e804cdd2ff1ce9bdcfa899a98eca856b/media/v14_blue_checker.mp4) · [Results & details](docs/community-projects.md#supermimic-backflip-diagnostics) · [Results](https://github.com/liudi159/supermimic-backflip-5090/blob/5b313d75e804cdd2ff1ce9bdcfa899a98eca856b/README.md#结果)

<a id="supermimic-pera"></a>

**[SuperMimic-PERA](https://github.com/shangchaohu718/supermimic-pera)** · [![0 stars](assets/stars/1430576677.svg)](https://github.com/shangchaohu718/supermimic-pera/stargazers)

**Stack:** UniLab / MuJoCo · **By:** shangchaohu718<br>
Frozen G1 tracker plus a separate simulated skateboarding policy.

[Repository](https://github.com/shangchaohu718/supermimic-pera) · [Demo](https://github.com/shangchaohu718/supermimic-pera/blob/0e89e55187a800341e609129b5d5200a607a467c/README.md) · [Results & details](docs/community-projects.md#supermimic-pera) · [Current status](https://github.com/shangchaohu718/supermimic-pera/blob/0e89e55187a800341e609129b5d5200a607a467c/README.md#当前状态)


<a id="frameworks-and-training-stacks"></a>

### Frameworks and training stacks (6)

<a id="holomotion--supermimic"></a>

**[HoloMotion · SuperMimic](https://github.com/HorizonRobotics/HoloMotion)** · [![750 stars](assets/stars/1028843437.svg)](https://github.com/HorizonRobotics/HoloMotion/stargazers)

**Stack:** MuJoCo Warp / Isaac PhysX / Hydra · **By:** Horizon Robotics<br>
Shared G1 tasks for PPO / SuperMimic on MuJoCo Warp and Isaac PhysX.

[Repository](https://github.com/HorizonRobotics/HoloMotion) · [Demo](https://github.com/HorizonRobotics/HoloMotion) · [Results & details](docs/community-projects.md#holomotion--supermimic) · [Training guide](https://github.com/HorizonRobotics/HoloMotion/blob/f52dd81ae935a828b0296f5ee0f833beb7378bf0/docs/supermimic.md)

<a id="unisupermimic"></a>
<a id="-unisupermimic"></a>

**[UniSuperMimic](https://github.com/Motphys/Uni-SuperMimic)** · [![205 stars](assets/stars/1429498465.svg)](https://github.com/Motphys/Uni-SuperMimic/stargazers) · ⭐ Maintainer’s Pick

**Stack:** UniLab / mjwarp / MuJoCo / Motrix · **By:** Motphys<br>
Three-backend G1 training with a 129k-clip BONES-SEED pipeline and full-library evaluation.

[Repository](https://github.com/Motphys/Uni-SuperMimic) · [Demo](https://github.com/Motphys/Uni-SuperMimic/blob/9bdcbde1f191d88b489309182624a9877e7b6c30/docs/assets/supermimic_comparison.mp4) · [Results & details](docs/community-projects.md#unisupermimic) · [Installation](https://github.com/Motphys/Uni-SuperMimic/blob/05a9772ca09509c50a4cc3fe96f9d6b3c180f3d2/README.md#installation)

<a id="scalebfm_plus--supermimic"></a>
<a id="-scalebfm_plus--supermimic"></a>

**[ScaleBFM_Plus · SuperMimic](https://github.com/Hxxxz0/ScaleBFM_Plus)** · [![19 stars](assets/stars/1431877986.svg)](https://github.com/Hxxxz0/ScaleBFM_Plus/stargazers) · ⭐ Maintainer’s Pick

**Stack:** Isaac Lab / RSL-RL · **By:** Hxxxz0, building on ScaleBFM<br>
SuperMimic updates for ScaleTrack's humanoid transformer, with held-out motion reports.

[Repository](https://github.com/Hxxxz0/ScaleBFM_Plus) · [Demo](https://github.com/Hxxxz0/ScaleBFM_Plus/blob/65e4d524bd31fdc4284ba8c6e624fb0b0127da03/ScaleTrack/assets/demos/supermimic_vs_official.gif) · [Results & details](docs/community-projects.md#scalebfm_plus--supermimic) · [Training and results](https://github.com/Hxxxz0/ScaleBFM_Plus/blob/65e4d524bd31fdc4284ba8c6e624fb0b0127da03/ScaleTrack/README.md#fast-training-with-a-learned-world-model-supermimic)

<a id="trackerlab-supermimic"></a>

**[TrackerLab SuperMimic](https://github.com/Renforce-Dynamics/trackerlab-supermimic)** · [![13 stars](assets/stars/1430222310.svg)](https://github.com/Renforce-Dynamics/trackerlab-supermimic/stargazers)

**Stack:** Isaac Lab / PhysX; optional MuJoCo Warp · **By:** Renforce Dynamics<br>
Multi-robot PhysX stack plus optional G1 Warp training; new CUDA qualification pending.

[Repository](https://github.com/Renforce-Dynamics/trackerlab-supermimic) · [Demo](https://github.com/Renforce-Dynamics/trackerlab-supermimic/blob/29d24524f2f731bf4df75b319c3e76544165849e/docs/media/g1_dance_032000.mp4) · [Results & details](docs/community-projects.md#trackerlab-supermimic) · [Install](https://github.com/Renforce-Dynamics/trackerlab-supermimic/blob/813f37a89d9be0791c9c72695a322307001a5d11/README.md#install)

<a id="supermimickit"></a>

**[SuperMimicKit](https://github.com/OMEGA-i/SuperMimicKit)** · [![4 stars](assets/stars/1431562951.svg)](https://github.com/OMEGA-i/SuperMimicKit/stargazers)

**Stack:** MuJoCo Warp / ONNX / WebGPU · **By:** OMEGA-i<br>
G1 / H2 train40 / val37 metrics and G1 / H2 / A3 ONNX / WebGPU previews.

[Repository](https://github.com/OMEGA-i/SuperMimicKit) · [Demo](https://github.com/OMEGA-i/SuperMimicKit/blob/6697ff8ca53adc9233ded12a7c8777610ca1154d/docs/media/teaser.mp4) · [Results & details](docs/community-projects.md#supermimickit) · [Preview release](https://github.com/OMEGA-i/SuperMimicKit/releases/tag/demo-preview-20261024)

<a id="supermimic-lab"></a>

**[SuperMimic Lab](https://github.com/chu-fa/isaaclab-supermimic)** · [![2 stars](assets/stars/1431327517.svg)](https://github.com/chu-fa/isaaclab-supermimic/stargazers)

**Stack:** Isaac Lab · **By:** chu-fa<br>
Isaac Lab learner / task contracts with a separately installable A3 example.

[Repository](https://github.com/chu-fa/isaaclab-supermimic) · [Demo](https://github.com/chu-fa/isaaclab-supermimic) · [Results & details](docs/community-projects.md#supermimic-lab) · [Setup](https://github.com/chu-fa/isaaclab-supermimic/blob/d350e4378c6dc08a3f2a1d35d47b45d83db0e081/docs/SETUP.md)


<a id="robot-porting-and-retargeting"></a>

### Robot porting and retargeting (6)

<a id="supermimic-mujoco"></a>

**[SuperMimic-MuJoCo](https://github.com/panhainan2020/SuperMimic-MuJoCo)** · [![15 stars](assets/stars/1430957174.svg)](https://github.com/panhainan2020/SuperMimic-MuJoCo/stargazers)

**Stack:** mjlab / CPU MuJoCo · **By:** panhainan2020<br>
G1 mjlab / CPU MuJoCo port with 3,573 held-out 100STYLE clips and policy weights.

[Repository](https://github.com/panhainan2020/SuperMimic-MuJoCo) · [Demo](https://github.com/panhainan2020/SuperMimic-MuJoCo/blob/db045afa9c52458f213e2c66037387e9c109a03a/README.md) · [Results & details](docs/community-projects.md#supermimic-mujoco) · [Setup](https://github.com/panhainan2020/SuperMimic-MuJoCo/blob/db045afa9c52458f213e2c66037387e9c109a03a/README.md#环境安装)

<a id="supermimic-retargeted"></a>
<a id="-supermimic-retargeted"></a>

**[SuperMimic Retargeted](https://github.com/tianshuwu/supermimic-retargeted)** · [![9 stars](assets/stars/1430469940.svg)](https://github.com/tianshuwu/supermimic-retargeted/stargazers) · ⭐ Maintainer’s Pick

**Stack:** mjlab / SOMA · **By:** tianshuwu<br>
G1 / A3 / X2 Ultra ports with SOMA retargeting and per-robot experiment records.

[Repository](https://github.com/tianshuwu/supermimic-retargeted) · [Demo](https://github.com/tianshuwu/supermimic-retargeted/blob/ff69a0e5305126eb5b80b323bcd815805bc3df4e/media/demo.mp4) · [Results & details](docs/community-projects.md#supermimic-retargeted) · [Quickstart](https://github.com/tianshuwu/supermimic-retargeted/blob/ff69a0e5305126eb5b80b323bcd815805bc3df4e/README.md#快速开始)

<a id="supermimic-wheel-legged-wheelbipe"></a>
<a id="supermimic-轮腿版wheelbipe"></a>

**[SuperMimic Wheel-Legged (wheelbipe)](https://github.com/RadiantForever/supermimic_wheelbipe)** · [![7 stars](assets/stars/1437090261.svg)](https://github.com/RadiantForever/supermimic_wheelbipe/stargazers)

**Stack:** Isaac Lab / PhysX · **By:** RadiantForever<br>
Wheelbipe forward / yaw / leg-height control learned through world-model rollouts.

[Repository](https://github.com/RadiantForever/supermimic_wheelbipe) · [Demo](https://www.bilibili.com/video/BV1haxM6CEGm/) · [Results & details](docs/community-projects.md#supermimic-wheel-legged-wheelbipe) · [Setup](https://github.com/RadiantForever/supermimic_wheelbipe/blob/0bf3456299a9f754289da58dce6c97c46afd3f03/README.md#setup)

<a id="supermimic-e1"></a>

**[SuperMimic E1](https://github.com/wenconggan/SuperMimic_e1)** · [![5 stars](assets/stars/1430480272.svg)](https://github.com/wenconggan/SuperMimic_e1/stargazers)

**Stack:** Isaac Lab 3 / MuJoCo · **By:** wenconggan<br>
21-DoF E1 tracking with native MuJoCo playback and separate full-clip metrics.

[Repository](https://github.com/wenconggan/SuperMimic_e1) · [Demo](https://github.com/wenconggan/SuperMimic_e1/blob/d5fbe8f219c438b84633130652c5e6e74beff628/docs/assets/e1_random10_80s.mp4) · [Results & details](docs/community-projects.md#supermimic-e1) · [Setup](https://github.com/wenconggan/SuperMimic_e1/blob/d5fbe8f219c438b84633130652c5e6e74beff628/README.md#安装与资源)

<a id="supermimic-oli"></a>

**[SuperMimic Oli](https://github.com/liuskywalkerjskd/supermimic_oli)** · [![3 stars](assets/stars/1431102076.svg)](https://github.com/liuskywalkerjskd/supermimic_oli/stargazers)

**Stack:** Isaac Lab 3 · **By:** liuskywalkerjskd<br>
31-DoF Oli adaptation with 40-clip metrics and full-motion videos.

[Repository](https://github.com/liuskywalkerjskd/supermimic_oli) · [Demo](https://github.com/liuskywalkerjskd/supermimic_oli/blob/2dc90d90e89fb2e097e985c84c8b99a77708fa5f/results/oli_walk1_subject1_full.mp4) · [Results & details](docs/community-projects.md#supermimic-oli) · [Setup](https://github.com/liuskywalkerjskd/supermimic_oli/blob/2dc90d90e89fb2e097e985c84c8b99a77708fa5f/README.md#setup)

<a id="supermimic-on-apple-m5"></a>

**[SuperMimic on Apple M5](https://github.com/WXyuany/supermimic-m5)** · [![1 stars](assets/stars/1430927278.svg)](https://github.com/WXyuany/supermimic-m5/stargazers)

**Stack:** MuJoCo / PyTorch MPS · **By:** WXyuany<br>
Apple M5: MPS learning, CPU MuJoCo physics and released G1 weights.

[Repository](https://github.com/WXyuany/supermimic-m5) · [Demo](https://github.com/WXyuany/supermimic-m5/blob/42451591718e1a9a5ec601366997f47c0ad180a3/assets/videos/walk1_subject1.mp4) · [Results & details](docs/community-projects.md#supermimic-on-apple-m5) · [Run the released model](https://github.com/WXyuany/supermimic-m5/blob/42451591718e1a9a5ec601366997f47c0ad180a3/README.md#三步运行已训练模型)


<a id="inspired-experiments"></a>

### Inspired experiments (2)

<a id="flatworld--supermimic-2d"></a>
<a id="-flatworld--supermimic-2d"></a>

**[FlatWorld · SuperMimic-2D](https://github.com/swaggyliu/FlatWorld)** · [![43 stars](assets/stars/1284715083.svg)](https://github.com/swaggyliu/FlatWorld/stargazers) · ⭐ Maintainer’s Pick

**Stack:** FlatWorld / 2D · **By:** swaggyliu<br>
2D multi-skill humanoid tracking to explore shared world-model learning.

[Repository](https://github.com/swaggyliu/FlatWorld) · [Demo](https://github.com/swaggyliu/FlatWorld/blob/886dad634c44ed652eea951be62370478f367d8b/docs/media/promo_supermimic.mp4) · [Results & details](docs/community-projects.md#flatworld--supermimic-2d) · [Quickstart](https://github.com/swaggyliu/FlatWorld/blob/c0f262d52e6492705079928ac69e453c775daeed/supermimic2d/README.md#quick-start)

<a id="g05--supermimic-style-steering"></a>

**[G0.5 · SuperMimic-style Steering](https://github.com/azizkhadraoui/g05)** · [![0 stars](assets/stars/1425368329.svg)](https://github.com/azizkhadraoui/g05/stargazers)

**Stack:** G0.5 / LIBERO · **By:** azizkhadraoui<br>
SuperMimic-style VLA steering and direct-policy fine-tuning failures on LIBERO.

[Repository](https://github.com/azizkhadraoui/g05) · [Demo](https://github.com/azizkhadraoui/g05/blob/e3de0de50db7d90068483e2d30f2eacd781300b4/README.md) · [Results & details](docs/community-projects.md#g05--supermimic-style-steering) · [Experiment code](https://github.com/azizkhadraoui/g05/blob/e3de0de50db7d90068483e2d30f2eacd781300b4/jobs/119_smsteer.py)

<!-- END GENERATED PROJECTS -->

## Original SuperMimic

**[SuperMimic: Scaling Humanoid Whole-Body Control with One Differentiable World Model](https://arxiv.org/abs/2610.28480)** — Qiayuan Liao, Yiyang Shao, Junfeng Long, Kevin Zakka, Roberto Horowitz, Pieter Abbeel, and Koushil Sreenath. **UC Berkeley · CoRL 2026 Oral.**

The original method fits a shared dynamics model and improves motion-tracking policies through short imagined rollouts. [Paper](https://arxiv.org/abs/2610.28480) · [Official website](https://supermimic.github.io/) · [Interactive demo](https://supermimic.github.io/demo/) · [Method, reported results and full official gallery](docs/original-supermimic.md).

<p align="center"><a href="https://supermimic.github.io/media/real/real_bay-wide.mp4"><img src="assets/official/real-g1-wide.gif" width="480" alt="Official SuperMimic real-G1 demonstration"></a><br><sub>Official author footage · <a href="assets/official/README.md">Media credits</a></sub></p>

## Related methods and baselines

These works provide methodological background or comparison points; they are separate research projects.

| Work | Connection | Primary resources |
| --- | --- | --- |
| **SuperTrack** (2021) | Earlier character motion tracking through a learned differentiable world model and gradient-based control learning. | [Author explanation](https://www.ubisoft.com/en-us/studio/laforge/news/7fMzaMaDgnd0gqPsCaJZYb/supertrack-motion-tracking-for-physically-simulated-characters-using-supervised-learning) · [Paper](https://staticctf.ubisoft.com/J3yJr34U2pZ2Ieem48Dwy9uqj5PNUQTn/OXYoOEqVwwtxSMiPzMIva/302e9a76da0b1f95ab62d6c766179868/SuperTrack.pdf) |
| **BeyondMimic** (2025) | Humanoid motion tracking and guided diffusion control; `supermimic_vibed` references its actuator and task conventions. | [Project](https://beyondmimic.github.io/) · [Paper](https://arxiv.org/abs/2508.08241) |
| **SONIC** (2025) | Large-scale humanoid motion tracking; the original SuperMimic work compares against a released SONIC checkpoint. | [Project](https://nvlabs.github.io/GEAR-SONIC/) · [Paper](https://arxiv.org/abs/2511.07820) · [Code](https://github.com/NVlabs/GR00T-WholeBodyControl) |

## Data and learning resources

- [LAFAN1 retargeting dataset](https://huggingface.co/datasets/lvhaidong/LAFAN1_Retargeting_Dataset) — G1 motion assets used by `supermimic_vibed`, UniSuperMimic, and SuperMimic-Reproduced. Follow each repository's preparation instructions and the dataset's own terms.
- [BONES-SEED](https://huggingface.co/datasets/bones-studio/seed) — the motion-data source used for the original paper's large-scale benchmark. The raw dataset and paper-filtered evaluation set have different counts. Access requires accepting the dataset's terms on Hugging Face.
- [Official interactive demo](https://supermimic.github.io/demo/) — explore the original policy in the browser before choosing a training stack.
- [Official method explanation](https://supermimic.github.io/#loop) — simulator collection, model fitting, and policy learning.
- [InstinctMJ releases](https://github.com/project-instinct/InstinctMJ/releases) — upstream distribution of task data and model assets; check the release description for the relevant branch and task.

## Contributing

Have a new implementation, extension, tutorial, or demo? Open a pull request using the [contribution guide](CONTRIBUTING.md). Include the original source, the relationship to SuperMimic, the relevant branch, and evidence for any result you quote.

<a id="ref2dex--dex-contact-mbrl"></a>

[Archived entries](docs/archived-projects.md) retain historical records for repositories currently unavailable to the public.

## Citation

When building on the method, cite the **original SuperMimic paper** and credit the implementation you use. BibTeX below follows the [official project](https://supermimic.github.io/#cite):

```bibtex
@inproceedings{liao2026supermimic,
  title     = {{SuperMimic}: Scaling Humanoid Whole-Body Control
               with One Differentiable World Model},
  author    = {Liao, Qiayuan and Shao, Yiyang and Long, Junfeng and
               Zakka, Kevin and Horowitz, Roberto and Abbeel, Pieter and
               Sreenath, Koushil},
  booktitle = {Conference on Robot Learning (CoRL)},
  year      = {2026}
}
```

## Acknowledgements and license

Thanks to the original SuperMimic authors and all community maintainers. The presentation of this list is inspired by [Awesome Nano Banana Images](https://github.com/PicoTrex/Awesome-Nano-Banana-images) and [Awesome World Models](https://github.com/knightnemo/Awesome-World-Models).

The original curation text in this collection is released under [CC0 1.0](LICENSE). Third-party code, papers, datasets, and media retain their respective rights and terms. This includes the [original paper figure and official video previews](assets/official/README.md) stored in this repository; they are not covered by this collection's CC0 dedication. [Community media previews and credits](assets/community/README.md) follow the same attribution rule.

## Star History

<p align="center"><b>If this list helps you, consider <a href="https://github.com/miao-org/awesome-supermimic">starring the repository</a> so more people can discover it.</b></p>

<p align="center">
  <a href="https://star-history.com/#miao-org/awesome-supermimic&Date">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=miao-org/awesome-supermimic&type=Date&theme=dark">
      <img src="https://api.star-history.com/svg?repos=miao-org/awesome-supermimic&type=Date" alt="Star history chart for miao-org/awesome-supermimic" width="100%">
    </picture>
  </a>
</p>
