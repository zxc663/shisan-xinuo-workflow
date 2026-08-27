# Skill Usage Module: Capability Discovery / Load-Decision Routing / Progressive vs. Full Read Classification

> Load this file when a task involves choosing a Skill, front-end / design work, how to obtain a Skill when none is local, or weak-model / context-constrained handling. It defines the load discipline for **already-registered** Skills — creation / registration themselves are meta-capability, handled elsewhere.
> Cross-references: `rules.md` §26/§28/§29/§38, `security.md` install vetting, `platform-adaptation.md` §1/§2.

## 0. Where Skill capability comes from & how it is discovered (meta-capability)

- **An agent can only use a Skill the platform has registered into its "available skills list"** — every session the platform injects all discoverable Skills' `name + one-line description` (in this session, the `available_skills` list in the system reminder). **A Skill that is not registered / injected cannot be triggered by the agent, even if its file exists on disk.**
- **Three-layer load model** (how platforms naturally work):
  - **L0 registry list** (name + description, injected in full every session, resident) — for **discovery & matching decisions**; occupies no body context unless triggered.
  - **L1 main file** (`SKILL.md`, read on demand when triggered).
  - **L2 `references/`** (read progressively on demand).
- **Trigger decision chain**: task → scan the L0 list → read several descriptions to judge the hit → trigger the Skill tool by name → read L1 → progressively read L2. **Description quality drives match accuracy and false-trigger cost** (concise + trigger words → accurate hit, low cost; otherwise you misjudge or end up dumping the whole body). **Trigger a Skill only with the exact `name` in the registry list** — letter prefix + plugin form use the full `plugin:skill` name; a Skill name from testing / training memory is **never guessed or invented** — only the exact names present in the injected list.
- **Agent (sub-agent) registration dimension**: whether you can use a Skill **depends on whether the executing agent itself has a Skill tool registered** — unrelated to whether the file exists on disk. Empirically: `general_purpose_task` / `Explore` / `Plan` carry a Skill tool, while `browser_use` does **not** (only the browser API + read-only tools). Two disciplines: ① when a delegated task falls within a Skill's capability, **first verify that sub-agent has a Skill tool registered**; if not, switch to an agent type that does, or **run it in the main session** — never delegate Skill-dependent work to an agent without the Skill tool; ② after delegating, the sub-agent itself follows this module's load order (scan the L0/L1/L2 it received) — the main session does not re-load the same Skill on top of the sub-agent's (saves tokens). This is a general discipline, recorded in `rules.md` §28.
- **Platform differences** (per `platform-adaptation.md` §1/§2): Trae injects the available list via system reminder and reads the body on demand; Claude Code requires a Skill to be registered under `.claude/skills/` before it can be parsed (**file present ≠ usable; depends on platform parsing**); Cursor / Windsurf etc. follow their platform mechanism. The load discipline must adapt to the platform being argued for and to whether the Skill is "registered & discoverable".
- **Registration vs. use separation**: creating / registering / updating a Skill is **meta-capability** (skill-creator on Trae, lark-skill-maker for Lark, the six-step flow in `rules.md` §38 for rules-type); this module only governs the **load discipline for already-registered Skills** — the two are not mixed.
- **Weak models / oversized skill libraries**: even with only descriptions injected, dozens of Skills' name + description resident in full can break a weak model's context → for weak models, shrink the discoverable list (platform-side filter / keep only the core) and rely on precise descriptions to avoid false triggers.

## 1. When to use / when NOT to use a Skill

- **Use**: when it raises professional capability and the task falls within a Skill's scope (writing / analysis / front-end / payments / documents / data, etc.).
- **NOT use**: **weak models / context-constrained cases** — the Skill's full text blows through the context limit; load it in a lean form or not at all, keeping only the master-sequence core (triage / red lines / must-ask). For users unused to Skills or who don't understand them yet, first show that Skills can raise an LLM's professional capability, but **a weak model may not need Skills** — forcing a load blows the context; judge the trade-off per §5.

## 2. Local Skills first, progressive loading

- A local / workspace Skill is available → **load it progressively** (main SKILL.md first → references on demand), **don't re-hand-roll**, and don't re-import an already-registered duplicate.

## 3. Getting a Skill when none is local

1. **Ask the user first** (per the asking-tool downgrade in `platform-adaptation.md` §4) one of two: whether to look for an **authoritative Skill source** to install, or whether this machine has **another Skill-install directory** to reuse.
2. **Authoritative-source judgment**: first-hand sources (official repos / registries / the skills ecosystem) > empirical sources (stars / maintenance / adoption) > community reputation; any install must pass the **mandatory open-source install vetting** in `security.md` (§1.5, 6 steps).
3. **Reuse another local directory**: filter by capability / description first, **read progressively only after confirming it is registered & discoverable on the platform** — don't re-import duplicates; if not registered, register it per the platform mechanism.

## 4. Progressive read vs. forced full read (classification) ← core change

- **Default: progressive read** — read the Skill's main file (SKILL.md / SKILL), read `references/` on demand at the current step; never preload all references; the context budget is not wasted.
- **Force full read (not progressive) — 3 exceptions**:
  1. **Core governance / workflow Skills** — the process gate cannot be skipped (Shisan Xinuo Agent Workflow itself is one such class).
  2. **Front-end / UI / design Skills always force a full read** (explicitly mandated) — **unconditional: not reduced even when context is ample or the user explicitly sets no budget limit**; design work depends on the complete spec / constraints, and progressive reading tends to miss component specs, design tokens, and usability / accessibility rules, producing non-compliant output.
  3. **The user explicitly allows no budget limit**: read in full directly (if it is a front-end class, it is already an unconditional full read — see #2). "Ample context" is the natural default state and is not a front-end waiver.
- **No full read needed**: tool-like / helper / trigger-on-demand Skills → progressive.
- **Front-end / UI / design Skill examples (illustrative)**: `frontend-design`, `frontend-skill`, `html-report`, `html-deck`, `canvas-design`, `web-artifacts-builder`, `shadcn`, `web-design-guidelines`, `theme-factory`, `brand-guidelines`, etc. — when triggered, read their SKILL.md and the needed references in full.

## 5. Weak-model / context-constrained handling

- **Judgment (qualitative, no hard threshold)**: weak model capability, or the context is about to be exhausted → **load only the minimal core that can move the task**; split heavy Skills into sub-tasks / new sessions.
- Log the decision (reason into the task record).

## 6. Skill description quality discipline (for Skill authors; also an adoption basis for users)

- The description should be **concise and carry clear trigger words**, so the agent can judge the hit with high accuracy from the description alone — lowering false triggers and the cost of reading the whole body.
- A description **that does not match the actual capability (inflated / stale) is the #1 cause of match errors and wasted context**; honestly flag when a Skill's docs don't match its implementation.

## 7. Skill vs. MCP / tools (capability boundary)

- A Skill may carry tools / MCP (exposed via `run_mcp` or the platform mechanism); triggering the Skill unlocks its tools, and the usage discipline follows the same triage / logging / cost rules as tools (`rules.md` §28/§29).
- When a Skill's capability is missing, follow the "capability-loss degradation" in `security.md` / `workflows.md` — degrade, don't block.