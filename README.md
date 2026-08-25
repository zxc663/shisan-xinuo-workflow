# Shisan Xinuo Agent Workflow · 十三希诺通用 Agent 工作流

[English](#english) | [中文](#中文)

A **general-purpose personal engineering-workflow specification delivered through strong prompt injection** (SKILL.md + platform rule files): it packages 43 discipline rules, a mandatory 11-step operating sequence, and 173 landing specifics — distilled from real development history — into an installable, cross-platform, on-demand-loaded Agent Skill that drives any agent (Trae / Codex / Claude Code / Cursor / Windsurf / WorkBuddy / CLI) through an auditable way of working, with no faked completions.

一个**依赖于强提示词注入（SKILL.md + 平台规则文件）的通用个人工程工作流程规范**：把真实开发历史中沉淀的 43 条纪律、11 步强制流程、173 条落地细则，打包成可跨平台注入、按需加载、可审计的 Agent Skill，驱动任意 Agent 平台（Trae / Codex / Claude Code / Cursor / Windsurf / WorkBuddy / CLI）按统一可审计的方式工作，禁止假实现。

---

## English

### Positioning

**What it is (honest).** A *general-purpose personal engineering-workflow specification* delivered through **strong prompt injection** — it has no scripts, no runtime, no enforcement. It works by injecting rules (SKILL.md + platform rule files) into any agent and relying on the agent to follow them. What makes it more than a saved prompt: structured progressive disclosure, a mandatory process skeleton with per-step gates, and 173 landing rules distilled from a real 800KB+ development history.

Five pillars:

- **Workflow is the soul** — a mandatory 11-step task operating sequence is the single entry for every task; each step has an *exit artifact* and the next step cannot begin without it (checkable, auditable, unskippable). Skipping it discards the soul.
- **Rules are the foundation** — the 43 discipline rules constrain what each step must observe; they are strongly coupled with the workflow (the workflow carries the rules into execution, the rules govern the workflow).
- **Dual perspectives are the mirror** — engineer view *and* product-manager view: planning runs a mandatory dual survey (code reality + design-plan soundness); on repeated-review / legacy-restlessness triggers it runs a product-polish diagnosis (feature logic / code coupling / UI / interaction flow / other) before touching code.
- **Verifiable evidence is the basis** — the mandatory online survey of mature open-source projects collects verifiable trust signals (stars / downloads / maintenance / adoption / feedback / advisories), never "it's popular online"; local verification is the final judge.
- **Safety is the baseline** — "open source ≠ safe": every Skill / MCP / script / dependency must pass the mandatory install-vetting flow; secrets never land in code/docs/chat.

It is not domain knowledge (no framework/library/API content); it is the *way of working* layered on top of whatever the task is.

### Market position (objective)

- **Category**: the scarce "cross-domain workflow governance / personal working-specification" niche inside the Agent Skills ecosystem — the vast majority of the 360K+ public skills are domain-specific SOPs (code review, git, deploy, vision…).
- **Form**: pure-document / strong-prompt-injection, unlike code tools (MCP), agent frameworks, or orchestration layers. Its strength is portability; its cost is zero enforcement.
- **Fit**: matches the ecosystem's current "skills as workflow nodes / SOP packaging" consensus (Anthropic & OpenAI open standard, progressive disclosure).
- **Honest risks**: research (SWE-Skills-Bench: 39/49 skills showed zero gain, ~451% token overhead; OpenAI: "files travel, the trust boundary does not") warns that prompt-only skills can become pass-through. This skill mitigates with progressive disclosure and injection-point discipline, but it still depends on description-based triggering and agent self-discipline.

### How it works (system map)

```
Platform adaptation (Step 0: detect → injection point → on-demand/forced)
        │
        ▼
Master sequence (mandatory entry, exit-artifact gates):
  ┌─ 0. Status clarification (when goals/state are fuzzy)
  │  0.1–0.4 preludes: online survey (trust signals) · reuse survey (iron law)
  │                    product-polish diagnosis · dual survey & planning
  ├─ 1 Receive → 2 experience log → 3 survey actual resources → 4 online survey
  ├─ 5 reuse survey → 6 restate → 7 ask → 8 product-view + triage + rollback
  ├─ 9 plan (after dual survey) → 10 execute → 11 self-check & archive
  └─ Rules (43, foundation) + Landing details (173, per-category on-demand)
```

Layered knowledge, loaded on demand (context discipline): `SKILL.md` stays lean; `references/` load per step — `rules.md` (43) as the foundation, `details.md` (173 fine-grained rules in 10 categories) as landing specifics, `workflows.md` (preludes + 9 task types), `security.md`, `platform-adaptation.md`.

### Quick start (快速体验)

**Try it in under a minute** (needs a skills-capable agent: Claude Code, Trae, Cursor, Codex…):

1. **Install** — copy `skill/shisan-xinuo-workflow/` into your platform's skill folder (see Install below), or `npm install @zxc663/shisan-xinuo-workflow` and copy the folder from `node_modules/`.
2. **Load** — open a session. The skill runs **Step 0 platform adaptation** automatically: detects the platform, writes a ~30-line rule file (`AGENTS.md`/`CLAUDE.md`/…) and picks an asking tool. (Existing rule files are backed up and merged, never overwritten.)
3. **Feel it** — give a small task: it restates understanding, writes 3-5 acceptance criteria, does the work, self-checks. Give a **risk task** (e.g. "delete this folder"): it must ask first — L3 triage in action.
4. **Goal mode** — say `目标：整理本目录文件并归组，注意不要删除任何内容` and watch it plan, set budgets, split by file boundaries and stop when the budget is hit.

Expected within one session: task triage, ask-before-acting, rollback before risky ops, records at the end.

### What it does

- **Step 0 platform adaptation & injection** — detects the platform, writes a condensed merge-safe rule file into the location the app *actually auto-injects every session* (never a workspace file the app ignores), asks whether you want **on-demand** (default) or **forced per-session** loading, and guides you to enable it in-app when the platform requires (e.g. Trae).
- **Mandatory master sequence with exit-artifact gates** — the 11-step operating sequence is the single entry; each step must produce its exit artifact before the next step (checkable, auditable, unskippable). Preludes: status clarification, online survey (trust signals), reuse survey (iron law), product-polish diagnosis, dual survey & planning.
- **43-rule foundation + 173 landing details** — progressive disclosure: rules as the base, fine-grained engineering specifics (environment / frontend / database / testing / API / ops / code quality / git / sessions·backup·governance / deep-dive from real dev logs) loaded per category on demand.
- **Ask-before-acting protocol** with a universal text-protocol fallback for platforms without a native asking tool.
- **Dual perspectives** — mandatory dual survey (engineer + product-manager) before planning; product-polish diagnosis (feature logic / code coupling / UI / humanized interaction flow / other) on repeated-review or legacy-restlessness triggers.
- **Verifiable online survey** — mature open-source research is mandatory, not a fallback; trust is judged by signals + local verification, never "it's popular online".
- **Vetting before any open-source install** — "open source ≠ safe": source verification → static scan → least privilege → sandbox test → license & advisories → recorded conclusion.
- **Rollback safety** — rollback point (commit/stash/snapshot) required *before* major changes or irreversible operations.
- **Dual modes** — normal (ask on consequential decisions) and goal mode (`目标：` / `goal mode` / `unattended` → autonomous per plan; secrets & destructive ops still pause).
- **Context-loss self-check** — agents cannot detect compaction, so two guards: reload on explicit signals + a core-elements self-check before work, commits, and major decisions.

### Use cases

- You want your agent to behave the same way across projects and platforms (Trae, Codex, Claude Code, Cursor, CLI…).
- You want risk-based autonomy: L1 routine work done directly, L3 high-risk work (secrets, deletion, migration, publishing) always asked first.
- You want unattended "goal mode" runs with a written plan, budgets, file-boundary isolation, and automatic stop.
- You want auditable sessions: acceptance criteria up front, task records, post-session knowledge distillation.
- You want planning reviewed from both the engineer and the product angle — not just code-correctness.

### What makes it different

| Compare with | This skill |
|---|---|
| A hand-written `AGENTS.md`/`CLAUDE.md` | Progressive disclosure, a full reference body, cross-platform adaptation — more than a one-page rule list, without taxing every session. |
| Platform built-in rules | Platform-independent: the same discipline everywhere; Step 0 adapts instead of you rewriting rules per tool. |
| Generic agent-system prompts | Operational, verifiable, checklist-driven: triage tables, exit-artifact gates, scanning checklists — not vague exhortation. |
| Other workflow/prompt skills | Most ship rules or a process; few add a **mandatory process skeleton with per-step gates**, **dual engineer/product views**, a **verifiable survey basis**, and a **mandatory install-vetting flow**. |
| Official skills repos | Fills the "general engineering-execution governance" niche: official repos are rich in domain skills but thin on cross-domain operating discipline. |

### Limitations (honest)

- **Context cost**: even with progressive disclosure, a governance layer consumes context — the trade-off for consistency; generated rule files are kept ~30 lines.
- **Strong-prompt-injection dependent**: it is a specification, not a tool — no runtime, no enforcement. Behavior depends on the platform actually injecting the rules and on description-based triggering; if injection is skipped or the description fails to match, it does nothing.
- **Relies on agent self-discipline**: no scripts enforce anything. A lazy agent can ignore rules; it also cannot detect its own compaction — mitigated by the self-check guards.
- **Detail volume**: the landing-details file is large (173 rules) — that is why it loads by category on demand; without progressive disclosure it would be heavy.
- **Detection heuristics are best-effort**: platform detection uses directory/env signals; if ambiguous, the skill asks rather than guessing.
- **No bundling of tooling**: deliberately zero scripts/dependencies/network. Capability gaps are handled by fallbacks.
- **Spec evolution**: built against the Agent Skills open standard; older platforms without skill support need manual loading.

### Where it comes from

Battle-tested in real production workflows — including a 800KB+ development history whose real pitfalls were distilled into the landing details — rewritten against the [Agent Skills specification](https://agentskills.io/) and its [best practices](https://agentskills.io/skill-creation/best-practices) (progressive disclosure, gotchas, checklists, plan-validate-execute).

### Edition differences (English / 中文 / Bilingual)

The three universal editions are **content-identical**; they differ only in language:

| Edition | Path | Language of content | Reply language |
|---|---|---|---|
| English | `skill/shisan-xinuo-workflow/` | English (brand name 「十三希诺」 kept in the title) | Follows the user — **no forced Chinese** |
| 中文 | `versions/universal-zh/` | Chinese | Follows the user; docs/records per project convention |
| Bilingual | `versions/universal-bilingual/` | Paragraph-level EN+ZH | Follows the user |

A personal workstation edition (embedded pitfall know-how, personalized clarification, Chinese-expression rule) is maintained in a **separate private repository** and is not part of this public repo.

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
  SKILL.md                         ← lean entry: positioning, master sequence, gates, map
  references/
    rules.md                       ← 43-rule foundation
    workflows.md                   ← preludes (0.0–0.4) + 9 task types + gates
    details.md                     ← 173 landing rules in 10 categories (on-demand)
    platform-adaptation.md         ← injection points, asking chain, structured protocol
    security.md                    ← safety red lines, install vetting, rollback, residue scan
versions/
  universal-zh/                    ← 通用版 · 中文
  universal-bilingual/             ← 通用版 · 中英双语
```

### Changelog

- **v1.0** — first public release (43-rule discipline, dual modes, rollback, progressive disclosure).
- **v1.1** — injection-point & injection mode (on-demand / forced per-session).
- **v1.2** — research-driven task operating sequence (11 steps).
- **v1.3** — repositioning: workflow as soul, rules as foundation; master sequence becomes the single entry with exit-artifact gates; status clarification prelude.
- **v1.3.1** — mandatory online survey (not a fallback) + the reuse iron law (least code, never hand-roll).
- **v1.3.2** — verifiable survey trust signals + mandatory open-source install vetting ("open source ≠ safe").
- **v1.4** — landing details (173 rules in 10 categories, distilled from real dev history) + product-polish diagnosis (five-question defect location) + mandatory dual survey & planning (engineer + product-manager views).

### Relationship to other standards

- [Agent Skills / agentskills.io](https://agentskills.io/) — follows the open standard (folder + `SKILL.md` + progressive disclosure), runs on any skills-compatible client.
- [AGENTS.md](https://agents.md/) — Step 0 generates exactly this kind of cross-platform rule file, in condensed form; the full workflow stays inside the skill.

### FAQ

- **Why not one big rule file?** Context discipline: only `name`+`description` preload; the body loads on activation; references load per step.
- **Will it overwrite my existing rules?** No — backup + merge only.
- **Does it send data anywhere?** No. Pure documentation; no scripts; no network.
- **Can the agent tell when its context was compacted?** No — that is exactly why the skill installs explicit-signal reload + milestone self-checks instead of relying on compaction awareness.
- **Is the survey just "whatever the web says"?** No — it collects verifiable trust signals with a defined authority hierarchy and local verification as the final judge.

### Contributors

- **十三希诺** — author & maintainer ([zxc663](https://github.com/zxc663))

Contributions welcome: open an issue or PR for rule improvements, workflow additions, or localization fixes. New rules follow the skill's own rule-addition process before merging.

### License

MIT — see [LICENSE](LICENSE).

---

## 中文

### 定位

**本质（如实）**：一个**依赖于强提示词注入的通用个人工程工作流程规范**——无脚本、无运行时、无强制；靠把规则（SKILL.md + 平台规则文件）注入任意 Agent 并依赖其自觉执行。它不只是"保存的提示词"：具备结构化渐进式披露、带每步门禁的强制流程骨架，以及从真实 800KB+ 开发历史提炼的 173 条落地细则。

五大支柱：

- **流程为魂**：强制 11 步任务主流程是每个任务的唯一入口，每步有「出口产物」，无产物不得进入下一步（可检查、可审计、不可跳步）——跳过即丢弃灵魂。
- **规则为基**：43 条纪律规则约束每步该守什么，与流程强耦合、相互依托（流程承载规则落地，规则约束流程执行）。
- **双视角为镜**：工程师视角 + 产品经理视角——规划前强制**双调研**（代码实况 + 设计规划合理性）；触发「反复审查 / 存量项目反复不足」时先做**产品完善度诊断**（功能逻辑 / 代码耦合 / 界面 UI / 人性化互动流程 / 其他）再动手。
- **可信证据为依据**：必须联网调研市面开源成熟项目，收集**可验证可信信号**（stars / 下载量 / 维护 / 被采用 / 口碑 / 安全通告），绝不凭「网上都说火」；本地实测兜底。
- **安全为底线**：「开源不等于安全」——任何 Skill / MCP / 脚本 / 依赖引入前必须走强制校验流程；密钥绝不进代码 / 文档 / 对话。

它不含领域知识（无框架 / 库 / API 内容），而是叠加在任务之上的「工作方式」。

### 市场定位（客观）

- **品类**：Agent Skills 生态中稀缺的「跨领域工作流治理 / 个人工作流程规范」细分——公开 36 万+ 技能绝大多数是领域型 SOP（code review / git / 部署 / 视觉…）。
- **形态**：纯文档 / 强提示词注入型，不同于代码工具（MCP）、Agent 框架或编排层。优势是可移植；代价是零强制执行。
- **契合**：符合生态当前「Skills = 工作流节点 / SOP 封装」的共识（Anthropic 与 OpenAI 开放标准、渐进式披露）。
- **诚实风险**：研究（SWE-Skills-Bench：39/49 个技能零收益、token 开销约 451%；OpenAI：「文件可迁移，信任边界不可迁移」）警示纯提示词型技能易沦为 pass-through——本 Skill 以渐进式披露与注入点纪律缓解，但仍依赖 description 触发质量与 Agent 自律。

### 工作原理（体系全景）

```
平台适配（第 0 步：检测 → 注入点 → 按需 / 强制注入）
        │
        ▼
总纲主流程（强制唯一入口，出口产物门禁）：
  ┌─ 0.0 状态澄清（目标 / 现状模糊时）
  │  0.2 联网调研（可信信号）· 0.1 复用调研（铁律）
  │  0.3 产品完善度诊断 · 0.4 强制双调研与规划
  ├─ 1 接收 → 2 经验库必读 → 3 调研实际资源 → 4 联网调研
  ├─ 5 复用调研 → 6 复述 → 7 疑问必问 → 8 产品视角 + 分级 + 回滚点
  ├─ 9 规划（双调研后）→ 10 执行 → 11 自查与归档
  └─ 规则（43 条，地基）+ 落地细则（173 条，按类按需加载）
```

分层知识、按需加载（上下文纪律）：`SKILL.md` 保持精简；`references/` 按步加载——`rules.md`（43 条地基）、`details.md`（173 条 / 10 类落地细则）、`workflows.md`（前置流程 + 9 类任务）、`security.md`、`platform-adaptation.md`。

### 快速体验

**一分钟跑通**（需要支持 Skill 的 Agent 环境：Claude Code / Trae / Cursor / Codex 等）：

1. **安装**：把 `skill/shisan-xinuo-workflow/` 复制到平台技能目录（见下方安装）；或 `npm install @zxc663/shisan-xinuo-workflow` 后从 `node_modules/` 复制该目录。
2. **加载**：新开会话。Skill 自动执行**第 0 步平台适配**：检测平台、写入约 30 行规则文件（`AGENTS.md`/`CLAUDE.md`/…）、选定提问工具（已有规则先备份再合并，绝不覆盖）。
3. **感受它**：给一个小任务观察——先复述理解、写 3-5 条验收标准、做完自查。再给**风险任务**（如「把这个目录删了」）：必须**先问再动手**——这就是 L3 分级。
4. **目标模式**：说 `目标：整理本目录文件并归组，注意不要删除任何内容`，观察它写计划、设预算、按文件边界拆分、超预算自动停。

一个会话内应看到：任务分级、关键必问、风险操作前回滚点、结束时留档。

### 它做什么

- **第 0 步平台适配与注入**：检测平台，把规则写入 agent 应用**每会话真正自动注入**的位置（绝不写进应用忽略的工作区文件）；询问**按需注入**（默认）还是**强制注入**；平台要求应用内启用时（如 Trae）引导你在应用设置里启用。
- **带出口产物门禁的强制总纲主流程**：11 步是唯一入口，每步先产出出口产物方可进入下一步（可检查、可审计、不可跳步）。前置：状态澄清、联网调研（可信信号）、复用调研（铁律）、产品完善度诊断、强制双调研与规划。
- **43 条规则地基 + 173 条落地细则**：渐进式披露——规则为基础，细粒度工程规范（环境 / 前端 / 数据库 / 测试 / API / 部署运维 / 代码质量 / Git / 会话·备份·治理 / 开发日志深挖）按类按需加载。
- **关键必问协议**：平台无原生提问工具时，提供通用结构化文本兜底协议。
- **双视角**：规划前强制**双调研**（工程师 + 产品经理）；「反复审查 / 存量不足」触发时先做**产品完善度诊断**（功能逻辑 / 代码耦合 / UI / 人性化互动流程 / 其他）。
- **可信联网调研**：市面开源成熟项目是**必须调研**而非降级兜底；以可验证信号 + 本地实测判定可信，绝不凭「网上都说火」。
- **开源安装强制校验**：「开源不等于安全」——来源核验 → 静态扫描 → 权限最小化 → 沙箱实测 → 许可与安全通告 → 结论留档，任一不过即停。
- **回滚安全**：重大修改 / 不可逆操作**前**必须先建回滚点（commit / stash / 快照）。
- **双模式**：普通模式（关键决策必问）+ 目标模式（`目标：`/`目标模式`/`无人值守`/`goal mode` → 按计划自主执行，密钥与破坏性操作仍暂停等待确认）。
- **上下文缺失自检**：Agent 无法感知被压缩，靠两道守卫——显式信号重载 + 开工 / 提交 / 重大决策前核心要素自检。

### 使用场景

- 希望 Agent 在跨项目、跨平台（Trae、Codex、Claude Code、Cursor、CLI 等）时行为一致。
- 希望按风险给自主权：L1 常规直接做，L3 高风险（密钥、删除、迁移、发布）一律先问。
- 希望「目标模式」无人值守运行：先写计划、设预算、按文件边界拆分、超预算自动停。
- 希望会话可审计：验收标准前置、任务记录、会话结束知识沉淀。
- 希望规划同时经工程师与产品双视角审查，而不只是查代码正确性。

### 差异化优势

| 对比对象 | 本 Skill |
|---|---|
| 手写 `AGENTS.md`/`CLAUDE.md` | 渐进式披露、完整引用体系、跨平台适配——不止一页规则，且不拖累每个会话 |
| 平台内置规则 | 平台无关：同一纪律任何平台生效；第 0 步自动适配，无需逐平台重写 |
| 通用系统提示词 | 可操作、可验证、清单驱动：分级表、出口产物门禁、扫描清单——不是空泛口号 |
| 其他工作流 / 提示词类 Skill | 多数只有规则或流程；本 Skill 同时具备**强制流程骨架 + 每步门禁**、**工程师 / 产品双视角**、**可信调研依据**、**开源安装强制校验** |
| 官方技能仓库 | 补位「通用工程执行治理」品类：官方仓库领域技能丰富，跨领域工作纪律稀缺 |

### 局限与代价（如实说明）

- **上下文成本**：即使渐进式披露，治理层仍消耗上下文——这是换取一致性的代价；生成的规则文件控制在约 30 行。
- **依赖强提示词注入**：本质是规范而非工具——无运行时、无强制；行为依赖平台实际注入规则与 description 触发；注入被跳过或描述未命中时，它什么也不会做。
- **依赖 Agent 自律**：无脚本强制执行。懒惰的 Agent 可以不遵守规则，也无法感知自己被压缩——已用自检双守卫缓解。
- **细则体量大**：落地细则 173 条较多——这正是按类按需加载的原因；不做渐进式披露会很重。
- **平台检测是启发式**：靠目录 / 环境变量信号判断；无法确定时直接问用户，不猜。
- **不捆绑工具**：刻意零脚本 / 零依赖 / 零网络。能力缺口用「兜底」解决，而非塞二进制。
- **规范演进**：基于 Agent Skills 开放标准构建；不支持 Skill 的旧平台需手动加载（见安装）。

### 来源与依据

源自真实生产工作流的实战沉淀——包括将 **800KB+ 开发历史**中的真实踩坑提炼为落地细则——按 [Agent Skills 开放规范](https://agentskills.io/)及其[最佳实践](https://agentskills.io/skill-creation/best-practices)重写（渐进式披露、Gotchas、Checklist、Plan-Validate-Execute）。

### 版本差异（英文 / 中文 / 双语）

三个通用版本**内容完全一致**，仅语言不同：

| 版本 | 路径 | 内容语言 | 回答语言 |
|---|---|---|---|
| 英文 | `skill/shisan-xinuo-workflow/` | 英文（标题保留品牌名「十三希诺」） | 跟随用户——**无强制中文** |
| 中文 | `versions/universal-zh/` | 中文 | 跟随用户；文档与记录按项目约定 |
| 双语 | `versions/universal-bilingual/` | 段落级中英对照 | 跟随用户 |

个人工作台版（内嵌个人经验、人格化澄清、中文表达规则）在**独立私有仓库**维护，不属于本公开仓。

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
  SKILL.md                         ← 精简入口：定位、总纲主流程、门禁、引用地图
  references/
    rules.md                       ← 43 条规则地基
    workflows.md                   ← 前置流程（0.0–0.4）+ 9 类任务 + 门禁
    details.md                     ← 173 条落地细则 / 10 类（按需加载）
    platform-adaptation.md         ← 注入点、提问降级链、结构化协议
    security.md                    ← 安全红线、安装校验、回滚、残留扫描
versions/
  universal-zh/                    ← 通用版 · 中文
  universal-bilingual/             ← 通用版 · 中英双语
```

### 版本历史

- **v1.0** — 首版发布（43 条纪律、双模式、回滚、渐进式披露）。
- **v1.1** — 注入点与注入模式（按需 / 强制每会话）。
- **v1.2** — 调研驱动的任务主流程（11 步）。
- **v1.3** — 定位翻转：流程为魂、规则为基；主流程升为唯一入口 + 出口产物门禁；状态澄清前置。
- **v1.3.1** — 联网调研·必须（非降级）+ 最铁铁律（最少代码、绝不自研组件）。
- **v1.3.2** — 联网调研可信信号 + 开源安装强制校验（「开源不等于安全」）。
- **v1.4** — 落地细则（173 条 / 10 类，提炼自真实开发历史）+ 产品完善度诊断（五问定位缺陷）+ 强制双调研与规划（工程师 + 产品经理双视角）。

### 与其他规范的关系

- [Agent Skills / agentskills.io](https://agentskills.io/)：遵循开放标准（文件夹 + `SKILL.md` + 渐进式披露），兼容所有支持 Skills 的客户端。
- [AGENTS.md](https://agents.md/)：第 0 步生成的就是这类跨平台规则文件（精简版），完整工作流保留在 Skill 内按需加载。

### 常见问题

- **为什么不做成一个大规则文件？** 上下文纪律：只预加载 `name`+`description`，激活才读正文，`references/` 按步加载。
- **会覆盖我已有的规则吗？** 不会——先备份再合并，绝不覆盖。
- **会对外发送数据吗？** 不会。纯文档、无脚本、无网络。
- **Agent 能感知自己被压缩吗？** 不能——这正是 Skill 用「显式信号重载 + 关键节点自检」的原因，不依赖压缩感知。
- **联网调研就是「网上说什么信什么」吗？** 不是——它按权威性分级收集可验证可信信号，并以本地实测兜底。

### 贡献者

- **十三希诺** — 作者与维护者（[zxc663](https://github.com/zxc663)）

欢迎贡献：规则改进、工作流补充、本地化修正请开 issue 或 PR。新增规则需先走本 Skill 自带的规则新增流程再合并。

### 许可证

MIT，见 [LICENSE](LICENSE)。
