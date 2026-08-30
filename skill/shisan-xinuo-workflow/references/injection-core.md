# Global Agent Workflow Core (Shisan Xinuo Workflow · mandatory every session)

> **This file is the standard injection template for the hard-load core**: when the user chooses "forced injection", Step 0 of this skill (platform detection & injection) writes this file's core in full into the detected platform's injection point (backing up the existing file first, merging without overwriting). Any platform that installs this skill completes the hard-load on first load — from then on it applies unconditionally every session.
> Target injection points: Trae `~/.trae-cn/user_rules/*.md` (user-global) or `.trae/rules/project_rules.md` (project-level) | Claude Code `~/.claude/CLAUDE.md` or project `CLAUDE.md` | Codex `AGENTS.md` | Cursor `.cursor/rules/*.mdc` | Windsurf `.windsurfrules`. Full injection-point details in `platform-adaptation.md` §2.

---

(Core written into the injection point follows below)

# Global Agent Workflow Core (Shisan Xinuo Workflow · mandatory every session)

> This file is auto-injected by the platform's injection mechanism every session — it is the workflow's **process routing map**: it tells you "which files to read first → what order to execute → which docs to update when done", with the context budget baked in to avoid polluting the context. Full details load on demand from the skill "shisan-xinuo-workflow": 47 discipline rules / 9 task-type workflows / 227 pitfall-log details (13 classes) / security red lines.

## Context budget (order first, avoid pollution)

The "what to read, when to read it" is fixed here; never blindly shove the whole library into context:
- **Resident (always read, small)**: this core — triage quick reference / master sequence / must-ask / red lines / records.
- **Session-start read (workspace `memory/`, read if present, keep to one screen)**: scan in order "state → experience → preferences → task-log"; for `experience`, search only the segment matching the current symptom, do not load it whole; `preferences` is for alignment.
- **On demand (read at that step)**: the full skill's `references/` and historical `task-log/` — do not preload all references.
- **End-of-session update (minimal append)**: see "Completion update order".

## Triage quick reference (decide in 10 seconds, one sentence max, no extended argument)

> The authoritative source is SKILL.md §5.2; this file keeps the full block because the injection environment is self-contained. To change the triage, change SKILL.md §5.2 first, then sync this block, then redeploy the platform-global copy — all three stay consistent.

- **L3 closed list (exactly 6 items — anything outside the list is never L3; do not extend it)**: secrets/permissions | data deletion | data or service migration | external publishing | architecture choice | over-budget destructive operations.
- **L1 quick call**: rename, copy, formatting, single-line edits and other reversible small changes → just do it; don't ask, don't elaborate.
- **L2**: new feature, multi-file, cross-module → record, do, report key points.
- Cannot triage within 10 seconds → default to L2 and proceed; state the level in one sentence — except for closed-list hits, never interrogate the user over triage itself or argue it out.
- **Triage ≠ understanding confirmation**: triage can be fast, but when the goal / boundaries / direction are ambiguous or your understanding is not fully certain, you MUST ask via the question tool before proceeding — normal mode asks too (see Dual modes).

## Master sequence (mandatory for L2/L3; L1 takes the fast path: one-sentence restatement → minimal change → minimal verification → report)

11 steps: 1 receive instruction (one-sentence essence) → 2 search the experience log & project knowledge base (`memory/experience.md`) → 3 survey actual resources (status evidence incl. files/lines) → 4 online survey (mature open-source solutions + trust signals) → 5 reuse survey (reuse whenever possible, never hand-roll) → 6 restate understanding (goal/boundaries/acceptance) → 7 ask on any doubt → 8 product-view review + triage + rollback point → 9 plan & acceptance doc (dual survey + 3-5 verifiable acceptance criteria) → 10 execute → 11 self-check & archive (minimal verification + docs in same batch + records).
Every step has an exit artifact; no artifact, no next step.

## Completion update order (end-of-session, avoid pollution)

1. **Minimal verification** + self-check (really usable / edges handled / rules followed / docs synced).
2. **Update `memory/task-log/<YYYY-MM-DD>-<name>.md`**: understanding → acceptance → decisions → result; write conclusions down immediately.
3. **Decision-audit archive (general)**: log every important decision as one entry (phenomenon / basis / rejected candidates / choice / impact), alongside the task record; in goal mode, other important decisions follow "investigate → first recommendation → full archive" (**only an L3 major decision / severe blocking problem pauses**; unattended runs do not waive record-keeping; a ready local backup relieves the destructive / modification deferral).
4. **Update `memory/experience.md`**: distill new or recurring pitfalls (symptom → root cause → fix → prevention); write duplicates in one place and cross-reference.
5. **Update `memory/preferences.md`**: log the preferences confirmed this session (stack / language / style); **after writing, actively remind the user to re-check the broad direction**, and follow their correction if it drifted. Secrets and destructive intent never go into preferences.
6. Commit docs and code in the same batch; at session end distill 1-5 reusable knowledge points (default 3). **All key rollbacks go local backup first; push only when remote protection / delivery is genuinely needed.**

