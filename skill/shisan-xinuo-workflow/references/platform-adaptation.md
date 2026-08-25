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

## 2. Injection points — where the agent app ACTUALLY auto-injects rules every session

> Writing a rule file into a workspace folder the app never reads is **useless** — the skill would still require manual triggering. Always target the platform's real injection point, and enable it in-app when required.

| Platform | Injection point (auto-injected every session) | In-app enable needed? | Native asking tool |
|---|---|---|---|
| Codex | `AGENTS.md` (project root) | No — auto-read | `request_user_input` |
| Claude Code | `CLAUDE.md` (project) or `~/.claude/CLAUDE.md` (user-global) | No — auto-read | none native → text protocol |
| Cursor | `.cursor/rules/*.mdc` or global Rules (app settings) | Usually auto-read; verify Rules toggle | none native → text protocol |
| Windsurf | `.windsurfrules` (project) or global rules | No — auto-read | none native → text protocol |
| Trae | app-managed project rules (set inside the Trae app: 设置 → 项目规则/Agent 规则) | **YES — user must enable/attach the rule in the app** | platform question tool if present, else text protocol |
| WorkBuddy | `BOOTSTRAP.md` (project bootstrap) + connector config | Yes — attach in app config | `AskUserQuestion` |
| Reasonix | `AGENTS.md` (plugin/rule input) | Per plugin config | none native → text protocol |
| Generic CLI | no auto-injection | n/a | none native → text protocol |

**For every platform**: after writing/merging the file, if the platform requires enabling it inside the app (e.g. Trae project rules), **guide the user to enable it in the app settings and wait for confirmation that it is active**. Do not claim "injected" until the app confirms the rule is loaded each session.

**Forced mode** = write the rule into the injection point above **and** append the per-session read command (section 3.0), so every session loads the discipline without manual triggering.

Generic CLI (no auto-injection): tell the user to open the skill once per session, or wrap the rule in their custom prompt.

## 3. Generate / merge the rule file

### 3.0 Choose the injection mode first (ask the user)

Before writing any rule file, use the asking chain in section 4 to let the user pick an injection mode; if no asking tool is available, default to **on-demand** and say so.

| Mode | Rule file contains | Context cost | Use when |
|---|---|---|---|
| **On-demand (default)** | lean discipline + pointer to this skill | lowest | most projects; skill triggers when relevant |
| **Forced per-session** | lean discipline + pointer + "read the full SKILL.md every session" | higher (full SKILL.md per session) | you want the discipline unconditionally active in every session, including contexts where the skill would not auto-trigger |

Forced-mode extra line to append to the template below:
```markdown
- **Forced injection**: every session MUST fully read the shisan-xinuo-workflow
  skill's SKILL.md before starting work and follow it; references load on demand.
```

### 3.1 Steps

1. **Backup first**: if the target file exists, copy it to `<file>.bak-<date>` before any change. Never edit an existing rule file in place without a backup.
2. **Merge, never overwrite**: preserve every existing line of the user's rules. Append the condensed operating discipline below under a clearly separated section, e.g. (append the forced-injection line only if the user chose forced mode):

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
4. **Verify**: after writing, restate the active essentials (triage, dual modes, injection mode, secrets red line, rollback rule, record discipline) in one line to the user and confirm no existing content was lost.

### 3.2 Session-start hook (optional, platform-supported only)

When the platform supports session-start hooks (e.g. Claude Code `SessionStart` via `.claude/settings.json` or `hooks.json`), the discipline can load **automatically** — the strongest form of "forced" mode.

- **Effect**: on every new session, the hook prints a discipline banner (triage / dual modes / secrets red line / rollback / record discipline) and points to the rule file + memory file, so the agent re-anchors before any work.
- **How**: templates live in `templates/hooks/` — `session-start.example.sh` (banner script) + `hooks.example.json` (Claude Code config: `SessionStart` → run the script). Copy and adapt to the platform.
- **Contract**: the hook is **optional and platform-gated** — a config example, not a bundled runtime; the skill stays zero-script. Skip on platforms without hooks.
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