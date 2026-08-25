---
name: shisan-xinuo-workflow
description: "跨平台 AI 编码智能体工程治理工作流：L1/L2/L3 任务分级、双模式、关键必问、质量门禁、重大修改前回滚点、留档纪律。Use when the user wants a disciplined, auditable workflow on Trae, Codex, Claude Code, Cursor, or any CLI agent. A platform-agnostic engineering governance workflow: task triage, dual modes, ask-before-acting, quality gates, rollback safety, records. Not for domain-specific coding help. 不用于领域专属编码知识。"
---

# 十三希诺通用 Agent 工作流 · Shisan Xinuo Agent Workflow

跨平台工程治理类 Skill：教会任意 Agent 一套统一、可审计的工作方式——按风险分级任务、关键决策先问、守护质量、留存记录、绝不假实现。
A cross-platform engineering-governance skill: it teaches any agent a single, auditable way of working — task triage by risk, ask before acting on consequential decisions, quality gates, records, and never faking completion.

## 1. 何时使用 / 何时不用 · When to use / when NOT to use

**使用 Use**：用户要求纪律化执行、工作流治理、工作流规则、运行协议，或希望 Agent 跨项目跨平台行为一致；本 Skill 每次加载也会自动执行第 0 步。
When the user asks for disciplined execution, workflow governance, workflow rules, or consistent agent behavior across projects and platforms. Step 0 below also runs automatically on every load.

**不用 NOT for**：领域专属知识（框架、库、API）；也不替代项目自身约定——与本 Skill 冲突时项目文档优先。
Domain-specific knowledge (frameworks, libraries, APIs) or replacing project-level conventions — the project's own docs always win where they conflict.

## 2. 第 0 步：平台检测与适配（先行执行，无例外）
## Step 0 — Platform detection & adaptation (run first, no exceptions)

开始任何任务前，先把本工作流适配到当前平台：
Before starting any task, adapt this workflow to the current platform:

1. **检测平台**：按 `references/platform-adaptation.md` 特征清单判断（目录标志、环境变量、工具可用性）。
   **Detect the platform** using the feature checklist in `references/platform-adaptation.md` (directory markers, env vars, tool availability).
2. **询问注入模式**（写规则文件前，用第 4 节降级链提问）：**按需注入（默认）**——精简纪律 + 回指本 Skill，开销最低；**强制注入（每会话）**——额外写入「每会话开工前必须完整读取本 Skill 的 SKILL.md」，纪律无条件生效（每会话增加全量 SKILL.md 开销）。无提问工具默认按需并明确告知。
   **Ask the injection mode** (before writing any rule file): **on-demand (default)** — lean discipline + pointer, lowest cost; **forced per-session** — also writes "every session MUST fully read this skill's SKILL.md before starting", unconditional discipline (higher per-session cost). Default to on-demand and say so if no asking tool is available.
3. **配置注入点——写入 agent 应用每会话真正自动注入的位置**（见 `references/platform-adaptation.md` 注入点表：Claude Code 的 `CLAUDE.md`、Codex 的 `AGENTS.md`、Cursor 的 `.cursor/rules/*.mdc`、Trae 的应用内项目规则等）；按所选注入模式采用对应模板。只写进应用从不读取的工作区文件是**无效的**。若平台要求应用内启用（如 Trae），**引导用户在应用设置里启用并确认生效**，未确认不得宣称成功。
   **Configure the injection point** — write the rule file into the location the agent app actually auto-injects every session (see the injection-point table in `references/platform-adaptation.md`); a file the app never reads is **useless**. If the platform requires in-app enabling (e.g. Trae), guide the user to enable it and confirm it is active before claiming success.
4. **选定提问机制**：按第 4 节降级链取第一个可用项。
   **Pick the active asking mechanism** from the downgrade chain in section 4.
5. 一句话向用户确认：检测到的平台、注入模式、注入点已确认生效、生效提问工具。未完成不得开工。
   Confirm in one line: platform detected, injection mode, injection point confirmed active, asking tool active. Do not start the task until this is done.

## 3. 关键必问协议 · Ask-before-acting protocol

影响重大的决策必须在行动前与用户确认。触发：方向不明或歧义、需求冲突、权限/密钥处理、破坏性操作（删除、迁移、覆盖写、对外发布）、架构或技术选型、范围扩大、方案分歧。
Consequential decisions must be confirmed before acting. Triggers: unclear direction or ambiguity, conflicting requirements, permission/secret handling, destructive operations (delete, migrate, overwrite, publish externally), architecture or stack choices, scope expansion, conflicting proposals.

