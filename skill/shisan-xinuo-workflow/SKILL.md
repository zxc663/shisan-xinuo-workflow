---
name: shisan-xinuo-workflow
description: "One-line positioning: forces every engineering task through an auditable agent workflow — mandatory research-driven 11-step master sequence + L1/L2/L3 closed-list quick triage + dual modes (normal/goal), with platform-agnostic hard injection of the core discipline. Use on any hands-on task."
license: MIT
compatibility: "Trae, Codex, Claude Code, Cursor, Windsurf, WorkBuddy and any CLI encoding agent supporting the Agent Skills standard"
metadata:
  version: 1.17.0
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

> **Reading order**: §1 use-musts → §2 executable lanes → §3 platform → §4 ask protocol → §5 triage & split → §6 close loop → §7 gates → §8 gotchas → §9 references → §10 records → §11 status surface → §12 quick-execution table.
> Every section is written **trigger → steps (checklist) → template → check → boundary**. If a step needs "interpretation", it does not belong here — report it (Paper-blind-test rule).

## 0. Meta-rules for reading this skill

- **Trigger first**: a rule applies only when its trigger fires. Trigger not met → skip.
- **Steps are checklists**: one performable action each, in order; a step you cannot act on = reload context (§9) or ask (§4).
- **Templates are copy-paste**: fill the one-line template and keep it in the named artifact.
- **Boundary says what is NOT done here**: ask-before-acting & red lines are never waived by any other rule.

## 1. When to use / when NOT to use

- **Use**: any hands-on engineering task (then advance along §2 lanes). **NOT a substitute for** learning a framework/API from its own docs; the project's own docs win where they conflict with this skill.
- **Honest note on details.md**: it is a **pitfall log** ("what went wrong there"), not a domain tutorial; the workflow/rules/gates layers are framework-agnostic.

## 2. Master: task operating sequence — executable lanes

**Trigger**: a hand-on task; you are the actor.
**Lane pick (10 seconds)**: run §5 triage → L1 / L2-S / L2-F.

### 2.1 L1 fast lane (small, reversible, low impact)

1. Restate in one sentence (goal/boundary). 2. Make the minimal change. 3. Run the minimal verification command, record exit code. 4. Report in one line.
**Template**: `L1 fast path: 改 X → "cmd"(exit=0) → done.`
**Check**: □ restate recorded □ cmd reruns clean □ task record marked "L1 fast path".

### 2.2 L2-S short workflow (default for small modules)

**Trigger**: ≤3 files, single domain, same shape as existing patterns; §5 three questions <2 yes.
1. **Integration-truth survey (mandatory, never skipped)** — table before any write:
   | 模块 | API/端点 | 对接方式 (path/method/envelope/fields/package) | 证据来源 (source:line / contract / docs) |
   |---|---|---|---|
   Fill rule: grep call site → read schema/type → confirm package ownership → then write. Naming intuition is banned (2026-08-30 counter-examples: envelope unwrap, `api.get`→ApiResponse, recharts wrong workspace, Nest DI name).
2. Restate 改哪 / 影响什么 / 怎么验 (3 short lines).
3. No plan doc: single file → do it; ≤3 files → one line "change + acceptance + rollback baseline".
4. Execute + minimal verification (rerunnable, capture exit).
5. GATE line (§7) + status-surface contribution (§11).
**Check**: □ integration table rows have evidence source □ 3 acceptance criteria are verifiable (number/visible state/rerunnable check) □ GATE cmd reruns.
**Boundary**: skips internet dual-survey / deep five-questions / plan doc / repeated asking — but ask-before-acting & red lines are NOT waived; direction/boundary ambiguity → §4.

### 2.3 L2-F full 11-step master (large modules)

**Trigger**: §5 three questions ≥2 yes, or any L3.

