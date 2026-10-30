# Jev curation / Jev 四维评分

Rank projects by **innovation, reproduction affordability, training time efficiency and framework completeness**, with **25% weight each**. The global Top 10 and within-category ordering use this composite. ⭐ remains a separate Jev recommendation decision; GitHub Stars are display metadata only.

按**创新性、复现成本、训练耗时、框架完整性**四个维度评分，**各占 25%**。总榜前十和分类内部使用同一个综合分；⭐ 由 Jev 单独判断。GitHub Star 数不参与评分。

## What each score means / 四项分别看什么

All dimension scores run from 0 to 100; **higher is better**. For cost and time, higher means more affordable reproduction and stronger evidence of useful time efficiency, not more money or more hours.

分项均为 0–100 分，**越高越好**；复现成本分高表示门槛低，训练耗时分高表示达到有效结果的时间效率证据更强，不表示花钱更多、训练更久。

| Dimension / 维度 | What matters / 判断依据 | What does not suffice / 不能直接当作优势 |
| --- | --- | --- |
| Innovation / 创新性 | Mechanisms, new capabilities and supported diagnostic insights relative to original SuperMimic / 相对原方法增加的机制、能力与有证据的诊断发现 | A renamed repository, new framework name or larger model alone / 只换名字、框架或增大模型 |
| Reproduction affordability / 复现成本 | GPU count/class/VRAM, data access, dependencies, setup and required physical hardware / 显卡与显存、数据获取、依赖、安装及真机要求 | Released inference weights do not establish cheap retraining / 有推理权重不等于低成本重训 |
| Training time efficiency / 训练耗时 | Elapsed time to an attained result, interpreted with hardware, task/data scale and evaluation conditions / 结合硬件、任务规模、效果和评测口径看训练时间 | Iterations, inference FPS and short clips are not training time; a small task is not automatically efficient / 迭代数、推理帧率和片段时长不算训练耗时，小任务也不自动得高分 |
| Framework completeness / 框架完整性 | Installation, data/assets, training, evaluation, configurations, artifacts and visualization/export for the stated scope / 在所声称范围内，安装、数据、训练、评测、配置、产物与展示/导出是否完整 | A large parent framework or planned backend is not a completed integration / 上游框架大、后端列得多，不等于已经接通验证 |

A focused project can have a complete framework. Innovation here is contribution distinctiveness relative to the original method, not a literature-wide novelty certification. Results from different tasks and machines do not become a speed benchmark by combining these scores.

单一任务也可以拥有完整流程。创新性衡量相对原方法的贡献特色，不是全领域首创认证。四项汇总后仍是项目选择参考，不是不同任务、不同机器间的训练速度排行榜。

## Missing evidence and arithmetic / 缺失信息与计算

Availability is checked against exact excerpts in the frozen summaries **before consuming the numeric scores**. Every profile describes a contribution and implementation scope, allowing innovation and completeness to be assessed, including incomplete prototypes. Cost needs a concrete hardware, data-access or setup/artifact-access fact. Time needs an explicit training duration linked to an attained outcome. Partial resource information permits a cautious cost score; it does not imply that GPU, VRAM, money and setup effort are all known.

先依据冻结简介中的原文摘录核对信息是否足够，再使用 Jev 的分数。所有条目都描述了贡献和实现范围，因此可评价创新性和完整性，包括尚不完整的原型。成本项至少需要明确的硬件、数据获取或安装/产物获取条件；耗时项需要训练时间与结果对应。部分资源信息可以支持谨慎评分，但不代表显卡、显存、金钱和配置工时全部已知。

**Composite = 25% × innovation + 25% × affordability + 25% × time efficiency + 25% × completeness.** Each available dimension equals the API Score × 25. N/A contributes zero to this fixed-denominator, evidence-supported total; it does not mean the project is poor, expensive or slow. We do not rescale the remaining dimensions to 100%. Missing evidence can lower rank, so the full table shows coverage. N/A means insufficient in the supplied summary, not necessarily absent from the repository.