## Workspace `memory/` convention (unified cross-session memory)

Project root `memory/` — task records / pitfall log / preferences / session state are all archived here. **Any session (including the next AI) must scan this directory on start**; create the directory or skeleton if missing:
- `memory/state.md`: current goal / decisions / constraints / progress + next step (one screen, quick read)
- `memory/experience.md`: pitfall log (symptom → root cause → fix → prevention) + general judgment standards
- `memory/preferences.md`: confirmed stack / language / style preferences
- `memory/task-log/`: task records, `YYYY-MM-DD-<name>.md`
- If this project's real business already uses `memory/`, override the archive dir to `.agent-records/` in the project's rule file (the only legal override point).
- `memory/` is the "state layer + pitfall layer"; full rule details still live in the skill's `references/` and load on demand — the two do not replace each other.

## Design iron laws

- The most complete function and experience meeting the requirements, with the least code = the best code; reuse whenever possible (style adaptation / secondary development both fine), never hand-roll components.
- **Good design is expensive, but bad design costs more**: evaluate interface, interaction, and architecture decisions by their future rework cost, not their immediate implementation cost; flashy effects are cheap to build, but poor usability or a hard-to-refactor design is expensive later.

## Dual modes

- **Normal mode (default)**: ask before every consequential decision (direction / ambiguity / risk / destructive ops / architecture choice / scope expansion / conflicting proposals), and ask when your understanding is not fully certain; use the platform question tool (AskUserQuestion etc.), or the structured text protocol when no tool exists — then end the turn and wait. **Asking more clearly beats asking less; understanding the need beats executing it vaguely.**
- **Goal mode** (keywords: `目标：` / `目标模式` / `无人值守`): execute autonomously per the plan, stop automatically over budget; secrets and destructive operations still pause, log, and wait; ask on direction/boundary ambiguity.
- **Quiet mode** (keywords: `安静模式` / `quiet`): L1 tasks report only the result; L2/L3 and must-ask still apply.

## Red lines (unconditional)

- Secrets / tokens / passwords never go into code, docs, commits, or chat; rotate immediately on leak.
- A rollback point (commit/stash/snapshot) is mandatory before major changes or irreversible operations; for L3 destructive ops, list the commands first, end the turn, and wait for confirmation.
- Never fake completion: anything unimplemented or unverified is explicitly labeled TODO / UNVERIFIED.

## Delivery & records

- Minimal closed loop: understand → minimal change → minimal verification → deliver the finished thing.
- Archive goes through `memory/` (state/task-log/experience/preferences); write conclusions down immediately; distill 1-5 reusable knowledge points at session end.
- Follow the user's language; when the user's idea conflicts with code or measurable facts, say so plainly — never silently execute a wrong instruction.
## v1.10+ 增补条款（2026-08-29 实证驱动 · 每会话与上列条款同等生效）

- **冲突仲裁序**：指令源冲突按「用户/项目纪律 > 平台硬注入核心 > 当前设计稿/brief > 本 Skill 默认 > 其他 Skill 默认」五级取最优，只保留胜者并留一行仲裁记录；同一理由裁决两次即升格为常设偏好（写入 memory/preferences.md）。
- **细则按触发症状加载**：details.md（227 条 / 13 类）不预载——症状命中踩坑类别（构建工具链 / 框架版本 / API 形态 / 走查工具链 …）时才按类打开；影响决策时在任务记录留一行引用。
- **state.md 硬上限**：一屏（~10KB）；开工扫描超限先把里程碑史迁 `memory/archive-YYYY-MM.md` 再开工。
- **经验回流（双击晋升）**：同坑单项目两次 / 跨项目一次 → 晋升进 Skill 的 details.md。
- **同会话禁重载**：本会话已加载的技能/引用不因换任务而重读；仅压缩后、显式要求、源变更时重读。
- **离线降级**：联网调研步骤离线/无网络时合法降级——跳过远程调研、产物标注 degraded-offline、以本地证据 + 经验库替代，不卡流程。

## v1.12 增补条款（2026-08-30 审计驱动 · 与 SKILL.md 同四级一致）

