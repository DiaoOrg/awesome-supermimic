# 社区项目详情

[返回排行榜](../README_zh-CN.md#most-starred-projects) · [English](community-projects.md)

以下成绩和演示均为上游报告，本清单未独立重跑；保留核查版本、作者、限制条件及媒体署名。
[全量核查记录与来源版本](project-review-2026-10-30.md)。

## 真机部署与 Sim2Real

真机运行栈与 Sim2Real 迁移路径。

<a name="supermimic-repro-sim2real"></a>

### ⭐ SuperMimic-Repro-Sim2Real

[仓库](https://github.com/NJU-R-L-Group-Embodied-Lab/SuperMimic-Repro-Sim2Real) · [快速开始](https://github.com/NJU-R-L-Group-Embodied-Lab/SuperMimic-Repro-Sim2Real/blob/f8f60d7bbdba68468c050ef100af02d752ca238e/README.md#快速开始) · [v1.1 真机记录](https://github.com/NJU-R-L-Group-Embodied-Lab/SuperMimic-Repro-Sim2Real/blob/f8f60d7bbdba68468c050ef100af02d752ca238e/docs/REAL_ROBOT_LEAN35KFS.md) · [G1 部署](https://github.com/NJU-R-L-Group-Embodied-Lab/SuperMimic-Repro-Sim2Real/blob/f8f60d7bbdba68468c050ef100af02d752ca238e/docs/DEPLOY_G1.md)

- **团队：NJU R&amp;L Group Embodied Lab。** 在 CuboiLeo 的 mjlab 复现上增加自定义舞蹈、视频动作工具、单段动作微调、ONNX 导出，以及原生 MuJoCo 和 Unitree SDK 的 G1 部署流程。
- **上游报告：** v1.0 公开一段由四个动作片段组成、约 **46 秒的 G1 真机舞蹈**。v1.1 的单段策略 `e24_0355000` 在真机上**连续两次完成约 22 秒舞蹈**，包含两次快速转体和一次单脚落地的跳跃；此前 9 个模型都未能完成该动作。两次运行均挂着松弛的保护绳，同一模型重复运行不构成消融实验。
- **选择时注意：** v1.1 检查点只针对这一段舞蹈微调，不是通用动作跟踪模型；按论文观测训练与增加锚点观测仍是不同配置。 [核查版本](https://github.com/NJU-R-L-Group-Embodied-Lab/SuperMimic-Repro-Sim2Real/blob/f8f60d7bbdba68468c050ef100af02d752ca238e/README.md)。

<a href="https://github.com/NJU-R-L-Group-Embodied-Lab/SuperMimic-Repro-Sim2Real/releases/download/v1.1/shanshenbu_pro_real_robot.mp4"><img src="https://raw.githubusercontent.com/NJU-R-L-Group-Embodied-Lab/SuperMimic-Repro-Sim2Real/f8f60d7bbdba68468c050ef100af02d752ca238e/docs/assets/shanshenbu_pro_demo.gif" width="480" alt="G1 真机 · v1.1 快速转体与单脚落地跳跃"></a><br><sub>G1 真机 · v1.1 单段舞蹈；左为人类参考，右为机器人</sub>

<br>

### SuperMimic G1 Deployment

[仓库](https://github.com/KyrieYoung926/supermimic_deploy) · [MuJoCo 使用](https://github.com/KyrieYoung926/supermimic_deploy/blob/7e63e3bbd5150d55afbdece28278781800f3ed21/README.md#3-run-in-mujoco) · [真机使用](https://github.com/KyrieYoung926/supermimic_deploy/blob/7e63e3bbd5150d55afbdece28278781800f3ed21/README.md#4-run-on-the-real-g1)

- **作者：KyrieYoung926。** 面向 29 自由度 G1 部署 SuperMimic-Reproduced 策略，采用 ONNX Runtime、MuJoCo 和 Unitree SDK2。
- **提供内容：** 提供仿真与 G1 真机演示，并分别说明如何准备部署资产、在仿真和真机上运行策略。
- **选择时注意：** 仓库重点是部署，不是新的训练基准；动作数据、模型权重和机器人资产保留各自条款，不由代码许可证统一覆盖。 [核查版本](https://github.com/KyrieYoung926/supermimic_deploy/blob/7e63e3bbd5150d55afbdece28278781800f3ed21/README.md)。

<a href="https://github.com/KyrieYoung926/supermimic_deploy"><img src="https://raw.githubusercontent.com/KyrieYoung926/supermimic_deploy/7e63e3bbd5150d55afbdece28278781800f3ed21/media/deploy_real.gif" width="480" alt="G1 真机 · 上游部署演示"></a><br><sub>G1 真机 · 上游部署演示</sub>

<br>


## 独立复现

从原方法复现入手，查看训练、评估和复现记录。

<a name="supermimic_vibed"></a>

### ⭐ supermimic_vibed

[仓库](https://github.com/zita-ch/supermimic_vibed) · [安装与使用](https://github.com/zita-ch/supermimic_vibed/blob/a1508d42c9d1699a52e8233ab16d08c488441ab9/README.md#setup) · [结果](https://github.com/zita-ch/supermimic_vibed/blob/a1508d42c9d1699a52e8233ab16d08c488441ab9/README.md#result-lafan1-40-clips-one-rtx-pro-6000-blackwell)

- **作者：Chong Zhang。** 基于 Isaac Lab 3 独立实现 G1 动作跟踪，提供 kit-less 环境、训练、完整动作评估和渲染工具。
- **上游报告：** 单张 RTX PRO 6000 Blackwell 训练 **1.47 小时**，40 条 LAFAN1 动作的归一化回报为 **0.829**，**0 / 40 失败**。
- **选择时注意：** 作者将其描述为快速开发、未经充分审查的复现；与论文的差异包括关闭自碰撞、MLP 使用 bf16，以及额外输入参考根部相对朝向。 [核查版本](https://github.com/zita-ch/supermimic_vibed/blob/a1508d42c9d1699a52e8233ab16d08c488441ab9/README.md)。
- **当前源码更新：** 地面资产改为本地缓存，避免 OmniClient 的 S3 下载导致启动停滞；源码还修复了动作结尾目标速度、重复重置分箱聚合及回放窗口采样。这些是实现修复，上述成绩仍属于此前报告，不能视为修复后重新测得的结果。[当前安装说明](https://github.com/zita-ch/supermimic_vibed/blob/8bfc1158bd968f729fcc65d5e897a05b05ea3d36/README.md#setup) · [核查差异](https://github.com/zita-ch/supermimic_vibed/compare/a1508d42c9d1699a52e8233ab16d08c488441ab9...8bfc1158bd968f729fcc65d5e897a05b05ea3d36)。

<a href="https://github.com/zita-ch/supermimic_vibed"><img src="https://raw.githubusercontent.com/zita-ch/supermimic_vibed/a1508d42c9d1699a52e8233ab16d08c488441ab9/results/supermimic_lafan1_highlight.gif" width="480" alt="仿真 · LAFAN1 动作集锦"></a><br><sub>仿真 · LAFAN1 动作集锦</sub>

<br>

<a name="supermimic-reproduced"></a>

### ⭐ SuperMimic-Reproduced

[仓库](https://github.com/CuboiLeo/SuperMimic-Reproduced) · [环境与安装](https://github.com/CuboiLeo/SuperMimic-Reproduced/blob/ba6105349069bf040f1fdad60873d13138d505a2/README.md#setup) · [实验日志](https://github.com/CuboiLeo/SuperMimic-Reproduced/blob/ba6105349069bf040f1fdad60873d13138d505a2/docs/EXPERIMENTS.md) · [检查点](https://github.com/CuboiLeo/SuperMimic-Reproduced/releases/tag/e8-boneseed-100k)

- **作者：CuboiLeo。** 基于 mjlab 从零实现 G1 跟踪，提供中文复现记录、LAFAN1/BONES-SEED 数据处理、多卡训练、交互回放和全量数据检查点。
- **上游报告：** 按论文观测在 **129,943 条 BONES-SEED 动作**上训练，4 张 RTX 5090 运行 **7.1 小时（约 28 GPU·h）**。实验日志报告该动作库上**回报 0.930、495 / 129,943 失败**；按名称排除 452 条后，过滤评测集上为**回报 0.932、145 / 129,491 失败（0.11%）**。在 LAFAN1 上，锚点相对观测达到 **0.904、3 / 40 失败**；三次论文观测运行则为 **0.56–0.59、3–9 / 40 失败**。
- **选择时注意：** BONES-SEED 片段较短（中位 5.8 秒），而论文观测策略在 100–300 秒的 LAFAN1 整段动作上会漂移；两种观测口径不能直接比较。上游 README 将 0.930 与过滤后的失败数并列；上述分集合数据采用[实验日志](https://github.com/CuboiLeo/SuperMimic-Reproduced/blob/ba6105349069bf040f1fdad60873d13138d505a2/docs/EXPERIMENTS.md)。 [核查版本](https://github.com/CuboiLeo/SuperMimic-Reproduced/blob/ba6105349069bf040f1fdad60873d13138d505a2/README.md)。

<a href="https://github.com/CuboiLeo/SuperMimic-Reproduced/releases/tag/e8-boneseed-100k"><img src="https://raw.githubusercontent.com/CuboiLeo/SuperMimic-Reproduced/ba6105349069bf040f1fdad60873d13138d505a2/media/g1_boneseed_highlights.gif" width="480" alt="仿真 · 同一个 BONES-SEED 全量策略完成跳跃、转体、单脚跳和起身"></a><br><sub>仿真 · 同一个 BONES-SEED 全量策略完成六段高难度动作</sub>

<br>

<a name="supermimic-mjlab"></a>

### ⭐ SuperMimic Mjlab

[仓库](https://github.com/Breezewrf/supermimic_mjlab) · [安装](https://github.com/Breezewrf/supermimic_mjlab/blob/77183062eb92026bfbee2daf276f87cad36fd957/doc/setup_en.md) · [消融实验与检查点](https://github.com/Breezewrf/supermimic_mjlab/blob/77183062eb92026bfbee2daf276f87cad36fd957/README.md#ablation-results-and-released-checkpoint)

- **作者：Breezewrf。** 基于 mjlab 为 Unitree G1 独立复现 SuperMimic，提供完整的性能提升消融实验、多动作与速度训练、OOD 动作回放、video2motion、完整动作评估，以及已发布的策略与世界模型检查点。
- **上游报告：** 所选检查点在全部 40 条 LAFAN 动作的固定起点、完整片段确定性评估中，达到 **40 / 40 成功、平均完成率 100%、归一化回报 0.8528**。使用 **单张 RTX A6000 48 GB**、4,096 个环境和 FP32 网络，训练 **15,000 次迭代约需 4 小时**。
- **性能提升消融：** 完整记录从 Actor/Critic 输入归一化，依次加入躯干坐标系下的动作朝向锚点、世界模型归一化及修正余弦学习率调度的提升过程：在全部 40 条动作、15,000 次迭代的评估中，归一化回报均值为 **0.6016 → 0.8130 → 0.8504 → 0.8526**。最终重复运行均值与上述所选检查点分数分别报告。 [核查版本](https://github.com/Breezewrf/supermimic_mjlab/blob/77183062eb92026bfbee2daf276f87cad36fd957/README.md)。

<a href="https://github.com/Breezewrf/supermimic_mjlab/blob/77183062eb92026bfbee2daf276f87cad36fd957/doc/assets/demo_v0.gif"><img src="../assets/community/mjlab-demo.gif" width="480" alt="仿真 · SuperMimic Mjlab 动作回放的 12 秒截取"></a><br><sub>仿真 · 60.8 秒动作回放中的 12 秒片段；点击查看上游完整 GIF</sub>

<br>

### supermimic_vibe

[仓库](https://github.com/dhmbb2/supermimic_vibe) · [安装](https://github.com/dhmbb2/supermimic_vibe/blob/d0934d069207ee745be8489d9631a8314c94c1f3/README.md#setup) · [结果记录](https://github.com/dhmbb2/supermimic_vibe/blob/d0934d069207ee745be8489d9631a8314c94c1f3/notes/RESULTS.md)

- **作者：dhmbb2。** G1 复现覆盖 LAFAN1 与 BONES-SEED 全量评测、PPO-Sim/PPO-WM 和 SONIC 对照、时域／critic 消融、推扰恢复与速度控制。
- **上游报告：** 单张 RTX A6000 上，选定的 LAFAN1 检查点在 **11.4 小时**达到 **0.947、0 / 40 失败**；PPO-Sim 在 **18 小时**后为 **0.543**。在**全部 128,904 条过滤后 BONES-SEED 动作**上，选定的 184k 检查点训练 **14.4 小时**后报告 **0.923、45 条失败**。
- **方法与限制：** BONES-SEED 配置让 **50% 的环境无探索噪声采集**，这是对论文的明确改动。论文原设置运行约 6 小时后崩溃；双卡零失败结论未复现。同仿真器的 SONIC 对照为 **0.893 / 642 条失败**。数据过滤与 A6000 硬件均不同于论文，不能据此跨项目排训练速度。
- **来源：** [当前 README](https://github.com/dhmbb2/supermimic_vibe/blob/d0934d069207ee745be8489d9631a8314c94c1f3/README.md#results) · [完整实验日志](https://github.com/dhmbb2/supermimic_vibe/blob/d0934d069207ee745be8489d9631a8314c94c1f3/notes/RESULTS.md)。评测从首帧执行完整动作，使用确定性策略并关闭噪声和随机化；训练耗时不含评测。BONES-SEED 结果现已公开，数据获取仍需接受许可。以上为上游报告，本列表未重跑。

<details>
<summary>历史记录：此前的介绍、成绩与媒体</summary>

以下说明对应所链接的早期版本。

[安装](https://github.com/dhmbb2/supermimic_vibe/blob/072f0910dadc9d95c720e625b546120e9ce917c9/README.md#setup) · [结果记录](https://github.com/dhmbb2/supermimic_vibe/blob/072f0910dadc9d95c720e625b546120e9ce917c9/notes/RESULTS.md)

- **作者：dhmbb2。** 基于 mjlab 独立复现 G1 跟踪，覆盖 PPO-Sim/PPO-WM 对照、时域与 critic 消融、推力恢复和速度控制实验。
- **上游报告：** 单张 RTX A6000 上，LAFAN1 完整动作确定性评测在 **1.34 小时**达到回报 **0.833**，**12 小时**达到 **0.946、0 / 40 失败**。
- **选择时注意：** 实验记录区分已复现、部分复现和待完成项；BONES-SEED 受数据许可限制，未覆盖真机迁移，A6000 耗时也不能直接等同于 H100。 [核查版本](https://github.com/dhmbb2/supermimic_vibe/blob/072f0910dadc9d95c720e625b546120e9ce917c9/README.md)。

<a href="https://github.com/dhmbb2/supermimic_vibe/blob/072f0910dadc9d95c720e625b546120e9ce917c9/README.md"><img src="../assets/community/vibe-results.png" width="720" alt="报告截图 · 单张 RTX A6000 上的复现与消融"></a><br><sub>报告截图 · 单张 RTX A6000 上的复现与消融</sub>

</details>

<br>

### SuperMimic on RTX 5080

[仓库](https://github.com/rzc156/supermimic-rtx5080) · [复现分析](https://github.com/rzc156/supermimic-rtx5080/blob/df967c61c29a2ed9ba6b188e1607ba59225fe8a7/REPRODUCTION_ANALYSIS.md) · [评测视频](https://github.com/rzc156/supermimic-rtx5080/blob/df967c61c29a2ed9ba6b188e1607ba59225fe8a7/results/lafan1_anchor/videos/index.html)

- **作者：rzc156。** 基于 CuboiLeo 的独立 mjlab 复现，面向单张 **16 GB RTX 5080**，使用 2,048 个训练环境和额外锚点相对观测。
- **上游报告：** **40k** 检查点训练 **2.7 小时**后达到 **0.8515 平均回报 / 0.8608 步加权回报**，**2 / 40 失败**；48k 检查点训练 **3.3 小时**，三次评测均值为 **0.8375**，**4–6 / 40 失败**。
- **选择时注意：** 只有单个训练 seed，且额外锚点观测使其不等价于论文观测口径。作者以 40k 为重点检查点，但 40k/44k/48k 的差异仍需多 seed 验证。 [核查版本](https://github.com/rzc156/supermimic-rtx5080/blob/df967c61c29a2ed9ba6b188e1607ba59225fe8a7/README.md)。

<a href="https://github.com/rzc156/supermimic-rtx5080/blob/df967c61c29a2ed9ba6b188e1607ba59225fe8a7/results/lafan1_anchor/videos/index.html"><img src="https://raw.githubusercontent.com/rzc156/supermimic-rtx5080/df967c61c29a2ed9ba6b188e1607ba59225fe8a7/results/lafan1_anchor/gifs/walk1.gif" width="480" alt="仿真 · RTX 5080 复现策略执行 G1 行走"></a><br><sub>仿真 · 40k 检查点在 15 秒 LAFAN1 行走片段上的回放；点击查看全部七段视频</sub>

<br>


## 方法改动与形态适配

关注算法改动、多本体形态适配和专项控制研究。

<a name="instanttrack"></a>

### ⭐ InstantTrack

[仓库](https://github.com/Huy-Quang-Dao/instantTrack) · [安装](https://github.com/Huy-Quang-Dao/instantTrack/blob/a33691a08bca8802d9d2985f62e2567479735a8e/README.md#setup) · [结果与消融](https://github.com/Huy-Quang-Dao/instantTrack/blob/a33691a08bca8802d9d2985f62e2567479735a8e/results/report.md) · [训练预设](https://github.com/Huy-Quang-Dao/instantTrack/blob/a33691a08bca8802d9d2985f62e2567479735a8e/scripts/presets.sh)

- **作者：Huy-Quang-Dao。** 基于 supermimic_vibed 的 mjlab 移植版实现 G1 跟踪，结合 GPU 训练循环优化、EMA 策略权重平均、更小的世界模型和失败重点采样；主预设还在想象轨迹中加入接触奖励。
- **上游报告：** 单张 RTX 5090 上，三个种子均在约 **15 分钟**达到 **LAFAN1 回报 ≥ 0.82、0 / 40 失败**，该时间点平均回报 **0.831**。报告的 **2.2 倍**加速相对于作者同机运行的 SuperMimic + EMA 基线，**6 倍**则相对于其未加 EMA 的基础复现。
- **选择时注意：** 时间取连续三个达标检查点中的首个，不含离线评估，也不是从环境安装开始的总耗时。评估覆盖仿真中的训练动作，尚无更大动作库或真机结果；模型大小、更新次数和训练奖励均有改动，不能据此作跨项目速度排名。 [核查版本](https://github.com/Huy-Quang-Dao/instantTrack/blob/a33691a08bca8802d9d2985f62e2567479735a8e/README.md)。

<a href="https://github.com/Huy-Quang-Dao/instantTrack/blob/a33691a08bca8802d9d2985f62e2567479735a8e/media/equal_time_15min.gif"><img src="https://raw.githubusercontent.com/Huy-Quang-Dao/instantTrack/a33691a08bca8802d9d2985f62e2567479735a8e/media/equal_time_15min.gif" width="480" alt="仿真 · 训练 15 分钟后的 SuperMimic + EMA 与 InstantTrack 对比"></a><br><sub>上游仿真演示 · 相同的 15 分钟训练预算；左为 SuperMimic + EMA，右为 InstantTrack，展示倒地起身动作</sub>

<br>

<a name="morphmimic"></a>

### ⭐ MorphMimic

[仓库](https://github.com/lzyang2000/morphmimic) · [安装](https://github.com/lzyang2000/morphmimic/blob/aa40fe46a7fa995ba7a7354ad065a2c8ad64a302/README.md#setup) · [方法差异](https://github.com/lzyang2000/morphmimic/blob/aa40fe46a7fa995ba7a7354ad065a2c8ad64a302/README.md#differences-from-supermimic)

- **作者：Lizhi Yang 等。** 在 mjlab 中扩展 SuperMimic，用形态参数条件化网络，让 G1、X2 Ultra 和 T2 共享世界模型、策略或两者。新增 `--goal-anchor robot` 模式，把动作目标改为相对机器人自身锚点表示，以修正漂移。
- **提供内容：** 提供完整动作跟踪和骨盆、双手腕、双脚踝的稀疏五点目标接口，附浏览器演示及遥操作、部署说明。
- **选择时注意：** robot-anchor 模式部署时需由动捕或状态估计提供机器人世界位置与朝向。不同机器人先映射到统一的 29 关节布局；README 还列出终止模型、归一化、预热和执行器延迟随机化等实现改动。 [核查版本](https://github.com/lzyang2000/morphmimic/blob/aa40fe46a7fa995ba7a7354ad065a2c8ad64a302/README.md)。

<a href="https://lzyang2000.github.io/morphmimic/static/videos/dance_hiphop_shuffle_sequence_v_001_R_003__A306.mp4"><img src="../assets/community/morphmimic.gif" width="480" alt="仿真 · G1 / X2 Ultra / T2 共享策略"></a><br><sub>仿真 · G1 / X2 Ultra / T2 共享策略</sub>

[演示视频](https://lzyang2000.github.io/morphmimic/static/videos/morphmimic.mp4) · [交互演示](https://lzyang2000.github.io/morphmimic/demo/)

<br>

### allmimic

[仓库](https://github.com/Shimingyi/allmimic) · [安装](https://github.com/Shimingyi/allmimic/blob/cb334ff674b2f57248f33f8c21b7fb526fbdf8cc/README.md#install) · [结果](https://github.com/Shimingyi/allmimic/blob/cb334ff674b2f57248f33f8c21b7fb526fbdf8cc/README.md#results)

- **作者：Shimingyi。** 基于 supermimic_vibe，在 mjlab 中混用上身残差动作与腿部绝对动作，并加入世界模型损失加权和动作均衡采样。
- **上游报告：** 单张 RTX 4090 使用推荐配置，训练 **0.83 小时**后，LAFAN1 完整动作评测达到 **0 / 40 失败、回报 0.91**；耗时不含评估。
- **选择时注意：** 推荐配置包含算法和数据采样改动；仅训练 306 条困难动作的实验，与完整 BONES-SEED 训练是不同实验。 [核查版本](https://github.com/Shimingyi/allmimic/blob/cb334ff674b2f57248f33f8c21b7fb526fbdf8cc/README.md)。
- **补充上游 BONES-SEED 报告：** 在**完整训练划分、两张 RTX 4090 上训练 6.6 小时 / 176k 轮**的策略完成 **306 / 306 条困难训练动作**，以及翻转、侧手翻、倒立共 **303 / 308 条**。BONES-SEED 未见动作报告 **100.0% 成功率 / 0.884 回报**，LAFAN1 为 **94.6% / 0.806**。这些测试集经过过滤并**切为 10 秒片段**，困难训练动作则完整评测；它与仅用 306 条动作训练的实验分开，也不代表整个 BONES-SEED 动作库零失败。[协议与表格](https://github.com/Shimingyi/allmimic/blob/cb334ff674b2f57248f33f8c21b7fb526fbdf8cc/README.md#bones-seed)。

<a href="https://github.com/Shimingyi/allmimic"><img src="https://raw.githubusercontent.com/Shimingyi/allmimic/cb334ff674b2f57248f33f8c21b7fb526fbdf8cc/assets/challenge_cases.gif" width="480" alt="仿真 · 高难度动作片段"></a><br><sub>仿真 · 高难度动作片段</sub>

<br>

### SuperMimic on LocoMuJoCo

[仓库](https://github.com/Alchedata/supermimic-locomujoco) · [安装](https://github.com/Alchedata/supermimic-locomujoco/blob/de9f39191b9e8b87ff1afd2b0129dd93d4795e8c/README.md#setup) · [结果](https://github.com/Alchedata/supermimic-locomujoco/blob/de9f39191b9e8b87ff1afd2b0129dd93d4795e8c/README.md#results)

- **团队：Alchedata。** 用 JAX 与 LocoMuJoCo 将方法移植到 H1，在 MLP、残差专家、动作敏感度和可信度相关的世界模型变体之外，新增**全状态 ODE 世界模型**和**抗饱和正则化**。
- **上游报告：** 固定 5,000 次迭代检查点、160 个初始状态时，在 Euler ODE 模型上增加抗饱和正则化，在三个 seed 上把总失败数从 **15 / 480 降到 1 / 480**。种子 43 从 **878.71 / 15 次失败**提升到 **935.38 / 0 次**，种子 42 则略有变差，因此并非所有 seed 都提高分数。
- **选择时注意：** 指标是 LocoMuJoCo 回合回报，与 G1 归一化跟踪分数不同；中点 ODE 加速实验仍在进行，未作为已完成结果计入。 [核查版本](https://github.com/Alchedata/supermimic-locomujoco/blob/de9f39191b9e8b87ff1afd2b0129dd93d4795e8c/README.md)。

<a href="https://github.com/Alchedata/supermimic-locomujoco/blob/de9f39191b9e8b87ff1afd2b0129dd93d4795e8c/docs/figures/return_vs_step.png"><img src="../assets/community/locomujoco-results.png" width="720" alt="训练曲线 · ODE 与抗饱和变体的回报随训练步数变化"></a><br><sub>上游训练曲线 · ODE 与抗饱和变体，固定 5k 评估检查点</sub>

<br>

### Rethinking SuperMimic

[仓库](https://github.com/btx0424/rethinking-supermimic) · [安装](https://github.com/btx0424/rethinking-supermimic/blob/2cbbd1278bfb8bd59c31fe48d7413c46ae205e32/README.md#installation) · [实现对照](https://github.com/btx0424/rethinking-supermimic/blob/2cbbd1278bfb8bd59c31fe48d7413c46ae205e32/README.md#ours-the-paper-and-supermimic_vibed) · [SuperMimic / SAC 入口](https://github.com/btx0424/rethinking-supermimic/blob/2cbbd1278bfb8bd59c31fe48d7413c46ae205e32/src/supermimic/train.py)

- **作者：btx0424。** 在 mjlab 的 G1 上研究拼接与 FiLM 目标条件化、HL-Gauss critic，以及 heading/pelvis 世界模型坐标。当前[训练入口](https://github.com/btx0424/rethinking-supermimic/blob/2cbbd1278bfb8bd59c31fe48d7413c46ae205e32/src/supermimic/train.py)可选择 SuperMimic 或新增的 SAC 基线。
- **本次更新：** 两套算法配置均提供策略 EMA（`pi_ema: 0.995`），并增加接触误差、神经元休眠、时域梯度、tanh 饱和及隐变量漂移诊断。[SuperMimic 配置](https://github.com/btx0424/rethinking-supermimic/blob/2cbbd1278bfb8bd59c31fe48d7413c46ae205e32/src/supermimic/conf/algo/supermimic.yaml) · [SAC 配置](https://github.com/btx0424/rethinking-supermimic/blob/2cbbd1278bfb8bd59c31fe48d7413c46ae205e32/src/supermimic/conf/algo/sac.yaml)。
- **选择时注意：** [实现对照](https://github.com/btx0424/rethinking-supermimic/blob/2cbbd1278bfb8bd59c31fe48d7413c46ae205e32/README.md#ours-the-paper-and-supermimic_vibed)继续说明观测、自碰撞、锚点与归一化差异。SAC/EMA 的支持已核对源码和配置；该 README 未发布新增 SAC/EMA 性能测量，本列表未执行这些训练入口。

<details>
<summary>历史记录：此前的介绍、成绩与媒体</summary>

以下说明对应所链接的早期版本。

[安装](https://github.com/btx0424/rethinking-supermimic/blob/aa77b71054a850075431248f1534bb77ca62b4d8/README.md#installation) · [实现对照](https://github.com/btx0424/rethinking-supermimic/blob/aa77b71054a850075431248f1534bb77ca62b4d8/README.md#ours-the-paper-and-supermimic_vibed)

- **作者：btx0424。** 在 mjlab 的 G1 跟踪任务中研究目标条件化：比较目标与本体观测直接拼接，以及用 FiLM 调制策略各层。最新版本加入 HL-Gauss critic、梯度检查，以及可选朝向坐标系或骨盆坐标系的世界模型坐标。
- **选择时注意：** 提供可配置观测、锚点选择及 Viser 回放；实现对照表解释了与论文、supermimic_vibed 在自碰撞、观测输入等方面的差异。 [核查版本](https://github.com/btx0424/rethinking-supermimic/blob/aa77b71054a850075431248f1534bb77ca62b4d8/README.md)。

<a href="https://github.com/btx0424/rethinking-supermimic/blob/ecdaeb6a916a16cf7eb69b19226c17be31a6bc27/README.md"><img src="../assets/community/rethinking-comparison.png" width="720" alt="历史实现对照表节选 · 2026-10-26 快照；当前对照见上方链接"></a><br><sub>历史实现对照表节选 · 2026-10-26 快照；当前对照见上方链接</sub>

</details>

<br>

### Standing MBRL vs PPO

[仓库](https://github.com/JackMin7/supermimic_whole_body_tracking) · [实验说明](https://github.com/JackMin7/supermimic_whole_body_tracking/blob/553a7d32dc5fc00cbe6de5ee46479af2fcceeda8/docs/EXPERIMENTS.md) · [复现说明](https://github.com/JackMin7/supermimic_whole_body_tracking/blob/553a7d32dc5fc00cbe6de5ee46479af2fcceeda8/docs/REPRODUCIBILITY.md)

- **作者：JackMin7。** 将 SuperMimic 的可微世界模型训练回路用于 G1 静态站立任务，并与基于 BeyondMimic 的 RSL-RL PPO 基线比较。
- **上游报告：** 在相同 29 自由度 G1、任务、奖励，以及约 1 小时、256 个环境的训练下，MBRL 在 **20 秒和 60 秒**测试中均 **32 / 32** 成功；PPO 分别为 **12 / 32** 和 **16 / 32**。20 秒平均关节 RMSE 为 **0.144 vs 0.415 rad**。
- **选择时注意：** 只有单个训练 seed，且共用 GPU、没有扰动；32 次 rollout 是同一策略的副本，不是独立 seed。作者未声称训练速度或真机收益。 [核查版本](https://github.com/JackMin7/supermimic_whole_body_tracking/blob/553a7d32dc5fc00cbe6de5ee46479af2fcceeda8/README.md)。

<a href="https://github.com/JackMin7/supermimic_whole_body_tracking/blob/553a7d32dc5fc00cbe6de5ee46479af2fcceeda8/media/ppo_vs_mbrl_60s.mp4"><img src="https://raw.githubusercontent.com/JackMin7/supermimic_whole_body_tracking/553a7d32dc5fc00cbe6de5ee46479af2fcceeda8/media/PPO%E4%B8%8EMBRL%E7%AB%99%E7%AB%8B%E5%AF%B9%E7%85%A7_60%E7%A7%92%E5%8A%A8%E5%9B%BE.gif" width="640" alt="仿真 · PPO 与 MBRL 的 G1 站立任务 60 秒对照"></a><br><sub>仿真 · 60 秒 PPO / MBRL 原速对照；PPO 终止后画面冻结</sub>

<br>


## 感知、地形与四足任务

视觉、高度扫描、地形与四足任务适配。

<a name="instinctmj--supermimic"></a>

### ⭐ InstinctMJ · SuperMimic

[仓库](https://github.com/project-instinct/InstinctMJ/tree/supermimic) · [方法与结果](https://github.com/project-instinct/InstinctMJ/blob/3f0952d36268c6aad299e256d27cc65d3bcc1434/src/instinct_mj/rl/supermimic/README.md#results) · [发布资源](https://github.com/project-instinct/InstinctMJ/releases)

- **团队：Project Instinct。** 在 **supermimic 分支**训练感知 G1 地形跟踪。世界模型现预测机器人状态；依据预测状态和已知场景／机器人网格，可微光线投射生成想象深度图，再加入相机噪声，策略损失端到端训练深度编码器。
- **上游报告：** 新渲染方案在**单张 RTX 3090、1,024 个环境**下训练 **8,000 轮 / 2.8 小时**，对 **5 类地形、10 个动作**报告 **95% 完整动作成功率 / 97% 完成度**。单种子，每个动作评测 12–13 次；从首帧开始，开启相机噪声，不施加推扰。
- **选择时注意：** 旧隐变量预测方案的 **97% / 3.2 小时**对应另一套设计与参数，耗时还包含共享 GPU 的评测；新结果只计训练时间。地形跟踪与平地 LAFAN1 不同，渲染依赖已知几何；外部检查点需适配关节顺序。[当前方法与结果](https://github.com/project-instinct/InstinctMJ/blob/3f0952d36268c6aad299e256d27cc65d3bcc1434/src/instinct_mj/rl/supermimic/README.md)。

<a href="https://github.com/project-instinct/InstinctMJ/blob/3f0952d36268c6aad299e256d27cc65d3bcc1434/src/instinct_mj/rl/supermimic/assets/method.png"><img src="https://raw.githubusercontent.com/project-instinct/InstinctMJ/3f0952d36268c6aad299e256d27cc65d3bcc1434/src/instinct_mj/rl/supermimic/assets/method.png" width="720" alt="当前方法 · 根据预测状态可微渲染深度图"></a><br><sub>当前方法 · 根据预测状态可微渲染深度图</sub>

<details>
<summary>历史记录：此前的介绍、成绩与媒体</summary>

以下说明对应所链接的早期版本。

[方法与结果](https://github.com/project-instinct/InstinctMJ/blob/7ca851e002980011f24a1664011305d0ba94aefc/src/instinct_mj/rl/supermimic/README.md#results) · [发布资源](https://github.com/project-instinct/InstinctMJ/releases)

- **团队：Project Instinct。** 在 mjlab / instinct_rl 中扩展到 G1 视觉动作跟踪和目标点跑酷；世界模型预测机器人状态及深度编码器潜变量，部分组件改编自 supermimic_vibed。
- **上游报告：** 单张 RTX 3090 训练 **8,000 次迭代 / 3.2 小时**，在 **5 类地形、10 个动作**上达到 **97% 完整动作成功率**；单种子，每个动作评估 12–13 次，开启相机噪声。
- **选择时注意：** 使用 **supermimic 分支**。这是地形跟踪任务，与平地 LAFAN1 不同；外部 checkpoint 需要适配关节顺序，许可为 CC BY-NC 4.0。 [核查版本](https://github.com/project-instinct/InstinctMJ/blob/7ca851e002980011f24a1664011305d0ba94aefc/src/instinct_mj/rl/supermimic/README.md)。

<a href="https://github.com/project-instinct/InstinctMJ/blob/7ca851e002980011f24a1664011305d0ba94aefc/src/instinct_mj/rl/supermimic/assets/world_model_simple.png"><img src="https://raw.githubusercontent.com/project-instinct/InstinctMJ/7ca851e002980011f24a1664011305d0ba94aefc/src/instinct_mj/rl/supermimic/assets/world_model_simple.png" width="720" alt="方法图 · 机器人状态与视觉潜变量预测"></a><br><sub>方法图 · 机器人状态与视觉潜变量预测</sub>

</details>

<br>

<a name="go2-supermimic"></a>

### ⭐ Go2-SuperMimic

[仓库](https://github.com/Zhengtianjin/go2-supermimic) · [快速开始](https://github.com/Zhengtianjin/go2-supermimic/blob/054a13c13285a1c94b2e69dc8ac7331f9a8c71cf/README.md#-quickstart) · [预训练策略](https://github.com/Zhengtianjin/go2-supermimic/blob/054a13c13285a1c94b2e69dc8ac7331f9a8c71cf/README.md#pretrained-policies)

- **作者：Zhengtianjin。** 在 mjlab 中将方法用于 Unitree Go2 追逐与闪避，覆盖平地、障碍和地形场景，接入激光或高度扫描输入。
- **提供内容：** 公开平地、障碍、地形三类 actor，以及评估与录制工具；仅下载 actor 可以回放，恢复训练还需要世界模型与 critic。
- **选择时注意：** 目前只有仿真验证，目标感知来自仿真真值；发布的地形策略在最难设置下仍会摔倒或撞杆。 [核查版本](https://github.com/Zhengtianjin/go2-supermimic/blob/054a13c13285a1c94b2e69dc8ac7331f9a8c71cf/README.md)。

<a href="https://github.com/Zhengtianjin/go2-supermimic"><img src="https://raw.githubusercontent.com/Zhengtianjin/go2-supermimic/054a13c13285a1c94b2e69dc8ac7331f9a8c71cf/resources/terrain.gif" width="480" alt="仿真 · Go2 地形追逐与闪避"></a><br><sub>仿真 · Go2 地形追逐与闪避</sub>

<br>

### SuperMimic Parkour

[仓库](https://github.com/yhx1203/supermimic_parkour) · [数据配置](https://github.com/yhx1203/supermimic_parkour/blob/f398519453a25b3f10722626b7356266d8b7f875/README.md#motion-data) · [检查点](https://github.com/yhx1203/supermimic_parkour/blob/f398519453a25b3f10722626b7356266d8b7f875/logs/php_five_skills/last.pt)

- **作者：yhx1203。** 基于 mjlab 和 PHP Parkour 动作匹配数据，用共享可微世界模型与 BPTT 策略学习实现五项技能的 G1 跑酷适配。
- **上游报告：** 在单张 GPU 上训练 **4 小时出头**，策略可跨越 **130 cm 障碍**；项目发布对应检查点并提供浏览器回放。
- **选择时注意：** PHP 动作包未随仓库分发，需要另行提供。这是上游单项演示与训练耗时报告，不是与 PPO 或 SuperMimic 的独立基准比较。 [核查版本](https://github.com/yhx1203/supermimic_parkour/blob/f398519453a25b3f10722626b7356266d8b7f875/README.md)。

<a href="https://github.com/yhx1203/supermimic_parkour/blob/f398519453a25b3f10722626b7356266d8b7f875/doc/%E5%BD%95%E5%B1%8F%202026%E5%B9%B410%E6%9C%8826%E6%97%A5%2016%E6%97%B641%E5%88%8626%E7%A7%92.gif"><img src="https://raw.githubusercontent.com/yhx1203/supermimic_parkour/f398519453a25b3f10722626b7356266d8b7f875/doc/%E5%BD%95%E5%B1%8F%202026%E5%B9%B410%E6%9C%8826%E6%97%A5%2016%E6%97%B641%E5%88%8626%E7%A7%92.gif" width="720" alt="仿真 · G1 跨越 130 cm 跑酷障碍"></a><br><sub>仿真 · 五项技能 PHP 跑酷策略，11.5 秒上游演示</sub>

<br>

### SuperMimic-perceptive

[仓库](https://github.com/mode1223345/SuperMimic-perceptive) · [方法](https://github.com/mode1223345/SuperMimic-perceptive/blob/3d38bacbaf5bee7e782bdada6a6da678264d0bfa/Ae.md) · [进展记录](https://github.com/mode1223345/SuperMimic-perceptive/blob/3d38bacbaf5bee7e782bdada6a6da678264d0bfa/Progress.md)

- **作者：mode1223345。** 基于 Isaac Lab 3 的 supermimic_vibed，先预训练高程图自编码器，再冻结同一个编码器，供 actor、critic 和世界模型共享。
- **提供内容：** 记录平地／台阶地形上的四组控制对照，并单独提供重建检查；已发布的控制对照仍处于进行中。
- **选择时注意：** 当前使用仿真真值地图，尚未接入真实深度重建与真机感知；继承的基线成绩不能证明共享编码器带来控制收益。 [核查版本](https://github.com/mode1223345/SuperMimic-perceptive/blob/3d38bacbaf5bee7e782bdada6a6da678264d0bfa/README.md)。

<a href="https://github.com/mode1223345/SuperMimic-perceptive/blob/3d38bacbaf5bee7e782bdada6a6da678264d0bfa/results/Curves.png"><img src="https://raw.githubusercontent.com/mode1223345/SuperMimic-perceptive/3d38bacbaf5bee7e782bdada6a6da678264d0bfa/results/Curves.png" width="720" alt="训练曲线 · 2026-10-24 快照，控制对照实验仍在进行"></a><br><sub>训练曲线 · 2026-10-24 快照，控制对照实验仍在进行</sub>

<br>


## 操作与灵巧手

机械臂、手部与物体交互任务，灵巧手项目集中在此；探索性的 Ref2Dex 接触控制项目列在[方法借鉴与探索](#方法借鉴与探索)。

<a name="supermimic-for-robot-manipulation"></a>

### ⭐ SuperMimic for Robot Manipulation

[仓库](https://github.com/emoPointer/supermimic_manipulation) · [安装](https://github.com/emoPointer/supermimic_manipulation/blob/810e5768c50117d2fec75f20f9e643a11cd0882b/README.md#install) · [结果](https://github.com/emoPointer/supermimic_manipulation/blob/810e5768c50117d2fec75f20f9e643a11cd0882b/README.md#results)

- **作者：Zhiqiang Zhou（emoPointer）。** 在 mjlab / MuJoCo Warp 中把 SuperMimic 迁移到仿真 ARX5 机械臂的基于状态操作任务，包括 Lemon、BoxInBin 和 MugHang。
- **上游报告：** 各任务使用第 4,000 轮检查点，在独立测试 reset bank 上完成 256 个完整回合，Lemon、BoxInBin、MugHang 成功率分别为 **100.0%、94.9%、96.9%**；单张 A100 80 GB 共卡训练耗时 **1.8 / 1.9 / 2.8 小时**。
- **选择时注意：** 使用 OmniReset 式重置类别缩短有效时域，想象阶段以可微几何代理替换接触成功判据；策略只输入低维状态。检查点与 reset bank 已在 Hugging Face 发布。 [核查版本](https://github.com/emoPointer/supermimic_manipulation/blob/810e5768c50117d2fec75f20f9e643a11cd0882b/README.md)。

<a href="https://github.com/emoPointer/supermimic_manipulation"><img src="https://raw.githubusercontent.com/emoPointer/supermimic_manipulation/810e5768c50117d2fec75f20f9e643a11cd0882b/docs/media/lemon.gif" width="480" alt="仿真 · ARX5 Lemon 任务的两个保留初态回放"></a><br><sub>仿真 · ARX5 Lemon 任务 · 两个保留初态回放</sub>

<br>

<a name="dex-supermimic"></a>

### ⭐ Dex SuperMimic

[仓库](https://github.com/CumulusAlpha/Dex-Supermimic) · [安装](https://github.com/CumulusAlpha/Dex-Supermimic/blob/3a7c1a33fd8e5c6cc047e381ea9309da96553c27/README.md#installation) · [演示](https://github.com/CumulusAlpha/Dex-Supermimic/blob/3a7c1a33fd8e5c6cc047e381ea9309da96553c27/README.md#demos) · [检查点](https://github.com/CumulusAlpha/Dex-Supermimic/releases/tag/pretrained-wuji-v2)

- **作者：CumulusAlpha。** 将基于世界模型的策略训练用于 Wuji Hand 1/Hand 2 手内方块重定向，以及 Wuji Hand 2 旋转笔，采用 mjlab / MuJoCo Warp 和 InstinctMJ 任务框架。
- **提供内容：** 三套任务配置、随包的手部与方块资产、Viser 回放，以及 `pretrained-wuji-v2` Release 中的三个 8,000 次迭代检查点。
- **选择时注意：** 这是灵巧操作任务的适配，任务和奖励与人形动作跟踪不同。 [核查版本](https://github.com/CumulusAlpha/Dex-Supermimic/blob/3a7c1a33fd8e5c6cc047e381ea9309da96553c27/README.md)。

<table>
  <tr>
    <td width="50%" align="center"><a href="https://github.com/CumulusAlpha/Dex-Supermimic/blob/3a7c1a33fd8e5c6cc047e381ea9309da96553c27/docs/demos/hand1_reorient.gif"><img src="https://raw.githubusercontent.com/CumulusAlpha/Dex-Supermimic/3a7c1a33fd8e5c6cc047e381ea9309da96553c27/docs/demos/hand1_reorient.gif" width="100%" alt="仿真 · Wuji Hand 1 手内方块重定向"></a><br><sub>Wuji Hand 1 · 手内方块重定向</sub></td>
    <td width="50%" align="center"><a href="https://github.com/CumulusAlpha/Dex-Supermimic/blob/3a7c1a33fd8e5c6cc047e381ea9309da96553c27/docs/demos/hand2_pen_spin.gif"><img src="https://raw.githubusercontent.com/CumulusAlpha/Dex-Supermimic/3a7c1a33fd8e5c6cc047e381ea9309da96553c27/docs/demos/hand2_pen_spin.gif" width="100%" alt="仿真 · Wuji Hand 2 旋转笔"></a><br><sub>Wuji Hand 2 · 旋转笔</sub></td>
  </tr>
</table>

<br>

<a name="in-hand-rotation-mjlab"></a>

### ⭐ In-Hand Rotation mjlab

[仓库](https://github.com/Msornerrrr/in-hand-rotation-mjlab) · [安装](https://github.com/Msornerrrr/in-hand-rotation-mjlab/blob/0ab03eb2244b4a1a020d94ef38a4823bb9e15ba0/README.md#install) · [结果](https://github.com/Msornerrrr/in-hand-rotation-mjlab/blob/0ab03eb2244b4a1a020d94ef38a4823bb9e15ba0/README.md#results) · [检查点](https://github.com/Msornerrrr/in-hand-rotation-mjlab/blob/0ab03eb2244b4a1a020d94ef38a4823bb9e15ba0/README.md#quick-start-the-released-policies)

- **作者：Msornerrrr。** 在 mjlab / MuJoCo Warp 中将 SuperMimic 式世界模型策略学习（在线重拟合的 MLP 世界模型、通过想象轨迹反向传播、TD(λ) 评论家与权重平均）用于 LEAP 灵巧手，并在相同环境上提供 PPO 基线：掌心向上的方块偏航旋转、SO(3) 方块重定向（仅 PPO）和掌心向下用指尖旋转 22 种物体；使用在真实手上辨识的舵机模型。两种方法的检查点均已发布。
- **上游报告：** 方块偏航任务中，世界模型策略在 **25 分钟、1,800 万环境步**时达到 PPO 的水平（每秒奖励约 0.26），PPO 需 6.5 小时、2.62 亿步，最终为 **0.292 对 0.261**。掌心向下指尖旋转任务中（每个物体 64 回合、每回合 60 秒，指垫摩擦随机化 0.25–1.2），仅用关节信息的世界模型策略计分偏航达到 **933°**、掉落 **4.0%**，而由教师蒸馏并已部署的 PPO 学生为 **675° / 10.4%**，特权 PPO 教师为 **944° / 2.1%**。
- **选择时注意：** 世界模型结果均在仿真中；真实机器人视频（偏航与 SO(3)）展示的是 PPO 策略。指尖任务数值采用仓库自带评测（旋转奖励速度上限 0.3 rad/s，物体偏移 30 mm 记为掉落）。每种配置单次运行；训练时间基于单张 RTX 4090。 [核查版本](https://github.com/Msornerrrr/in-hand-rotation-mjlab/blob/0ab03eb2244b4a1a020d94ef38a4823bb9e15ba0/README.md)。

<a href="https://github.com/Msornerrrr/in-hand-rotation-mjlab"><img src="https://raw.githubusercontent.com/Msornerrrr/in-hand-rotation-mjlab/0ab03eb2244b4a1a020d94ef38a4823bb9e15ba0/assets/sim_fingertip.gif" width="480" alt="仿真 · 仅用关节信息的世界模型策略在掌心向下时用指尖旋转球体、方块、圆柱和长方体"></a><br><sub>仿真 · 掌心向下指尖旋转，仅用关节信息的世界模型策略</sub>

<br>

### Humanoid Mimic · SuperMimic

[仓库](https://github.com/shuayyy/humanoid-amp-ppo) · [快速开始](https://github.com/shuayyy/humanoid-amp-ppo/blob/4889389118e0c88d3945dff54d2cd3f992ed815e/README.md#quickstart) · [结果与协议](https://github.com/shuayyy/humanoid-amp-ppo/blob/4889389118e0c88d3945dff54d2cd3f992ed815e/docs/supermimic/RESULTS.md)

- **作者：shuayyy。** 在 mjlab 的同一组 G1 行走、下蹲和搬箱任务上对照 SuperMimic 与 PPO-Sim，仓库另含独立的 AMP-PPO 路线。
- **上游报告：** 两个 SuperMimic 种子在 **3,100 万环境步**时，64 回合随机评测的搬箱成功率达到 **100%**；成功条件是结束时箱子高度距参考值不超过 10 cm。
- **选择时注意：** 上述 SuperMimic 分数使用无噪声观测；新版评估已加入观测噪声，公开检查点尚未按这一设置重评。 [核查版本](https://github.com/shuayyy/humanoid-amp-ppo/blob/4889389118e0c88d3945dff54d2cd3f992ed815e/README.md)。

<a href="https://github.com/shuayyy/humanoid-amp-ppo/blob/4889389118e0c88d3945dff54d2cd3f992ed815e/assets/supermimic_vs_ppo_lift.mp4"><img src="https://raw.githubusercontent.com/shuayyy/humanoid-amp-ppo/4889389118e0c88d3945dff54d2cd3f992ed815e/assets/supermimic_vs_ppo_lift.gif" width="480" alt="搬箱 · SuperMimic 12k / PPO-Sim 6k 次迭代"></a><br><sub>搬箱 · SuperMimic 12k / PPO-Sim 6k 次迭代</sub>

<br>


## 肌肉驱动、交互与诊断

肌肉驱动本体、物理交互与接触诊断。

<a name="muscle-supermimic"></a>

### ⭐ Muscle SuperMimic

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

<a href="https://github.com/shangchaohu718/supermimic-pera/blob/0e89e55187a800341e609129b5d5200a607a467c/README.md"><img src="../assets/community/pera-tracking-results.png" width="720" alt="报告截图 · 跟踪检查点 500–6000，与滑板实验分开"></a><br><sub>报告截图 · 跟踪检查点 500–6000，与滑板实验分开</sub>

<br>

### SuperMimic Backflip Diagnostics

[仓库](https://github.com/liudi159/supermimic-backflip-5090) · [结果](https://github.com/liudi159/supermimic-backflip-5090/blob/5b313d75e804cdd2ff1ce9bdcfa899a98eca856b/README.md#结果) · [快速入口](https://github.com/liudi159/supermimic-backflip-5090/blob/5b313d75e804cdd2ff1ce9bdcfa899a98eca856b/README.md#快速入口)

- **作者：liudi159。** 使用 Isaac Lab 3 和单张 RTX 5090 专项研究 G1 后空翻，记录双腿对称性、接触力、穿透和落地稳定性。
- **上游报告：** 最终 V14 检查点完成后翻与落地保持，但原始严格评测记录到 1 帧非脚部穿透，**仍未通过验收**。
- **选择时注意：** 独立重评的临界接触结果出现变化，两次记录均保留；演示不能据此表述为稳健成功或论文全部实验复现。 [核查版本](https://github.com/liudi159/supermimic-backflip-5090/blob/5b313d75e804cdd2ff1ce9bdcfa899a98eca856b/README.md)。

<a href="https://github.com/liudi159/supermimic-backflip-5090/blob/5b313d75e804cdd2ff1ce9bdcfa899a98eca856b/media/v14_blue_checker.mp4"><img src="../assets/community/backflip.gif" width="480" alt="仿真 · 最终 V14 策略；严格评估未通过"></a><br><sub>仿真 · 最终 V14 策略；严格评估未通过</sub>

<br>


## 框架与训练栈

可复用的训练、评估流程及与既有框架的集成。

<a name="unisupermimic"></a>

### ⭐ UniSuperMimic

[仓库](https://github.com/Motphys/Uni-SuperMimic) · [安装](https://github.com/Motphys/Uni-SuperMimic/blob/05a9772ca09509c50a4cc3fe96f9d6b3c180f3d2/README.md#installation) · [结果](https://github.com/Motphys/Uni-SuperMimic/blob/05a9772ca09509c50a4cc3fe96f9d6b3c180f3d2/README.md#results)

- **团队：Motphys。** 基于 UniLab 的独立 SuperMimic 复现，面向 G1，支持 mjwarp、MuJoCo 与 Motrix 三种后端。集成可微世界模型、目标条件策略，以及 LAFAN1 / BONES-SEED 的下载、转换、过滤、打包、训练和确定性全库评测流程。
- **上游全库报告：** 在**全部 129,487 段过滤后 BONES-SEED 动作**上，mjwarp 基线在**单张 RTX 4090（48 GB）上训练 12,000 轮、learner 耗时 1.69 小时**，报告归一化回报 **0.9243**，失败 **350 / 129,487 段（0.27%）**。
- **上游训练优化：** 加入 **EMA（`pi_ema: 0.995`）、no-sync 训练及 `lr: 4e-4`** 后，**8,000 轮**检查点在相同全库和 GPU 配置下报告回报 **0.9395**，失败 **193 / 129,487 段（0.15%）**。[结果与曲线](https://github.com/Motphys/Uni-SuperMimic/blob/05a9772ca09509c50a4cc3fe96f9d6b3c180f3d2/README.md#results)。
- **选择时注意：** 以上为上游报告，本列表未独立复现。量化结果来自 mjwarp 对训练动作库的评测，不能据此判断未见动作泛化或 MuJoCo / Motrix 的同条件指标。12,000 轮全库结果使用早期“每段一个环境”的评测器，当前评测器会回收已结束环境。[核查版本](https://github.com/Motphys/Uni-SuperMimic/blob/05a9772ca09509c50a4cc3fe96f9d6b3c180f3d2/README.md)。

<details>
<summary>历史记录：此前的 LAFAN1 与 BONES-SEED 抽样评测</summary>

以下保留早期版本的说明与来源；其中关于“仅抽样评测”的限制对应当时版本。

[安装](https://github.com/Motphys/Uni-SuperMimic/blob/9bdcbde1f191d88b489309182624a9877e7b6c30/README.md#installation) · [结果](https://github.com/Motphys/Uni-SuperMimic/blob/9bdcbde1f191d88b489309182624a9877e7b6c30/README.md#results)

- **团队：Motphys。** 将 supermimic_vibed 移植到 UniLab 的 Manager-Based G1 任务，提供 LAFAN1 与 BONES-SEED 数据流程、可选仿真后端、确定性完整动作评估和视频导出。
- **上游报告：** 第 **12,000** 次迭代的 LAFAN1 检查点报告 **0.827227**、**0 / 40 失败**。为新的 BONES-SEED 对照在同机重跑 LAFAN1 得到 **0.8336、0 / 40**；在 **129,487 条 BONES-SEED 动作**上，单张 RTX 5090 训练 **2.55 小时**，在随机抽取的 **10,000 条**上评分为 **0.9262**，**30 / 10,000 失败（0.3%）**。
- **选择时注意：** BONES-SEED 是抽样评估，不是全量动作库；已发布的跟踪成绩均使用 mjwarp，MuJoCo 和 Motrix 的运行入口不代表已经取得相同训练成绩。 [核查版本](https://github.com/Motphys/Uni-SuperMimic/blob/9bdcbde1f191d88b489309182624a9877e7b6c30/README.md)。

</details>

<a href="https://github.com/Motphys/Uni-SuperMimic/blob/9bdcbde1f191d88b489309182624a9877e7b6c30/docs/assets/supermimic_comparison.mp4"><img src="https://raw.githubusercontent.com/Motphys/Uni-SuperMimic/9bdcbde1f191d88b489309182624a9877e7b6c30/docs/assets/supermimic_comparison.gif" width="480" alt="仿真 · G1 跳跃跟踪"></a><br><sub>仿真 · G1 跳跃跟踪</sub>

<br>

<a name="scalebfm_plus--supermimic"></a>

### ⭐ ScaleBFM_Plus · SuperMimic

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

[仓库](https://github.com/Renforce-Dynamics/trackerlab-supermimic) · [安装](https://github.com/Renforce-Dynamics/trackerlab-supermimic/blob/813f37a89d9be0791c9c72695a322307001a5d11/README.md#install) · [结果与限制](https://github.com/Renforce-Dynamics/trackerlab-supermimic/blob/813f37a89d9be0791c9c72695a322307001a5d11/docs/results.md) · [可选 G1 Warp 训练](https://github.com/Renforce-Dynamics/trackerlab-supermimic/blob/813f37a89d9be0791c9c72695a322307001a5d11/docs/warp_training.md)

- **团队：Renforce Dynamics。** 保留 G1、Go2、A3、T1、Bumi、Pi+ 的 Isaac Lab / PhysX 重定向、训练和评测流程，新增独立的 **G1 MuJoCo-Warp** 训练入口，采用 GPU 常驻动作参考、BF16 MLP 与 CUDA Graphs。
- **当前改动：** 共享修复仅对超出动作结尾的合成目标保持末帧姿态并将速度归零，保留原本为 50 Hz 的全部源帧，稳定归一化缓冲区存储。更换加载器后需重新核对派生动作缓存。[边界与归一化修复](https://github.com/Renforce-Dynamics/trackerlab-supermimic/blob/813f37a89d9be0791c9c72695a322307001a5d11/docs/reference_tail_fix.md)。
- **成绩与限制：** 早期 PhysX 检查点的 **0.8694663 / 40 条 LAFAN1 中 0 失败**保留为历史结果。导入的 Warp 运行时需要预先准备 root83 缓存，目前面向从随机初始化训练 G1。上游集成已覆盖 CPU 回归检查，目标机器上的 CUDA 运行验收及新训练结果仍待完成；来源遥操作实验的吞吐量不能视为本仓库集成的基准。[Warp 环境与范围](https://github.com/Renforce-Dynamics/trackerlab-supermimic/blob/813f37a89d9be0791c9c72695a322307001a5d11/docs/warp_training.md)。

<details>
<summary>历史记录：此前的介绍、成绩与媒体</summary>

以下说明对应所链接的早期版本。

[安装](https://github.com/Renforce-Dynamics/trackerlab-supermimic/blob/29d24524f2f731bf4df75b319c3e76544165849e/README.md#install) · [结果与限制](https://github.com/Renforce-Dynamics/trackerlab-supermimic/blob/29d24524f2f731bf4df75b319c3e76544165849e/docs/results.md)

- **团队：Renforce Dynamics。** 在 Isaac Lab / PhysX 中提供统一的重定向、训练、完整动作评估与导出流程，覆盖 G1、Go2、A3、T1、Bumi 和 Pi+，另含 Go2 任务策略。
- **上游报告：** 重新评估第 32,000 次迭代的 G1 上游检查点，得到归一化回报 **0.8694663、0 / 40 条 LAFAN1 动作失败**。
- **选择时注意：** 结果使用 PhysX，而 supermimic_vibed 使用 MuJoCo Warp；各本体的动作库与训练过程不同，未见动作泛化仍未测量。 [核查版本](https://github.com/Renforce-Dynamics/trackerlab-supermimic/blob/29d24524f2f731bf4df75b319c3e76544165849e/README.md)。

<a href="https://github.com/Renforce-Dynamics/trackerlab-supermimic/blob/29d24524f2f731bf4df75b319c3e76544165849e/docs/media/g1_dance_032000.mp4"><img src="https://raw.githubusercontent.com/Renforce-Dynamics/trackerlab-supermimic/29d24524f2f731bf4df75b319c3e76544165849e/docs/media/g1_dance_032000.gif" width="480" alt="仿真 · G1 策略与参考舞蹈"></a><br><sub>仿真 · G1 策略与参考舞蹈</sub>

</details>

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


## 机器人移植与重定向

面向机器人本体、仿真器或硬件平台的移植，以及动作重定向工具。

<a name="supermimic-retargeted"></a>

### ⭐ SuperMimic Retargeted

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

<a href="https://github.com/panhainan2020/SuperMimic-MuJoCo/blob/db045afa9c52458f213e2c66037387e9c109a03a/README.md"><img src="../assets/community/mujoco-evaluation.png" width="720" alt="报告截图 · LAFAN 训练动作与未见 100STYLE 动作"></a><br><sub>报告截图 · LAFAN 训练动作与未见 100STYLE 动作</sub>

[完整视频展示](https://supermimic-mujoco-results.zippyaspen7.chatgpt.site)

<br>

<a id="supermimic-wheel-legged-wheelbipe"></a>

### SuperMimic 轮腿版（wheelbipe）

[仓库](https://github.com/RadiantForever/supermimic_wheelbipe) · [安装](https://github.com/RadiantForever/supermimic_wheelbipe/blob/0bf3456299a9f754289da58dce6c97c46afd3f03/README.md#setup) · [结果](https://github.com/RadiantForever/supermimic_wheelbipe/blob/0bf3456299a9f754289da58dce6c97c46afd3f03/README.md#results)

- **作者：RadiantForever。** 将 SuperMimic 下游移植到 wheelbipe V14_2 轮腿机器人。人形动作库换成速度指令库；6 维动作（4 个腿目标 + 2 个轮速）在可微世界模型里优化，PhysX / Isaac Lab 只提供数据，训练过程不跑 PPO。
- **上游报告：** 16 条指令网格中统一检查点 **0 / 16 摔倒**、归一化回报 **0.983**；高速专项检查点跟踪 **1.40 m/s、误差 0.01**，偏航到 **10.21 rad/s（1.62 圈/秒）**，变腿行程 **0.20-0.28 m**。单卡 RTX 4090，4096 个并行环境，多段续训累计 3.72 小时；单次运行，未做多随机种子。
- **选择时注意：** 同一台机器人的预训练 PPO 策略只在世界模型前 800 轮混入 buffer，且未做「完全不给老师」的对照，因此这些数字不能全部归因于方法本身。移植需要上游仓库的机器人 USD 资产，没有 URDF。 [核查版本](https://github.com/RadiantForever/supermimic_wheelbipe/blob/0bf3456299a9f754289da58dce6c97c46afd3f03/README.md)。

<a href="https://www.bilibili.com/video/BV1haxM6CEGm/"><img src="../assets/community/wheelbipe-grid.gif" width="480" alt="仿真 · 四种指令工况"></a><br><sub>仿真 · 四种指令工况：10 rad/s 偏航（左上）、0.20-0.28 m 变腿（右上）、1.5 m/s 前进并变腿（左下）、偏航并变腿（右下）</sub>

<br>


## 方法借鉴与探索

将方法思路迁移到其他控制场景；任务和评估协议各不相同。

<a name="flatworld--supermimic-2d"></a>

### ⭐ FlatWorld · SuperMimic-2D

[仓库](https://github.com/swaggyliu/FlatWorld) · [快速开始](https://github.com/swaggyliu/FlatWorld/blob/886dad634c44ed652eea951be62370478f367d8b/supermimic2d/README.md#quick-start) · [参考动作](https://github.com/swaggyliu/FlatWorld/blob/886dad634c44ed652eea951be62370478f367d8b/supermimic2d/README.md#reference-motions-lafan-like-2d)

- **作者：swaggyliu。** 用八关节二维人形角色，在 FlatWorld 中实现共享世界模型与想象策略学习的动作跟踪流程。
- **提供内容：** 提供训练、参考动作物理处理、逐技能渲染和一段 **33.3 秒多技能宣传片**，覆盖行走、跑步、跳跃、舞蹈、格斗、蹲伏及跌倒后起身。
- **选择时注意：** 参考动作是程序生成的 LAFAN 风格二维动作，并非 LAFAN1 数据集；角色还使用轻度根部辅助，因此适合作为方法示例，不是 G1 基准复现。 [核查版本](https://github.com/swaggyliu/FlatWorld/blob/886dad634c44ed652eea951be62370478f367d8b/supermimic2d/README.md)。

<a href="https://github.com/swaggyliu/FlatWorld/blob/886dad634c44ed652eea951be62370478f367d8b/docs/media/promo_supermimic.mp4"><img src="../assets/community/flatworld.gif" width="480" alt="二维仿真 · 33 秒多技能动作跟踪宣传片"></a><br><sub>二维仿真 · 完整 33.3 秒多技能宣传片</sub>

### G0.5 · SuperMimic-style Steering

[仓库](https://github.com/azizkhadraoui/g05) · [实验代码](https://github.com/azizkhadraoui/g05/blob/e3de0de50db7d90068483e2d30f2eacd781300b4/jobs/119_smsteer.py)

- **作者：azizkhadraoui。** 将 SuperMimic 式梯度学习借鉴到 LIBERO 上的 G0.5 VLA 引导：通过世界模型、critic 和冻结流匹配采样器训练噪声策略。
- **选择时注意：** 这是更大 VLA 系统中的一个特定任务引导实验；所链接脚本对应相关方法，仓库中其他规划与记忆结果属于不同实验。 [核查版本](https://github.com/azizkhadraoui/g05/blob/e3de0de50db7d90068483e2d30f2eacd781300b4/jobs/119_smsteer.py)。
- **上游负结果：** 通过世界模型与 critic 直接微调 G0.5 策略权重时，普通锚定配置的切换指令成功数为 **0 / 200**，原任务成功数由 **99 / 100 降至 0 / 100**；更强锚定配置为 **40 / 200**，冻结基线为 **39 / 200**。该直接策略实验与仓库中噪声策略、规划器和记忆模块的成绩分开，本列表未重跑这些测量。[结果表](https://github.com/azizkhadraoui/g05/blob/e3de0de50db7d90068483e2d30f2eacd781300b4/README.md)。

<a href="https://github.com/azizkhadraoui/g05/blob/e3de0de50db7d90068483e2d30f2eacd781300b4/README.md"><img src="../assets/community/g05-steering-entry.png" width="720" alt="代码索引截图 · 世界模型与 critic 引导实验"></a><br><sub>代码索引截图 · 世界模型与 critic 引导实验</sub>

<br>
