# New-project bootstrap (English · v1.12, 2026-08-30)

> When the first task is about a workspace where any of these hold, run this BEFORE master step 3: no `memory/` dir · no reference project/repo known · no prior experience entries · a migrated workspace. Goal: make the "research-on-demand" matrix and the step-2 experience search have a ground to stand on, and fail loud when they don't.

## Run order (first task only)

1. **Skeleton** — copy `templates/workspace-memory-template.md` into the project root as `memory/` (state / experience / preferences / task-log). If the project overrides the archive dir (`.agent-records/`), use that instead, and say so in the project rule file.
2. **Register reference slots (may be empty)** — list in `memory/state.md`: reference projects/repos the user pointed to, reference skills installed, key external docs. Empty is fine; the field exists so the next session knows what does NOT exist (fail-loud, not guess).
3. **Set project strictness tier** — S3 / S2 / S1 with the triggers from `workflows.md` §0.5 (S3: production / external / security / financial / multi-collaborator / user-named strict; S2 default; S1 personal/prototype). Write the tier + reason into `memory/state.md` and the project rule file; it feeds every later research-matrix decision.
4. **First-experience write-back** — "no experience → normal research → same-day pitfall write": whatever pit yawned or shortcut you discovered on the first task, distill it into `memory/experience.md` the same day (symptom → root cause → fix → prevention). The bootstrap is complete only when this entry exists.

## What each future session reads

- `memory/state.md` — strictness tier + reference slots + current goal (one screen).
- `memory/experience.md` — step-2 symptom search now has real entries.
- Research matrix applies: small-module L2 under S2 → light; S3 → full even for small modules.

## Precondition honesty

If steps 1-4 cannot be completed (e.g., user stays in a brand-new repo with zero reference), write "bootstrap partial: no reference/experience yet" into state.md — the matrix still applies, with the S-tier set by the user's first statement. Do not silently assume S2 when the user said "production".
