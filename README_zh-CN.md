<div align="center">

# Awesome SuperMimic

[![Awesome](https://awesome.re/badge.svg)](https://github.com/sindresorhus/awesome) [![论文](https://img.shields.io/badge/arXiv-2610.28480-b31b1b.svg)](https://arxiv.org/abs/2610.28480) [![License: CC0](https://img.shields.io/badge/License-CC0_1.0-blue.svg)](LICENSE) [![欢迎贡献](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

**收集 SuperMimic 的社区实现、方法扩展、演示和学习资源。**

[English](README.md) · 简体中文

[原始论文](https://arxiv.org/abs/2610.28480) · [官方项目](https://supermimic.github.io/) · [交互演示](https://supermimic.github.io/demo/) · [社区项目](#社区项目)

</div>

<p align="center">
  <a href="https://supermimic.github.io/media/world-model/wm_on.mp4"><img src="assets/official/world-model.gif" alt="SuperMimic 官方世界模型演示：蓝色预测轨迹叠加在仿真动作上" width="100%"></a><br>
  <b>世界模型预测</b>
</p>

<table>
  <tr>
    <td width="50%" align="center">
      <a href="https://supermimic.github.io/media/hero/hero_montage_desktop.mp4"><img src="assets/official/simulation-wide.gif" alt="SuperMimic 官方仿真演示：G1 翻转、侧滚与舞蹈" width="100%"></a><br>
      <b>仿真全身动作</b>
    </td>
    <td width="50%" align="center">
      <a href="https://supermimic.github.io/media/real/real_bay-wide.mp4"><img src="assets/official/real-g1-wide.gif" alt="SuperMimic 官方真机演示：G1 在海湾边完成侧滚与翻转" width="100%"></a><br>
      <b>G1 真机演示</b>
    </td>
  </tr>
</table>

<p align="center"><sub>原作影像：<a href="https://supermimic.github.io/">SuperMimic 作者</a> · 点击预览观看原视频 · <a href="assets/official/README.md">素材来源</a></sub></p>

建议先了解原始工作，再按框架和任务选择实现。本仓库由社区维护，各收录项目的贡献归属于其作者。

## 目录

- [原始 SuperMimic](#原始-supermimic)
- [社区项目](#社区项目)
- [相关方法与基线](#相关方法与基线)
- [数据与学习资源](#数据与学习资源)
- [参与贡献](#参与贡献)
- [论文引用](#论文引用)
- [致谢与许可](#致谢与许可)

## 原始 SuperMimic

**[SuperMimic: Scaling Humanoid Whole-Body Control with One Differentiable World Model](https://arxiv.org/abs/2610.28480)**<br>
Qiayuan Liao、Yiyang Shao、Junfeng Long、Kevin Zakka、Roberto Horowitz、Pieter Abbeel、Koushil Sreenath。<br>
**UC Berkeley · CoRL 2026 Oral**

[论文](https://arxiv.org/abs/2610.28480) · [PDF](https://arxiv.org/pdf/2610.28480) · [项目主页](https://supermimic.github.io/) · [官方视频](https://supermimic.github.io/media/real/film-1080.mp4) · [浏览器演示](https://supermimic.github.io/demo/)

SuperMimic 从仿真状态转移中学习一个共享的可微世界模型，再通过短时想象轨迹训练动作跟踪策略。世界模型和策略在同一个循环中持续更新，策略梯度经过学习到的模型。[方法介绍](https://supermimic.github.io/#loop)。

<p align="center">
  <a href="https://arxiv.org/pdf/2610.28480v1#page=4">
    <img src="assets/official/training-loop.png" width="100%" alt="SuperMimic 原论文图 2：数据采集、世界模型拟合与策略改进共享回放缓冲区，虚线表示梯度路径">
  </a>
</p>
<p align="center">
  <sub>原论文 Figure 2 · <a href="https://arxiv.org/pdf/2610.28480v1#page=4">算法框架，第 4 页</a> · <a href="https://arxiv.org/pdf/2610.28480v1#page=15">完整伪代码 Algorithm A.1，第 15 页</a></sub>
</p>

世界模型使用 **8 步回放窗口**拟合，策略和 critic 通过 **32 步想象轨迹**学习。更新策略时，世界模型的权重固定，但梯度仍经过模型传回策略。图中蓝色虚线表示梯度，❄️ 表示该阶段权重冻结，🔥 表示该阶段权重参与训练。

作者报告：**单张 H100 训练 3 小时**超过 SONIC 已发布 checkpoint 的回报，**129,514 个动作中失败 25 个**；两张 H100 训练 9.8 小时后失败数为 0。这是训练动作覆盖结果，且两者训练硬件与数据规模不同。[原始结果与计算量口径](https://supermimic.github.io/#compute)。

**官方代码状态（2026-10-26 核查）：**官方主页提供论文、视频和浏览器演示，尚未链接训练代码仓库。下列条目均为社区实现或扩展。

## 社区项目

按用途收录 **33 个社区项目**。已有条目于 **2026-10-26** 对照上游文档及部分源码核查，ScaleBFM_Plus、SuperMimic Mjlab、SuperMimic for Robot Manipulation 与 Muscle SuperMimic 于 **2026-10-27** 核查，每项附有对应版本的来源链接。成绩和演示均为上游报告，本清单未独立重跑实验。

- 🔬 **[独立复现](#独立复现)** — **4 个项目** · 复现与评估原始方法。
- 🧩 **[方法与任务扩展](#方法与任务扩展)** — **13 个项目** · 探索算法改动、新任务和控制场景。
- 🛠️ **[框架、本体适配与部署](#框架本体适配与部署)** — **13 个项目** · 按框架、本体和部署需求选实现。
- 💡 **[方法借鉴与探索](#方法借鉴与探索)** — **3 个项目** · 将相关思路迁移到其他控制问题。

## 独立复现

从原方法复现入手，查看训练、评估和复现记录。

### supermimic_vibed

[仓库](https://github.com/zita-ch/supermimic_vibed) · [安装与使用](https://github.com/zita-ch/supermimic_vibed/blob/a1508d42c9d1699a52e8233ab16d08c488441ab9/README.md#setup) · [结果](https://github.com/zita-ch/supermimic_vibed/blob/a1508d42c9d1699a52e8233ab16d08c488441ab9/README.md#result-lafan1-40-clips-one-rtx-pro-6000-blackwell)

- **作者：Chong Zhang。** 基于 Isaac Lab 3 独立实现 G1 动作跟踪，提供 kit-less 环境、训练、完整动作评估和渲染工具。
- **上游报告：** 单张 RTX PRO 6000 Blackwell 训练 **1.47 小时**，40 条 LAFAN1 动作的归一化回报为 **0.829**，**0 / 40 失败**。
- **选择时注意：** 作者将其描述为快速开发、未经充分审查的复现；与论文的差异包括关闭自碰撞、MLP 使用 bf16，以及额外输入参考根部相对朝向。 [核查版本](https://github.com/zita-ch/supermimic_vibed/blob/a1508d42c9d1699a52e8233ab16d08c488441ab9/README.md)。

<a href="https://github.com/zita-ch/supermimic_vibed"><img src="https://raw.githubusercontent.com/zita-ch/supermimic_vibed/a1508d42c9d1699a52e8233ab16d08c488441ab9/results/supermimic_lafan1_highlight.gif" width="480" alt="仿真 · LAFAN1 动作集锦"></a><br><sub>仿真 · LAFAN1 动作集锦</sub>

<br>

### SuperMimic-Reproduced

[仓库](https://github.com/CuboiLeo/SuperMimic-Reproduced) · [环境与安装](https://github.com/CuboiLeo/SuperMimic-Reproduced/blob/d9be385b3eeb13a638fb33fb200d3bfd9be9839f/README.md#环境) · [实验日志](https://github.com/CuboiLeo/SuperMimic-Reproduced/blob/d9be385b3eeb13a638fb33fb200d3bfd9be9839f/docs/EXPERIMENTS.md)

- **作者：CuboiLeo。** 基于 mjlab 从零实现 G1 跟踪，提供中文复现记录、LAFAN1/BONES-SEED 数据处理、多卡训练和交互回放。
- **上游报告：** 加入锚点相对观测后，单张 RTX 5090 训练 **1.66 小时**达到 LAFAN1 回报 **0.824、5 / 40 失败**；**3.3 小时**时为 **0.904、3 / 40 失败**。
- **选择时注意：** 按论文观测训练 1.8 小时的结果为 **0.56、9 / 40 失败**，两种观测设置不能混为同一结果；BONES-SEED 成绩使用 2,000 条动作评估子集。 [核查版本](https://github.com/CuboiLeo/SuperMimic-Reproduced/blob/d9be385b3eeb13a638fb33fb200d3bfd9be9839f/README.md)。

<a href="https://github.com/CuboiLeo/SuperMimic-Reproduced/blob/d9be385b3eeb13a638fb33fb200d3bfd9be9839f/README.md"><img src="assets/community/reproduced-results.png" width="720" alt="报告截图 · 论文观测与锚点相对观测的结果"></a><br><sub>报告截图 · 论文观测与锚点相对观测的结果</sub>

<br>

### supermimic_vibe

[仓库](https://github.com/dhmbb2/supermimic_vibe) · [安装](https://github.com/dhmbb2/supermimic_vibe/blob/072f0910dadc9d95c720e625b546120e9ce917c9/README.md#setup) · [结果记录](https://github.com/dhmbb2/supermimic_vibe/blob/072f0910dadc9d95c720e625b546120e9ce917c9/notes/RESULTS.md)

- **作者：dhmbb2。** 基于 mjlab 独立复现 G1 跟踪，覆盖 PPO-Sim/PPO-WM 对照、时域与 critic 消融、推力恢复和速度控制实验。
- **上游报告：** 单张 RTX A6000 上，LAFAN1 完整动作确定性评测在 **1.34 小时**达到回报 **0.833**，**12 小时**达到 **0.946、0 / 40 失败**。
- **选择时注意：** 实验记录区分已复现、部分复现和待完成项；BONES-SEED 受数据许可限制，未覆盖真机迁移，A6000 耗时也不能直接等同于 H100。 [核查版本](https://github.com/dhmbb2/supermimic_vibe/blob/072f0910dadc9d95c720e625b546120e9ce917c9/README.md)。

<a href="https://github.com/dhmbb2/supermimic_vibe/blob/072f0910dadc9d95c720e625b546120e9ce917c9/README.md"><img src="assets/community/vibe-results.png" width="720" alt="报告截图 · 单张 RTX A6000 上的复现与消融"></a><br><sub>报告截图 · 单张 RTX A6000 上的复现与消融</sub>

<br>

### SuperMimic Mjlab

[仓库](https://github.com/Breezewrf/supermimic_mjlab) · [安装](https://github.com/Breezewrf/supermimic_mjlab/blob/23c76cad5bf41110709c7f929b54c1da1be6b248/doc/setup_en.md) · [消融实验与检查点](https://github.com/Breezewrf/supermimic_mjlab/blob/23c76cad5bf41110709c7f929b54c1da1be6b248/README.md#ablation-results-and-released-checkpoint)

- **作者：Breezewrf。** 基于 mjlab 为 Unitree G1 独立复现 SuperMimic，提供完整的性能提升消融实验、多动作训练、完整动作评估，以及已发布的策略与世界模型检查点。
- **上游报告：** 所选检查点在全部 40 条 LAFAN 动作的固定起点、完整片段确定性评估中，达到 **40 / 40 成功、平均完成率 100%、归一化回报 0.8528**。使用 **单张 RTX A6000 48 GB**、4,096 个环境和 FP32 网络，训练 **15,000 次迭代约需 4 小时**。
- **性能提升消融：** 完整记录从 Actor/Critic 输入归一化，依次加入躯干坐标系下的动作朝向锚点、世界模型归一化及修正余弦学习率调度的提升过程：在全部 40 条动作、15,000 次迭代的评估中，归一化回报均值为 **0.6016 → 0.8130 → 0.8504 → 0.8526**。最终重复运行均值与上述所选检查点分数分别报告。 [核查版本](https://github.com/Breezewrf/supermimic_mjlab/blob/23c76cad5bf41110709c7f929b54c1da1be6b248/README.md)。

<a href="https://github.com/Breezewrf/supermimic_mjlab/blob/23c76cad5bf41110709c7f929b54c1da1be6b248/doc/assets/evaluation.png"><img src="https://raw.githubusercontent.com/Breezewrf/supermimic_mjlab/23c76cad5bf41110709c7f929b54c1da1be6b248/doc/assets/evaluation.png" width="720" alt="评估面板 · SuperMimic Mjlab 回报、成功率与逐动作完成率"></a><br><sub>上游评估面板 · 回报、成功率与逐动作完成率 · 各配置消融对比见上方链接</sub>

<br>

## 方法与任务扩展

关注算法改动、新任务，以及感知、形态和交互方面的实验。

### MorphMimic

[仓库](https://github.com/lzyang2000/morphmimic) · [安装](https://github.com/lzyang2000/morphmimic/blob/2e35049e9519e511889ef987e4acde55d4f5b017/README.md#setup) · [方法差异](https://github.com/lzyang2000/morphmimic/blob/2e35049e9519e511889ef987e4acde55d4f5b017/README.md#differences-from-supermimic)

- **作者：Lizhi Yang 等。** 在 mjlab 中扩展 SuperMimic，用形态参数条件化网络，让 G1、X2 Ultra 和 T2 共享世界模型、策略或两者。
- **提供内容：** 提供完整动作跟踪和骨盆、双手腕、双脚踝的稀疏五点目标接口，附浏览器演示及遥操作、部署说明。
- **选择时注意：** 不同机器人先映射到统一的 29 关节布局；README 列出了终止模型、归一化、预热和执行器延迟随机化等实现改动。 [核查版本](https://github.com/lzyang2000/morphmimic/blob/2e35049e9519e511889ef987e4acde55d4f5b017/README.md)。

<a href="https://lzyang2000.github.io/morphmimic/static/videos/dance_hiphop_shuffle_sequence_v_001_R_003__A306.mp4"><img src="assets/community/morphmimic.gif" width="480" alt="仿真 · G1 / X2 Ultra / T2 共享策略"></a><br><sub>仿真 · G1 / X2 Ultra / T2 共享策略</sub>

[演示视频](https://lzyang2000.github.io/morphmimic/static/videos/morphmimic.mp4) · [交互演示](https://lzyang2000.github.io/morphmimic/demo/)

<br>

### allmimic

[仓库](https://github.com/Shimingyi/allmimic) · [安装](https://github.com/Shimingyi/allmimic/blob/cb334ff674b2f57248f33f8c21b7fb526fbdf8cc/README.md#install) · [结果](https://github.com/Shimingyi/allmimic/blob/cb334ff674b2f57248f33f8c21b7fb526fbdf8cc/README.md#results)

- **作者：Shimingyi。** 基于 supermimic_vibe，在 mjlab 中混用上身残差动作与腿部绝对动作，并加入世界模型损失加权和动作均衡采样。
- **上游报告：** 单张 RTX 4090 使用推荐配置，训练 **0.83 小时**后，LAFAN1 完整动作评测达到 **0 / 40 失败、回报 0.91**；耗时不含评估。
- **选择时注意：** 推荐配置包含算法和数据采样改动；仅训练 306 条困难动作的实验，与完整 BONES-SEED 训练是不同实验。 [核查版本](https://github.com/Shimingyi/allmimic/blob/cb334ff674b2f57248f33f8c21b7fb526fbdf8cc/README.md)。

<a href="https://github.com/Shimingyi/allmimic"><img src="https://raw.githubusercontent.com/Shimingyi/allmimic/cb334ff674b2f57248f33f8c21b7fb526fbdf8cc/assets/challenge_cases.gif" width="480" alt="仿真 · 高难度动作片段"></a><br><sub>仿真 · 高难度动作片段</sub>

<br>

### SuperMimic on LocoMuJoCo

[仓库](https://github.com/Alchedata/supermimic-locomujoco) · [安装](https://github.com/Alchedata/supermimic-locomujoco/blob/cc1375d48a38bde062d088ffd132122e0cd7b7da/README.md#setup) · [结果](https://github.com/Alchedata/supermimic-locomujoco/blob/cc1375d48a38bde062d088ffd132122e0cd7b7da/README.md#results-at-5k)

- **团队：Alchedata。** 用 JAX 与 LocoMuJoCo 将方法移植到 H1，对比 MLP 基线、残差专家、动作敏感度和可信度相关的世界模型变体。
- **上游报告：** 公开固定 5,000 次迭代检查点的 160 回合评测，既保留表现较好的种子，也记录了残差专家因动作输出饱和而停滞的运行。
- **选择时注意：** 指标是 LocoMuJoCo 回合回报，与 G1 归一化跟踪分数不同；恢复干预与继续训练的对照分别记录。 [核查版本](https://github.com/Alchedata/supermimic-locomujoco/blob/cc1375d48a38bde062d088ffd132122e0cd7b7da/README.md)。

<a href="https://github.com/Alchedata/supermimic-locomujoco/blob/cc1375d48a38bde062d088ffd132122e0cd7b7da/README.md"><img src="assets/community/locomujoco-results.png" width="720" alt="报告截图 · 固定 5k 检查点，160 个评估回合"></a><br><sub>报告截图 · 固定 5k 检查点，160 个评估回合</sub>

<br>

### Rethinking SuperMimic

[仓库](https://github.com/btx0424/rethinking-supermimic) · [安装](https://github.com/btx0424/rethinking-supermimic/blob/ecdaeb6a916a16cf7eb69b19226c17be31a6bc27/README.md#installation) · [实现对照](https://github.com/btx0424/rethinking-supermimic/blob/ecdaeb6a916a16cf7eb69b19226c17be31a6bc27/README.md#ours-the-paper-and-supermimic_vibed)

- **作者：btx0424。** 在 mjlab 的 G1 跟踪任务中研究目标条件化：比较目标与本体观测直接拼接，以及用 FiLM 调制策略各层。
- **选择时注意：** 提供可配置观测、锚点选择及 Viser 回放；实现对照表解释了与论文、supermimic_vibed 在自碰撞、观测输入等方面的差异。 [核查版本](https://github.com/btx0424/rethinking-supermimic/blob/ecdaeb6a916a16cf7eb69b19226c17be31a6bc27/README.md)。

<a href="https://github.com/btx0424/rethinking-supermimic/blob/ecdaeb6a916a16cf7eb69b19226c17be31a6bc27/README.md"><img src="assets/community/rethinking-comparison.png" width="720" alt="实现对照表节选 · 前三项设计选择，点击查看完整对照"></a><br><sub>实现对照表节选 · 前三项设计选择，点击查看完整对照</sub>

<br>

### InstinctMJ · SuperMimic

[仓库](https://github.com/project-instinct/InstinctMJ/tree/supermimic) · [方法与结果](https://github.com/project-instinct/InstinctMJ/blob/7ca851e002980011f24a1664011305d0ba94aefc/src/instinct_mj/rl/supermimic/README.md#results) · [发布资源](https://github.com/project-instinct/InstinctMJ/releases)

- **团队：Project Instinct。** 在 mjlab / instinct_rl 中扩展到 G1 视觉动作跟踪和目标点跑酷；世界模型预测机器人状态及深度编码器潜变量，部分组件改编自 supermimic_vibed。
- **上游报告：** 单张 RTX 3090 训练 **8,000 次迭代 / 3.2 小时**，在 **5 类地形、10 个动作**上达到 **97% 完整动作成功率**；单种子，每个动作评估 12–13 次，开启相机噪声。
- **选择时注意：** 使用 **supermimic 分支**。这是地形跟踪任务，与平地 LAFAN1 不同；外部 checkpoint 需要适配关节顺序，许可为 CC BY-NC 4.0。 [核查版本](https://github.com/project-instinct/InstinctMJ/blob/7ca851e002980011f24a1664011305d0ba94aefc/src/instinct_mj/rl/supermimic/README.md)。

<a href="https://github.com/project-instinct/InstinctMJ/blob/7ca851e002980011f24a1664011305d0ba94aefc/src/instinct_mj/rl/supermimic/assets/world_model_simple.png"><img src="https://raw.githubusercontent.com/project-instinct/InstinctMJ/7ca851e002980011f24a1664011305d0ba94aefc/src/instinct_mj/rl/supermimic/assets/world_model_simple.png" width="720" alt="方法图 · 机器人状态与视觉潜变量预测"></a><br><sub>方法图 · 机器人状态与视觉潜变量预测</sub>

<br>

### SuperMimic-perceptive

[仓库](https://github.com/mode1223345/SuperMimic-perceptive) · [方法](https://github.com/mode1223345/SuperMimic-perceptive/blob/3d38bacbaf5bee7e782bdada6a6da678264d0bfa/Ae.md) · [进展记录](https://github.com/mode1223345/SuperMimic-perceptive/blob/3d38bacbaf5bee7e782bdada6a6da678264d0bfa/Progress.md)

- **作者：mode1223345。** 基于 Isaac Lab 3 的 supermimic_vibed，先预训练高程图自编码器，再冻结同一个编码器，供 actor、critic 和世界模型共享。
- **提供内容：** 记录平地／台阶地形上的四组控制对照，并单独提供重建检查；已发布的控制对照仍处于进行中。
- **选择时注意：** 当前使用仿真真值地图，尚未接入真实深度重建与真机感知；继承的基线成绩不能证明共享编码器带来控制收益。 [核查版本](https://github.com/mode1223345/SuperMimic-perceptive/blob/3d38bacbaf5bee7e782bdada6a6da678264d0bfa/README.md)。

<a href="https://github.com/mode1223345/SuperMimic-perceptive/blob/3d38bacbaf5bee7e782bdada6a6da678264d0bfa/results/Curves.png"><img src="https://raw.githubusercontent.com/mode1223345/SuperMimic-perceptive/3d38bacbaf5bee7e782bdada6a6da678264d0bfa/results/Curves.png" width="720" alt="训练曲线 · 2026-10-24 快照，控制对照实验仍在进行"></a><br><sub>训练曲线 · 2026-10-24 快照，控制对照实验仍在进行</sub>

<br>

### Go2-SuperMimic

[仓库](https://github.com/Zhengtianjin/go2-supermimic) · [快速开始](https://github.com/Zhengtianjin/go2-supermimic/blob/054a13c13285a1c94b2e69dc8ac7331f9a8c71cf/README.md#-quickstart) · [预训练策略](https://github.com/Zhengtianjin/go2-supermimic/blob/054a13c13285a1c94b2e69dc8ac7331f9a8c71cf/README.md#pretrained-policies)

- **作者：Zhengtianjin。** 在 mjlab 中将方法用于 Unitree Go2 追逐与闪避，覆盖平地、障碍和地形场景，接入激光或高度扫描输入。
- **提供内容：** 公开平地、障碍、地形三类 actor，以及评估与录制工具；仅下载 actor 可以回放，恢复训练还需要世界模型与 critic。
- **选择时注意：** 目前只有仿真验证，目标感知来自仿真真值；发布的地形策略在最难设置下仍会摔倒或撞杆。 [核查版本](https://github.com/Zhengtianjin/go2-supermimic/blob/054a13c13285a1c94b2e69dc8ac7331f9a8c71cf/README.md)。

<a href="https://github.com/Zhengtianjin/go2-supermimic"><img src="https://raw.githubusercontent.com/Zhengtianjin/go2-supermimic/054a13c13285a1c94b2e69dc8ac7331f9a8c71cf/resources/terrain.gif" width="480" alt="仿真 · Go2 地形追逐与闪避"></a><br><sub>仿真 · Go2 地形追逐与闪避</sub>

<br>

### Dex SuperMimic

[仓库](https://github.com/CumulusAlpha/Dex-Supermimic) · [安装](https://github.com/CumulusAlpha/Dex-Supermimic/blob/5ca57628af3666a9b2878c00f461f43d6edb5b61/README.md#download-and-installation) · [检查点](https://github.com/CumulusAlpha/Dex-Supermimic/releases/tag/pretrained-wuji-v1)

- **作者：CumulusAlpha。** 将世界模型策略训练用于 Wuji Hand 2 手内方块重定向，采用 mjlab / MuJoCo Warp 和 InstinctMJ 任务框架。
- **提供内容：** 提供 model_8000.pt 检查点与 Viser 回放；手部资产随包提供，预训练检查点需从 Releases 单独下载。
- **选择时注意：** 这是灵巧操作任务的适配，任务和奖励与人形动作跟踪不同。 [核查版本](https://github.com/CumulusAlpha/Dex-Supermimic/blob/5ca57628af3666a9b2878c00f461f43d6edb5b61/README.md)。

<a href="https://github.com/CumulusAlpha/Dex-Supermimic/blob/5ca57628af3666a9b2878c00f461f43d6edb5b61/teaser.jpg"><img src="https://raw.githubusercontent.com/CumulusAlpha/Dex-Supermimic/5ca57628af3666a9b2878c00f461f43d6edb5b61/teaser.jpg" width="480" alt="仿真截图 · Wuji Hand 2 手内方块重定向"></a><br><sub>仿真截图 · Wuji Hand 2 手内方块重定向</sub>

<br>

### SuperMimic for Robot Manipulation

[仓库](https://github.com/emoPointer/supermimic_manipulation) · [安装](https://github.com/emoPointer/supermimic_manipulation/blob/810e5768c50117d2fec75f20f9e643a11cd0882b/README.md#install) · [结果](https://github.com/emoPointer/supermimic_manipulation/blob/810e5768c50117d2fec75f20f9e643a11cd0882b/README.md#results)

- **作者：Zhiqiang Zhou（emoPointer）。** 在 mjlab / MuJoCo Warp 中把 SuperMimic 迁移到仿真 ARX5 机械臂的基于状态操作任务，包括 Lemon、BoxInBin 和 MugHang。
- **上游报告：** 各任务使用第 4,000 轮检查点，在独立测试 reset bank 上完成 256 个完整回合，Lemon、BoxInBin、MugHang 成功率分别为 **100.0%、94.9%、96.9%**；单张 A100 80 GB 共卡训练耗时 **1.8 / 1.9 / 2.8 小时**。
- **选择时注意：** 使用 OmniReset 式重置类别缩短有效时域，想象阶段以可微几何代理替换接触成功判据；策略只输入低维状态。检查点与 reset bank 已在 Hugging Face 发布。 [核查版本](https://github.com/emoPointer/supermimic_manipulation/blob/810e5768c50117d2fec75f20f9e643a11cd0882b/README.md)。

<a href="https://github.com/emoPointer/supermimic_manipulation"><img src="https://raw.githubusercontent.com/emoPointer/supermimic_manipulation/810e5768c50117d2fec75f20f9e643a11cd0882b/docs/media/lemon.gif" width="480" alt="仿真 · ARX5 Lemon 任务的两个保留初态回放"></a><br><sub>仿真 · ARX5 Lemon 任务 · 两个保留初态回放</sub>

<br>

### Humanoid Mimic · SuperMimic

[仓库](https://github.com/shuayyy/humanoid-amp-ppo) · [快速开始](https://github.com/shuayyy/humanoid-amp-ppo/blob/4889389118e0c88d3945dff54d2cd3f992ed815e/README.md#quickstart) · [结果与协议](https://github.com/shuayyy/humanoid-amp-ppo/blob/4889389118e0c88d3945dff54d2cd3f992ed815e/docs/supermimic/RESULTS.md)

- **作者：shuayyy。** 在 mjlab 的同一组 G1 行走、下蹲和搬箱任务上对照 SuperMimic 与 PPO-Sim，仓库另含独立的 AMP-PPO 路线。
- **上游报告：** 两个 SuperMimic 种子在 **3,100 万环境步**时，64 回合随机评测的搬箱成功率达到 **100%**；成功条件是结束时箱子高度距参考值不超过 10 cm。
- **选择时注意：** 上述 SuperMimic 分数使用无噪声观测；新版评估已加入观测噪声，公开检查点尚未按这一设置重评。 [核查版本](https://github.com/shuayyy/humanoid-amp-ppo/blob/4889389118e0c88d3945dff54d2cd3f992ed815e/README.md)。

<a href="https://github.com/shuayyy/humanoid-amp-ppo/blob/4889389118e0c88d3945dff54d2cd3f992ed815e/assets/supermimic_vs_ppo_lift.mp4"><img src="https://raw.githubusercontent.com/shuayyy/humanoid-amp-ppo/4889389118e0c88d3945dff54d2cd3f992ed815e/assets/supermimic_vs_ppo_lift.gif" width="480" alt="搬箱 · SuperMimic 12k / PPO-Sim 6k 次迭代"></a><br><sub>搬箱 · SuperMimic 12k / PPO-Sim 6k 次迭代</sub>

<br>

### Muscle SuperMimic

[仓库](https://github.com/kaibohex/muscle-supermimic) · [安装](https://github.com/kaibohex/muscle-supermimic/blob/b7c7cdd83e82399e057cb9d3f1b76f23ca022c7b/README.md#install) · [当前状态](https://github.com/kaibohex/muscle-supermimic/blob/b7c7cdd83e82399e057cb9d3f1b76f23ca022c7b/README.md#status)

- **作者：Kaibo He（kaibohex）。** 在 mjlab / MuJoCo Warp 中将 SuperMimic 扩展到肌肉驱动全身动作跟踪，支持 MS-Human-700（700 块肌肉）和 MyoFullBody（354 块肌肉）。
- **上游报告：** 使用 4,096 个环境、单张 RTX 5090，在 MuscleMimic 的 108 条 KIT 保留动作上，MS-Human-700 训练 **10.1 小时**达到归一化回报 **0.91**（第 16k 轮，**104 / 108** 完成）；MyoFullBody 训练 **6.0 小时**达到 **0.83**（第 10k 轮，**101 / 108** 完成）。
- **选择时注意：** 项目仍在持续更新；策略以 100 Hz 控制每块肌肉的激励，提供可微 torch 肌肉模型和重定向工具。KIT 数据需接受许可，AMASS 数据与重定向结果不得再分发；MS-Human-700 以 Git 子模块提供。 [核查版本](https://github.com/kaibohex/muscle-supermimic/blob/b7c7cdd83e82399e057cb9d3f1b76f23ca022c7b/README.md)。

<a href="https://github.com/kaibohex/muscle-supermimic"><img src="https://raw.githubusercontent.com/kaibohex/muscle-supermimic/b7c7cdd83e82399e057cb9d3f1b76f23ca022c7b/docs/assets/teaser_three.gif" width="480" alt="仿真 · 第 10000 轮 MS-Human-700 与 MyoFullBody 跟踪 KIT 动作"></a><br><sub>仿真 · MS-Human-700 与 MyoFullBody · 第 10000 轮</sub>

<br>

### SuperMimic-PERA

[仓库](https://github.com/shangchaohu718/supermimic-pera) · [当前状态](https://github.com/shangchaohu718/supermimic-pera/blob/0e89e55187a800341e609129b5d5200a607a467c/README.md#当前状态) · [滑板实验](https://github.com/shangchaohu718/supermimic-pera/blob/0e89e55187a800341e609129b5d5200a607a467c/docs/FIRST_SKATEBOARD_SKILL.md)

- **作者：shangchaohu718。** 基于 UniSuperMimic 开展 G1 交互实验，在 UniLab / MuJoCo 中冻结原跟踪器，再开发独立交互策略。
- **上游报告：** 独立滑板策略从 1 个标准初态和 8 个保留扰动初态出发，均完成 30 秒仿真滑行，前进 **39.87–42.13 m**。
- **选择时注意：** 跟踪与滑板仍需显式选择不同分支，尚未形成共享世界模型驱动的通用交互 actor；报告中的搬箱和楼梯原型尚未达到成功条件。 [核查版本](https://github.com/shangchaohu718/supermimic-pera/blob/0e89e55187a800341e609129b5d5200a607a467c/README.md)。

<a href="https://github.com/shangchaohu718/supermimic-pera/blob/0e89e55187a800341e609129b5d5200a607a467c/README.md"><img src="assets/community/pera-tracking-results.png" width="720" alt="报告截图 · 跟踪检查点 500–6000，与滑板实验分开"></a><br><sub>报告截图 · 跟踪检查点 500–6000，与滑板实验分开</sub>

<br>

### SuperMimic Backflip Diagnostics

[仓库](https://github.com/liudi159/supermimic-backflip-5090) · [结果](https://github.com/liudi159/supermimic-backflip-5090/blob/5b313d75e804cdd2ff1ce9bdcfa899a98eca856b/README.md#结果) · [快速入口](https://github.com/liudi159/supermimic-backflip-5090/blob/5b313d75e804cdd2ff1ce9bdcfa899a98eca856b/README.md#快速入口)

- **作者：liudi159。** 使用 Isaac Lab 3 和单张 RTX 5090 专项研究 G1 后空翻，记录双腿对称性、接触力、穿透和落地稳定性。
- **上游报告：** 最终 V14 检查点完成后翻与落地保持，但原始严格评测记录到 1 帧非脚部穿透，**仍未通过验收**。
- **选择时注意：** 独立重评的临界接触结果出现变化，两次记录均保留；演示不能据此表述为稳健成功或论文全部实验复现。 [核查版本](https://github.com/liudi159/supermimic-backflip-5090/blob/5b313d75e804cdd2ff1ce9bdcfa899a98eca856b/README.md)。

<a href="https://github.com/liudi159/supermimic-backflip-5090/blob/5b313d75e804cdd2ff1ce9bdcfa899a98eca856b/media/v14_blue_checker.mp4"><img src="assets/community/backflip.gif" width="480" alt="仿真 · 最终 V14 策略；严格评估未通过"></a><br><sub>仿真 · 最终 V14 策略；严格评估未通过</sub>

<br>

## 框架、本体适配与部署

按仿真框架和机器人本体选择训练、重定向、模型导出与部署工具。

### ScaleBFM_Plus · SuperMimic

[仓库](https://github.com/Hxxxz0/ScaleBFM_Plus) · [训练与结果](https://github.com/Hxxxz0/ScaleBFM_Plus/blob/65e4d524bd31fdc4284ba8c6e624fb0b0127da03/ScaleTrack/README.md#fast-training-with-a-learned-world-model-supermimic) · [发布权重](https://github.com/Hxxxz0/ScaleBFM_Plus/tree/65e4d524bd31fdc4284ba8c6e624fb0b0127da03/ScaleTrack/checkpoints/supermimic_m)

- **作者：Hxxxz0，基于 ScaleBFM 扩展。** 在 IsaacLab / RSL-RL 的 G1 ScaleTrack 流程中接入 SuperMimic 式世界模型学习与 32 步 BPTT，保留 humanoid transformer 和跟踪模式，支持兼容 PPO 格式的策略导出与回放。
- **上游报告：** 使用 BONES-SEED、any4hdmi、LAFAN1 共 **309 小时 / 13.8 万条动作**，在 **16 张 RTX 5090 上训练 8.3 小时**，对 **2,575 条留出测试动作**报告 **99.5% 跟踪成功率**。在 386 条高动态测试动作中，该策略与官方 ScaleBFM-M 检查点均成功 **376 / 386**，平均全局身体位置误差分别为 **6.35 cm** 和 **6.43 cm**。
- **选择时注意：** 这是 ScaleBFM 的社区扩展。报告的 **26× 单步提速**对比的是 **16 张 RTX 5090 上的 0.65 秒**与 PPO 在 **8 张 RTX 5090 上的 17.0 秒**，并非相同算力或达到同等质量所需时间的对照。 [核查版本](https://github.com/Hxxxz0/ScaleBFM_Plus/blob/65e4d524bd31fdc4284ba8c6e624fb0b0127da03/ScaleTrack/README.md)。

<a href="https://github.com/Hxxxz0/ScaleBFM_Plus/blob/65e4d524bd31fdc4284ba8c6e624fb0b0127da03/ScaleTrack/assets/demos/supermimic_vs_official.gif"><img src="https://media.githubusercontent.com/media/Hxxxz0/ScaleBFM_Plus/65e4d524bd31fdc4284ba8c6e624fb0b0127da03/ScaleTrack/assets/demos/supermimic_vs_official.gif" width="480" alt="仿真 · 官方 ScaleBFM-M（左）与 SuperMimic（右），未见 LAFAN 舞蹈"></a><br><sub>仿真 · 官方 ScaleBFM-M（左）与 SuperMimic（右），未见 LAFAN 舞蹈 · 来源：Hxxxz0 / ScaleBFM_Plus</sub>

<br>

### HoloMotion · SuperMimic

[仓库](https://github.com/HorizonRobotics/HoloMotion) · [训练指南](https://github.com/HorizonRobotics/HoloMotion/blob/adaacd50ada6ba9338f6c3f539093f85453e2554/docs/supermimic.md) · [结果](https://github.com/HorizonRobotics/HoloMotion/blob/adaacd50ada6ba9338f6c3f539093f85453e2554/docs/supermimic.md#7-recorded-30-minute-results)

- **团队：Horizon Robotics。** 将 SuperMimic 接入 HoloMotion 的 G1 资产、HDF5 动作数据和 Hydra 流程，在 MuJoCo Warp 与 Isaac PhysX 上共用 PPO 的任务和评测接口。
- **上游报告：** 选定的 MuJoCo Warp 配置在单张 RTX 5090 上训练 **30 分钟**后，完整通过 **32 / 40 条 LAFAN1 训练动作**。
- **选择时注意：** 已验证路线使用紧凑策略；预览来自另一轮运行的短片段，不能替代完整动作评测，也不代表规划中的大策略集成已经验证。 [核查版本](https://github.com/HorizonRobotics/HoloMotion/blob/adaacd50ada6ba9338f6c3f539093f85453e2554/docs/supermimic.md)。

<a href="https://github.com/HorizonRobotics/HoloMotion"><img src="https://raw.githubusercontent.com/HorizonRobotics/HoloMotion/adaacd50ada6ba9338f6c3f539093f85453e2554/docs/media/supermimic_training_progress.webp" width="480" alt="仿真 · PPO / SuperMimic，两个仿真后端"></a><br><sub>仿真 · PPO / SuperMimic，两个仿真后端</sub>

<br>

### TrackerLab SuperMimic

[仓库](https://github.com/Renforce-Dynamics/trackerlab-supermimic) · [安装](https://github.com/Renforce-Dynamics/trackerlab-supermimic/blob/29d24524f2f731bf4df75b319c3e76544165849e/README.md#install) · [结果与限制](https://github.com/Renforce-Dynamics/trackerlab-supermimic/blob/29d24524f2f731bf4df75b319c3e76544165849e/docs/results.md)

- **团队：Renforce Dynamics。** 在 Isaac Lab / PhysX 中提供统一的重定向、训练、完整动作评估与导出流程，覆盖 G1、Go2、A3、T1、Bumi 和 Pi+，另含 Go2 任务策略。
- **上游报告：** 重新评估第 32,000 次迭代的 G1 上游检查点，得到归一化回报 **0.8694663、0 / 40 条 LAFAN1 动作失败**。
- **选择时注意：** 结果使用 PhysX，而 supermimic_vibed 使用 MuJoCo Warp；各本体的动作库与训练过程不同，未见动作泛化仍未测量。 [核查版本](https://github.com/Renforce-Dynamics/trackerlab-supermimic/blob/29d24524f2f731bf4df75b319c3e76544165849e/README.md)。

<a href="https://github.com/Renforce-Dynamics/trackerlab-supermimic/blob/29d24524f2f731bf4df75b319c3e76544165849e/docs/media/g1_dance_032000.mp4"><img src="https://raw.githubusercontent.com/Renforce-Dynamics/trackerlab-supermimic/29d24524f2f731bf4df75b319c3e76544165849e/docs/media/g1_dance_032000.gif" width="480" alt="仿真 · G1 策略与参考舞蹈"></a><br><sub>仿真 · G1 策略与参考舞蹈</sub>

<br>

### UniSuperMimic

[仓库](https://github.com/Motphys/Uni-SuperMimic) · [安装](https://github.com/Motphys/Uni-SuperMimic/blob/faf7818e8abac3ec6abb8f00e6e904d3577f800b/README.md#installation) · [结果](https://github.com/Motphys/Uni-SuperMimic/blob/faf7818e8abac3ec6abb8f00e6e904d3577f800b/README.md#results)

- **团队：Motphys。** 将 supermimic_vibed 移植到 UniLab 的 Manager-Based G1 任务，提供资产准备、仿真后端选择、确定性完整动作评估和视频导出。
- **上游报告：** 采用 UniLab 1.5.0、mjwarp 和 4,096 个训练环境，第 **12,000** 次迭代的逐动作平均归一化回报为 **0.827227**，**0 / 40 条 LAFAN1/G1 动作失败**。
- **选择时注意：** 已报告跟踪成绩使用 mjwarp；MuJoCo 和 Motrix 的运行入口不代表已经取得相同训练成绩。 [核查版本](https://github.com/Motphys/Uni-SuperMimic/blob/faf7818e8abac3ec6abb8f00e6e904d3577f800b/README.md)。

<a href="https://github.com/Motphys/Uni-SuperMimic/blob/faf7818e8abac3ec6abb8f00e6e904d3577f800b/docs/assets/supermimic_comparison.mp4"><img src="https://raw.githubusercontent.com/Motphys/Uni-SuperMimic/faf7818e8abac3ec6abb8f00e6e904d3577f800b/docs/assets/supermimic_comparison.gif" width="480" alt="仿真 · G1 跳跃跟踪"></a><br><sub>仿真 · G1 跳跃跟踪</sub>

<br>

### SuperMimic Lab

[仓库](https://github.com/chu-fa/isaaclab-supermimic) · [安装](https://github.com/chu-fa/isaaclab-supermimic/blob/d350e4378c6dc08a3f2a1d35d47b45d83db0e081/docs/SETUP.md) · [自定义任务](https://github.com/chu-fa/isaaclab-supermimic/blob/d350e4378c6dc08a3f2a1d35d47b45d83db0e081/docs/CUSTOM_TASKS.md)

- **作者：chu-fa。** 将 SuperMimic learner 和 runner 整理为可复用的 Isaac Lab 自定义任务接口，附可单独安装的 AGIBOT A3 示例。
- **提供内容：** 提供任务接口约定、安装说明和后端验证记录；自定义任务需要提供可微状态、观测、奖励与终止函数。
- **选择时注意：** 面向 Isaac Lab 3 开发版 API；A3 预览中的各片段独立初始化，尚未确立收敛、后端等价性或真机部署结果。 [核查版本](https://github.com/chu-fa/isaaclab-supermimic/blob/d350e4378c6dc08a3f2a1d35d47b45d83db0e081/README.md)。

<a href="https://github.com/chu-fa/isaaclab-supermimic"><img src="https://raw.githubusercontent.com/chu-fa/isaaclab-supermimic/d350e4378c6dc08a3f2a1d35d47b45d83db0e081/docs/media/a3_reference_vs_policy.webp" width="480" alt="A3 参考 / 策略 · 各片段分别初始化"></a><br><sub>A3 参考 / 策略 · 各片段分别初始化</sub>

<br>

### SuperMimicKit

[仓库](https://github.com/OMEGA-i/SuperMimicKit) · [预览版发布](https://github.com/OMEGA-i/SuperMimicKit/releases/tag/demo-preview-20261024) · [评估与限制](https://github.com/OMEGA-i/SuperMimicKit/blob/6697ff8ca53adc9233ded12a7c8777610ca1154d/docs/preview-release.md)

- **团队：OMEGA-i。** 面向 G1、H2 和 A3 的独立 MuJoCo Warp 实现，提供动作重定向、策略／世界模型 ONNX 导出及 WebGPU 浏览器预览。
- **上游报告：** 分别公开 G1/H2 的 train40 与未见动作 val37 评估。G1 55.5k 预览在 train40 上为 **0.7990、3 / 40 失败**，val37 上为 **0.3103、31 / 37 失败**；A3 100k 完整动作评估仍待完成。
- **选择时注意：** 当前是实验性预览，未见动作跟踪较弱，后期检查点出现过回退；需自行提供获许可的动作数据，核查版本中未找到仓库顶层代码许可证。 [核查版本](https://github.com/OMEGA-i/SuperMimicKit/blob/6697ff8ca53adc9233ded12a7c8777610ca1154d/README.md)。

<a href="https://github.com/OMEGA-i/SuperMimicKit/blob/6697ff8ca53adc9233ded12a7c8777610ca1154d/docs/media/teaser.mp4"><img src="https://raw.githubusercontent.com/OMEGA-i/SuperMimicKit/6697ff8ca53adc9233ded12a7c8777610ca1154d/docs/media/teaser.gif" width="480" alt="浏览器预览 · G1 / H2 / A3"></a><br><sub>浏览器预览 · G1 / H2 / A3</sub>

<br>

### SuperMimic Retargeted

[仓库](https://github.com/tianshuwu/supermimic-retargeted) · [快速开始](https://github.com/tianshuwu/supermimic-retargeted/blob/ff69a0e5305126eb5b80b323bcd815805bc3df4e/README.md#快速开始) · [数据说明](https://github.com/tianshuwu/supermimic-retargeted/blob/ff69a0e5305126eb5b80b323bcd815805bc3df4e/docs/DATA.md)

- **作者：tianshuwu。** 基于 CuboiLeo 的 mjlab 复现适配 G1、A3 与 X2 Ultra，加入本体运动学、SOMA 重定向、坐标修正及脚底接触检查。
- **提供内容：** 公开 LAFAN1/BONES-SEED 数据准备流程和历史评测记录；训练权重不随仓库发布，动作数据需另行准备。
- **选择时注意：** 已报告策略增加了从仿真真值计算的锚点相对观测，真机需有对应的状态估计；尚未完成实机验证。 [核查版本](https://github.com/tianshuwu/supermimic-retargeted/blob/ff69a0e5305126eb5b80b323bcd815805bc3df4e/README.md)。

<a href="https://github.com/tianshuwu/supermimic-retargeted/blob/ff69a0e5305126eb5b80b323bcd815805bc3df4e/media/demo.mp4"><img src="https://raw.githubusercontent.com/tianshuwu/supermimic-retargeted/ff69a0e5305126eb5b80b323bcd815805bc3df4e/media/demo-preview.gif" width="480" alt="仿真 · G1 / X2 Ultra / A3"></a><br><sub>仿真 · G1 / X2 Ultra / A3</sub>

<br>

### SuperMimic E1

[仓库](https://github.com/wenconggan/SuperMimic_e1) · [安装与资源](https://github.com/wenconggan/SuperMimic_e1/blob/d5fbe8f219c438b84633130652c5e6e74beff628/README.md#安装与资源) · [结果](https://github.com/wenconggan/SuperMimic_e1/blob/d5fbe8f219c438b84633130652c5e6e74beff628/README.md#已测结果)

- **作者：wenconggan。** 将 Isaac Lab 3 实现适配到 21 自由度 DroidUp E1，提供独立的原生 MuJoCo sim-to-sim 回放与评估。
- **上游报告：** 164k 检查点在 Isaac Lab 中完成 **40 / 40 条训练动作**，回报 **0.8559**；另一个 168k 检查点在原生 MuJoCo 中完成 **10 / 10 个抽样的 8 秒片段**。
- **选择时注意：** 完整动作评测与独立初始化短片段采用不同协议，两者都不代表未见动作泛化或真机迁移。 [核查版本](https://github.com/wenconggan/SuperMimic_e1/blob/d5fbe8f219c438b84633130652c5e6e74beff628/README.md)。

<a href="https://github.com/wenconggan/SuperMimic_e1/blob/d5fbe8f219c438b84633130652c5e6e74beff628/docs/assets/e1_random10_80s.mp4"><img src="https://raw.githubusercontent.com/wenconggan/SuperMimic_e1/d5fbe8f219c438b84633130652c5e6e74beff628/docs/assets/e1_preview.gif" width="480" alt="E1 sim2sim · 原生 MuJoCo"></a><br><sub>E1 sim2sim · 原生 MuJoCo</sub>

<br>

### SuperMimic Oli

[仓库](https://github.com/liuskywalkerjskd/supermimic_oli) · [安装](https://github.com/liuskywalkerjskd/supermimic_oli/blob/2dc90d90e89fb2e097e985c84c8b99a77708fa5f/README.md#setup) · [结果](https://github.com/liuskywalkerjskd/supermimic_oli/blob/2dc90d90e89fb2e097e985c84c8b99a77708fa5f/README.md#results)

- **作者：liuskywalkerjskd。** 在 Isaac Lab 3 中将 supermimic_vibed 移植到 31 自由度 LimX Oli，加入动作重定向、本体运动学和完整动作视频导出。
- **上游报告：** 单张 RTX 4090 训练约 **2.20 小时**，第 **18,000** 次迭代的原始 40 条 LAFAN1 动作评测为回报 **0.6783、36 / 40 完成**。
- **选择时注意：** 展示的行走动图是选定片段；判断动作覆盖情况时应查看完整动作库评测。 [核查版本](https://github.com/liuskywalkerjskd/supermimic_oli/blob/2dc90d90e89fb2e097e985c84c8b99a77708fa5f/README.md)。

<a href="https://github.com/liuskywalkerjskd/supermimic_oli/blob/2dc90d90e89fb2e097e985c84c8b99a77708fa5f/results/oli_walk1_subject1_full.mp4"><img src="https://raw.githubusercontent.com/liuskywalkerjskd/supermimic_oli/2dc90d90e89fb2e097e985c84c8b99a77708fa5f/results/oli_walk1_subject1_preview.gif" width="480" alt="仿真 · Oli 行走精选片段"></a><br><sub>仿真 · Oli 行走精选片段</sub>

<br>

### SuperMimic on Apple M5

[仓库](https://github.com/WXyuany/supermimic-m5) · [运行已训练模型](https://github.com/WXyuany/supermimic-m5/blob/42451591718e1a9a5ec601366997f47c0ad180a3/README.md#三步运行已训练模型) · [结果](https://github.com/WXyuany/supermimic-m5/blob/42451591718e1a9a5ec601366997f47c0ad180a3/README.md#实验结果)

- **作者：WXyuany。** 将 CuboiLeo 的 G1 复现适配到 Apple Silicon，用 CPU MuJoCo 运行物理仿真、PyTorch MPS 训练，附公开权重与回放工具。
- **上游报告：** 24 GB Apple M5、seed 0 的公开 21k 检查点，原始 40 条动作评测为回报 **0.7081、25 / 40 完成**；独立新环境复核为 **26 / 40 完成**。
- **选择时注意：** 回报按已执行步数归一化，失败后的剩余帧不补零，actor 额外使用 9 维锚点观测；需结合完成率阅读，未测试未见动作泛化。 [核查版本](https://github.com/WXyuany/supermimic-m5/blob/42451591718e1a9a5ec601366997f47c0ad180a3/README.md)。

<a href="https://github.com/WXyuany/supermimic-m5/blob/42451591718e1a9a5ec601366997f47c0ad180a3/assets/videos/walk1_subject1.mp4"><img src="https://raw.githubusercontent.com/WXyuany/supermimic-m5/42451591718e1a9a5ec601366997f47c0ad180a3/assets/images/walk-preview.gif" width="480" alt="仿真 · Apple M5 上的 G1 行走"></a><br><sub>仿真 · Apple M5 上的 G1 行走</sub>

<br>

### SuperMimic-MuJoCo

[仓库](https://github.com/panhainan2020/SuperMimic-MuJoCo) · [安装](https://github.com/panhainan2020/SuperMimic-MuJoCo/blob/db045afa9c52458f213e2c66037387e9c109a03a/README.md#环境安装) · [评测](https://github.com/panhainan2020/SuperMimic-MuJoCo/blob/db045afa9c52458f213e2c66037387e9c109a03a/README.md#评估结果)

- **作者：panhainan2020。** 面向 G1 的独立 mjlab / CPU MuJoCo 移植，基于 supermimic_vibed，提供观测兼容配置、推理权重及未见 100STYLE 动作评测。
- **上游报告：** 固定 98k 策略完成 **40 / 40 条 LAFAN 训练动作**，回报 **0.8713**；未经微调完成 **3,569 / 3,573 条未见 100STYLE 片段**，回报 **0.8045**。
- **选择时注意：** 两组数据的时长和重定向流程不同；“完成”表示没有触发终止条件，不代表复现了论文完整训练日程或全部实验。 [核查版本](https://github.com/panhainan2020/SuperMimic-MuJoCo/blob/db045afa9c52458f213e2c66037387e9c109a03a/README.md)。

<a href="https://github.com/panhainan2020/SuperMimic-MuJoCo/blob/db045afa9c52458f213e2c66037387e9c109a03a/README.md"><img src="assets/community/mujoco-evaluation.png" width="720" alt="报告截图 · LAFAN 训练动作与未见 100STYLE 动作"></a><br><sub>报告截图 · LAFAN 训练动作与未见 100STYLE 动作</sub>

[完整视频展示](https://supermimic-mujoco-results.zippyaspen7.chatgpt.site)

<br>

### SuperMimic-Repro-Sim2Real

[仓库](https://github.com/NJU-R-L-Group-Embodied-Lab/SuperMimic-Repro-Sim2Real) · [快速开始](https://github.com/NJU-R-L-Group-Embodied-Lab/SuperMimic-Repro-Sim2Real/blob/99d310d5460333aabe853337b1d55ee27940a3fe/README.md#快速开始) · [G1 部署](https://github.com/NJU-R-L-Group-Embodied-Lab/SuperMimic-Repro-Sim2Real/blob/99d310d5460333aabe853337b1d55ee27940a3fe/docs/DEPLOY_G1.md)

- **团队：NJU R&amp;L Group Embodied Lab。** 在 CuboiLeo 的 mjlab 复现上增加自定义舞蹈、视频动作工具、ONNX 导出，以及原生 MuJoCo 和 Unitree SDK 的 G1 部署流程。
- **上游报告：** 公开一段由四个动作片段组成、约 **46 秒的 G1 真机舞蹈**，并提供预训练模型与原始视频。
- **选择时注意：** README 区分按论文观测训练与增加锚点观测的训练；后者依赖该真机部署配置无法提供的全局相对信息。 [核查版本](https://github.com/NJU-R-L-Group-Embodied-Lab/SuperMimic-Repro-Sim2Real/blob/99d310d5460333aabe853337b1d55ee27940a3fe/README.md)。

<a href="https://github.com/NJU-R-L-Group-Embodied-Lab/SuperMimic-Repro-Sim2Real/releases/download/v1.0/shanshenbu_real_robot_v3.mp4"><img src="https://raw.githubusercontent.com/NJU-R-L-Group-Embodied-Lab/SuperMimic-Repro-Sim2Real/99d310d5460333aabe853337b1d55ee27940a3fe/docs/assets/shanshenbu_demo.gif" width="480" alt="G1 真机 · 舞蹈与人类参考"></a><br><sub>G1 真机 · 舞蹈与人类参考</sub>

<br>

### SuperMimic G1 Deployment

[仓库](https://github.com/KyrieYoung926/supermimic_deploy) · [MuJoCo 使用](https://github.com/KyrieYoung926/supermimic_deploy/blob/7e63e3bbd5150d55afbdece28278781800f3ed21/README.md#3-run-in-mujoco) · [真机使用](https://github.com/KyrieYoung926/supermimic_deploy/blob/7e63e3bbd5150d55afbdece28278781800f3ed21/README.md#4-run-on-the-real-g1)

- **作者：KyrieYoung926。** 面向 29 自由度 G1 部署 SuperMimic-Reproduced 策略，采用 ONNX Runtime、MuJoCo 和 Unitree SDK2。
- **提供内容：** 提供仿真与 G1 真机演示，并分别说明如何准备部署资产、在仿真和真机上运行策略。
- **选择时注意：** 仓库重点是部署，不是新的训练基准；动作数据、模型权重和机器人资产保留各自条款，不由代码许可证统一覆盖。 [核查版本](https://github.com/KyrieYoung926/supermimic_deploy/blob/7e63e3bbd5150d55afbdece28278781800f3ed21/README.md)。

<a href="https://github.com/KyrieYoung926/supermimic_deploy"><img src="https://raw.githubusercontent.com/KyrieYoung926/supermimic_deploy/7e63e3bbd5150d55afbdece28278781800f3ed21/media/deploy_real.gif" width="480" alt="G1 真机 · 上游部署演示"></a><br><sub>G1 真机 · 上游部署演示</sub>

<br>

## 方法借鉴与探索

将方法思路迁移到其他控制场景；任务和评估协议各不相同。

### Ref2Dex · Dex Contact MBRL

[仓库](https://github.com/hitsz-oyx/Ref2Dex-agent) · [任务与结果](https://github.com/hitsz-oyx/Ref2Dex-agent/blob/31cdb9ac759838b83d62bbc0addfd5cf28f3dff4/src/task/dex-contact-mbrl/README.md)

- **作者：hitsz-oyx。** 在 Isaac Gym / DExplore 的 Inspire 手任务中，探索动作条件接触动力学和短时 BPTT，结合接触记忆与原生碰撞几何查询。
- **提供内容：** 分别记录行为克隆、动力学拟合、受限的 actor/critic 更新和原生物理评估。
- **选择时注意：** 已报告对照中，参考动作存活率提高的同时平均回报下降；尚未确立可靠的模型控制收益，接触代理指标也不等于抓取成功。 [核查版本](https://github.com/hitsz-oyx/Ref2Dex-agent/blob/31cdb9ac759838b83d62bbc0addfd5cf28f3dff4/src/task/dex-contact-mbrl/README.md)。

<a href="https://github.com/hitsz-oyx/Ref2Dex-agent/blob/31cdb9ac759838b83d62bbc0addfd5cf28f3dff4/src/task/dex-contact-mbrl/docs/CONTACT-REFINEMENT-RESULTS-20261026.md"><img src="assets/community/contact-bptt-results.png" width="720" alt="报告截图 · 原生物理对照；参考动作存活率提高，平均回报降低"></a><br><sub>报告截图 · 原生物理对照；参考动作存活率提高，平均回报降低</sub>

<br>

### G0.5 · SuperMimic-style Steering

[仓库](https://github.com/azizkhadraoui/g05) · [实验代码](https://github.com/azizkhadraoui/g05/blob/e3de0de50db7d90068483e2d30f2eacd781300b4/jobs/119_smsteer.py)

- **作者：azizkhadraoui。** 将 SuperMimic 式梯度学习借鉴到 LIBERO 上的 G0.5 VLA 引导：通过世界模型、critic 和冻结流匹配采样器训练噪声策略。
- **选择时注意：** 这是更大 VLA 系统中的一个特定任务引导实验；所链接脚本对应相关方法，仓库中其他规划与记忆结果属于不同实验。 [核查版本](https://github.com/azizkhadraoui/g05/blob/e3de0de50db7d90068483e2d30f2eacd781300b4/jobs/119_smsteer.py)。

<a href="https://github.com/azizkhadraoui/g05/blob/e3de0de50db7d90068483e2d30f2eacd781300b4/README.md"><img src="assets/community/g05-steering-entry.png" width="720" alt="代码索引截图 · 世界模型与 critic 引导实验"></a><br><sub>代码索引截图 · 世界模型与 critic 引导实验</sub>

<br>

### FlatWorld · SuperMimic-2D

[仓库](https://github.com/swaggyliu/FlatWorld) · [快速开始](https://github.com/swaggyliu/FlatWorld/blob/207e9e9c61ef21b8f145c3e0c4d8b121a03bf45a/supermimic2d/README.md#quick-start) · [参考动作](https://github.com/swaggyliu/FlatWorld/blob/207e9e9c61ef21b8f145c3e0c4d8b121a03bf45a/supermimic2d/README.md#reference-motions-lafan-like-2d)

- **作者：swaggyliu。** 用八关节二维人形角色，在 FlatWorld 中实现共享世界模型与想象策略学习的动作跟踪流程。
- **提供内容：** 提供训练、参考动作物理处理、逐技能渲染与多技能展示，包含行走、跑步、跳跃、舞蹈等动作。
- **选择时注意：** 参考动作是程序生成的 LAFAN 风格二维动作，并非 LAFAN1 数据集；角色还使用轻度根部辅助，因此适合作为方法示例，不是 G1 基准复现。 [核查版本](https://github.com/swaggyliu/FlatWorld/blob/207e9e9c61ef21b8f145c3e0c4d8b121a03bf45a/supermimic2d/README.md)。

<a href="https://github.com/swaggyliu/FlatWorld/blob/207e9e9c61ef21b8f145c3e0c4d8b121a03bf45a/supermimic2d/runs/lafan2d/showcase_30s.mp4"><img src="assets/community/flatworld.gif" width="480" alt="二维仿真 · 动作跟踪集锦"></a><br><sub>二维仿真 · 动作跟踪集锦</sub>

## 相关方法与基线

以下是帮助理解方法背景和比较对象的独立研究工作。

| 工作 | 与本清单的关系 | 一手资料 |
| --- | --- | --- |
| **SuperTrack**（2021） | 较早通过学习可微世界模型与梯度优化训练物理角色动作跟踪策略的工作。 | [作者讲解](https://www.ubisoft.com/en-us/studio/laforge/news/7fMzaMaDgnd0gqPsCaJZYb/supertrack-motion-tracking-for-physically-simulated-characters-using-supervised-learning) · [论文](https://staticctf.ubisoft.com/J3yJr34U2pZ2Ieem48Dwy9uqj5PNUQTn/OXYoOEqVwwtxSMiPzMIva/302e9a76da0b1f95ab62d6c766179868/SuperTrack.pdf) |
| **BeyondMimic**（2025） | 人形动作跟踪与引导扩散控制；`supermimic_vibed` 参考其执行器和任务设置。 | [项目](https://beyondmimic.github.io/) · [论文](https://arxiv.org/abs/2508.08241) |
| **SONIC**（2025） | 大规模人形动作跟踪；原始 SuperMimic 使用其已发布 checkpoint 作为比较对象。 | [项目](https://nvlabs.github.io/GEAR-SONIC/) · [论文](https://arxiv.org/abs/2511.07820) · [代码](https://github.com/NVlabs/GR00T-WholeBodyControl) |

## 数据与学习资源

- [LAFAN1 重定向数据集](https://huggingface.co/datasets/lvhaidong/LAFAN1_Retargeting_Dataset)：`supermimic_vibed`、UniSuperMimic 与 SuperMimic-Reproduced 使用的 G1 动作资产；按各项目的准备流程及数据自身条款使用。
- [BONES-SEED](https://huggingface.co/datasets/bones-studio/seed)：原论文大规模 benchmark 使用的动作数据来源。原始数据集与论文过滤后的评估集数量不同；访问文件需要在 Hugging Face 接受数据条款。
- [官方交互演示](https://supermimic.github.io/demo/)：先在浏览器中体验原始策略，再选择训练框架。
- [官方方法讲解](https://supermimic.github.io/#loop)：了解仿真采集、世界模型拟合和策略学习。
- [InstinctMJ 发布页](https://github.com/project-instinct/InstinctMJ/releases)：任务数据与模型资产的上游入口，按发布说明确认适用分支与任务。

## 参与贡献

欢迎通过 PR 添加新实现、扩展、教程或演示。请阅读[贡献指南](CONTRIBUTING.md)，提供原始来源、与 SuperMimic 的关系、所需分支，以及所引用结果的证据。

## 论文引用

使用方法时请引用**原始 SuperMimic 论文**，同时注明所使用的具体实现。以下 BibTeX 来自[官方项目](https://supermimic.github.io/#cite)：

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

## 致谢与许可

感谢 SuperMimic 原作者和社区维护者。清单的组织和展示参考了 [Awesome Nano Banana Images](https://github.com/PicoTrex/Awesome-Nano-Banana-images) 与 [Awesome World Models](https://github.com/knightnemo/Awesome-World-Models)。

本清单原创整理文字采用 [CC0 1.0](LICENSE)。第三方代码、论文、数据及媒体保留各自的权利与使用条款，包括存放在本仓库中的[原论文框架图与官方视频预览](assets/official/README.md)；这些素材不属于本清单的 CC0 授权范围。[社区媒体预览与来源](assets/community/README.md)同样保留原作者权利。
