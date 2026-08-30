---
name: shisan-xinuo-workflow-bilingual
description: "一句话定位：把任何工程任务强制按「调研驱动的 11 步主流程 + L1/L2/L3 封闭清单速判 + 双模式」推进的可审计 Agent 工程纪律工作流，核心纪律可平台无关硬注入。任何动手任务开工必用。One-line positioning: forces every engineering task through an auditable agent workflow — research-driven 11-step master sequence + L1/L2/L3 closed-list quick triage + dual modes, with platform-agnostic hard injection of the core. Use on any hands-on task."
license: MIT
compatibility: "Trae、Codex、Claude Code、Cursor、Windsurf、WorkBuddy 及任意支持 Agent Skills 标准的 CLI 编码智能体 / any CLI encoding agent supporting Agent Skills"
metadata:
  version: 1.19.0
  tags:
    - agent-skill
    - workflow-governance
    - engineering-discipline
    - quality-gates
    - auditability
    - codex
    - claude-code
    - trae
    - cursor
  author: zxc663
  edition: universal-bilingual
  homepage: https://github.com/zxc663/shisan-xinuo-workflow
  topics:
    - agent-skills
    - ai-agent-workflow
    - prompt-injection-defense
---

# 十三希诺通用 Agent 工作流 · Shisan Xinuo Agent Workflow

> **定位：流程为魂、规则为基。** 通用工作执行流程是灵魂（每个任务强制通用的推进骨架），编号纪律规则（`references/rules.md`）是地基（约束每步该守什么）；二者强耦合、相互依托——流程承载规则落地，规则约束流程执行，缺一不可。
> **Positioning: workflow is the soul, rules are the foundation.** The universal operating sequence is the soul (the mandatory skeleton every task advances along); the numbered discipline rules (`references/rules.md`) are the foundation (what each step must observe). Strongly coupled and mutually dependent — the workflow carries the rules into execution; the rules govern the workflow.

## 1. 何时使用 / 何时不用 · When to use / when NOT to use

**使用 Use**：任何工程任务（只要动手，就按第 2 节总纲推进）；纪律化执行、工作流治理、跨项目跨平台行为一致。本 Skill 加载时也执行第 3 节第 0 步（平台适配）。Any engineering task (advance along the master sequence in section 2); disciplined execution, workflow governance, consistent behavior across projects and platforms. Step 0 (section 3) also runs on load.

**不用 NOT for**：替代不了用官方文档学习框架 / 库 / API；项目自身约定优先于本 Skill。Not a substitute for learning a framework/API from its docs; the project's own docs always win where they conflict.
> **落地细则诚实说明 Honest note**：`details.md` 确实含绑定具体栈（Next.js / Prisma / Playwright 等）的真实工程经验——它是**踩坑日志**而非**技术教程**；流程 / 规则 / 门禁层与框架无关。details.md does carry stack-bound experience — treat it as a *pitfall log*, not a tutorial; the workflow/rules layers are framework-agnostic.

## 2. 总纲：任务主流程——强制通用推进骨架（唯一入口）· Master: task operating sequence — mandatory universal skeleton (single entry)

> **这是本 Skill 的核心，不是参考项。** 每步有「出口产物」，无产物 = 未完成 = 不得进入下一步；流程门禁可检查、可审计、不可跳步。
> **This is the core, not a reference.** Every step has an exit artifact — no artifact means unfinished; the gate is checkable, auditable, unskippable.

### 2.1 前置：状态澄清（目标 / 现状模糊时）· Prelude: status clarification (when goals / state are fuzzy)

用户理不清状态 / 目标不明 / 现状模糊时，先走「状态澄清」对话（`references/workflows.md` 澄清流程）：主导式逐层追问（一次一问）→ 摸清现状、拆解问题、锁定线索 → 产出【澄清纪要：目标 / 现状 / 约束 / 卡点】→ 确认后回到主流程第 1 步。When the user cannot sort out state or the baseline is fuzzy, first run the clarification dialogue: drive one-question-at-a-time interrogation → map state, decompose, lock the lead → produce a clarification memo (goal / state / constraints / blockers) → return to master step 1 after confirmation.

### 2.2 强制 11 步主流程（每步含出口产物）· Mandatory 11-step master sequence (exit artifact per step)