| # | Step (trigger → action) | Exit artifact (template) |
|---|---|---|
| 1 | Receive instruction → distill essence | one-line task essence |
| 2 | Experience search: read `memory/experience-mustread.md` (TOP ≤10) FIRST + symptom-grep `experience.md` hot segment | hit-records; 0 hits → note "no prior experience" |
| 3 | Reality survey: read structure/contracts + integration-truth table (§2.2) + module list with **real status** (done/planned/not-started) | fact list (file:line) |
| 4 | Online survey: candidates + trust signals (stars/activity/adoption/community/security) | survey record (`degraded-offline` tag if no net) |
| 5 | Reuse decision (local → mature OSS; five-question chain; self-build only if all empty + reason) | reuse conclusion |
| 6 | Restate understanding (goal/boundary/acceptance) | user confirmation |
| 7 | Ask anything unclear (§4) — no code before clarity | ask/confirm record |
| 8 | Product-view five questions (mandatory): one-line user-request decomposition / ≥1 rejected alternative / rework-cost / boundaries+not-do / 3-5 acceptance | five-question record (+ L3 risk-layer evidence) |
| 9 | Plan doc (plan-template: acceptance 3-5 verifiable + rollback point; goal-mode adds budgets/file borders) | plan |
| 10 | Execute with checkpoints; goal mode auto-stop over budget | execution record |
| 11 | Verify (rerun core flow) → real-user walk-through → five-check → GATE → archive (§10) → commit | GATE + records |

**Check**: □ every exit artifact exists before next step □ rollback point before disruptive work □ GATE cmd reruns exit 0.

### 2.4 New project / first load — project information doc

**Trigger**: first task in a workspace with no docs/指导说明 (or fragmentary).
1. Create `docs/project-info.md` (index-style if docs already cover parts — never duplicate content).
2. Six sections: ① architecture (shape/package boundaries/one-line data flow) ② goal planning (summarized from the user's description, staged) ③ module table `模块 | 真实状态(已实现/规划中/未实现) | 关键描述` (real status is the lifeline — never mark planned as done) ④ research navigation (this doc's purpose: research these / skip those, by status×change surface) ⑤ reference resources (name+purpose+path, reusable later) ⑥ restate to the user for confirmation (signature column).
3. Each session: minimal-diff update (status/goal/new resources) + note in task record.
**Check**: □ six sections □ status factual □ restate confirmed by user □ updated this session if changed.

## 3. Step 0: Platform detection & injection

**Trigger**: first run on a platform.
1. Detect platform → injection point (Trae `~/.trae-cn/user_rules/*.md` | Codex `AGENTS.md` | Claude `CLAUDE.md` | Cursor `.cursor/rules/*.mdc` | Windsurf `.windsurfrules` | WorkBuddy `BOOTSTRAP.md`).
2. Write injection-core core (≤~55 lines) — merge, never overwrite; backup `<file>.bak-<date>` first.
3. After write: re-read injected copy → three-way consistency (SKILL §5.2 block = injection-core = injected copy).
**Boundary**: never preload references.

### 3.1 Skill self-update protocol (three-way merge, user-local wins)

**Trigger**: this skill updated upstream; user asks to pull/update (or status surface shows version mismatch).
1. Run `python scripts/syncer.py` (repo root): it does ① health-diff (finds user-owned files in the installed copy) ② backup `.bak-<ts>` ③ migrate non-source files (e.g. `personal-playbook.md` → `user-notes/`) ④ overwrite upstream (SKILL/references/templates) ⑤ write change-list + dual task-log (repo `memory/task-log` AND installed-copy `memory/task-log`).
2. Merge policy (layer table): source-authoritative (triage block/red lines/ask protocol — three-way consistency) → upstream wins; **user rules in `user-notes/` + `memory/` → NEVER touched (local user wins)**; coexist files → both kept; unresolvable conflict → keep local + mark `CONFLICT` in list for user.
3. Never edit in place by hand: any manual edit to installed copy belongs in `user-notes/` (else the next sync overwrites it).
**Check**: □ script ran with exit=0 □ change-list exists (both logs) □ user-notes/ & memory/.bak untouched □ version line updated in both copies.


