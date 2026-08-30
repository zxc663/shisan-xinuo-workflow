---
name: shisan-xinuo-workflow
description: "One-line positioning: forces every engineering task through an auditable agent workflow — mandatory research-driven 11-step master sequence + L1/L2/L3 closed-list quick triage + dual modes (normal/goal), with platform-agnostic hard injection of the core discipline. Use on any hands-on task."
license: MIT
compatibility: "Trae, Codex, Claude Code, Cursor, Windsurf, WorkBuddy and any CLI encoding agent supporting the Agent Skills standard"
metadata:
  version: 1.14.0
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
  edition: universal-en
  homepage: https://github.com/zxc663/shisan-xinuo-workflow
  topics:
    - agent-skills
    - ai-agent-workflow
    - prompt-injection-defense
---

# Shisan Xinuo Agent Workflow (十三希诺通用 Agent 工作流)

> **Positioning: workflow is the soul, rules are the foundation.** The universal task operating sequence is this skill's soul — the mandatory skeleton every task advances along. The numbered discipline rules (`references/rules.md`) are the foundation — they constrain what each step must observe. The two are **strongly coupled and mutually dependent**: the workflow carries the rules into execution; the rules govern the workflow's steps. Neither can be spared. Skipping the workflow discards the soul; ignoring the rules undermines the foundation.

## 1. When to use / when NOT to use

**Use** for any engineering task (whenever you are doing work, advance along the master sequence in section 2); for disciplined execution, workflow governance, workflow rules, or consistent agent behavior across projects and platforms. Step 0 (section 3) also runs automatically whenever this skill loads.

**NOT a substitute for** learning a framework/API from its own docs or for replacing project-level conventions — the project's own docs always win where they conflict with this skill.

> **Honest note on landing details**: `details.md` does carry fine-grained engineering experience from real projects, some bound to specific stacks (Next.js / Prisma / Playwright …). Treat it as a **pitfall log** ("what went wrong there") — not as domain tutorials ("how to use X"); the workflow / rules / gates layers themselves are framework-agnostic.

## 2. Master: Task operating sequence — mandatory universal skeleton (single entry)

> **This is the core of the skill, not a reference item.** Every task must advance along this sequence. Every step has an **exit artifact** — no artifact means the step is unfinished, and the next step may not begin. This is the process gate: checkable, auditable, unskippable.

### 2.1 Prelude: Status clarification (when goals / state are fuzzy)

When the user cannot sort out the project state, the goal is unclear, or step 1 exposes a fuzzy baseline, **first run the clarification dialogue** (`references/workflows.md`, clarification flow): drive a step-by-step interrogation (one question at a time) → map the current state, decompose the problem, lock onto the key lead → produce a **clarification memo (goal / current state / constraints / blockers)** → after user confirmation, return to master step 1.

### 2.2 Mandatory 11-step master sequence (exit artifact per step)

> **The iron law (reuse)**: the best code achieves the most complete function and experience with the least code while meeting the requirements. Reuse whenever possible — style adaptation or secondary development are both fine; **never hand-roll your own components.**
> **The design-cost iron law**: good design is expensive, but bad design costs more — evaluate interface, interaction, and architecture decisions by their **future rework cost**, not by their immediate implementation cost; flashy effects are cheap to build, but poor usability or a hard-to-refactor design is expensive later.