> **最铁铁律（复用铁律）The iron law (reuse)**：以最少的代码，实现最完整的功能和体验，并达到需求描述——就是最好的代码；能复用就复用，风格适配或二次开发都可以，**绝不自己自研组件**。The best code achieves the most complete function and experience with the least code while meeting the requirements; reuse whenever possible — style adaptation or secondary development both fine; never hand-roll your own components.
> **设计成本铁律 The design-cost iron law**：好的设计是昂贵的，但糟糕的设计成本更高——界面、交互、架构决策按「后期改造成本」评估，不按「当下实现成本」评估。Good design is expensive, but bad design costs more — evaluate interface, interaction, and architecture decisions by their future rework cost, not their immediate implementation cost.

| 步 Step | 动作 Action | 出口产物 Exit artifact（无则不进入下一步 must exist first） |
|---|---|---|
| 1 | 接收指令：第一性原理（本质 / 必要 / 惯性）Receive; first principles | 任务本质一句话 One-sentence essence |
| 2 | 经验库必读：按症状检索 Experience log first | 命中记录 Hit record |
| 3 | 调研实际资源：代码 + 环境 + 工作区 + Skill/MCP Survey actual resources | 现状事实清单 Status fact list |
| 4 | 联网调研·必须 Online survey (mandatory)：调研市面开源成熟项目 / 库 / 方案，收集**可验证可信信号**（stars / 下载量 / 维护 / 被采用 / 口碑 / 安全通告），不以「网上都说火」为依据；清单见 workflows.md §0.2 research mature open-source projects; collect verifiable trust signals, never "it's popular"; see §0.2。**离线 / 无网络是合法降级**：跳过远程调研、产物标注 `degraded-offline`、以第 3 步本地证据 + 经验库替代 offline is a legitimate degradation: mark `degraded-offline`, substitute local evidence + experience log | 市面方案调研记录 Market solution survey record（候选 + 可信信号 + 安全风险 + 降级 degradation） |
| 5 | 复用调研·铁律 Reuse survey (iron law)：能复用就复用，风格适配 / 二次开发皆可，绝不自研组件 reuse, adapt, or second-dev; never hand-roll | 复用结论 Reuse conclusion |
| 6 | 复述理解：目标 / 边界 / 验收 Restate understanding | 用户确认 User confirmation |
| 7 | 疑问必问：不理解 / 方向偏移→提问 Ask on doubt | 提问记录 Ask record |
| 8 | 产品视角 + 约束 + 分级 + 回滚点 Product-view + triage + rollback：触发反复审查/存量不足时**先做产品完善度诊断**（五问：功能逻辑/代码耦合/UI/互动流程/其他，见 §0.3）Product-polish diagnosis first on repeated-review triggers | 分级 + 回滚点记录 Triage + rollback record（+诊断报告 diagnosis report） |
| 9 | 规划与验收文档（强制双调研后）Plan & acceptance doc (after the mandatory dual survey)：工程师视角 + 产品经理视角双调研后产出详细规划文档（双调研结论 + 验收标准，§0.4）Dual survey (engineer + product-manager) then a detailed plan doc | 详细规划文档 Detailed plan doc（含双调研结论） |
| 10 | 执行：按分级；目标模式自主 + 预算 Execute per triage | 执行记录 Execution record |
| 11 | 自查与归档：验证→自查→文档→双写→提交 Self-check & archive | 验证结果 + 归档 Verification + archive |

**门禁 Gate**：进入下一步前上一步产物必须存在；无法产出的步须在任务记录写明理由，不得静默跳过。The previous step's artifact must exist before the next step; legitimate skips must record the reason, never silently.

### 2.3 L1 快速通道（判级先行）· L1 fast path (triage-first)

第 1 步接收后**先判级**：L1 常规（小改动、可逆、低影响）走 **L1 快速通道**：一句话复述 → 最小修改 → 最小验证 → 汇报，任务记录显式标注「L1 快速通道」（命名通道，非静默跳步）；L2 / L3 仍走完整 11 步（第 8 步再补全判级）。Triage right after step 1: L1 routine → fast lane (restate → minimal change → minimal verify → report), explicitly labelled "L1 fast path" in the record; L2/L3 keep the full 11 steps (triage finalized at step 8).

细节与分类型清单见 `references/workflows.md`。Details and per-task-type checklists in `references/workflows.md`.

## 3. 第 0 步：平台检测与注入 · Step 0: Platform detection & injection