**综合分 = 创新性 × 25% + 复现成本 × 25% + 训练耗时 × 25% + 框架完整性 × 25%。** 可评分项使用 API Score × 25。N/A 在固定权重的「证据支持总分」中不贡献分数，不代表项目差、昂贵或缓慢；也不把剩余权重重新放大到 100%。缺失信息可能降低排名，所以完整表同时展示覆盖度。N/A 只表示此次简介不足，不等于仓库一定没写。

Sorting uses the unrounded composite, with case-insensitive owner/repository as the exact-tie breaker. Displayed scores have one decimal; close scores should not be treated as meaningful differences. ⭐ uses the unchanged independent Jev Choice, considering strengths and tradeoffs in these same four dimensions, with no quota or score threshold.

排序使用未舍入的综合分，同分按 owner/repository 排序，展示保留一位小数；相近分数不宜理解为显著差距。⭐ 原样采用 Jev 的独立 Choice，综合考虑这四方面的优势和取舍，不设名额或分数门槛。

## Snapshot / 本次快照

- **2026-10-30 · TypeSafe `jev-1.14.0` · 38 projects / 项目。**
- **38 actual API calls:** four dimension Scores, one independent recommendation Choice and four auxiliary availability Choices per call. / 实际调用 38 次，每次含四项评分、独立推荐判断和四个辅助信息存在性判断。
- **29 ⭐ recommendations; 10 overview entries. / 29 个推荐项目，前表展示 10 个。**
- Reuse the same 38 frozen, source-linked profiles as the preceding run; this changes criteria, not the upstream revision cutoff. InstinctMJ is at `03563ee`; the previous freshness audit covered the other 37 pinned heads. / 复用上一轮已核查的 38 份证据简介，本轮更新评价维度，不宣称重新刷新了上游版本。
- Project owner/title/URL, GitHub Stars and earlier rankings/marks are not sent as metadata. Dependency names in the prose remain; this is not complete anonymization. / 不发送仓库元数据、Star 或旧排名；正文自然出现的依赖名称仍保留，并非完全匿名。
- **API-reported usage / API 返回用量:** 88,759 input tokens, 9,209 output tokens.

The auxiliary availability Choices failed a factual QA check: for example, allmimic's explicit 0.83-hour result was missed. They are therefore **retained for audit but not used**. All 38 profiles received the same excerpt-based availability review. The four numeric Scores and recommendation Choice were not edited or rerun; only deterministic aggregation uses the reviewed evidence flags. Both the initial model-gated aggregation and final results are retained.

辅助的信息存在性判断未通过事实检查，例如漏读了 allmimic 明示的 0.83 小时，因此**只保留备查、不参与计算**。全部 38 个条目均按同一规则做了原文依据核对；四项数值评分和推荐判断没有改写或重跑，计算仅改用经核对的可评分标记。最初的模型门控汇总和最终汇总都保留。

## Full score breakdown / 全量分项

Each dimension is out of 100. Click a project for its pinned source. N/A = insufficient summary evidence; coverage counts assessed dimensions, not benchmark completeness.

每个分项满分 100，项目链接指向核查时的上游版本；N/A 表示简介证据不足，覆盖度是可评分维度数量，不是实验完成比例。