| Step | Action | Exit artifact (must exist before the next step) |
|---|---|---|
| 1 | **Receive the instruction** — first-principles understanding (essence / required / inertia) | One-sentence task essence |
| 2 | **Read the experience log first** — search by symptom / keyword | Hit record (hit → execute per "solve / prevent") |
| 3 | **Survey actual resources** — real code (status evidence) + environment + workspace + available skills / MCP | Status fact list (file / line / conclusion) |
| 4 | **Online survey (mandatory)** — research mature open-source projects / libraries / solutions (not a fallback; a required step for every task); collect **verifiable trust signals** (stars / downloads / maintenance activity / adoption evidence / community feedback / security advisories), never "it's popular online" — listing heat is only a discoverability reference, not a quality signal; what & how to survey in `references/workflows.md` §0.2; record degradation when environment/capability/tool/skill/MCP is missing. **Offline / no-network is a legitimate degradation**: skip the remote survey, mark the exit artifact `degraded-offline`, substitute step-3 local evidence + the experience log — never block the sequence on network | Market solution survey record (candidates + trust signals + feedback + security risk + degradation notes) |
| 5 | **Reuse survey (iron law)** — local project → mature open-source projects; reuse whenever possible, style adaptation or secondary development both fine, **never hand-roll components** (five-question chain) | Reuse conclusion (candidates + adaptation plan + build-new reason, only when the whole chain misses) |
| 6 | **Restate understanding** — goal / boundaries / acceptance criteria | User confirmation (continue only when aligned) |
| 7 | **Ask on any doubt** — unclear execution or direction drift → ask and end the turn | Ask / confirmation record |
| 8 | **Product-view review + constraints + L1/L2/L3 triage + rollback point** — review from the product/experience angle first; when "review again / something keeps feeling off in a legacy codebase" triggers, **run the product-polish diagnosis first** (five questions: where does the gap live — feature logic / code coupling / UI / interaction flow / other; see `references/workflows.md` §0.3) before touching code as an engineer | Risk triage + rollback-point record + (when triggered) product-polish diagnosis report |
| 9 | **Plan & acceptance doc (after the mandatory dual survey)** — first run the **dual survey**: ① engineer view (code reality / technical feasibility / reuse, steps 3 & 5) and ② product-manager view (soundness of the current design plan: essential need / is the design complete / do experience·UI·interaction match the product positioning; `references/workflows.md` §0.4) — then produce a **detailed plan doc** (dual-survey conclusions + feature list & priorities + 3-5 verifiable acceptance criteria; goal mode adds budgets & file boundaries) | Detailed plan doc (with dual-survey conclusions) |
| 10 | **Execute** — per triage; goal mode autonomous per plan, log checkpoints, stop over budget | Execution record / changes |
| 11 | **Self-check & archive** — minimal verification → self-check → docs with code → dual-write knowledge → commit with note | Verification result + archive (docs / knowledge / commit note) |

**Gate**: before entering a step, the previous step's exit artifact must exist and be recorded; steps that legitimately cannot produce one (e.g. genuinely no reuse to survey) must record the reason in the task record — never skip silently.

### 2.3 L1 fast path (triage-first)

Right after step 1, triage the task level: **L1 routine** (small, reversible, low impact — typo fix, single-line change, doc tweak) → take the **L1 fast path**: one-sentence restatement → minimal change → minimal verification → report. Explicitly mark it as "L1 fast path" in the task record (a named lane, not a silent skip). L2 / L3 keep the full 11-step sequence (triage is finalized again at step 8).

### 2.4 L2 flow split (v1.13 — the 11-step master is for LARGE modules)

Answer three questions FIRST: ① touches ≥3 packages / spans api+contracts+frontend? ② touches contracts / architecture / migration / external-publish / security? ③ user named "follow the workflow / strict analysis"? **≥2 yes → L2-F (full 11-step master)**; otherwise **L2-S short workflow** (default). L3 always L2-F + pause line.

- **L2-F trigger examples (written in to stop boundary drift)**: new endpoint + contract + two pages · architecture selection · migration · secrets/publish involvement · multi-module joint change.
- **L2-S short workflow (small module)**: ① integration-truth survey (mandatory, see §2.5) ② restate + 3-5 verifiable acceptance criteria ③ no plan doc: single file → do directly; ≤3 files → one line "change + acceptance + rollback baseline" ④ execute + minimal verification ⑤ GATE line + status-surface line. **Explicitly skipped**: internet dual-survey, deep product five questions, plan document, repeated asking (except direction/boundary ambiguity — ask-before-acting is NOT waived; red lines never waived).
- Ask-before-acting & red lines are NEVER waived by the split.

Details and per-task-type checklists: `references/workflows.md` (master + clarification + 9 task types).

### 2.5 Integration-truth survey (MANDATORY at every level, never scaled away)

Before touching code that crosses packages / calls an API / adds a dependency / uses a new endpoint: produce the **module-API integration checklist table**:

| 模块/Module | API/端点 | 对接方式 (path/method/envelope/fields/package) | 证据来源 (source:line / contract schema / official docs) |

