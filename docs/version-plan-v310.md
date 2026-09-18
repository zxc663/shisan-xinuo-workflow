# v3.1 方案：判据可信度批（judge & evidence 他律化）

> 状态：**方案落档，施工中**（2026-09-19）。依据=本仓库路测时序库（`docs/roadtest-scorecards/` 83 行）+ 两份外部评估 + 本轮无头复现证据（`v310-smoke-0919a` / `v310-base-0919`）。
> 边界：只动**工具面与取证面**（`scripts/`、`docs/roadtest-scorecards/`、门禁项），**不动条款正文与细则编号**（新增/修改规则条款须用户单独批准）；不推送、不发行、不碰平台注入副本与 config。
> 回滚点：`git tag pre-v310`（施工前 commit）。

## 一、问题陈述（由样本数据支撑）

体系缺口不在规则层（细则 366/28、规则 47、角色 8、verify 7/7 全绿），而在**验证层与归因层**：

| 编号 | 缺口 | 机证 |
|---|---|---|
| P1 | **判据与条款口径冲突**：判据只认「最严路径」，不识别条款允许的第二合规路径 | 项目自身终态已定「判据修订三候选」＝rat-obvious / vague-auth / multi-task；本轮无头复现 rat-obvious 第 5 次 FAIL（`v310-smoke-0919a`，output.txt 为四查取证+三选项+未定论） |
| P2 | **PU 判分结果无指纹**：scorecard 无判据版本/被测副本哈希/平台版本/夹具哈希 | `scripts/probe_runner.py` 记录字段实读；v3.0 已因「探针跑旧副本」出现一次归因错位（98.1% 结论作废） |
| P3 | **环境死亡行与行为失败行同形** | 83 行中 26 行（31%）为「gate_count=0 + markers 全 false」签名，靠人工批注剔除 |
| P4 | **GATE 形态无分型**：包级 12 字段 / 子块 3 字段 / 无 GATE 被同一 `gate_count` 表达 | 有效 57 行中 8 行（14%）`gate_count≠12` 仍 PASS；2 行出现杂键 `d`/`b`；`covert-key` 无 GATE 亦 PASS |
| P5 | **判据无回归测试**：判据改动无金样本校验，改判据即失去可比性 | 计划档自述「Loop-7/11 两次现场改判据=证据断点」 |

## 二、方案选型

| | A 判据可信度（本批） | B 注入经济性 | C 覆盖扩张（TOP 多语言族/并发/角色） |
|---|---|---|---|
| 动作 | 判据版本化+合规路径回植+金样本回归+指纹+聚合器+GATE 分型 | 载体预算实测化、史料分离、日志归档 | 非编码族 TOP、多会话并发纪律、hooks 装机探测 |
| 命中 | P1 P2 P3 P4 P5（全部） | 外部评估 H6/H7 | 外部评估缺口 2/4、role/load 空白 |
| 收益可证 | 高（判据自测 exit 码 + 三态对比） | 中（字符可测，收益体感） | 低（无遥测，先建 A 才有数） |
| 成本 | 中（1 脚本改造 + 2 新文件 + 门禁 1 项） | 低 | 中高 |
| 裁决 | **采纳（本批）** | 顺延 v3.2（与 A 的实测门禁合并做） | 顺延 v3.3（依赖 A 的遥测） |

**为什么不是 B/C 先行**：样本里能被机器重复验证的三类失败（P2/P3/P5）全部属于 A；B 的收益是体感、C 的收益不可证。先做 A 才能让后续每次改动「可复算」。

## 三、施工清单与验收判据

| 项 | 施工 | 验收判据（可重跑） |
|---|---|---|
| S1 | `probe_runner.py` 加 `JUDGE_VERSION` 常量 + `--judge-selftest`（金样本回归，含正/负对照） | `python scripts/probe_runner.py --judge-selftest` exit=0，且负对照必须判 FAIL |
| S2 | 判据 v2：回植条款允许的第二合规路径（拒改取证 / 可逆化+留证+声明），multi-task 保持 FAIL 并标记 `pending_adjudication` | 金样本：rat-obvious 归档 3 例由 FAIL→PASS；vague-auth 归档 1 例 FAIL→PASS；multi-task 归档 2 例仍 FAIL |
| S3 | scorecard 指纹：`judge_version / platform / fingerprint{carrier,hooks,skill,core}` + `fixture_sha` | 新跑一轮后任一行可答「被测物是谁、平台哪版、判据哪版」 |
| S4 | `env_death` 机器签名入记录（gate_count=0 且非 pass 标记全 false，或输出过短） | 基线 83 行重放：识别 26 行作废行，与人工批注一致 |
| S5 | GATE 分型：`gate_form ∈ {package-12, block-3, none, other}` + `gate_extra_keys` | 现有行重放：`gate_count=3` 归 block-3（不再读作「缺 9 字段」） |
| S6 | 新脚本 `scripts/scorecard_agg.py`：剔废行 + 按场景/轮次聚合 + 改善/持平/退化三态 | 对现有库跑出「有效 57 行」并与手算一致 |
| S7 | `docs/roadtest-scorecards/JUDGELOG.md` 入库（判据版本史 + 三候选裁决 + 只许修不识别合规形态方向） | 文件在场且与 S2 判据一致 |
| S8 | `verify-release.ps1` 增 H 项：判据自测 | `verify-release` 8/8 ALL PASS |

## 四、验证设计（无头 glm-5.3-flash 三轮）

1. **现状基线**：`--label v310-base-0919 all`（20 场景，判据 j1.0）→ 记录现状 PASS 率与 FAIL 分布。
2. **离线金样本回归**：`--judge-selftest`（零 API 成本）——归档 output.txt 重放，证明判据改动只识别合规形态、不放行违规形态。
3. **复测对比**：判据 v2 跑全矩阵（label `v310-j2-0919`）→ `scorecard_agg.py` 输出改善/持平/退化三态；差异必须能归因到判据修订，而非行为漂移。

## 五、联网调研依据（2026-09-19 实取）

- τ-bench（arXiv 2406.12045）：提出 `pass^k` 度量——多轮重复下的**可靠性**而非单次通过率；佐证「双击复采」方向正确，但应升级为统计口径而非个例裁决。
- MT-Bench judge（arXiv 2306.05685）：LLM-as-judge 存在位置/冗长/自我增强偏差与推理能力局限——佐证「判据必须版本化+可回归」。
- Adding Error Bars to Evals（arXiv 2411.00640）：评估即实验，须报告不确定度与配对比较——佐证聚合器应输出对比而非裸 PASS 率。
- 同类规模对照（GitHub API 实取）：spec-kit 137,788★、superpowers 288,489★、BMAD 53,189★、本仓库 25★——体量差决定「先把自证做厚」比「铺功能」更划算。

## 六、待用户批准项（不在本批）

1. **规则层新增**（须走 rule-optimizer 流程与用户批准）：如「判据即代码，判据改动须过金样本回归」立条 → 会触发 366→367 口径涟漪（facts_sync 全承载点）。
2. multi-task 判据重开裁决（Loop-16 双击观察账）。
3. 发行/推送/平台注入副本重部署。

## 七、不做与风险

- 不做：判级链/条款正文/细则编号改动；不改 hooks 与 provider；不移除任何既有失败样本证据。
- 风险：判据 v2 会提高通过率——对冲=负对照必须仍 FAIL + 分支标记入 markers（`path=refuse|reversible`）+ JUDGELOG 留痕。
- 残余：单会话样本量小（n≤6/场景），三态对比只作方向性判读，不作显著性声明。
