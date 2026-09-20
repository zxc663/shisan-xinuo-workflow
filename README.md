# Shisan Xinuo Agent Workflow

**十三希诺 · 纪律元工作流（v3.1.0）**——让规则**真正被消费**、让结论**可复算**的工程治理元 Skill。中文优先，单版本分发。

> **一句话定位**：它不是让 Agent 更聪明的提示词，而是把 Agent 的工程纪律做成**可执行、可复跑、可复算**的流程结构——过程可追责，结论可复核。

> **English summary** — A discipline meta-workflow for coding agents. It makes rules *actually consumed* rather than merely present, and makes conclusions *re-computable*: three-lane routing (L1 fast lane / L2-S short workflow / L2-F full 9-step), a closed L3 checklist for irreversible actions, a confirmation protocol with recommendations, re-runnable `GATE` evidence blocks, a project-level ledger (`memory/agent-log.md`), platform injection adapters for five agent platforms, and a symptom-indexed library of **368 lessons across 29 categories**. Ships as three independently installable packages (core / flows / roles). Every number below is machine-produced: **20/20** behaviour probes on the v3.1 matrix and **22/24** on the post-deployment run (judge j2.4, with fingerprints), **21/21** judge gold-sample regression, 52 probes at 98.1% on the v2.9.0 baseline, plus an independent review pass.

## 作者的话 · A note from the author

> **「工程化的确定性和稳定性，才是让 AI Agent 从玩具落到实地的真正要点。」**

我做这套东西，不是为了给 Agent 再加一层规则，而是因为反复看到同一类失败：**规则在场却不被执行，结论自述却无法复算**。所以这里的每条机制最后都落到三件事上——可复跑的 `GATE` 证据、可追责的过程留档、以及从 v3.1 起可复算的判据与指纹。

它不承诺让模型更聪明；它承诺的是：过程对得起复核，结论对得起复算。如果你只用一句话判断它值不值得装——**看它有没有让"我验证过了"变成"你可以自己验一遍"**。

## 目录 · Contents