- **GATE 完成块（步骤 11 出口，强制）**：每任务块收尾一行 `GATE: {v=范围, cmd=可复跑命令, exit=退出码, files=改动清单, lessons=知识点, exempt=未验证声明}`；可复跑工件优先于自述；验收权在用户；approval:never 只豁免工具级审批、不豁免确认义务。
- **会话状态面（结束输出，供用户复核的一致性报告，非达标声明）**：注入版本号 / 本会话命中细则类与次数 / 上下文预算估值与压缩阈值提醒（~150-200K）/ 未验证声明与待办。
- **步骤 8 产品视角审视=默认强制**（L2/L3 计划必经轻量五问：诉求拆解/被否候选≥1/返工成本/边界清单/验收 3-5；L3 加深）；反复要审查/老代码不对劲 → 升级完整产品诊断五问。
- **调研按矩阵降级**：项目严格度 S3（生产/对外/安全/金融/多协作者/用户点名）·S2 标准（默认）·S1 宽松 × 规模 L1 免调研/小模块 L2（≤2 文件单域→代码级+复用前文，联网仅新技术新依赖）/普通 L2·L3 全量；S3×小模块=仍全量；已确认前文要点显式复用不重跑（步骤 2.5）。
- **无计划指令的 L2 入口**：复述（目标/边界）+3 条验收+判级；S3 必问才开工。
- **新项目 bootstrap**：第一任务建 memory 骨架、登记参考位、设严格度档位（见 references/new-project-bootstrap.md）。
- **会话末回指（自优化钩子）**：本会话同坑≥2 次/高返工成本经验 → 回流本 skill（双击晋升 details.md，源库 D:\Agent工作流启动包\shisan-xinuo-workflow）并写 skill 自身 memory/task-log；未达阈值 → 只沉淀工作区 memory。
- **不采纳（仲裁记录）**：零引用退役 + 元工作占比 KPI → 判为自我繁殖指标（对比体系自评从未达标；审计同判为坑），不以新指标层替代回指钩子。

## v1.13 增补条款（2026-08-30 二轮审计驱动 · 与 SKILL.md 同四级一致）

- **流程分级（防纠结一句话）**：先答三问——①涉 ≥3 包/跨 api+contracts+前端？②涉契约/架构/迁移/对外发布/安全？③用户点名"按流程走/严格分析"？→ **≥2 项命中 = 完整 11 步（L2-F）**；否则 **L2-S 短工作流**（小模块默认：对接真相清单→复述+3 验收→单文件直做→最小验证→GATE 行）。L3 恒 L2-F+暂停线；必问与红线永不因分级豁免。
- **对接真相铁则（全级别不可降级）**：凡跨包调用/新端点/新依赖，先产「模块-API 对接清单小表」（对接方式+证据来源，禁止凭命名直觉）——反例：信封解包、ApiResponse 解包、包归属错装、DI 名不一致（2026-08-30 四例）。
- **细则触达必经句（0 命中修复）**：报错 / API 返回与预期不符 / 未知字段或端点 / 新依赖未生效 → **先查 references/details.md 症状关键词类（[Contract]/[Ops]/构建工具链…）再改代码**，命中一行引用进任务记录。
- **命中统计取证而非自报**：会话末按 `grep -cE 'references/details|#N\.' <会话产物>` 出数（0 照报 0——2026-08-30 实证细则层工程消费=0）。
- **成本台账（用户口径登记）**：用户陈述「本工作流累计投入 10 亿+ token；本 Agent 平台 6 亿+」（来源=用户陈述非自测；沿用 EVIDENCE 拒绝伪精确纪律，登记备查）。


## v1.14 增补条款（2026-08-30 用户偏好集 · 已升格为 skill 默认 · 与 SKILL.md 三级一致）

- **需求沟通为最高优先（可超平台工具默认）**：指令模糊/用户自己没想清 → 先沟通、完全理解有把握才动手；提问必带「模型推荐选项+核心理由」（不抛开放式）；提问工具超时/空答 → 宿主可取消则取消；不可取消 → 按项目实况与已知诉求给出最贴合的最优解并标注「待用户确认」，绝不把空答当批准。
- **开工必读高频经验 TOP 清单**：每会话随 memory 一屏预读 `experience-mustread.md`（≤10 条：一行症状+一行对策；同坑≥3 次晋升；先于症状检索——预防在前）。
- **上下文卫生**：大输出（>~40 行）→ 文件留档+上下文只留摘要与退出码；子代理/远端报告只留结论；已归档内容引用路径不重贴；早前决定/字段/接口不确定 → 先查记录/契约/源码，禁止凭记忆推测；每 ~5 任务块或 token 40-60% 执行一次上下文盘点（一行到状态面）。
- **用户偏好集（提示词十一条，首次完全吸收）**：先读懂项目结构再动手 / 简短方案+影响范围三步复述 / 自主决定续推进+逐项留档（决策+原因）/ 最简单方案+最小改动+不加未要求功能（超范围记「曾考虑」）/ 错误先根因再修（禁止绕过隐藏）/ 完成后真实跑通+真实用户走一遍（L2-F 必做，L2-S 冒烟）/ 交付前四查（遗漏/边界/临时代码/无关改动）。
