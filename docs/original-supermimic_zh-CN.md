[← Awesome SuperMimic](../README_zh-CN.md)

## 原始 SuperMimic

**[SuperMimic: Scaling Humanoid Whole-Body Control with One Differentiable World Model](https://arxiv.org/abs/2610.28480)**<br>
Qiayuan Liao、Yiyang Shao、Junfeng Long、Kevin Zakka、Roberto Horowitz、Pieter Abbeel、Koushil Sreenath。<br>
**UC Berkeley · CoRL 2026 Oral**

[论文](https://arxiv.org/abs/2610.28480) · [PDF](https://arxiv.org/pdf/2610.28480) · [项目主页](https://supermimic.github.io/) · [官方视频](https://supermimic.github.io/media/real/film-1080.mp4) · [浏览器演示](https://supermimic.github.io/demo/)

SuperMimic 从仿真状态转移中学习一个共享的可微世界模型，再通过短时想象轨迹训练动作跟踪策略。世界模型和策略在同一个循环中持续更新，策略梯度经过学习到的模型。[方法介绍](https://supermimic.github.io/#loop)。

<p align="center">
  <a href="https://arxiv.org/pdf/2610.28480v1#page=4">
    <img src="../assets/official/training-loop.png" width="100%" alt="SuperMimic 原论文图 2：数据采集、世界模型拟合与策略改进共享回放缓冲区，虚线表示梯度路径">
  </a>
</p>
<p align="center">
  <sub>原论文 Figure 2 · <a href="https://arxiv.org/pdf/2610.28480v1#page=4">算法框架，第 4 页</a> · <a href="https://arxiv.org/pdf/2610.28480v1#page=15">完整伪代码 Algorithm A.1，第 15 页</a></sub>
</p>

世界模型使用 **8 步回放窗口**拟合，策略和 critic 通过 **32 步想象轨迹**学习。更新策略时，世界模型的权重固定，但梯度仍经过模型传回策略。图中蓝色虚线表示梯度，❄️ 表示该阶段权重冻结，🔥 表示该阶段权重参与训练。

作者报告：**单张 H100 训练 3 小时**超过 SONIC 已发布 checkpoint 的回报，**129,514 个动作中失败 25 个**；两张 H100 训练 9.8 小时后失败数为 0。这是训练动作覆盖结果，且两者训练硬件与数据规模不同。[原始结果与计算量口径](https://supermimic.github.io/#compute)。

**官方代码状态（2026-10-28 核查）：**官方主页提供论文、视频和浏览器演示，尚未链接训练代码仓库。下列条目均为社区实现或扩展。

<p align="center">
  <a href="https://supermimic.github.io/media/world-model/wm_on.mp4"><img src="../assets/official/world-model.gif" alt="SuperMimic 官方世界模型演示：蓝色预测轨迹叠加在仿真动作上" width="100%"></a><br>
  <b>世界模型预测</b>
</p>

<table>
  <tr>
    <td width="50%" align="center">
      <a href="https://supermimic.github.io/media/hero/hero_montage_desktop.mp4"><img src="../assets/official/simulation-wide.gif" alt="SuperMimic 官方仿真演示：G1 翻转、侧滚与舞蹈" width="100%"></a><br>
      <b>仿真全身动作</b>
    </td>
    <td width="50%" align="center">
      <a href="https://supermimic.github.io/media/real/real_bay-wide.mp4"><img src="../assets/official/real-g1-wide.gif" alt="SuperMimic 官方真机演示：G1 在海湾边完成侧滚与翻转" width="100%"></a><br>
      <b>G1 真机演示</b>
    </td>
  </tr>
</table>

<p align="center"><sub>原作影像：<a href="https://supermimic.github.io/">SuperMimic 作者</a> · 点击预览观看原视频 · <a href="../assets/official/README.md">素材来源</a></sub></p>

建议先了解原始工作，再按框架和任务选择实现。本仓库由社区维护，各收录项目的贡献归属于其作者。
