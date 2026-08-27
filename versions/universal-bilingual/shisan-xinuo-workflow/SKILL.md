---
name: shisan-xinuo-workflow
description: "一句话定位：把任何工程任务强制按「调研驱动的 11 步主流程 + L1/L2/L3 封闭清单速判 + 双模式」推进的可审计 Agent 工程纪律工作流，核心纪律可平台无关硬注入。任何动手任务开工必用。One-line positioning: forces every engineering task through an auditable agent workflow — research-driven 11-step master sequence + L1/L2/L3 closed-list quick triage + dual modes, with platform-agnostic hard injection of the core. Use on any hands-on task."
version: 1.6.0
license: MIT
compatibility: "Trae、Codex、Claude Code、Cursor、Windsurf、WorkBuddy 及任意支持 Agent Skills 标准的 CLI 编码智能体 / any CLI encoding agent supporting Agent Skills"
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
metadata:
  author: zxc663
  edition: universal-bilingual
  homepage: https://github.com/zxc663/shisan-xinuo-workflow
  topics:
    - agent-skills
    - ai-agent-workflow
    - prompt-injection-defense
---

# 十三希诺通用 Agent 工作流 · Shisan Xinuo Agent Workflow

> **定位：流程为魂、规则为基。** 通用工作执行流程是灵魂（每个任务强制通用的推进骨架），43 条纪律规则是地基（约束每步该守什么）；二者强耦合、相互依托——流程承载规则落地，规则约束流程执行，缺一不可。
> **Positioning: workflow is the soul, rules are the foundation.** The universal operating sequence is the soul (the mandatory skeleton every task advances along); the 43 rules are the foundation (what each step must observe). Strongly coupled and mutually dependent — the workflow carries the rules into execution; the rules govern the workflow.

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
| 4 | 联网调研·必须 Online survey (mandatory)：调研市面开源成熟项目 / 库 / 方案，收集**可验证可信信号**（stars / 下载量 / 维护 / 被采用 / 口碑 / 安全通告），不以「网上都说火」为依据；清单见 workflows.md §0.2 research mature open-source projects; collect verifiable trust signals, never "it's popular"; see §0.2 | 市面方案调研记录 Market solution survey record（候选 + 可信信号 + 安全风险） |
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

影响重大的决策必须在行动前与用户确认。触发：方向不明或歧义、需求冲突、权限/密钥、破坏性操作（删除/迁移/覆盖/发布）、架构选型、范围扩大、方案分歧。Consequential decisions must be confirmed before acting. Triggers: ambiguity, conflict, permissions/secrets, destructive ops, architecture, scope, proposals.

**降级链 Downgrade chain**：① 平台原生提问工具 Native asking tool；② 不可用 → 结构化文本协议（a 理解 b 选项优缺点 c 风险后果 d 推荐），**结束回合等待** end the turn and wait。L1 常规不问；L3 必问。**偏好记忆 Preference memory**：用户确认选择（技术栈/语言/风格）后写入 memory/「用户偏好」字段，同类场景直接采用不再重复问；只覆盖已确认重复偏好，绝不覆盖密钥与破坏性操作。Do not over-ask on L1; always ask on L3; confirmed preferences go to the memory file and are reused, never secrets or destructive ops.

## 5. 双模式与任务分级 · Execution modes & task triage

| 模式 Mode | 触发 Trigger | 行为 Behavior |
|---|---|---|
| **普通 Normal**（默认） | 无关键词 | 关键决策必问 Ask before consequential decisions |
| **目标 Goal mode** | `目标：`/`目标模式`/`无人值守`/`goal mode`/`unattended` | 按计划自主执行；密钥与破坏性操作仍暂停等待 Autonomous per plan; secrets & destructive ops pause |
| **安静 Quiet mode** | `安静模式`/`quiet`/`quiet mode` | L1 只汇报结果（隐藏中间推理/调研展示）Report only results on L1; L2/L3 unchanged; secrets & destructive still ask |

目标模式附加：执行前写计划（范围/风险/预算）、子任务按文件边界拆分、超预算自动停、交付复盘 + 待确认清单。Goal mode: plan first, budgets, file-boundary split, auto-stop, retrospective.

| 级别 Level | 判定 Criteria | 普通 Normal | 目标 Goal |
|---|---|---|---|
| L1 常规 routine | 小改动、可逆、低影响 | 直接做 do | 直接做 do |
| L2 中风险 medium | 新功能、多文件、跨模块 | 记录后做，汇报关键点 record & report | 按计划执行，节点记录 per plan |
| L3 高风险 high | 密钥/权限/删除/迁移/发布/架构 | **先问再做 ask first** | 选推荐标注 `REVIEW:`；密钥与破坏性操作暂停留档 pick recommended, label REVIEW; pause on secrets/destructive |