- [作者的话](#作者的话--a-note-from-the-author)
- [为什么用它](#为什么用它--why-this)
- [它为谁解决什么](#它为谁解决什么--who-its-for)
- [工作原理（文字版）](#工作原理文字版--how-it-works)
- [三包体系](#三包体系--packages)
- [功能全景](#功能全景--feature-map)
- [差异化优势](#差异化优势--differentiation)
- [架构真相（诚实）](#架构真相诚实--architecture-truths)
- [验证与路测](#验证与路测--evidence)
- [分发渠道](#分发渠道--distribution)
- [快速体验](#快速体验--quick-start)
- [安装与注入](#安装与注入--install--inject)
- [口径块](#口径块--facts-at-a-glance)
- [仓库结构](#仓库结构--repository-layout)
- [版本说明](#版本说明--editions)
- [局限与代价](#局限与代价--limitations)
- [常见问题](#常见问题--faq)
- [来源与依据](#来源与依据--sources)
- [版本历史](#版本历史--changelog)
- [许可](#贡献者与许可--license)

## 为什么用它 · Why this

Agent 的常见失败不是「不会写代码」，而是**规则在场却不被执行**：约束写在提示词里，任务一开始就被遗忘；该问的没问、该留的回滚点没留、该复跑的验证没跑；错误处理靠猜、结论靠感觉。

本 Skill 把"纪律"做成**可执行的流程结构**，而不是一段希望被记住的说明：

1. **跑道化**——任务先分级选道，L1 直做、L2-S 短工作流、L2-F 完整 9 步；分级不靠气氛靠判据。
2. **门禁化**——每个任务块收尾产出可复跑的 `GATE` 行（含真实命令与退出码），验证变成**证据**而非声明。
3. **承载化**——项目根落 `memory/agent-log.md` 一档制（状态段/教训区/偏好段/流水区），跨会话续接有据可查。
4. **注入化**——五种平台各有注入适配，规则在新会话**在场**；验收判据是平台解析到的 Base directory，不是文件里的版本号。
5. **教训化**——踩过的坑按症状索引入库（368 条/29 类），下次同类症状先检索再动手。

## 它为谁解决什么 · Who it's for

- **长时间、多会话的工程任务**：需要跨会话续接、需要别人（或未来的自己）能读懂决策链。
- **多平台/多模型切换的人**：Codex、Claude Code、Trae、WorkBuddy、ZCode 之间换着用，行为期望一致。
- **审计 / 评审 / QA 视角**：`GATE` 可复跑、状态面可核对、判分口径预注册——可直接当"Agent 行为审计样张"。
- **踩过坑的独立开发者**：细则层就是一本按症状检索的踩坑日志 + 错误必查 TOP。

## 工作原理（文字版）· How it works

一句话：**场景判定 → 开工四步 → 三级跑道 → 必问与红线 → 执行与验证 → 留档与自更新**。

1. **场景判定**：有项目特征（`git`/多文件/既有 `memory` 或 `docs`）= 持续项目；无特征且非工程任务 = 单发（纪律照走、承载豁免）。
2. **开工四步**（每步有出口产物）：①复述理解 + 一行状态行 → ②承载检查（定承载根、建/补 `memory/agent-log.md`、项目级规则文件）→ ③记忆对齐（只读状态段一屏 + 按症状检索）→ ④前置门 + 能力检索 + 判级选道。
3. **三级跑道**：
   - **L1 快速通道**：改名/文案/格式等可逆小改——一句话复述 → 最小修改 → 最小验证 → 一行汇报。
   - **L2-S 短工作流**：新功能/多文件——对接真相清单 → 复述 → ≤3 文件改动 + 验收 + 回滚基线 → 执行与最小验证 → `GATE`。
   - **L2-F 完整 9 步**：接收 → 调研真实资源（含对接真相表）→ 双调研 → 复述 → 必问 → 五问审查 + 判级 + 回滚点 → 规划与验收 → 执行 → 自查归档。
4. **L3 封闭清单**（仅 6 项，不得自行扩展）：密钥/权限 · 数据删除 · 数据或服务迁移 · 对外发布 · 架构选型 · 超预算破坏性操作。命中即**先问后用**。
5. **必问协议**：关键决策（方向/歧义/风险/破坏性/架构/范围扩大/方案分歧）必问；新建项目与地基决策前先过场景清单；「你看着选」只覆盖明示项。
6. **执行与验证**：最小闭环 = 理解 → 最小修改 → 最小验证 → 交付；「没跑过 = 未完成」。改动验证需覆盖 ≥2 种负载形状。
7. **留档与自更新**：`GATE` 行 + `agent-log` 流水/教训/偏好 + 项目文档同批更新；`scripts/syncer.py` 做三路合并同步到各平台副本。

**Token 精算机（v3.0 机制）**：省的是仪式不是实质——检索按档位（L1 零检索 / L2-S ≤1 次 / L2-F 双预算）、命中即停；结论外部化沉淀（真相表/`caps`/confirm 下次直读）；调研超 2 轮无定论或预算耗尽 → 写 `stop_reason` 止损上报，而非无声燃烧。

**状态锚定（v3.0 机制）**：状态段首行 `STATE: task_id|level|route|confirm|gates_passed|last_errpath` 单行结构化；跨天首轮、子任务派发前、判级选道前三触发重读；复述不出 `level/confirm` 即视为状态失效。

**判据可信度（v3.1 机制）**：判据与结论都是工件，不是自述——①判据改动**只许**修「不识别合规形态」方向，且必须 bump 判据版本 + 过金样本回归（正例必放行、负对照必拒）+ 版本史留档；②每条路测结论带**指纹**（被测副本哈希 / 平台版本 / 判据版本 / 夹具哈希），无指纹的通过率不构成跨批次结论；③环境失败行按**证据**剔除（provider 报错栈 / 空输出），不得与行为失败混计；④`GATE` 合规率按**形态分型**统计（包级 12 字段 / 子块简式 / 杂键），不以单一字段数判合规。落地件：`scripts/probe_runner.py`（`--judge-selftest` / `--rescore`）、`scripts/scorecard_agg.py`、`docs/roadtest-scorecards/JUDGELOG.md`。

## 三包体系 · Packages

三个包可独立安装、组合使用，共同构成一套完整纪律体系：

| 包 | 定位 | 内容 |
| --- | --- | --- |
| `shisan-xinuo-workflow` | **核心**（纪律元工作流） | 三级跑道 / 判级速查 / 必问与红线 / `GATE` 12 字段 / 状态锚定 / 承载与留档 / 部署与自更新 / `references/`（注入核心、细则库、平台适配、规则清单）+ `templates/`（含 hooks 模板） |
| `shisan-xinuo-flows` | **流程包** | 9 类任务工作流分册（新功能 / Bug 修复 / 重构 / 数据迁移 / 发布 / 前端设计 / 运维 / 文档 / 探索调研）+ 澄清流程 + 双调研与复用五问 + 模板 7 件 |
| `shisan-xinuo-roles` | **角色包** | 8 个审查/执行角色（critic / risk-reviewer / security-auditor / debugger / contract / test / frontend / perf），每角色六字段解剖 + dispatch 矩阵 + 行动契约 |

## 功能全景 · Feature map

| 能力 | 说明 | 载体 |
| --- | --- | --- |
| 三级跑道 | L1/L2-S/L2-F 分级与选道三问 | 核心 `SKILL.md` §2 |
| 判级速查 | L3 封闭清单 6 项 + 三层分界（判级≠理解确认） | 注入核心 + 核心 §2.2 |
| 开工四步 | 复述 → 承载 → 记忆对齐 → 能力检索与选道 | 注入核心 |
| 状态行 | `Context: state=… L=… confirm=…`，每轮首产物可校验 | 注入核心 |
| `GATE` 完成块 | 12 字段单行、可复跑；证据三挂靠（cmd 原文 / exit 真值 / files 真变） | 核心 §9 + `scripts/gate_audit.py` |
| 细则库 | 368 条 / 29 类，症状索引检索键 100% 覆盖 | `references/details.md` |
| 细则检索端口 | `python scripts/detail_lookup.py "<症状关键词>"`（关键词/编号/症状域三查） | `scripts/detail_lookup.py` |
| 项目承载 | `memory/agent-log.md` 一档制（状态段/教训区/偏好段/流水区）+ 项目级规则文件 | 模板 + 核心 §5 |
| 平台注入 | 五平台注入点表、按需/强制两种模式、备份合并不覆盖 | `references/platform-adaptation.md` + `scripts/deploy_injection.py` |
| hooks 加固 | SessionStart/Stop 常驻提醒（可选加固面，非运行时必需） | `templates/hooks/` |
| 委托纪律包 | 子代理不继承注入——委托必须内联最小纪律包 | 核心 §6 + 角色包 |
| 行为面 harness | 20 场景探针矩阵（19 + 发布面双因变体），隔离断言 + scorecard 随仓归档 | `scripts/probe_runner.py` |
| 判据自证 | 判据版本化 + 金样本回归（`--judge-selftest`）+ 同批输出两版判据离线重判（`--rescore`）+ 判据版本史 | `scripts/probe_runner.py`、`docs/roadtest-scorecards/JUDGELOG.md` |
| 时序库聚合 | 作废行机器签名剔除 + GATE 形态分型 + 改善/持平/退化三态对比 | `scripts/scorecard_agg.py` |
| 门禁 | **8 项**发行门禁（含 H 判据自测）+ 事实对账单源断言（含条目上限） | `scripts/verify-release.ps1`、`scripts/facts_sync.py` |
| 自更新 | 三路合并同步多平台副本，备份落平台扫描路径外 | `scripts/syncer.py` |
| 自检彩蛋 | 会话内输入 `zxc663` → 注入方式 / 已应用轮数 / 源库 vs 副本版本 | 核心 §11 |

## 差异化优势 · Differentiation

- **规则被消费 ≠ 规则在场**：每条机制都有行为面判据与探针证据，不靠"写得很全"自证。
- **可复跑证据**：`GATE` 行带真实命令与退出码；`git` 变更与文件 mtime 可外部审计（`gate_audit.py`）。
- **反作弊设计**：虚假 `GATE`（自报与探针不符）会被判定并降级为未完成——自报字段必须配外部痕迹。
- **诚实分档**：L2-S / L2-F 允许边界豁免，但**跳过必声明**（复述跳过项 + 留依据 + 一行提醒），静默跳过=违规。
- **跨平台一致**：同一套纪律在五个平台注入副本同步，验收以平台解析到的 Base directory 为准。
- **负面结论更严**：判"不复现/不存在"需判据逐字对齐 + 真实调用链（禁自造模拟）+ 对照实验，否则降"未定论"。

## 架构真相（诚实）· Architecture truths

- 本仓库 = **源库 + 标本库**：既是 Skill 分发源，也是"用本 Skill 开发本 Skill"的实证场（细则库中相当一部分条目来自本项目自身的踩坑）。
- **三层注入**：记忆层（平台记忆/项目记忆文件）· 规则层（`AGENTS.md` / `CLAUDE.md` / 平台规则文件）· 配置层（hooks / provider / model）。项目级规则文件按平台注入点表定名，**先备份、合并不覆盖**。
- **验收判据**是平台解析到的 Base directory 与注入副本内容，不是文件头里的版本号。
- **注入版本 = 会话创建时的快照**：升级副本后必须**重开新会话**才生效。
- 单版本策略：Skill 本体仅中文，README 中文优先 + 英文摘要，不做多语种平行维护。

## 验证与路测 · Evidence

本仓库所有验证数字都来自可复跑工件（原始输出 + scorecard JSONL），完整证据链在 [`EVIDENCE.md`](EVIDENCE.md)。

| 维度 | 结果 | 证据位 |
| --- | --- | --- |
| 行为面基线（v2.9.0 旧副本） | 52 探针 **51 PASS = 98.1%**（11 场景 × n；唯一 FAIL 为 L 类灰色带 n=2 方差） | 夜班监控报告 + scorecards |
| v3.0 场景矩阵 | 19 场景 **18/19 PASS**；8 项新机制 7/8 首跑绿；`gate_fields=12` 全量生效 | `docs/roadtest-scorecards/` |
| 双击复采 | skip-floor 复采 ×2 双 PASS → 首跑 FAIL 判为单例方差（留观察不立条） | 同上 |
| v3.0.0 注入副本冒烟 | **2/2 PASS · GATE 12/12**（真实 headless 探针） | `docs/roadtest-scorecards/smoke.jsonl` |
| 红线行为面 | 密钥（含 covert 变体）/ 发布 / 删除 / 迁移 / 笼统授权 全绿（双样本） | `EVIDENCE.md` §三十三 |
| 独立审查 | 由另一模型无头新会话只读审查（口径一致性/字段/引用/包路径），P0×1 当日修复，P1/P2/P3 分诊并回填 | [`docs/independent-review-v3.0-20260918.md`](docs/independent-review-v3.0-20260918.md) |
| 无头 vs 交互面对照 | 同一平台：无头 `-p` 面注入 0/13 断裂；交互面注入 111/112 在场——**注入面效力只能由真会话验证** | `EVIDENCE.md` §二十六 |
| v3.1 全矩阵（无头 glm-5.3-flash） | 20 场景 **20/20 PASS**（判据 j2.4；**单批存量样本，含同批重判，非稳定率**）；同批输出重判 j1.0 18/20 → j2.2 20/20 | `docs/roadtest-scorecards/v310-j2-0919.jsonl` |
| v3.1.0 部署后实跑（无限循环路测 3.1） | 有效 **24 针 22 PASS**（判据 j2.2，指纹全符）；矩阵级唯一 FAIL=skip-floor 判据滞后（状态行 `confirm=` 形态），j2.3/j2.4 修订后重判 **20/20** | `docs/roadtest-loop-plan-3.1.md`、`v310-inf-01.jsonl` |
| 判据金样本回归 | **21/21**（正例 8 / 负例 13）——含「改了但无验证痕迹必 FAIL」「合规答案提及环境错误词不算会话死亡」「状态行 `confirm=` 属显式澄清申报」等正负对照 | `python scripts/probe_runner.py --judge-selftest` |
| 判据修订史 | j1.0→j2.4 十一处变更逐条附依据（项目终态三候选 + 设计原文对账 + 两处裁决 + 状态行形态） | `docs/roadtest-scorecards/JUDGELOG.md` |
| 外部评审审计（2026-09-20） | 双轨审计（独立五维 + 与外部评审逐条对账）；**8/8 门禁 / FACTS / 判据自测 21/21 / 新采样 7 针 5 PASS** 实测在档；独立发现 8 项（P2×6 / P3×2），条款级 6 项改动作提案待批 | [`docs/audit-external-review-20260920.md`](docs/audit-external-review-20260920.md) |

> **口径脚注（可复算入口）**：①「24 针」范围 = `precheck 1 + v310-inf-01 20 + 双击复采 v310-inf-01r 2 + v310-inf-02 1`，作废行（`env_death`）全数剔除、双击复采行**计入**；声明后新增的 `v310-inf-05` 不在该分母内。②按「剔除复采」读法重算得 23 有效 / 22 PASS，可用 `python scripts/scorecard_agg.py --exclude-recollect` 机检。③「20/20」为单批样本（含同批重判），不代表稳定通过率；2026-09-20 独立审计的新采样 7 针得 5 PASS / 2 FAIL（失败集=skip-floor / multi-task，与存量批同构）。

## 分发渠道 · Distribution

单版本分发，**五个渠道同步发行**；下表为 2026-09-20 实测状态，滚动数据与分渠道分析见[发行成果汇总报告](docs/release-outcome-report-20260920.md)：

| # | 渠道 | 链接 / 安装方式 | 当前版本 | 说明 |
| --- | --- | --- | --- | --- |
| 1 | **GitHub**（源库 + Release） | [github.com/zxc663/shisan-xinuo-workflow](https://github.com/zxc663/shisan-xinuo-workflow) · [Releases](https://github.com/zxc663/shisan-xinuo-workflow/releases) | v3.1.0 | 权威源库；每版附 dist zip |
| 2 | **npm**（GitHub Packages） | [包页](https://github.com/zxc663/shisan-xinuo-workflow/pkgs/npm/shisan-xinuo-workflow) · `npm install @zxc663/shisan-xinuo-workflow` | 3.1.0 | 包为**私有可见性**，读取需 GitHub PAT（`.npmrc` 写 `//npm.pkg.github.com/:_authToken=<PAT>`）；**npmjs.org 未分发** |
| 3 | **Gitee**（镜像 + Release） | [gitee.com/zxc663/shisan-xinuo-workflow](https://gitee.com/zxc663/shisan-xinuo-workflow) · [发行版](https://gitee.com/zxc663/shisan-xinuo-workflow/releases) | v3.1.0 | 与 GitHub 同 commit/tag 双推；每版附 zip 附件 |
| 4 | **ClawHub**（OpenClaw 技能市场） | [clawhub.ai/zxc663/shisan-xinuo-workflow](https://clawhub.ai/zxc663/shisan-xinuo-workflow) · `openclaw skills install @zxc663/shisan-xinuo-workflow` | 1.0.19（平台侧递增号） | 平台侧版本号 1.0.x 递增，内容对应本仓版本；security scans 平台侧过审中 |
| 5 | **skills.sh**（Agent Skills 索引） | [skills.sh/zxc663/shisan-xinuo-workflow](https://skills.sh/zxc663/shisan-xinuo-workflow) · `npx skills add zxc663/shisan-xinuo-workflow` | 随 GitHub 同步 | 自动索引 GitHub 源库 |

配套动作：每版发行时 GitHub + Gitee 仓库简介（About）双端同步 PATCH。

## 快速体验 · Quick start

1. **装核心包**（任选其一）：
   - skills 市场：`npx skills add zxc663/shisan-xinuo-workflow`
   - 仓库直装：`git clone <repo>` → `pwsh scripts/install-skill.ps1`
   - npm（GitHub Packages）：`@zxc663/shisan-xinuo-workflow`——读取需 GitHub PAT（`.npmrc` 写 `//npm.pkg.github.com/:_authToken=<PAT>`）；npmjs.org 未分发
2. **重开一个新会话**（注入版本=会话创建时快照），输入 `zxc663` 自检：应回答「注入方式 / 已应用轮数 / 源库 vs 副本版本 / Base directory」。
3. **给它一个真实任务**：观察三个标志物——①每轮首产物是复述 + 状态行；②关键决策会先问（而不是先做）；③任务块末尾有 `GATE:` 单行与可复跑命令。
4. **想验行为面**：`python scripts/probe_runner.py --label demo l1-rename l3-delete`（探针默认落在系统临时目录，与仓库隔离）；**想验判据**：`python scripts/probe_runner.py --judge-selftest`（零 API 成本，正/负对照全过才算判据可用）。

## 安装与注入 · Install & inject

```powershell
# 1) 技能副本安装（默认识别平台技能目录；可选 -Link / -HardInject）
pwsh scripts/install-skill.ps1
pwsh scripts/install-skill.ps1 -Family            # 三包一起装

# 2) 平台注入（记忆层/规则层/配置层；先备份、合并不覆盖）
python scripts/deploy_injection.py --only codex,claude,trae,workbuddy,zcode
python scripts/deploy_injection.py --check --only zcode        # 注入副本验收

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
| 版本 | **v3.1.0**（已全渠道发行 2026-09-19；上一版 v3.0.0 2026-09-18） |
| 交付形态 | **三包**：核心 `shisan-xinuo-workflow` + 流程包 `shisan-xinuo-flows` + 角色包 `shisan-xinuo-roles` |
| 细则库 | **368 条 / 29 类**（编号至 `#369`；类数=分节数，单源断言） |
| 注入核心 | **≤ 6000 字符**（PowerShell 字符数 + Python code-point 双口径） |
| 完成块 | `GATE` **12 字段**：`level / v / cmd / exit / files / refs / errpath / lessons / exempt / caps / effort / stop_reason` |
| 行为面 | v3.1 全矩阵 **20/20 PASS**（判据 j2.4，**单批样本**）；v3.1.0 部署后实跑 **24 针 22 PASS**（scorecard 带被测副本/平台/判据指纹，全批指纹核验通过）；**判据金样本回归 21/21**（正例 8 / 负例 13）；同批输出两版判据重判：j1.0 18/20 → j2.2–j2.4 **20/20**（判据效应与行为方差分离）；口径构成见「验证与路测」表下脚注 |
| 判据可信度 | 判据版本化（j1.0→j2.4）+ `--judge-selftest` 金样本回归 + `--rescore` 同批重判 + 环境死亡行**证据签名**（provider 报错栈/空输出）+ GATE 形态分型（包级 12 / 子块简式 / 杂键） |
| 门禁 | `scripts/verify-release.ps1` **8 项**（A 内容锚点 / B hooks 三层 / C 版本一致 / D 泄漏红线 / E 正文净化 / F 索引完整性 / G 事实对账 / **H 判据自测**） |

## 仓库结构 · Repository layout

```text
.
├── skill/
│   ├── shisan-xinuo-workflow/    # 核心包：SKILL.md + references/ + templates/
│   ├── shisan-xinuo-flows/       # 流程包：9 类工作流分册 + 模板
│   └── shisan-xinuo-roles/       # 角色包：8 角色 + dispatch 矩阵
├── scripts/                      # 工具面：部署/同步/门禁/事实对账/审计/探针
├── docs/                         # 项目导航 + 计划 + 独立审查/审计报告 + 路测 scorecards
├── memory/                       # 单项目承载（本地档案，随 .gitignore 不入仓）
├── dist/                         # 发行 zip（版本化）
├── README.md · CHANGELOG.md · EVIDENCE.md · RELEASE-CHECKLIST.md
└── package.json · LICENSE
```

## 版本说明 · Editions

- **单版本（中文）**：Skill 本体只有中文一套，不维护多语种平行版本；README 中文优先 + 英文摘要。
- 版本号以 `package.json` 为准，三包 `SKILL.md` 的 `name/version` 与之一致（门禁断言）。

## 局限与代价 · Limitations

- **上下文成本真实存在**：注入核心常驻 ≤6000 字符（约 4-6K token）。你的窗口越小，收益/成本比越需要权衡。
- **不是"零错误保证"**：它降低的是"流程性失误"（漏问、漏验证、漏留档），不替代业务判断。
- **平台能力有差异**：无头模式（`-p`）注入面可能断裂；hooks 落盘面受平台持久化策略影响——因此行为结论**只认请求体/rollout 层证据**。
- **行为面存在方差**：同一场景 n=1 不可作结论（本项目用双击复采区分"缺口"与"噪声"）。
- **维护成本**：细则与副本需要同步；改模板 ≠ 改副本（hooks 指向仓外脚本的场景尤其明显）。

## 常见问题 · FAQ

**Q：它和"写一份很长的提示词"有什么区别？**
A：提示词是"希望被记住"；本 Skill 是流程结构 + 门禁 + 证据：分级选道、必问触发、`GATE` 可复跑、教训可检索。**规则在场 ≠ 规则被遵守**，前者靠提示词，后者靠机制。

**Q：会拖慢简单任务吗？**
A：L1 快速通道就是为此存在：一句话复述 + 最小修改 + 最小验证 + 一行汇报；承载与细则检索都可豁免（豁免须声明）。

**Q：升级后为什么行为没变？**
A：注入版本=会话创建时快照。升级副本后要**重开新会话**；`zxc663` 自检可确认副本版本与 Base directory。

**Q：能不能只装流程包/角色包？**
A：可以独立安装，但它们默认假定核心包的纪律面在场（`GATE`/状态行/判级），建议核心 + 目标包组合。

**Q：`GATE` 行会不会变成"应试作文"？**
A：设计上就是防这个：`GATE` 三挂靠（命令原文/退出码真值/文件真变）可被 `scripts/gate_audit.py` 外部抽检；自报与探针不符会被判**虚假 GATE** 并降级。`caps/effort` 这类自报字段要求配可核对痕迹。

**Q：数据与隐私？**
A：默认不联网、不外发；密钥类信息**绝不写入**代码/文档/提交/对话（门禁 D 项扫描发布物），泄露即轮换。

## 来源与依据 · Sources

- 细则库来源逐条标注（`*来源/晋升*` 字段），晋升遵循"同坑单项目两次 / 跨项目一次"经验回流制。
- 引用外部项目与资料登记在 [`docs/reference-sources.md`](docs/reference-sources.md)。
- 行为面数字来自本仓库自己的探针批与路测（`EVIDENCE.md` + `docs/roadtest-scorecards/`），不含推测数据。

## 版本历史 · Changelog

- **v3.1.0**（2026-09-19，**已发行**）：**判据可信度批**——判据版本化 j1.0→j2.4 + 金样本回归 21/21 + scorecard 指纹 + GATE 形态分型 + 环境死亡行证据签名 + 新增时序库聚合器与判据版本史；判据修订三处（回植「拒改取证」「可逆化+声明」两条合规路径、cap-web 检索痕迹对齐设计原文）、两处裁决（multi-task 维持 FAIL、`verify_trace`/`effort` 去自满足）与状态行 `confirm=` 形态补口（第三例判据滞后）；`verify-release` 增至 8 项（H 判据自测），细则 366→**368 条 / 29 类**（#368 判据即代码 + #369 L3 无人值守双合规路径）。无头全矩阵 **20/20**；v3.1.0 部署后无限循环实跑 **24 针 22 PASS**。
- **v3.0.0**（2026-09-18，**已全渠道发行**）：三包体系（核心/流程/角色）+ 细则治理（366 条/28 类，检索键 100% 覆盖）+ Token 精算机 + 反作弊与状态锚定 + `GATE` 12 字段 + 探针 harness 收编进仓 + 利用率处置批 + 五平台注入重部署。
- **v2.9.0**（2026-09-15/16）：独立审查修正批（P1×11 + P2×16 机制级）+ 安全基线 + 分级自审。
- **v2.6.0 – v2.8.0**：开工四步收敛、留档一档制、每轮复述强制、压缩接续与重载在用 Skills、系统级可逆配置判级。
- 完整沿革见 [`CHANGELOG.md`](CHANGELOG.md) 与 `git log`；发行回执见 [`RELEASE-CHECKLIST.md`](RELEASE-CHECKLIST.md)。

## 贡献者与许可 · License

- 作者：十三希诺（single-maintainer 项目，中文优先）。
- 许可：[MIT](LICENSE)。
- 反馈：issue / PR 欢迎；涉及规则语义的改动请附**行为面证据**（探针输出或真实会话片段），否则只按文档修正处理。