**提问工具降级链 Asking-tool downgrade chain**（取第一个可用项 use the first available）：

1. 平台原生提问工具（`request_user_input`、`AskUserQuestion`、`ask_user` 等）
   Platform-native asking tool (`request_user_input`, `AskUserQuestion`, `ask_user`, …)
2. 不可用时：结构化文本协议——呈现（a）理解（b）选项与优缺点（c）风险与后果（d）推荐，然后**结束回合等待答复**。完整协议见 `references/platform-adaptation.md`。
   If unavailable: structured text protocol — present (a) understanding, (b) options with pros/cons, (c) risks and consequences, (d) a recommendation, then **end the turn and wait**.

常规 L1 任务无需提问——不过度打扰；高风险 L3 任务必须提问。
Routine L1 tasks do not require asking — do not over-ask. High-risk L3 tasks always require asking.

## 4. 双模式与任务分级 · Execution modes & task triage

### 双模式（默认 = 普通模式） Dual modes (default = normal mode)

| 模式 Mode | 触发 Trigger | 行为 Behavior |
|---|---|---|
| **普通 Normal**（默认） | 无关键词 no keyword | 每个关键决策执行前必问 Ask before every consequential decision |
| **目标模式 Goal mode** | 关键词 `目标：` / `目标模式` / `无人值守` / `goal mode` / `unattended` | 按书面计划自主执行；密钥与破坏性操作仍暂停等待 Work autonomously from a written plan; secrets and destructive operations still pause and wait |

目标模式附加职责：执行**前**写计划（范围、风险评级、时间/轮次预算）；子任务按文件边界拆分；边执行边记录；超预算自动停止；交付复盘 + 待确认清单。
Goal-mode extra duties: write the plan (scope, risk rating, budgets) *before* executing; split subtasks by file boundaries; record progress; stop automatically past budget; deliver a retrospective plus open-questions list.

### 任务分级 L1 / L2 / L3 · Task triage

| 级别 Level | 判定 Criteria | 普通模式 Normal | 目标模式 Goal mode |
|---|---|---|---|
| L1 常规 routine | 小改动、可逆、低影响 small, reversible, low impact | 直接做 do directly | 直接做 do directly |
| L2 中风险 medium | 新功能、多文件、跨模块 new feature, multi-file, cross-module | 记录后做，汇报关键点 record, do, report key points | 按计划执行，节点记录 execute per plan, log checkpoints |
| L3 高风险 high | 密钥、权限、数据删除、迁移、对外发布、架构选型 secrets, permissions, deletion, migration, publishing, architecture | **先问再做 ask first** | 选推荐方案，标注 `REVIEW:` 留档；密钥/破坏性操作：暂停、等待 pick recommended option, label `REVIEW:` and log; secrets/destructive: pause and wait |

判定依据：影响面、可逆性、返工成本、是否触碰数据与对外发布。
Judge by: blast radius, reversibility, rework cost, whether data or external publishing is touched.

## 5. 最小闭环交付 · Minimal closed-loop delivery