**判级速查（10 秒定论，一句话即止，禁止展开论证）Triage quick reference**：L3 封闭清单（仅 6 项，清单外一律不是 L3，不得自行扩展）：密钥/权限｜数据删除｜数据或服务迁移｜对外发布｜架构选型｜超预算破坏性操作。L1 速判：改名、文案、格式、单行修改等可逆小改动直接做；L2：新功能、多文件、跨模块，记录后做。10 秒判不了级默认按 L2 直接推进；判级结论一句话即止，除命中 L3 清单外判级本身不追问用户、不展开分析。Closed list of 6 for L3 (nothing outside it is L3); L1 = reversible small changes, just do them; cannot triage in 10s → default L2, one-sentence verdict, no arguing.

## 6. 最小闭环交付（第 11 步交付原则）· Minimal closed-loop delivery (step-11 principle)

理解 → 最小修改（复用优先）→ 最小验证 → 交付成品；不交半成品、不留占位、绝不假实现。Understand → minimal change (reuse first) → minimal verification → deliver finished work; no placeholders, never fake completion.

## 7. 质量门禁与回滚 · Quality gates & rollback

提交前审查者视角重读 diff、重跑验证、文档与代码同批；重大修改/不可逆操作前必建回滚点（commit/stash/快照）；**原子操作锁（L3 破坏性操作）**：删除/迁移/覆盖写/发布类操作先输出命令清单、结束回合等用户确认再执行；对外发布先批准 + 约 30 分钟观察期。Review the diff, re-run validation, ship docs with code; rollback point BEFORE major changes; **atomic-operation lock**: output the command list and wait for user confirmation before L3 destructive ops; publish after approval + observation window.

## 8. 易错点 · Gotchas

- **判级内耗 Triage burnout**：琐碎判级一句话定论——改名 / 文案 / 格式类一律 L1 直接做；L3 只认第 5 节封闭清单，清单外不构成 L3。为判级展开论证或反复纠结是 token 浪费的最大来源之一。Settle trivial triage in one sentence; L3 honors only the closed list in section 5.
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
| `references/rules.md` | 43 条纪律（地基）The 43-rule discipline (foundation) |
| `references/workflows.md` | 总纲细节、澄清流程、9 类工作流、复用五问、质量门禁 Master details, clarification, task types, reuse, gates |
| `references/details.md` | 落地细则（工程规范 / 具体做法）12 类：环境/前端/数据库/测试/API/部署运维/代码质量/Git/会话·备份·治理/深挖补充/铁律纪律/源项目深挖 Landing details, 12 categories (env/frontend/DB/testing/API/ops/code quality/git/sessions/deep-dive/iron laws/source-project), load by category |
| `references/security.md` | 密钥红线、应急、回滚细节 Secrets, incident, rollback, prompt-injection, supply-chain |
| `references/never-list.md` | 永不清单（明线）Never list — 开工/提交/风险前自查 quick self-check before start/commit/risky ops |

**上下文缺失自检（压缩不可感知）Context-loss self-check**：显式信号（用户提示重载/平台重置）→ **立即按重载顺序执行 Reload sequence**：①重读本 SKILL.md；②重读记忆文件 `memory/`；③重读当前步骤引用；④向用户复述任务与验收再继续；关键节点（开工/提交/重大决策）先默写核心要素（总纲步序、模式、回滚、必问），复述不全即重读。On explicit reload/reset signals: ① re-read SKILL.md → ② re-read memory file → ③ re-read needed references → ④ restate task + acceptance to the user; self-check core elements (master steps, mode, rollback, ask) before key milestones.

## 10. 留档与知识纪律（摘要）· Records & knowledge discipline (summary)

任务记录随会话维护（理解 → 验收 → 决策 → 结果），各步出口产物随记录留档；会话结束双写知识（知识版 + 个人版）；经验库开工必读（按症状检索，路径项目自定）；**记忆文件协议（外部化长期记忆）**：项目约定位置维护 `memory/`（当前目标 / 决策 / 约束 / 进度 / 踩坑，一屏内），关键节点与上下文 40-60% 前写入，压缩 / 重置 / 会话开始**先读再继续**；**用户偏好**：memory/ 维护「用户偏好」字段（已确认的技术栈/语言/风格），会话开始读取、同类决策复用不再重复问（细节见 `references/workflows.md`）；文档与代码同批、归档前有现行等价物。Task record per session with step artifacts; dual-write knowledge at session end; experience log mandatory at start; **memory-file protocol**: maintain `memory/` per project convention, write at milestones & before 40-60% context, read first after compaction/reset; **user preferences**: keep confirmed choices in the memory file and reuse them to avoid re-asking; docs ship with code. **配套模板 Templates**：规划 / 验收 / 任务记录 / 复盘 / 回滚点 / 提示词预算模板 + 会话钩子（`templates/hooks/`）+ 审查子代理（`templates/agents/`）位于 `templates/`（复制填写）。Templates (plan/acceptance/task-record/retrospective/rollback/prompt-budget), hooks and review sub-agents live in `templates/` (copy & fill).
