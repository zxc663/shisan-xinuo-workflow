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

## 2. 规则文件映射与提问工具 · Rule-file mapping & asking tools

| 平台 Platform | 规则文件 Rule file | 原生提问工具 Native asking tool |
|---|---|---|
| Codex | `AGENTS.md`（项目根 project root） | `request_user_input` |
| Claude Code | `CLAUDE.md`（+ Skill 装 `.claude/skills/`）+ this skill under `.claude/skills/` | 无原生 → 文本协议 none → text protocol |
| Cursor | `.cursor/rules/workflow.mdc` | 无原生 → 文本协议 none → text protocol |
| Windsurf | `.windsurfrules` | 无原生 → 文本协议 none → text protocol |
| Trae | 项目规则文件（平台管理）project rules file (platform-managed) | 平台提问工具若存在，否则文本协议 platform question tool if present, else text protocol |
| WorkBuddy | `BOOTSTRAP.md` | `AskUserQuestion` |
| Reasonix | `AGENTS.md` | 无原生 → 文本协议 none → text protocol |
| 通用 CLI | `README.md` 说明 + 本 Skill 目录 `README.md` note + this skill folder | 无原生 → 文本协议 none → text protocol |

## 3. 生成 / 合并规则文件 · Generate / merge the rule file

1. **先备份 Backup first**：目标文件存在则复制为 `<文件名>.bak-<日期>` 再动。Copy to `<file>.bak-<date>` before any change. 绝不原地直改。Never edit in place without a backup.
2. **合并而非覆盖 Merge, never overwrite**：完整保留已有每一行，把精简纪律追加到分隔区块。Preserve every existing line; append the condensed discipline in a separated section:

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
4. **校验 Verify**：一句话复述生效要点（分级、双模式、密钥红线、回滚、留档），确认未丢失既有内容。Restate the active essentials and confirm no existing content was lost.

## 4. 提问工具降级链 · Asking-tool downgrade chain

1. 平台原生提问工具（`request_user_input` / `AskUserQuestion` / `ask_user` / 平台提问工具）。Native asking tool.
2. 结构化文本协议（见下），然后**结束回合等待答复**——所有平台通用兜底。Structured text protocol (below), then **end the turn and wait** — the universal fallback.

适用：方向、歧义、风险（权限 / 密钥 / 破坏性操作 / 需求不明 / 架构选型 / 范围扩大 / 分歧 / 复杂任务）。L1 常规不问。Use on direction, ambiguity, and risk; do not ask for L1 routine work.

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

控制在约 30 行内（上文模板）。完整 43 条与工作流保留在本 Skill 的 `references/` 按需加载——全量写入项目规则文件会让每个会话都背上上下文负担；平台只接受单短文件时，上文区块即足够。
Keep the generated file under ~30 lines (the template above). The full rules stay in `references/` and load on demand — writing everything into the project rule file inflates every session's context; the condensed block suffices when the platform only accepts one short file.