---
name: shisan-xinuo-workflow
description: "A cross-platform engineering-execution skill for AI coding agents with the workflow as its soul and the discipline rules as its foundation: a mandatory universal task operating sequence (research-driven 11 steps, exit-artifact gates per step, status-clarification prelude), dual execution modes, ask-before-acting, quality gates, rollback-before-major-changes, recordkeeping. Use when the user wants a disciplined, auditable, process-driven way of working on Trae, Codex, Claude Code, Cursor, or any CLI agent. Not for domain-specific coding help."
---

# Shisan Xinuo Agent Workflow (十三希诺通用 Agent 工作流)

> **Positioning: workflow is the soul, rules are the foundation.** The universal task operating sequence is this skill's soul — the mandatory skeleton every task advances along. The 43 discipline rules are the foundation — they constrain what each step must observe. The two are **strongly coupled and mutually dependent**: the workflow carries the rules into execution; the rules govern the workflow's steps. Neither can be spared. Skipping the workflow discards the soul; ignoring the rules undermines the foundation.

## 1. When to use / when NOT to use

**Use** for any engineering task (whenever you are doing work, advance along the master sequence in section 2); for disciplined execution, workflow governance, workflow rules, or consistent agent behavior across projects and platforms. Step 0 (section 3) also runs automatically whenever this skill loads.

**NOT for** domain-specific knowledge (frameworks, libraries, APIs) or for replacing project-level conventions — the project's own docs always win where they conflict with this skill.

## 2. Master: Task operating sequence — mandatory universal skeleton (single entry)

> **This is the core of the skill, not a reference item.** Every task must advance along this sequence. Every step has an **exit artifact** — no artifact means the step is unfinished, and the next step may not begin. This is the process gate: checkable, auditable, unskippable.

### 2.1 Prelude: Status clarification (when goals / state are fuzzy)

When the user cannot sort out the project state, the goal is unclear, or step 1 exposes a fuzzy baseline, **first run the clarification dialogue** (`references/workflows.md`, clarification flow): drive a step-by-step interrogation (one question at a time) → map the current state, decompose the problem, lock onto the key lead → produce a **clarification memo (goal / current state / constraints / blockers)** → after user confirmation, return to master step 1.

### 2.2 Mandatory 11-step master sequence (exit artifact per step)

> **The iron law (reuse)**: the best code achieves the most complete function and experience with the least code while meeting the requirements. Reuse whenever possible — style adaptation or secondary development are both fine; **never hand-roll your own components.**

| Step | Action | Exit artifact (must exist before the next step) |
|---|---|---|
| 1 | **Receive the instruction** — first-principles understanding (essence / required / inertia) | One-sentence task essence |
| 2 | **Read the experience log first** — search by symptom / keyword | Hit record (hit → execute per "solve / prevent") |
| 3 | **Survey actual resources** — real code (status evidence) + environment + workspace + available skills / MCP | Status fact list (file / line / conclusion) |
| 4 | **Online survey (mandatory)** — research mature open-source projects / libraries / solutions (not a fallback; a required step for every task); collect **verifiable trust signals** (stars / downloads / maintenance activity / adoption evidence / community feedback / security advisories), never "it's popular online" — listing heat is only a discoverability reference, not a quality signal; what & how to survey in `references/workflows.md` §0.2; record degradation when environment/capability/tool/skill/MCP is missing | Market solution survey record (candidates + trust signals + feedback + security risk + degradation notes) |
| 5 | **Reuse survey (iron law)** — local project → mature open-source projects; reuse whenever possible, style adaptation or secondary development both fine, **never hand-roll components** (five-question chain) | Reuse conclusion (candidates + adaptation plan + build-new reason, only when the whole chain misses) |
| 6 | **Restate understanding** — goal / boundaries / acceptance criteria | User confirmation (continue only when aligned) |
| 7 | **Ask on any doubt** — unclear execution or direction drift → ask and end the turn | Ask / confirmation record |
| 8 | **Product-view review + constraints + L1/L2/L3 triage + rollback point** | Risk triage + rollback-point record |
| 9 | **Plan & acceptance doc** — 3-5 verifiable criteria; goal mode adds budgets and file boundaries | Plan & acceptance doc |
| 10 | **Execute** — per triage; goal mode autonomous per plan, log checkpoints, stop over budget | Execution record / changes |
| 11 | **Self-check & archive** — minimal verification → self-check → docs with code → dual-write knowledge → commit with note | Verification result + archive (docs / knowledge / commit note) |

