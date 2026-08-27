# Shisan Xinuo Agent Workflow · 十三希诺 Agent 工作流

> **渐进式工程治理 Skill——不是把整本手册砸进上下文，而是像神经系统：只在任务到达某一步骤时，注入那一步所需的少量规则。**
> A progressive, on-demand engineering-governance Skill for AI coding agents: it injects only the few rules a step needs, when that step arrives.

![version](https://img.shields.io/badge/version-1.9.0-blue) ![license](https://img.shields.io/badge/license-MIT-green) ![platforms](https://img.shields.io/badge/platforms-Codex%20%7C%20Claude%20Code%20%7C%20Cursor%20%7C%20Trae%20%7C%20Windsurf-orange)

---

## 一句话定位 · One-line positioning

一个**渐进式披露 + 按需注入 + 判级动态路由**的工程治理元 Skill：把 **47 条纪律规则 + 11 步强制主流程（每步出口产物门禁）+ 203 条落地细则（12 类）+ 配套模板 / 提示词预算 / 会话钩子 / 审查子代理 / 永不清单**，打包成跨平台（Trae / Codex / Claude Code / Cursor / Windsurf / WorkBuddy / CLI）可审计的治理层。价值：**治理一致性、可审计性、防假实现**；代价：依赖平台注入与 Agent 自律，无运行时强制。

A progressive, on-demand, triage-routed governance meta-skill: **47 discipline rules + an 11-step mandatory master sequence (per-step exit-artifact gates) + 203 landing details (12 categories) + templates / prompt budget / session hooks / review sub-agents / NEVER list**, packaged into a cross-platform, auditable governance layer. Value: consistency, auditability, no-fake-completions; cost: injection-dependent, zero runtime enforcement.

---

## 目录 · Contents

1. [为什么用它 · Why](#为什么用它--why-this)
2. [它为谁解决什么 · Who it's for](#它为谁解决什么--who-its-for)
3. [工作原理（渐进式 / 状态机）· How it works](#工作原理渐进式--状态机--how-it-works)
4. [功能全景 · Feature map](#功能全景--feature-map)
5. [差异化优势 · Differentiation](#差异化优势--differentiation)
6. [架构真相（诚实）· Architecture truths](#架构真相诚实--architecture-truths)
7. [快速体验 · Quick start](#快速体验--quick-start)
8. [安装 · Install](#安装--install)
9. [仓库结构 · Repository layout](#仓库结构--repository-layout)
10. [版本差异（三语）· Editions](#版本差异三语--editions)
11. [参考项目 · Reference projects](#参考项目--reference-projects)
12. [局限与代价 · Limitations](#局限与代价--limitations)
13. [常见问题 · FAQ](#常见问题--faq)
14. [来源与依据 · Sources](#来源与依据--sources)
15. [版本历史 · Changelog](#版本历史--changelog)
16. [贡献者与许可 · Contributors & License](#贡献者与许可--contributors--license)

---

## 为什么用它 · Why this

- **把「AI 直觉」变成「工程纪律」**：L1/L2/L3 风险分级、关键必问、回滚点、留档纪律——不再靠 Agent 自觉碰运气。Turns AI instinct into auditable engineering discipline.
- **省 token 不丢纪律**：渐进式加载 + L1 快速通道——小任务不烧完整流程，大任务不破底线。Saves tokens without losing discipline: on-demand loading + L1 fast lane.
- **跨平台行为一致**：同一套治理任何平台生效，第 0 步自动适配，无需逐平台重写。Consistent behavior across platforms; Step 0 adapts instead of rewriting.

## 它为谁解决什么 · Who it's for

- **重度 AI 编码用户**（Cursor / Claude Code / Trae / Codex 深度用户）：希望 Agent 跨项目、跨平台行为一致、可审计，尤其痛恨「假完成 / 伪造测试 / 虚报数据」。Heavy AI-coding users who want consistent, auditable, no-fake-completion behavior.
- **需要按风险放权的人**：L1 常规直接做，L3 高风险（密钥、删除、迁移、发布）一律先问。Risk-based autonomy: L1 done directly, L3 always asked first.
- **想要无人值守目标模式的人**：`目标：…` → 写计划、设预算、按文件边界拆分、超预算自动停。Unattended goal mode: plan, budgets, file-boundary isolation, auto-stop.
- **想省 token 又不丢纪律的人**：渐进式加载 + L1 快速通道。Token-efficient without losing discipline.
- **做 Agent 生态研究 / 开源设计的人**：了解「渐进式 Skill」如何把静态约束变成动态治理。Researchers designing progressive governance skills.

---

## 工作原理（渐进式 / 状态机）· How it works

```
平台硬加载（第 0 步：检测平台 → 定位该平台真实注入点 → 按需 / 强制注入核心）
Platform hard-load (Step 0: detect → locate the REAL injection point → on-demand / forced core injection)
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
      └─ 规则（47 条，地基）Rules + 落地细则（203 条 / 12 类，按类按需加载）Details
```

**渐进式（Progressive）体现在三层**：
1. **入口精简**：平台只预加载 `name` + `description`（约几 KB）；激活才读 SKILL.md 正文（<500 行）。
2. **按步加载**：`references/` 只在对应步骤需要时才读——`rules.md`（地基）、`details.md`（按类按需）、`workflows.md`、`security.md`、`platform-adaptation.md`、`never-list.md`、`skill-usage.md`。
3. **动态路由**：任务判级前置 → L1 走快速通道（省上下文），L2/L3 走完整主流程（兜底线）；触发式诊断（反复审查 → 产品完善度诊断）。

**上下文纪律**：`SKILL.md` 精简；生成的规则文件约 30 行；记忆文件（`memory/`）一屏内；压缩后先读记忆再继续。

---

## 功能全景 · Feature map

| 能力 Capability | 说明 Description | 入口 Entry |
|---|---|---|
| 第 0 步平台检测与硬加载 | 检测平台 → 定位真实注入点 → 按需（9 行精简）/ 强制（`injection-core.md` 核心全文硬加载）双模式 | `SKILL.md` §3 / `references/injection-core.md` / `platform-adaptation.md` |
| 强制总纲主流程（11 步）| 每步出口产物门禁，可检查、可审计、不可跳步 | `SKILL.md` §2 / `references/workflows.md` |
| L1 快速通道 + 判级速查 | 判级先行（L3 封闭清单 6 项，10 秒定论，判不了默认 L2）；L1 走「复述→最小修改→最小验证→汇报」 | `SKILL.md` §2.3 / §5 |
| 47 条规则地基 | 工作纪律 / 思考 / 执行 / 协作 / 安全 / 交付 / 回滚 | `references/rules.md` |
| 203 条落地细则（12 类）| 环境 / 前端 / 数据库 / 测试 / API / 运维 / 代码质量 / Git / 会话 / 深挖 / 铁律 / 源项目深挖 | `references/details.md` |
| 永不清单 | 7 类明线禁止项（假完成 / 密钥 / 跳步 / Git / 复用 / 提问 / 提示注入）一页自查 | `references/never-list.md` |
| 记忆文件协议 + 压缩重载 | 外部化长期记忆，压缩/重置后先读再继续 | `SKILL.md` §10 / `workflows.md` |
| 关键必问 + 原子操作锁 | L3 先问；破坏性操作先出命令清单等确认 | `SKILL.md` §4 / §7 |
| 双视角（工程师 + 产品）| 规划前强制双调研；反复审查先做产品完善度诊断 | `workflows.md` §0.3-0.4 |
| 可信联网调研 + 安装强制校验 | 可信信号分级；「开源 ≠ 安全」强制校验 | `workflows.md` §0.2 / `security.md` §1.5 |
| 提示注入防御 + 供应链/SBOM | 信任边界、指令层级、依赖校验、扫描、SBOM | `security.md` §6-7 |
| 双模式（普通 / 目标）+ 安静模式 | 关键必问 vs 无人值守；L1 只汇报结果 | `SKILL.md` §5 |
| 配套模板 | 规划 / 验收 / 任务记录 / 复盘 / 回滚点 / 提示词预算 6 类模板 | `templates/` |
| 会话启动钩子 | 平台支持时自动打印纪律横幅（配置示例） | `templates/hooks/` |
| 审查 / 风险 / 安全子代理 | critic / risk-reviewer / security-auditor 子代理模板 | `templates/agents/` |

---

## 差异化优势 · Differentiation

| 对比对象 Compare with | 本 Skill This skill |
|---|---|
| 手写 `AGENTS.md` / `CLAUDE.md` | 渐进式披露、完整引用体系、跨平台适配——不止一页规则，且不拖累每个会话。Progressive disclosure, full reference body, cross-platform adaptation. |
| 平台内置规则 Platform built-in rules | 平台无关：同一纪律任何平台生效；第 0 步自动适配。Platform-independent; Step 0 adapts. |
| 通用系统提示词 Generic prompts | 可操作、可验证、清单驱动：分级表、出口产物门禁、扫描清单。Operational, verifiable, checklist-driven. |
| 静态规则包 / 单文件提示词 | 本 Skill 是**渐进式**：按步加载 + 判级动态路由（L1 快速通道），不是一次全量注入。Progressive, triage-routed — not a one-shot static dump. |
| 其他工作流 / 提示词类 Skill | 多数只有规则或流程；本 Skill 同时具备**强制流程骨架 + 每步门禁 + 判级路由 + 双视角 + 可信调研 + 安装校验 + 记忆协议 + 压缩重载**。Most ship rules or a process; this one adds gates, routing, dual views, verifiable survey, vetting, memory/reload. |
| 官方技能仓库 / 同类治理 Skill | **工程治理全家桶完整度第一**：规则 + 门禁流程 + 落地细则 + 跨平台注入 + 双视角 + 记忆/重载 + 模板 / 预算 / 钩子 / 审查子代理 / 永不清单，一套完整闭环。The most complete governance package — rules, gated process, landing details, injection, dual views, memory/reload, templates, budget, hooks, sub-agents, NEVER list in one. |

---

## 架构真相（诚实）· Architecture truths

> 供人（和 AI）快速判断它到底是什么、做不到什么。**全无脚本 / 无运行时 / 无网络调用**——它是一份规范，不是工具。A specification, not a tool.

| 真相 Truth | 说明 Detail |
|---|---|
| 本质是「强提示词注入」 | 无脚本、无运行时、无强制；靠注入 + Agent 自觉。It is a specification, not a tool. |
| 记忆靠「外部化文件」 | Agent 无长期记忆、无法感知压缩——用 `memory/` + 显式重载顺序 + 关键节点自检兜底。 |
| 细则层绑技术栈 | `details.md` 含真实项目踩坑（Next.js / Prisma / Playwright 等）——**踩坑日志**不是**技术教程**。 |
| 不提供「硬门禁」 | 强制依赖平台（hooks / CI / 沙箱）——本 Skill 不捆绑工具；缺口用「兜底」。 |
| 定位是「治理层」 | 不替代领域知识、不替代项目自身文档——冲突时项目文档优先。 |

---

## 快速体验 · Quick start

**一分钟跑通**（需要支持 Skill 的 Agent 环境：Claude Code / Trae / Cursor / Codex 等）· **Try it in under a minute** (needs a skills-capable agent):

1. **安装 Install**：把 `skill/shisan-xinuo-workflow/` 复制到平台技能目录（见下方安装）；或从 `dist/` 解压发布 zip。
2. **加载 Load**：新开会话。Skill 自动执行**第 0 步平台检测与注入**：检测平台 → 定位该平台**真实注入点**（Trae `~/.trae-cn/user_rules/`、Claude Code `CLAUDE.md`、Codex `AGENTS.md`、Cursor `.cursor/rules/`、Windsurf `.windsurfrules`）→ 询问**按需 / 强制注入**。选**按需**：写入约 9 行精简纪律 + 回指本 Skill；选**强制（硬加载）**：把 `references/injection-core.md` 核心全文（判级速查 + 11 步主流程 + 设计铁律 + 双模式 + 红线，约 55 行）写入注入点——此后每会话无条件生效，**不再依赖模型自觉加载本 Skill**（已有规则先备份再合并，绝不覆盖）。
3. **感受它 Feel it**：给一个小任务观察——先复述理解、写 3-5 条验收标准、做完自查。给**风险任务**（如「把这个目录删了」）：必须**先问再动手**——这就是 L3 分级。
4. **目标模式 Goal mode**：说 `目标：整理本目录文件并归组，注意不要删除任何内容`，观察它写计划、设预算、按文件边界拆分、超预算自动停。

一个会话内应看到：任务分级、关键必问、风险操作前回滚点、结束时留档。Expected within one session: triage, ask-before-acting, rollback before risky ops, records at the end.

---

## 安装 · Install

把 skill 目录复制到所用平台的技能目录；纯文档、零依赖、零网络调用，加载即自动适配平台。Copy the skill folder into your platform's skills directory; pure documentation, zero deps, zero network — loading is enough, Step 0 adapts it.

| 平台 Platform | 位置 Location |
|---|---|
| **开放式技能生态（skills.sh）** | `npx skills add zxc663/shisan-xinuo-workflow --skill shisan-xinuo-workflow`（英文规范入口；中文版用 `--skill shisan-xinuo-workflow-zh`，双语版用 `--skill shisan-xinuo-workflow-bilingual`） |
| Claude Code | `~/.claude/skills/shisan-xinuo-workflow/` |
| Codex / 通用环境 | 克隆本仓库，将技能发现指向 `skill/shisan-xinuo-workflow/`；或解压 `dist/` 发布 zip |
| Trae / Cursor / 其他 | 按平台技能目录约定放置；`Trae` 需在应用设置启用项目规则 |
| npm（GitHub Packages） | `npm install @zxc663/shisan-xinuo-workflow` 后从 `node_modules/` 复制 skill 目录 |

> 已收录于 [skills.sh](https://skills.sh/) 开放式 Agent 技能生态：公开仓库 `zxc663/shisan-xinuo-workflow` 一经 `npx skills add` 安装即通过安装遥测自动计入 skills.sh 排行榜，三个通用语言版（en / zh / bilingual）按名称独立收录。

---

## 仓库结构 · Repository layout

```
shisan-xinuo-workflow/              ← 仓库根
├── README.md                       ← 本文件（双语 · 中文优先，门面）
├── LICENSE                         ← MIT
├── 项目信息.md                      ← 内部维护文档（供下一个 AI 助手读写）
├── package.json / .npmrc           ← npm 发行物配置（GitHub Packages）
├── dist/                           ← 版本发布 zip（v1.0.0 … v1.7.0）
├── skill/shisan-xinuo-workflow/    ← 默认交付（英文）
│   ├── SKILL.md                    ← 精简入口：定位、总纲主流程、门禁、引用地图、重载顺序
│   ├── templates/                  ← 配套模板（规划/验收/任务记录/复盘/回滚点/提示词预算/会话钩子/审查子代理）
│   └── references/                 ← 按需加载的引用
│       ├── injection-core.md       ← 硬加载核心模板（强制注入时全文写入平台注入点）
│       ├── rules.md                ← 47 条规则地基
│       ├── workflows.md            ← 前置 0.0-0.4 + 9 类任务 + 门禁 + 记忆文件协议 + 重载顺序
│       ├── details.md              ← 203 条落地细则 / 12 类（踩坑日志）
│       ├── platform-adaptation.md  ← 注入点、提问降级链、结构化协议、会话钩子协议
│       ├── security.md             ← 安全红线、安装校验、回滚、提示注入、供应链/SBOM、残留扫描
│       ├── never-list.md           ← 永不清单（明线禁止，自查用）
│       └── skill-usage.md          ← Skill 使用：能力发现/注册、加载决策路由、渐进 vs 完整读取
└── versions/
    ├── universal-zh/               ← 通用版 · 中文
    └── universal-bilingual/        ← 通用版 · 中英双语
```
---

## 版本差异（三语）· Editions

三个通用版本**内容完全一致**，仅语言不同；另有独立私有工作台版（不进本公开仓）。The three universal editions are content-identical, differing only in language; a private personal-workstation edition is maintained separately and is **not** part of this public repo.

| 版本 Edition | 路径 Path | 内容语言 Content language | 回答语言 Reply language |
|---|---|---|---|
| 英文 English | `skill/shisan-xinuo-workflow/` | 英文（标题保留品牌名「十三希诺」）| 跟随用户——无强制中文 |
| 中文 中文 | `versions/universal-zh/` | 中文 | 跟随用户；文档与记录按项目约定 |
| 双语 Bilingual | `versions/universal-bilingual/` | 段落级中英对照 | 跟随用户 |
| 工作台版（私有）Personal (private) | 独立私有仓 | 中英混合 + 内嵌个人经验手册 | 统一中文 |

---

## 参考项目 · Reference projects

> 按实际情况如实登记：本 Skill 的机制 / 结构 / 细节借鉴自以下**协议与同类项目**（借鉴机制与结构，非复制代码）。同类项目独立演进，本 Skill 为后发者，差异定位见「差异化优势」。Mechanism borrowing, not code copying; this skill is a later entrant.

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

## 局限与代价（如实）· Limitations

- **依赖强提示词注入 Strong-prompt-injection dependent**：本质是规范而非工具——无运行时、无强制；注入被跳过或描述未命中时，它什么也不会做。It is a specification, not a tool; if injection is skipped or the description fails to match, it does nothing.
- **依赖 Agent 自律 Agent self-discipline**：无脚本强制执行；懒惰的 Agent 可以不遵守规则，也无法感知自己被压缩——用自检双守卫 + 显式重载顺序缓解。No scripts enforce anything; mitigated by self-check guards + explicit reload sequence.
- **上下文成本 Context cost**：即使渐进式，治理层仍消耗上下文——这是换取一致性的代价；规则文件约 30 行、记忆文件一屏内。A governance layer consumes context — the trade-off for consistency.
- **细则体量大 Detail volume**：落地细则 203 条较多——这正是按类按需加载的原因。203 rules is heavy — hence per-category on-demand loading.
- **平台检测是启发式 Detection heuristics**：靠目录 / 环境变量信号判断；无法确定时直接问用户，不猜。Best-effort; asks rather than guesses when ambiguous.
- **不捆绑工具 Zero tooling bundled**：刻意零脚本 / 零依赖 / 零网络；能力缺口用「兜底」解决。Deliberately zero scripts / dependencies / network; gaps handled by fallbacks.
- **规范演进 Spec evolution**：基于 Agent Skills 开放标准构建；不支持 Skill 的旧平台需手动加载。Built on the Agent Skills open standard; older platforms need manual loading.

---

## 常见问题 · FAQ

- **为什么不做成一个大规则文件？** 上下文纪律：只预加载 `name`+`description`，激活才读正文，`references/` 按步加载。Why not one big rule file? Context discipline: only name+description preload; references load per step.
- **会覆盖我已有的规则吗？** 不会——先备份再合并，绝不覆盖。Will it overwrite my rules? No — backup + merge only.
- **会对外发送数据吗？** 不会。纯文档、无脚本、无网络。Does it send data anywhere? No. Pure documentation; no scripts; no network.
- **Agent 能感知自己被压缩吗？** 不能——这正是 Skill 用「显式信号重载 + 关键节点自检」的原因。Can the agent detect compaction? No — hence explicit-signal reload + milestone self-checks.
- **上下文压缩后怎么重载？** 用户说「重载 / 你被压缩了 / 从头加载」或平台重置 → ①重读 SKILL.md → ②重读 memory/ → ③重读当前引用 → ④向用户复述任务与验收再继续。How to reload after compaction? Follow the reload sequence.
- **联网调研就是「网上说什么信什么」吗？** 不是——它按权威性分级收集可验证可信信号，并以本地实测兜底。Is the survey just "whatever the web says"? No — verifiable trust signals + local verification.
- **细则层为什么含具体技术栈？** 如实说明：details.md 是真实项目踩坑日志（什么会错），不是技术教程（怎么用）；机制层与框架无关。Honest: it is a pitfall log, not a tutorial; the mechanism layer is framework-agnostic.

---

## 来源与依据 · Sources

**数据口径（实测）**——本 Skill 的 203 条落地细则 / 12 类，提炼自作者真实生产开发沉淀；源文档存放于独立工作项目目录，**不随本公开仓 / zip / npm 分发**，此处给出可核实的实测数据：

| 源文档（工作项目目录） | 实测大小 | 内容 |
|---|---|---|
| `开发日志与经验记录.md` | **863.6 KB / ≈50.1 万字符 / 8,299 行** | "800KB+ 开发历史"的实证来源，真实踩坑主库 |
| `会话交接与待办清单.md` | 209.2 KB / ≈11.6 万字符 / 786 行 | 多会话交接与待办沉淀 |
| `AI会话知识沉淀.md` | 70.3 KB / ≈3.6 万字符 / 426 行 | 会话知识双写沉淀 |
| `踩坑经验库.md` | 59.8 KB / ≈3.6 万字符 / 323 行 | 踩坑条目库 |
| `AGENTS.md` / `TRAE.md` / `README-工作区导航.md` 等 | — | 工作区规则文档（去敏提炼增量） |

提炼方式：分片子代理审查（覆盖开发日志 / 踩坑库 / AI 知识沉淀 / 交接清单 / 规则文档）→ 去重 → 泛化脱敏 → 形成 `details.md` 203 条 / 12 类 + 个人经验手册。机制部分按 [Agent Skills 开放规范](https://agentskills.io/)及其[最佳实践](https://agentskills.io/skill-creation/best-practices)重写（渐进式披露、Gotchas、Checklist、Plan-Validate-Execute）。

**EN** — 203 landing details in 12 categories are distilled from real production work (source docs live in a separate working-directory, not shipped here). The main dev-log is **863.6 KB / ~501K chars / 8,299 lines** (the basis of the "800KB+ development history" claim); mechanics rewritten against the [Agent Skills specification](https://agentskills.io/) and its [best practices](https://agentskills.io/skill-creation/best-practices).

---

## 版本历史 · Changelog

- **v1.9.0** — **推广先导 + 元数据规范化**：SKILL.md frontmatter 规范化（顶层 `version`/`tags` 迁入 `metadata.*`，符合 Agent Skills 标准可移植字段，`metadata.tags` 供 [skills.sh](https://skills.sh/) 按分类收录）；README「安装」新增**开放式技能生态（skills.sh）一键安装入口**（`npx skills add zxc663/shisan-xinuo-workflow --skill shisan-xinuo-workflow`，中文版 `--skill shisan-xinuo-workflow-zh`、双语版 `--skill shisan-xinuo-workflow-bilingual`）；`.gitignore` 增加 `versions/personal-zh/` 与 `memory/` 防护，杜绝个人版被技能市场扫描收录。Promo-first release: frontmatter metadata spec-normalization, skills.sh one-click install entry, personal-edition leak guard via .gitignore.
- **v1.8.0** — **Skill 使用模块 + 决策审计归档 + 规则扩充至 47 条 + 目标模式窄化**：新增 `references/skill-usage.md`（能力发现/注册机制、加载决策路由、渐进 vs 完整读取分类、Agent 注册维度与 Skill 工具注册校验）；`rules.md` 新增 §44-47（决策分层与审计归档 / 备份纪律·本地优先 / 成本与资源意识 / 注入分层与硬注入提醒）；双模式补决策纪律（普通模式重大决策即时复述留档；目标模式仅 L3/严重阻塞暂停、每里程碑强制留档、本地备份优先不默认 git push）；判级同步链单一权威源（SKILL.md §5.2 → injection-core → 全局注入副本）；注入点「层级」列 + 分层注入规则；安装期「注入模式选择提问」中英双语；规则计数 43→47 全仓校正；双语版按增量注入保留整页排版。Skill-usage module, decision-audit archive, rules to 47, goal-mode narrowing, injection layering, triage sync chain.
- **v1.7.0** — **流程路由地图 + 上下文预算法 + 工作区 memory/ 统一归档 + 偏好写后复核**：injection-core 升级为流程路由地图，写死「先读哪些文件 → 按什么顺序执行 → 结束后更新哪些文档」；**上下文预算法**（常驻小 / 开工读 memory 一屏 / 按需读 references 不预载 / 结束更新最小追加）根治上下文污染；**工作区 `memory/` 统一归档 + 自动建骨架**（state / experience / preferences / task-log，任何会话先扫、缺则自建，唯一覆盖点 `.agent-records/`）+ 新增 `templates/workspace-memory-template.md`（三语）；**偏好写后复核提醒**（写入 `memory/preferences.md` 后主动向用户复核大类方向，偏差由用户修正）；**完成更新序**（task-log → experience → preferences → 提交）；**必问强化 + 判级≠理解确认**（理解不尽确定也必问，问清楚比问少了更重要）。Process routing map, context budget, unified workspace `memory/`, post-write preference review, must-ask reinforcement, triage ≠ understanding.
- **v1.6.0** — **平台无关硬加载核心**：三语新增 `references/injection-core.md`（判级速查 + 11 步主流程 + 设计铁律 + 双模式 + 红线的标准注入模板）；第 0 步升级为「检测平台 → 定位该平台真实注入点 → 写入核心全文」——任何平台首次加载一次即完成硬加载、每会话无条件生效；「每会话读 SKILL.md」弱指令全线降级（实测不可靠）；Trae 注入点实证修正为 `~/.trae-cn/user_rules/*.md`。**判级速查**：L3 封闭清单（仅 6 项）+ 10 秒定论 + 判不了默认 L2，根治琐碎判级 token 内耗。**设计成本铁律**：好的设计是昂贵的，但糟糕
的设计成本更高（按后期改造成本评估）。description 改一句话核心定位。Platform-agnostic hard-load core (injection-core.md ×3), closed-list triage quick reference, design-cost iron law, one-line positioning.
- **v1.5.0** — P0/P1 治理完整度补强：`templates/`（6 模板）+ `templates/hooks/`（会话钩子）+ `templates/agents/`（3 子代理）+ `references/never-list.md`（永不清单）+ security.md 提示注入防御与供应链/SBOM + README 重构（差异化 reposition + 参考项目章节）；三版同步。Governance completeness: templates, hooks, review sub-agents, never-list, security defenses; README rebuilt.
- **v1.4.5** — 细则扩展至 **203 条 / 12 类**（源项目多文档审查提炼，新增第 12 类 17 条）。Details expanded to 203 rules / 12 categories.
- **v1.4.4** — 安静模式（`安静模式`/`quiet`）+ 偏好记忆（memory/ 用户偏好字段）+ 原子操作锁（L3 先出命令清单等确认）。Quiet mode, preference memory, atomic-operation lock.
- **v1.4.3** — 定位升级「渐进式」+ 压缩后显式重载顺序 + README 重构。Positioned as progressive; explicit reload sequence.
- **v1.4.2** — 定位诚实话（机制层跨领域 / 细则层踩坑日志）+ L1 快速通道 + 记忆文件协议。Honest layered positioning; L1 fast path; memory-file protocol.
- **v1.4.0** — 落地细则（186 条 / 11 类）+ 产品完善度诊断 + 强制双调研 + 五支柱定位 + README 重构。Landing details, product-polish diagnosis, dual survey, five-pillar positioning.
- **v1.3.x** — 定位翻转「流程为魂、规则为基」+ 11 步主流程门禁 + 联网调研必须 + 可信依据 + 开源安装强制校验。Positioning flip; gated master sequence; mandatory verified survey.
- **v1.2.0** — 调研驱动的 11 步任务主流程。Research-driven 11-step master sequence.
- **v1.1.0** — 注入点与注入模式（按需 / 强制）。Injection points & modes.
- **v1.0** — 首版发布（43 条纪律、双模式、回滚、渐进式披露）。First release.

---

## 贡献者与许可 · Contributors & License

- **十三希诺** — 作者与维护者 Author & maintainer（[zxc663](https://github.com/zxc663)）
- 欢迎贡献：规则改进、工作流补充、本地化修正请开 issue 或 PR；新增规则需先走 Skill 自带的规则新增流程再合并。Contributions welcome via issue or PR; new rules follow the skill's own rule-addition process.
- **许可 License**：MIT，见 [LICENSE](LICENSE)。