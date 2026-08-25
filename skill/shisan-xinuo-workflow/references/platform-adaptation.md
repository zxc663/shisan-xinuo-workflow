# Platform Adaptation (English)

Load this file for Step 0 (platform detection & adaptation) and whenever the asking-tool downgrade chain or the structured asking protocol is needed.

## 1. Detect the current platform

Check the following signals in order; the first strong hit decides:

| Platform | Strong signals |
|---|---|
| Codex (OpenAI) | CLI `codex` available; `~/.codex/` exists; project has `AGENTS.md` loaded into context |
| Claude Code | CLI `claude` available; `~/.claude/` exists; `.claude/skills/` resolvable |
| Cursor | `.cursor/` directory or `.cursorrules` present in project; Cursor env vars (`CURSOR_*`) |
| Windsurf | `.windsurfrules` in project; Windsurf env vars |
| Trae | Trae-specific runtime indicators (plugin/skill mechanism active, Trae env vars) |
| WorkBuddy | `BOOTSTRAP.md` convention; `AskUserQuestion` tool available |
| Reasonix | `AGENTS.md` scheduled as plugin/rule input |
| Generic CLI / other | None of the above; plain shell + model API |

If uncertain, ask the user which platform this is — do not guess when a rule file will be written.

## 2. Rule-file mapping & asking tools

| Platform | Rule file to create/merge | Native asking tool |
|---|---|---|
| Codex | `AGENTS.md` (project root) | `request_user_input` |
| Claude Code | `CLAUDE.md` (+ this skill installed under `.claude/skills/`) | none native → text protocol |
| Cursor | `.cursor/rules/workflow.mdc` | none native → text protocol |
| Windsurf | `.windsurfrules` | none native → text protocol |
| Trae | project rules file (platform-managed) | platform question tool if present, else text protocol |
| WorkBuddy | `BOOTSTRAP.md` | `AskUserQuestion` |
| Reasonix | `AGENTS.md` | none native → text protocol |
| Generic CLI | `README.md` note + this skill folder | none native → text protocol |

## 3. Generate / merge the rule file

1. **Backup first**: if the target file exists, copy it to `<file>.bak-<date>` before any change. Never edit an existing rule file in place without a backup.
2. **Merge, never overwrite**: preserve every existing line of the user's rules. Append the condensed operating discipline below under a clearly separated section, e.g.:

```markdown
## Agent workflow discipline (shisan-xinuo-workflow)

1. Task triage L1/L2/L3; L3 (secrets / permissions / data deletion / migration /
   external publishing / architecture choice) requires asking the user first.
2. Two modes: normal (ask on consequential decisions) and goal mode
   (keywords 目标：/ 目标模式 / 无人值守 / goal mode / unattended — autonomous per
   plan, but secrets & destructive ops pause and wait).
3. Restate the task (goal / boundaries / acceptance) before acting; write 3-5
   verifiable acceptance criteria up front.
4. Never fake completion — label unfinished work explicitly.
5. Quality gates: review-diff, run the project's test baseline, ship docs with code.
6. Rollback point (commit/stash or snapshot) BEFORE major changes or destructive ops.
7. Keep a task record per session; read the experience log before troubleshooting.
8. Full rules: see the shisan-xinuo-workflow skill (references/rules.md).
```

3. **Point back to the skill**: the rule file should reference where the full workflow lives (this skill's folder or repo URL), so details stay progressive-disclosure-friendly.
4. **Verify**: after writing, restate the active essentials (triage, dual modes, secrets red line, rollback rule, record discipline) in one line to the user and confirm no existing content was lost.

## 4. Asking-tool downgrade chain

1. Native asking tool (`request_user_input` / `AskUserQuestion` / `ask_user` / platform question tool).
2. Structured text protocol (below), then **end the turn and wait** — this works on every platform and is the universal fallback.

Use asking on: direction, ambiguity, risk (permissions / secrets / destructive ops / unclear requirements / architecture & stack choice / scope expansion / conflicting proposals / complex tasks). Do not ask for L1 routine work.

## 5. Structured asking protocol (text fallback)

Write the following four sections, then end the turn. Keep it tight.

```markdown
【需要确认 / Needs confirmation】
<one line on what must be decided>

【我的理解 / My understanding】
<restatement of goal, boundaries, acceptance>

【选项对比 / Options】
1. <option A> — 优点 <pros> / 缺点 <cons> / 风险 <risks>
2. <option B> — 优点 <pros> / 缺点 <cons> / 风险 <risks>

【推荐 / Recommendation】
<option X>，理由：<why；含后果与代价>

请确认或修正后我再继续。 / Please confirm or correct before I continue.
```

## 6. Generated rule file size

Keep the generated rule file under ~30 lines (the template above). The full 43 rules and workflows stay in this skill's `references/` and load on demand — writing everything into the project rule file inflates every session's context for all tasks. If the platform's rule mechanism only accepts a single short file, the condensed block above is sufficient.