1. **检测平台 Detect**（`references/platform-adaptation.md` 特征清单）
2. **定位该平台真实注入点 Locate the platform's REAL injection point**（platform-adaptation.md 第 2 节注入点表）：Trae `~/.trae-cn/user_rules/*.md`（用户全局，文件存在即每会话自动注入）或 `.trae/rules/project_rules.md`；Claude Code `~/.claude/CLAUDE.md` 或项目 `CLAUDE.md`；Codex `AGENTS.md`；Cursor `.cursor/rules/*.mdc`；Windsurf `.windsurfrules`。只写应用从不读取的工作区文件是**无效的**。A file written only into a folder the app never reads is useless.
3. **询问注入模式 Ask the injection mode**：**按需（默认）on-demand (default)**——注入点只写约 9 行精简纪律 + 回指本 Skill；**强制注入（硬加载）forced injection (hard-load)**——把 `references/injection-core.md` 核心全文写入该平台注入点（先备份、合并不覆盖），工作流每会话无条件在场、不依赖模型自觉加载（每会话固定约 2-3K token）。**不要用「每会话完整读 SKILL.md」弱指令实现强制注入——模型不会可靠执行，必须直接写入核心全文。** Do NOT implement forced injection as "read the full SKILL.md every session" — models do not reliably execute extra reads; write the core text itself. 无提问工具默认按需并告知。
4. **选定提问机制 Pick asking mechanism**（第 4 节降级链）
5. **校验生效 Verify**：复述生效要点（平台 / 注入点 / 注入模式 / 提问工具），未确认生效不得宣称成功，未完成不得开工。Restate the active essentials (platform / injection point / mode / asking tool) before starting.

## 4. 关键必问协议 · Ask-before-acting protocol

影响重大的决策必须在行动前与用户确认。触发：方向不明或歧义、需求冲突、权限/密钥、破坏性操作（删除/迁移/覆盖/发布）、架构选型、范围扩大、方案分歧，**及对需求理解不尽确定**。Consequential decisions must be confirmed before acting. Triggers: ambiguity, **not-fully-certain understanding**, conflict, permissions/secrets, destructive ops, architecture, scope, proposals. **问清楚比问少了更重要，理解需求比模糊执行更重要 / Asking clearly beats asking less; understanding the need beats executing it vaguely.**

**降级链 Downgrade chain**：① 平台原生提问工具 Native asking tool；② 不可用 → 结构化文本协议（a 理解 b 选项优缺点 c 风险后果 d 推荐），**结束回合等待** end the turn and wait。L1 常规不问；L3 必问。**偏好记忆 Preference memory**：用户确认选择（技术栈/语言/风格）后写入 memory/「用户偏好」字段，同类场景直接采用不再重复问；只覆盖已确认重复偏好，绝不覆盖密钥与破坏性操作。Do not over-ask on L1; always ask on L3; confirmed preferences go to the memory file and are reused, never secrets or destructive ops.

**冲突仲裁序 Conflict arbitration order**——两个指令源相抵触时按固定顺序取最优、**只保留胜者**（删败方引用，绝不两听、不折中）：① 用户/项目纪律（项目规则文件、已确认 D 系决策、设计契约）the brief wins → ② 平台硬注入核心 injected core → ③ 当前设计稿/brief → ④ 本 Skill 默认值 this skill's defaults → ⑤ 其他 Skill 默认 other skills' defaults。任务记录留一行仲裁（来源 A vs B → 采用 X，因为…）；同一理由裁决两次即升格为常设决策，写入 `memory/preferences.md`。When two sources disagree, follow this fixed order, keep only the winner, log one arbitration line; a conflict resolved twice for the same reason becomes a standing preference.

## 5. 双模式与任务分级 · Execution modes & task triage

