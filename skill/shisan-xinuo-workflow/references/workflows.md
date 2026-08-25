# Task-Type Workflows & Quality Gates (English)

Load this file when starting work that matches one of the task types below, or when SKILL.md cites a workflow. Each flow is a checklist — track progress against it.

## 0. Prelude & master — mandatory sequence (run before ANY task type)

### 0.0 Status clarification (run first when goals / state are fuzzy)

**Triggers**: "can't sort this out / project is a mess / unclear where things stand / where do I even start / help me organize / what's next / should I do X / I'm a bit lost"; or master step 1 exposes a fuzzy baseline.

- [ ] 1. Empathize & frame: restate the user's situation and stuck feeling in one line; declare the clarification dialogue
- [ ] 2. First question: start at the highest-leverage point (usually "what is the result you want / what is blocking you")
- [ ] 3. Drill layer by layer: follow up per answer (3-5 causal layers, explicit constraints/assumptions, convert obstacles into the real problem), 1-2 questions per round
- [ ] 4. Offer leads: give observed leads/hypotheses for the user to verify, avoid question fatigue
- [ ] 5. Converge & structure: stop when enough info; produce a clarification memo (goal / current state / constraints / blockers)
- [ ] 6. Plan together: structured action plan (goal → priorities → next steps); after confirmation, return to master step 1

### 0.1 Mandatory master sequence (11 steps, exit-artifact gates)

Exit artifacts per step are in SKILL.md §2.2; the previous step's artifact must exist before the next step; legitimate skips must record the reason in the task record, never silently.

- [ ] 1. Receive instruction (artifact: one-sentence task essence)
- [ ] 2. Read the experience log first (hit record)
- [ ] 3. Survey actual resources (status fact list)
- [ ] 4. Online survey (mandatory) (market solution survey record)
- [ ] 5. Reuse survey (iron law) (reuse conclusion)
- [ ] 6. Restate understanding (user confirmation)
- [ ] 7. Ask on any doubt (ask record)
- [ ] 8. Product-view + constraints + triage + rollback point (triage + rollback record)
- [ ] 9. Plan & acceptance doc (plan & acceptance doc)
- [ ] 10. Execute (execution record)
- [ ] 11. Self-check & archive (verification result + archive)

## 1. New feature / new project (15 steps)

- [ ] 1. Startup self-check (platform adapted, rule file active)
- [ ] 2. Read project rules and the relevant task-type flow
- [ ] 3. Read project docs (goals, architecture, module docs, test baseline)
- [ ] 4. Restate understanding: goal / boundaries / acceptance
- [ ] 5. First-principles analysis: essence of the task
- [ ] 6. Convert goal obstacles into the real problem to solve
- [ ] 7. Identify constraints & hidden assumptions; verify each
- [ ] 8. Product view first: is this feature necessary from the experience/behavior angle
- [ ] 9. Reuse decision chain (five questions, below)
- [ ] 10. Research existing open-source wheels before self-building
- [ ] 11. Follow-up questions for ambiguous requirements
- [ ] 12. Write 3-5 verifiable acceptance criteria
- [ ] 13. Plan (and TDD where the project uses it)
- [ ] 14. Implement
- [ ] 15. Verify (lint / type-check / baseline tests), safety & performance gates, independent review, commit code+docs together, confirm acceptance, update docs/log

## 2. Bug fix & troubleshooting (7 steps)

- [ ] 1. Search the experience log by current symptom keywords (mandatory; on hit apply "solution / prevention")
- [ ] 2. Miss? Also search dev log / task records for the same issue
- [ ] 3. Reproduce the problem
- [ ] 4. Root-cause it: systematic debugging + causal chain (3-5 layers of why, verify each link)
- [ ] 5. Write a regression test
- [ ] 6. Minimal fix
- [ ] 7. Verify all green; record the pitfall (distill into experience log if repeated / high-rework-cost)

## 3. UI / design rework

- [ ] 1. Product-view review (brand 3 questions: positioning / success criteria / structural constraints; user-journey layers: discover → judge → trust → connect)
- [ ] 2. Read the project's design spec and component reuse list
- [ ] 3. Check component reuse (five questions); if missed, self-build + record the reason
- [ ] 4. Visual review (screenshots / vision tool comparison)
- [ ] 5. Implement per spec (whitelist guardrails)
- [ ] 6. Verify in both viewport widths with screenshots
- [ ] 7. Accessibility & performance checks
- [ ] 8. Record the rework in the project rework doc

## 4. Deploy & operations

