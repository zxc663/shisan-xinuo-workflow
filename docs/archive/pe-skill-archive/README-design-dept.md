# product-engineering-skill · 产品工程 Skill（设计部）

> 十三希诺工作流家族第四包 `shisan-xinuo-product` 的**设计源（设计部）**：问题定义、方向档、八份调研蒸馏、可判定门禁与实证；包本体随家族主仓分发——[shisan-xinuo-workflow](https://github.com/zxc663/shisan-xinuo-workflow)（`skill/shisan-xinuo-product/`，包版本 **0.2.6**，本批联动发行）。
> 冷启动先读：[docs/one-page-definition.md](docs/one-page-definition.md)——一页说完「是什么 / 不是什么 / 哪里还不牢」（简明版规范，术语消歧也在里面）。
> 两仓分工一句话：**主仓管纪律面（拦「不该发生的动作」），本包管产品面（拦「不该缺失的能力」）**——共同目标是让 AI 的产出可判定、可复算。

## 怎么获取与安装

- **随家族一次装齐**（推荐）：`git clone https://github.com/zxc663/shisan-xinuo-workflow` → `pwsh scripts/install-skill.ps1 -Family`（核心 + 流程 + 角色 + 产品工程，四包）。
- **skills 市场**：`npx skills add zxc663/shisan-xinuo-workflow`（装到平台技能目录后按需加载本包）。
- **用本仓 Release**：从本仓 Releases 下载 `shisan-xinuo-product-v0.2.6.zip`，解压后将 `shisan-xinuo-product/` 放入平台技能目录。
- **与核心联动**：核心包已埋条件式挂接钩子（skill-usage §8）——本包在场则三缝合点自动生效（计划检索位 / GATE 门禁真值 / 收尾账本写回）；不在场则跳过并声明。分合都可用。

---

## 产品工程究竟解决什么问题，这个问题从何而来？

### 一句话

产品工程解决的问题是：当 AI 承担产品实现时，「已做的是否没错」和「该有的是否都有」之间出现了一个**判据无人区**，缺失逻辑恰好落在那里——而缺失是不可观测的偏差。

### 一、问题从何而来：两层来源

**经验层（导火索）**：财务项目复盘 + 工作流「Skill 前置」条，暴露出四个症状——

1. 成熟共识不用（重复造轮子）
2. 上游组件库闲置（另造轮子）
3. 反人类交互（甩 JSON、无出路）
4. 假理想功能（按钮没接事件、死代码、空 catch）

**结构层（真问题，在一个由 AI agent 长期持续开发的项目中）**：上面四个症状统一起来，指向一个更冷的事实——**模型与产品的成本结构，逐项镜像颠倒**。

| | 对当前模型 | 对产品未来 |
|---|---|---|
| 写新 | 便宜 | 最贵 |
| 复用 | 贵 | 最便宜 |
| 验证 | 贵 | 唯一真实 |
| 信任 | 0 | 一切 |

这不是「AI 不够聪明」，是结构性错配：每次会话的模型都是失忆的、只做局部最优的工人。它的最优路径，系统性地就是产品的最昂贵路径。

而这个错配只在 AI 接管实现之后才出现。人做实现时，兑现义务由人自己扛着，成本结构不颠倒。所以问题不是从「AI 不会想产品」来——产品决策侧不归它管；问题是从「**产品已决定，但 AI 把它做歪了**」来。

### 二、问题究竟是什么：三层收敛

**症状层**：产品 = 承诺的集合。四个症状统一为承诺的——不兑现 / 反直觉 / 冲突 / 无知。

**机制层**：兑现义务的履行时点错了。承诺是在产品被生成时欠下的，但兑现被留到了交互时——那时模型早已离场，没人兜底。所以 Skill 的本质是：**把兑现义务从交互时前移到生成时**。

**结构层（真正的病灶）**：

- 产品判据是正向完备：该有的都有
- 工程判据是负向无错：已做的没错
- 缺失逻辑两头都管不着

而缺陷三级成本阶梯是：bug → 逻辑错 → 缺失逻辑。最后一级最贵，恰恰因为——**错误是可观测的偏差，缺失是不可观测的偏差**。没人报 bug，因为那功能根本不存在。测试全绿，因为没测的东西不会红。

### 三、为什么老办法解决不了

现有机制全作用在上下文（劝导），无一作用在交付物（拦截）。效力衰减链五级：

**在场不触发 → 计划不引用 → 压缩失真 → 仪式化合规 → 产出照旧反人类**

一句话：**劝导会衰减，法律不会。** Skill 是劝导，可复跑工件才是法律。

### 四、产品工程的答案（及它的边界）

答案：**把「产品该有的都得有」翻译成「机器能检查」。**

给失忆的工人外置工匠三件套：

- **地图**（registry：项目里已有什么）
- **厂规**（判定表：这个项目什么算对）
- **验收机**（门禁：交付是不是真的，带真实退出码）

手法层（怎么写才好看：样式、组件、动效、文案）是设计类 Skill 的红海；本项目的位置在那之外的**结构层**——设计 Skill 只设计怎么做，我们定义各功能的流程状态怎么来。中心对象是**联通层**——功能语义 ↔ 交互逻辑之间的可判定契约，载体是 statechart（无死端 / 全可达 / 错误态有恢复 =「出路」的数学表述）。

它的边界必须说清：

- **PE ≠ PI**：不管产品创新，那是产品决策侧（该创造什么 / 市场机会 / 商业模式）
- **三不管**：不定义主题与组件、不管审美手法、不管流程纪律
- **唯一职责**：规定「这个功能应怎么来」
- **范围**：本包 = Product Contracts 规范层的**第一垂直域**（交互工程，层级门 + 上游产品对象定义 + 中游交互工程已落地）；母架构其余域**未实现**，诚实占位——[docs/product-architecture.md](docs/product-architecture.md)
- **目的态**：3 万与 30 万的 APP 功能清单可以完全相同，差价全在旅程完整性——空态有引导 / 等待不焦虑 / 出错不慌 / 反悔有路 / 回来还认识。AI 把组件样式压成通缩品，这个差价就是它要变成可判定、可生产清单的东西。

**核心句**最终落在（可对照实验度量，而非不可验证的「全局最优」）：

> **让对当前模型最便宜的路径，不再系统性地成为对产品未来最昂贵的路径。**

### 诚实栏（已实证 ／ 待追认 ／ 现在还不牢）

**已实证（可重跑）**

- **「缺失可检出」已实证**：statechart-gate C1-C7 四变异反向注入全拦、对照组全绿，可重跑 `docs/reverse-injection/verify.py`；**L0 层再证**——l0-l5-gate 对三个真实会话工作区「目标未陈述」检出 3/3。
- **真实新会话生效链已闭合（原「最后一环」）**：六个 CUA 真会话探针实证——注入核心（zxc663 自检+hooks 双通道+复述/承载/教训纪律）在真实新会话完整生效；产品包自然触发曾失败（NR1 关键失败样本）→ 断点定位到 description 选择显著性 → v0.2.2 触发词前置 → NR6 同任务对照**触发成功**（能力检索命中自证+statechart 双跑 exit=0+实机走查 6 验收+真缺陷修复回归）。全文：[docs/real-session/nr-batch1-judgment.md](docs/real-session/nr-batch1-judgment.md)。
**待追认（设计在案）**装 Skill 侧维护债 13 vs 对照 50、内联样式 1 vs 38、持久测试 63 vs 0；对照侧一个真 bug 从 R1 存活到 R3（无测试防线）；token 曲线递减 vs 暴涨。限定单次对照，随机性未消除。
- **上游 L0-L4 全获机器判据**：product-object-gate P1-P4（真实项目首用即检出 10 项真缺口）+ l0-l5-gate（L0 目标合格线 11 格电池+L5 结构底线三轨；「≤3 clicks」被实证否决不入判据）。
**现在还不牢** N=1（随机性未消除）；门禁只吃扁平 statechart schema；跨项目泛化待做；L5 语义项（标签同义/混类/阈值）与 tree testing 实测属人工域；A/B 四指标口径草案待追认——全文见一页纸 §「现在哪里还不牢」。

---

## 核心构件

| 构件 | 一句话 | 出处挂靠 |
|---|---|---|
| 产品对象六问 | 上游先于一切：为什么存在/职责句/能力清单/主次（恰好一个主功能）/能力完整性（八组闭环）/可运营性（谁能管）——缺答=停 | 用户定稿 2026-09-23（四偏移纠正，direction §十二） |
| 层级栈 L0-L10 + 层级门 | 先定位「在回答哪一层的问题」→检上游→才允许下沉；**实现层完整性≠产品工程完整性** | 用户定稿 2026-09-23（direction §十三） |
| 功能天生六问 | 输入什么/何时发生/成功落哪/防失败-恢复-出路/能否反悔/下次换环境还认吗 | Norman 行动七阶段+两个鸿沟 |
| 联通层 | 功能语义↔交互逻辑的**可判定契约**（双向可追溯+机器可验） | Garrett 五层（范围↔结构接口） |
| statechart 载体 | 态+转换矩阵的源=机器可读 JSON（无死端/全可达/错误态有恢复=「出路」的严格表述） | Harel 1987 / XState |
| 双底双顶+第四底 | 不难用/不难看/无障碍（底线·法律）+更好用/更好看（上限·劝导） | Nielsen/ISO 9241-11/WCAG POUR |
| 反借口表 | 借口→驳斥成对，危险词触发自检；一切规则二值化 | taste-skill 教训 |
| 裁决账本 | 记「为何这么定」，跨会话复利——劝导会衰减，法律不会 | 本项目原创（同类空白） |
| 效力衰减链 | 在场不触发→计划不引用→压缩失真→仪式化→产出照旧：五级衰减与对策 | 见 docs/direction.md §七 |
| 契约 schema | Interaction/Gate/Evidence 三件；硬层机器可验、软层可追溯（禁全链 JSON 化） | 用户裁决 2026-09-23 |
| 风险自适应四档 | 档0 不启动 / 档1 轻量 / 档2 六问+trace / 档3 +recovery+evidence+regression | 判定表 §风险档位（2026-09-23 由 L0-L3 改名防与层栈混淆） |

## 仓库结构

```
docs/one-page-definition.md ← **一页纸：这个 Skill 是什么**（简明版规范，冷启动先读）
docs/direction.md          ← 方向档（问题定义/衰减链/品味与时序/联通层/强制边界/修正记录 §十一-十三）——权威设计档
docs/product-architecture.md ← 母架构与定位边界（Product Contracts 七域；已落地=Interaction）
docs/three-definitions.md  ← 三定义调研（产品/工程/产品工程 加固定义 + 缺失逻辑可检出表述）
docs/layer-judgement-matrix.md ← 层×判据矩阵（11 层各自有哪些判据/人工裁决域/空白）
docs/reverse-injection/EVIDENCE.md ← 「缺失可检出」反向注入实证（可重跑：verify.py）
docs/cold-start-report.md  ← 触发链三条件×8 样本实验（断点定位→修复→闭环）
docs/ab-four-metrics.md    ← A/B 四指标口径草案（defect_escape/rework/coverage/cost，待追认）
参考Skill/A~H              ← 八份调研蒸馏（设计品味系/工作流极简系/工具文档系/外部同类/桌面项目/成熟方法论/高密度界面/结构层蓝海）
skill/…（在家族主仓）       ← 第四包本体：SKILL.md + references 九件 + scripts 八台门禁与提取器（权威副本在母仓 skill/shisan-xinuo-product/scripts/）
memory/agent-log.md        ← 工作流水（诚实留档：含每轮 GATE 与教训）
```

## 门禁用法（八台，均带 `--selftest` 两态自测）

> 权威副本在母仓 `skill/shisan-xinuo-product/scripts/`（安装后位于技能目录 `shisan-xinuo-product/scripts/`），下例用母仓路径。

```bash
# ① 组件归因检查（自研必须带归因标记 registry:）
python skill/shisan-xinuo-product/scripts/registry-gate.py --path <组件目录> --selftest
# ② statechart 结构检查 C1-C7（出路严格表述 + 引用完整性 + 契约 recovery 双向对账）
python skill/shisan-xinuo-product/scripts/statechart-gate.py --file statechart.json --selftest
# ③ 双向追溯（功能行↔组件↔后端块↔证据；T4 UI 孤儿 / T5 死逻辑）
python skill/shisan-xinuo-product/scripts/spec-trace-gate.py --trace <trace.csv> --selftest
# ④ 产品对象上游判据 P1-P4（定义存在性/主功能唯一/层级声明+上游引用/可运营性）
python skill/shisan-xinuo-product/scripts/product-object-gate.py --file <object.json> --selftest
# ⑤ L0 目标合格线 + L5 结构底线（单值性/度量口径/KR 时间窗/导航三件套/前门可达/死端页）
python skill/shisan-xinuo-product/scripts/l0-l5-gate.py --selftest
# ⑥ 前端 lint（内联样式/硬编码色/console/空 catch；基线豁免存量只拦新增）
python skill/shisan-xinuo-product/scripts/frontend-lint-gate.py --selftest
# ⑦ 可达性静态底线 A1-A4（img-alt/控件可访问名/交互元素可访问名/html-lang）
python skill/shisan-xinuo-product/scripts/a11y-gate.py --selftest
# ⑧ 使用率监控（装了没人触发=衰减警报）
python skill/shisan-xinuo-product/scripts/usage-probe.py --selftest
# 附：绑定清单自动提取器（从组件目录/后端声明生成 comps/backs 喂 spec-trace-gate）
python skill/shisan-xinuo-product/scripts/spec-trace-extract.py --help
```

## 与家族的关系

本包 = 家族**第四包**（核心 / 流程 / 角色 / 产品工程，四包独立可装、建议同装）。`shisan-xinuo-workflow` 核心包已埋**条件式挂接钩子**（skill-usage §8）：本包在场→三缝合点自动生效（计划检索位 / GATE 门禁真值 / 收尾账本写回）；不在场→跳过+GATE exempt 声明。主仓 `install-skill.ps1 -Family` 已纳入本包（四包齐装）；获取方式见文首「怎么获取与安装」。

## 设计纪律（本仓库自己的规矩）

- 隐私红线：真实账单/密钥绝不入仓。
- 诚实红线：未实现/未验证显式标注；出处带信心级（原文读过/转述可靠/待验），接受抽验。
- 强制清单宁缺毋滥：新增强制须过「可机器判定+决策点拦截+成本检验」三判据；新机制过元规则六问，答不上就删。
- 反面校验：不写更多抽象原则；不追求「模型拥有审美」；厂规不写一千条。

## License

MIT（与家族主仓一致）
