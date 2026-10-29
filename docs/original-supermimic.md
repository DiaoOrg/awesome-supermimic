[← Awesome SuperMimic](../README.md)

## Original SuperMimic

**[SuperMimic: Scaling Humanoid Whole-Body Control with One Differentiable World Model](https://arxiv.org/abs/2610.28480)**<br>
Qiayuan Liao, Yiyang Shao, Junfeng Long, Kevin Zakka, Roberto Horowitz, Pieter Abbeel, and Koushil Sreenath.<br>
**UC Berkeley · CoRL 2026 Oral**

[Paper](https://arxiv.org/abs/2610.28480) · [PDF](https://arxiv.org/pdf/2610.28480) · [Project](https://supermimic.github.io/) · [Video](https://supermimic.github.io/media/real/film-1080.mp4) · [Browser demo](https://supermimic.github.io/demo/)

SuperMimic learns shared humanoid dynamics from simulator transitions and improves a motion-tracking policy through short imagined rollouts. The world model and policy are updated in the same training loop; policy gradients pass through the learned model. [Method overview](https://supermimic.github.io/#loop).

<p align="center">
  <a href="https://arxiv.org/pdf/2610.28480v1#page=4">
    <img src="../assets/official/training-loop.png" width="100%" alt="Original SuperMimic Figure 2: data collection, world-model fitting and policy improvement share a replay buffer; dashed arrows show gradients">
  </a>
</p>
<p align="center">
  <sub>Original paper, Figure 2 · <a href="https://arxiv.org/pdf/2610.28480v1#page=4">Framework, p. 4</a> · <a href="https://arxiv.org/pdf/2610.28480v1#page=15">Algorithm A.1, p. 15</a></sub>
</p>

The world model is fit on **8-step replay windows**; the policy and critic learn from **32-step imagined rollouts**. During the policy update, model weights stay fixed while gradients pass through the model to the policy. Blue dashed arrows show gradients; ❄️ marks frozen weights and 🔥 marks weights being trained in that phase.

The authors report surpassing SONIC's released-checkpoint return after **3 hours on one H100**, with **25 / 129,514 failed motions**, and **0 / 129,514** after 9.8 hours on two H100s. These are training-motion coverage results, with different training hardware and data from SONIC. See the [official results and compute accounting](https://supermimic.github.io/#compute).

**Official code status — checked 2026-10-28:** the official website links the paper, video, and browser demo, but does not link a training-code repository. The projects below are community implementations and extensions.

<p align="center">
  <a href="https://supermimic.github.io/media/world-model/wm_on.mp4"><img src="../assets/official/world-model.gif" alt="Official SuperMimic world-model predictions in blue overlaid on simulator motion" width="100%"></a><br>
  <b>World-model predictions</b>
</p>

<table>
  <tr>
    <td width="50%" align="center">
      <a href="https://supermimic.github.io/media/hero/hero_montage_desktop.mp4"><img src="../assets/official/simulation-wide.gif" alt="Official SuperMimic simulation: G1 flips, rolls, and dances" width="100%"></a><br>
      <b>Simulation</b>
    </td>
    <td width="50%" align="center">
      <a href="https://supermimic.github.io/media/real/real_bay-wide.mp4"><img src="../assets/official/real-g1-wide.gif" alt="Official SuperMimic real G1 performing a side roll and a flip by the bay" width="100%"></a><br>
      <b>Real G1</b>
    </td>
  </tr>
</table>

<p align="center"><sub>Original footage: <a href="https://supermimic.github.io/">SuperMimic authors</a> · Click a preview for the full video · <a href="../assets/official/README.md">Media credits</a></sub></p>
