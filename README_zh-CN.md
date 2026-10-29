<div align="center">

# Awesome SuperMimic

[![Awesome](https://awesome.re/badge.svg)](https://github.com/sindresorhus/awesome) [![论文](https://img.shields.io/badge/arXiv-2610.28480-b31b1b.svg)](https://arxiv.org/abs/2610.28480) [![License: CC0](https://img.shields.io/badge/License-CC0_1.0-blue.svg)](LICENSE) [![欢迎贡献](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

**收集 SuperMimic 的社区实现、方法扩展、演示和学习资源。**

[English](README.md) · 简体中文

[原始论文](https://arxiv.org/abs/2610.28480) · [官方项目](https://supermimic.github.io/) · [交互演示](https://supermimic.github.io/demo/) · [社区项目](#社区项目)

</div>

按 GitHub Stars、任务与技术栈寻找社区实现。Stars 反映仓库关注度；⭐ 维护者精选推荐有来源支持的技术特点。成绩与演示均为上游报告，本清单未独立重跑。

<a id="目录"></a>

[排行榜](#most-starred-projects) · [分类浏览](#browse-by-category) · [维护者精选](#maintainers-picks) · [新收录项目](#new--noteworthy) · [原始工作](#原始-supermimic) · [参与贡献](#参与贡献)

## 社区项目

<!-- BEGIN GENERATED PROJECTS -->

**38 个项目 · 9 个分类**

<a id="most-starred-projects"></a>

### Most Starred Projects · Stars 排行榜

GitHub API 数值快照：**2026-10-29 16:57:08 UTC** · 每日检查 · Stars 降序，同分按 `owner/repo` 忽略大小写升序。Stars 计入整个仓库（含更大框架），反映关注度，不代表基准成绩。

数据状态：完整有效快照。 [Update policy](docs/star-rankings.md).

| 排名 | 项目 | GitHub&nbsp;Stars | 分类 | 一句话亮点 |
| ---: | --- | --- | --- | --- |
| 1 | [HoloMotion · SuperMimic](https://github.com/HorizonRobotics/HoloMotion) | [![750 stars](assets/stars/1028843437.svg)](https://github.com/HorizonRobotics/HoloMotion/stargazers) | [框架与训练栈](#框架与训练栈) | SuperMimic 与 PPO 共享 HoloMotion 任务和评估。 |
| 2 | [supermimic_vibed](https://github.com/zita-ch/supermimic_vibed) | [![724 stars](assets/stars/1428714029.svg)](https://github.com/zita-ch/supermimic_vibed/stargazers) | [独立复现](#独立复现) | G1 LAFAN1 基线与完整片段评估工具。 |
| 3 | [SuperMimic-Reproduced](https://github.com/CuboiLeo/SuperMimic-Reproduced) | [![315 stars](assets/stars/1429037845.svg)](https://github.com/CuboiLeo/SuperMimic-Reproduced/stargazers) | [独立复现](#独立复现) | BONES-SEED 训练日志、权重与观测配置对照。 |
| 4 | [InstinctMJ · SuperMimic](https://github.com/project-instinct/InstinctMJ/tree/supermimic) | [![301 stars](assets/stars/1176761185.svg)](https://github.com/project-instinct/InstinctMJ/stargazers) | [感知与地形](#感知地形与四足任务) | 深度感知 G1 世界模型与地形跟踪；使用 supermimic 分支。 |
| 5 | [UniSuperMimic](https://github.com/Motphys/Uni-SuperMimic) | [![205 stars](assets/stars/1429498465.svg)](https://github.com/Motphys/Uni-SuperMimic/stargazers) | [框架与训练栈](#框架与训练栈) | 含 LAFAN1 与 BONES-SEED 流程的 G1 训练栈。 |
| 6 | [MorphMimic](https://github.com/lzyang2000/morphmimic) | [![152 stars](assets/stars/1430789167.svg)](https://github.com/lzyang2000/morphmimic/stargazers) | [方法改动](#方法改动与形态适配) | G1、X2 Ultra、T2 跨本体共享世界模型与策略。 |
| 7 | [Dex SuperMimic](https://github.com/CumulusAlpha/Dex-Supermimic) | [![74 stars](assets/stars/1433804344.svg)](https://github.com/CumulusAlpha/Dex-Supermimic/stargazers) | [操作与灵巧手](#操作与灵巧手) | Wuji 灵巧手方块重定向、转笔与公开权重。 |
| 8 | [Go2-SuperMimic](https://github.com/Zhengtianjin/go2-supermimic) | [![69 stars](assets/stars/1431486582.svg)](https://github.com/Zhengtianjin/go2-supermimic/stargazers) | [感知与地形](#感知地形与四足任务) | Go2 追逐、闪避任务与公开仿真策略。 |
| 9 | [InstantTrack](https://github.com/Huy-Quang-Dao/instantTrack) | [![52 stars](assets/stars/1438037302.svg)](https://github.com/Huy-Quang-Dao/instantTrack/stargazers) | [方法改动](#方法改动与形态适配) | GPU 训练循环优化，附三个种子的 LAFAN1 报告。 |
| 10 | [FlatWorld · SuperMimic-2D](https://github.com/swaggyliu/FlatWorld) | [![43 stars](assets/stars/1284715083.svg)](https://github.com/swaggyliu/FlatWorld/stargazers) | [学习示例](#方法借鉴与探索) | 用二维人形角色演示共享世界模型学习。 |
| 11 | [SuperMimic for Robot Manipulation](https://github.com/emoPointer/supermimic_manipulation) | [![39 stars](assets/stars/1433554854.svg)](https://github.com/emoPointer/supermimic_manipulation/stargazers) | [操作与灵巧手](#操作与灵巧手) | 三项 ARX5 机械臂任务，附权重与重置状态库。 |
| 12 | [SuperMimic-Repro-Sim2Real](https://github.com/NJU-R-L-Group-Embodied-Lab/SuperMimic-Repro-Sim2Real) | [![36 stars](assets/stars/1433556794.svg)](https://github.com/NJU-R-L-Group-Embodied-Lab/SuperMimic-Repro-Sim2Real/stargazers) | [真机部署](#真机部署与-sim2real) | G1 真机舞蹈演示与单片段部署记录。 |
| 13 | [In-Hand Rotation mjlab](https://github.com/Msornerrrr/in-hand-rotation-mjlab) | [![34 stars](assets/stars/1162247047.svg)](https://github.com/Msornerrrr/in-hand-rotation-mjlab/stargazers) | [操作与灵巧手](#操作与灵巧手) | LEAP 灵巧手世界模型与 PPO 仿真对照。 |
| 14 | [Muscle SuperMimic](https://github.com/kaibohex/muscle-supermimic) | [![33 stars](assets/stars/1434932501.svg)](https://github.com/kaibohex/muscle-supermimic/stargazers) | [肌肉与交互](#肌肉驱动交互与诊断) | 两种肌肉驱动本体，附未见 KIT 动作评估。 |
| 15 | [allmimic](https://github.com/Shimingyi/allmimic) | [![31 stars](assets/stars/1431958748.svg)](https://github.com/Shimingyi/allmimic/stargazers) | [方法改动](#方法改动与形态适配) | 上半身残差动作与均衡动作采样。 |
| 16 | [Rethinking SuperMimic](https://github.com/btx0424/rethinking-supermimic) | [![27 stars](assets/stars/1429359559.svg)](https://github.com/btx0424/rethinking-supermimic/stargazers) | [方法改动](#方法改动与形态适配) | 目标条件化对照、HL-Gauss critic 与梯度检查。 |
| 17 | [Standing MBRL vs PPO](https://github.com/JackMin7/supermimic_whole_body_tracking) | [![20 stars](assets/stars/1429495052.svg)](https://github.com/JackMin7/supermimic_whole_body_tracking/stargazers) | [方法改动](#方法改动与形态适配) | 站立任务中 MBRL 与 PPO 的条件对照。 |
| 18 | [ScaleBFM_Plus · SuperMimic](https://github.com/Hxxxz0/ScaleBFM_Plus) | [![19 stars](assets/stars/1431877986.svg)](https://github.com/Hxxxz0/ScaleBFM_Plus/stargazers) | [框架与训练栈](#框架与训练栈) | 人形 Transformer 策略集成与留出动作评估。 |
| 19 | [SuperMimic-MuJoCo](https://github.com/panhainan2020/SuperMimic-MuJoCo) | [![15 stars](assets/stars/1430957174.svg)](https://github.com/panhainan2020/SuperMimic-MuJoCo/stargazers) | [本体移植](#机器人移植与重定向) | G1 移植，附留出 100STYLE 评估与推理权重。 |
| 20 | [TrackerLab SuperMimic](https://github.com/Renforce-Dynamics/trackerlab-supermimic) | [![13 stars](assets/stars/1430222310.svg)](https://github.com/Renforce-Dynamics/trackerlab-supermimic/stargazers) | [框架与训练栈](#框架与训练栈) | 多本体重定向、训练、评估与导出工具。 |
| 21 | [SuperMimic Parkour](https://github.com/yhx1203/supermimic_parkour) | [![12 stars](assets/stars/1430513100.svg)](https://github.com/yhx1203/supermimic_parkour/stargazers) | [感知与地形](#感知地形与四足任务) | 五技能 G1 跑酷检查点与浏览器回放。 |
| 22 | [SuperMimic Retargeted](https://github.com/tianshuwu/supermimic-retargeted) | [![9 stars](assets/stars/1430469940.svg)](https://github.com/tianshuwu/supermimic-retargeted/stargazers) | [本体移植](#机器人移植与重定向) | G1 / A3 / X2 Ultra 重定向与坐标检查。 |
| 23 | [SuperMimic Mjlab](https://github.com/Breezewrf/supermimic_mjlab) | [![8 stars](assets/stars/1429560578.svg)](https://github.com/Breezewrf/supermimic_mjlab/stargazers) | [独立复现](#独立复现) | 逐项训练消融与公开检查点。 |
| 24 | [SuperMimic G1 Deployment](https://github.com/KyrieYoung926/supermimic_deploy) | [![8 stars](assets/stars/1430946541.svg)](https://github.com/KyrieYoung926/supermimic_deploy/stargazers) | [真机部署](#真机部署与-sim2real) | 29 自由度 G1 部署，含仿真与真机指南。 |
| 25 | [Humanoid Mimic · SuperMimic](https://github.com/shuayyy/humanoid-amp-ppo) | [![8 stars](assets/stars/1285577591.svg)](https://github.com/shuayyy/humanoid-amp-ppo/stargazers) | [操作与灵巧手](#操作与灵巧手) | G1 行走、下蹲与抬箱的共享任务对照。 |
| 26 | [SuperMimic Wheel-Legged (wheelbipe)](https://github.com/RadiantForever/supermimic_wheelbipe) | [![7 stars](assets/stars/1437090261.svg)](https://github.com/RadiantForever/supermimic_wheelbipe/stargazers) | [本体移植](#机器人移植与重定向) | 面向 wheelbipe 轮足机器人的速度指令学习。 |
| 27 | [SuperMimic-perceptive](https://github.com/mode1223345/SuperMimic-perceptive) | [![6 stars](assets/stars/1432125557.svg)](https://github.com/mode1223345/SuperMimic-perceptive/stargazers) | [感知与地形](#感知地形与四足任务) | 策略、critic 与世界模型共享冻结高度图编码器。 |
| 28 | [SuperMimic on LocoMuJoCo](https://github.com/Alchedata/supermimic-locomujoco) | [![5 stars](assets/stars/1432664861.svg)](https://github.com/Alchedata/supermimic-locomujoco/stargazers) | [方法改动](#方法改动与形态适配) | H1 ODE 世界模型与抗饱和消融。 |
| 29 | [supermimic_vibe](https://github.com/dhmbb2/supermimic_vibe) | [![5 stars](assets/stars/1429888171.svg)](https://github.com/dhmbb2/supermimic_vibe/stargazers) | [独立复现](#独立复现) | PPO-Sim / PPO-WM 对照与时域、critic 消融。 |
| 30 | [SuperMimic E1](https://github.com/wenconggan/SuperMimic_e1) | [![5 stars](assets/stars/1430480272.svg)](https://github.com/wenconggan/SuperMimic_e1/stargazers) | [本体移植](#机器人移植与重定向) | DroidUp E1 适配与原生 MuJoCo 跨仿真回放。 |
| 31 | [SuperMimicKit](https://github.com/OMEGA-i/SuperMimicKit) | [![4 stars](assets/stars/1431562951.svg)](https://github.com/OMEGA-i/SuperMimicKit/stargazers) | [框架与训练栈](#框架与训练栈) | G1 / H2 / A3 重定向与实验性浏览器预览。 |
| 32 | [SuperMimic Oli](https://github.com/liuskywalkerjskd/supermimic_oli) | [![3 stars](assets/stars/1431102076.svg)](https://github.com/liuskywalkerjskd/supermimic_oli/stargazers) | [本体移植](#机器人移植与重定向) | 31 自由度 LimX Oli 移植与完整动作视频导出。 |
| 33 | [SuperMimic Lab](https://github.com/chu-fa/isaaclab-supermimic) | [![2 stars](assets/stars/1431327517.svg)](https://github.com/chu-fa/isaaclab-supermimic/stargazers) | [框架与训练栈](#框架与训练栈) | 可复用学习器与 runner，附独立 A3 示例。 |
| 34 | [SuperMimic Backflip Diagnostics](https://github.com/liudi159/supermimic-backflip-5090) | [![2 stars](assets/stars/1432819468.svg)](https://github.com/liudi159/supermimic-backflip-5090/stargazers) | [肌肉与交互](#肌肉驱动交互与诊断) | G1 后空翻的对称性、接触与落地诊断。 |
| 35 | [SuperMimic on RTX 5080](https://github.com/rzc156/supermimic-rtx5080) | [![2 stars](assets/stars/1434000857.svg)](https://github.com/rzc156/supermimic-rtx5080/stargazers) | [独立复现](#独立复现) | 面向 16 GB RTX 5080 的 G1 复现。 |
| 36 | [SuperMimic on Apple M5](https://github.com/WXyuany/supermimic-m5) | [![1 stars](assets/stars/1430927278.svg)](https://github.com/WXyuany/supermimic-m5/stargazers) | [本体移植](#机器人移植与重定向) | Apple Silicon 训练适配与公开 G1 权重。 |
| 37 | [G0.5 · SuperMimic-style Steering](https://github.com/azizkhadraoui/g05) | [![0 stars](assets/stars/1425368329.svg)](https://github.com/azizkhadraoui/g05/stargazers) | [学习示例](#方法借鉴与探索) | 以世界模型、critic 梯度开展 VLA 引导实验。 |
| 38 | [SuperMimic-PERA](https://github.com/shangchaohu718/supermimic-pera) | [![0 stars](assets/stars/1430576677.svg)](https://github.com/shangchaohu718/supermimic-pera/stargazers) | [肌肉与交互](#肌肉驱动交互与诊断) | 冻结跟踪策略与独立交互实验。 |

<a id="browse-by-category"></a>

### Browse by Category · 分类浏览

[真机部署 (2)](#真机部署与-sim2real) · [独立复现 (5)](#独立复现) · [方法改动 (6)](#方法改动与形态适配) · [感知与地形 (4)](#感知地形与四足任务) · [操作与灵巧手 (4)](#操作与灵巧手) · [肌肉与交互 (3)](#肌肉驱动交互与诊断) · [框架与训练栈 (6)](#框架与训练栈) · [本体移植 (6)](#机器人移植与重定向) · [学习示例 (2)](#方法借鉴与探索)

分类内同样按 Stars 排序；完整实验、限制与 GIF 见各项目详情。

<a id="maintainers-picks"></a>

### Maintainer’s Picks · 维护者精选

⭐ 延续原有人工精选，理由来自已收录资料，与 Stars 排名独立。

| 项目 | 推荐理由 |
| --- | --- |
| ⭐ [SuperMimic-Repro-Sim2Real](#supermimic-repro-sim2real) | G1 真机演示与部署记录 |
| ⭐ [supermimic_vibed](#supermimic_vibed) | LAFAN1 训练基线 |
| ⭐ [SuperMimic-Reproduced](#supermimic-reproduced) | BONES-SEED 实验日志与权重 |
| ⭐ [SuperMimic Mjlab](#supermimic-mjlab) | 逐项性能消融与公开检查点 |
| ⭐ [InstantTrack](#instanttrack) | 单张 RTX 5090 约 15 分钟达标 LAFAN1，三个种子 |
| ⭐ [MorphMimic](#morphmimic) | G1、X2 Ultra、T2 跨本体共享世界模型或策略 |
| ⭐ [InstinctMJ · SuperMimic](#instinctmj--supermimic) | 深度视觉世界模型与地形跟踪 |
| ⭐ [Go2-SuperMimic](#go2-supermimic) | 四足追逐与闪避，附公开策略 |
| ⭐ [SuperMimic for Robot Manipulation](#supermimic-for-robot-manipulation) | 三项 ARX5 机械臂任务，附权重与重置状态库 |
| ⭐ [Dex SuperMimic](#dex-supermimic) | Wuji 灵巧手方块重定向、转笔与公开权重 |
| ⭐ [In-Hand Rotation mjlab](#in-hand-rotation-mjlab) | LEAP 手世界模型 / PPO 仿真对照 |
| ⭐ [Muscle SuperMimic](#muscle-supermimic) | 两种肌肉驱动本体，含未见 KIT 动作评估 |
| ⭐ [UniSuperMimic](#unisupermimic) | UniLab 集成与两套动作数据流程 |
| ⭐ [ScaleBFM_Plus · SuperMimic](#scalebfm_plus--supermimic) | 人形 Transformer 策略集成与留出动作评估 |
| ⭐ [SuperMimic Retargeted](#supermimic-retargeted) | G1 / A3 / X2 Ultra 重定向与坐标检查 |
| ⭐ [FlatWorld · SuperMimic-2D](#flatworld--supermimic-2d) | 用 2D 多技能演示理解学习闭环 |

<a id="new--noteworthy"></a>

### New & Noteworthy · 新收录项目

最近五个收录条目，按本清单 Git 历史中的首次收录日期排序，同日按仓库名排序。日期链接可核查；不是项目发布日期或质量评分，不设 Stars 门槛。

| 收录日期 | 项目 | 看点 |
| --- | --- | --- |
| [2026-10-29](https://github.com/miao-org/awesome-supermimic/commit/4ec2021a76c389760c79cf8149fa5a20e998fe98) | [InstantTrack](#instanttrack) | GPU 训练循环优化，附三个种子的 LAFAN1 报告。 |
| [2026-10-28](https://github.com/miao-org/awesome-supermimic/commit/0035f0d90c1fae44cf2ecbf6fb8584bee6f1f415) | [Standing MBRL vs PPO](#standing-mbrl-vs-ppo) | 站立任务中 MBRL 与 PPO 的条件对照。 |
| [2026-10-28](https://github.com/miao-org/awesome-supermimic/commit/f03b1b9e0a24b3ca65f6da06ec3f12aa8eced02c) | [In-Hand Rotation mjlab](#in-hand-rotation-mjlab) | LEAP 灵巧手世界模型与 PPO 仿真对照。 |
| [2026-10-28](https://github.com/miao-org/awesome-supermimic/commit/9706213a5c3eee8ea16e0e53fdc3d589eab23441) | [SuperMimic Wheel-Legged (wheelbipe)](#supermimic-wheel-legged-wheelbipe) | 面向 wheelbipe 轮足机器人的速度指令学习。 |
| [2026-10-28](https://github.com/miao-org/awesome-supermimic/commit/0035f0d90c1fae44cf2ecbf6fb8584bee6f1f415) | [SuperMimic on RTX 5080](#supermimic-on-rtx-5080) | 面向 16 GB RTX 5080 的 G1 复现。 |

<a id="真机部署与-sim2real"></a>

### 真机部署与 Sim2Real (2)

<a id="supermimic-repro-sim2real"></a>
<a id="-supermimic-repro-sim2real"></a>

**[SuperMimic-Repro-Sim2Real](https://github.com/NJU-R-L-Group-Embodied-Lab/SuperMimic-Repro-Sim2Real)** · [![36 stars](assets/stars/1433556794.svg)](https://github.com/NJU-R-L-Group-Embodied-Lab/SuperMimic-Repro-Sim2Real/stargazers) · ⭐ 维护者精选

**技术栈:** mjlab / MuJoCo / Unitree SDK · **作者:** NJU R&amp;L Group Embodied Lab<br>
G1 真机舞蹈演示与单片段部署记录。

[仓库](https://github.com/NJU-R-L-Group-Embodied-Lab/SuperMimic-Repro-Sim2Real) · [演示](https://github.com/NJU-R-L-Group-Embodied-Lab/SuperMimic-Repro-Sim2Real/releases/download/v1.1/shanshenbu_pro_real_robot.mp4) · [实验与详情](docs/community-projects_zh-CN.md#supermimic-repro-sim2real) · [快速开始](https://github.com/NJU-R-L-Group-Embodied-Lab/SuperMimic-Repro-Sim2Real/blob/f8f60d7bbdba68468c050ef100af02d752ca238e/README.md#快速开始)

<a id="supermimic-g1-deployment"></a>

**[SuperMimic G1 Deployment](https://github.com/KyrieYoung926/supermimic_deploy)** · [![8 stars](assets/stars/1430946541.svg)](https://github.com/KyrieYoung926/supermimic_deploy/stargazers)

**技术栈:** ONNX Runtime / MuJoCo / Unitree SDK2 · **作者:** KyrieYoung926<br>
29 自由度 G1 部署，含仿真与真机指南。

[仓库](https://github.com/KyrieYoung926/supermimic_deploy) · [演示](https://github.com/KyrieYoung926/supermimic_deploy) · [实验与详情](docs/community-projects_zh-CN.md#supermimic-g1-deployment) · [MuJoCo 使用](https://github.com/KyrieYoung926/supermimic_deploy/blob/7e63e3bbd5150d55afbdece28278781800f3ed21/README.md#3-run-in-mujoco)


<a id="独立复现"></a>

### 独立复现 (5)

<a id="supermimic_vibed"></a>
<a id="-supermimic_vibed"></a>

**[supermimic_vibed](https://github.com/zita-ch/supermimic_vibed)** · [![724 stars](assets/stars/1428714029.svg)](https://github.com/zita-ch/supermimic_vibed/stargazers) · ⭐ 维护者精选

**技术栈:** Isaac Lab 3 · **作者:** Chong Zhang<br>
G1 LAFAN1 基线与完整片段评估工具。

[仓库](https://github.com/zita-ch/supermimic_vibed) · [演示](https://github.com/zita-ch/supermimic_vibed) · [实验与详情](docs/community-projects_zh-CN.md#supermimic_vibed) · [安装与使用](https://github.com/zita-ch/supermimic_vibed/blob/a1508d42c9d1699a52e8233ab16d08c488441ab9/README.md#setup)

<a id="supermimic-reproduced"></a>
<a id="-supermimic-reproduced"></a>

**[SuperMimic-Reproduced](https://github.com/CuboiLeo/SuperMimic-Reproduced)** · [![315 stars](assets/stars/1429037845.svg)](https://github.com/CuboiLeo/SuperMimic-Reproduced/stargazers) · ⭐ 维护者精选

**技术栈:** mjlab · **作者:** CuboiLeo<br>
BONES-SEED 训练日志、权重与观测配置对照。

[仓库](https://github.com/CuboiLeo/SuperMimic-Reproduced) · [演示](https://github.com/CuboiLeo/SuperMimic-Reproduced/releases/tag/e8-boneseed-100k) · [实验与详情](docs/community-projects_zh-CN.md#supermimic-reproduced) · [环境与安装](https://github.com/CuboiLeo/SuperMimic-Reproduced/blob/ba6105349069bf040f1fdad60873d13138d505a2/README.md#setup)

<a id="supermimic-mjlab"></a>
<a id="-supermimic-mjlab"></a>

**[SuperMimic Mjlab](https://github.com/Breezewrf/supermimic_mjlab)** · [![8 stars](assets/stars/1429560578.svg)](https://github.com/Breezewrf/supermimic_mjlab/stargazers) · ⭐ 维护者精选

**技术栈:** mjlab · **作者:** Breezewrf<br>
逐项训练消融与公开检查点。

[仓库](https://github.com/Breezewrf/supermimic_mjlab) · [演示](https://github.com/Breezewrf/supermimic_mjlab/blob/77183062eb92026bfbee2daf276f87cad36fd957/doc/assets/demo_v0.gif) · [实验与详情](docs/community-projects_zh-CN.md#supermimic-mjlab) · [安装](https://github.com/Breezewrf/supermimic_mjlab/blob/77183062eb92026bfbee2daf276f87cad36fd957/doc/setup_en.md)

<a id="supermimic_vibe"></a>

**[supermimic_vibe](https://github.com/dhmbb2/supermimic_vibe)** · [![5 stars](assets/stars/1429888171.svg)](https://github.com/dhmbb2/supermimic_vibe/stargazers)

**技术栈:** mjlab · **作者:** dhmbb2<br>
PPO-Sim / PPO-WM 对照与时域、critic 消融。

[仓库](https://github.com/dhmbb2/supermimic_vibe) · [演示](https://github.com/dhmbb2/supermimic_vibe/blob/072f0910dadc9d95c720e625b546120e9ce917c9/README.md) · [实验与详情](docs/community-projects_zh-CN.md#supermimic_vibe) · [安装](https://github.com/dhmbb2/supermimic_vibe/blob/072f0910dadc9d95c720e625b546120e9ce917c9/README.md#setup)

<a id="supermimic-on-rtx-5080"></a>

**[SuperMimic on RTX 5080](https://github.com/rzc156/supermimic-rtx5080)** · [![2 stars](assets/stars/1434000857.svg)](https://github.com/rzc156/supermimic-rtx5080/stargazers)

**技术栈:** mjlab · **作者:** rzc156<br>
面向 16 GB RTX 5080 的 G1 复现。

[仓库](https://github.com/rzc156/supermimic-rtx5080) · [演示](https://github.com/rzc156/supermimic-rtx5080/blob/df967c61c29a2ed9ba6b188e1607ba59225fe8a7/results/lafan1_anchor/videos/index.html) · [实验与详情](docs/community-projects_zh-CN.md#supermimic-on-rtx-5080) · [复现分析](https://github.com/rzc156/supermimic-rtx5080/blob/df967c61c29a2ed9ba6b188e1607ba59225fe8a7/REPRODUCTION_ANALYSIS.md)


<a id="方法改动与形态适配"></a>

### 方法改动与形态适配 (6)

<a id="morphmimic"></a>
<a id="-morphmimic"></a>

**[MorphMimic](https://github.com/lzyang2000/morphmimic)** · [![152 stars](assets/stars/1430789167.svg)](https://github.com/lzyang2000/morphmimic/stargazers) · ⭐ 维护者精选

**技术栈:** mjlab · **作者:** Lizhi Yang et al<br>
G1、X2 Ultra、T2 跨本体共享世界模型与策略。

[仓库](https://github.com/lzyang2000/morphmimic) · [演示](https://lzyang2000.github.io/morphmimic/static/videos/dance_hiphop_shuffle_sequence_v_001_R_003__A306.mp4) · [实验与详情](docs/community-projects_zh-CN.md#morphmimic) · [安装](https://github.com/lzyang2000/morphmimic/blob/aa40fe46a7fa995ba7a7354ad065a2c8ad64a302/README.md#setup)

<a id="instanttrack"></a>
<a id="-instanttrack"></a>

**[InstantTrack](https://github.com/Huy-Quang-Dao/instantTrack)** · [![52 stars](assets/stars/1438037302.svg)](https://github.com/Huy-Quang-Dao/instantTrack/stargazers) · ⭐ 维护者精选

**技术栈:** mjlab · **作者:** Huy-Quang-Dao<br>
GPU 训练循环优化，附三个种子的 LAFAN1 报告。

[仓库](https://github.com/Huy-Quang-Dao/instantTrack) · [演示](https://github.com/Huy-Quang-Dao/instantTrack/blob/a33691a08bca8802d9d2985f62e2567479735a8e/media/equal_time_15min.gif) · [实验与详情](docs/community-projects_zh-CN.md#instanttrack) · [安装](https://github.com/Huy-Quang-Dao/instantTrack/blob/a33691a08bca8802d9d2985f62e2567479735a8e/README.md#setup)

<a id="allmimic"></a>

**[allmimic](https://github.com/Shimingyi/allmimic)** · [![31 stars](assets/stars/1431958748.svg)](https://github.com/Shimingyi/allmimic/stargazers)

**技术栈:** mjlab · **作者:** Shimingyi<br>
上半身残差动作与均衡动作采样。

[仓库](https://github.com/Shimingyi/allmimic) · [演示](https://github.com/Shimingyi/allmimic) · [实验与详情](docs/community-projects_zh-CN.md#allmimic) · [安装](https://github.com/Shimingyi/allmimic/blob/cb334ff674b2f57248f33f8c21b7fb526fbdf8cc/README.md#install)

<a id="rethinking-supermimic"></a>

**[Rethinking SuperMimic](https://github.com/btx0424/rethinking-supermimic)** · [![27 stars](assets/stars/1429359559.svg)](https://github.com/btx0424/rethinking-supermimic/stargazers)

**技术栈:** mjlab · **作者:** btx0424<br>
目标条件化对照、HL-Gauss critic 与梯度检查。

[仓库](https://github.com/btx0424/rethinking-supermimic) · [演示](https://github.com/btx0424/rethinking-supermimic/blob/ecdaeb6a916a16cf7eb69b19226c17be31a6bc27/README.md) · [实验与详情](docs/community-projects_zh-CN.md#rethinking-supermimic) · [安装](https://github.com/btx0424/rethinking-supermimic/blob/aa77b71054a850075431248f1534bb77ca62b4d8/README.md#installation)

<a id="standing-mbrl-vs-ppo"></a>

**[Standing MBRL vs PPO](https://github.com/JackMin7/supermimic_whole_body_tracking)** · [![20 stars](assets/stars/1429495052.svg)](https://github.com/JackMin7/supermimic_whole_body_tracking/stargazers)

**技术栈:** RSL-RL / G1 · **作者:** JackMin7<br>
站立任务中 MBRL 与 PPO 的条件对照。

[仓库](https://github.com/JackMin7/supermimic_whole_body_tracking) · [演示](https://github.com/JackMin7/supermimic_whole_body_tracking/blob/553a7d32dc5fc00cbe6de5ee46479af2fcceeda8/media/ppo_vs_mbrl_60s.mp4) · [实验与详情](docs/community-projects_zh-CN.md#standing-mbrl-vs-ppo) · [实验说明](https://github.com/JackMin7/supermimic_whole_body_tracking/blob/553a7d32dc5fc00cbe6de5ee46479af2fcceeda8/docs/EXPERIMENTS.md)

<a id="supermimic-on-locomujoco"></a>

**[SuperMimic on LocoMuJoCo](https://github.com/Alchedata/supermimic-locomujoco)** · [![5 stars](assets/stars/1432664861.svg)](https://github.com/Alchedata/supermimic-locomujoco/stargazers)

**技术栈:** JAX / LocoMuJoCo · **作者:** Alchedata<br>
H1 ODE 世界模型与抗饱和消融。

[仓库](https://github.com/Alchedata/supermimic-locomujoco) · [演示](https://github.com/Alchedata/supermimic-locomujoco/blob/de9f39191b9e8b87ff1afd2b0129dd93d4795e8c/docs/figures/return_vs_step.png) · [实验与详情](docs/community-projects_zh-CN.md#supermimic-on-locomujoco) · [安装](https://github.com/Alchedata/supermimic-locomujoco/blob/de9f39191b9e8b87ff1afd2b0129dd93d4795e8c/README.md#setup)


<a id="感知地形与四足任务"></a>

### 感知、地形与四足任务 (4)

<a id="instinctmj--supermimic"></a>
<a id="-instinctmj--supermimic"></a>

**[InstinctMJ · SuperMimic](https://github.com/project-instinct/InstinctMJ/tree/supermimic)** · [![301 stars](assets/stars/1176761185.svg)](https://github.com/project-instinct/InstinctMJ/stargazers) · ⭐ 维护者精选

**技术栈:** mjlab / instinct_rl · **作者:** Project Instinct<br>
深度感知 G1 世界模型与地形跟踪；使用 supermimic 分支。

[仓库](https://github.com/project-instinct/InstinctMJ/tree/supermimic) · [演示](https://github.com/project-instinct/InstinctMJ/blob/7ca851e002980011f24a1664011305d0ba94aefc/src/instinct_mj/rl/supermimic/assets/world_model_simple.png) · [实验与详情](docs/community-projects_zh-CN.md#instinctmj--supermimic) · [方法与结果](https://github.com/project-instinct/InstinctMJ/blob/7ca851e002980011f24a1664011305d0ba94aefc/src/instinct_mj/rl/supermimic/README.md#results)

<a id="go2-supermimic"></a>
<a id="-go2-supermimic"></a>

**[Go2-SuperMimic](https://github.com/Zhengtianjin/go2-supermimic)** · [![69 stars](assets/stars/1431486582.svg)](https://github.com/Zhengtianjin/go2-supermimic/stargazers) · ⭐ 维护者精选

**技术栈:** mjlab · **作者:** Zhengtianjin<br>
Go2 追逐、闪避任务与公开仿真策略。

[仓库](https://github.com/Zhengtianjin/go2-supermimic) · [演示](https://github.com/Zhengtianjin/go2-supermimic) · [实验与详情](docs/community-projects_zh-CN.md#go2-supermimic) · [快速开始](https://github.com/Zhengtianjin/go2-supermimic/blob/054a13c13285a1c94b2e69dc8ac7331f9a8c71cf/README.md#-quickstart)

<a id="supermimic-parkour"></a>

**[SuperMimic Parkour](https://github.com/yhx1203/supermimic_parkour)** · [![12 stars](assets/stars/1430513100.svg)](https://github.com/yhx1203/supermimic_parkour/stargazers)

**技术栈:** mjlab / PHP Parkour · **作者:** yhx1203<br>
五技能 G1 跑酷检查点与浏览器回放。

[仓库](https://github.com/yhx1203/supermimic_parkour) · [演示](https://github.com/yhx1203/supermimic_parkour/blob/f398519453a25b3f10722626b7356266d8b7f875/doc/%E5%BD%95%E5%B1%8F%202026%E5%B9%B410%E6%9C%8826%E6%97%A5%2016%E6%97%B641%E5%88%8626%E7%A7%92.gif) · [实验与详情](docs/community-projects_zh-CN.md#supermimic-parkour) · [数据配置](https://github.com/yhx1203/supermimic_parkour/blob/f398519453a25b3f10722626b7356266d8b7f875/README.md#motion-data)

<a id="supermimic-perceptive"></a>

**[SuperMimic-perceptive](https://github.com/mode1223345/SuperMimic-perceptive)** · [![6 stars](assets/stars/1432125557.svg)](https://github.com/mode1223345/SuperMimic-perceptive/stargazers)

**技术栈:** Isaac Lab 3 · **作者:** mode1223345<br>
策略、critic 与世界模型共享冻结高度图编码器。

[仓库](https://github.com/mode1223345/SuperMimic-perceptive) · [演示](https://github.com/mode1223345/SuperMimic-perceptive/blob/3d38bacbaf5bee7e782bdada6a6da678264d0bfa/results/Curves.png) · [实验与详情](docs/community-projects_zh-CN.md#supermimic-perceptive) · [方法](https://github.com/mode1223345/SuperMimic-perceptive/blob/3d38bacbaf5bee7e782bdada6a6da678264d0bfa/Ae.md)


<a id="操作与灵巧手"></a>

### 操作与灵巧手 (4)

<a id="dex-supermimic"></a>
<a id="-dex-supermimic"></a>

**[Dex SuperMimic](https://github.com/CumulusAlpha/Dex-Supermimic)** · [![74 stars](assets/stars/1433804344.svg)](https://github.com/CumulusAlpha/Dex-Supermimic/stargazers) · ⭐ 维护者精选

**技术栈:** mjlab / MuJoCo Warp / InstinctMJ · **作者:** CumulusAlpha<br>
Wuji 灵巧手方块重定向、转笔与公开权重。

[仓库](https://github.com/CumulusAlpha/Dex-Supermimic) · [演示](https://github.com/CumulusAlpha/Dex-Supermimic/blob/3a7c1a33fd8e5c6cc047e381ea9309da96553c27/docs/demos/hand1_reorient.gif) · [实验与详情](docs/community-projects_zh-CN.md#dex-supermimic) · [安装](https://github.com/CumulusAlpha/Dex-Supermimic/blob/3a7c1a33fd8e5c6cc047e381ea9309da96553c27/README.md#installation)

<a id="supermimic-for-robot-manipulation"></a>
<a id="-supermimic-for-robot-manipulation"></a>

**[SuperMimic for Robot Manipulation](https://github.com/emoPointer/supermimic_manipulation)** · [![39 stars](assets/stars/1433554854.svg)](https://github.com/emoPointer/supermimic_manipulation/stargazers) · ⭐ 维护者精选

**技术栈:** mjlab / MuJoCo Warp · **作者:** Zhiqiang Zhou (emoPointer)<br>
三项 ARX5 机械臂任务，附权重与重置状态库。

[仓库](https://github.com/emoPointer/supermimic_manipulation) · [演示](https://github.com/emoPointer/supermimic_manipulation) · [实验与详情](docs/community-projects_zh-CN.md#supermimic-for-robot-manipulation) · [安装](https://github.com/emoPointer/supermimic_manipulation/blob/810e5768c50117d2fec75f20f9e643a11cd0882b/README.md#install)

<a id="in-hand-rotation-mjlab"></a>
<a id="-in-hand-rotation-mjlab"></a>

**[In-Hand Rotation mjlab](https://github.com/Msornerrrr/in-hand-rotation-mjlab)** · [![34 stars](assets/stars/1162247047.svg)](https://github.com/Msornerrrr/in-hand-rotation-mjlab/stargazers) · ⭐ 维护者精选

**技术栈:** mjlab / MuJoCo Warp · **作者:** Msornerrrr<br>
LEAP 灵巧手世界模型与 PPO 仿真对照。

[仓库](https://github.com/Msornerrrr/in-hand-rotation-mjlab) · [演示](https://github.com/Msornerrrr/in-hand-rotation-mjlab) · [实验与详情](docs/community-projects_zh-CN.md#in-hand-rotation-mjlab) · [安装](https://github.com/Msornerrrr/in-hand-rotation-mjlab/blob/0ab03eb2244b4a1a020d94ef38a4823bb9e15ba0/README.md#install)

<a id="humanoid-mimic--supermimic"></a>

**[Humanoid Mimic · SuperMimic](https://github.com/shuayyy/humanoid-amp-ppo)** · [![8 stars](assets/stars/1285577591.svg)](https://github.com/shuayyy/humanoid-amp-ppo/stargazers)

**技术栈:** mjlab · **作者:** shuayyy<br>
G1 行走、下蹲与抬箱的共享任务对照。

[仓库](https://github.com/shuayyy/humanoid-amp-ppo) · [演示](https://github.com/shuayyy/humanoid-amp-ppo/blob/4889389118e0c88d3945dff54d2cd3f992ed815e/assets/supermimic_vs_ppo_lift.mp4) · [实验与详情](docs/community-projects_zh-CN.md#humanoid-mimic--supermimic) · [快速开始](https://github.com/shuayyy/humanoid-amp-ppo/blob/4889389118e0c88d3945dff54d2cd3f992ed815e/README.md#quickstart)


<a id="肌肉驱动交互与诊断"></a>

### 肌肉驱动、交互与诊断 (3)

<a id="muscle-supermimic"></a>
<a id="-muscle-supermimic"></a>

**[Muscle SuperMimic](https://github.com/kaibohex/muscle-supermimic)** · [![33 stars](assets/stars/1434932501.svg)](https://github.com/kaibohex/muscle-supermimic/stargazers) · ⭐ 维护者精选

**技术栈:** mjlab / MuJoCo Warp · **作者:** Kaibo He (kaibohex)<br>
两种肌肉驱动本体，附未见 KIT 动作评估。

[仓库](https://github.com/kaibohex/muscle-supermimic) · [演示](https://github.com/kaibohex/muscle-supermimic) · [实验与详情](docs/community-projects_zh-CN.md#muscle-supermimic) · [安装](https://github.com/kaibohex/muscle-supermimic/blob/b7c7cdd83e82399e057cb9d3f1b76f23ca022c7b/README.md#install)

<a id="supermimic-backflip-diagnostics"></a>

**[SuperMimic Backflip Diagnostics](https://github.com/liudi159/supermimic-backflip-5090)** · [![2 stars](assets/stars/1432819468.svg)](https://github.com/liudi159/supermimic-backflip-5090/stargazers)

**技术栈:** Isaac Lab 3 · **作者:** liudi159<br>
G1 后空翻的对称性、接触与落地诊断。

[仓库](https://github.com/liudi159/supermimic-backflip-5090) · [演示](https://github.com/liudi159/supermimic-backflip-5090/blob/5b313d75e804cdd2ff1ce9bdcfa899a98eca856b/media/v14_blue_checker.mp4) · [实验与详情](docs/community-projects_zh-CN.md#supermimic-backflip-diagnostics) · [结果](https://github.com/liudi159/supermimic-backflip-5090/blob/5b313d75e804cdd2ff1ce9bdcfa899a98eca856b/README.md#结果)

<a id="supermimic-pera"></a>

**[SuperMimic-PERA](https://github.com/shangchaohu718/supermimic-pera)** · [![0 stars](assets/stars/1430576677.svg)](https://github.com/shangchaohu718/supermimic-pera/stargazers)

**技术栈:** UniLab / MuJoCo · **作者:** shangchaohu718<br>
冻结跟踪策略与独立交互实验。

[仓库](https://github.com/shangchaohu718/supermimic-pera) · [演示](https://github.com/shangchaohu718/supermimic-pera/blob/0e89e55187a800341e609129b5d5200a607a467c/README.md) · [实验与详情](docs/community-projects_zh-CN.md#supermimic-pera) · [当前状态](https://github.com/shangchaohu718/supermimic-pera/blob/0e89e55187a800341e609129b5d5200a607a467c/README.md#当前状态)


<a id="框架与训练栈"></a>

### 框架与训练栈 (6)

<a id="holomotion--supermimic"></a>

**[HoloMotion · SuperMimic](https://github.com/HorizonRobotics/HoloMotion)** · [![750 stars](assets/stars/1028843437.svg)](https://github.com/HorizonRobotics/HoloMotion/stargazers)

**技术栈:** MuJoCo Warp / Isaac PhysX / Hydra · **作者:** Horizon Robotics<br>
SuperMimic 与 PPO 共享 HoloMotion 任务和评估。

[仓库](https://github.com/HorizonRobotics/HoloMotion) · [演示](https://github.com/HorizonRobotics/HoloMotion) · [实验与详情](docs/community-projects_zh-CN.md#holomotion--supermimic) · [训练指南](https://github.com/HorizonRobotics/HoloMotion/blob/adaacd50ada6ba9338f6c3f539093f85453e2554/docs/supermimic.md)

<a id="unisupermimic"></a>
<a id="-unisupermimic"></a>

**[UniSuperMimic](https://github.com/Motphys/Uni-SuperMimic)** · [![205 stars](assets/stars/1429498465.svg)](https://github.com/Motphys/Uni-SuperMimic/stargazers) · ⭐ 维护者精选

**技术栈:** UniLab · **作者:** Motphys<br>
含 LAFAN1 与 BONES-SEED 流程的 G1 训练栈。

[仓库](https://github.com/Motphys/Uni-SuperMimic) · [演示](https://github.com/Motphys/Uni-SuperMimic/blob/9bdcbde1f191d88b489309182624a9877e7b6c30/docs/assets/supermimic_comparison.mp4) · [实验与详情](docs/community-projects_zh-CN.md#unisupermimic) · [安装](https://github.com/Motphys/Uni-SuperMimic/blob/9bdcbde1f191d88b489309182624a9877e7b6c30/README.md#installation)

<a id="scalebfm_plus--supermimic"></a>
<a id="-scalebfm_plus--supermimic"></a>

**[ScaleBFM_Plus · SuperMimic](https://github.com/Hxxxz0/ScaleBFM_Plus)** · [![19 stars](assets/stars/1431877986.svg)](https://github.com/Hxxxz0/ScaleBFM_Plus/stargazers) · ⭐ 维护者精选

**技术栈:** Isaac Lab / RSL-RL · **作者:** Hxxxz0, building on ScaleBFM<br>
人形 Transformer 策略集成与留出动作评估。

[仓库](https://github.com/Hxxxz0/ScaleBFM_Plus) · [演示](https://github.com/Hxxxz0/ScaleBFM_Plus/blob/65e4d524bd31fdc4284ba8c6e624fb0b0127da03/ScaleTrack/assets/demos/supermimic_vs_official.gif) · [实验与详情](docs/community-projects_zh-CN.md#scalebfm_plus--supermimic) · [训练与结果](https://github.com/Hxxxz0/ScaleBFM_Plus/blob/65e4d524bd31fdc4284ba8c6e624fb0b0127da03/ScaleTrack/README.md#fast-training-with-a-learned-world-model-supermimic)

<a id="trackerlab-supermimic"></a>

**[TrackerLab SuperMimic](https://github.com/Renforce-Dynamics/trackerlab-supermimic)** · [![13 stars](assets/stars/1430222310.svg)](https://github.com/Renforce-Dynamics/trackerlab-supermimic/stargazers)

**技术栈:** Isaac Lab / PhysX · **作者:** Renforce Dynamics<br>
多本体重定向、训练、评估与导出工具。

[仓库](https://github.com/Renforce-Dynamics/trackerlab-supermimic) · [演示](https://github.com/Renforce-Dynamics/trackerlab-supermimic/blob/29d24524f2f731bf4df75b319c3e76544165849e/docs/media/g1_dance_032000.mp4) · [实验与详情](docs/community-projects_zh-CN.md#trackerlab-supermimic) · [安装](https://github.com/Renforce-Dynamics/trackerlab-supermimic/blob/29d24524f2f731bf4df75b319c3e76544165849e/README.md#install)

<a id="supermimickit"></a>

**[SuperMimicKit](https://github.com/OMEGA-i/SuperMimicKit)** · [![4 stars](assets/stars/1431562951.svg)](https://github.com/OMEGA-i/SuperMimicKit/stargazers)

**技术栈:** MuJoCo Warp / ONNX / WebGPU · **作者:** OMEGA-i<br>
G1 / H2 / A3 重定向与实验性浏览器预览。

[仓库](https://github.com/OMEGA-i/SuperMimicKit) · [演示](https://github.com/OMEGA-i/SuperMimicKit/blob/6697ff8ca53adc9233ded12a7c8777610ca1154d/docs/media/teaser.mp4) · [实验与详情](docs/community-projects_zh-CN.md#supermimickit) · [预览版发布](https://github.com/OMEGA-i/SuperMimicKit/releases/tag/demo-preview-20261024)

<a id="supermimic-lab"></a>

**[SuperMimic Lab](https://github.com/chu-fa/isaaclab-supermimic)** · [![2 stars](assets/stars/1431327517.svg)](https://github.com/chu-fa/isaaclab-supermimic/stargazers)

**技术栈:** Isaac Lab · **作者:** chu-fa<br>
可复用学习器与 runner，附独立 A3 示例。

[仓库](https://github.com/chu-fa/isaaclab-supermimic) · [演示](https://github.com/chu-fa/isaaclab-supermimic) · [实验与详情](docs/community-projects_zh-CN.md#supermimic-lab) · [安装](https://github.com/chu-fa/isaaclab-supermimic/blob/d350e4378c6dc08a3f2a1d35d47b45d83db0e081/docs/SETUP.md)


<a id="机器人移植与重定向"></a>

### 机器人移植与重定向 (6)

<a id="supermimic-mujoco"></a>

**[SuperMimic-MuJoCo](https://github.com/panhainan2020/SuperMimic-MuJoCo)** · [![15 stars](assets/stars/1430957174.svg)](https://github.com/panhainan2020/SuperMimic-MuJoCo/stargazers)

**技术栈:** mjlab / CPU MuJoCo · **作者:** panhainan2020<br>
G1 移植，附留出 100STYLE 评估与推理权重。

[仓库](https://github.com/panhainan2020/SuperMimic-MuJoCo) · [演示](https://github.com/panhainan2020/SuperMimic-MuJoCo/blob/db045afa9c52458f213e2c66037387e9c109a03a/README.md) · [实验与详情](docs/community-projects_zh-CN.md#supermimic-mujoco) · [安装](https://github.com/panhainan2020/SuperMimic-MuJoCo/blob/db045afa9c52458f213e2c66037387e9c109a03a/README.md#环境安装)

<a id="supermimic-retargeted"></a>
<a id="-supermimic-retargeted"></a>

**[SuperMimic Retargeted](https://github.com/tianshuwu/supermimic-retargeted)** · [![9 stars](assets/stars/1430469940.svg)](https://github.com/tianshuwu/supermimic-retargeted/stargazers) · ⭐ 维护者精选

**技术栈:** mjlab / SOMA · **作者:** tianshuwu<br>
G1 / A3 / X2 Ultra 重定向与坐标检查。

[仓库](https://github.com/tianshuwu/supermimic-retargeted) · [演示](https://github.com/tianshuwu/supermimic-retargeted/blob/ff69a0e5305126eb5b80b323bcd815805bc3df4e/media/demo.mp4) · [实验与详情](docs/community-projects_zh-CN.md#supermimic-retargeted) · [快速开始](https://github.com/tianshuwu/supermimic-retargeted/blob/ff69a0e5305126eb5b80b323bcd815805bc3df4e/README.md#快速开始)

<a id="supermimic-wheel-legged-wheelbipe"></a>
<a id="supermimic-轮腿版wheelbipe"></a>

**[SuperMimic Wheel-Legged (wheelbipe)](https://github.com/RadiantForever/supermimic_wheelbipe)** · [![7 stars](assets/stars/1437090261.svg)](https://github.com/RadiantForever/supermimic_wheelbipe/stargazers)

**技术栈:** Isaac Lab / PhysX · **作者:** RadiantForever<br>
面向 wheelbipe 轮足机器人的速度指令学习。

[仓库](https://github.com/RadiantForever/supermimic_wheelbipe) · [演示](https://www.bilibili.com/video/BV1haxM6CEGm/) · [实验与详情](docs/community-projects_zh-CN.md#supermimic-wheel-legged-wheelbipe) · [安装](https://github.com/RadiantForever/supermimic_wheelbipe/blob/0bf3456299a9f754289da58dce6c97c46afd3f03/README.md#setup)

<a id="supermimic-e1"></a>

**[SuperMimic E1](https://github.com/wenconggan/SuperMimic_e1)** · [![5 stars](assets/stars/1430480272.svg)](https://github.com/wenconggan/SuperMimic_e1/stargazers)

**技术栈:** Isaac Lab 3 / MuJoCo · **作者:** wenconggan<br>
DroidUp E1 适配与原生 MuJoCo 跨仿真回放。

[仓库](https://github.com/wenconggan/SuperMimic_e1) · [演示](https://github.com/wenconggan/SuperMimic_e1/blob/d5fbe8f219c438b84633130652c5e6e74beff628/docs/assets/e1_random10_80s.mp4) · [实验与详情](docs/community-projects_zh-CN.md#supermimic-e1) · [安装与资源](https://github.com/wenconggan/SuperMimic_e1/blob/d5fbe8f219c438b84633130652c5e6e74beff628/README.md#安装与资源)

<a id="supermimic-oli"></a>

**[SuperMimic Oli](https://github.com/liuskywalkerjskd/supermimic_oli)** · [![3 stars](assets/stars/1431102076.svg)](https://github.com/liuskywalkerjskd/supermimic_oli/stargazers)

**技术栈:** Isaac Lab 3 · **作者:** liuskywalkerjskd<br>
31 自由度 LimX Oli 移植与完整动作视频导出。

[仓库](https://github.com/liuskywalkerjskd/supermimic_oli) · [演示](https://github.com/liuskywalkerjskd/supermimic_oli/blob/2dc90d90e89fb2e097e985c84c8b99a77708fa5f/results/oli_walk1_subject1_full.mp4) · [实验与详情](docs/community-projects_zh-CN.md#supermimic-oli) · [安装](https://github.com/liuskywalkerjskd/supermimic_oli/blob/2dc90d90e89fb2e097e985c84c8b99a77708fa5f/README.md#setup)

<a id="supermimic-on-apple-m5"></a>

**[SuperMimic on Apple M5](https://github.com/WXyuany/supermimic-m5)** · [![1 stars](assets/stars/1430927278.svg)](https://github.com/WXyuany/supermimic-m5/stargazers)

**技术栈:** MuJoCo / PyTorch MPS · **作者:** WXyuany<br>
Apple Silicon 训练适配与公开 G1 权重。

[仓库](https://github.com/WXyuany/supermimic-m5) · [演示](https://github.com/WXyuany/supermimic-m5/blob/42451591718e1a9a5ec601366997f47c0ad180a3/assets/videos/walk1_subject1.mp4) · [实验与详情](docs/community-projects_zh-CN.md#supermimic-on-apple-m5) · [运行已训练模型](https://github.com/WXyuany/supermimic-m5/blob/42451591718e1a9a5ec601366997f47c0ad180a3/README.md#三步运行已训练模型)


<a id="方法借鉴与探索"></a>

### 方法借鉴与探索 (2)

<a id="flatworld--supermimic-2d"></a>
<a id="-flatworld--supermimic-2d"></a>

**[FlatWorld · SuperMimic-2D](https://github.com/swaggyliu/FlatWorld)** · [![43 stars](assets/stars/1284715083.svg)](https://github.com/swaggyliu/FlatWorld/stargazers) · ⭐ 维护者精选

**技术栈:** FlatWorld / 2D · **作者:** swaggyliu<br>
用二维人形角色演示共享世界模型学习。

[仓库](https://github.com/swaggyliu/FlatWorld) · [演示](https://github.com/swaggyliu/FlatWorld/blob/886dad634c44ed652eea951be62370478f367d8b/docs/media/promo_supermimic.mp4) · [实验与详情](docs/community-projects_zh-CN.md#flatworld--supermimic-2d) · [快速开始](https://github.com/swaggyliu/FlatWorld/blob/886dad634c44ed652eea951be62370478f367d8b/supermimic2d/README.md#quick-start)

<a id="g05--supermimic-style-steering"></a>

**[G0.5 · SuperMimic-style Steering](https://github.com/azizkhadraoui/g05)** · [![0 stars](assets/stars/1425368329.svg)](https://github.com/azizkhadraoui/g05/stargazers)

**技术栈:** G0.5 / LIBERO · **作者:** azizkhadraoui<br>
以世界模型、critic 梯度开展 VLA 引导实验。

[仓库](https://github.com/azizkhadraoui/g05) · [演示](https://github.com/azizkhadraoui/g05/blob/e3de0de50db7d90068483e2d30f2eacd781300b4/README.md) · [实验与详情](docs/community-projects_zh-CN.md#g05--supermimic-style-steering) · [实验代码](https://github.com/azizkhadraoui/g05/blob/e3de0de50db7d90068483e2d30f2eacd781300b4/jobs/119_smsteer.py)

<!-- END GENERATED PROJECTS -->

## 原始 SuperMimic

**[SuperMimic: Scaling Humanoid Whole-Body Control with One Differentiable World Model](https://arxiv.org/abs/2610.28480)** — Qiayuan Liao、Yiyang Shao、Junfeng Long、Kevin Zakka、Roberto Horowitz、Pieter Abbeel、Koushil Sreenath。**UC Berkeley · CoRL 2026 Oral。**

原始方法学习共享动力学模型，通过短时想象轨迹改进动作跟踪策略。[论文](https://arxiv.org/abs/2610.28480) · [官网](https://supermimic.github.io/) · [交互演示](https://supermimic.github.io/demo/) · [方法、作者报告结果与完整官方演示](docs/original-supermimic_zh-CN.md)。

<p align="center"><a href="https://supermimic.github.io/media/real/real_bay-wide.mp4"><img src="assets/official/real-g1-wide.gif" width="480" alt="SuperMimic 官方 G1 真机演示"></a><br><sub>原作者演示 · <a href="assets/official/README.md">媒体来源</a></sub></p>

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

<a id="ref2dex--dex-contact-mbrl"></a>

[归档条目](docs/archived-projects.md#中文)保留当前无法公开访问仓库的历史记录。

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

## Star History

<p align="center"><b>如果这份清单对你有帮助，欢迎<a href="https://github.com/miao-org/awesome-supermimic">点个 Star</a>，让更多人发现它。</b></p>

<p align="center">
  <a href="https://star-history.com/#miao-org/awesome-supermimic&Date">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=miao-org/awesome-supermimic&type=Date&theme=dark">
      <img src="https://api.star-history.com/svg?repos=miao-org/awesome-supermimic&type=Date" alt="Star history chart for miao-org/awesome-supermimic" width="100%">
    </picture>
  </a>
</p>