| 模式 Mode | 触发 Trigger | 行为 Behavior |
|---|---|---|
| **普通 Normal**（默认） | 无关键词 | 关键决策必问；**关键决策即时复述确认 + 决策审计归档**（重要决策即时落盘供可解释）。Ask before consequential decisions; **immediately restate key decisions to the user for confirmation and log them to the decision-audit archive**. |
| **目标 Goal mode** | `目标：`/`目标模式`/`无人值守`/`goal mode`/`unattended` | 按计划自主执行；**暂停仅两情形——重大决策（L3）/ 严重阻塞**；其余重要决策「先调研→按第一推荐推进→完整归档」；**每里程碑强制留档**；**回滚点本地备份、默认不 git push（省宽带+token）**；**本地快照就绪→破坏性/修改类可安全执行（L3 除外，仍暂停）**；密钥与破坏性操作仍暂停等待。Autonomous per plan; pause only for major decisions (L3) / severe blocking; every milestone forces a record; rollback points go local backup, no default git push; a local snapshot ready → destructive/modification ops safe (L3 excepted); secrets & destructive ops pause. |
| **安静 Quiet mode** | `安静模式`/`quiet`/`quiet mode` | L1 只汇报结果（隐藏中间推理/调研展示）Report only results on L1; L2/L3 unchanged; secrets & destructive still ask |

目标模式附加：执行前写计划（范围/风险/预算）、子任务按文件边界拆分、超预算自动停、交付复盘 + 待确认清单。Goal mode: plan first, budgets, file-boundary split, auto-stop, retrospective.

| 级别 Level | 判定 Criteria | 普通 Normal | 目标 Goal |
|---|---|---|---|
| L1 常规 routine | 小改动、可逆、低影响 | 直接做 do | 直接做 do |
| L2 中风险 medium | 新功能、多文件、跨模块 | 记录后做，汇报关键点 record & report | 按计划执行，节点记录 per plan |
| L3 高风险 high | 密钥/权限/删除/迁移/发布/架构 | **先问再做 ask first** | **暂停留档等用户确认（即便本地备份就绪也不豁免——备份回滚覆盖不了对外影响与权限/安全面）；密钥与破坏性操作暂停留档等用户 Pause, log, and wait for user confirmation (not waived even when a local backup is ready — it cannot cover external impact and the permissions/security surface); secrets & destructive ops pause, log, wait** |

**判级速查（10 秒定论，一句话即止，禁止展开论证）Triage quick reference**：L3 封闭清单（仅 6 项，清单外一律不是 L3，不得自行扩展）：密钥/权限｜数据删除｜数据或服务迁移｜对外发布｜架构选型｜超预算破坏性操作。L1 速判：改名、文案、格式、单行修改等可逆小改动直接做；L2：新功能、多文件、跨模块，记录后做。10 秒判不了级默认按 L2 直接推进；判级结论一句话即止，除命中 L3 清单外判级本身不追问用户、不展开分析。Closed list of 6 for L3 (nothing outside it is L3); L1 = reversible small changes, just do them; cannot triage in 10s → default L2, one-sentence verdict, no arguing.

**判级同步链 Triage sync chain（三处一致 unanimous in three places）**：本块是 L3 封闭清单与 L1/L2 速判的**唯一权威源**；`injection-core.md` 因注入环境自包含必须保留全文、且被部署为平台全局 `user_rules` 写入副本——**本块 → `injection-core.md` → 已注入的平台全局副本三级必须同步**；改判级先改本块，再同步 injection-core，最后重新部署到注入点，三处保持一致。This block is the single authoritative source; `injection-core.md` must keep the full text (injection is self-contained) and is deployed as a platform-global copy — this block → injection-core → the injected global copy must stay consistent. To change triage, change here first, then sync injection-core, then redeploy.

## 6. 最小闭环交付（第 11 步交付原则）· Minimal closed-loop delivery (step-11 principle)

理解 → 最小修改（复用优先）→ 最小验证 → 交付成品；不交半成品、不留占位、绝不假实现。Understand → minimal change (reuse first) → minimal verification → deliver finished work; no placeholders, never fake completion.

## 7. 质量门禁与回滚 · Quality gates & rollback

提交前审查者视角重读 diff、重跑验证、文档与代码同批；重大修改/不可逆操作前必建回滚点（commit/stash/快照）；**原子操作锁（L3 破坏性操作）**：删除/迁移/覆盖写/发布类操作先输出命令清单、结束回合等用户确认再执行；对外发布先批准 + 约 30 分钟观察期。Review the diff, re-run validation, ship docs with code; rollback point BEFORE major changes; **atomic-operation lock**: output the command list and wait for user confirmation before L3 destructive ops; publish after approval + observation window.

## 8. 易错点 · Gotchas