**Gate**: before entering a step, the previous step's exit artifact must exist and be recorded; steps that legitimately cannot produce one (e.g. genuinely no reuse to survey) must record the reason in the task record — never skip silently.

Details and per-task-type checklists: `references/workflows.md` (master + clarification + 9 task types).

## 3. Step 0: Platform detection & injection (on load / first run)

Before starting tasks, adapt this workflow to the current platform:

1. **Detect the platform** using the feature checklist in `references/platform-adaptation.md` (directory markers, env vars, tool availability).
2. **Ask the injection mode** — use the asking chain from section 4 and let the user choose:
   - **On-demand (default)** — the rule file holds a lean discipline and points back to this skill; the full skill activates when triggered. Lowest context cost.
   - **Forced per-session** — the rule file additionally commands every session to fully read this skill's `SKILL.md` before starting work, so the discipline applies unconditionally each session (higher per-session context cost).
   If no asking tool is available, default to on-demand and say so explicitly.
3. **Configure the injection point — write the rule file into the location the agent app actually auto-injects every session** (see the injection-point table in `references/platform-adaptation.md`: e.g. `CLAUDE.md` for Claude Code, `AGENTS.md` for Codex, `.cursor/rules/*.mdc` for Cursor, app-managed project rules for Trae). A file written only into a workspace folder the app never reads is **useless**. If the platform requires enabling the rule inside the app (e.g. Trae project rules), **guide the user to enable it in the app settings and confirm it is active**; do not claim success until the app confirms it injects the rule.
4. **Pick the active asking mechanism** from the downgrade chain in section 4.
5. Confirm to the user in one line: platform detected, injection mode, injection point confirmed active, asking tool active. Do not start the task until this is done.

## 4. Ask-before-acting protocol

Consequential decisions must be confirmed with the user before acting. Triggers: unclear direction or ambiguity, conflicting requirements, permissions/secret handling, destructive operations (deletion, migration, overwrite, external publishing), architecture or tech-stack choices, scope expansion, conflicting proposals.

**Asking-tool downgrade chain** (use the first available):

1. Platform-native asking tool (`request_user_input`, `AskUserQuestion`, `ask_user`, …)
2. If unavailable: structured text protocol — present (a) understanding, (b) options with pros/cons, (c) risks and consequences, (d) a recommendation, then **end the turn and wait**. Full protocol in `references/platform-adaptation.md`.

Routine L1 tasks do not require asking — do not over-ask. High-risk L3 tasks always require asking.

## 5. Execution modes & task triage

### Dual modes (default = normal mode)

| Mode | Trigger | Behavior |
|---|---|---|
| **Normal** (default) | no keyword | Ask before every consequential decision (section 4). |
| **Goal mode** | keywords `目标：` / `目标模式` / `无人值守` / `goal mode` / `unattended` | Work autonomously from a written plan; secrets and destructive operations still pause and wait for the user. |

Goal-mode extra duties: write a plan (scope, risk rating, time/round budget) *before* executing; split subtasks by file boundaries; record progress as you go; stop automatically when the budget is exceeded; deliver a retrospective plus an open-questions list.

### Task triage L1 / L2 / L3

| Level | Criteria | Normal mode | Goal mode |
|---|---|---|---|
| L1 routine | small, reversible, low impact | do it directly | do it directly |
| L2 medium risk | new feature, multi-file, cross-module changes | record, do, report key points | execute per plan, log checkpoints |
| L3 high risk | secrets, permissions, data deletion, migration, external publishing, architecture choice | **ask first** | pick the recommended option, label it `REVIEW:` and log it; secrets / destructive ops: pause, log, wait for the user |

Judge by: blast radius, reversibility, rework cost, whether data or external publishing is touched.

