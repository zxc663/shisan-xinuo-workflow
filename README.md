# Shisan Xinuo Agent Workflow

**十三希诺 · 纪律元工作流（v3.4.0）**——让规则**真正被消费**、让结论**可复算**、让高危动作**先停后行**的工程治理元 Skill。

> **本质一句话**：把「工程纪律」从**提示词**升级成**机制**——提示词只是载体（规则怎么送到模型面前），本体是四件套：**流程结构**（三级跑道 + 出口产物）+ **可跑门禁**（发行 8 项 / 产品工程 8 台）+ **可复算证据**（`GATE` 三挂靠 / 判据版本化 / 事实与叙述对账）+ **停点与记忆**（L3 封闭清单 / `risk_scan` / 406 条细则 / agent-log）。

| 看法 | 它是什么 | 决定什么 |
| --- | --- | --- |
| **载体** | 可注入的 Skill：`SKILL.md` + `references/` + `templates/` + 五平台注入器 | 规则**能不能到场** |
| **本体** | 把纪律变成机制：触达 / 执行 / 证据 / 防线与记忆 四组机制 | 到场之后**有没有用** |

> **一句话定位**：它不承诺更好的代码——它承诺更少的事故。它把 Agent 的工程纪律做成**可执行、可复跑、可复算**的流程结构：过程可追责，结论可复核；密钥外泄、误发布、通配符删库、无备份迁移这类**严重工程事故**，被 L3 停点拦在发生之前（红线行为面探针双样本全绿，`EVIDENCE.md` §三十三）。

> **English summary** — A discipline meta-workflow for coding agents. It makes rules *actually consumed* rather than merely present, and makes conclusions *re-computable*: three-lane routing (L1 fast lane / L2-S short workflow / L2-F full 9-step), a closed L3 checklist for irreversible actions plus an execution-layer enumeration of out-of-list high-risk domains, a confirmation protocol with recommendations, re-runnable `GATE` evidence blocks with an evidence-layer field (`ev=exec/cover/invariant/indep`), a project-level ledger (`memory/agent-log.md`, dual-metric cap + mechanical rotation), platform injection adapters for five agent platforms with content-hash acceptance, and a symptom-indexed library of **406 lessons across 33 categories**. Ships as four independently installable packages (core / flows / roles / product). Its headline claim is deliberately narrow — not better code, but **fewer severe incidents**: red-line behaviour probes (secrets / release / deletion / migration / blanket authorization) pass on double samples. Every number below is machine-produced: **20/20** behaviour probes on the v3.1 matrix and **22/24** on the post-deployment run (judge j2.4, with fingerprints), **23/23** judge gold-sample regression (judge j2.5), 52 probes at 98.1% on the v2.9.0 baseline, plus an independent review pass.

## 作者的话 · A note from the author

> **「工程化的确定性和稳定性，才是让 AI Agent 从玩具落到实地的真正要点。」**

确定性，是同一套纪律换一个会话、换一个模型、换一个平台仍然复现——所以这里的每条规则都带**触达端口**（注入锚点 / 错误时刻推送 / 预读 TOP），而不是靠"希望模型记得住"；该问的停下来问，该跑的真跑一遍。

稳定性，是不因遗忘、压缩、换人而失效——所以这里的结论必须**可复算**：`GATE` 带真实命令与退出码，判据有版本与金样本回归，高危动作被 L3 停点拦在发生之前。过程对得起复核，结论对得起复算；**做不到的，这里不写进承诺**。

## 收益与代价 · The trade-off

**它实际买到的（作者实测口径，只报能兑现的）**：

- **误操作被拦下来是真的**：作者日常使用中多次拦下本该发生的操作；红线行为面探针（密钥 / 发布 / 删除 / 迁移 / 笼统授权，双样本全绿，`EVIDENCE.md` §三十三）给出可复跑的同向证据。这是该装它的第一理由。
- **返工少了**：该问的先问、该留的回滚点先留、结论终带可复跑证据——错误在发生前/发生时被抓住，而不是在复盘时。
- **跨会话不断链**：`memory/agent-log.md` 一档制 + 细则库（406 条/33 类）把踩过的坑留给下一次。

**它明确要付的（别被"轻量"误导）**：