## 4. Ask-before-acting protocol

**Trigger**: direction/boundary/conflict/permission/secrets/destructive/architecture/scope-expansion fuzzy — or "triage ≠ understanding confirmed".
**Steps**:
1. Never code first: trigger fires → stop and ask before implementation.
2. Every question carries **recommended option + core reason + consequence of alternative** — never open-ended "what do you want?" Core reason to state: "insufficient preparation + fuzzy requirement is the real pain point" (user wording, internalized).
3. Ask via platform question tool; if none → structured text protocol (understanding + options pros/cons + risks + recommendation), then end turn.
4. Timeout/empty-answer: prefer cancelling the wait (host support); if not — **do not treat empty answer as approval**: research real implementation + known intent → produce closest-to-project recommended solution → mark **"pending user confirmation"** for one-shot confirm.
5. After answer: confirmed → act; redirected → re-split (§5); rejected (not what they wanted / workflow wrong) → **rejection log** (§12 R1).
**Check**: □ recommendation+reason in question □ no implementation before clarity □ empty-answer path = research+pending-confirm, never silent action.

## 5. Execution modes & task triage

### 5.1 Modes
- Normal (default): every major decision asks; understanding-not-sure asks.
- Goal (`目标：`/`目标模式`/`无人值守`/`goal mode`/`unattended`): per written plan; pause only for L3-major or hard block; else decide → research-first → recommend → archive; rollback local-first, no push by default.
- Quiet (`安静模式`/`quiet`/`quiet mode`): L1 report result only; L2/L3 unchanged; secrets/destructive still ask.
**Check**: □ mode keyword present? □ mode obligations in task record.

### 5.2 Triage (10 seconds) + flow split

| Question (answer these 3) | Yes count | Lane |
|---|---|---|
| ① ≥3 packages / spans api+contracts+frontend? ② contracts/architecture/migration/publish/security? ③ user named "follow the workflow / strict analysis"? | **≥2** → **L2-F** (§2.3) |
| | else → **L2-S** (§2.2) |
| L1: small/reversible/low impact | always | L1 (§2.1) |
| L3 closed list (secrets/permissions · data deletion · data/service migration · external publish · architecture choice · over-budget destructive) | always ≥ | L2-F + pause line (ask; local backup never replaces confirmation) |
**Check**: □ one-line triage in task record □ L2-F boundary templates written (new endpoint+contract+two pages / architecture / migration / secrets+publish / multi-module joint).

## 6. Minimal closed-loop delivery (step 11 essence)

1. Run the core flow for real — **no run = not done**.
2. Walk through as a real user once (L2-F always; L2-S smoke the referenced path); fix usability issues until actually usable (multiple rounds allowed).
3. Six-report: what ran / exit code / what changed / unverified (exempt) / knowledge points / user-visible errors logged to the log module.
**Template**: GATE (§7).

## 7. Quality gates & rollback

**Trigger**: before commit / before disruptive change.
1. **GATE block** (per task block): `GATE: {v=<scope>, cmd=<rerunnable cmd>, exit=<exit code>, files=<changed files>, lessons=<knowledge points>, exempt=<unverified claims>}`.
2. **Five-check before delivery**: missing requirements / edge cases / temporary or commented code / unrelated modifications / **errors logged to the log module** (grep `console.` / empty `catch {}` in diff = zero tolerance when a log module exists).
3. **Rollback point**: git tracked → clean tree + commit/stash/branch BEFORE disruptive work; record the line ("current clean baseline is the point" allowed).
4. **Log-module enforcement**: design line in the integration table (`报错→哪种日志/级别/谁调/文案同源`); catch triple = log + user-visible fallback + (if needed) audit trace; user-visible message and log message stay in sync.
**Check**: □ GATE cmd reruns with recorded exit □ five-check done □ red line never crossed (`approval:never` exempts tool-level approval only, never confirmation duty).