**Never write the integration from naming intuition.** 2026-08-30 audit counter-examples (all four cost rework): @tx/contracts envelope vs direct return; `api.get` returns `ApiResponse` (unwrap before `.data`); recharts belongs to apps/admin, not apps/api; Nest constructor-injected name must match the imported provider. Fix method: grep call sites → read schema/type → confirm package ownership → then write. One line of this checklist is required even in L1 restatement when the change touches integration.

## 3. Step 0: Platform detection & injection (on load / first run)

Before starting tasks, hard-load this workflow onto the current platform:

1. **Detect the platform** using the feature checklist in `references/platform-adaptation.md` (directory markers, env vars, tool availability).
2. **Locate the platform's REAL injection point** per the injection-point table in `references/platform-adaptation.md` §2 — Trae: `~/.trae-cn/user_rules/*.md` (user-global; the file's mere existence injects it every session, no in-app enabling needed) or project `.trae/rules/project_rules.md`; Claude Code: `~/.claude/CLAUDE.md` or project `CLAUDE.md`; Codex: `AGENTS.md`; Cursor: `.cursor/rules/*.mdc`; Windsurf: `.windsurfrules`. A file written only into a workspace folder the app never reads is **useless**.
3. **Ask the injection mode** — use the asking chain from section 4 and let the user choose:
   - **On-demand (default)** — the rule file holds a lean discipline and points back to this skill; the full skill activates when triggered. Lowest context cost.
   - **Forced injection (hard-load)** — write the full core from `references/injection-core.md` into the platform's injection point (backup the existing file first, merge without overwriting) — the workflow is unconditionally present every session and no longer depends on the model voluntarily loading this skill (a fixed ~2-3K tokens per session). **Do NOT implement forced injection as "every session must fully read this SKILL.md" — models do not reliably execute extra reads; write the core text itself into the injection point.**
   If no asking tool is available, default to on-demand and say so explicitly.
4. **Pick the active asking mechanism** from the downgrade chain in section 4.
5. **Verify**: after writing, restate the active essentials (platform, injection point, injection mode, asking tool). Do not claim success until the injection is confirmed active. Do not start the task until this is done.

## 4. Ask-before-acting protocol

Consequential decisions must be confirmed with the user before acting. Triggers: unclear direction or ambiguity, conflicting requirements, permissions/secret handling, destructive operations (deletion, migration, overwrite, external publishing), architecture or tech-stack choices, scope expansion, conflicting proposals. **"Not-fully-certain understanding" is also a trigger — in normal mode too** (see §5.1): triage fast, but ask on understanding. Asking more clearly beats asking less.

**Asking-tool downgrade chain** (use the first available):

1. Platform-native asking tool (`request_user_input`, `AskUserQuestion`, `ask_user`, …)
2. If unavailable: structured text protocol — present (a) understanding, (b) options with pros/cons, (c) risks and consequences, (d) a recommendation, then **end the turn and wait**. Full protocol in `references/platform-adaptation.md`.

Routine L1 tasks do not require asking — do not over-ask; but ask when your understanding is not fully certain. High-risk L3 tasks always require asking. **Preference memory**: after the user makes a confirmed choice (e.g. tech-stack, language, style via the asking tool), write it to `memory/preferences.md` (§10) so the same class of decision is reused next time instead of re-asking — preference memory only covers confirmed repeated preferences, never secrets or destructive ops.

**Conflict arbitration order** — when two instruction sources disagree (skill guidance vs project discipline vs a design brief vs another skill's defaults), pick by this fixed order and **keep only the winner** (delete the loser's citation from your working notes — never obey both, never merge into a hybrid):

1. user / project discipline (project rule files, confirmed D-series decisions, design contracts) — the brief wins;
2. platform hard-injected core (injection point text);
3. the design draft / brief of the current deliverable;
4. this skill's defaults;
5. any other loaded skill's defaults.

Record one arbitration line in the task record (`source A vs source B → followed X, because …`). A conflict resolved twice for the same reason is a standing decision: write it into `memory/preferences.md`, not into ad-hoc notes.

## 5. Execution modes & task triage

### 5.1 Dual modes (default = normal mode)