- [ ] 1. Build locally (follow the project's build command)
- [ ] 2. Package and upload
- [ ] 3. On server: unpack + migrate + reload process
- [ ] 4. Prepare the rollback plan (rollback point rule 43)
- [ ] 5. Health checks and alert wiring
- [ ] 6. Publish approval + observation window (~30 min), monitor errors / latency / alerts
- [ ] 7. Alert response: confirm → classify → locate → dispose → review
- [ ] 8. Backup/restore drill on a schedule
- [ ] 9. Record the deployment

## 5. Documentation & handover

- [ ] 1. Update authoritative docs in the same commit as code
- [ ] 2. Register every newly referenced external site / open-source project / tool in the project's reference-resources doc
- [ ] 3. Update the handover checklist
- [ ] 4. Record lessons learned
- [ ] 5. Self-check consistency (key numbers match the project's authoritative docs)
- [ ] 6. Archive check (equivalence precondition, rule 37)

## 6. Major decisions & complex tasks

- [ ] 1. Recognize the trigger (direction / architecture / scope / conflict)
- [ ] 2. Build a decision brief: understanding + options comparison + pros/cons + consequences + recommendation （TOC thinking: constraints and hidden assumptions first, then compare options around the constraint)
- [ ] 3. Ask via the asking tool or text protocol; end the turn and wait
- [ ] 4. Execute the confirmed direction
- [ ] 5. Review and record the decision

## 7. Goal mode / unattended run

- [ ] 1. Confirm goal and mode with the user
- [ ] 2. Write the execution plan with risk rating into the task record (time / round / cost budgets; subtasks split by file boundaries, isolated writes)
- [ ] 3. Triage decisions by L1/L2/L3 (SKILL.md §4)
- [ ] 4. Execute autonomously, record everything; stop automatically past budget
- [ ] 5. Retrospective delivery + open-questions list; commit/push with explanation

## 8. Multi-session orchestration

- [ ] 1. Trigger: roadmap / handover-list status summary marks the task as multi-session
- [ ] 2. Read the orchestration authority line for this session's number and topic
- [ ] 3. Each session: own branch + task record (restatement / risk rating / 3-5 acceptance criteria)
- [ ] 4. Before starting and before committing: check `git status` and target-file mtimes; pause and coordinate on uncommitted concurrent edits
- [ ] 5. Execute and close per this session's acceptance criteria
- [ ] 6. Update the handover checklist completion block and status summary; refresh baseline numbers
- [ ] 7. Commit/push (re-read diff — only this session's files), merge
- [ ] 8. Next session continues from "Next step"; avoid overloading one session

## 9. Adding a new workflow rule (6 steps, no landing without user approval)

1. **Collect** — run the rule-index listing (numbers / titles / references) as the dedupe baseline.
2. **Analyze (five questions)** — necessity / consequence of violation / executability / duplication (pre-check suspected duplicates) / ripple scope (which docs must sync).
3. **Draft (four-paragraph template)** — source ｜ problem it solves ｜ consequence of violation ｜ relationship to existing rules; numbered after the current section; mark the solidification date.
4. **Approve** — present the candidate (with five-question conclusions and suspected-duplicate list) via the asking tool; user may approve / modify / veto; no answer or veto = no landing.
5. **Land & re-check** — append the entry → index integrity check green → sync affected docs.
6. **Record & commit** — task record carries the five-question conclusions / approval record / verification result; commit message states change + verification.

## Reuse decision chain (five questions)

Before building anything new, answer in order; only a full miss allows self-building (and then record the research conclusion):

1. **Is the feature necessary?** Judge from the product view first (experience & visible behavior win over feature design); no real user-facing value → don't build.
2. **Does the platform support it natively?** (HTML/CSS/browser APIs first: dialog, Popover, details/summary, Clipboard, scroll-behavior, `:has()`, native drag…)
3. **Can existing stdlib / component library cover it?** Prefer the current project's component library and home-grown kept components.
4. **Can an existing dependency cover it?** Prefer already-installed dependencies; don't install duplicates.
5. **Can it be done with the least code?** Prefer composing existing components (ideally one-line-level composition).

## Quality gates

- **Pre-commit:** lint / type-check / unit+integration tests (project baseline is authoritative; baseline regression blocks) / coverage (core ≥ 80% target) / dependency audit (before release) / commit message (header ≤ 100 chars) / docs shipped with code (`git status` check).
- **CI:** every push runs lint + type-check + guardrails + unit + integration; releases additionally run E2E + performance.
- **Review loop:** reviewer-view diff re-read (boundaries / security / readability / unverified items / reuse & least code / product view); fail → fix → re-run (max 3 rounds) → still failing: stop and report; requirement change mid-way: record impact first.
- **Safety:** secret scan before every commit (CI mandatory); leak emergency: revoke/rotate → map exposure → record review.
- **Periodic:** monthly dependency maintenance / workflow retrospective / memory upkeep; quarterly skill audit & doc reconciliation.

## Notes on tools & skills strategy (generic)

- Load at most 1-3 skills per task, filtered by catalog first.
- No skill available does not block: fall back to general capability + official docs; record the fallback.
- Repeated needs (2-3 times) become new skills via workflow 9.