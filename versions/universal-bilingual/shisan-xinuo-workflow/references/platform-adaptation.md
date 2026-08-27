# 平台适配 · Platform Adaptation（中英双语 · Bilingual）

加载时机：第 0 步（平台检测与适配）、需要提问工具降级链或结构化提问协议时。When to load: Step 0 (detection & adaptation), the asking-tool downgrade chain, or the structured asking protocol.

## 1. 检测当前平台 · Detect the current platform

按顺序检查下列信号，第一个强命中即判定。Check in order; the first strong hit decides:

| 平台 Platform | 强信号 Strong signals |
|---|---|
| Codex（OpenAI） | CLI `codex` 可用；`~/.codex/` 存在；`AGENTS.md` 已载入上下文。CLI available; `~/.codex/` exists; `AGENTS.md` loaded into context |
| Claude Code | CLI `claude` 可用；`~/.claude/` 存在；`.claude/skills/` 可解析。CLI available; `~/.claude/` exists; `.claude/skills/` resolvable |
| Cursor | `.cursor/` 目录或 `.cursorrules`；Cursor 环境变量（`CURSOR_*`）。`.cursor/` dir or `.cursorrules`; Cursor env vars |
| Windsurf | `.windsurfrules`；Windsurf 环境变量。` .windsurfrules`; Windsurf env vars |
| Trae | Trae 运行时特征（插件 / Skill 机制、环境变量）。Trae runtime indicators (plugin/skill mechanism, env vars) |
| WorkBuddy | `BOOTSTRAP.md` 约定；有 `AskUserQuestion` 工具。`BOOTSTRAP.md` convention; `AskUserQuestion` available |
| Reasonix | `AGENTS.md` 作为插件 / 规则输入。`AGENTS.md` as plugin/rule input |
| 通用 CLI / 其他 Generic CLI / other | 以上皆无；纯 shell + 模型 API。None of the above; plain shell + model API |

无法确定时直接问用户是哪个平台——要写规则文件时不允许猜测。If uncertain, ask the user which platform this is — do not guess when a rule file will be written.

## 2. 注入点——应用每会话真正自动注入规则的位置 · Injection points — where the app ACTUALLY auto-injects rules every session

> 只把规则文件写进应用从不读取的工作区目录是**无效的**——仍会被迫手动触发。必须对准平台真正的注入点；需应用内启用时先引导用户在应用里启用。
> A rule file the app never reads is **useless** — you would still have to trigger the skill manually. Target the platform's real injection point and enable it in-app when required.

| 平台 Platform | 注入点 Injection point（每会话自动注入 auto-injected every session） | 层级 Layer | 需应用内启用 In-app enable | 原生提问工具 Native asking tool |
|---|---|---|---|---|
| Codex | `AGENTS.md`（项目根 project root） | 项目-应用层 project-app（按策略可设全局 global possible per policy） | 否 No — auto-read | `request_user_input` |
| Claude Code | `CLAUDE.md`（项目 project）或 `~/.claude/CLAUDE.md`（用户全局 user-global） | 项目-应用层 / agent 应用全局层 project-app / agent-app global | 否 No — auto-read | 无原生 → 文本协议 none → text protocol |
| Cursor | `.cursor/rules/*.mdc` 或应用设置全局 Rules / or global Rules in app settings | 项目-应用层 / agent 应用全局层 project-app / agent-app global | 通常自动读取；核对 Rules 开关 Usually auto-read; verify Rules toggle | 无原生 → 文本协议 none → text protocol |
| Windsurf | `.windsurfrules`（项目）或全局规则 / or global rules | 项目-应用层 / agent 应用全局层 project-app / agent-app global | 否 No — auto-read | 无原生 → 文本协议 none → text protocol |
| Trae | `~/.trae-cn/user_rules/*.md`（用户全局，所有项目每会话自动注入 user-global, auto-injected every session）或项目 or project `.trae/rules/project_rules.md` | agent 应用全局层（`~/.trae-cn/user_rules/*.md`）/ 项目-应用层（`.trae/rules/project_rules.md`）agent-app global / project-app | 否——文件存在即注入（已实证）No — the file's mere existence injects it (verified) | 平台提问工具若存在，否则文本协议 platform tool if present, else text protocol |
| WorkBuddy | `BOOTSTRAP.md` + 连接器配置 + connector config | 项目-应用层 project-app | 是——应用配置中挂载 Yes — attach in app config | `AskUserQuestion` |
| Reasonix | `AGENTS.md`（插件 / 规则输入 plugin/rule input） | 项目-应用层 project-app（按插件配置 per plugin config） | 视插件配置 per plugin config | 无原生 → 文本协议 none → text protocol |
| 通用 CLI | 无自动注入 no auto-injection | 不适用 n/a | 不适用 n/a | 无原生 → 文本协议 none → text protocol |