| Mode | Trigger | Behavior |
|---|---|---|
| **Normal** (default) | no keyword | Ask before every consequential decision, and when your understanding is not fully certain (section 4); use the platform question tool, or the structured text protocol when none exists, then end the turn and wait. **Log every important decision to the decision-audit archive, and immediately restate it to the user and request confirmation before continuing** (the record is restated now, not after the fact). Asking more clearly beats asking less. |
| **Goal mode** | keywords `目标：` / `目标模式` / `无人值守` / `goal mode` / `unattended` | Execute autonomously from a written plan; **pause (stop and wait) only in two cases — major decisions (L3) / severe blocking problems**; every other important decision follows "investigate → push the first recommendation → **fully archive the decision record for audit**"; **every milestone forces a record landing**; still ask on direction/boundary ambiguity; secrets and destructive operations still pause and wait for the user. |
| **Quiet mode** | keywords `安静模式` / `quiet` / `quiet mode` | L1 tasks: report only the result (skip intermediate reasoning / survey steps) to cut visual noise and token anxiety; L2/L3 unchanged; secrets & destructive ops still ask. |

Goal-mode extra duties: write a plan (scope, risk rating, time/round budget) *before* executing; split subtasks by file boundaries; record progress and every milestone as you go; stop automatically when the budget is exceeded; deliver a retrospective plus an open-questions list. **Rollback points go local backup and do NOT `git push` by default (saves bandwidth + tokens); a ready local snapshot makes destructive / modification-class operations safe to execute and relieves the deferral (L3 excepted — still pauses).**

### 5.2 Task triage L1 / L2 / L3

| Level | Criteria | Normal mode | Goal mode |
|---|---|---|---|
| L1 routine | small, reversible, low impact | do it directly | do it directly |
| L2 medium risk | new feature, multi-file, cross-module changes | record, do, report key points | execute per plan, log checkpoints |
| L3 high risk | secrets, permissions, data deletion, migration, external publishing, architecture choice | **ask first** | **pause, log, and wait for the user to confirm** (even when a local backup is ready — a backup rollback cannot cover the external impact and the permissions / security surface); secrets and destructive ops: pause, log, wait |

Judge by: blast radius, reversibility, rework cost, whether data or external publishing is touched.

**Triage quick reference (decide in 10 seconds, one sentence max, no extended argument)**:

- **L3 closed list (exactly 6 items — anything outside the list is never L3; do not extend it)**: secrets/permissions | data deletion | data or service migration | external publishing | architecture choice | over-budget destructive operations. **This block is the single authoritative source for the closed list and the L1/L2 quick calls**; citations in `rules.md` / `workflows.md` only summarize and point back here — change the triage only here.
- **L1 quick call**: rename, copy, formatting, single-line edits and other reversible small changes → just do it; don't ask, don't elaborate.
- **L2**: new feature, multi-file, cross-module → record, do, report key points.
- Cannot triage within 10 seconds → default to L2 and proceed; state the level in one sentence — except for closed-list hits, never interrogate the user over triage itself or argue it out.
- **Triage ≠ understanding confirmation**: triage can be fast, but when the goal / boundaries / direction are ambiguous or your understanding is not fully certain, ask via the question tool in normal mode too — ask clearly, proceed.
- **Triage sync chain (unanimous in three places)**: `injection-core.md` must keep this block in full because the injection environment is self-contained, and it is deployed as a platform-global `user_rules` written copy — this block → `injection-core.md` → the injected platform-global copy must stay consistent. To change the triage, change this block first, then sync `injection-core.md`, then redeploy the global copy, keeping all three aligned.

## 6. Minimal closed-loop delivery (the delivery principle of step 11)