- **判级内耗 Triage burnout**：琐碎判级一句话定论——改名 / 文案 / 格式类一律 L1 直接做；L3 只认第 5 节封闭清单，清单外不构成 L3。为判级展开论证或反复纠结是 token 浪费的最大来源之一。Settle trivial triage in one sentence; L3 honors only the closed list in section 5.（判级 ≠ 理解确认 Triage ≠ understanding confirmation——以第 5 节为权威，authoritative there.）
- **同会话重载是纯浪费 Same-session reload is waste**：当前会话已加载的 Skill / 引用，同会话下一任务不再重读；「每会话重载」适用于跨会话，仅压缩后 / 显式要求 / 源变更时重读。Skills already loaded in this session are not re-read for the next task in it; reload only after compaction, explicit request, or source change.
- **流程不可跳步**：调研（第 3 步）与复用调研（第 5 步）最常被跳过，是最常见违规。The sequence is unskippable; survey steps are the most-skipped.
- **反复审查先做产品完善度诊断**：以产品角度定位缺陷（功能逻辑/代码耦合/UI/互动流程/其他，§0.3），别只查代码正确性。Diagnose by product dimension before code.
- **触发关键词是活开关**：目标模式关键词会静默改变决策模型，每条消息都要检查。Goal-mode keywords are live switches.
- **绝不覆盖已有规则文件**：备份 + 合并。Never overwrite rule files — backup + merge.
- **代码与实测为准**：用户想法与代码冲突时直说。Code and measurements win.
- **无原生提问工具**：用文本协议并结束回合，绝不埋头直冲。Ask first, act never.
- **过度提问毁采纳率**：L1 直接做，L3 必问。Act on L1, ask on L3.
- **Skill 加载 ≠ 任务开工**：第 2 节总纲强制执行。Master sequence is mandatory.
- **密钥绝不落盘**：提交前扫描，泄露立即轮换。Secrets never in code/docs/chat.
- **结论即时落盘**。Keep records at analysis time.

## 9. 引用地图 · Reference map

| 文件 File | 何时加载 When to load |
|---|---|
| `references/injection-core.md` | 第 3 节强制注入（硬加载）时——平台无关核心模板，全文写入检测到的平台注入点 Section 3 forced injection — the platform-agnostic core template, written in full into the detected injection point |
| `references/platform-adaptation.md` | 第 3 节平台检测；提问降级链；结构化协议全文 Section 3 detection; asking chain; protocol |
| `references/rules.md` | 编号纪律（地基）The numbered-rule discipline (foundation)；引用规则编号 / 需查原文时 a numbered rule is cited |
| `references/skill-usage.md` | Skill 能力发现 / 注册机制 + 加载决策路由 + 渐进 / 完整读取分类；任务涉及 Skill 选用、前端 / 设计类任务、本地无 Skill 获取、弱模型处理时加载 Skill capability discovery / registration + load-decision routing + progressive-vs-full-read classification; load when choosing a Skill, doing front-end/design work, getting a Skill when none is local, or weak-model handling |
| `references/workflows.md` | 总纲细节、澄清流程、9 类工作流、复用五问、质量门禁 Master details, clarification, task types, reuse, gates |
| `references/details.md` | 落地细则（工程规范 / 具体做法）13 类：环境/前端/数据库/测试/API/部署运维/代码质量/Git/会话·备份·治理/深挖补充/铁律纪律/源项目深挖 Landing details, 13 categories (env/frontend/DB/testing/API/ops/code quality/git/sessions/deep-dive/iron laws/source-project/blog backflow), load by category |
| `references/security.md` | 密钥红线、应急、回滚细节 Secrets, incident, rollback, prompt-injection, supply-chain |
| `references/never-list.md` | 永不清单（明线）Never list — 开工/提交/风险前自查 quick self-check before start/commit/risky ops |
| `templates/workspace-memory-template.md` | 初始化工作区 `memory/` 骨架（state / experience / preferences / task-log），会话开工自动创建时用它 Initialize the workspace `memory/` skeleton (state / experience / preferences / task-log); use it when auto-creating on session start |

**上下文缺失自检（压缩不可感知）Context-loss self-check**：显式信号（用户提示重载/平台重置）→ **立即按重载顺序执行 Reload sequence**：①重读本 SKILL.md；②重读记忆文件 `memory/`；③重读当前步骤引用；④向用户复述任务与验收再继续；关键节点（开工/提交/重大决策）先默写核心要素（总纲步序、模式、回滚、必问），复述不全即重读。On explicit reload/reset signals: ① re-read SKILL.md → ② re-read memory file → ③ re-read needed references → ④ restate task + acceptance to the user; self-check core elements (master steps, mode, rollback, ask) before key milestones.

