# 十三希诺 Agent 工作流 · Shisan Xinuo Agent Workflow

> **一个按需调用的「渐进式」工程治理 Skill**：不是把整本手册一次性砸进上下文，而是像神经系统一样——只在任务到达某个步骤（如开始调研、准备提交）时，才注入那一步所需的少量规则；只在任务被识别为 L1 常规时才走快速通道。它把真实开发历史中沉淀的 **43 条纪律、11 步主流程（每步出口产物门禁）、203 条落地细则（12 类）**，打包成跨平台（Trae / Codex / Claude Code / Cursor / Windsurf / WorkBuddy / CLI）注入、按需加载、可审计的治理元 Skill（Governance Meta-Skill），驱动 Agent 按统一、可审计的方式工作，**禁止假实现**。
>
> **EN** — An **on-demand, progressive engineering-governance Skill**: not a whole manual dumped into context at once, but a nervous system — it injects only the few rules a step needs (survey, commit, …) when that step arrives, and routes L1 trivial tasks to a fast lane. It packages **43 discipline rules, an 11-step master sequence (per-step exit-artifact gates), and 203 landing details in 12 categories** — distilled from real development history — into a cross-platform, on-demand-loaded, auditable governance meta-skill, driving any Agent platform with **no faked completions**.

---

## 目录 · Contents