**注入分层规则（普通 vs 硬注入，见 `rules.md` 第 47 条）Injection layering rule (normal vs. hard injection, see `rules.md` §47)**：**普通（按需 / 精简）注入只写「项目-应用层」**（项目 `.trae/rules/project_rules.md` / `AGENTS.md` / `CLAUDE.md` 等），不写全局层——防污染无关会话上下文。**硬注入（强制）才写「agent 应用全局层」**，且执行前**必须先提醒用户确认**——给出：平台 / 目标注入点 / 内容长度（约行数）/ 每会话 token 成本 / 影响范围，确认后再写入。Normal (on-demand / lean) injection writes only to the project-app layer; hard injection (forced) writes only to the agent-app global layer, and must first remind the user to confirm — platform / target point / content length (~lines) / per-session token cost / scope of impact, then write.

**对每个平台 For every platform**：写入 / 合并文件后，向用户复述生效要点（平台、注入点、注入模式、提问工具）并确认未丢失既有内容；若某平台后续证实需要应用内启用，再引导用户在应用设置里启用。After writing/merging, restate the active essentials (platform, injection point, injection mode, asking tool) and confirm no existing content was lost; if a platform is later shown to require in-app enabling, then guide the user.

**强制注入（硬加载）Forced injection (hard-load)** = 把 `references/injection-core.md` 的核心全文写入上面检测到的平台注入点（先备份、合并不覆盖）——工作流每会话无条件在场。**不要**用「每会话完整读取 SKILL.md」这类弱指令实现强制注入：模型不会可靠执行额外读取动作，必须直接写入核心全文（实测教训：弱指令模式下新会话只遵循最通用的几条纪律）。Write the full core from `references/injection-core.md` into the detected platform's injection point (backup first, merge without overwriting) — the workflow is unconditionally present every session. Do NOT implement it as "read the full SKILL.md every session": models do not reliably execute extra reads (field-tested lesson).

通用 CLI（无自动注入 Generic CLI, no auto-injection）：提示用户每会话打开一次本 Skill，或写入自定义提示词。Open the skill once per session or wrap it in your custom prompt.

## 3. 生成 / 合并规则文件 · Generate / merge the rule file

### 3.0 先选注入模式（询问用户）· Choose the injection mode first (ask the user)

写任何规则文件前，用第 4 节降级链让用户选择；无提问工具默认**按需注入**并明确告知。
Before writing any rule file, let the user pick an injection mode via the section-4 chain; default to **on-demand** and say so if no asking tool is available.

| 模式 Mode | 规则文件内容 Rule file contains | 上下文开销 Context cost | 适用 Use when |
|---|---|---|---|
| **按需注入（默认）On-demand (default)** | 精简纪律（约 9 行）+ 回指本 Skill lean discipline (~9 lines) + pointer | 最低 lowest | 多数项目；Skill 按触发激活 most projects; triggers when relevant |
| **强制注入（硬加载）Forced injection (hard-load)** | `references/injection-core.md` 核心全文（判级速查 + 11 步主流程 + 设计铁律 + 双模式 + 红线 + 交付留档）the full core from injection-core.md | 每会话固定约 2-3K token a fixed ~2-3K tokens per session | 要求工作流每会话无条件在场、不依赖模型自觉 unconditional presence without depending on the model's discipline |

