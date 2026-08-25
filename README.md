# 十三希诺 Agent 工作流 · Shisan Xinuo Agent Workflow

> 一个**依赖于强提示词注入（SKILL.md + 平台规则文件）的通用个人工程工作流程规范**：把真实开发历史中沉淀的 43 条纪律、11 步强制流程（每步含出口产物门禁）、186 条落地细则（11 类），打包成跨平台注入、按需加载、可审计的治理元 Skill（Governance Meta-Skill），驱动任意 Agent 平台（Trae / Codex / Claude Code / Cursor / Windsurf / WorkBuddy / CLI）按统一、可审计的方式工作，**禁止假实现**。
>
> **EN** — A **general-purpose personal engineering-workflow specification delivered through strong prompt injection** (SKILL.md + platform rule files): it packages 43 discipline rules, a mandatory 11-step operating sequence with per-step exit-artifact gates, and 186 landing details in 11 categories — distilled from real development history — into an installable, cross-platform, on-demand-loaded governance meta-skill that drives any Agent platform through a disciplined, auditable way of working, **with no faked completions**.

---

## 目录 · Contents

1. [定位 · Positioning](#定位--positioning)
2. [市场定位（客观）· Market position](#市场定位客观--market-position)
3. [工作原理（体系全景）· How it works](#工作原理体系全景--how-it-works)
4. [快速体验 · Quick start](#快速体验--quick-start)
5. [它做什么 · What it does](#它做什么--what-it-does)
6. [使用场景 · Use cases](#使用场景--use-cases)
7. [差异化优势 · What makes it different](#差异化优势--what-makes-it-different)
8. [局限与代价（如实）· Limitations](#局限与代价如实--limitations)
9. [版本差异（三语）· Edition differences](#版本差异三语--edition-differences)
10. [安装 · Install](#安装--install)
11. [仓库结构 · Repository layout](#仓库结构--repository-layout)
12. [版本历史 · Changelog](#版本历史--changelog)
13. [与其他规范的关系 · Relationship to standards](#与其他规范的关系--relationship-to-standards)
14. [常见问题 · FAQ](#常见问题--faq)
15. [来源与依据 · Where it comes from](#来源与依据--where-it-comes-from)
16. [贡献者与许可 · Contributors & License](#贡献者与许可--contributors--license)

---

## 定位 · Positioning

**本质（如实）**：一个**依赖于强提示词注入的通用个人工程工作流程规范**——无脚本、无运行时、无强制；靠把规则（SKILL.md + 平台规则文件）注入任意 Agent 并依赖其自觉执行。它不只是「保存的提示词」：具备结构化渐进式披露、带每步门禁的强制流程骨架，以及从真实 800KB+ 开发历史提炼的 186 条落地细则。

**EN** — **What it is (honest)**: a *general-purpose personal engineering-workflow specification* delivered through **strong prompt injection** — no scripts, no runtime, no enforcement. It works by injecting rules into any agent and relying on the agent's self-discipline. It is more than a saved prompt: structured progressive disclosure, a mandatory process skeleton with per-step gates, and 186 landing rules distilled from a real 800KB+ development history.

五大支柱 · **Five pillars**：

| 支柱 Pillar | 内容 Content |
|---|---|
| 流程为魂 Workflow is the soul | 强制 11 步任务主流程是每个任务的唯一入口，每步有「出口产物」，无产物不得进入下一步（可检查、可审计、不可跳步）。A mandatory 11-step master sequence is the single entry for every task; each step has an *exit artifact* — checkable, auditable, unskippable. |
| 规则为基 Rules are the foundation | 43 条纪律规则约束流程每步该守什么，与流程强耦合、相互依托。The 43 discipline rules govern what each step must observe, strongly coupled with the workflow. |
| 双视角为镜 Dual eyes as the mirror | 工程师视角 + 产品经理视角：规划前强制双调研；「反复审查 / 存量不足」触发时先做产品完善度诊断。Engineer *and* product-manager views: mandatory dual survey before planning; product-polish diagnosis on repeated-review triggers. |
| 可信证据为依据 Verifiable evidence | 必须联网调研市面开源成熟项目，收集可验证可信信号（stars / 下载量 / 维护 / 被采用 / 口碑 / 安全通告），绝不凭「网上都说火」；本地实测兜底。Mandatory online survey of mature open-source solutions collecting verifiable trust signals; local verification is the final judge. |
| 安全为底线 Safety is the baseline | 「开源不等于安全」：任何 Skill / MCP / 脚本 / 依赖引入前必须走强制校验流程；密钥绝不进代码 / 文档 / 对话。"Open source ≠ safe": mandatory install-vetting flow; secrets never land in code / docs / chat. |

它的**机制层**（流程 / 规则 / 门禁 / 分级）不依赖任何框架，是叠加在任务之上的「工作方式」；**细则层**（`details.md`）确实含绑定具体技术栈（Next.js / Prisma / Playwright 等）的真实工程经验——如实说明：它是**踩坑日志**（什么会错），不是**技术教程**（怎么用），也不替代官方文档。

**EN** — Its **mechanism layer** (workflow / rules / gates / triage) is framework-agnostic — the *way of working* layered on top of any task; its **details layer** (`details.md`) honestly does carry stack-bound engineering experience (Next.js / Prisma / Playwright …) — treat it as a *pitfall log* ("what went wrong"), not as domain tutorials ("how to use X"), and never as a substitute for official docs.

---

## 市场定位（客观）· Market position

- **品类 · Category**：Agent Skills 生态中稀缺的「跨领域工作流治理 / 个人工作流程规范」细分——公开 36 万+ 技能绝大多数是领域型 SOP（code review / git / 部署 / 视觉…）。The scarce "cross-domain workflow-governance" niche inside the Agent Skills ecosystem — most of the 360K+ public skills are domain-specific SOPs.
- **形态 · Form**：纯文档 / 强提示词注入型，不同于代码工具（MCP）、Agent 框架或编排层。优势是可移植；代价是零强制执行。Pure-document / strong-prompt-injection, unlike code tools or orchestration layers. Portable; but zero enforcement.
- **契合 · Fit**：符合生态当前「Skills = 工作流节点 / SOP 封装」的共识（Anthropic 与 OpenAI 开放标准、渐进式披露）。Matches the ecosystem's "skills as workflow nodes" consensus.
- **诚实风险 · Honest risks**：研究（[SWE-Skills-Bench](https://arxiv.org/abs/2603.15401)：39/49 个技能零收益、token 开销约 451%；OpenAI「文件可迁移，信任边界不可迁移」——出处待核实）警示纯提示词型技能易沦为 pass-through——本 Skill 以渐进式披露与注入点纪律缓解，但仍依赖 description 触发质量与 Agent 自律。Research warns that prompt-only skills can become pass-through; this skill mitigates with progressive disclosure and injection-point discipline, but still depends on description-based triggering and agent self-discipline.

---

## 工作原理（体系全景）· How it works

```
平台适配（第 0 步：检测 → 注入点 → 按需 / 强制注入）
Platform adaptation (Step 0: detect → injection point → on-demand / forced)
        │
        ▼
总纲主流程（强制唯一入口，出口产物门禁）· Master sequence (mandatory single entry, exit-artifact gates):
  ┌─ 0.0 状态澄清（目标 / 现状模糊时）· status clarification
  │  0.1 主流程细节 · 0.2 联网调研（可信信号）· online survey
  │  0.3 产品完善度诊断（触发式）· product-polish diagnosis
  │  0.4 强制双调研与规划（规划前必过）· mandatory dual survey
  ├─ 1 接收 → 2 经验库必读 → 3 调研实际资源 → 4 联网调研（必须）
  ├─ 5 复用调研（铁律）→ 6 复述理解 → 7 疑问必问 → 8 产品视角+分级+回滚点
  ├─ 9 规划（双调研后，含 3-5 条可验证验收标准）→ 10 执行 → 11 自查与归档
  └─ 规则（43 条，地基）Rules + 落地细则（186 条 / 11 类，按类按需加载）Details
```

分层知识、按需加载（上下文纪律）：`SKILL.md` 保持精简（<500 行）；`references/` 按步加载——`rules.md`（43 条地基）、`details.md`（186 条 / 11 类落地细则）、`workflows.md`（前置 0.0-0.4 + 9 类任务）、`security.md`、`platform-adaptation.md`。

**EN** — Layered knowledge, loaded on demand (context discipline): `SKILL.md` stays lean; `references/` load per step — `rules.md` (43, the foundation), `details.md` (186 fine-grained rules in 11 categories), `workflows.md` (preludes 0.0–0.4 + 9 task types), `security.md`, `platform-adaptation.md`.

---

## 快速体验 · Quick start

**一分钟跑通**（需要支持 Skill 的 Agent 环境：Claude Code / Trae / Cursor / Codex 等）· **Try it in under a minute** (needs a skills-capable agent):

1. **安装 Install**：把 `skill/shisan-xinuo-workflow/` 复制到平台技能目录（见下方安装）；或从 `dist/` 解压发布 zip。Copy the skill folder into your platform's skill directory (see Install below), or unpack the release zip from `dist/`.
2. **加载 Load**：新开会话。Skill 自动执行**第 0 步平台适配**：检测平台、询问**按需 / 强制注入**、把约 30 行规则文件（`AGENTS.md`/`CLAUDE.md`/…）写入 agent 应用**每会话真正自动注入**的位置（已有规则先备份再合并，绝不覆盖）；平台要求应用内启用时（如 Trae）引导你在应用设置启用。Step 0 runs automatically: detects the platform, asks on-demand/forced injection, writes a ~30-line rule file into the location the app *actually auto-injects every session* (backup + merge, never overwrite).
3. **感受它 Feel it**：给一个小任务观察——先复述理解、写 3-5 条验收标准、做完自查。给**风险任务**（如「把这个目录删了」）：必须**先问再动手**——这就是 L3 分级。Give it a small task — it restates understanding, writes acceptance criteria, self-checks. Give it a **risk task** — it must ask first (L3 triage).
4. **目标模式 Goal mode**：说 `目标：整理本目录文件并归组，注意不要删除任何内容`，观察它写计划、设预算、按文件边界拆分、超预算自动停。Say `目标：…` and watch it plan, set budgets, split by file boundaries and stop over budget.

一个会话内应看到：任务分级、关键必问、风险操作前回滚点、结束时留档。Expected within one session: task triage, ask-before-acting, rollback before risky ops, records at the end.

---

## 它做什么 · What it does

- **第 0 步平台适配与注入 · Step 0 platform adaptation & injection**：检测平台，写入 app 每会话真正自动注入的位置（绝不写进应用忽略的工作区文件）；询问按需（默认）/ 强制注入；应用内需启用时引导启用并确认生效。Detects the platform, injects into the location the app actually reads every session; asks on-demand (default) / forced; guides in-app enablement (e.g. Trae).
- **带出口产物门禁的强制总纲主流程 · Mandatory master sequence with exit-artifact gates**：11 步是唯一入口，每步先产出出口产物方可进入下一步（可检查、可审计、不可跳步）；无法产出的步须在任务记录写明理由。The 11-step sequence is the single entry; each step requires its exit artifact before the next (checkable, auditable, unskippable).
- **43 条规则地基 + 186 条落地细则 / 11 类 · 43-rule foundation + 186 landing details in 11 categories**：渐进式披露——规则为基础；细粒度工程规范（环境 / 前端 / 数据库 / 测试 / API 契约 / 部署运维 / 代码质量 / Git / 会话·备份·治理 / 开发日志深挖 / 铁律纪律）按类按需加载。Progressive disclosure; fine-grained engineering specifics loaded per category on demand.
- **关键必问协议 · Ask-before-acting protocol**：平台无原生提问工具时，提供通用结构化文本兜底协议（理解 / 选项与利弊 / 风险与后果 / 推荐方案，结束回合等待）。Text-protocol fallback for platforms without a native asking tool.
- **双视角 · Dual perspectives**：规划前强制双调研（工程师 + 产品经理）；「反复审查 / 存量不足」触发时先做产品完善度诊断（功能逻辑 / 代码耦合 / UI / 人性化互动流程 / 其他）。Mandatory dual survey before planning; product-polish diagnosis on repeated-review triggers.
- **可信联网调研 · Verifiable online survey**：市面开源成熟项目是**必须调研**而非降级兜底；以可验证信号 + 本地实测判定可信。Mandatory, not a fallback; trust judged by verifiable signals + local verification.
- **开源安装强制校验 · Mandatory install vetting**：「开源不等于安全」——来源核验 → 静态扫描 → 权限最小化 → 沙箱实测 → 许可与安全通告 → 结论留档，任一不过即停。"Open source ≠ safe": source verification → static scan → least privilege → sandbox test → license & advisories → recorded conclusion.
- **回滚安全 · Rollback safety**：重大修改 / 不可逆操作**前**必须先建回滚点（commit / stash / 快照）。Rollback point required *before* major changes or irreversible operations.
- **双模式 · Dual modes**：普通模式（关键决策必问）+ 目标模式（`目标：`/`无人值守`/`goal mode` → 按计划自主执行，密钥与破坏性操作仍暂停）。Normal mode + goal mode (autonomous per plan; secrets & destructive ops still pause).
- **L1 快速通道 · L1 fast path**：第 1 步后先判级——L1 常规任务走「一句话复述 → 最小修改 → 最小验证 → 汇报」快速通道（显式标注，非静默跳步），L2/L3 仍走完整 11 步。Triage-first: L1 routine takes a fast lane; L2/L3 keep the full sequence.
- **记忆文件协议 · Memory-file protocol**：外部化长期记忆——项目 `memory/` 文件记录目标 / 决策 / 约束 / 进度，关键节点与上下文 40-60% 前写入，压缩 / 重置后先读再继续。Externalized long-term memory: write at milestones, read first after compaction.
- **上下文缺失自检 · Context-loss self-check**：Agent 无法感知被压缩——两道守卫：显式信号重载 + 开工 / 提交 / 重大决策前核心要素自检。Two guards: reload on explicit signals + milestone self-checks.

---

## 使用场景 · Use cases

- 希望 Agent 在跨项目、跨平台（Trae / Codex / Claude Code / Cursor / CLI 等）行为一致。Consistent agent behavior across projects and platforms.
- 希望按风险给自主权：L1 常规直接做，L3 高风险（密钥、删除、迁移、发布）一律先问。Risk-based autonomy: L1 done directly, L3 always asked first.
- 希望「目标模式」无人值守运行：先写计划、设预算、按文件边界拆分、超预算自动停。Unattended goal-mode runs with written plan, budgets, file-boundary isolation, auto-stop.
- 希望会话可审计：验收标准前置、任务记录、会话结束知识沉淀（双写）。Auditable sessions: acceptance criteria up front, task records, post-session knowledge distillation.
- 希望规划同时经工程师与产品双视角审查，而不只是查代码正确性。Planning reviewed from both engineer and product angles, not just code-correctness.

---

## 差异化优势 · What makes it different

| 对比对象 Compare with | 本 Skill This skill |
|---|---|
| 手写 `AGENTS.md` / `CLAUDE.md` | 渐进式披露、完整引用体系、跨平台适配——不止一页规则，且不拖累每个会话。Progressive disclosure, full reference body, cross-platform adaptation. |
| 平台内置规则 Platform built-in rules | 平台无关：同一纪律任何平台生效；第 0 步自动适配，无需逐平台重写。Platform-independent; Step 0 adapts instead of rewriting rules per tool. |
| 通用系统提示词 Generic system prompts | 可操作、可验证、清单驱动：分级表、出口产物门禁、扫描清单——不是空泛口号。Operational, verifiable, checklist-driven. |
| 其他工作流 / 提示词类 Skill Other workflow skills | 多数只有规则或流程；本 Skill 同时具备**强制流程骨架 + 每步门禁**、**工程师/产品双视角**、**可信调研依据**、**开源安装强制校验**。Most ship rules or a process; this one adds a mandatory process skeleton with gates, dual views, verifiable survey basis, and mandatory install vetting. |
| 官方技能仓库 Official skills repos | 补位「通用工程执行治理」品类：官方仓库领域技能丰富，跨领域工作纪律稀缺。Fills the "general engineering-execution governance" niche. |

---

## 局限与代价（如实）· Limitations

- **上下文成本 Context cost**：即使渐进式披露，治理层仍消耗上下文——这是换取一致性的代价；生成的规则文件控制在约 30 行。A governance layer consumes context — the trade-off for consistency; generated rule files are kept ~30 lines.
- **依赖强提示词注入 Strong-prompt-injection dependent**：本质是规范而非工具——无运行时、无强制；注入被跳过或描述未命中时，它什么也不会做。It is a specification, not a tool; if injection is skipped or the description fails to match, it does nothing.
- **依赖 Agent 自律 Agent self-discipline**：无脚本强制执行；懒惰的 Agent 可以不遵守规则，也无法感知自己被压缩——用自检双守卫缓解。No scripts enforce anything; mitigated by the self-check guards.
- **细则体量大 Detail volume**：落地细则 186 条较多——这正是按类按需加载的原因。186 rules is heavy — hence per-category on-demand loading.
- **平台检测是启发式 Detection heuristics**：靠目录 / 环境变量信号判断；无法确定时直接问用户，不猜。Best-effort; asks rather than guesses when ambiguous.
- **不捆绑工具 Zero tooling bundled**：刻意零脚本 / 零依赖 / 零网络；能力缺口用「兜底」解决。Deliberately zero scripts / dependencies / network; gaps handled by fallbacks.
- **规范演进 Spec evolution**：基于 Agent Skills 开放标准构建；不支持 Skill 的旧平台需手动加载。Built on the Agent Skills open standard; older platforms need manual loading.

---

## 版本差异（三语）· Edition differences

三个通用版本**内容完全一致**，仅语言不同；另有独立私有工作台版（不进本公开仓）。The three universal editions are content-identical, differing only in language; a private personal-workstation edition is maintained separately and is **not** part of this public repo.

| 版本 Edition | 路径 Path | 内容语言 Content language | 回答语言 Reply language |
|---|---|---|---|
| 英文 English | `skill/shisan-xinuo-workflow/` | 英文（标题保留品牌名「十三希诺」）| 跟随用户——无强制中文 |
| 中文 中文 | `versions/universal-zh/` | 中文 | 跟随用户；文档与记录按项目约定 |
| 双语 Bilingual | `versions/universal-bilingual/` | 段落级中英对照 | 跟随用户 |
| 工作台版（私有）Personal (private) | 独立私有仓 | 中英混合 + 内嵌个人经验手册 | 统一中文 |

---

## 安装 · Install

把 skill 目录复制到所用平台的技能目录；纯文档、零依赖、零网络调用，加载即自动适配平台。Copy the skill folder into your platform's skills directory; pure documentation, zero deps, zero network — loading is enough, Step 0 adapts it to the platform.

| 平台 Platform | 位置 Location |
|---|---|
| Claude Code | `~/.claude/skills/shisan-xinuo-workflow/` |
| Codex / 通用环境 | 克隆本仓库，将技能发现指向 `skill/shisan-xinuo-workflow/`；或解压 `dist/` 发布 zip |
| Trae / Cursor / 其他 | 按平台技能目录约定放置；`Trae` 需在应用设置启用项目规则 |
| npm（GitHub Packages） | `npm install @zxc663/shisan-xinuo-workflow` 后从 `node_modules/` 复制 skill 目录 |

---

## 仓库结构 · Repository layout

```
shisan-xinuo-workflow/              ← 仓库根
├── README.md                       ← 本文件（双语 · 中文优先）
├── LICENSE                         ← MIT
├── 项目信息.md                      ← 内部维护文档（供下一个 AI 助手读写）
├── package.json / .npmrc           ← npm 发行物配置（GitHub Packages）
├── dist/                           ← 版本发布 zip（v1.0.0 … v1.4.1）
├── skill/shisan-xinuo-workflow/    ← 默认交付（英文）
│   ├── SKILL.md                    ← 精简入口：定位、总纲主流程、门禁、引用地图
│   └── references/                 ← 按需加载的引用
│       ├── rules.md                ← 43 条规则地基
│       ├── workflows.md            ← 前置 0.0-0.4 + 9 类任务 + 门禁
│       ├── details.md              ← 186 条落地细则 / 11 类
│       ├── platform-adaptation.md  ← 注入点、提问降级链、结构化协议
│       └── security.md             ← 安全红线、安装校验、回滚、残留扫描
└── versions/
    ├── universal-zh/               ← 通用版 · 中文
    └── universal-bilingual/        ← 通用版 · 中英双语
```

---

## 版本历史 · Changelog

- **v1.0** — 首版发布（43 条纪律、双模式、回滚、渐进式披露）。
- **v1.1** — 注入点与注入模式（按需 / 强制每会话）。
- **v1.2** — 调研驱动的任务主流程（11 步）。
- **v1.3** — 定位翻转：流程为魂、规则为基；主流程升为唯一入口 + 出口产物门禁；状态澄清前置。
- **v1.3.1** — 联网调研·必须（非降级）+ 最铁铁律（最少代码、绝不自研组件）。
- **v1.3.2** — 联网调研可信信号 + 开源安装强制校验（「开源不等于安全」）。
- **v1.4** — 落地细则（186 条 / 11 类，含开发日志深挖 + 铁律纪律补充）+ 产品完善度诊断 + 强制双调研 + 五支柱定位 + README 重构。
- **v1.4.1** — 文档一致性修复：README 条数校准（173→186 / 10 类→11 类）、英文版 details.md 类别编号重排（缺 4 / 重复 9）、四版 SKILL.md 引用地图补全 11 类、决策记录「待推送 / 不推送」状态对齐发布记录、补研究引用链接；新增「双仓同步检查清单」。
- **v1.4.2** — ①**定位诚实话**：不再宣称「不含领域知识」——机制层跨领域，细则层（details.md）如实声明为绑定具体技术栈的**踩坑日志**而非技术教程（修正自第三方审阅意见）；②**L1 快速通道**：第 1 步后先判级，L1 常规任务走「复述→最小修改→最小验证→汇报」快速通道，治「简单任务杀鸡用牛刀」；③**记忆文件协议**：外部化长期记忆（`memory/` 状态文件，压缩 / 重置后先读再继续），治「上下文稀释」。

**EN — v1.4.1** — documentation-consistency fixes: README numbers calibrated (173→186 / 10→11 categories), English details.md category numbering fixed (missing 4 / duplicate 9), all four SKILL.md reference maps expanded to 11 categories, decision-record push-status aligned with release records, research citations added; plus a two-repo sync checklist.
**EN — v1.4.2** — ① honest positioning: mechanisms are framework-agnostic, but the details layer is now honestly declared a stack-bound **pitfall log**, not a tutorial; ② **L1 fast path** (triage-first, fixes over-governance on trivial tasks); ③ **memory-file protocol** (externalized long-term memory — write at milestones, read first after compaction, fixes context dilution).

---

## 与其他规范的关系 · Relationship to standards

- [Agent Skills / agentskills.io](https://agentskills.io/)：遵循开放标准（文件夹 + `SKILL.md` + 渐进式披露），兼容所有支持 Skills 的客户端。Follows the open standard; runs on any skills-compatible client.
- [AGENTS.md](https://agents.md/)：第 0 步生成的就是这类跨平台规则文件（精简版），完整工作流保留在 Skill 内按需加载。Step 0 generates exactly this kind of cross-platform rule file, in condensed form.

---

## 常见问题 · FAQ

- **为什么不做成一个大规则文件？** 上下文纪律：只预加载 `name`+`description`，激活才读正文，`references/` 按步加载。Why not one big rule file? Context discipline: only name+description preload; references load per step.
- **会覆盖我已有的规则吗？** 不会——先备份再合并，绝不覆盖。Will it overwrite my rules? No — backup + merge only.
- **会对外发送数据吗？** 不会。纯文档、无脚本、无网络。Does it send data anywhere? No. Pure documentation; no scripts; no network.
- **Agent 能感知自己被压缩吗？** 不能——这正是 Skill 用「显式信号重载 + 关键节点自检」的原因。Can the agent detect compaction? No — hence the explicit-signal reload + milestone self-checks.
- **联网调研就是「网上说什么信什么」吗？** 不是——它按权威性分级收集可验证可信信号，并以本地实测兜底。Is the survey just "whatever the web says"? No — verifiable trust signals with a defined authority hierarchy, local verification as the final judge.

---

## 来源与依据 · Where it comes from

源自真实生产工作流的实战沉淀——包括将 **800KB+ 开发历史**中的真实踩坑提炼为落地细则——按 [Agent Skills 开放规范](https://agentskills.io/)及其[最佳实践](https://agentskills.io/skill-creation/best-practices)重写（渐进式披露、Gotchas、Checklist、Plan-Validate-Execute）。

**EN** — Battle-tested in real production workflows, including a 800KB+ development history whose real pitfalls were distilled into the landing details, rewritten against the [Agent Skills specification](https://agentskills.io/) and its [best practices](https://agentskills.io/skill-creation/best-practices).

---

## 贡献者与许可 · Contributors & License

- **十三希诺** — 作者与维护者 Author & maintainer（[zxc663](https://github.com/zxc663)）
- 欢迎贡献：规则改进、工作流补充、本地化修正请开 issue 或 PR；新增规则需先走 Skill 自带的规则新增流程再合并。Contributions welcome via issue or PR; new rules follow the skill's own rule-addition process before merging.
- **许可 License**：MIT，见 [LICENSE](LICENSE)。