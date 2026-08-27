# Workspace `memory/` skeleton (Shisan Xinuo Agent Workflow · unified cross-session memory)

> This template is the initialization skeleton for the project-root `memory/` directory. Any session (including the next AI / a new session) **scans this directory first**; create it (or any missing file) from this template. If this project's real business already uses `memory/`, override the archive directory to `.agent-records/` inside the project rule file (the only legal override point).
> Note: `memory/` is the "state layer + pitfall layer" — the context reads only one screen of it; full rule details still load on demand from the skill's `references/`.

```
memory/
├── state.md          # Session state (one screen, quick read)
├── experience.md     # Pitfall log (symptom → root cause → fix → prevention) + general judgment standards
├── preferences.md    # Confirmed preferences (stack / language / style)
└── task-log/         # Task records (YYYY-MM-DD-<name>.md)
```

Skeleton for each file:

## `memory/state.md`

```markdown
# Session state (Shisan Xinuo Agent Workflow)

- Current goal: <one sentence>
- Decisions made: <list>
- Constraints: <list>
- Progress + next step: <list>
```

## `memory/experience.md`

```markdown
# Pitfall log (Shisan Xinuo Agent Workflow)

> Symptom → root cause → fix → prevention. Search by symptom keyword; on a hit, follow "fix / prevention"; write duplicates in one place and cross-reference.

## <symptom keyword>

- Symptom: <description>
- Root cause: <description>
- Fix: <steps>
- Prevention: <steps>
```

## `memory/preferences.md`

```markdown
# Project preferences (Shisan Xinuo Agent Workflow)

> Confirmed stack / language / style preferences. **After writing, actively remind the user to re-check the broad direction**, and follow their correction if it drifted. Secrets and destructive intent never go into preferences.

- Stack: <list>
- Language / expression: <list>
- Style / conventions: <list>
```

## `memory/task-log/` task records

```markdown
# <YYYY-MM-DD> <Task name>

- Understanding: <goal / boundaries / acceptance, 1-3 sentences>
- Acceptance criteria: <3-5 verifiable>
- Decisions: <key decisions + reasons>
- Result: <completion status / minimal verification outcome>
- Knowledge points (0-5): <trigger scenario | judgment | action>
```

Follow-up rule: read `state.md` + `experience.md` + `preferences.md` at session start; update before context reaches 40-60% and at session end.