强制注入即把 `references/injection-core.md` 核心全文写入注入点（先备份、合并）——**没有**额外的「每会话必读」行：这类弱指令模型不可靠执行，不得作为强制注入的实现方式。There is no extra "read every session" line — weak commands like that are not reliably executed by models.

**安装期「注入模式选择提问」用双语 This install-time injection-mode choice is bilingual（中 + EN）**：这是安装共用的一步，本「先选注入模式」的提问（含选项单与推荐）以**中 + 英双语呈现**，让不同语言用户 / 模型都能看懂并各选其**自己想要的真正答案**——

**请选注入模式（Please choose the injection mode）：**
1. **按需注入（默认 On-demand, default）**——只写精简纪律并回指本 Skill，上下文开销最低（writes a compact discipline block and points back to the Skill; lowest context cost）。
2. **强制注入 / 硬加载（Force injection / Hard-load）**——把核心全文写入注入点，工作流每会话无条件在场、固定约 2-3K token/会话（writes the core full-text into the injection point; the workflow is present every session; ~2-3K token/session）。

**推荐 / Recommended**：默认按需注入（On-demand by default）；要求工作流每会话无条件在场时才用强制注入（choose force injection only when you need it present every session）。

**仅此一个安装期提问双语 This is the ONLY bilingual install-time question**：安装完成后的日常交互一律用用户偏好语言（`memory/preferences.md` 择定），不做双语重复记录——本 Skill 不设"语言桥"条款。After install, daily interaction uses the user's preferred language — no bilingual duplicate logging; this skill sets no "language bridge" clause.

### 3.1 步骤 Steps

1. **先备份 Backup first**：目标文件存在则复制为 `<文件名>.bak-<日期>` 再动。Copy to `<file>.bak-<date>` before any change. 绝不原地直改。Never edit in place without a backup.
2. **合并而非覆盖 Merge, never overwrite**：完整保留已有每一行——**按需注入**用下面的精简纪律块；**强制注入**用 `references/injection-core.md` 核心全文。Preserve every existing line — **on-demand mode** uses the lean block below; **forced mode** writes the full core from `references/injection-core.md` instead. 按需注入精简块 On-demand lean block:

```markdown
## Agent 工作流纪律（shisan-xinuo-workflow）· Agent workflow discipline

1. 任务分级 L1/L2/L3；L3（密钥 / 权限 / 数据删除 / 迁移 / 对外发布 /
   架构选型）必须先问用户。
   Task triage L1/L2/L3; L3 (secrets / permissions / deletion / migration /
   publishing / architecture) requires asking the user first.
2. 双模式：普通（关键决策必问）；目标模式（目标：/ 目标模式 / 无人值守 /
   goal mode / unattended —— 按计划自主，密钥与破坏性操作暂停等待）。
   Two modes: normal (ask on consequential decisions); goal mode
   (keywords 目标：/ 目标模式 / 无人值守 / goal mode / unattended —
   autonomous per plan, but secrets & destructive ops pause and wait).
3. 开工先复述任务（目标 / 边界 / 验收），前置 3-5 条可验证验收标准。
   Restate the task before acting; write 3-5 verifiable acceptance criteria.
4. 绝不假实现——未完成内容显式标注。
   Never fake completion — label unfinished work explicitly.
5. 质量门禁：审查 diff、跑项目测试基线、文档与代码同批提交。
   Quality gates: review the diff, run the test baseline, ship docs with code.
6. 重大修改 / 破坏性操作前必建回滚点。
   Rollback point BEFORE major changes or destructive ops.
7. 每会话维护任务记录；排查前先读经验库。
   Keep a task record per session; read the experience log first.
8. 完整规则见 shisan-xinuo-workflow Skill（references/rules.md）。
   Full rules: see the shisan-xinuo-workflow skill (references/rules.md).
```

3. **回指本 Skill Point back to the skill**：注明完整工作流位置（Skill 目录或仓库 URL），保持渐进式披露。Reference where the full workflow lives.
4. **校验 Verify**：一句话复述生效要点（分级、双模式、注入模式、密钥红线、回滚、留档），确认未丢失既有内容。Restate the active essentials (triage, dual modes, injection mode, secrets, rollback, records) and confirm no existing content was lost.