## 6. Minimal closed-loop delivery (the delivery principle of step 11)

1. **Understand** — restate the goal, boundaries, and acceptance criteria in 1-3 sentences.
2. **Minimal change** — modify only what the task requires. Prefer existing code, dependencies, platform-native capabilities, and existing open-source solutions over writing new ones (five-question reuse chain in `references/workflows.md`).
3. **Minimal verification** — run the smallest check that proves the change works (lint / type-check / tests — the project's own baseline).
4. **Deliver the finished thing** — no half-done work and no placeholders. Anything unfinished must be explicitly labeled (`TODO`, `NOT IMPLEMENTED`, `UNVERIFIED`). **Never fake completion.**

## 7. Quality gates & rollback

- Before committing: re-read the diff as a reviewer (boundaries, security, readability, unverified claims, reuse), re-run validation, and ship docs in the same commit as code.
- **Rollback rule — create a rollback point BEFORE major changes or irreversible operations.** Git-tracked files: confirm a clean worktree, then commit/stash the current state (or work on a separate branch). Non-git files: copy a snapshot first. Run high-risk commands only after a rollback point exists.
- External publishing: user approval first, then an observation period (~30 min) monitoring errors/latency/alerts; roll back on anomaly.

## 8. Gotchas

- **The sequence is unskippable.** Survey (step 3) and reuse survey (step 5) are the most-skipped steps — skipping breaks the sequence and is the most common violation.
- **Trigger keywords are live switches.** Goal-mode keywords (`目标：`, `unattended`, …) silently change the decision model. Check every user message for them, including mid-task messages.
- **Never overwrite an existing rule file** (`AGENTS.md`, `CLAUDE.md`, …). Backup + merge only.
- **User idea vs code conflict** — code and measurements win. Say so plainly; never silently execute a wrong instruction.
- **No native asking tool?** The most common failure is charging ahead instead of using the text protocol and ending the turn. Ask first, act never.
- **Over-asking kills adoption.** Repeated confirmation on L1 work gets this skill disabled. Default: act on L1, ask on L3.
- **Skill loaded ≠ task started.** The master sequence in section 2 is mandatory even when the user's message looks trivial.
- **Secrets** (keys, tokens, passwords) never go into code, docs, commits, or chat. Scan before committing; rotate immediately on leak.
- **Keep records at the time of analysis, not at cleanup.** Conclusions written late get lost in long sessions.

## 9. Reference map — load on demand only

| File | When to load |
|---|---|
| `references/platform-adaptation.md` | Section 3 platform detection; asking-tool downgrade chain; full structured asking protocol |
| `references/rules.md` | The 43-rule discipline (foundation); whenever a numbered rule is cited, or when you need the letter of the rule |
| `references/workflows.md` | Master-sequence details, status-clarification flow, 9 task-type workflows, reuse chain, quality-gate details |
| `references/security.md` | Secrets red line, incident response, production safety red lines, rollback procedure details |

Do not preload all references — load only the one the current step needs. **You cannot detect context compaction yourself — do not rely on sensing it; rely on two guards:** (a) explicit signal — the user says "reload / you were compacted / start fresh", or the platform visibly reset the context → immediately re-read this SKILL.md and any references you still need; (b) milestone self-check — before starting a task, committing, or a major decision, recite the core elements (master-sequence steps, current mode, rollback rule, ask-before-acting); if you cannot restate any of them in full, treat it as missing context and reload before continuing.

## 10. Records & knowledge discipline (summary)

Full detail in `references/rules.md` (rules 30-38) and `references/workflows.md`. Essentials:

- Every session keeps a **task record** in the project's defined location: understanding → acceptance criteria → decisions → results. Write conclusions immediately; archive each step's exit artifacts with the task record.
- At session end, distill 1-5 reusable knowledge points (default 3) in the form scenario → judgment → action; write the knowledge version to the project's knowledge doc, and give a plain-language version to the user.
- An **experience log** (lessons learned, pitfalls) is mandatory reading at session start — search by symptom keywords. Its location is defined by the project; this skill does not impose one.
- Docs ship in the same commit as code; a doc may be archived only after a current equivalent exists.