| # | Project / 项目 | Innovation / 创新 | Affordability / 成本 | Time / 耗时 | Completeness / 完整性 | Total / 综合 | Coverage / 覆盖 |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | ⭐ [SuperMimic Mjlab](https://github.com/Breezewrf/supermimic_mjlab/blob/a7cee74636a4c596cd8710f8c2e51f82d78bb150/README.md) | 70.0 | 42.5 | 66.0 | 88.2 | **66.7** | 4/4 |
| 2 | ⭐ [In-Hand Rotation mjlab](https://github.com/Msornerrrr/in-hand-rotation-mjlab/blob/0ab03eb2244b4a1a020d94ef38a4823bb9e15ba0/README.md) | 37.0 | 49.5 | 84.2 | 54.0 | **56.2** | 4/4 |
| 3 | ⭐ [InstantTrack](https://github.com/Huy-Quang-Dao/instantTrack/blob/a33691a08bca8802d9d2985f62e2567479735a8e/README.md) | 46.8 | 49.5 | 77.2 | 38.0 | **52.9** | 4/4 |
| 4 | ⭐ [SuperMimic for Robot Manipulation](https://github.com/emoPointer/supermimic_manipulation/blob/810e5768c50117d2fec75f20f9e643a11cd0882b/README.md) | 35.8 | 56.8 | 60.5 | 55.5 | **52.1** | 4/4 |
| 5 | ⭐ [InstinctMJ · SuperMimic](https://github.com/project-instinct/InstinctMJ/blob/03563ee02665f327425106372264070315673748/src/instinct_mj/rl/supermimic/README.md) | 61.3 | 55.2 | 48.2 | 41.8 | **51.6** | 4/4 |
| 6 | ⭐ [supermimic_vibe](https://github.com/dhmbb2/supermimic_vibe/blob/d0934d069207ee745be8489d9631a8314c94c1f3/README.md) | 53.5 | 42.2 | 54.5 | 50.5 | **50.2** | 4/4 |
| 7 | ⭐ [SuperMimic-Reproduced](https://github.com/CuboiLeo/SuperMimic-Reproduced/blob/ba6105349069bf040f1fdad60873d13138d505a2/README.md) | 38.5 | 27.3 | 53.5 | 76.0 | **48.8** | 4/4 |
| 8 | ⭐ [UniSuperMimic](https://github.com/Motphys/Uni-SuperMimic/blob/05a9772ca09509c50a4cc3fe96f9d6b3c180f3d2/README.md) | 30.8 | 47.5 | 48.0 | 62.5 | **47.2** | 4/4 |
| 9 | ⭐ [supermimic_vibed](https://github.com/zita-ch/supermimic_vibed/blob/8bfc1158bd968f729fcc65d5e897a05b05ea3d36/README.md) | 22.0 | 46.2 | 51.0 | 68.5 | **46.9** | 4/4 |
| 10 | ⭐ [Muscle SuperMimic](https://github.com/kaibohex/muscle-supermimic/blob/932ac22ca720b1c4db40c4323a3b67bf3c1eaa99/README.md) | 45.0 | 41.0 | 55.2 | 40.8 | **45.5** | 4/4 |
| 11 | ⭐ [allmimic](https://github.com/Shimingyi/allmimic/blob/cb334ff674b2f57248f33f8c21b7fb526fbdf8cc/README.md) | 37.8 | 49.8 | 44.5 | 38.2 | **42.6** | 4/4 |
| 12 | ⭐ [SuperMimic on RTX 5080](https://github.com/rzc156/supermimic-rtx5080/blob/df967c61c29a2ed9ba6b188e1607ba59225fe8a7/README.md) | 26.0 | 53.0 | 47.5 | 43.5 | **42.5** | 4/4 |
| 13 | ⭐ [SuperMimic Parkour](https://github.com/yhx1203/supermimic_parkour/blob/f398519453a25b3f10722626b7356266d8b7f875/README.md) | 31.5 | 39.0 | 44.2 | 42.0 | **39.2** | 4/4 |
| 14 | ⭐ [SuperMimic Oli](https://github.com/liuskywalkerjskd/supermimic_oli/blob/2dc90d90e89fb2e097e985c84c8b99a77708fa5f/README.md) | 26.0 | 47.8 | 36.8 | 41.8 | **38.1** | 4/4 |
| 15 | [SuperMimic Wheel-Legged (wheelbipe)](https://github.com/RadiantForever/supermimic_wheelbipe/blob/0bf3456299a9f754289da58dce6c97c46afd3f03/README.md) | 29.2 | 44.5 | 36.2 | 41.2 | **37.8** | 4/4 |
| 16 | ⭐ [ScaleBFM_Plus · SuperMimic](https://github.com/Hxxxz0/ScaleBFM_Plus/blob/65e4d524bd31fdc4284ba8c6e624fb0b0127da03/ScaleTrack/README.md) | 26.8 | 27.0 | 46.5 | 50.2 | **37.6** | 4/4 |
| 17 | ⭐ [HoloMotion · SuperMimic](https://github.com/HorizonRobotics/HoloMotion/blob/f52dd81ae935a828b0296f5ee0f833beb7378bf0/docs/supermimic.md) | 16.8 | 42.5 | 37.5 | 42.8 | **34.9** | 4/4 |
| 18 | ⭐ [SuperMimic on Apple M5](https://github.com/WXyuany/supermimic-m5/blob/42451591718e1a9a5ec601366997f47c0ad180a3/README.md) | 21.8 | 59.5 | N/A | 48.2 | **32.4** | 3/4 |
| 19 | ⭐ [Go2-SuperMimic](https://github.com/Zhengtianjin/go2-supermimic/blob/d9eee9b3f248e5300e636c433255db2c1c3e086a/README.md) | 26.5 | 50.7 | N/A | 49.8 | **31.8** | 3/4 |
| 20 | ⭐ [SuperMimic-MuJoCo](https://github.com/panhainan2020/SuperMimic-MuJoCo/blob/db045afa9c52458f213e2c66037387e9c109a03a/README.md) | 27.3 | 42.8 | N/A | 50.2 | **30.1** | 3/4 |
| 21 | ⭐ [Dex SuperMimic](https://github.com/CumulusAlpha/Dex-Supermimic/blob/3a7c1a33fd8e5c6cc047e381ea9309da96553c27/README.md) | 23.8 | 50.5 | N/A | 41.0 | **28.8** | 3/4 |
| 22 | [SuperMimic Retargeted](https://github.com/tianshuwu/supermimic-retargeted/blob/ff69a0e5305126eb5b80b323bcd815805bc3df4e/README.md) | 34.8 | 34.2 | N/A | 40.5 | **27.4** | 3/4 |
| 23 | [SuperMimic Backflip Diagnostics](https://github.com/liudi159/supermimic-backflip-5090/blob/5b313d75e804cdd2ff1ce9bdcfa899a98eca856b/README.md) | 28.0 | 46.2 | N/A | 34.0 | **27.1** | 3/4 |
| 24 | [Standing MBRL vs PPO](https://github.com/JackMin7/supermimic_whole_body_tracking/blob/553a7d32dc5fc00cbe6de5ee46479af2fcceeda8/README.md) | 32.0 | N/A | 46.8 | 29.2 | **27.0** | 3/4 |
| 25 | ⭐ [SuperMimic Lab](https://github.com/chu-fa/isaaclab-supermimic/blob/d350e4378c6dc08a3f2a1d35d47b45d83db0e081/README.md) | 20.0 | 48.5 | N/A | 37.8 | **26.6** | 3/4 |
| 26 | ⭐ [MorphMimic](https://github.com/lzyang2000/morphmimic/blob/770394b4a0cad9effbf807a6c03435d1699733d0/README.md) | 44.5 | 16.8 | N/A | 43.0 | **26.1** | 3/4 |
| 27 | ⭐ [SuperMimic G1 Deployment](https://github.com/KyrieYoung926/supermimic_deploy/blob/7e63e3bbd5150d55afbdece28278781800f3ed21/README.md) | 15.8 | 33.0 | N/A | 55.0 | **25.9** | 3/4 |
| 28 | [SuperMimicKit](https://github.com/OMEGA-i/SuperMimicKit/blob/6697ff8ca53adc9233ded12a7c8777610ca1154d/README.md) | 33.8 | 26.0 | N/A | 44.0 | **25.9** | 3/4 |
| 29 | ⭐ [Rethinking SuperMimic](https://github.com/btx0424/rethinking-supermimic/blob/2cbbd1278bfb8bd59c31fe48d7413c46ae205e32/README.md) | 48.8 | N/A | N/A | 52.2 | **25.2** | 2/4 |
| 30 | ⭐ [SuperMimic-Repro-Sim2Real](https://github.com/NJU-R-L-Group-Embodied-Lab/SuperMimic-Repro-Sim2Real/blob/f8f60d7bbdba68468c050ef100af02d752ca238e/README.md) | 39.0 | 10.5 | N/A | 45.2 | **23.7** | 3/4 |
| 31 | ⭐ [SuperMimic on LocoMuJoCo](https://github.com/Alchedata/supermimic-locomujoco/blob/de9f39191b9e8b87ff1afd2b0129dd93d4795e8c/README.md) | 58.0 | N/A | N/A | 34.2 | **23.1** | 2/4 |
| 32 | ⭐ [TrackerLab SuperMimic](https://github.com/Renforce-Dynamics/trackerlab-supermimic/blob/813f37a89d9be0791c9c72695a322307001a5d11/README.md) | 30.0 | N/A | N/A | 59.0 | **22.2** | 2/4 |
| 33 | [SuperMimic-perceptive](https://github.com/mode1223345/SuperMimic-perceptive/blob/3d38bacbaf5bee7e782bdada6a6da678264d0bfa/README.md) | 37.0 | N/A | N/A | 43.5 | **20.1** | 2/4 |
| 34 | ⭐ [SuperMimic E1](https://github.com/wenconggan/SuperMimic_e1/blob/d5fbe8f219c438b84633130652c5e6e74beff628/README.md) | 25.5 | N/A | N/A | 48.0 | **18.4** | 2/4 |
| 35 | ⭐ [Humanoid Mimic · SuperMimic](https://github.com/shuayyy/humanoid-amp-ppo/blob/681874bab20273ba9211cb92d5ff108900ce3490/README.md) | 20.2 | N/A | N/A | 44.8 | **16.2** | 2/4 |
| 36 | [FlatWorld · SuperMimic-2D](https://github.com/swaggyliu/FlatWorld/blob/601d96c3aa69b5b226533f767d1c2e6f917c5a5d/supermimic2d/README.md) | 24.2 | N/A | N/A | 40.0 | **16.1** | 2/4 |
| 37 | [SuperMimic-PERA](https://github.com/shangchaohu718/supermimic-pera/blob/0e89e55187a800341e609129b5d5200a607a467c/README.md) | 32.5 | N/A | N/A | 25.5 | **14.5** | 2/4 |
| 38 | [G0.5 · SuperMimic-style Steering](https://github.com/azizkhadraoui/g05/blob/e3de0de50db7d90068483e2d30f2eacd781300b4/jobs/119_smsteer.py) | 30.2 | N/A | N/A | 25.0 | **13.8** | 2/4 |

## Records and limits / 记录与边界

- [Frozen source-linked summaries / 冻结证据简介](2026-10-30-four-dimensions/inputs.json)
- [Current four-dimension rules and aggregation / 当前规则与汇总方式](2026-10-30-four-dimensions/rubric.json)
- [Exact source excerpts supporting availability / 可评分标记的原文依据](2026-10-30-four-dimensions/evidence-availability.json)
- [All exact API requests and unchanged responses / 全部实际请求与未改动的返回](2026-10-30-four-dimensions/run.json)
- [Final four-dimensional scores and ranking / 最终四维评分与排名](2026-10-30-four-dimensions/results.json)
- [Original API question specification / 实际调用时的问题规范](2026-10-30-four-dimensions/request-rubric.json)
- [Superseded availability-gate aggregation, for QA audit only / 已弃用的模型门控汇总，仅用于检查追溯](2026-10-30-four-dimensions/model-gated-results.json)

The [previous single-priority-score snapshot](2026-10-30/results.json) is retained as history; its values are not comparable with this four-dimension composite.

[上一轮单项优先级快照](2026-10-30/results.json)保留作历史记录，数值不能与本次四维综合分直接比较。

Jev evaluates prepared summaries, not an independent reading of every repository or a rerun of experiments. Summary coverage and wording affect scores. This single inference snapshot has not been calibrated as a robotics benchmark; confidence measures output-distribution concentration, not factual correctness. The quantitative Top 10 highlights are source-grounded editorial summaries, not Jev-generated prose.

Jev 评估整理后的简介，没有独立通读全部仓库或重跑实验。简介覆盖度和措辞会影响结果；本次单轮推理未经过机器人基准校准。confidence 表示输出分布集中程度，不代表事实正确率。Top 10 的量化亮点根据来源整理，不是 Jev 生成的文字。

When evidence or dimension definitions change, freeze a new complete snapshot and review all entries consistently. Changing only weights can reuse the raw dimension Scores. Preserve actual responses and prior snapshots; never selectively rerun for preferred winners or substitute invented judgments.

证据或维度定义变化时，建立完整新快照并对全部条目一致处理；仅调整权重可以复用分项原始分数。保留实际返回和旧快照，不为偏好名次选择性重跑，也不编造评分。

API semantics: [Score](https://docs.typesafe.ai/primitives/score), [Choice](https://docs.typesafe.ai/primitives/choice), [models](https://docs.typesafe.ai/models).
