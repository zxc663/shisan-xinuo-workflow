# Shisan Xinuo Agent Workflow · 十三希诺通用 Agent 工作流

[English](#english) | [中文](#中文)

A cross-platform engineering-governance **Agent Skill**: one installable folder that teaches any agent (Trae / Codex / Claude Code / Cursor / Windsurf / WorkBuddy / CLI) a single auditable way of working — task triage by risk, ask-before-acting, quality gates, rollback safety, recordkeeping — with no faked completions.

一个跨平台的工程治理类 **Agent Skill**：一个可安装目录，让任意 Agent 平台按统一可审计的方式工作——任务分级、关键必问、质量门禁、改动前回滚点、留档纪律，禁止假实现。

---

## English

### Positioning

**Workflow is the soul, rules are the foundation.** The universal task operating sequence is the core asset — a mandatory skeleton every task advances along, with an exit-artifact gate on every step. The 43 discipline rules are the foundation that constrains each step. The two are strongly coupled and mutually dependent — the workflow carries the rules into execution, the rules govern the workflow. It is not domain knowledge (no framework/library/API content); it is the *way of working* layered on top of whatever the task is.

### Quick start (快速体验)

**Try it in under a minute** (needs a skills-capable agent: Claude Code, Trae, Cursor, Codex…):

1. **Install** — copy `skill/shisan-xinuo-workflow/` into your platform's skill folder (see Install below), or `npm install @zxc663/shisan-xinuo-workflow` and copy the folder from `node_modules/`.
2. **Load** — open a session. The skill runs **Step 0 platform adaptation** automatically: it detects the platform, writes a ~30-line rule file (`AGENTS.md`/`CLAUDE.md`/…) and picks an asking tool. (Existing rule files are backed up and merged, never overwritten.)
3. **Feel it** — give a small task and watch it behave: it restates understanding first, writes 3-5 acceptance criteria, does the work, then self-checks. Now give a **risk task** (e.g. "delete this folder"): it must ask before acting — that is L3 triage in action.
4. **Goal mode** — say `目标：整理本目录文件并归组，注意不要删除任何内容` and watch it plan, set budgets, split by file boundaries and stop when the budget is hit.

Expected within one session: task triage, ask-before-acting, rollback before risky ops, and records at the end.

### What it does

- **Step 0 platform adaptation** — on load, detects the platform (Codex / Claude Code / Cursor / …) and generates a condensed, merge-safe rule file (`AGENTS.md`, `CLAUDE.md`, `.cursor/rules/*.mdc`, …). Existing rule files are backed up and merged, never overwritten.
- **43-rule operating discipline** (task triage L1/L2/L3, dual modes, five-question reuse chain, quality gates, secrets red line, recordkeeping) via progressive disclosure — `SKILL.md` stays lean, `references/` load on demand.
- **Ask-before-acting protocol** with a universal text-protocol fallback for platforms without a native asking tool.
- **Rollback safety** — rollback point (commit/stash/snapshot) required *before* major changes or irreversible operations.
- **Dual modes** — normal (ask on consequential decisions) and goal mode (`目标：` / `goal mode` / `unattended` → autonomous per plan; secrets & destructive ops still pause).
- **Context-loss self-check** — agents cannot detect their own context compaction, so instead of assuming, the skill installs two guards: reload on explicit signals (user says "reload" / platform reset) and a core-elements self-check before work starts, commits, or major decisions.
- **Injection-point & injection mode** — Step 0 writes the rule into the location the agent app **actually auto-injects every session** (e.g. `CLAUDE.md`, `AGENTS.md`, `.cursor/rules`, app-managed project rules for Trae) — never a workspace file the app ignores. It asks whether you want **on-demand** (default, lean rule) or **forced per-session** (rule commands reading the full SKILL.md every session, no manual trigger needed), and guides you to enable the rule inside the app when the platform requires it (e.g. Trae).
- **Mandatory master sequence with exit-artifact gates** — the 11-step task operating sequence is the single entry for every task; each step must produce its exit artifact before the next step may begin (checkable, auditable, unskippable). A status-clarification prelude (driving one-question-at-a-time interrogation) runs first when goals/state are fuzzy. The **iron law** runs throughout: the best code achieves the most complete function and experience with the least code while meeting the requirements — reuse (including mature open-source projects, with style adaptation or secondary development) before ever hand-rolling components. The online survey of mature open-source projects is a **mandatory step**, not a fallback. Sequence: understand → experience log → survey actual resources → online survey (mandatory) → reuse survey (iron law) → restate → ask → product-view + triage + rollback → plan & acceptance doc → execute → self-check & archive.

### Use cases

- You want your agent to behave the same way across projects and platforms (Trae, Codex, Claude Code, Cursor, CLI…).
- You want risk-based autonomy: L1 routine work done directly, L3 high-risk work (secrets, deletion, migration, publishing) always asked first.
- You want unattended "goal mode" runs with a written plan, budgets, file-boundary isolation, and automatic stop.
- You want auditable sessions: acceptance criteria up front, task records, post-session knowledge distillation.

### What makes it different

| Compare with | This skill |
|---|---|
| A hand-written `AGENTS.md`/`CLAUDE.md` | Adds progressive disclosure (lean preload, on-demand detail), a full reference body, and cross-platform adaptation logic — more than a one-page rule list, without taxing every session. |
| Platform built-in rules | Platform-independent: same discipline on every platform; Step 0 adapts instead of you rewriting rules per tool. |
| Generic agent-system prompts | Operational, verifiable, checklist-driven: task triage tables, rollback procedure, scanning checklists — not vague exhortation. |
| Official skills repos | Fills the "general workflow governance" niche: repos are rich in domain skills but thin on cross-domain operating discipline. |

### Limitations (honest)

- **Context cost**: even with progressive disclosure, a governance layer consumes context. Trade-off for consistency; keep generated rule files ~30 lines to limit it.
- **Relies on agent self-discipline**: no scripts enforce anything. A lazy agent can ignore rules; it also cannot detect its own compaction — mitigated by the self-check guards (see above).
- **Detection heuristics are best-effort**: platform detection uses directory/env signals; if ambiguous, the skill asks the user instead of guessing.
- **No bundling of tooling**: deliberately zero scripts/dependencies/network. Capability gaps are handled by *fallbacks* (native ask protocol, generic ability + official docs), not by shipping binaries.
- **Spec evolution**: built against the Agent Skills open standard (agentskills.io); older platforms without skill support need manual loading (see Install).

### Where it comes from

Battle-tested in real production workflows, rewritten against the [Agent Skills specification](https://agentskills.io/) and its [best practices](https://agentskills.io/skill-creation/best-practices) (progressive disclosure, gotchas, checklists, plan-validate-execute).

### Edition differences (English / 中文 / Bilingual)

The three universal editions are **content-identical**; they differ only in language:

| Edition | Path | Language of content | Reply language |
|---|---|---|---|
| English | `skill/shisan-xinuo-workflow/` | English (brand name 「十三希诺」 kept in the title) | Follows the user — **no forced Chinese**; chat replies mirror the user's language |
| 中文 | `versions/universal-zh/` | Chinese | Follows the user; docs/records per project convention |
| Bilingual | `versions/universal-bilingual/` | Paragraph-level EN+ZH | Follows the user |

A personal workstation edition (embedded pitfall know-how, full dual-mode table, Chinese-expression rule) is maintained in a **separate private repository** and is not part of this public repo.

### Install

Copy the skill folder into your platform's skills directory:

| Platform | Target |
|---|---|
| Claude Code | `~/.claude/skills/shisan-xinuo-workflow/` |
| Codex / generic | clone the repo, point skill discovery at `skill/shisan-xinuo-workflow/` |
| Others | follow the platform's skill-folder convention; see `references/platform-adaptation.md` |

No scripts, no dependencies, no network calls. Loading the skill is enough — Step 0 adapts it to the platform.

### Repository layout

```
skill/shisan-xinuo-workflow/       ← default deliverable (English)
  SKILL.md
  references/ (rules / workflows / platform-adaptation / security)
versions/
  universal-zh/                    ← 通用版 · 中文
  universal-bilingual/             ← 通用版 · 中英双语
```

### Relationship to other standards

- [Agent Skills / agentskills.io](https://agentskills.io/) — this skill follows the open standard (folder + `SKILL.md` + progressive disclosure), so it runs on any skills-compatible client.
- [AGENTS.md](https://agents.md/) — Step 0 generates exactly this kind of cross-platform rule file, in condensed form; the full workflow stays inside the skill.

### FAQ

- **Why not one big rule file?** Context discipline. The skill preloads only `name`+`description`; the body loads on activation; `references/` load per step. A giant rule file would tax every session.
- **Will it overwrite my existing rules?** No — backup + merge only (rule: merge, never overwrite).
- **Does it send data anywhere?** No. Pure documentation; no scripts; no network.
- **Can the agent tell when its context was compacted?** No — that is exactly why rule 25 installs explicit-signal reload + milestone self-checks instead of relying on compaction awareness.

### Contributors

- **十三希诺** — author & maintainer ([zxc663](https://github.com/zxc663))

Contributions welcome: open an issue or PR for rule improvements, workflow additions, or localization fixes. New rules follow the skill's own rule-addition process (workflow 9) before merging.

### License

MIT — see [LICENSE](LICENSE).

---

## 中文

### 定位

**流程为魂、规则为基。** 通用工作执行流程是核心资产——每个任务强制通用的推进骨架，每步带出口产物门禁；43 条纪律规则是约束每步的地基。二者强耦合、相互依托：流程承载规则落地，规则约束流程执行。它不含领域知识（无框架 / 库 / API 内容），而是叠加在任务之上的「工作方式」。

### 快速体验

**一分钟跑通**（需要支持 Skill 的 Agent 环境：Claude Code / Trae / Cursor / Codex 等）：

1. **安装**：把 `skill/shisan-xinuo-workflow/` 复制到平台技能目录（见下方安装）；或 `npm install @zxc663/shisan-xinuo-workflow` 后从 `node_modules/` 复制该目录。
2. **加载**：新开会话。Skill 自动执行**第 0 步平台适配**：检测平台、写入约 30 行规则文件（`AGENTS.md`/`CLAUDE.md`/…）、选定提问工具（已有规则先备份再合并，绝不覆盖）。
3. **感受它**：先给一个小任务观察行为——它会先复述理解、写 3-5 条验收标准、做完自查。再给一个**风险任务**（如「把这个目录删了」）：它必须**先问再动手**——这就是 L3 分级在起作用。
4. **目标模式**：说 `目标：整理本目录文件并归组，注意不要删除任何内容`，观察它写计划、设预算、按文件边界拆分、超预算自动停。

一个会话内应看到：任务分级、关键必问、风险操作前回滚点、结束时留档。

### 它做什么

- **第 0 步平台适配**：加载即检测平台（Codex / Claude Code / Cursor / Trae / Windsurf / WorkBuddy / 通用 CLI），生成精简且合并安全的规则文件（`AGENTS.md`、`CLAUDE.md`、`.cursor/rules/*.mdc` 等）。已有规则先备份再合并，绝不覆盖。
- **43 条工作纪律**（L1/L2/L3 任务分级、双模式、复用五问决策链、质量门禁、密钥红线、留档纪律），按渐进式披露组织——`SKILL.md` 保持精简，`references/` 按需加载。
- **关键必问协议**：平台无原生提问工具时，提供通用结构化文本兜底协议。
- **回滚安全**：重大修改/不可逆操作**前**必须先建回滚点（commit/stash/快照），高危命令执行前同样要求。
- **双模式**：普通模式（关键决策必问）+ 目标模式（关键词 `目标：`/`目标模式`/`无人值守`/`goal mode` → 按计划自主执行，密钥与破坏性操作仍暂停等待确认）。
- **上下文缺失自检**：Agent 无法感知自己被压缩，因此不靠感知、靠两道守卫——显式信号（用户说「重载」/ 平台重置）即重读；开工 / 提交 / 重大决策前默写核心要素，复述不全即重读。
- **注入点与注入模式**：第 0 步把规则写入 agent 应用**每会话真正自动注入**的位置（如 `CLAUDE.md`、`AGENTS.md`、`.cursor/rules`、Trae 应用内项目规则）——绝不写进应用忽略的工作区文件。它会询问你选择**按需注入**（默认，精简规则）还是**强制注入**（规则命令每会话完整读取 SKILL.md，无需手动触发），并在平台要求时（如 Trae）**引导你在应用设置里启用规则**。
- **带出口产物门禁的强制总纲主流程**：11 步任务主流程是每个任务的唯一入口；每步必须先产出其出口产物方可进入下一步（可检查、可审计、不可跳步）。目标/现状模糊时先走**状态澄清前置**（主导式一次一问追问）。贯穿全程的**最铁铁律**：以最少的代码实现最完整的功能和体验并达到需求描述——能复用就复用（含市面开源成熟项目，风格适配/二次开发皆可），绝不自己自研组件；**联网调研市面开源成熟项目是必须步骤，不是降级兜底**。步序：理解 → 经验库必读 → 调研实际资源 → 联网调研·必须 → 复用调研·铁律 → 复述 → 疑问必问 → 产品视角 + 分级 + 回滚点 → 规划验收文档 → 执行 → 自查与归档。

### 使用场景

- 希望 Agent 在跨项目、跨平台（Trae、Codex、Claude Code、Cursor、CLI 等）时行为一致。
- 希望按风险给自主权：L1 常规直接做，L3 高风险（密钥、删除、迁移、发布）一律先问。
- 希望「目标模式」无人值守运行：先写计划、设预算、按文件边界拆分、超预算自动停。
- 希望会话可审计：验收标准前置、任务记录、会话结束知识沉淀。

### 差异化优势

| 对比对象 | 本 Skill |
|---|---|
| 手写 `AGENTS.md`/`CLAUDE.md` | 增加渐进式披露（精简预加载 + 按需细节）、完整引用体系与跨平台适配逻辑——不止一页规则，且不拖累每个会话 |
| 平台内置规则 | 平台无关：同一纪律在任何平台上生效；第 0 步自动适配，无需逐平台重写 |
| 通用系统提示词 | 可操作、可验证、清单驱动：分级表、回滚流程、扫描清单——不是空泛口号 |
| 官方技能仓库 | 补位「通用工作流治理」品类：官方仓库领域技能丰富，跨领域工作纪律稀缺 |

### 局限与代价（如实说明）

- **上下文成本**：即使渐进式披露，治理层仍消耗上下文——这是换取一致性的代价；生成的规则文件控制在约 30 行以内以限制成本。
- **依赖 Agent 自律**：无脚本强制执行。懒惰的 Agent 可以不遵守规则，也无法感知自己被压缩——已用自检双守卫缓解（见上）。
- **平台检测是启发式**：靠目录 / 环境变量信号判断；无法确定时直接问用户，不猜。
- **不捆绑工具**：刻意零脚本 / 零依赖 / 零网络。能力缺口用「兜底」解决（文本提问协议、通用能力 + 官方文档），而非塞二进制。
- **规范演进**：基于 Agent Skills 开放标准（agentskills.io）构建；不支持 Skill 的旧平台需手动加载（见安装）。

### 来源与依据

源自真实生产工作流的实战沉淀，按 [Agent Skills 开放规范](https://agentskills.io/)及其[最佳实践](https://agentskills.io/skill-creation/best-practices)重写（渐进式披露、Gotchas、Checklist、Plan-Validate-Execute）。

### 版本差异（英文 / 中文 / 双语）

三个通用版本**内容完全一致**，仅语言不同：

| 版本 | 路径 | 内容语言 | 回答语言 |
|---|---|---|---|
| 英文 | `skill/shisan-xinuo-workflow/` | 英文（标题保留品牌名「十三希诺」） | 跟随用户——**无强制中文**，对话语言与用户保持一致 |
| 中文 | `versions/universal-zh/` | 中文 | 跟随用户；文档与记录按项目约定 |
| 双语 | `versions/universal-bilingual/` | 段落级中英对照 | 跟随用户 |

个人工作台版（内嵌个人踩坑经验、完整双模式表、中文表达规则）在**独立私有仓库**维护，不属于本公开仓。

### 安装

把 skill 目录复制到所用平台的技能目录：

| 平台 | 位置 |
|---|---|
| Claude Code | `~/.claude/skills/shisan-xinuo-workflow/` |
| Codex / 通用环境 | 克隆本仓库，将技能发现指向 `skill/shisan-xinuo-workflow/` |
| Trae / Cursor / 其他 | 按平台技能目录约定放置；详见 `references/platform-adaptation.md` |

纯文档、零依赖、零网络调用。加载即自动适配平台。

### 仓库结构

```
skill/shisan-xinuo-workflow/       ← 默认交付（英文）
  SKILL.md
  references/ (rules / workflows / platform-adaptation / security)
versions/
  universal-zh/                    ← 通用版 · 中文
  universal-bilingual/             ← 通用版 · 中英双语
```

### 与其他规范的关系

- [Agent Skills / agentskills.io](https://agentskills.io/)：本 Skill 遵循开放标准（文件夹 + `SKILL.md` + 渐进式披露），兼容所有支持 Skills 的客户端。
- [AGENTS.md](https://agents.md/)：第 0 步生成的就是这类跨平台规则文件（精简版），完整工作流保留在 Skill 内按需加载。

### 常见问题

- **为什么不做成一个大规则文件？** 上下文纪律：Skill 只预加载 `name`+`description`，激活才读正文，`references/` 按步加载。巨型规则文件会拖累每个会话。
- **会覆盖我已有的规则吗？** 不会——先备份再合并，绝不覆盖。
- **会对外发送数据吗？** 不会。纯文档、无脚本、无网络。
- **Agent 能感知自己被压缩吗？** 不能——这正是第 25 条规则改为「显式信号重载 + 关键节点自检」的原因，不依赖压缩感知。

### 贡献者

- **十三希诺** — 作者与维护者（[zxc663](https://github.com/zxc663)）

欢迎贡献：规则改进、工作流补充、本地化修正请开 issue 或 PR。新增规则需先走本 Skill 自带的规则新增流程（工作流 9）再合并。

### 许可证

MIT，见 [LICENSE](LICENSE)。