1. [一句话定位 · One-line positioning](#一句话定位--one-line-positioning)
2. [它为谁解决什么 · Who is this for](#它为谁解决什么--who-is-this-for)
3. [工作原理（渐进式 / 状态机）· How it works](#工作原理渐进式--状态机--how-it-works)
4. [架构真相（诚实）· Architecture truths](#架构真相诚实--architecture-truths)
5. [快速体验 · Quick start](#快速体验--quick-start)
6. [它做什么 · What it does](#它做什么--what-it-does)
7. [差异化优势 · What makes it different](#差异化优势--what-makes-it-different)
8. [使用场景 · Use cases](#使用场景--use-cases)
9. [局限与代价（如实）· Limitations](#局限与代价如实--limitations)
10. [版本差异（三语）· Edition differences](#版本差异三语--edition-differences)
11. [安装 · Install](#安装--install)
12. [仓库结构 · Repository layout](#仓库结构--repository-layout)
13. [版本历史 · Changelog](#版本历史--changelog)
14. [与其他规范的关系 · Relationship to standards](#与其他规范的关系--relationship-to-standards)
15. [常见问题 · FAQ](#常见问题--faq)
16. [来源与依据 · Where it comes from](#来源与依据--where-it-comes-from)
17. [贡献者与许可 · Contributors & License](#贡献者与许可--contributors--license)

---

## 一句话定位 · One-line positioning

**中文**：这是一个「渐进式披露 + 按需注入」的工程治理 Skill——它不会在会话启动时预载全部规则，而是在任务推进到具体步骤时（调研 / 复用判断 / 规划 / 提交 / 回滚）才加载该步所需的少量规则；它按任务风险分级动态路由（L1 走快速通道，L2/L3 走完整主流程）。机制层（流程 / 规则 / 门禁 / 分级）与框架无关；细则层（details.md）是绑定具体技术栈的踩坑日志。价值：治理一致性、可审计性、防假实现——代价：依赖平台注入与 Agent 自律，无运行时强制。

**EN** — A progressive-disclosure engineering-governance Skill that loads rules *per step, on demand* and routes tasks by risk tier (L1 fast lane; L2/L3 full sequence). The mechanism layer is framework-agnostic; the details layer is a stack-bound pitfall log. Value: governance consistency, auditability, no-fake-completions; cost: depends on injection + agent self-discipline, zero runtime enforcement.

---

## 它为谁解决什么 · Who is this for

- **重度 AI 编码用户**（Cursor / Claude Code / Trae 深度用户）：希望 Agent 跨项目、跨平台行为一致、可审计，尤其痛恨「假完成 / 伪造测试 / 虚报数据」。
- **需要按风险放权的人**：L1 常规直接做，L3 高风险（密钥、删除、迁移、发布）一律先问。
- **想要无人值守目标模式的人**：`目标：…` → 写计划、设预算、按文件边界拆分、超预算自动停。
- **想省 token 又不丢纪律的人**：渐进式加载 + L1 快速通道，避免在小任务上过度消耗上下文。
- **做 Agent 生态研究 / 开源设计的人**：了解「渐进式 Skill」如何把静态约束变成动态治理。

---

## 工作原理（渐进式 / 状态机）· How it works

```
平台适配（第 0 步：检测 → 注入点 → 按需 / 强制注入）
Platform adaptation (Step 0: detect → injection point → on-demand / forced)
        │
        ▼
任务判级（Triage-first，每任务开始）┐
  ├─ L1 常规 → 快速通道：一句话复述 → 最小修改 → 最小验证 → 汇报
  └─ L2 / L3 → 完整 11 步主流程（每步出口产物门禁）：
      ├─ 0.0 状态澄清（目标 / 现状模糊时）· status clarification
      │  0.1 主流程细节 · 0.2 联网调研（可信信号）· online survey
      │  0.3 产品完善度诊断（触发式）· product-polish diagnosis
      │  0.4 强制双调研与规划（规划前必过）· mandatory dual survey
      ├─ 1 接收 → 2 经验库必读 → 3 调研实际资源 → 4 联网调研（必须）
      ├─ 5 复用调研（铁律）→ 6 复述理解 → 7 疑问必问 → 8 产品视角+分级+回滚点
      ├─ 9 规划（双调研后，含 3-5 条可验证验收标准）→ 10 执行 → 11 自查与归档
      └─ 规则（43 条，地基）Rules + 落地细则（203 条 / 12 类，按类按需加载）Details
```

**渐进式（Progressive）体现在三层**：
1. **入口精简**：平台只预加载 `name` + `description`（约几 KB）；激活才读 SKILL.md 正文（<500 行）。
2. **按步加载**：`references/` 只在对应步骤需要时才读——`rules.md`（地基）、`details.md`（按类按需）、`workflows.md`、`security.md`、`platform-adaptation.md`。
3. **动态路由**：任务判级前置 → L1 走快速通道（省上下文），L2/L3 走完整主流程（兜底线）；触发式诊断（反复审查 → 产品完善度诊断）。

**上下文纪律**：`SKILL.md` 精简；规则文件约 30 行；记忆文件（`memory/`）一屏内；压缩后先读记忆再继续。

---

## 架构真相（诚实）· Architecture truths

> 供人（和 AI）快速判断它到底是什么、做不到什么。**全无脚本 / 无运行时 / 无网络调用**——它是一份规范，不是工具。

| 真相 Truth | 说明 Detail |
|---|---|
| 本质是「强提示词注入」 | 无脚本、无运行时、无强制；靠把规则注入 Agent 并依赖其自觉。It is a specification, not a tool. |
| 记忆靠「外部化文件」 | Agent 无长期记忆、也无法感知上下文压缩——用 `memory/` 文件 + 显式重载顺序 + 关键节点自检兜底（见 FAQ）。 |
| 细则层绑技术栈 | `details.md` 含真实项目踩坑（Next.js / Prisma / Playwright 等）——是**踩坑日志**不是**技术教程**。 |
| 不提供「硬门禁」 | 强制依赖平台（hooks / CI / 沙箱）——本 Skill 不捆绑工具；能力缺口用「兜底」。 |
| 定位是「治理层」 | 不替代领域知识、不替代项目自身文档——冲突时项目文档优先。 |

---

## 快速体验 · Quick start

**一分钟跑通**（需要支持 Skill 的 Agent 环境：Claude Code / Trae / Cursor / Codex 等）· **Try it in under a minute** (needs a skills-capable agent):

1. **安装 Install**：把 `skill/shisan-xinuo-workflow/` 复制到平台技能目录（见下方安装）；或从 `dist/` 解压发布 zip。Copy the skill folder into your platform's skill directory, or unpack the release zip from `dist/`.
2. **加载 Load**：新开会话。Skill 自动执行**第 0 步平台适配**：检测平台、询问**按需 / 强制注入**、把约 30 行规则文件（`AGENTS.md`/`CLAUDE.md`/…）写入 agent 应用**每会话真正自动注入**的位置（已有规则先备份再合并，绝不覆盖）；平台要求应用内启用时（如 Trae）引导你在应用设置启用。Step 0 runs automatically: detects the platform, asks on-demand/forced injection, writes a ~30-line rule file into the location the app *actually auto-injects every session* (backup + merge, never overwrite).
3. **感受它 Feel it**：给一个小任务观察——先复述理解、写 3-5 条验收标准、做完自查。给**风险任务**（如「把这个目录删了」）：必须**先问再动手**——这就是 L3 分级。Give it a small task — it restates understanding, writes acceptance criteria, self-checks. Give it a **risk task** — it must ask first (L3 triage).
4. **目标模式 Goal mode**：说 `目标：整理本目录文件并归组，注意不要删除任何内容`，观察它写计划、设预算、按文件边界拆分、超预算自动停。Say `目标：…` and watch it plan, set budgets, split by file boundaries and stop over budget.

一个会话内应看到：任务分级、关键必问、风险操作前回滚点、结束时留档。Expected within one session: task triage, ask-before-acting, rollback before risky ops, records at the end.

---

## 它做什么 · What it does

- **第 0 步平台适配与注入 · Step 0 platform adaptation & injection**：检测平台，写入 app 每会话真正自动注入的位置（绝不写进应用忽略的工作区文件）；询问按需（默认）/ 强制注入；应用内需启用时引导启用并确认生效。Detects the platform, injects into the location the app actually reads every session; asks on-demand (default) / forced; guides in-app enablement (e.g. Trae).
- **带出口产物门禁的强制总纲主流程 · Mandatory master sequence with exit-artifact gates**：11 步是唯一入口，每步先产出出口产物方可进入下一步（可检查、可审计、不可跳步）；无法产出的步须在任务记录写明理由。The 11-step sequence is the single entry; each step requires its exit artifact before the next (checkable, auditable, unskippable).
- **L1 快速通道 · L1 fast path**：第 1 步后先判级——L1 常规任务走「一句话复述 → 最小修改 → 最小验证 → 汇报」快速通道（显式标注，非静默跳步），L2/L3 仍走完整 11 步。Triage-first: L1 routine takes a fast lane; L2/L3 keep the full sequence.
- **43 条规则地基 + 203 条落地细则 / 12 类 · 43-rule foundation + 203 landing details in 12 categories**：渐进式披露——规则为基础；细粒度工程规范（环境 / 前端 / 数据库 / 测试 / API 契约 / 部署运维 / 代码质量 / Git / 会话·备份·治理 / 开发日志深挖 / 铁律纪律 / 源项目深挖补充）按类按需加载。Progressive disclosure; fine-grained engineering specifics loaded per category on demand.
- **记忆文件协议 · Memory-file protocol**：外部化长期记忆——项目 `memory/` 文件记录目标 / 决策 / 约束 / 进度，关键节点与上下文 40-60% 前写入，压缩 / 重置后先读再继续。Externalized long-term memory: write at milestones, read first after compaction.
- **压缩后显式重载 · Reload sequence after compaction**：用户说「重载 / 你被压缩了」或平台重置上下文 → ①重读 SKILL.md → ②重读 memory/ → ③重读当前引用 → ④向用户复述任务与验收再继续。Explicit reload order: SKILL.md → memory file → references → restate task + acceptance.
- **关键必问协议 · Ask-before-acting protocol**：平台无原生提问工具时，提供通用结构化文本兜底协议（理解 / 选项与利弊 / 风险与后果 / 推荐方案，结束回合等待）。Text-protocol fallback for platforms without a native asking tool.
- **双视角 · Dual perspectives**：规划前强制双调研（工程师 + 产品经理）；「反复审查 / 存量不足」触发时先做产品完善度诊断（功能逻辑 / 代码耦合 / UI / 人性化互动流程 / 其他）。Mandatory dual survey before planning; product-polish diagnosis on repeated-review triggers.
- **可信联网调研 · Verifiable online survey**：市面开源成熟项目是**必须调研**而非降级兜底；以可验证信号 + 本地实测判定可信。Mandatory, not a fallback; trust judged by verifiable signals + local verification.
- **开源安装强制校验 · Mandatory install vetting**：「开源不等于安全」——来源核验 → 静态扫描 → 权限最小化 → 沙箱实测 → 许可与安全通告 → 结论留档，任一不过即停。"Open source ≠ safe": source verification → static scan → least privilege → sandbox test → license & advisories → recorded conclusion.
- **回滚安全 · Rollback safety**：重大修改 / 不可逆操作**前**必须先建回滚点（commit / stash / 快照）。Rollback point required *before* major changes or irreversible operations.
- **双模式 · Dual modes**：普通模式（关键决策必问）+ 目标模式（`目标：`/`无人值守`/`goal mode` → 按计划自主执行，密钥与破坏性操作仍暂停）。Normal mode + goal mode (autonomous per plan; secrets & destructive ops still pause).
- **上下文缺失自检 · Context-loss self-check**：Agent 无法感知被压缩——两道守卫：显式信号重载（含重载顺序）+ 开工 / 提交 / 重大决策前核心要素自检。Two guards: reload on explicit signals + milestone self-checks.
- **安静模式 · Quiet mode**：关键词 `安静模式` / `quiet`——L1 任务只汇报结果（隐藏中间推理 / 调研展示），降视觉噪音与 Token 焦虑；L2/L3 与密钥 / 破坏性操作不受影响。L1 reports only results; L2/L3 and secrets/destructive ops unchanged.
- **偏好记忆 · Preference memory**：用户确认的技术栈 / 语言 / 风格写入 `memory/`「用户偏好」字段，会话开始读取、同类决策直接采用不再重复问。Confirmed choices are remembered and reused instead of re-asking.
- **原子操作锁 · Atomic-operation lock**：L3 破坏性操作（删除 / 迁移 / 覆盖写 / 发布）先输出待执行命令清单、结束回合等用户确认再执行——最后一道闸门交给人类。L3 destructive ops output the command list and wait for human confirmation.
- **配套模板 · Templates**：`templates/` 提供规划 / 验收标准 / 任务记录 / 复盘 / 回滚点 / 提示词预算 6 类模板（复制填写，不原地编辑）。Ready-to-fill templates (plan / acceptance / task-record / retrospective / rollback / prompt-budget) live in `templates/`; copy & fill.
- **提示词预算 · Prompt budget**：可选预算档位（nano / minimal / standard / full）控制渐进式加载深度，让记忆文件与任务记录保持在 token 预算内（预算指引非强制）。Optional budget profiles control on-demand loading depth; budgets are guidance, not enforcement.
- **会话启动钩子 · Session-start hook**：平台支持时（如 Claude Code `SessionStart`）可自动打印纪律横幅，把「强制注入」从靠文本自觉升级为平台钩子自动执行（配置示例，可选）。Session-start hook auto-prints the discipline banner (config example, optional).
- **审查 / 风险 / 安全子代理 · Review sub-agents**：`templates/agents/` 提供 critic（对抗式方案评审）/ risk-reviewer（风险评审）/ security-auditor（安全审计）子代理模板，提升第 11 步独立审查。Optional sub-agent templates (critic / risk-reviewer / security-auditor) strengthen independent review.
- **永不清单 · Never list**：`references/never-list.md` 将 7 类明线禁止项（假完成 / 密钥 / 跳步 / Git / 复用 / 提问 / 提示注入）浓缩为一页自查表。The NEVER list condenses 7 categories of bright-line prohibitions into a one-page self-check.

---

## 差异化优势 · What makes it different

| 对比对象 Compare with | 本 Skill This skill |
|---|---|
| 手写 `AGENTS.md` / `CLAUDE.md` | 渐进式披露、完整引用体系、跨平台适配——不止一页规则，且不拖累每个会话。Progressive disclosure, full reference body, cross-platform adaptation. |
| 平台内置规则 Platform built-in rules | 平台无关：同一纪律任何平台生效；第 0 步自动适配，无需逐平台重写。Platform-independent; Step 0 adapts instead of rewriting rules per tool. |
| 通用系统提示词 Generic system prompts | 可操作、可验证、清单驱动：分级表、出口产物门禁、扫描清单——不是空泛口号。Operational, verifiable, checklist-driven. |
| 静态规则包 / 单文件提示词 | 本 Skill 是**渐进式**：按步加载 + 判级动态路由（L1 快速通道），不是一次全量注入。Progressive, triage-routed, on-demand — not a one-shot static dump. |
| 其他工作流 / 提示词类 Skill Other workflow skills | 多数只有规则或流程；本 Skill 同时具备**强制流程骨架 + 每步门禁**、**判级动态路由**、**工程师/产品双视角**、**可信调研依据**、**开源安装强制校验**、**记忆文件协议 + 压缩重载**。Most ship rules or a process; this one adds gates, triage routing, dual views, verifiable survey, install vetting, and memory/reload discipline. |
| 官方技能仓库 / 同类治理 Skill Official repos / peer governance skills | **工程治理全家桶完整度第一**：多数项目只有规则、流程或模板之一；本 Skill 同时集齐 43 条规则地基 + 11 步流程门禁 + 203 条落地细则 + 跨平台注入 + 双视角 + 记忆协议 + 压缩重载 + 配套模板 / 预算 / 钩子 / 审查子代理 / 永不清单，一套完整闭环。The most complete engineering-governance package — rules + gated process + landing details + cross-platform injection + dual views + memory/reload + templates / budget / hooks / review sub-agents / never-list in one. |

---

## 使用场景 · Use cases

- 希望 Agent 在跨项目、跨平台（Trae / Codex / Claude Code / Cursor / CLI 等）行为一致。Consistent agent behavior across projects and platforms.
- 希望按风险给自主权：L1 常规直接做，L3 高风险（密钥、删除、迁移、发布）一律先问。Risk-based autonomy: L1 done directly, L3 always asked first.
- 希望「目标模式」无人值守运行：先写计划、设预算、按文件边界拆分、超预算自动停。Unattended goal-mode runs with written plan, budgets, file-boundary isolation, auto-stop.
- 希望会话可审计：验收标准前置、任务记录、会话结束知识沉淀（双写）。Auditable sessions: acceptance criteria up front, task records, post-session knowledge distillation.
- 希望规划同时经工程师与产品双视角审查，而不只是查代码正确性。Planning reviewed from both engineer and product angles, not just code-correctness.
- 希望省 token 不丢纪律：渐进式加载 + L1 快速通道，小任务不烧完整流程。Token-efficient: on-demand loading + fast lane for trivial tasks.

---

## 局限与代价（如实）· Limitations

- **依赖强提示词注入 Strong-prompt-injection dependent**：本质是规范而非工具——无运行时、无强制；注入被跳过或描述未命中时，它什么也不会做。It is a specification, not a tool; if injection is skipped or the description fails to match, it does nothing.
- **依赖 Agent 自律 Agent self-discipline**：无脚本强制执行；懒惰的 Agent 可以不遵守规则，也无法感知自己被压缩——用自检双守卫 + 显式重载顺序缓解。No scripts enforce anything; mitigated by self-check guards + explicit reload sequence.
- **上下文成本 Context cost**：即使渐进式，治理层仍消耗上下文——这是换取一致性的代价；生成的规则文件控制在约 30 行、记忆文件一屏内。A governance layer consumes context — the trade-off for consistency; rule files ~30 lines, memory file ≤1 screen.
- **细则体量大 Detail volume**：落地细则 203 条较多——这正是按类按需加载的原因。203 rules is heavy — hence per-category on-demand loading.
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
├── dist/                           ← 版本发布 zip（v1.0.0 … v1.5.0）
├── skill/shisan-xinuo-workflow/    ← 默认交付（英文）
│   ├── SKILL.md                    ← 精简入口：定位、总纲主流程、门禁、引用地图、重载顺序
│   ├── templates/                  ← 主流程配套模板（规划/验收/任务记录/复盘/回滚点/提示词预算/会话钩子/审查子代理）
│   └── references/                 ← 按需加载的引用
│       ├── rules.md                ← 43 条规则地基
│       ├── workflows.md            ← 前置 0.0-0.4 + 9 类任务 + 门禁 + 记忆文件协议 + 重载顺序
│       ├── details.md              ← 203 条落地细则 / 12 类（踩坑日志）
│       ├── platform-adaptation.md  ← 注入点、提问降级链、结构化协议
│       ├── security.md             ← 安全红线、安装校验、回滚、提示注入、供应链/SBOM、残留扫描
│       └── never-list.md           ← 永不清单（明线禁止，自查用）
└── versions/
    ├── universal-zh/               ← 通用版 · 中文
    └── universal-bilingual/        ← 通用版 · 中英双语
```

---

## 版本历史 · Changelog

- **v1.5.0** — **P0/P1 治理完整度补强**：新增 `templates/`（plan / acceptance / task-record / retrospective / rollback / prompt-budget 模板）+ `templates/hooks/`（session-start 钩子示例）+ `templates/agents/`（critic / risk-reviewer / security-auditor 子代理）+ `references/never-list.md`（永不清单明线）+ security.md 补提示注入防御与供应链/SBOM + README 重写（差异化主张改为「工程治理全家桶完整度第一」、新增参考项目章节）；三版同步。
**EN — v1.5.0** — governance completeness: templates/ (plan/acceptance/task-record/retrospective/rollback/prompt-budget) + hooks/ (session-start) + agents/ (critic/risk-reviewer/security-auditor) + never-list + prompt-injection & supply-chain defenses + README reposition (most-complete package) + reference-projects section; all editions synced.

- **v1.0** — 首版发布（43 条纪律、双模式、回滚、渐进式披露）。
- **v1.1** — 注入点与注入模式（按需 / 强制每会话）。
- **v1.2** — 调研驱动的任务主流程（11 步）。
- **v1.3** — 定位翻转：流程为魂、规则为基；主流程升为唯一入口 + 出口产物门禁；状态澄清前置。
- **v1.3.1** — 联网调研·必须（非降级）+ 最铁铁律（最少代码、绝不自研组件）。
- **v1.3.2** — 联网调研可信信号 + 开源安装强制校验（「开源不等于安全」）。
- **v1.4** — 落地细则（186 条 / 11 类，含开发日志深挖 + 铁律纪律补充）+ 产品完善度诊断 + 强制双调研 + 五支柱定位 + README 重构。
- **v1.4.1** — 文档一致性修复：README 条数校准（173→186 / 10 类→11 类）、英文版 details.md 类别编号重排（缺 4 / 重复 9）、四版 SKILL.md 引用地图补全 11 类、决策记录「待推送 / 不推送」状态对齐发布记录、补研究引用链接；新增「双仓同步检查清单」。
- **v1.4.2** — ①**定位诚实话**：不再宣称「不含领域知识」——机制层跨领域，细则层（details.md）如实声明为绑定具体技术栈的**踩坑日志**而非技术教程（修正自第三方审阅意见）；②**L1 快速通道**：第 1 步后先判级，L1 常规任务走「复述→最小修改→最小验证→汇报」快速通道，治「简单任务杀鸡用牛刀」；③**记忆文件协议**：外部化长期记忆（`memory/` 状态文件，压缩 / 重置后先读再继续），治「上下文稀释」。
- **v1.4.3** — ①**定位升级为「渐进式」**：把「按需加载 + 判级动态路由 + 快速通道」明确为核心定位（不再是静态提示词）；②**压缩后显式重载顺序**：用户说「重载 / 你被压缩了」或平台重置 → ①重读 SKILL.md → ②重读 memory/ → ③重读当前引用 → ④向用户复述任务与验收再继续（写进四版 SKILL.md 与 workflows.md）；③README 重构：一句话定位 / 架构真相 / 差异化完善 / FAQ 补充（省 token）。
- **v1.4.4** — ①**安静模式**：关键词 `安静模式`/`quiet`——L1 任务只汇报结果，降视觉噪音与 Token 焦虑（应对"决策疲劳 / 视觉噪音"）；②**偏好记忆**：用户确认的技术栈/语言/风格写入 `memory/`「用户偏好」字段，同类决策直接采用不再重复问（应对"强制询问疲劳 / 无用户画像"）；③**原子操作锁**：L3 破坏性操作先输出待执行命令清单、结束回合等用户确认再执行，最后一道闸门交给人类（应对"43 条纪律纯靠自觉"）；四版同步，私有仓试点本机偏好文件。
- **v1.4.5** — **细则扩展至 203 条 / 12 类**：对作者 863KB 开发日志 + 踩坑库 / AI 知识沉淀 / 交接清单 / 规则文档进行分片审查提炼，与既有 186 条去重后精选 **17 条新增**（编号 187-203，第 12 类「源项目深挖补充」）：Windows 保留端口段 / schannel 吊销、MCP 配置不热加载、动效仅 transform+opacity、SPA ref 失效、0/1 基口径、加载态落交互点、WCAG 对比度实测、Prisma where 非空但 TS 可空、复合唯一键 null 哨兵、限流死配置核对、202+轮询约定、进程内定时任务兜底、部署抽样断言静态资源、一次性令牌 remote 还原、推理模型 max_tokens≥512、LLM HTTP200 空内容按失败。

**EN — v1.4.1** — documentation-consistency fixes: README numbers calibrated (173→186 / 10→11 categories), English details.md category numbering fixed (missing 4 / duplicate 9), all four SKILL.md reference maps expanded to 11 categories, decision-record push-status aligned with release records, research citations added; plus a two-repo sync checklist.
**EN — v1.4.2** — ① honest positioning: mechanisms are framework-agnostic, but the details layer is now honestly declared a stack-bound **pitfall log**, not a tutorial; ② **L1 fast path** (triage-first, fixes over-governance on trivial tasks); ③ **memory-file protocol** (externalized long-term memory — write at milestones, read first after compaction, fixes context dilution).
**EN — v1.4.3** — ① positioned as **progressive / on-demand / triage-routed** (not a static prompt); ② **explicit reload sequence after compaction** (re-read SKILL.md → memory file → references → restate task + acceptance) written into all editions; ③ README rebuilt: one-line positioning / architecture truths / sharpened differentiation / expanded FAQ (token-cheap).
**EN — v1.4.4** — ① **quiet mode** (`安静模式`/`quiet`): L1 reports only results, cutting visual noise & token anxiety; ② **preference memory**: confirmed tech-stack/language/style choices stored in `memory/` and reused instead of re-asking; ③ **atomic-operation lock**: L3 destructive ops output the command list and wait for human confirmation — the final gate is human, not agent self-discipline. All editions synced; personal edition pilots a machine-local preference file.
**EN — v1.4.5** — details expanded to **203 rules / 12 categories**: review of the 863KB dev log + pitfall/knowledge libraries yielded 17 new rules (187-203) after dedup — Windows reserved ports / schannel revoke, MCP config not hot-reloaded, animate only transform+opacity, SPA ref invalidation, 0/1-based index mismatches, loading state at the interaction point, measured WCAG contrast, Prisma where-nonnull-but-TS-nullable, nullable composite-unique sentinel, dead rate-limit config, 202+poll convention, in-process job fallback, sample-assert static resources, restore token-less remote, reasoning max_tokens≥512, HTTP-200-empty as failure.

---

## 与其他规范的关系 · Relationship to standards

- [Agent Skills / agentskills.io](https://agentskills.io/)：遵循开放标准（文件夹 + `SKILL.md` + 渐进式披露），兼容所有支持 Skills 的客户端。规范由 Anthropic 发起、开放治理，30+ 客户端支持（Claude / Codex / Cursor / Gemini CLI / GitHub Copilot 等）。Follows the open standard (folder + `SKILL.md` + progressive disclosure); runs on any skills-compatible client.
- [Agent Skills 最佳实践](https://agentskills.io/skill-creation/best-practices)：渐进式披露、Gotchas、Checklist、Plan-Validate-Execute——机制层按此重写。Mechanics rewritten against the official best practices.
- [AGENTS.md](https://agents.md/)：第 0 步生成的就是这类跨平台规则文件（精简版），完整工作流保留在 Skill 内按需加载。规范由 Linux 基金会 Agentic AI Foundation（AAIF）托管，60,000+ 开源项目采用。Step 0 generates this kind of cross-platform rule file in condensed form.

## 参考项目 · Reference projects

> 按实际情况如实登记：本 Skill 的机制 / 结构 / 细节借鉴自以下**协议与同类项目**（借鉴机制与结构，非复制代码）。同类项目独立演进，本 Skill 为后发者，差异定位见「差异化优势」。All mechanisms/structures/detail layers borrow from the protocols and peer projects below — mechanism borrowing, not code copying; this skill is a later entrant.

### 协议与规范（必列）· Protocols & standards

| 参考 Reference | 链接 Link | 借鉴内容 Borrowed |
|---|---|---|
| Agent Skills 规范 Specification | [agentskills.io/specification](https://agentskills.io/specification) | `SKILL.md` 结构、渐进式披露、name+description 激活机制 |
| Agent Skills 最佳实践 Best practices | [agentskills.io/skill-creation/best-practices](https://agentskills.io/skill-creation/best-practices) | Gotchas、Checklist、Plan-Validate-Execute、上下文纪律 |
| AGENTS.md 规范 | [agents.md](https://agents.md/) | 第 0 步生成的跨平台规则文件格式（精简 + 回指） |

### 同类工程治理项目（机制借鉴）· Peer governance projects (mechanism borrowing)

| 参考项目 Project | 链接 Link | 借鉴内容 Borrowed |
|---|---|---|
| screenleon/agent-playbook-template | [github.com/screenleon/agent-playbook-template](https://github.com/screenleon/agent-playbook-template) | prompt-budget 预算管理、critic / risk-reviewer 子代理、harness 门禁思路 |
| vignesh2027/AI-AGENT-SKILLS | [github.com/vignesh2027/AI-AGENT-SKILLS](https://github.com/vignesh2027/AI-AGENT-SKILLS) | session-start 会话启动钩子 |
| peva3/anchor | [github.com/peva3/anchor](https://github.com/peva3/anchor) | NEVER list 明线结构、提示注入防御、供应链 / SBOM 专项 |
| buildbetter-app/skills | [github.com/buildbetter-app/skills](https://github.com/buildbetter-app/skills) | 模板体系（spec / plan / tasks / checklist） |
| Eriemon/agents-md-generator | [github.com/Eriemon/agents-md-generator](https://github.com/Eriemon/agents-md-generator) | 多平台规则文件（AGENTS.md / CLAUDE.md / GEMINI.md） |

### 早期审阅参考（v1.4.0 记入项目信息决策 16）· Earlier review references

- **engineering-policies**（token / context-rot / 停止规则）
- **nadvolod AGENTS.md**（风险分级证据 / 人为审查边界）
- **ponytail**（七级决策阶梯 / 删除优于添加）
- **软件开发准则**（DRY / KISS / YAGNI / SoC / LoD）→ 进入 details.md 铁律与纪律类

---

## 常见问题 · FAQ

- **为什么不做成一个大规则文件？** 上下文纪律：只预加载 `name`+`description`，激活才读正文，`references/` 按步加载。Why not one big rule file? Context discipline: only name+description preload; references load per step.
- **会覆盖我已有的规则吗？** 不会——先备份再合并，绝不覆盖。Will it overwrite my rules? No — backup + merge only.
- **会对外发送数据吗？** 不会。纯文档、无脚本、无网络。Does it send data anywhere? No. Pure documentation; no scripts; no network.
- **Agent 能感知自己被压缩吗？** 不能——这正是 Skill 用「显式信号重载 + 关键节点自检」的原因。Can the agent detect compaction? No — hence the explicit-signal reload + milestone self-checks.
- **上下文压缩后怎么重载？** 用户说「重载 / 你被压缩了 / 从头加载」或平台重置 → ①重读 SKILL.md → ②重读 memory/ → ③重读当前引用 → ④向用户复述任务与验收再继续。How to reload after compaction? Follow the reload sequence: SKILL.md → memory file → references → restate task + acceptance.
- **联网调研就是「网上说什么信什么」吗？** 不是——它按权威性分级收集可验证可信信号，并以本地实测兜底。Is the survey just "whatever the web says"? No — verifiable trust signals with a defined authority hierarchy, local verification as the final judge.
- **细则层为什么含具体技术栈？** 如实说明：details.md 是真实项目踩坑日志（什么会错），不是技术教程（怎么用）；机制层与框架无关。Why stack-bound details? Honest: they are a pitfall log, not a tutorial; the mechanism layer is framework-agnostic.

---

## 来源与依据 · Where it comes from

**数据口径（v1.4.5 实测）**——本 Skill 的 203 条落地细则 / 12 类，提炼自作者真实生产开发沉淀；源文档存放于独立工作项目目录，**不随本公开仓 / zip / npm 分发**，此处给出可核实的实测数据：

| 源文档（工作项目目录） | 实测大小 | 内容 |
|---|---|---|
| `开发日志与经验记录.md` | **863.6 KB / ≈50.1 万字符 / 8,299 行** | "800KB+ 开发历史"的实证来源，真实踩坑主库 |
| `会话交接与待办清单.md` | 209.2 KB / ≈11.6 万字符 / 786 行 | 多会话交接与待办沉淀 |
| `AI会话知识沉淀.md` | 70.3 KB / ≈3.6 万字符 / 426 行 | 会话知识双写沉淀 |
| `踩坑经验库.md` | 59.8 KB / ≈3.6 万字符 / 323 行 | 踩坑条目库 |
| `AGENTS.md` / `TRAE.md` / `README-工作区导航.md` 等 | — | 工作区规则文档（去敏提炼增量） |

提炼方式：分片子代理审查（v1.4.5 覆盖开发日志 / 踩坑库 / AI 知识沉淀 / 交接清单 / 规则文档）→ 与既有 186 条去重 → 精选 17 条 → 泛化脱敏 → 形成 `details.md` 203 条 / 12 类 + 个人经验手册。

**踩坑记录涵盖（11 类示例）**：PowerShell / Windows 终端 ｜ 前端 Next.js / React 环境 ｜ Prisma / PostgreSQL ｜ 测试与质量门禁 ｜ 视觉 MCP / 截图 ｜ 浏览器自动化 / E2E（Playwright）｜ Git 与提交 ｜ MCP 与工具链 ｜ API 契约与前后端联动 ｜ 监控 / 运维 / 压测 / 证书 ｜ 长会话与协作纪律。机制部分按 [Agent Skills 开放规范](https://agentskills.io/)及其[最佳实践](https://agentskills.io/skill-creation/best-practices)重写（渐进式披露、Gotchas、Checklist、Plan-Validate-Execute）。

**EN** — 203 landing details in 12 categories are distilled from real production work (source docs live in a separate working-directory, not shipped here). Measured facts: the main dev-log is **863.6 KB / ~501K chars / 8,299 lines** (the basis of the "800KB+ development history" claim), plus a 209 KB session-handover log, 70 KB knowledge distillations and a 60 KB pitfall library; mechanics rewritten against the [Agent Skills specification](https://agentskills.io/) and its [best practices](https://agentskills.io/skill-creation/best-practices).

---

## 贡献者与许可 · Contributors & License

- **十三希诺** — 作者与维护者 Author & maintainer（[zxc663](https://github.com/zxc663)）
- 欢迎贡献：规则改进、工作流补充、本地化修正请开 issue 或 PR；新增规则需先走 Skill 自带的规则新增流程再合并。Contributions welcome via issue or PR; new rules follow the skill's own rule-addition process before merging.
- **许可 License**：MIT，见 [LICENSE](LICENSE)。