### 3.2 会话钩子（可选，仅平台支持时）· Session hooks (optional, platform-supported only)

平台支持会话钩子时（如 Claude Code `SessionStart`/`SessionEnd`，经 `.claude/settings.json` 或 `hooks.json`），可让纪律**自动**加载，而非只靠规则文本——这是「强制」模式的最强形态。When the platform supports session hooks (e.g. Claude Code `SessionStart`/`SessionEnd`), the discipline can load automatically — the strongest form of "forced" mode.

- **效果 Effect**：新会话启动时 start 钩子打印纪律横幅（分级/双模式/密钥红线/回滚/留档），指向规则文件与记忆文件，工作前重新锚定；会话结束前 end 钩子重新锚定收尾（验证/任务记录/记忆同步/密钥红线/回滚/显式安全清理）。On session start, the start hook prints a discipline banner and points to the rule + memory files; before session end, the end hook re-anchors closure (verification / task record / memory sync / secrets red line / rollback / explicit-safe cleanup).
- **方式 How**：模板在 `templates/hooks/`——`session-start.example.sh` + `session-end.example.sh` + `hooks.example.json`（`SessionStart`/`SessionEnd` → 运行脚本）。复制适配。Templates in `templates/hooks/`; copy & adapt.
- **契约 Contract**：可选且受平台门控，配置示例非捆绑运行时，保持零脚本；无 hooks 的平台跳过。Optional & platform-gated; config example, not bundled runtime; skip on platforms without hooks.
## 4. 提问工具降级链 · Asking-tool downgrade chain

1. 平台原生提问工具（`request_user_input` / `AskUserQuestion` / `ask_user` / 平台提问工具）。Native asking tool.
2. 结构化文本协议（见下），然后**结束回合等待答复**——所有平台通用兜底。Structured text protocol (below), then **end the turn and wait** — the universal fallback.

适用：方向、歧义、风险（权限 / 密钥 / 破坏性操作 / 需求不明 / 架构选型 / 范围扩大 / 分歧 / 复杂任务）及**对需求理解不尽确定**。L1 常规不问。Use on direction, ambiguity, risk, and when **understanding is not fully certain**; do not ask for L1 routine work. **问清楚比问少了更重要，理解需求比模糊执行更重要 / Asking clearly beats asking less; understanding the need beats executing it vaguely.**

## 5. 结构化提问协议（文本兜底） · Structured asking protocol (text fallback)

依次写四节，然后结束回合。写紧凑。Write the four sections, then end the turn. Keep it tight.

```markdown
【需要确认 / Needs confirmation】
<一句话说明必须决定什么。One line on what must be decided.>

【我的理解 / My understanding】
<目标 / 边界 / 验收口径复述。Restatement of goal, boundaries, acceptance.>

【选项对比 / Options】
1. <方案 A> — 优点 / 缺点 / 风险 <pros / cons / risks>
2. <方案 B> — 优点 / 缺点 / 风险 <pros / cons / risks>

【推荐 / Recommendation】
<方案 X>，理由：<…；含后果与代价。why; including consequences and cost.>

请确认或修正后我再继续。 / Please confirm or correct before I continue.
```

## 6. 生成规则文件的体量 · Generated rule file size

**按需注入 On-demand**：控制在约 30 行内（上文精简块）。**强制注入（硬加载）Forced injection (hard-load)**：写入 `references/injection-core.md` 核心全文（约 55 行，每会话固定约 2-3K token——用固定小成本换取工作流无条件在场）。完整 47 条与工作流保留在本 Skill 的 `references/` 按需加载；平台只接受单短文件时，精简块即足够。On-demand: under ~30 lines. Forced: write the full core from `references/injection-core.md` (~55 lines, a fixed ~2-3K tokens per session — a small fixed cost that buys unconditional presence). Full rules stay in `references/`; the lean block suffices when the platform only accepts one short file.