**加载纪律 Loading discipline**：只在（a）命中引用行内的触发症状、（b）走到点名步骤、（c）用户显式要求时打开引用，绝不预载；某份引用影响决策时在任务记录留一行引用。Open a reference only on its trigger symptom, the step naming it, or explicit user request — never preload; cite it one-line in the task record when it changed a decision.

## 10. 留档与知识纪律（摘要）· Records & knowledge discipline (summary)

任务记录随会话维护（理解 → 验收 → 决策 → 结果），**每条记录附带平台会话 id（暴露时）与产出提交哈希**（使会话→提交→质量可追溯），各步出口产物随记录留档；会话结束双写知识（知识版 + 个人版）；经验库开工必读（按症状检索，路径项目自定）；**记忆文件协议（外部化长期记忆）**：项目约定位置维护 `memory/`（当前目标 / 决策 / 约束 / 进度 / 踩坑，一屏内），关键节点与上下文 40-60% 前写入，压缩 / 重置 / 会话开始**先读再继续**；**用户偏好**：memory/ 维护「用户偏好」字段（已确认的技术栈/语言/风格），会话开始读取、同类决策复用不再重复问（细节见 §11 与 `references/workflows.md`）；文档与代码同批、归档前有现行等价物。Task record per session (carrying session id + commit hashes for traceability) with step artifacts; dual-write knowledge at session end; experience log mandatory at start; **memory-file protocol**: maintain `memory/` per project convention, write at milestones & before 40-60% context, read first after compaction/reset; **user preferences**: keep confirmed choices in the memory file and reuse them to avoid re-asking; docs ship with code. **配套模板 Templates**：规划 / 验收 / 任务记录 / 复盘 / 回滚点 / 提示词预算模板 + 会话钩子（`templates/hooks/`）+ 审查子代理（`templates/agents/`）+ 工作区记忆骨架（`templates/workspace-memory-template.md`）位于 `templates/`（复制填写）。Templates (plan/acceptance/task-record/retrospective/rollback/prompt-budget), hooks, review sub-agents, and the workspace-memory skeleton live in `templates/` (copy & fill).

## 11. 上下文预算与工作区 `memory/` 约定 · Context budget & workspace `memory/` convention

**上下文预算法 Context budget（先定序，防污染 order first, avoid pollution）**——把「读哪些、何时读」写死，避免无脑把整本砸进上下文：

- **常驻（必读，小）Resident (small)**：本核心——判级速查 / 主流程 / 必问 / 红线 / 留档。Triage / master sequence / must-ask / red lines / records.
- **开工读（工作区 `memory/`，存在才读，一屏内）Session-start (workspace `memory/`, one screen)**：按「state → experience → preferences → task-log」顺序扫一遍；`experience` 按当前症状检索命中段。Scan in order; search `experience` by symptom only.
- **按需（到步骤才读）On demand**：完整 Skill 的 `references/`、历史 `task-log/`；不预载全部引用。Do not preload all references.
- **结束更新（最小追加）End-of-session (minimal append)**：见「完成后更新序」。See the completion update order below.

**工作区 `memory/` 约定（跨会话记忆统一归档）Workspace `memory/` convention**：项目根 `memory/`——任务记录 / 踩坑库 / 偏好 / 会话状态统一归档，**任何会话（含下一个 AI）开工必扫该目录**，不存在则自动创建骨架（模板 `templates/workspace-memory-template.md`）。Project root `memory/` — task records / pitfall log / preferences / session state archived in one place; **any session (incl. the next AI) must scan it on start**; auto-create the skeleton from the template if missing:

- `memory/state.md`：当前目标 / 已做决策 / 约束 / 进度 + 下一步（一屏内，秒读）。Goal / decisions / constraints / progress + next (one screen).**骨架非日记——硬上限约一屏（~10KB）**：开工扫描发现超一屏，先把里程碑史迁入 `memory/archive-YYYY-MM.md` 再开工（移动非删除）Skeleton, not diary — hard cap one screen (~10KB); archive milestone history before starting when over。
- `memory/experience.md`：踩坑经验库（症状→根因→解决→预防）。Pitfall log (symptom→cause→fix→prevention).
- `memory/preferences.md`：已确认偏好（技术栈/语言/风格）。Confirmed stack / language / style preferences.
- `memory/task-log/`：任务记录，`YYYY-MM-DD-名称.md`。Task records (date-named).
- 若本项目真实业务恰用 `memory/`，可在项目规则文件内改 `.agent-records/`（唯一合法覆盖点）。If the project's business uses `memory/`, override to `.agent-records/` in the project rule file (the only legal override point).
- **经验回流（双击晋升制）Experience backflow (two-strike promotion)**：同一踩坑单项目两次 / 跨项目各一次（症状符、根因同）→ 提炼「症状→根因→解决→预防」提交进本 Skill `references/details.md`；回流是稳定教训的晋升，首例噪音永不进 Skill。A pitfall confirmed twice in one project or once in two gets promoted into the skill's details.md — promotion of stabilized lessons only.
- memory 是「状态层 + 踩坑层」，完整细则仍在 `references/` 按需加载，互不替代。`memory/` is the state + pitfall layer; full details still load on demand from `references/`.

**完成后更新序 Completion update order（结束收尾，避免污染）**——最小验证后依序收尾：

1. **最小验证 + 自查**。Minimal verification + self-check.
2. **更新 `memory/task-log/<日期>-<名称>.md`**：理解 → 验收 → 决策 → 结果。Understanding → acceptance → decisions → result.
3. **更新 `memory/experience.md`**：新踩坑或重复坑（症状→根因→解决→预防）。Distill new or recurring pitfalls.
4. **更新 `memory/preferences.md`**：偏好写入后**主动向用户复核大类方向**（技术栈 / 语言 / 风格），偏离按其修正；密钥与破坏性意图绝不写入。After writing preferences, actively remind the user to re-check the broad direction; secrets never go in.
5. 文档与代码同批提交；会话结束提炼 1-5 条可复用知识点（默认 3）。Docs + code in the same batch; distill 1-5 knowledge points (default 3).


## Sync Additions · v1.12-1.18 (additive sync · 2026-08-30)
> 与英文主交付物增补同步（增补制）；主交付物为权威全量。


### 增补节 · v1.12-1.18（增补制 · 2026-08-30 同步）
> 与英文主交付物（v1.16 起执行化全文）保持增补同步；主交付物为权威全量，本版为其要点增补。

GATE 完成块：每任务块一行 `GATE: {v,cmd,exit,files,lessons,exempt}`（可复跑工件>自述；验收权在用户；approval:never 只豁免工具级审批不豁免确认）。
会话状态面（结束，给用户复核的一致性报告）：版本/细则命中取证行（grep，0 照报 0）/上下文预算（150-200K 提醒压缩）/版本一致性（副本 vs 源库）/未验证待办。
产品视角五问（L2/L3 计划默认强制）：诉求拆解/被否候选≥1/返工成本/边界清单/验收 3-5。
调研矩阵：项目严格度 S3(生产/对外/安全/金融/多协作者/点名)/S2(默认)/S1(宽松) × 规模 L1 免/小模块 L2(≤2 文件→代码级+复用前文；联网仅新技术新依赖)/普通 L2·L3 全量；S3×小模块=仍全量。
前文复用（步骤 2.5）：同会话已确认要点显式复用+一行引用，不重跑。
无 /plan 的 L2 入口：复述+3 验收+判级一句；S3 必问。
ExitPlanMode 四件套：验收/判级/回滚点（或明示基线）/边界清单。
新项目 bootstrap：docs/project-info.md 六节（架构/目标/模块真实状态表/调研导航/参考资源/复述签章）。
用户偏好集（默认级）：先沟通再动手（空答→调研+待确认标注，绝不当批准）/读懂再动手+三步复述/自主决定留档/YAGNI 最小改动/错误先根因（禁绕过隐藏）/真实运行+真实用户走一遍/交付五查。
经验强制预读：experience-mustread.md TOP≤10（≥3 次或高返工晋升；先于症状检索）。
上下文管理：>~40 行输出归档留摘要；子代理只留结论；模糊先重取；每~5 块盘点。
时间戳：`YYYY-MM-DD HH:mm:ss`（秒级必填；日级=不完整）；活头部校验；记录>120 行或>3 块开新文件。
日志对接（项目有日志模块时）：设计期「日志对接行」+ catch 三件套（记日志+降级提示+审计）+ 五查含日志；console/空 catch 零容忍。
会话五条：拒绝→偏好提炼闭环（被拒=金矿）；会话看板（done/进行/待确认/评审点）；停点三检查（需输入/全完/风险发布面）；活头部同步；记录上限。
复述增强 RE：关键决定即时「决定X｜依据…｜影响…」；块尾总复述（子复述仅提炼要点）。
A4 决策改判/A5 验收漂移：同栏留档（原决定+改判原因+触发；验收变更=用户确认或记「范围变更」）。
彩蛋 zxc663：回复「已应用，注入方式：［按需/硬注入］，已应用 N 轮会话｜源库 vX vs 副本 vY」（纯自检）。
自更新：`python scripts/syncer.py` 三路合并（体检/备份/迁移 user-notes/ 覆盖/双落盘）；user-notes+memory+.bak 永不碰；手动改副本只许写 user-notes/。