## 8. Gotchas

- Same-session no-reload: already-loaded content not re-read unless compacted / explicit / source changed.
- Main flow: no step skipping; the survey steps are the most-skipped — use lanes instead.
- Over-asking kills adoption: decide non-core details yourself (§12 P4) and keep going.
- Skill load ≠ task start.
- Secrets never in code/docs/commits/dialogue; leak → rotate immediately.
- Regression ≥3 or high-rework → promote to must-read (§12 P2).

## 9. Reference map — load on demand

**Trigger**: a step needs the specific how-to, or an error matches a symptom class (banned: preloading).
1. Read the map (below), open ONLY the matched file by category.
2. **Mandatory error-time entry point**: on error / unexpected API shape / unknown field or endpoint / new dependency not working → FIRST search `details.md` symptom class (e.g. build-tool, [Contract], [Ops]) then change code; on hit, one reference line into the task record.
3. After use: one citation line (`细则 #N 命中：…`).

| reference | content | trigger |
|---|---|---|
| injection-core.md | platform-injected core (triage/11-step/modes/red lines/update order) — always in context | every session (injected) |
| workflows.md | task-type flows & quality gates (§0 preludes incl. product-view & research matrix) | step-8/9 quality doubts |
| details.md | concrete pitfall entries, 13 classes, symptom index | symptom keyword matches (build tool / framework version / API shape / deploy …) |
| rules.md | 47 numbered discipline rules (8 groups) | discipline disputes |
| security.md | 6 production red lines + open-source install check + response plans | secrets/publish/supply-chain |
| never-list.md | bright-line never list (7 groups) | before commit / before L3 |
| skill-usage.md | skill discovery/loading rules | multiple skills / front-end class load |
| personal-playbook.md | personal-zh only: 11 stack symptom→root→fix→prevention tables | personal edition start / troubleshooting |

**Check**: □ matched file only □ citation line if used □ preloading avoided (0-hit audit evidence: engineering consumption of details.md = 0; entry point above is the fix).
**Boundary**: details.md = pitfall log, not tutorial.

## 10. Records & knowledge discipline

**Trigger**: session start / block end / session end.
- **Session start**: read `memory/` one screen — `experience-mustread.md` TOP FIRST (≤10, one-line symptom + one-line countermeasure; ≥3 hits or high-rework promotes; two clean periods demotes), then `state.md`, then `experience.md` symptom search.
- **Block end**: task record append (understanding → acceptance → decisions → results → GATE) — timestamp **`YYYY-MM-DD HH:mm:ss`** (seconds REQUIRED; day-granularity counts as incomplete).
- **Session end**: ① minimal verification + self-check ② task-log ③ experience (new/recurring; one copy, cross-ref) ④ preferences (+ remind user to re-check direction) ⑤ commit docs+code together; then distill 1-5 knowledge points (default 3).
- **Live header check**: header `更新：` timestamp must be ≥ newest body entry; updating body without header = violation.
- **Record size cap**: task record >~120 lines or >3 task blocks → new file (`-名称-2.md`) or archive.
**Check**: □ must-read read before work □ timestamps to seconds □ live-header consistent □ record within cap.

## 11. Session status surface (end-of-session consistency report — user review; NOT compliant/effective claim)

```
注入版本: 1.17.0
细则命中: grep -cE 'references/details|#2[0-9][0-9]\.' <session outputs> → N（0 照报 0）；打开类: [Contract]×N / [Ops]×N
上下文预算: ~X tokens（阈值 150-200K → 压缩+重载序）
版本一致性: 副本 vs 源库（不一致 → 跑 syncer.py）
未验证/待办: <exempt 与未完成项——必须是真待办，不得留「已完成却未清」的陈旧注记>
```
**Rules**: evidence-based not self-claimed; timestamps to seconds; pending items must be real.