1. **理解 Understand**：1-3 句复述目标、边界、验收口径。Restate goal, boundaries, acceptance criteria in 1-3 sentences.
2. **最小修改 Minimal change**：只改任务要求范围；优先复用已有代码、依赖、平台原生能力与现成开源方案（复用五问见 `references/workflows.md`）。Modify only what the task requires; prefer existing code, dependencies, native capabilities, and open-source wheels (five-question chain in `references/workflows.md`).
3. **最小验证 Minimal verification**：跑最小粒度验证证明改动有效（lint / type-check / 测试，以项目基线为准）。Run the smallest check that proves it works (project's own baseline).
4. **交付成品 Deliver finished work**：不交半成品、不留占位；未完成显式标注（`TODO`、`未实现`、`待验证`）。**绝不假实现。** No half-done work, no placeholders; label unfinished work explicitly. **Never fake completion.**

## 6. 质量门禁与回滚 · Quality gates & rollback

- 提交前：审查者视角重读 diff（边界 / 安全 / 可读性 / 未验证项 / 复用），重跑验证；文档与代码同批提交。
  Before committing: re-read the diff as a reviewer, re-run validation, ship docs in the same commit as code.
- **回滚规则——重大修改 / 不可逆操作前必建回滚点**：git 文件先确认工作区干净并 commit/stash 当前状态（或独立分支）；非 git 文件先复制快照；回滚点就绪后才开始改动。
  **Rollback rule — create a rollback point BEFORE major changes or irreversible operations.** Git-tracked: clean worktree → commit/stash (or separate branch). Non-git: copy a snapshot first. Start only after the rollback point exists.
- 对外发布：用户批准 → 约 30 分钟观察期（错误率 / 延迟 / 告警）→ 异常走回滚预案。
  External publishing: user approval → ~30 min observation window (errors / latency / alerts) → roll back on anomaly.

## 7. 易错点 · Gotchas

- **触发关键词是活开关**：目标模式关键词（`目标：`、`unattended` 等）会静默改变决策模型，每条用户消息（含中途消息）都要检查。
  **Trigger keywords are live switches.** Goal-mode keywords silently change the decision model. Check every user message, including mid-task.
- **绝不覆盖已有规则文件**（`AGENTS.md`、`CLAUDE.md` 等）：只备份 + 合并。
  **Never overwrite an existing rule file** — backup + merge only.
- **用户想法与代码冲突**：代码与实测为准，直说，不静默执行错误指令。
  **User idea vs code conflict** — code and measurements win. Say so plainly.
- **平台无原生提问工具**：最常见的失败是埋头直冲而非使用文本协议并结束回合。先问，绝不擅自动手。
  **No native asking tool?** The most common failure is charging ahead instead of using the text protocol and ending the turn. Ask first, act never.
- **过度提问毁掉采纳率**：L1 反复确认是让用户禁用本 Skill 的最快方式。默认：L1 直接做，L3 必问。
  **Over-asking kills adoption.** Default: act on L1, ask on L3.
- **Skill 加载 ≠ 任务开工**：第 0 步即使用户消息简单也强制执行。
  **Skill loaded ≠ task started.** Step 0 is mandatory even for trivial-looking messages.
- **密钥**绝不进入代码、文档、提交或对话；提交前扫描；泄露立即轮换。
  **Secrets** never go into code, docs, commits, or chat; scan before committing; rotate on leak.
- **结论即时落盘**：分析时即时记录，拖到收尾会在长会话中丢失。
  **Keep records at analysis time, not at cleanup.**

## 8. 引用地图——按需加载 · Reference map — load on demand only

| 文件 File | 何时加载 When to load |
|---|---|
| `references/platform-adaptation.md` | 第 0 步检测；提问工具降级链；结构化提问协议全文 Step 0 detection, asking chain, structured asking protocol |
| `references/rules.md` | 43 条完整纪律；引用规则编号或需查原文时 The full 43-rule discipline; when a numbered rule is cited |
| `references/workflows.md` | 分类型工作流（新功能、Bug、UI、部署、文档、重大决策、多会话）、复用五问、质量门禁 Task-type workflows, reuse chain, quality-gate details |
| `references/security.md` | 密钥红线、应急响应、安全生产红线、回滚细节 Secrets red line, incident response, safety red lines, rollback details |

不要预加载全部引用，只加载当前步骤需要的。**你无法自行感知上下文是否被压缩——不靠感知，靠两道守卫**：(a) 显式信号（用户说「重载 / 你被压缩了 / 从头加载」或平台重置）→ 立即重读 SKILL.md 与仍需要的引用；(b) 关键节点自检：开工 / 提交 / 重大决策前默写核心要素（分级、模式、回滚、必问），任一复述不全即视为上下文缺失，先重读再继续。You cannot detect context compaction — rely on explicit reload signals plus a core-elements self-check at key milestones; never continue on a compressed impression.

## 9. 留档与知识纪律（摘要） · Records & knowledge discipline (summary)

完整细节见 `references/rules.md`（第 30-38 条）与 `references/workflows.md`。要点：
Full detail in `references/rules.md` (rules 30-38) and `references/workflows.md`. Essentials:

- 每个会话在项目约定位置维护**任务记录**：理解 → 验收标准 → 决策 → 结果；结论即时写入。
  Every session keeps a **task record**: understanding → acceptance criteria → decisions → results; write conclusions immediately.
- 会话结束提炼 1-5 条可复用知识点（默认 3 条），按「场景 → 判断 → 行动」结构；知识版入项目知识文档，个人版（类比 + 判断标准）在对话中给用户。
  At session end, distill 1-5 reusable points (default 3) as scenario → judgment → action; write the knowledge version to the project's knowledge doc, give the plain-language version to the user in chat.
- **经验库**为会话开工必读——按症状关键词搜索；路径由项目定义，本 Skill 不强加。
  An **experience log** is mandatory reading at session start — search by symptom keywords; its location is project-defined.
- 文档与代码同批提交；归档前必须有现行等价物。
  Docs ship with code; nothing is archived without a current equivalent.