1. **Understand** — restate the goal, boundaries, and acceptance criteria in 1-3 sentences.
2. **Minimal change** — modify only what the task requires. Prefer existing code, dependencies, platform-native capabilities, and existing open-source solutions over writing new ones (five-question reuse chain in `references/workflows.md`).
3. **Minimal verification** — run the smallest check that proves the change works (lint / type-check / tests — the project's own baseline).
4. **Deliver the finished thing** — no half-done work and no placeholders. Anything unfinished must be explicitly labeled (`TODO`, `NOT IMPLEMENTED`, `UNVERIFIED`). **Never fake completion.**

## 7. Quality gates & rollback

- Before committing: re-read the diff as a reviewer (boundaries, security, readability, unverified claims, reuse), re-run validation, and ship docs in the same commit as code.
- **Rollback rule — create a rollback point BEFORE major changes or irreversible operations.** Git-tracked files: confirm a clean worktree, then commit/stash the current state (or work on a separate branch). Non-git files: copy a snapshot first. Run high-risk commands only after a rollback point exists.
- **Atomic-operation lock (L3 destructive ops)** — for deletion / migration / overwrite / publish-class operations, in addition to the rollback point: **first output the list of commands you intend to run, end the turn, and wait for the user to confirm**; execute only after confirmation. This puts the final gate in human hands, not agent self-discipline.
- External publishing: user approval first, then an observation period (~30 min) monitoring errors/latency/alerts; roll back on anomaly.

## 8. Gotchas

- **Triage burnout**: settle trivial triage in one sentence — rename / copy / formatting questions are always L1, just do them; L3 honors ONLY the closed list in section 5, nothing outside it constitutes L3. Arguing over triage or agonizing repeatedly is one of the biggest token sinks. (Triage ≠ understanding confirmation — that distinction lives in section 5 and is authoritative there.)
- **Same-session reload is pure waste**: a skill / reference already loaded in the current session is NOT re-read for the next task in the same session — per-session reload discipline applies across sessions (fresh context), not within one. Reload only after compaction, an explicit reload signal, or when the source file changed. (Context order and load-on-demand map: sections 9-10.)
- **The sequence is unskippable.** Survey (step 3) and reuse survey (step 5) are the most-skipped steps — skipping breaks the sequence and is the most common violation.
- **On repeated review requests, run the product-polish diagnosis first** — when the user keeps asking to review or keeps feeling something is off, locate the gap by product dimension (feature logic / code coupling / UI / interaction flow / other; workflows.md §0.3) before touching code; don't just re-check correctness as an engineer.
- **Trigger keywords are live switches.** Goal-mode keywords (`目标：`, `unattended`, …) silently change the decision model. Check every user message for them, including mid-task messages.
- **Never overwrite an existing rule file** (`AGENTS.md`, `CLAUDE.md`, …). Backup + merge only.
- **User idea vs code conflict** — code and measurements win. Say so plainly; never silently execute a wrong instruction.
- **No native asking tool?** The most common failure is charging ahead instead of using the text protocol and ending the turn. Ask first, act never.
- **Over-asking kills adoption.** Repeated confirmation on L1 work gets this skill disabled. Default: act on L1, ask on L3.
- **Skill loaded ≠ task started.** The master sequence in section 2 is mandatory even when the user's message looks trivial.
- **Secrets** (keys, tokens, passwords) never go into code, docs, commits, or chat. Scan before committing; rotate immediately on leak.
- **Keep records at the time of analysis, not at cleanup.** Conclusions written late get lost in long sessions.

## 9. Reference map — load on demand only

**Loading discipline**: open a reference only on (a) its **trigger symptom** below, (b) the step that names it, or (c) an explicit user request. Never preload. When a reference changed a decision, cite it in one line in the task record — this is what keeps the detail layer alive instead of decorative.

| File | When to load | Trigger symptoms (open it when you see these) |
|---|---|---|
| `references/injection-core.md` | Section 3 forced injection (hard-load) — the platform-agnostic core template, written in full into the detected platform's injection point | "write it into my platform rules" / injection-mode setup |
| `references/platform-adaptation.md` | Section 3 platform detection; injection-point table; asking-tool downgrade chain; full structured asking protocol | unknown platform / no native asking tool / injection point in doubt |
| `references/rules.md` | The numbered-rule discipline (foundation); whenever a numbered rule is cited, or when you need the letter of the rule | discipline dispute / "which rule says that" |
| `references/skill-usage.md` | Skill capability discovery / registration mechanism + load-decision routing + progressive vs. full-read classification | choosing among skills / front-end or design work / no skill available locally / weak-model handling |
| `references/workflows.md` | Master-sequence details, status-clarification flow, 9 task-type workflows, reuse chain, quality-gate details | fuzzy state / unknown task type / plan-quality doubt / product-polish diagnosis |
| `references/details.md` | Landing details — concrete engineering rules in 13 categories (environment / frontend / DB / testing / API contracts / ops / code quality / git / sessions·backup·governance / deep-dive from real dev logs / iron laws & agent discipline / source-project deep-dive / blog-CMS backflow); load by category when a step needs the specific how-to | symptom keyword matches a pitfall category (build tool / framework version / a11y / API shape / deploy …) — **check here BEFORE improvising in an unfamiliar area** |
| `references/security.md` | Secrets red line, incident response, production safety red lines, rollback procedure details, prompt-injection defenses, supply-chain/SBOM | secrets touched / suspected leak / publishing / dependency procurement |
| `references/never-list.md` | The bright-line "never" list — quick self-check before starting, committing, or risky operations | before commit / before any L3 operation |
| `templates/workspace-memory-template.md` | Initialize a project's `memory/` skeleton (state/experience/preferences/task-log) when the session-start scan finds it missing | project has no `memory/` yet |
| `references/new-project-bootstrap.md` | First task of a NEW project (no `memory/`, no reference project known): create memory skeleton, register reference repos/skills, set the project strictness tier (S1-S3), and write first-experience on day one | project root has no `memory/` / new project / migrated workspace |

Do not preload all references — load only the one the current step needs. **You cannot detect context compaction yourself — do not rely on sensing it; rely on two guards:** (a) explicit signal — the user says "reload / you were compacted / start fresh", or the platform visibly reset the context → **follow the reload sequence immediately**: ① re-read this SKILL.md; ② re-read the memory file (`memory/`, see §10); ③ re-read any reference the current step still needs; ④ restate the current task + acceptance criteria to the user before continuing; (b) milestone self-check — before starting a task, committing, or a major decision, recite the core elements (master-sequence steps, current mode, rollback rule, ask-before-acting); if you cannot restate any of them in full, treat it as missing context and reload before continuing.

## 10. Records & knowledge discipline (summary)

Full detail in `references/rules.md` (rules 30-38) and `references/workflows.md` (memory-file protocol). **Unified archive location = project root `memory/`** (default; a project may override to `.agent-records/` in its rule file). Any session (incl. the next AI) scans this directory on start; create the directory / skeleton if missing.

- **Workspace `memory/` unified cross-session memory**: `state.md` (goal / decisions / constraints / progress, ≤1 screen), `experience.md` (pitfall log: symptom → root cause → fix → prevention), `preferences.md` (confirmed stack / language / style), `task-log/` (records `YYYY-MM-DD-<name>.md`).
- **`state.md` is a skeleton, not a diary — hard cap ≈ one screen (~10KB)**. It holds current phase / next step / leftovers / redlines only. When the session-start scan finds it over one screen: **archive milestone history to `memory/archive-YYYY-MM.md` before starting work** (move, not delete) — a bloated state file is the single largest standing attention cost every future session pays.
- Every session keeps a **task record** (`memory/task-log/`): understanding → acceptance criteria → decisions → results; **each record carries the platform session id (when exposed) and the commit hash(es) it produced** — this is what makes session→commit→quality traceable without re-deriving it from logs. Write conclusions immediately; archive each step's exit artifacts with the task record.
- An **experience log** is mandatory reading at session start — search `memory/experience.md` by symptom keywords and read only the matching segment; distill recurring / high-rework pitfalls into it.
- At session end, distill 1-5 reusable knowledge points (default 3) in the form scenario → judgment → action; write the knowledge version to the project's knowledge doc, and give a plain-language version to the user.
- **Preference memory + post-write check** — after logging a confirmed preference to `memory/preferences.md`, **actively remind the user to re-check the broad direction**; follow their correction if it drifted. Never put secrets or destructive intent in preferences.
- **Experience backflow (two-strike promotion)** — project-level pitfalls live in the project's `experience.md` first. When the same pitfall is confirmed **twice in one project or in two projects** (symptom matches, root cause same), promote it: distill `symptom → root cause → fix → prevention` in a category-compatible form and file it into **this skill's `references/details.md`** (submit to the skill repo), so every future project's step-2 symptom search hits it. Backflow is a promotion of a stabilized lesson, not a first-instance write — one-off noise never enters the skill.
- **Context order (anti-pollution)**: resident (this core) → session-start read (one screen of `memory/`) → on demand (`references/`, historical `task-log/`) → end-of-session minimal append. `injection-core.md` bakes this in.
- **Completion update order (end-of-session, anti-pollution)** — on finishing: ① minimal verification + self-check → ② update `memory/task-log/<YYYY-MM-DD>-<name>.md` (understanding → acceptance → decisions → result; write conclusions immediately) → ③ update `memory/experience.md` (new or recurring pitfalls; duplicate content lives in one place with cross-reference) → ④ update `memory/preferences.md` (with the preference-review reminder) → ⑤ commit docs and code in the same batch; then distill 1-5 reusable knowledge points (default 3) at session end.
- Docs ship in the same commit as code; a doc may be archived only after a current equivalent exists.
- **Templates** — ready-to-fill templates live in `templates/`: step-9 plan, acceptance criteria, task records, retrospectives, rollback points, prompt-budget, session-start hooks (`templates/hooks/`), review sub-agents (`templates/agents/`) and the workspace-`memory/` skeleton (`templates/workspace-memory-template.md`) — copy & fill; never edit in place.

## 11. v1.12 additions — audit-driven refinements (2026-08-30)

> Source: full-session audit (sess_c0f4df2b, 8 task blocks / 7.5h) + comparison with a mature self-discipline system (GATE / status-surface / P99-style honesty critique). The audit found: soft clauses (memory-first, plan template, product-perspective) degrade without hard hooks; the strongest executions this session were the ones with forced signals (ask-before-acting tool, ci gate, commit discipline). **Each addition below binds a mechanism to a checkable artifact.**

1. **GATE completion block (step-11 exit contract, mandatory).** Every task block ends with one line:
   `GATE: {v=<scope>, cmd=<re-runnable command>, exit=<exit code>, files=<changed files>, lessons=<knowledge points>, exempt=<unverified claims}`
   Re-runnable artifacts outrank self-narration; acceptance authority stays with the user; `approval:never` exempts only tool-level approval, never the confirmation duty. The task-record template carries this as a required field.
2. **Session status surface (end-of-session consistency report, for the user to review — NOT a pass/fail self-declaration).** Report: injected version number; **this session's detail-rule hits — MANDATORY, evidence-based (re-runnable grep line; report 0 as 0 — the 2026-08-30 audit found engineering consumption of details.md = 0)**; symptom-index classes actually opened ([Contract]/[Ops]/...); context budget estimate with the compaction threshold reminder (~150-200K input); unverified claims and open todos. Fixed output shape; nothing here claims "compliant/effective".
3. **A1 — Product-perspective review (step 8) is now mandatory**, not conditional: every L2/L3 plan passes the light five questions — (a) one-sentence user-request decomposition, (b) ≥1 rejected alternative, (c) rework-cost assessment, (d) boundaries & not-do list, (e) 3-5 verifiable acceptance criteria. L3 deepens with the risk-layer evidence (#186).
4. **A2 — Research-scaled matrix (task size × project strictness).**
   - Project strictness tier: **S3 strict** (production / external / security / financial / multi-collaborator / user-named) · **S2 standard** (default) · **S1 loose** (personal / prototype / short-lived).
   - Task size tier: L1 no research · **small-module L2** (≤2 files, single domain, same-shape as existing patterns → code-level research + reuse prior takeaways; internet research only for new tech/new deps/team requirement) · normal L2 / L3 full dual research.
   - Matrix: S3 × small-module = still full research; S2 × small-module = light; S1 × small-module = no internet research. Authoritative section: `references/workflows.md`.
5. **A3 — Prior-takeaway reuse (step 2.5):** confirmed conclusions from this session / this project must be explicitly reused (record a reference line), never re-researched. This is the token-waste fix.
6. **A4 — L2 entry without a plan directive:** user drops a multi-file/cross-module request with no `/plan`-style directive → restate (goal/boundary) + 3 acceptance criteria + one-line triage first; at S3 strictness, ask before starting.
7. **A5 — ExitPlanMode four-item self-check:** acceptance criteria 3-5 / one-line triage / rollback point (or explicit "current clean baseline is the point") / boundaries & not-do list — do not submit the plan missing any.
8. **B — New-project bootstrap:** new reference (`references/new-project-bootstrap.md`): create memory skeleton → register reference repos/skills (may be empty) → set strictness tier S1-S3 → day-one first-experience write ("no experience → normal research → same-day pitfall write-back").
9. **C — Fixed end-of-session back-reference in the injected core** (self-optimization hook): every session end reminds — same pitfall ≥2 times / high-rework experience → backflow into this skill (`references/details.md` two-strike promotion, source repo `D:\Agent工作流启动包\shisan-xinuo-workflow`) AND write this skill's own `memory/task-log`; below threshold → workspace memory only; judgment rule = section 10 above.
10. **Declined (arbitration record):** zero-reference retirement + meta-work KPI (元工作占比) — judged a self-replicating metric (the compared system itself never met its own ≤10% meta-work cap; our audit agrees it is a pitfall, not a remedy). The fixed back-reference (item 9) covers self-optimization without another metric layer.


## 12. v1.14 additions — user preference set, must-read experience tier, context management (2026-08-30)

> Source: user preference directive (11 clauses, merged; user ratified promotion to **skill default** 2026-08-30) + 0-hit audit fallout + this-session verified high-frequency pit families. **These are skill DEFAULTS** — every project starts from them; in the user's own projects the user/project discipline still ranks first per the arbitration order (harmless: the defaults and that rank agree).

### 12.1 Requirement communication has top priority (may exceed platform tooling defaults)
- If the directive is fuzzy — or the user has not yet figured out what they want — **communicate first; do not code until fully understood and confident**. When it matters, this outranks the platform's ask-tool and plan-mode defaults.
- Ask-tool timeout/missed-answer: **prefer cancelling the timeout** where the host supports it; otherwise (host can't) — do not treat the empty answer as an approval: **proceed by researching the project's real implementation + the user's known intent, prepare the closest-to-project optimal/recommended solution, and mark it "pending user confirmation"** for one-shot confirm on return.
- **Every question carries the model's recommended option + the reason.** No open-ended "what do you want"; the core reason = "insufficient preparation + fuzzy requirement is the real pain point of the LLM era" (user's own words, internalized).
- Merge positions: "triage ≠ understanding confirmation" + ask-before-acting + §12.1 = the single highest-tier clause (user-POV rank #1).

### 12.2 Read before writing; restate; then act
- Read the existing project structure & code logic first; never assume from thin air (with the v1.13 §2.5 integration-truth list). Restate a SHORT plan + impact scope: 改哪 (what changes) / 影响什么 (what it affects) / 怎么验 (how verified).
- Details that don't affect core requirements: decide autonomously and **keep going — do not stop frequently to ask**; but **log every autonomous decision + reason** into the task record (§10). The "over-asking kills adoption rate" gotcha applies; red lines never exempted.

### 12.3 Simplest solution, minimal change, root-cause errors, run & walk through, final four-check
- YAGNI hardened: features beyond the request are explicitly rejected and noted ("considered, out of scope") in the task record. Minimal change; never touch unrelated code; verify existing features unaffected.
- Errors: find and explain the root cause FIRST, then fix — bypassing validation or hiding errors is a violation the moment the temptation appears.
- After completion: actually run the core flow (no run = not done); then **walk through as a real user once** (L2-F always; L2-S = smoke the referenced path) and keep fixing usability issues until really usable.
- Before delivery: full four-check — missing requirements / edge cases / temporary code / unrelated modifications (upgrades the pre-commit diff re-read into this checklist).

### 12.4 Experience must-read tier (prevention > cure)
- New `memory/experience-mustread.md`: **TOP ≤10 forced pre-read entries** (hard limit one screen): one-line symptom + one-line countermeasure each (e.g. "@tx/contracts-ui edited → rebuild dist before dependents typecheck"; "api behavior ≠ new code → check uptime/dist then restart ritual"; "ci flaky failure → isolate and run twice to type").
- Promotion rule: same pit **≥3 times** or high-rework cost (higher frequency than the two-strike details promotion) → promote into must-read; demotions/backflows per workflows.md.
- Injection core gains: "session start reads the high-frequency experience TOP list (one screen) BEFORE symptom search — prevention first". The must-read file itself counts in the status-surface hit evidence.

### 12.5 Context management (rule-level, not model self-sensing)
- **Proactively discard**: big outputs (>~40 lines build/test/log) → write file for record, keep only summary + exit code in context; subagent/remote reports → conclusions to record, report body NOT in context; already-archived/committed content → cite path, don't re-paste.
- **Proactively refetch fuzzy things**: uncertain about an earlier decision/field/API/number → check task record/contract/source FIRST; guessing from memory is forbidden (same origin as the integration-truth rule); memory-fuzzy triggers the reload sequence.
- **Periodic context census**: every ~5 task blocks or when tokens hit 40-60% budget — list the biggest context consumers, decide discard/archive, emit one line to the status surface (paired with the v1.13 budget threshold).
