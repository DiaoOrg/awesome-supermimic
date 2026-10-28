<div align="center">

# Awesome SuperMimic

[![Awesome](https://awesome.re/badge.svg)](https://github.com/sindresorhus/awesome) [![Paper](https://img.shields.io/badge/arXiv-2610.28480-b31b1b.svg)](https://arxiv.org/abs/2610.28480) [![License: CC0](https://img.shields.io/badge/License-CC0_1.0-blue.svg)](LICENSE) [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

**A curated collection of SuperMimic implementations, extensions, demos, and resources.**

English · [简体中文](README_zh-CN.md)

[Original paper](https://arxiv.org/abs/2610.28480) · [Official website](https://supermimic.github.io/) · [Interactive demo](https://supermimic.github.io/demo/) · [Community projects](#community-projects)

</div>

<p align="center">
  <a href="https://supermimic.github.io/media/world-model/wm_on.mp4"><img src="assets/official/world-model.gif" alt="Official SuperMimic world-model predictions in blue overlaid on simulator motion" width="100%"></a><br>
  <b>World-model predictions</b>
</p>

<table>
  <tr>
    <td width="50%" align="center">
      <a href="https://supermimic.github.io/media/hero/hero_montage_desktop.mp4"><img src="assets/official/simulation-wide.gif" alt="Official SuperMimic simulation: G1 flips, rolls, and dances" width="100%"></a><br>
      <b>Simulation</b>
    </td>
    <td width="50%" align="center">
      <a href="https://supermimic.github.io/media/real/real_bay-wide.mp4"><img src="assets/official/real-g1-wide.gif" alt="Official SuperMimic real G1 performing a side roll and a flip by the bay" width="100%"></a><br>
      <b>Real G1</b>
    </td>
  </tr>
</table>

<p align="center"><sub>Original footage: <a href="https://supermimic.github.io/">SuperMimic authors</a> · Click a preview for the full video · <a href="assets/official/README.md">Media credits</a></sub></p>

Start with the original work below, then choose an implementation by framework and task. This is a community-maintained resource list; the linked implementations are credited to their own authors.

## Contents

- [Original SuperMimic](#original-supermimic)
- [Community projects](#community-projects)
- [Related methods and baselines](#related-methods-and-baselines)
- [Data and learning resources](#data-and-learning-resources)
- [Contributing](#contributing)
- [Citation](#citation)
- [Acknowledgements and license](#acknowledgements-and-license)

## Original SuperMimic

**[SuperMimic: Scaling Humanoid Whole-Body Control with One Differentiable World Model](https://arxiv.org/abs/2610.28480)**<br>
Qiayuan Liao, Yiyang Shao, Junfeng Long, Kevin Zakka, Roberto Horowitz, Pieter Abbeel, and Koushil Sreenath.<br>
**UC Berkeley · CoRL 2026 Oral**

[Paper](https://arxiv.org/abs/2610.28480) · [PDF](https://arxiv.org/pdf/2610.28480) · [Project](https://supermimic.github.io/) · [Video](https://supermimic.github.io/media/real/film-1080.mp4) · [Browser demo](https://supermimic.github.io/demo/)

SuperMimic learns shared humanoid dynamics from simulator transitions and improves a motion-tracking policy through short imagined rollouts. The world model and policy are updated in the same training loop; policy gradients pass through the learned model. [Method overview](https://supermimic.github.io/#loop).

<p align="center">
  <a href="https://arxiv.org/pdf/2610.28480v1#page=4">
    <img src="assets/official/training-loop.png" width="100%" alt="Original SuperMimic Figure 2: data collection, world-model fitting and policy improvement share a replay buffer; dashed arrows show gradients">
  </a>
</p>
<p align="center">
  <sub>Original paper, Figure 2 · <a href="https://arxiv.org/pdf/2610.28480v1#page=4">Framework, p. 4</a> · <a href="https://arxiv.org/pdf/2610.28480v1#page=15">Algorithm A.1, p. 15</a></sub>
</p>

The world model is fit on **8-step replay windows**; the policy and critic learn from **32-step imagined rollouts**. During the policy update, model weights stay fixed while gradients pass through the model to the policy. Blue dashed arrows show gradients; ❄️ marks frozen weights and 🔥 marks weights being trained in that phase.

The authors report surpassing SONIC's released-checkpoint return after **3 hours on one H100**, with **25 / 129,514 failed motions**, and **0 / 129,514** after 9.8 hours on two H100s. These are training-motion coverage results, with different training hardware and data from SONIC. See the [official results and compute accounting](https://supermimic.github.io/#compute).

**Official code status — checked 2026-10-26:** the official website links the paper, video, and browser demo, but does not link a training-code repository. The projects below are community implementations and extensions.

## Community projects

**35 community projects**, grouped by purpose. Existing descriptions were checked against upstream documentation and selected source files on **2026-10-26**; ScaleBFM_Plus, SuperMimic Mjlab, SuperMimic for Robot Manipulation and Muscle SuperMimic were checked on **2026-10-27**; In-Hand Rotation mjlab on **2026-10-28**. Each entry links to the reviewed source revision. Results and demos are upstream reports; this list has not independently rerun the experiments.

- 🚀 **[Real-robot deployment and Sim2Real](#real-robot-deployment-and-sim2real)** — **2 projects** · Follow real-robot runtimes and sim-to-real transfer paths.
- 🔬 **[Independent reproductions](#independent-reproductions)** — **4 projects** · Reproduce and evaluate the original method.
- 🧩 **[Method and morphology variants](#method-and-morphology-variants)** — **4 projects** · Explore algorithm changes, robot-morphology adaptations and focused control studies.
- 👁️ **[Perception, terrain and quadrupeds](#perception-terrain-and-quadrupeds)** — **3 projects** · Find vision, height-scan, terrain and quadruped task adaptations.
- 🦾 **[Manipulation and dexterous hands](#manipulation-and-dexterous-hands)** — **4 projects** · Find arm, hand and object-interaction tasks.
- 💪 **[Muscle, interaction and diagnostics](#muscle-interaction-and-diagnostics)** — **3 projects** · Explore muscle-actuated bodies, physical interaction and contact-focused studies.
- 🛠️ **[Frameworks and training stacks](#frameworks-and-training-stacks)** — **6 projects** · Find integrations and reusable training or evaluation stacks.
- 🤖 **[Robot porting and retargeting](#robot-porting-and-retargeting)** — **6 projects** · Find robot-, simulator- or hardware-specific ports and retargeting tools.
- 💡 **[Inspired experiments](#inspired-experiments)** — **3 projects** · Transfer ideas to other control problems.

## Real-robot deployment and Sim2Real

Real-robot runtimes and sim-to-real transfer paths.

### SuperMimic-Repro-Sim2Real

[Repository](https://github.com/NJU-R-L-Group-Embodied-Lab/SuperMimic-Repro-Sim2Real) · [Quickstart](https://github.com/NJU-R-L-Group-Embodied-Lab/SuperMimic-Repro-Sim2Real/blob/99d310d5460333aabe853337b1d55ee27940a3fe/README.md#快速开始) · [G1 deployment](https://github.com/NJU-R-L-Group-Embodied-Lab/SuperMimic-Repro-Sim2Real/blob/99d310d5460333aabe853337b1d55ee27940a3fe/docs/DEPLOY_G1.md)

- **By NJU R&amp;L Group Embodied Lab.** Extends the CuboiLeo mjlab baseline with custom dance/video-motion tools, ONNX export and G1 deployment through native MuJoCo and the Unitree SDK.
- **Upstream report:** Publishes a roughly **46-second real-G1 dance** combining four motion segments, alongside pretrained models and the original video.
- **Useful context:** The README separates paper-style observations from anchor-augmented training. The latter requires global-relative information unavailable in the demonstrated hardware setup. [Source snapshot](https://github.com/NJU-R-L-Group-Embodied-Lab/SuperMimic-Repro-Sim2Real/blob/99d310d5460333aabe853337b1d55ee27940a3fe/README.md).

<a href="https://github.com/NJU-R-L-Group-Embodied-Lab/SuperMimic-Repro-Sim2Real/releases/download/v1.0/shanshenbu_real_robot_v3.mp4"><img src="https://raw.githubusercontent.com/NJU-R-L-Group-Embodied-Lab/SuperMimic-Repro-Sim2Real/99d310d5460333aabe853337b1d55ee27940a3fe/docs/assets/shanshenbu_demo.gif" width="480" alt="Real G1 · dance with human reference"></a><br><sub>Real G1 · dance with human reference</sub>

<br>

### SuperMimic G1 Deployment

[Repository](https://github.com/KyrieYoung926/supermimic_deploy) · [MuJoCo guide](https://github.com/KyrieYoung926/supermimic_deploy/blob/7e63e3bbd5150d55afbdece28278781800f3ed21/README.md#3-run-in-mujoco) · [Real-G1 guide](https://github.com/KyrieYoung926/supermimic_deploy/blob/7e63e3bbd5150d55afbdece28278781800f3ed21/README.md#4-run-on-the-real-g1)

- **By KyrieYoung926.** A deployment runtime for a SuperMimic-Reproduced policy on the 29-DoF G1, using ONNX Runtime, MuJoCo and Unitree SDK2.
- **What it provides:** Provides both simulation and real-G1 demos, with separate guides for fetching deployment assets and running the policy on each target.
- **Useful context:** This repository covers deployment, not a new training benchmark. Motion data, model weights and robot assets retain their own terms beyond the code license. [Source snapshot](https://github.com/KyrieYoung926/supermimic_deploy/blob/7e63e3bbd5150d55afbdece28278781800f3ed21/README.md).

<a href="https://github.com/KyrieYoung926/supermimic_deploy"><img src="https://raw.githubusercontent.com/KyrieYoung926/supermimic_deploy/7e63e3bbd5150d55afbdece28278781800f3ed21/media/deploy_real.gif" width="480" alt="Real G1 · upstream deployment demo"></a><br><sub>Real G1 · upstream deployment demo</sub>

<br>

## Independent reproductions

Reimplementations of the original method, with training, evaluation and reproduction notes.

### supermimic_vibed

[Repository](https://github.com/zita-ch/supermimic_vibed) · [Setup and usage](https://github.com/zita-ch/supermimic_vibed/blob/a1508d42c9d1699a52e8233ab16d08c488441ab9/README.md#setup) · [Results](https://github.com/zita-ch/supermimic_vibed/blob/a1508d42c9d1699a52e8233ab16d08c488441ab9/README.md#result-lafan1-40-clips-one-rtx-pro-6000-blackwell)

- **By Chong Zhang.** An independent G1 implementation on Isaac Lab 3, with a kit-less setup, training, full-clip evaluation and rendering tools.
- **Upstream report:** On 40 LAFAN1 clips, normalized return **0.829** and **0 / 40 failures** after **1.47 hours on one RTX PRO 6000 Blackwell**.
- **Useful context:** The author describes it as a rapid, unreviewed reproduction. Documented deviations include disabled self-collisions, bf16 MLP computation and an extra reference-root orientation input. [Source snapshot](https://github.com/zita-ch/supermimic_vibed/blob/a1508d42c9d1699a52e8233ab16d08c488441ab9/README.md).

<a href="https://github.com/zita-ch/supermimic_vibed"><img src="https://raw.githubusercontent.com/zita-ch/supermimic_vibed/a1508d42c9d1699a52e8233ab16d08c488441ab9/results/supermimic_lafan1_highlight.gif" width="480" alt="Simulation · LAFAN1 highlights"></a><br><sub>Simulation · LAFAN1 highlights</sub>

<br>

### SuperMimic-Reproduced

[Repository](https://github.com/CuboiLeo/SuperMimic-Reproduced) · [Setup](https://github.com/CuboiLeo/SuperMimic-Reproduced/blob/d9be385b3eeb13a638fb33fb200d3bfd9be9839f/README.md#环境) · [Experiment log](https://github.com/CuboiLeo/SuperMimic-Reproduced/blob/d9be385b3eeb13a638fb33fb200d3bfd9be9839f/docs/EXPERIMENTS.md)

- **By CuboiLeo.** A from-scratch mjlab implementation for G1, with Chinese reproduction notes, LAFAN1/BONES-SEED processing, multi-GPU training and an interactive replay viewer.
- **Upstream report:** With anchor-relative observations, one RTX 5090 reaches LAFAN1 return **0.824**, **5 / 40 failures** at **1.66 hours**, and **0.904**, **3 / 40 failures** at **3.3 hours**.
- **Useful context:** The paper-observation run reports **0.56** and **9 / 40 failures** at 1.8 hours. These observation settings are not equivalent; the reported BONES-SEED scores use a 2,000-motion evaluation subset. [Source snapshot](https://github.com/CuboiLeo/SuperMimic-Reproduced/blob/d9be385b3eeb13a638fb33fb200d3bfd9be9839f/README.md).

<a href="https://github.com/CuboiLeo/SuperMimic-Reproduced/blob/d9be385b3eeb13a638fb33fb200d3bfd9be9839f/README.md"><img src="assets/community/reproduced-results.png" width="720" alt="Report screenshot · paper-style and anchor-relative observations"></a><br><sub>Report screenshot · paper-style and anchor-relative observations</sub>

<br>

### supermimic_vibe

[Repository](https://github.com/dhmbb2/supermimic_vibe) · [Setup](https://github.com/dhmbb2/supermimic_vibe/blob/072f0910dadc9d95c720e625b546120e9ce917c9/README.md#setup) · [Results log](https://github.com/dhmbb2/supermimic_vibe/blob/072f0910dadc9d95c720e625b546120e9ce917c9/notes/RESULTS.md)

- **By dhmbb2.** An independent G1 reproduction in mjlab, covering PPO-Sim/PPO-WM comparisons, horizon and critic ablations, push recovery and velocity-control experiments.
- **Upstream report:** On one RTX A6000, LAFAN1 normalized return reaches **0.833 at 1.34 hours** and **0.946 with 0 / 40 failures at 12 hours**, using complete deterministic clip evaluation.
- **Useful context:** The experiment log distinguishes reproduced, partial and pending results. BONES-SEED remains data-gated, hardware transfer is out of scope, and the A6000 timings are not H100 timings. [Source snapshot](https://github.com/dhmbb2/supermimic_vibe/blob/072f0910dadc9d95c720e625b546120e9ce917c9/README.md).

<a href="https://github.com/dhmbb2/supermimic_vibe/blob/072f0910dadc9d95c720e625b546120e9ce917c9/README.md"><img src="assets/community/vibe-results.png" width="720" alt="Report screenshot · reproduction and ablations on one RTX A6000"></a><br><sub>Report screenshot · reproduction and ablations on one RTX A6000</sub>

<br>

### SuperMimic Mjlab

[Repository](https://github.com/Breezewrf/supermimic_mjlab) · [Setup](https://github.com/Breezewrf/supermimic_mjlab/blob/23c76cad5bf41110709c7f929b54c1da1be6b248/doc/setup_en.md) · [Ablations and checkpoint](https://github.com/Breezewrf/supermimic_mjlab/blob/23c76cad5bf41110709c7f929b54c1da1be6b248/README.md#ablation-results-and-released-checkpoint)

- **By Breezewrf.** An independent SuperMimic reproduction for Unitree G1 in mjlab, with a complete performance-improvement ablation study, multi-motion training, full-clip evaluation and released policy/world-model checkpoints.
- **Upstream report:** On all 40 LAFAN motions, the selected checkpoint achieves **40 / 40 successful motions**, **100% mean completion** and **0.8528 normalized return** in fixed-start, full-clip deterministic evaluation. Training for **15,000 iterations takes approximately 4 hours on one RTX A6000 48 GB**, with 4,096 environments and FP32 networks.
- **Useful context:** Documents the full progression from Actor/Critic input normalization through a torso-frame motion orientation anchor, world-model normalization and a corrected cosine learning-rate schedule: mean normalized return **0.6016 → 0.8130 → 0.8504 → 0.8526** at 15,000 iterations over all 40 motions. The final rerun mean is distinct from the selected checkpoint score above. [Source snapshot](https://github.com/Breezewrf/supermimic_mjlab/blob/23c76cad5bf41110709c7f929b54c1da1be6b248/README.md).

<a href="https://github.com/Breezewrf/supermimic_mjlab/blob/23c76cad5bf41110709c7f929b54c1da1be6b248/doc/assets/evaluation.png"><img src="https://raw.githubusercontent.com/Breezewrf/supermimic_mjlab/23c76cad5bf41110709c7f929b54c1da1be6b248/doc/assets/evaluation.png" width="720" alt="Evaluation dashboard · SuperMimic Mjlab return, success and per-motion completion"></a><br><sub>Upstream evaluation dashboard · return, success and per-motion completion · configuration ablations linked above</sub>

<br>

## Method and morphology variants

Algorithm changes, multi-robot morphology adaptations and focused control studies.

### MorphMimic

[Repository](https://github.com/lzyang2000/morphmimic) · [Setup](https://github.com/lzyang2000/morphmimic/blob/2e35049e9519e511889ef987e4acde55d4f5b017/README.md#setup) · [Method differences](https://github.com/lzyang2000/morphmimic/blob/2e35049e9519e511889ef987e4acde55d4f5b017/README.md#differences-from-supermimic)

- **By Lizhi Yang et al.** Extends SuperMimic in mjlab to share a world model, a policy, or both across G1, X2 Ultra and T2, conditioning the networks on robot morphology.
- **What it provides:** Supports full-motion tracking and sparse five-point goals for the pelvis, wrists and ankles; the project includes a browser demo and teleoperation/deployment instructions.
- **Useful context:** Robots are mapped to a common 29-joint layout. The README documents changes to termination modeling, normalization, warm-up and actuator-delay randomization. [Source snapshot](https://github.com/lzyang2000/morphmimic/blob/2e35049e9519e511889ef987e4acde55d4f5b017/README.md).

<a href="https://lzyang2000.github.io/morphmimic/static/videos/dance_hiphop_shuffle_sequence_v_001_R_003__A306.mp4"><img src="assets/community/morphmimic.gif" width="480" alt="Simulation · one shared policy for G1 / X2 Ultra / T2"></a><br><sub>Simulation · one shared policy for G1 / X2 Ultra / T2</sub>

[Video](https://lzyang2000.github.io/morphmimic/static/videos/morphmimic.mp4) · [Interactive demo](https://lzyang2000.github.io/morphmimic/demo/)

<br>

### allmimic

[Repository](https://github.com/Shimingyi/allmimic) · [Install](https://github.com/Shimingyi/allmimic/blob/cb334ff674b2f57248f33f8c21b7fb526fbdf8cc/README.md#install) · [Results](https://github.com/Shimingyi/allmimic/blob/cb334ff674b2f57248f33f8c21b7fb526fbdf8cc/README.md#results)

- **By Shimingyi.** Builds on supermimic_vibe for G1 in mjlab, mixing residual upper-body actions with absolute leg actions, weighting world-model losses and balancing motion sampling.
- **Upstream report:** With the recommended preset on one RTX 4090, full-length LAFAN1 evaluation reports **0 / 40 failures and return 0.91 after 0.83 hours**; training time excludes evaluation.
- **Useful context:** The recommended preset changes the method and data sampling. The 306-hard-motion-only run and full BONES-SEED training are separate experiments. [Source snapshot](https://github.com/Shimingyi/allmimic/blob/cb334ff674b2f57248f33f8c21b7fb526fbdf8cc/README.md).

<a href="https://github.com/Shimingyi/allmimic"><img src="https://raw.githubusercontent.com/Shimingyi/allmimic/cb334ff674b2f57248f33f8c21b7fb526fbdf8cc/assets/challenge_cases.gif" width="480" alt="Simulation · challenging motion clips"></a><br><sub>Simulation · challenging motion clips</sub>

<br>

### SuperMimic on LocoMuJoCo

[Repository](https://github.com/Alchedata/supermimic-locomujoco) · [Setup](https://github.com/Alchedata/supermimic-locomujoco/blob/cc1375d48a38bde062d088ffd132122e0cd7b7da/README.md#setup) · [Results](https://github.com/Alchedata/supermimic-locomujoco/blob/cc1375d48a38bde062d088ffd132122e0cd7b7da/README.md#results-at-5k)

- **By Alchedata.** Ports the method to H1 with JAX and LocoMuJoCo, comparing an MLP baseline with residual-expert, action-sensitivity and trust-aware world models.
- **Upstream report:** Publishes fixed 5,000-iteration checkpoints evaluated over 160 episodes, including both successful seeds and a residual-expert run that became stuck with saturated actions.
- **Useful context:** The reward is LocoMuJoCo episode return, not the G1 normalized tracking score. Recovery interventions and their continuation controls are recorded separately. [Source snapshot](https://github.com/Alchedata/supermimic-locomujoco/blob/cc1375d48a38bde062d088ffd132122e0cd7b7da/README.md).

<a href="https://github.com/Alchedata/supermimic-locomujoco/blob/cc1375d48a38bde062d088ffd132122e0cd7b7da/README.md"><img src="assets/community/locomujoco-results.png" width="720" alt="Report screenshot · fixed 5k checkpoints, 160 evaluation episodes"></a><br><sub>Report screenshot · fixed 5k checkpoints, 160 evaluation episodes</sub>

<br>

### Rethinking SuperMimic

[Repository](https://github.com/btx0424/rethinking-supermimic) · [Installation](https://github.com/btx0424/rethinking-supermimic/blob/ecdaeb6a916a16cf7eb69b19226c17be31a6bc27/README.md#installation) · [Implementation comparison](https://github.com/btx0424/rethinking-supermimic/blob/ecdaeb6a916a16cf7eb69b19226c17be31a6bc27/README.md#ours-the-paper-and-supermimic_vibed)

- **By btx0424.** Studies goal conditioning for G1 in mjlab: concatenating the goal with proprioception versus using FiLM to modulate the policy layers.
- **Useful context:** Provides configurable observations, anchor choices and Viser playback. Its implementation table explains differences from the paper and supermimic_vibed, including self-collisions and observation inputs. [Source snapshot](https://github.com/btx0424/rethinking-supermimic/blob/ecdaeb6a916a16cf7eb69b19226c17be31a6bc27/README.md).

<a href="https://github.com/btx0424/rethinking-supermimic/blob/ecdaeb6a916a16cf7eb69b19226c17be31a6bc27/README.md"><img src="assets/community/rethinking-comparison.png" width="720" alt="Implementation table excerpt · first three design choices; click for the full comparison"></a><br><sub>Implementation table excerpt · first three design choices; click for the full comparison</sub>

<br>

## Perception, terrain and quadrupeds

Vision, height-scan, terrain and quadruped task adaptations.

### InstinctMJ · SuperMimic

[Repository](https://github.com/project-instinct/InstinctMJ/tree/supermimic) · [Method and results](https://github.com/project-instinct/InstinctMJ/blob/7ca851e002980011f24a1664011305d0ba94aefc/src/instinct_mj/rl/supermimic/README.md#results) · [Releases](https://github.com/project-instinct/InstinctMJ/releases)

- **By Project Instinct.** Extends the method to perceptive G1 tracking and goal-reaching parkour in mjlab / instinct_rl. The world model predicts robot state and depth-encoder latents; components are adapted from supermimic_vibed.
- **Upstream report:** **97% full-motion success** across **10 motions on 5 terrains** after **8,000 iterations / 3.2 hours on one RTX 3090**; one seed, 12–13 episodes per motion, camera noise enabled.
- **Useful context:** Use the **supermimic branch**. This is terrain tracking, distinct from flat-ground LAFAN1; external checkpoints require joint-order adaptation. Licensed CC BY-NC 4.0. [Source snapshot](https://github.com/project-instinct/InstinctMJ/blob/7ca851e002980011f24a1664011305d0ba94aefc/src/instinct_mj/rl/supermimic/README.md).

<a href="https://github.com/project-instinct/InstinctMJ/blob/7ca851e002980011f24a1664011305d0ba94aefc/src/instinct_mj/rl/supermimic/assets/world_model_simple.png"><img src="https://raw.githubusercontent.com/project-instinct/InstinctMJ/7ca851e002980011f24a1664011305d0ba94aefc/src/instinct_mj/rl/supermimic/assets/world_model_simple.png" width="720" alt="Method diagram · robot-state and visual-latent prediction"></a><br><sub>Method diagram · robot-state and visual-latent prediction</sub>

<br>

### SuperMimic-perceptive

[Repository](https://github.com/mode1223345/SuperMimic-perceptive) · [Method](https://github.com/mode1223345/SuperMimic-perceptive/blob/3d38bacbaf5bee7e782bdada6a6da678264d0bfa/Ae.md) · [Progress](https://github.com/mode1223345/SuperMimic-perceptive/blob/3d38bacbaf5bee7e782bdada6a6da678264d0bfa/Progress.md)

- **By mode1223345.** Builds on supermimic_vibed in Isaac Lab 3, pretraining a heightmap autoencoder and freezing one shared encoder for the actor, critic and world model.
- **What it provides:** Documents four flat-ground/step-terrain control experiments and separate reconstruction checks; the published control comparisons remain in progress.
- **Useful context:** Maps come from simulator ground truth. Real-depth reconstruction and hardware perception are not integrated, and inherited baseline scores do not establish gains from the encoder. [Source snapshot](https://github.com/mode1223345/SuperMimic-perceptive/blob/3d38bacbaf5bee7e782bdada6a6da678264d0bfa/README.md).

<a href="https://github.com/mode1223345/SuperMimic-perceptive/blob/3d38bacbaf5bee7e782bdada6a6da678264d0bfa/results/Curves.png"><img src="https://raw.githubusercontent.com/mode1223345/SuperMimic-perceptive/3d38bacbaf5bee7e782bdada6a6da678264d0bfa/results/Curves.png" width="720" alt="Training curves · 2026-10-24 snapshot; control comparisons in progress"></a><br><sub>Training curves · 2026-10-24 snapshot; control comparisons in progress</sub>

<br>

### Go2-SuperMimic

[Repository](https://github.com/Zhengtianjin/go2-supermimic) · [Quickstart](https://github.com/Zhengtianjin/go2-supermimic/blob/054a13c13285a1c94b2e69dc8ac7331f9a8c71cf/README.md#-quickstart) · [Pretrained policies](https://github.com/Zhengtianjin/go2-supermimic/blob/054a13c13285a1c94b2e69dc8ac7331f9a8c71cf/README.md#pretrained-policies)

- **By Zhengtianjin.** Adapts SuperMimic to Unitree Go2 chase-and-dodge tasks in mjlab, covering flat ground, obstacles and terrain with LiDAR or height-scan inputs.
- **What it provides:** Publishes separate flat, obstacle and terrain actors, plus evaluation and recording tools. Actor-only downloads support playback; resuming training also needs the world model and critic.
- **Useful context:** Simulation only, with ground-truth target perception. The released terrain policy still has falls and bar collisions under the hardest settings. [Source snapshot](https://github.com/Zhengtianjin/go2-supermimic/blob/054a13c13285a1c94b2e69dc8ac7331f9a8c71cf/README.md).

<a href="https://github.com/Zhengtianjin/go2-supermimic"><img src="https://raw.githubusercontent.com/Zhengtianjin/go2-supermimic/054a13c13285a1c94b2e69dc8ac7331f9a8c71cf/resources/terrain.gif" width="480" alt="Simulation · Go2 terrain chase and dodge"></a><br><sub>Simulation · Go2 terrain chase and dodge</sub>

<br>

## Manipulation and dexterous hands

Arm, hand and object-interaction tasks, with dexterous manipulation grouped here. The exploratory Ref2Dex contact-control project is listed under [Inspired experiments](#inspired-experiments).

### Dex SuperMimic

[Repository](https://github.com/CumulusAlpha/Dex-Supermimic) · [Installation](https://github.com/CumulusAlpha/Dex-Supermimic/blob/5ca57628af3666a9b2878c00f461f43d6edb5b61/README.md#download-and-installation) · [Checkpoint](https://github.com/CumulusAlpha/Dex-Supermimic/releases/tag/pretrained-wuji-v1)

- **By CumulusAlpha.** Adapts world-model-based policy training to in-hand cube reorientation with Wuji Hand 2, using mjlab / MuJoCo Warp and the InstinctMJ task framework.
- **What it provides:** Provides the model_8000.pt checkpoint and a Viser viewer. Hand assets are bundled with the package; the pretrained checkpoint is downloaded separately from Releases.
- **Useful context:** This is a dexterous-manipulation adaptation with a different task and reward from humanoid motion tracking. [Source snapshot](https://github.com/CumulusAlpha/Dex-Supermimic/blob/5ca57628af3666a9b2878c00f461f43d6edb5b61/README.md).

<a href="https://github.com/CumulusAlpha/Dex-Supermimic/blob/5ca57628af3666a9b2878c00f461f43d6edb5b61/teaser.jpg"><img src="https://raw.githubusercontent.com/CumulusAlpha/Dex-Supermimic/5ca57628af3666a9b2878c00f461f43d6edb5b61/teaser.jpg" width="480" alt="Simulation screenshot · Wuji Hand 2 cube reorientation"></a><br><sub>Simulation screenshot · Wuji Hand 2 cube reorientation</sub>

<br>

### SuperMimic for Robot Manipulation

[Repository](https://github.com/emoPointer/supermimic_manipulation) · [Setup](https://github.com/emoPointer/supermimic_manipulation/blob/810e5768c50117d2fec75f20f9e643a11cd0882b/README.md#install) · [Results](https://github.com/emoPointer/supermimic_manipulation/blob/810e5768c50117d2fec75f20f9e643a11cd0882b/README.md#results)

- **By Zhiqiang Zhou (emoPointer).** Adapts SuperMimic to state-based manipulation with a simulated ARX5 arm in mjlab / MuJoCo Warp across the Lemon, BoxInBin and MugHang tasks.
- **Upstream report:** Held-out reset banks with 256 complete episodes per task at 4,000 iterations reach **100.0%** Lemon, **94.9%** BoxInBin and **96.9%** MugHang success; the runs take **1.8 / 1.9 / 2.8 hours on one A100 80 GB** while sharing the GPU.
- **Useful context:** OmniReset-style reset categories shorten the effective horizon, and contact-based success tests use differentiable geometric surrogates during imagination. The policy observes low-dimensional state only; released checkpoints and reset banks are on Hugging Face. [Source snapshot](https://github.com/emoPointer/supermimic_manipulation/blob/810e5768c50117d2fec75f20f9e643a11cd0882b/README.md).

<a href="https://github.com/emoPointer/supermimic_manipulation"><img src="https://raw.githubusercontent.com/emoPointer/supermimic_manipulation/810e5768c50117d2fec75f20f9e643a11cd0882b/docs/media/lemon.gif" width="480" alt="Simulation · ARX5 Lemon task with two held-out resets"></a><br><sub>Simulation · ARX5 Lemon task · two held-out resets</sub>

<br>

### Humanoid Mimic · SuperMimic

[Repository](https://github.com/shuayyy/humanoid-amp-ppo) · [Quickstart](https://github.com/shuayyy/humanoid-amp-ppo/blob/4889389118e0c88d3945dff54d2cd3f992ed815e/README.md#quickstart) · [Results and protocol](https://github.com/shuayyy/humanoid-amp-ppo/blob/4889389118e0c88d3945dff54d2cd3f992ed815e/docs/supermimic/RESULTS.md)

- **By shuayyy.** Compares SuperMimic and PPO-Sim on shared G1 walking, squatting and box-lifting tasks in mjlab; the repository also contains a separate AMP-PPO stack.
- **Upstream report:** Box-lift success reaches **100% at 31 million environment steps**, reported for two SuperMimic seeds with 64 randomized evaluation episodes; success means finishing within 10 cm of the reference box height.
- **Useful context:** Those SuperMimic scores used clean observations. The newer evaluation adds observation noise, and the published checkpoints have not been re-evaluated under that setting. [Source snapshot](https://github.com/shuayyy/humanoid-amp-ppo/blob/4889389118e0c88d3945dff54d2cd3f992ed815e/README.md).

<a href="https://github.com/shuayyy/humanoid-amp-ppo/blob/4889389118e0c88d3945dff54d2cd3f992ed815e/assets/supermimic_vs_ppo_lift.mp4"><img src="https://raw.githubusercontent.com/shuayyy/humanoid-amp-ppo/4889389118e0c88d3945dff54d2cd3f992ed815e/assets/supermimic_vs_ppo_lift.gif" width="480" alt="Box lift · SuperMimic 12k / PPO-Sim 6k iterations"></a><br><sub>Box lift · SuperMimic 12k / PPO-Sim 6k iterations</sub>

<br>

### In-Hand Rotation mjlab

[Repository](https://github.com/Msornerrrr/in-hand-rotation-mjlab) · [Install](https://github.com/Msornerrrr/in-hand-rotation-mjlab/blob/0ab03eb2244b4a1a020d94ef38a4823bb9e15ba0/README.md#install) · [Results](https://github.com/Msornerrrr/in-hand-rotation-mjlab/blob/0ab03eb2244b4a1a020d94ef38a4823bb9e15ba0/README.md#results) · [Checkpoints](https://github.com/Msornerrrr/in-hand-rotation-mjlab/blob/0ab03eb2244b4a1a020d94ef38a4823bb9e15ba0/README.md#quick-start-the-released-policies)

- **By Msornerrrr.** Applies SuperMimic-style world-model policy learning (an MLP world model refit online, backpropagation through imagined rollouts, a TD(λ) critic and weight averaging) to the LEAP Hand in mjlab / MuJoCo Warp, next to PPO baselines on the same environments: palm-up cube yaw, SO(3) cube reorientation (PPO only) and palm-down fingertip rotation of 22 objects, on a servo model identified on the real hand. Checkpoints for both methods are released.
- **Upstream report:** On cube yaw, the world-model policy reaches PPO's level (≈0.26 reward/s) after **25 minutes and 18M env steps**, where PPO needs 6.5 hours and 262M, and ends at **0.292 vs 0.261**. On palm-down fingertip rotation (64 rollouts per object, 60 s, randomized pad friction 0.25–1.2), a joints-only world-model policy reaches **933°** rewarded yaw with **4.0%** drops, against **675° / 10.4%** for the deployed PPO student distilled from a teacher, and **944° / 2.1%** for the privileged PPO teacher.
- **Useful context:** World-model results are in simulation; the real-robot videos (yaw and SO(3)) show PPO policies. Fingertip numbers use the repository's own evaluation (rotation reward capped at 0.3 rad/s; a drop is 30 mm of drift). Single runs per configuration; wall-clock times are on one RTX 4090. [Source snapshot](https://github.com/Msornerrrr/in-hand-rotation-mjlab/blob/0ab03eb2244b4a1a020d94ef38a4823bb9e15ba0/README.md).

<a href="https://github.com/Msornerrrr/in-hand-rotation-mjlab"><img src="https://raw.githubusercontent.com/Msornerrrr/in-hand-rotation-mjlab/0ab03eb2244b4a1a020d94ef38a4823bb9e15ba0/assets/sim_fingertip.gif" width="480" alt="Simulation · palm-down fingertip rotation of a sphere, cube, cylinder and cuboid by a joints-only world-model policy"></a><br><sub>Simulation · palm-down fingertip rotation, joints-only world-model policy</sub>

<br>

## Muscle, interaction and diagnostics

Muscle-actuated bodies, physical interaction and contact-focused diagnostics.

### Muscle SuperMimic

[Repository](https://github.com/kaibohex/muscle-supermimic) · [Setup](https://github.com/kaibohex/muscle-supermimic/blob/b7c7cdd83e82399e057cb9d3f1b76f23ca022c7b/README.md#install) · [Status](https://github.com/kaibohex/muscle-supermimic/blob/b7c7cdd83e82399e057cb9d3f1b76f23ca022c7b/README.md#status)

- **By Kaibo He (kaibohex).** Extends SuperMimic to muscle-driven whole-body tracking on MS-Human-700 (700 muscles) and MyoFullBody (354 muscles) in mjlab / MuJoCo Warp.
- **Upstream report:** On MuscleMimic's 108 held-out KIT clips with 4,096 environments on one RTX 5090, MS-Human-700 reaches **0.91 normalized return after 10.1 hours** (iteration 16k, **104 / 108 tracked**); MyoFullBody reaches **0.83 after 6.0 hours** (iteration 10k, **101 / 108 tracked**).
- **Useful context:** Active development. The policy controls muscle excitation at 100 Hz, and the project provides a differentiable torch muscle model plus retargeting tools. The retargeted KIT data is gated and subject to AMASS terms; MS-Human-700 is provided as a Git submodule. [Source snapshot](https://github.com/kaibohex/muscle-supermimic/blob/b7c7cdd83e82399e057cb9d3f1b76f23ca022c7b/README.md).

<a href="https://github.com/kaibohex/muscle-supermimic"><img src="https://raw.githubusercontent.com/kaibohex/muscle-supermimic/b7c7cdd83e82399e057cb9d3f1b76f23ca022c7b/docs/assets/teaser_three.gif" width="480" alt="Simulation · MS-Human-700 and MyoFullBody tracking KIT clips at iteration 10000"></a><br><sub>Simulation · MS-Human-700 and MyoFullBody · iteration 10000</sub>

<br>

### SuperMimic-PERA

[Repository](https://github.com/shangchaohu718/supermimic-pera) · [Current status](https://github.com/shangchaohu718/supermimic-pera/blob/0e89e55187a800341e609129b5d5200a607a467c/README.md#当前状态) · [Skateboarding report](https://github.com/shangchaohu718/supermimic-pera/blob/0e89e55187a800341e609129b5d5200a607a467c/docs/FIRST_SKATEBOARD_SKILL.md)

- **By shangchaohu718.** Builds on UniSuperMimic for G1 interaction experiments, retaining a frozen tracker while developing separate interaction policies in UniLab / MuJoCo.
- **Upstream report:** A separate skateboarding policy completes 30-second simulated runs from one standard and eight held-out perturbed initial states, traveling **39.87–42.13 m**.
- **Useful context:** Tracking and skateboarding are selected as separate branches. A shared world-model-driven interaction actor is not established; box handling and stairs remain unsuccessful in the reported prototype. [Source snapshot](https://github.com/shangchaohu718/supermimic-pera/blob/0e89e55187a800341e609129b5d5200a607a467c/README.md).

<a href="https://github.com/shangchaohu718/supermimic-pera/blob/0e89e55187a800341e609129b5d5200a607a467c/README.md"><img src="assets/community/pera-tracking-results.png" width="720" alt="Report screenshot · tracking checkpoints 500–6000; separate from skateboarding"></a><br><sub>Report screenshot · tracking checkpoints 500–6000; separate from skateboarding</sub>

<br>

### SuperMimic Backflip Diagnostics

[Repository](https://github.com/liudi159/supermimic-backflip-5090) · [Results](https://github.com/liudi159/supermimic-backflip-5090/blob/5b313d75e804cdd2ff1ce9bdcfa899a98eca856b/README.md#结果) · [Quickstart](https://github.com/liudi159/supermimic-backflip-5090/blob/5b313d75e804cdd2ff1ce9bdcfa899a98eca856b/README.md#快速入口)

- **By liudi159.** A focused G1 backflip study on Isaac Lab 3 and one RTX 5090, tracking leg symmetry, contact forces, penetration and landing stability.
- **Upstream report:** The final V14 checkpoint completes the rotation and landing hold, but the original strict evaluation records one frame of non-foot penetration and **fails acceptance**.
- **Useful context:** An independent rerun changes the borderline contact outcome. Both records are retained, so the clip should not be read as robust success or reproduction of all paper experiments. [Source snapshot](https://github.com/liudi159/supermimic-backflip-5090/blob/5b313d75e804cdd2ff1ce9bdcfa899a98eca856b/README.md).

<a href="https://github.com/liudi159/supermimic-backflip-5090/blob/5b313d75e804cdd2ff1ce9bdcfa899a98eca856b/media/v14_blue_checker.mp4"><img src="assets/community/backflip.gif" width="480" alt="Simulation · final V14 policy; strict evaluation failed"></a><br><sub>Simulation · final V14 policy; strict evaluation failed</sub>

<br>

## Frameworks and training stacks

Integrations and reusable training or evaluation stacks.

### ScaleBFM_Plus · SuperMimic

[Repository](https://github.com/Hxxxz0/ScaleBFM_Plus) · [Training and results](https://github.com/Hxxxz0/ScaleBFM_Plus/blob/65e4d524bd31fdc4284ba8c6e624fb0b0127da03/ScaleTrack/README.md#fast-training-with-a-learned-world-model-supermimic) · [Released checkpoint](https://github.com/Hxxxz0/ScaleBFM_Plus/tree/65e4d524bd31fdc4284ba8c6e624fb0b0127da03/ScaleTrack/checkpoints/supermimic_m)

- **By Hxxxz0, building on ScaleBFM.** Integrates SuperMimic-style world-model learning and 32-step BPTT into ScaleTrack for G1 in IsaacLab / RSL-RL, retaining the humanoid transformer and tracking modes, with PPO-compatible policy export and playback.
- **Upstream report:** Training on **309 h / 138k clips** from BONES-SEED, any4hdmi and LAFAN1 for **8.3 h on 16 RTX 5090s** yields **99.5% tracking success on 2,575 held-out motions**. On 386 dynamic test motions, both this policy and the official ScaleBFM-M checkpoint succeed on **376 / 386**, with mean global body-position errors of **6.35 cm** and **6.43 cm**, respectively.
- **Useful context:** This is a community extension of ScaleBFM. The reported **26× per-step speedup** compares **0.65 s on 16 RTX 5090s** with PPO's **17.0 s on 8 RTX 5090s**; it is not a matched-compute or time-to-quality comparison. [Source snapshot](https://github.com/Hxxxz0/ScaleBFM_Plus/blob/65e4d524bd31fdc4284ba8c6e624fb0b0127da03/ScaleTrack/README.md).

<a href="https://github.com/Hxxxz0/ScaleBFM_Plus/blob/65e4d524bd31fdc4284ba8c6e624fb0b0127da03/ScaleTrack/assets/demos/supermimic_vs_official.gif"><img src="https://media.githubusercontent.com/media/Hxxxz0/ScaleBFM_Plus/65e4d524bd31fdc4284ba8c6e624fb0b0127da03/ScaleTrack/assets/demos/supermimic_vs_official.gif" width="480" alt="Simulation · official ScaleBFM-M (left) and SuperMimic (right), unseen LAFAN dance"></a><br><sub>Simulation · official ScaleBFM-M (left) and SuperMimic (right), unseen LAFAN dance · Source: Hxxxz0 / ScaleBFM_Plus</sub>

<br>

### HoloMotion · SuperMimic

[Repository](https://github.com/HorizonRobotics/HoloMotion) · [Training guide](https://github.com/HorizonRobotics/HoloMotion/blob/adaacd50ada6ba9338f6c3f539093f85453e2554/docs/supermimic.md) · [Results](https://github.com/HorizonRobotics/HoloMotion/blob/adaacd50ada6ba9338f6c3f539093f85453e2554/docs/supermimic.md#7-recorded-30-minute-results)

- **By Horizon Robotics.** Integrates SuperMimic into HoloMotion’s G1 assets, HDF5 motion data and Hydra workflow, sharing tasks and evaluation with PPO on MuJoCo Warp and Isaac PhysX.
- **Upstream report:** The selected MuJoCo Warp recipe completes **32 / 40 LAFAN1 training clips after 30 minutes on one RTX 5090**.
- **Useful context:** The validated route uses a compact policy. The preview shows short excerpts from a separate run; it does not replace complete-clip evaluation or establish the planned large-policy integration. [Source snapshot](https://github.com/HorizonRobotics/HoloMotion/blob/adaacd50ada6ba9338f6c3f539093f85453e2554/docs/supermimic.md).

<a href="https://github.com/HorizonRobotics/HoloMotion"><img src="https://raw.githubusercontent.com/HorizonRobotics/HoloMotion/adaacd50ada6ba9338f6c3f539093f85453e2554/docs/media/supermimic_training_progress.webp" width="480" alt="Simulation · PPO / SuperMimic, two backends"></a><br><sub>Simulation · PPO / SuperMimic, two backends</sub>

<br>

### TrackerLab SuperMimic

[Repository](https://github.com/Renforce-Dynamics/trackerlab-supermimic) · [Install](https://github.com/Renforce-Dynamics/trackerlab-supermimic/blob/29d24524f2f731bf4df75b319c3e76544165849e/README.md#install) · [Results and limits](https://github.com/Renforce-Dynamics/trackerlab-supermimic/blob/29d24524f2f731bf4df75b319c3e76544165849e/docs/results.md)

- **By Renforce Dynamics.** Provides a shared Isaac Lab / PhysX workflow for retargeting, training, full-clip evaluation and export across G1, Go2, A3, T1, Bumi and Pi+, plus Go2 task policies.
- **Upstream report:** Re-evaluation of the 32,000-iteration G1 parent checkpoint reports normalized return **0.8694663** and **0 / 40 LAFAN1 failures**.
- **Useful context:** Results use PhysX, while supermimic_vibed uses MuJoCo Warp. Robot-specific motion libraries and training histories differ; held-out motion generalization remains unmeasured. [Source snapshot](https://github.com/Renforce-Dynamics/trackerlab-supermimic/blob/29d24524f2f731bf4df75b319c3e76544165849e/README.md).

<a href="https://github.com/Renforce-Dynamics/trackerlab-supermimic/blob/29d24524f2f731bf4df75b319c3e76544165849e/docs/media/g1_dance_032000.mp4"><img src="https://raw.githubusercontent.com/Renforce-Dynamics/trackerlab-supermimic/29d24524f2f731bf4df75b319c3e76544165849e/docs/media/g1_dance_032000.gif" width="480" alt="Simulation · G1 policy / reference dance"></a><br><sub>Simulation · G1 policy / reference dance</sub>

<br>

### UniSuperMimic

[Repository](https://github.com/Motphys/Uni-SuperMimic) · [Installation](https://github.com/Motphys/Uni-SuperMimic/blob/faf7818e8abac3ec6abb8f00e6e904d3577f800b/README.md#installation) · [Results](https://github.com/Motphys/Uni-SuperMimic/blob/faf7818e8abac3ec6abb8f00e6e904d3577f800b/README.md#results)

- **By Motphys.** Ports supermimic_vibed to a UniLab Manager-Based G1 task, with asset preparation, selectable simulation backends, deterministic full-clip evaluation and video export.
- **Upstream report:** At iteration **12,000**, macro normalized return is **0.827227** with **0 / 40 LAFAN1/G1 failures**, using UniLab 1.5.0, mjwarp and 4,096 training environments.
- **Useful context:** The published tracking result uses mjwarp. MuJoCo and Motrix entry points do not establish equivalent training results. [Source snapshot](https://github.com/Motphys/Uni-SuperMimic/blob/faf7818e8abac3ec6abb8f00e6e904d3577f800b/README.md).

<a href="https://github.com/Motphys/Uni-SuperMimic/blob/faf7818e8abac3ec6abb8f00e6e904d3577f800b/docs/assets/supermimic_comparison.mp4"><img src="https://raw.githubusercontent.com/Motphys/Uni-SuperMimic/faf7818e8abac3ec6abb8f00e6e904d3577f800b/docs/assets/supermimic_comparison.gif" width="480" alt="Simulation · G1 jump tracking"></a><br><sub>Simulation · G1 jump tracking</sub>

<br>

### SuperMimic Lab

[Repository](https://github.com/chu-fa/isaaclab-supermimic) · [Setup](https://github.com/chu-fa/isaaclab-supermimic/blob/d350e4378c6dc08a3f2a1d35d47b45d83db0e081/docs/SETUP.md) · [Custom-task guide](https://github.com/chu-fa/isaaclab-supermimic/blob/d350e4378c6dc08a3f2a1d35d47b45d83db0e081/docs/CUSTOM_TASKS.md)

- **By chu-fa.** Packages a reusable SuperMimic learner and runner for Isaac Lab custom tasks, with a separately installable AGIBOT A3 example.
- **What it provides:** Provides task contracts, setup instructions and backend validation records. A custom task must supply differentiable state, observation, reward and termination functions.
- **Useful context:** Targets the Isaac Lab 3 development API. The A3 preview uses separately initialized segments; convergence, backend equivalence and hardware deployment are not established. [Source snapshot](https://github.com/chu-fa/isaaclab-supermimic/blob/d350e4378c6dc08a3f2a1d35d47b45d83db0e081/README.md).

<a href="https://github.com/chu-fa/isaaclab-supermimic"><img src="https://raw.githubusercontent.com/chu-fa/isaaclab-supermimic/d350e4378c6dc08a3f2a1d35d47b45d83db0e081/docs/media/a3_reference_vs_policy.webp" width="480" alt="A3 reference / policy · separately initialized segments"></a><br><sub>A3 reference / policy · separately initialized segments</sub>

<br>

### SuperMimicKit

[Repository](https://github.com/OMEGA-i/SuperMimicKit) · [Preview release](https://github.com/OMEGA-i/SuperMimicKit/releases/tag/demo-preview-20261024) · [Evaluation and limits](https://github.com/OMEGA-i/SuperMimicKit/blob/6697ff8ca53adc9233ded12a7c8777610ca1154d/docs/preview-release.md)

- **By OMEGA-i.** An independent MuJoCo Warp implementation for G1, H2 and A3, with motion retargeting, policy/world-model ONNX export and WebGPU browser previews.
- **Upstream report:** Publishes separate train40 and held-out val37 evaluations for G1/H2. The G1 55.5k preview reports **0.7990, 3 / 40 failures** on train40 and **0.3103, 31 / 37 failures** on val37; A3 100k full-clip evaluation is pending.
- **Useful context:** An experimental preview with limited held-out tracking and documented later-checkpoint regressions. Supply licensed motion data; no top-level code license was found at the reviewed revision. [Source snapshot](https://github.com/OMEGA-i/SuperMimicKit/blob/6697ff8ca53adc9233ded12a7c8777610ca1154d/README.md).

<a href="https://github.com/OMEGA-i/SuperMimicKit/blob/6697ff8ca53adc9233ded12a7c8777610ca1154d/docs/media/teaser.mp4"><img src="https://raw.githubusercontent.com/OMEGA-i/SuperMimicKit/6697ff8ca53adc9233ded12a7c8777610ca1154d/docs/media/teaser.gif" width="480" alt="Browser preview · G1 / H2 / A3"></a><br><sub>Browser preview · G1 / H2 / A3</sub>

<br>

## Robot porting and retargeting

Robot-, simulator- and hardware-specific ports, together with motion-retargeting tools.

### SuperMimic Retargeted

[Repository](https://github.com/tianshuwu/supermimic-retargeted) · [Quickstart](https://github.com/tianshuwu/supermimic-retargeted/blob/ff69a0e5305126eb5b80b323bcd815805bc3df4e/README.md#快速开始) · [Data guide](https://github.com/tianshuwu/supermimic-retargeted/blob/ff69a0e5305126eb5b80b323bcd815805bc3df4e/docs/DATA.md)

- **By tianshuwu.** Extends the CuboiLeo mjlab baseline to G1, A3 and X2 Ultra, adding robot-specific kinematics, SOMA retargeting, coordinate corrections and foot-contact checks.
- **What it provides:** Publishes LAFAN1/BONES-SEED preparation workflows and historical evaluation records. Training weights are not distributed, and motion data must be prepared separately.
- **Useful context:** The reported policies use extra anchor-relative observations computed from simulator truth. These require corresponding state estimation on hardware; real-robot transfer is not validated. [Source snapshot](https://github.com/tianshuwu/supermimic-retargeted/blob/ff69a0e5305126eb5b80b323bcd815805bc3df4e/README.md).

<a href="https://github.com/tianshuwu/supermimic-retargeted/blob/ff69a0e5305126eb5b80b323bcd815805bc3df4e/media/demo.mp4"><img src="https://raw.githubusercontent.com/tianshuwu/supermimic-retargeted/ff69a0e5305126eb5b80b323bcd815805bc3df4e/media/demo-preview.gif" width="480" alt="Simulation · G1 / X2 Ultra / A3"></a><br><sub>Simulation · G1 / X2 Ultra / A3</sub>

<br>

### SuperMimic E1

[Repository](https://github.com/wenconggan/SuperMimic_e1) · [Setup](https://github.com/wenconggan/SuperMimic_e1/blob/d5fbe8f219c438b84633130652c5e6e74beff628/README.md#安装与资源) · [Results](https://github.com/wenconggan/SuperMimic_e1/blob/d5fbe8f219c438b84633130652c5e6e74beff628/README.md#已测结果)

- **By wenconggan.** Adapts the Isaac Lab 3 implementation to the 21-DoF DroidUp E1, with standalone native-MuJoCo sim-to-sim playback and evaluation.
- **Upstream report:** The 164k checkpoint completes **40 / 40 training motions**, return **0.8559**, in Isaac Lab. A separate 168k checkpoint completes **10 / 10 sampled eight-second segments** in native MuJoCo.
- **Useful context:** Complete-clip evaluation and independently initialized short segments use different protocols. Neither result measures unseen-motion generalization or hardware transfer. [Source snapshot](https://github.com/wenconggan/SuperMimic_e1/blob/d5fbe8f219c438b84633130652c5e6e74beff628/README.md).

<a href="https://github.com/wenconggan/SuperMimic_e1/blob/d5fbe8f219c438b84633130652c5e6e74beff628/docs/assets/e1_random10_80s.mp4"><img src="https://raw.githubusercontent.com/wenconggan/SuperMimic_e1/d5fbe8f219c438b84633130652c5e6e74beff628/docs/assets/e1_preview.gif" width="480" alt="E1 sim-to-sim · native MuJoCo"></a><br><sub>E1 sim-to-sim · native MuJoCo</sub>

<br>

### SuperMimic Oli

[Repository](https://github.com/liuskywalkerjskd/supermimic_oli) · [Setup](https://github.com/liuskywalkerjskd/supermimic_oli/blob/2dc90d90e89fb2e097e985c84c8b99a77708fa5f/README.md#setup) · [Results](https://github.com/liuskywalkerjskd/supermimic_oli/blob/2dc90d90e89fb2e097e985c84c8b99a77708fa5f/README.md#results)

- **By liuskywalkerjskd.** Ports supermimic_vibed to the 31-DoF LimX Oli in Isaac Lab 3, adding motion retargeting, robot kinematics and full-motion video export.
- **Upstream report:** At iteration **18,000**, the original 40-motion LAFAN1 evaluation reports return **0.6783** and **36 / 40 completed clips**, after about **2.20 hours on one RTX 4090**.
- **Useful context:** The displayed walking clip is a selected excerpt. Use the full-library evaluation when judging tracking coverage. [Source snapshot](https://github.com/liuskywalkerjskd/supermimic_oli/blob/2dc90d90e89fb2e097e985c84c8b99a77708fa5f/README.md).

<a href="https://github.com/liuskywalkerjskd/supermimic_oli/blob/2dc90d90e89fb2e097e985c84c8b99a77708fa5f/results/oli_walk1_subject1_full.mp4"><img src="https://raw.githubusercontent.com/liuskywalkerjskd/supermimic_oli/2dc90d90e89fb2e097e985c84c8b99a77708fa5f/results/oli_walk1_subject1_preview.gif" width="480" alt="Simulation · selected Oli walking excerpt"></a><br><sub>Simulation · selected Oli walking excerpt</sub>

<br>

### SuperMimic on Apple M5

[Repository](https://github.com/WXyuany/supermimic-m5) · [Run the released model](https://github.com/WXyuany/supermimic-m5/blob/42451591718e1a9a5ec601366997f47c0ad180a3/README.md#三步运行已训练模型) · [Results](https://github.com/WXyuany/supermimic-m5/blob/42451591718e1a9a5ec601366997f47c0ad180a3/README.md#实验结果)

- **By WXyuany.** Adapts the CuboiLeo G1 baseline to Apple Silicon, using CPU MuJoCo for physics and PyTorch MPS for learning, with released weights and playback tools.
- **Upstream report:** For the released 21k checkpoint on a 24 GB Apple M5, seed 0, the original 40-motion evaluation reports return **0.7081** and **25 / 40 completed clips**; a fresh-environment check completes **26 / 40**.
- **Useful context:** Return is normalized by executed steps without zero-padding after failure, and the actor uses nine extra anchor-observation dimensions. Read return together with completion; held-out generalization is untested. [Source snapshot](https://github.com/WXyuany/supermimic-m5/blob/42451591718e1a9a5ec601366997f47c0ad180a3/README.md).

<a href="https://github.com/WXyuany/supermimic-m5/blob/42451591718e1a9a5ec601366997f47c0ad180a3/assets/videos/walk1_subject1.mp4"><img src="https://raw.githubusercontent.com/WXyuany/supermimic-m5/42451591718e1a9a5ec601366997f47c0ad180a3/assets/images/walk-preview.gif" width="480" alt="Simulation · G1 walking on Apple M5"></a><br><sub>Simulation · G1 walking on Apple M5</sub>

<br>

### SuperMimic-MuJoCo

[Repository](https://github.com/panhainan2020/SuperMimic-MuJoCo) · [Setup](https://github.com/panhainan2020/SuperMimic-MuJoCo/blob/db045afa9c52458f213e2c66037387e9c109a03a/README.md#环境安装) · [Evaluation](https://github.com/panhainan2020/SuperMimic-MuJoCo/blob/db045afa9c52458f213e2c66037387e9c109a03a/README.md#评估结果)

- **By panhainan2020.** A standalone mjlab / CPU MuJoCo port of supermimic_vibed for G1, with observation-compatibility profiles, inference weights and held-out 100STYLE evaluation.
- **Upstream report:** The fixed 98k policy completes **40 / 40 LAFAN training motions** at return **0.8713**, and **3,569 / 3,573 unseen 100STYLE clips** at **0.8045**, without fine-tuning.
- **Useful context:** The datasets differ in duration and retargeting. “Completed” means no termination was triggered; this does not reproduce the paper’s full training schedule or all experiments. [Source snapshot](https://github.com/panhainan2020/SuperMimic-MuJoCo/blob/db045afa9c52458f213e2c66037387e9c109a03a/README.md).

<a href="https://github.com/panhainan2020/SuperMimic-MuJoCo/blob/db045afa9c52458f213e2c66037387e9c109a03a/README.md"><img src="assets/community/mujoco-evaluation.png" width="720" alt="Report screenshot · LAFAN training motions and unseen 100STYLE clips"></a><br><sub>Report screenshot · LAFAN training motions and unseen 100STYLE clips</sub>

[Full video gallery](https://supermimic-mujoco-results.zippyaspen7.chatgpt.site)

<br>

### SuperMimic Wheel-Legged (wheelbipe)

[Repository](https://github.com/RadiantForever/supermimic_wheelbipe) · [Setup](https://github.com/RadiantForever/supermimic_wheelbipe/blob/0bf3456299a9f754289da58dce6c97c46afd3f03/README.md#setup) · [Results](https://github.com/RadiantForever/supermimic_wheelbipe/blob/0bf3456299a9f754289da58dce6c97c46afd3f03/README.md#results)

- **By RadiantForever.** Downstream port of SuperMimic to the wheeled-legged wheelbipe V14_2. The humanoid motion library is replaced by a velocity-command library; a 6-DoF action policy (four leg targets plus two wheel speeds) is optimised inside the differentiable world model, with PhysX / Isaac Lab as the data source and no PPO in the loop.
- **Upstream report:** On a 16-command grid the unified checkpoint reaches **0 / 16 falls** and normalized return **0.983**; a speed-focused checkpoint tracks **1.40 m/s at 0.01 error**, and yaw reaches **10.21 rad/s (1.62 rev/s)** with a **0.20-0.28 m** leg cycle. Single RTX 4090, 4096 environments, 3.72 h cumulative over resumed runs; one run, no seed sweep.
- **Useful context:** A pretrained PPO policy for the same robot is mixed into the world-model buffer for the first 800 iterations only, and no teacher-free ablation was run, so these numbers are not attributable to the method alone. The port requires the robot USD asset from the upstream repository; there is no URDF. [Source snapshot](https://github.com/RadiantForever/supermimic_wheelbipe/blob/0bf3456299a9f754289da58dce6c97c46afd3f03/README.md).

<a href="https://www.bilibili.com/video/BV1haxM6CEGm/"><img src="assets/community/wheelbipe-grid.gif" width="480" alt="Simulation · four commanded conditions"></a><br><sub>Simulation · four commanded conditions: 10 rad/s yaw (top-left), 0.20-0.28 m leg cycle (top-right), 1.5 m/s forward with leg cycle (bottom-left), yaw with leg cycle (bottom-right)</sub>

<br>

## Inspired experiments

Ideas transferred to other control settings, with different tasks and evaluation protocols.

### Ref2Dex · Dex Contact MBRL

[Repository](https://github.com/hitsz-oyx/Ref2Dex-agent) · [Task and results](https://github.com/hitsz-oyx/Ref2Dex-agent/blob/31cdb9ac759838b83d62bbc0addfd5cf28f3dff4/src/task/dex-contact-mbrl/README.md)

- **By hitsz-oyx.** Explores action-conditioned contact dynamics and short-horizon BPTT for the Inspire hand in Isaac Gym / DExplore, combining contact memory with native collision-geometry queries.
- **What it provides:** Separately records behavior cloning, dynamics fitting, bounded actor/critic updates and native-physics evaluation.
- **Useful context:** Improved reference survival comes with lower mean return in the reported comparison. Reliable model-based manipulation gains are not established, and contact proxies are not certified grasp success. [Source snapshot](https://github.com/hitsz-oyx/Ref2Dex-agent/blob/31cdb9ac759838b83d62bbc0addfd5cf28f3dff4/src/task/dex-contact-mbrl/README.md).

<a href="https://github.com/hitsz-oyx/Ref2Dex-agent/blob/31cdb9ac759838b83d62bbc0addfd5cf28f3dff4/src/task/dex-contact-mbrl/docs/CONTACT-REFINEMENT-RESULTS-20261026.md"><img src="assets/community/contact-bptt-results.png" width="720" alt="Report screenshot · native-physics comparison; higher reference survival, lower mean return"></a><br><sub>Report screenshot · native-physics comparison; higher reference survival, lower mean return</sub>

<br>

### G0.5 · SuperMimic-style Steering

[Repository](https://github.com/azizkhadraoui/g05) · [Experiment code](https://github.com/azizkhadraoui/g05/blob/e3de0de50db7d90068483e2d30f2eacd781300b4/jobs/119_smsteer.py)

- **By azizkhadraoui.** Transfers SuperMimic-style gradient-based learning to G0.5 VLA steering on LIBERO: a noise policy is trained through a frozen flow sampler using world-model and critic gradients.
- **Useful context:** This is one task-specific steering experiment within a broader VLA stack. The linked script identifies the relevant method; the repository’s other planning and memory results are separate experiments. [Source snapshot](https://github.com/azizkhadraoui/g05/blob/e3de0de50db7d90068483e2d30f2eacd781300b4/jobs/119_smsteer.py).

<a href="https://github.com/azizkhadraoui/g05/blob/e3de0de50db7d90068483e2d30f2eacd781300b4/README.md"><img src="assets/community/g05-steering-entry.png" width="720" alt="Code index screenshot · world-model / critic steering experiment"></a><br><sub>Code index screenshot · world-model / critic steering experiment</sub>

<br>

### FlatWorld · SuperMimic-2D

[Repository](https://github.com/swaggyliu/FlatWorld) · [Quickstart](https://github.com/swaggyliu/FlatWorld/blob/207e9e9c61ef21b8f145c3e0c4d8b121a03bf45a/supermimic2d/README.md#quick-start) · [Reference motions](https://github.com/swaggyliu/FlatWorld/blob/207e9e9c61ef21b8f145c3e0c4d8b121a03bf45a/supermimic2d/README.md#reference-motions-lafan-like-2d)

- **By swaggyliu.** Recreates the shared-world-model and imagined-policy-learning loop in FlatWorld with an eight-joint 2D humanoid and motion-tracking tasks.
- **What it provides:** Provides training, reference baking, per-skill rendering and a multi-skill showcase for walking, running, jumping, dancing and other motions.
- **Useful context:** References are procedural, LAFAN-like 2D motions, not the LAFAN1 dataset. The character also uses a mild root assist, so this is an illustrative adaptation rather than a G1 benchmark. [Source snapshot](https://github.com/swaggyliu/FlatWorld/blob/207e9e9c61ef21b8f145c3e0c4d8b121a03bf45a/supermimic2d/README.md).

<a href="https://github.com/swaggyliu/FlatWorld/blob/207e9e9c61ef21b8f145c3e0c4d8b121a03bf45a/supermimic2d/runs/lafan2d/showcase_30s.mp4"><img src="assets/community/flatworld.gif" width="480" alt="2D simulation · motion-tracking showcase"></a><br><sub>2D simulation · motion-tracking showcase</sub>

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