## 12. Quick-execution table (v1.12-1.15 clauses as executable one-liners)

| id | 触发 | 动作 | 模板/自检 | 边界 |
|---|---|---|---|---|
| G1 | task block ends | write GATE line | `GATE: {v,cmd,exit,files,lessons,exempt}`; cmd reruns | — |
| S1 | session ends | status surface (§11) | three lines | not a pass/fail claim |
| A1 | L2/L3 plan | five questions (§2.3 step 8) | decomposition/rejected alt/rework/boundary/acceptance | L3 adds risk evidence |
| A2 | research | strictness tier S3/S2/S1 × task size | S3×small=full; S2×small=light; S1×small=no internet | — |
| A3 | confirmed conclusion in-session/project | reuse + one reference line | no re-survey | — |
| A4 | L2 request without /plan | restate + 3 acceptance + triage | §2.2 step 2 | S3 → ask first |
| A5 | exit plan mode | four-item check (acceptance/triage/rollback/boundaries) | don't submit missing any | — |
| B | new project, no docs | project-info.md six sections (§2.4) | user confirms restate | index, not duplicate |
| P1 | fuzzy intent | communicate first; ask with recommendation+reason; empty-answer → research+pending-confirm | §4 | never treat empty answer as approval |
| P2 | same pit ≥3 | promote to experience-mustread.md; 2 clean periods → demote | one-line symptom + one-line countermeasure | one copy only (cross-ref) |
| P3 | big output >~40 lines / subagent report | file + summary only; conclusions only; cite path instead of re-paste; census per ~5 blocks | context-census line | fuzzy → refetch record/contract/source |
| P4 | non-core detail | decide + keep going | log decision+reason | core/boundary/red-line → ask |
| P5 | error found | root cause first, then fix | grep zero tolerance | bypass/hide = violation |
| P6 | done | real run + real-user walk (L2-F) / smoke referenced path (L2-S) | fix until usable | no run = not done |
| P7 | delivery | five-check (req/edge/temp/unrelated/log-module) | §7 | — |
| R1 | plan rejected / user redirects | rejection log: original wording + implicit need → preference (preferences.md) or requirements change (task record) → backflow | one line each | rejection is gold, not noise |
| R2 | user pastes big code/styles | ask first: "evidence or requirement?" | handle per answer | never guess intent from paste |
| R3 | task block done | session board line (done ▸ in-progress ▸ pending-confirm ▸ review point) | top of task record | user can check anytime |
| R4 | block end | stop-check: need user input / all done / risk-publish surfaced — else continue | 3-stop checklist | "continue" cost counts |
| R5 | updating memory | live header check | header ts ≥ newest body ts | — |
| R6 | record grows | >120 lines or >3 blocks → new file/archive | `-名称-2.md` | — |
| DC | module has log module | design line in integration table; catch triple; five-check #5 | log+fallback+audit | console-only/silent = violation |
| TS | any record | timestamp `YYYY-MM-DD HH:mm:ss` | seconds required | day-only incomplete |
| ZE | user types meaningless `zxc663` | self-check reply:「十三希诺工作流已应用，注入方式是：［按需 / 硬注入］，已经应用 N 轮会话/对话（N=按任务记录/文档数快速统计）｜源库 vX vs 副本 vY（不一致 → 建议跑 syncer.py）」 | no action beyond version compare | pure test trigger |

## Templates

Ready-to-fill templates live in `templates/`: plan / acceptance-criteria / task-record (GATE field) / retrospective / rollback-point / prompt-budget / workspace-memory / session hooks / review sub-agents. Copy & fill; never edit in place.

---

*Style note: if you found a paragraph that needs "interpretation", report it — the Paper-blind-test rule (v1.16) says it does not belong.*