> 与英文主交付物（v1.16 起执行化全文）保持增补同步；主交付物为权威全量，本版为其要点增补。

GATE 完成块：每任务块一行 `GATE: {v,cmd,exit,files,lessons,exempt}`（可复跑工件>自述；验收权在用户；approval:never 只豁免工具级审批不豁免确认）。
会话状态面（结束，给用户复核的一致性报告）：版本/细则命中取证行（grep，0 照报 0）/上下文预算（150-200K 提醒压缩）/版本一致性（副本 vs 源库）/未验证待办。
产品视角五问（L2/L3 计划默认强制）：诉求拆解/被否候选≥1/返工成本/边界清单/验收 3-5。
调研矩阵：项目严格度 S3(生产/对外/安全/金融/多协作者/点名)/S2(默认)/S1(宽松) × 规模 L1 免/小模块 L2(≤2 文件→代码级+复用前文；联网仅新技术新依赖)/普通 L2·L3 全量；S3×小模块=仍全量。
前文复用（步骤 2.5）：同会话已确认要点显式复用+一行引用，不重跑。
无 /plan 的 L2 入口：复述+3 验收+判级一句；S3 必问。
ExitPlanMode 四件套：验收/判级/回滚点（或明示基线）/边界清单。
新项目 bootstrap：docs/project-info.md 六节（架构/目标/模块真实状态表/调研导航/参考资源/复述签章）。
用户偏好集（默认级）：先沟通再动手（空答→调研+待确认标注，绝不当批准）/读懂再动手+三步复述/自主决定留档/YAGNI 最小改动/错误先根因（禁绕过隐藏）/真实运行+真实用户走一遍/交付五查。
经验强制预读：experience-mustread.md TOP≤10（≥3 次或高返工晋升；先于症状检索）。
上下文管理：>~40 行输出归档留摘要；子代理只留结论；模糊先重取；每~5 块盘点。
时间戳：`YYYY-MM-DD HH:mm:ss`（秒级必填；日级=不完整）；活头部校验；记录>120 行或>3 块开新文件。
日志对接（项目有日志模块时）：设计期「日志对接行」+ catch 三件套（记日志+降级提示+审计）+ 五查含日志；console/空 catch 零容忍。
会话五条：拒绝→偏好提炼闭环（被拒=金矿）；会话看板（done/进行/待确认/评审点）；停点三检查（需输入/全完/风险发布面）；活头部同步；记录上限。
复述增强 RE：关键决定即时「决定X｜依据…｜影响…」；块尾总复述（子复述仅提炼要点）。
A4 决策改判/A5 验收漂移：同栏留档（原决定+改判原因+触发；验收变更=用户确认或记「范围变更」）。
彩蛋 zxc663：回复「已应用，注入方式：［按需/硬注入］，已应用 N 轮会话｜源库 vX vs 副本 vY」（纯自检）。
自更新：`python scripts/syncer.py` 三路合并（体检/备份/迁移 user-notes/ 覆盖/双落盘）；user-notes+memory+.bak 永不碰；手动改副本只许写 user-notes/。

- **v1.19（上下文管理四修复）**：两步式（读→提炼→落盘→只留指针+摘要）；盘点按信号触发；会话级上下文账本（入状态面）；重置点（5 块回引或成本 2×→建议新会话）；信息单一源。