- **token 成本是真的**：注入核心**每会话常驻 ≤6000 字符**（中文按常见分词器约 **4–6K token**；`EVIDENCE.md` §九 另有 ÷4 的保守估算口径与逐版实测表），另有在场锚块与平台开销。
- **按需加载另计**：细则按症状加载 **1–3K token/次**；`SKILL.md` 全载 **6–10K**（仅在「完整读取」触发时）。
- **L2-F 流程本身也花 token**：调研、门禁、留档、复跑都是成本——**它的主张从来不是"更省 token"，而是"用可控的固定治理成本，换确定性与可审计性"**（`EVIDENCE.md` §九 定稿口径）。

**什么时候值 / 什么时候不值**：值——高危操作、长周期、跨会话、要交付给别人复核的活；不值——一次性小脚本、纯问答、短平快任务（用 **L1 快速通道**，或干脆别装）。

## 目录 · Contents

- [作者的话](#作者的话--a-note-from-the-author)
- [收益与代价](#收益与代价--the-trade-off)
- [为什么用它](#为什么用它--why-this)
- [它能拦住什么](#它能拦住什么--what-it-stops)
- [它为谁解决什么](#它为谁解决什么--who-its-for)
- [四包体系](#四包体系--packages)
- [功能全景](#功能全景--feature-map)
- [差异化优势](#差异化优势--differentiation)
- [架构真相](#架构真相--architecture-truths)
- [验证与路测](#验证与路测--evidence)
- [分发渠道](#分发渠道--distribution)
- [快速体验](#快速体验--quick-start)
- [安装与注入](#安装与注入--install--inject)
- [口径块](#口径块--facts-at-a-glance)
- [仓库结构](#仓库结构--repository-layout)
- [局限与代价](#局限与代价--limitations)
- [常见问题](#常见问题--faq)
- [来源与依据](#来源与依据--sources)
- [版本历史](#版本历史--changelog)
- [贡献者与许可](#贡献者与许可--license)

## 为什么用它 · Why this

它有两种看法，答案不同：**当载体看**，它是一份可注入的 Skill——SKILL.md 是正文、references 按需加载、templates 可复制，靠五平台注入把规则送到模型面前；**当本体看**，它是一套把纪律变成机制的治理层——**规则要被消费**（触达端口）、**结论要可复算**（门禁与证据）、**高危要先停**（L3 停点）、**经验要复利**（细则库与账本）。载体决定「能不能到场」，本体决定「到场之后有没有用」——本项目全部重心在本体。

Agent 的常见失败不是「不会写代码」，而是**规则在场却不被执行**：约束写在提示词里，任务一开始就被遗忘；该问的没问、该留的回滚点没留、该复跑的验证没跑；错误处理靠猜、结论靠感觉。

本 Skill 把「纪律」做成**可执行的流程结构**：任务先过场景判定与开工四步（复述+状态行 → 承载检查 → 记忆对齐 → 前置门+能力检索+判级选道），再走三级跑道，收尾产出一行可复跑 `GATE`：

1. **跑道化**——任务先分级选道，L1 直做、L2-S 短工作流、L2-F 完整 9 步；分级不靠气氛靠判据。
2. **门禁化**——每个任务块收尾产出可复跑的 `GATE` 行（含真实命令与退出码），验证变成**证据**而非声明。
3. **承载化**——项目根落 `memory/agent-log.md` 一档制（状态段/教训区/偏好段/流水区），跨会话续接有据可查。
4. **注入化**——五种平台各有注入适配，规则在新会话**在场**；验收判据是平台解析到的 Base directory，不是文件里的版本号。
5. **教训化**——踩过的坑按症状索引入库（406 条/33 类），下次同类症状先检索再动手。
6. **停点化**——L3 封闭清单（密钥/权限 · 数据删除 · 迁移 · 对外发布 · 架构选型 · 超预算破坏性）命中**先问后做**；清单外高危域有 `risk_scan.py` 机检兜底。规则可以补救，事故不能——这是整套机制的最后一道防线。

三条常驻机制：**Token 精算机**（省的是仪式不是实质：检索按档位、命中即停、超预算写 `stop_reason` 止损）；**状态锚定**（状态段首行 `STATE: task_id|level|route|confirm|gates_passed|last_errpath`，三触发重读）；**判据可信度**（判据版本化 + 金样本回归 + 指纹，版本史见 `docs/roadtest-scorecards/JUDGELOG.md`）。

## 它能拦住什么 · What it stops

先把主张说小：**它不提升代码质量——质量该由评审与测试负责；它拦的是「根本不该发生的动作」。** 这类动作不靠写得更优雅来防，只靠停点来防：

| 事故形态 | 拦截机制 | 证据位 |
| --- | --- | --- |
| 密钥写进代码 / 提交 / 对话 | L3 封闭清单（密钥/权限）命中先问 + 门禁 D 项泄漏扫描 | 红线行为面双样本全绿（`EVIDENCE.md` §三十三） |
| 未经确认的对外发布 | L3「对外发布」停点（含发布面双因变体探针） | 同上 |
| 通配符 / 递归删库 | L3「数据删除」停点问询 | 同上 |
| 无回滚点的数据 / 服务迁移 | L3「迁移」停点 + 回滚点红线 | 同上 |
| 「你看着选」式笼统授权被扩大 | 只覆盖明示项，未答项仍必问 | 同上 |
| 清单外高危域（CI/CD · DNS · IAM · 计费 · feature flag · webhook · 限流 · OAuth 回调 · 生产配置写） | `scripts/risk_scan.py` 机检，命中至少按 L3 停点 | `细则 #370` |

**真仓对照实证**（工具箱对照实验，同任务甲/乙双仓）：使用本 Skill 的甲仓在复查轮抓到并修复「meta 工具清单漏登新增工具」，未使用的乙仓同缺陷留在 HEAD；甲仓沉淀 63 项测试 + 四道机器门禁 + 规格/账本文档链，乙仓零测试、零说明文档。公平性注记：单任务小样本对照，乙仓并非全面更差，这组证据说明的是**纪律层改变了错误被发现的时机与知识是否沉淀**。

## 它为谁解决什么 · Who it's for

- **长时间、多会话的工程任务**：需要跨会话续接、需要别人（或未来的自己）能读懂决策链。
- **多平台/多模型切换的人**：Codex、Claude Code、Trae、WorkBuddy、ZCode 之间换着用，行为期望一致。
- **审计 / 评审 / QA 视角**：`GATE` 可复跑、状态面可核对、判分口径预注册——可直接当"Agent 行为审计样张"。
- **踩过坑的独立开发者**：细则层就是一本按症状检索的踩坑日志 + 错误必查 TOP。
- **无人值守 / 批处理场景**：L3 停点是没人看的时候仍在场的「人类回路」——密钥、删除、迁移、发布在无人值守下也会先停下来。

## 四包体系 · Packages

四包独立可装、组合使用，共同构成一套完整纪律体系；`pwsh scripts/install-skill.ps1 -Family` 一次装齐（核心 + 流程 + 角色 + 产品工程）：

| 包 | 定位 | 内容 |
| --- | --- | --- |
| `shisan-xinuo-workflow` | **核心**（纪律元工作流） | 三级跑道 / 判级速查 / 必问与红线 / `GATE` 12 字段 / 状态锚定 / 承载与留档 / 部署与自更新 / `references/`（注入核心、细则库、平台适配、规则清单）+ `templates/`（含 hooks 模板） |
| `shisan-xinuo-flows` | **流程包** | 9 类任务工作流分册（新功能 / Bug 修复 / 重构 / 数据迁移 / 发布 / 前端设计 / 运维 / 文档 / 探索调研）+ 澄清流程 + 双调研与复用五问 + 模板 7 件 |
| `shisan-xinuo-roles` | **角色包** | 8 个审查/执行角色（critic / risk-reviewer / security-auditor / debugger / contract / test / frontend / perf），每角色六字段解剖 + dispatch 矩阵 + 行动契约 |
| `shisan-xinuo-product` | **产品工程包**（独立版本线 v0.2.7，本批 checker 反向变异修复；设计源与全部实证在 [product-engineering-skill](https://github.com/zxc663/product-engineering-skill)） | 层级门（L0-L10）/ 产品对象六问 / 联通层契约（statechart）/ 双底双顶 / 判定表 / 8 台可重跑门禁（组件归因 / 态机 C1-C7 / 双向追溯 / 产品对象 P1-P4 / L0-L5 / 前端 lint / 可达性 / 使用率） |

> 另含**单文件版**（`skill/shisan-xinuo-single/`）：核心包 SKILL.md 全文并入一个文件（自用硬注入）；写入平台规则文件后每会话常驻（文件内含「要动的文件」表）；细则库 / 流程 / 角色 / 产品包与脚本门禁仍在主体系。

产品工程包解决的是另一类失败——**「产品该有的都得有」缺了没人报**：缺失是不可观测的偏差，测试全绿不代表该有的都在。它把「缺失逻辑」翻译成机器能检查的门禁（「缺失可检出」反向注入四变异实证，可重跑见设计源仓 `docs/reverse-injection/`）。

## 功能全景 · Feature map

| 机制组 | 能力 | 说明 | 载体 |
| --- | --- | --- | --- |
| **触达**（规则要被消费） | 平台注入与自更新 | 五平台注入点表、备份合并不覆盖、副本内容哈希验收；三路合并同步多平台副本；SessionStart/PostToolUseFailure hooks 加固（可选面） | `references/platform-adaptation.md` + `scripts/deploy_injection.py`、`scripts/syncer.py`、`templates/hooks/` |
| **执行**（流程要被走完） | 跑道与判级 | 三级跑道（L1/L2-S/L2-F）+ 选道三问 + L3 封闭清单 6 项 + 三层分界（判级≠理解确认） | 核心 `SKILL.md` §2 + 注入核心 |
| **执行** | 开工四步与状态行 | 复述 → 承载 → 记忆对齐 → 能力检索与选道；每轮首产物可 grep 校验 `Context: state=… L=… confirm=…` | 注入核心 |
| **证据**（结论要可复算） | `GATE` 完成块 | 12 字段单行、可复跑；证据三挂靠（cmd 原文 / exit 真值 / files 真变）；`ev=` 验证层级 | 核心 §6 + `scripts/gate_audit.py` |
| **证据** | 门禁 | **8 项**发行门禁（含 H 判据自测）+ 事实对账单源断言（含条目上限） | `scripts/verify-release.ps1`、`scripts/facts_sync.py` |
| **证据** | 行为面 harness | 探针矩阵 + scorecard 随仓 + 判据版本化/金样本自证/同批重判 | `scripts/probe_runner.py`、`docs/roadtest-scorecards/` |
| **防线与记忆**（高危先停 / 经验复利） | 清单外高危域机检 | `risk_scan.py` 扫 CI/CD·DNS·IAM·计费·feature flag·webhook·限流·OAuth 回调·生产配置写——命中即至少按 L3 停点问询 | `细则 #370` |
| **防线与记忆** | 细则库 | 406 条 / 33 类，症状索引检索键 100% 覆盖 | `references/details.md` |
| **防线与记忆** | 细则检索端口 | `python scripts/detail_lookup.py "<症状关键词>"`（关键词/编号/症状域三查） | `scripts/detail_lookup.py` |
| **防线与记忆** | 项目承载 | `memory/agent-log.md` 一档制（四区）+ 双指标上限 + 机械归档 | 模板 + 核心 §8 |
| **产品面**（第四包） | 产品工程门禁 | 8 台可重跑门禁，各带 `--selftest` 两态自测 | `skill/shisan-xinuo-product/scripts/` |

## 差异化优势 · Differentiation

- **规则被消费 ≠ 规则在场**：每条机制都有行为面判据与探针证据，不靠"写得很全"自证。
- **可复跑证据**：`GATE` 行带真实命令与退出码；`git` 变更与文件 mtime 可外部审计（`gate_audit.py`）。
- **反作弊设计**：虚假 `GATE`（自报与探针不符）会被判定并降级为未完成——自报字段必须配外部痕迹。
- **诚实分档**：L2-S / L2-F 允许边界豁免，但**跳过必声明**（复述跳过项 + 留依据 + 一行提醒），静默跳过=违规。
- **跨平台一致**：同一套纪律在五个平台注入副本同步，验收以平台解析到的 Base directory 为准。
- **负面结论更严**：判"不复现/不存在"需判据逐字对齐 + 真实调用链（禁自造模拟）+ 对照实验，否则降"未定论"。
- **主张说小、证据说满**：头条主张不是"更好的代码"，而是"更少的事故"——用红线行为面探针（双样本全绿）与高危域机检来证，不用形容词证。

## 架构真相 · Architecture truths

- 本仓库 = **源库 + 实证场**：既是 Skill 分发源，也是「用本工作流开发自身」的实证场——细则库中相当一部分条目来自本项目自身的踩坑。
- **三层注入**：记忆层（平台记忆/项目记忆文件）· 规则层（`AGENTS.md` / `CLAUDE.md` / 平台规则文件）· 配置层（hooks / provider / model）。项目级规则文件按平台注入点表定名，**先备份、合并不覆盖**。
- **验收判据**是平台解析到的 Base directory 与注入副本内容，不是文件头里的版本号。
- **注入版本 = 会话创建时的快照**：升级副本后必须**重开新会话**才生效。
- **版本口径**：版本号以 `package.json` 为准，三个同线包 `SKILL.md` 的 `name/version` 与之一致（门禁断言）；产品工程包独立版本线（v0.2.7）。

## 验证与路测 · Evidence

| 维度 | 结果 | 证据位 |
| --- | --- | --- |
| 红线行为面 | 密钥（含 covert 变体）/ 发布 / 删除 / 迁移 / 笼统授权 全绿（双样本） | `EVIDENCE.md` §三十三 |
| 判据自证 | 判据版本化 j1.0→j2.5 + 金样本回归 **23/23** + 同批输出离线重判 + 环境失败行证据签名 | `python scripts/probe_runner.py --judge-selftest`、`JUDGELOG.md` |
| v3.1 全矩阵 + 三面校准 | 20 场景 **20/20 PASS**（单批样本）；部署后实跑 **24 针 22 PASS**；v3.2.0/v3.3.0 源库 · 五平台注入 `--check --hash` 5/5 · 六处副本一致 | `docs/roadtest-scorecards/`、`EVIDENCE.md` §四十一/§四十三 |
| 外部独立审查/审计 | 另一模型无头只读审查（P0 当日修复）；双轨审计 + 6 项条款级提案落地 | `docs/independent-review-v3.0-20260918.md`、`docs/audit-external-review-20260920.md` |
| 已知缺口（诚实） | v3.3.0 批 A′ Flash 档无头矩阵 13/20（`ev=`/stateLine 未稳定）；五门禁反向注入 27 例漏报 15 | `EVIDENCE.md` §四十三、`docs/gap-list-20260929.md` |

> **口径脚注（可复算入口）**：①「24 针」范围 = `precheck 1 + v310-inf-01 20 + 双击复采 v310-inf-01r 2 + v310-inf-02 1`，作废行（`env_death`）全数剔除、双击复采行**计入**。②按「剔除复采」读法可用 `python scripts/scorecard_agg.py --exclude-recollect` 机检。③「20/20」为单批样本（含同批重判），不代表稳定通过率；2026-09-20 独立审计的新采样 7 针得 5 PASS / 2 FAIL（失败集=skip-floor / multi-task）。完整证据链见 [`EVIDENCE.md`](EVIDENCE.md) 与 `docs/roadtest-scorecards/`。

## 分发渠道 · Distribution

单一批次同步发行五渠道；下表为**上一发行版 v3.3.1** 条目（本批 v3.4.0 准备态，发行后更新），发行回执见 [`RELEASE-CHECKLIST.md`](RELEASE-CHECKLIST.md)，滚动数据与分渠道分析见[发行成果汇总报告](docs/release-outcome-report-20260920.md)：

| # | 渠道 | 链接 / 安装方式 | 本批版本 | 说明 |
| --- | --- | --- | --- | --- |
| 1 | **GitHub**（源库 + Release） | [github.com/zxc663/shisan-xinuo-workflow](https://github.com/zxc663/shisan-xinuo-workflow) · [Releases](https://github.com/zxc663/shisan-xinuo-workflow/releases) | v3.3.1 | 权威源库；每版附 dist zip |
| 2 | **npm**（GitHub Packages） | [包页](https://github.com/zxc663/shisan-xinuo-workflow/pkgs/npm/shisan-xinuo-workflow) · `npm install @zxc663/shisan-xinuo-workflow` | 3.3.1 | 包为**私有可见性**，读取需 GitHub PAT（`.npmrc` 写 `//npm.pkg.github.com/:_authToken=<PAT>`）；**npmjs.org 未分发** |
| 3 | **Gitee**（镜像 + Release） | [gitee.com/zxc663/shisan-xinuo-workflow](https://gitee.com/zxc663/shisan-xinuo-workflow) · [发行版](https://gitee.com/zxc663/shisan-xinuo-workflow/releases) | v3.3.1 | 与 GitHub 同 commit/tag 双推；每版附 zip 附件 |
| 4 | **ClawHub**（OpenClaw 技能市场） | [clawhub.ai/zxc663/shisan-xinuo-workflow](https://clawhub.ai/zxc663/shisan-xinuo-workflow) · `openclaw skills install @zxc663/shisan-xinuo-workflow` | 平台侧递增号 | 平台侧版本号 1.0.x 递增，内容对应本仓版本；security scans 平台侧异步 |
| 5 | **skills.sh**（Agent Skills 索引） | [skills.sh/zxc663/shisan-xinuo-workflow](https://skills.sh/zxc663/shisan-xinuo-workflow) · `npx skills add zxc663/shisan-xinuo-workflow` | 随 GitHub 同步 | 自动索引 GitHub 源库 |

配套动作：每版发行时 GitHub + Gitee 仓库简介（About）双端同步 PATCH。产品工程包随 `skill/` 全树进入 dist zip 与 npm 包；其独立仓 [product-engineering-skill](https://github.com/zxc663/product-engineering-skill) 同步发行 v0.2.6（README 重构 + 口径修复 + 累积机制补发）。

## 快速体验 · Quick start

1. **装包**（任选其一）：
   - skills 市场：`npx skills add zxc663/shisan-xinuo-workflow`
   - 仓库直装：`git clone <repo>` → `pwsh scripts/install-skill.ps1 -Family`（四包一次装齐）
   - npm（GitHub Packages）：`@zxc663/shisan-xinuo-workflow`——读取需 GitHub PAT（`.npmrc` 写 `//npm.pkg.github.com/:_authToken=<PAT>`）；npmjs.org 未分发
2. **重开一个新会话**（注入版本=会话创建时快照），输入 `zxc663` 自检：应回答「注入方式 / 已应用轮数 / 源库 vs 副本版本 / Base directory」。
3. **给它一个真实任务**：观察三个标志物——①每轮首产物是复述 + 状态行；②关键决策会先问（而不是先做）；③任务块末尾有 `GATE:` 单行与可复跑命令。
4. **想验行为面**：`python scripts/probe_runner.py --label demo l1-rename l3-delete`（探针默认落在系统临时目录，与仓库隔离）；**想验判据**：`python scripts/probe_runner.py --judge-selftest`（零 API 成本，正/负对照全过才算判据可用）。

## 安装与注入 · Install & inject

```powershell
# 1) 技能副本安装（默认识别平台技能目录；可选 -Link / -HardInject）
pwsh scripts/install-skill.ps1
pwsh scripts/install-skill.ps1 -Family            # 四包一起装（核心+流程+角色+产品工程）

# 2) 平台注入（记忆层/规则层/配置层；先备份、合并不覆盖）
python scripts/deploy_injection.py --only codex,claude,trae,workbuddy,zcode
python scripts/deploy_injection.py --check --only zcode        # 注入副本验收
python scripts/deploy_injection.py --check --hash              # 副本内容哈希验收（版本串一致≠内容一致）

# 3) 上游更新同步（体检→备份→迁移→覆盖→双落盘）
python scripts/syncer.py
python scripts/syncer.py --family                 # 全家族包逐包同步

# 4) 发行前门禁（8 项，H=判据自测）
pwsh scripts/verify-release.ps1
python scripts/facts_sync.py --check
python scripts/probe_runner.py --judge-selftest
python scripts/scorecard_agg.py --baseline <旧标签> --current <新标签>   # 路测三态对比
```

**平台注入点**：Codex → `AGENTS.md`；Claude Code → `CLAUDE.md`；Trae → 项目级规则文件；WorkBuddy → `MEMORY.md`；ZCode → `AGENTS.md`。完整注入点表与降级链见 `references/platform-adaptation.md`。

## 口径块 · Facts at a glance

| 项 | 值 |
| --- | --- |
| 版本 | **v3.4.0**（本批准备态 2026-09-30；上一发行版 v3.3.1 全渠道 2026-09-29，回执见 RELEASE-CHECKLIST） |
| 交付形态 | **四包**：核心 `shisan-xinuo-workflow` + 流程包 + 角色包 + 产品工程包（独立版本线 v0.2.7） |
| 细则库 | **406 条 / 33 类**（编号至 `#407`；类数=分节数，单源断言） |
| 注入核心 | **≤ 6000 字符**（PowerShell 字符数 + Python code-point 双口径） |
| 完成块 | `GATE` **12 字段**：`level / v / cmd / exit / files / refs / errpath / lessons / exempt / caps / effort / stop_reason` |
| 行为面 | v3.1 全矩阵 **20/20 PASS**（单批样本）；部署后实跑 **24 针 22 PASS**；判据金样本 **23/23**（j2.5）；v3.3.0 Flash 档基线 13/20（模型档位归因，诚实口径） |
| 判据可信度 | 判据版本化（j1.0→j2.5）+ `--judge-selftest` 金样本回归 + `--rescore` 同批重判 + 环境死亡行**证据签名** + GATE 形态分型 |
| 门禁 | `scripts/verify-release.ps1` **8 项**（A 内容锚点 / B hooks / C 版本一致 / D 泄漏红线 / E 正文净化 / F 索引完整性 / G 事实对账 / **H 判据自测**） |
| 产品工程门禁 | 8 台（registry / statechart C1-C7 / spec-trace / product-object P1-P4 / l0-l5 / frontend-lint / a11y / usage-probe），均带 `--selftest` |

## 仓库结构 · Repository layout

```text
.
├── skill/
│   ├── shisan-xinuo-workflow/    # 核心包：SKILL.md + references/ + templates/
│   ├── shisan-xinuo-flows/       # 流程包：9 类工作流分册 + 模板
│   ├── shisan-xinuo-roles/       # 角色包：8 角色 + dispatch 矩阵
│   ├── shisan-xinuo-product/     # 产品工程包：判据 + 8 台门禁（设计源与实证在独立仓）
│   └── shisan-xinuo-single/      # 单文件版（核心全量·自用硬注入）
├── scripts/                      # 工具面：部署/同步/门禁/事实对账/审计/探针
├── docs/                         # 项目导航 + 计划 + 独立审查/审计报告 + 路测 scorecards
├── memory/                       # 单项目承载（本地档案，随 .gitignore 不入仓）
├── dist/                         # 发行 zip（版本化）
├── README.md · CHANGELOG.md · EVIDENCE.md · RELEASE-CHECKLIST.md
└── package.json · LICENSE
```

## 局限与代价 · Limitations

- **上下文成本真实存在**：注入核心常驻 ≤6000 字符（中文约 4–6K token，口径见「收益与代价」与 `EVIDENCE.md` §九）；细则按需 1–3K、`SKILL.md` 全载 6–10K。窗口越小，收益/成本比越需要权衡。
- **不是"零错误保证"，也不提升代码质量**：它降低的是**严重事故发生率**（删库 / 泄密 / 误发布 / 失守迁移）与流程性失误（漏问、漏验证、漏留档），不是缺陷率——代码质量仍由评审与测试负责，业务判断不替代。
- **平台能力有差异、行为面存在方差**：无头模式（`-p`）注入面可能断裂；hooks 落盘面受平台持久化策略影响——行为结论**只认请求体/rollout 层证据**，同一场景 n=1 不可作结论（本项目用双击复采区分"缺口"与"噪声"）。
- **维护成本**：细则与副本需要同步；改模板 ≠ 改副本（hooks 指向仓外脚本的场景尤其明显）。

## 常见问题 · FAQ

**Q：它和"写一份很长的提示词"有什么区别？**
A：提示词是"希望被记住"；本 Skill 是流程结构 + 门禁 + 证据：分级选道、必问触发、`GATE` 可复跑、教训可检索。**规则在场 ≠ 规则被遵守**，前者靠提示词，后者靠机制。

**Q：它能让代码质量变好吗？**
A：这不是它的主张。它拦的是"根本不该发生的动作"（L3 清单 + 高危域机检），不是"写得不够好的代码"。质量请交给评审与测试；事故才交给停点。

**Q：会拖慢简单任务吗？**
A：L1 快速通道就是为此存在：一句话复述 + 最小修改 + 最小验证 + 一行汇报；承载与细则检索都可豁免（豁免须声明）。

**Q：升级后为什么行为没变？**
A：注入版本=会话创建时快照。升级副本后要**重开新会话**；`zxc663` 自检可确认副本版本与 Base directory。

**Q：能不能只装流程包/角色包/产品工程包？**
A：可以独立安装，但它们默认假定核心包的纪律面在场（`GATE`/状态行/判级），建议核心 + 目标包组合；`-Family` 一次装齐四包。

**Q：`GATE` 行会不会变成"应试作文"？**
A：设计上就是防这个：`GATE` 三挂靠（命令原文/退出码真值/文件真变）可被 `scripts/gate_audit.py` 外部抽检；自报与探针不符会被判**虚假 GATE** 并降级。`caps/effort` 这类自报字段要求配可核对痕迹。

**Q：数据与隐私？**
A：默认不联网、不外发；密钥类信息**绝不写入**代码/文档/提交/对话（门禁 D 项扫描发布物），泄露即轮换。

## 来源与依据 · Sources

- 细则库来源逐条标注（`*来源/晋升*` 字段），晋升遵循"同坑单项目两次 / 跨项目一次"经验回流制。
- 引用外部项目与资料登记在 [`docs/reference-sources.md`](docs/reference-sources.md)。
- 行为面数字来自本仓库自己的探针批与路测（`EVIDENCE.md` + `docs/roadtest-scorecards/`），不含推测数据。

## 版本历史 · Changelog

- **v3.4.0**（2026-09-30，**本批·准备态**）：**弱锚结构化 + 批X 反向变异修复 + 对标 A/C/D 施工**——①`ev=` 升格为与 GATE 12 字段并列的内联键（Flash 档 0/20 散文弱锚实证→结构化），stateLine 模板补实例形态；②批X 五 checker 十三缺口修复（registry/product-object/l0-l5/frontend-lint/a11y 的类型穿透/变体绕过/枚举死代码），selftest 全部补反向样例（细则 #407）；③`risk_scan` 高危域扩至 IaC 落盘+基础设施 reload；④flows 新增 §10 会话诊断复盘（七维+path:line 举证）、§9 五问升六问（+基线反例）；⑤盲评执行细化档落库；⑥退役机制首跑验证（usage-probe，双批次窗口未满零删除）。细则 **406 条/33 类**（+1：#407）。
- **v3.3.1**（2026-09-29，**已发行**）：**双仓门面重构 + 净化瘦身 + 产品仓联动发行**——①README 分层瘦身（314→约 200 行）：宣发式元话术净化、四包口径对齐、facts 承载点重锚；②产品工程包升格为正式列名第四包并同步发行 v0.2.6（设计源仓 README 重构 + Release + zip）；③`install-skill.ps1 -Family` 纳入产品包（四包齐装）；④口径校对：AGENTS.md 基线行/scripts/README 门禁项数/facts_sync 死锚修复。细则 405 条/32 类、判据 j2.5、门禁 8 项不变。
- **v3.3.0**（2026-09-29，**已发行**）：细则 373→**405 条 / 32 类** + 语义检索三层 + 机制八件（`narrative_sync` / `anchor_sweep` / `sync-all` / `net_pick` / `usage_probe` / 退役候选 / `#379` 权威声明 / Mimosa 反馈包）+ 行为面诚实口径（批 A′ 13/20 + 反向注入漏报 15 入预注册）。
- **v3.2.0**（2026-09-20，**已发行**）：外部评审审计 + 条款级落刀批——`细则 #370`-`#374`（清单外高危域 / `GATE ev=` / 记忆档双指标 / 机器事实优先 / 副本内容哈希）+ 四个机检端口 + 判据 j2.5（金样本 23/23）。细则 368→373 条。
- **v3.1.0 / v3.0.0 / v2.9.0**（2026-09-15~19，**均已发行**）：判据可信度批（j1.0→j2.4 + scorecard 指纹）/ 三包体系与 `GATE` 12 字段 / 独立审查修正批与安全基线。
- 完整沿革见 [`CHANGELOG.md`](CHANGELOG.md) 与 `git log`；发行回执见 [`RELEASE-CHECKLIST.md`](RELEASE-CHECKLIST.md)。

## 贡献者与许可 · License

- 作者：十三希诺（single-maintainer 项目，中文优先）。
- 许可：[MIT](LICENSE)。
- 反馈：issue / PR 欢迎；涉及规则语义的改动请附**行为面证据**（探针输出或真实会话片段），否则只按文档修正处理。
