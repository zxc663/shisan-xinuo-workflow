# Skill 使用模块：能力发现 / 加载决策路由 / 渐进与完整读取分类 · Skill Usage: Capability Discovery / Load-Decision Routing / Progressive vs Full Read（中英双语 · Bilingual）

加载时机：任务涉及 Skill 选用、前端 / 设计类任务、本地无 Skill 时如何获取、弱模型 / 上下文受限处理时加载本文件。When to load: when a task involves choosing a Skill, front-end / design work, how to obtain a Skill when none is local, or weak-model / context-constrained handling. 本文件定义「已注册 Skill」的加载使用纪律——创建 / 注册本身属元能力，另见别处。This file defines the load discipline for already-registered Skills — creation / registration themselves are meta-capability, handled elsewhere.
交叉引用 Cross-references：`rules.md` §26/§28/§29/§38、`security.md` 安装校验 install vetting、`platform-adaptation.md` §1/§2。

## 0. Skill 能力来源与发现机制（元能力）· Where Skill capability comes from & how it is discovered (meta-capability)

- **Agent 能用的 Skill 能力，前提是被平台注册进「可用 Skill 清单」**——每会话注入所有可发现 Skill 的 `name + 一句话 description`（即会话上下文的 available skills 列表）。**未被注册 / 注入的 Skill，文件即使存在也无法被 Agent 触发**。An agent can only use a Skill the platform has registered into its "available skills list" — every session it injects all discoverable Skills' `name + one-line description`; a Skill that is not registered / injected cannot be triggered even if its file exists.
- **三层加载模型 Three-layer load model**（平台天然如此 how platforms naturally work）：
  - **L0 注册清单 Registry list**（name+description，平台全量注入、每会话常驻，injected in full every session, resident）——用于**发现与匹配决策**，不触发即不占正文。For discovery & matching decisions; occupies no body context unless triggered.
  - **L1 主文件 Main file**（`SKILL.md`，触发后按需读取）。
  - **L2 `references/`**（按需渐进读取 read progressively on demand）。
- **触发决策链路 Trigger decision chain**：任务 → 扫 L0 清单 → 读多条 description 判定命中 → Skill 工具按 name 触发 → 读 L1 → 渐进 L2。Task → scan the L0 list → judge the hit from descriptions → trigger by name → read L1 → read L2 progressively. **description 质量决定匹配准度与误触发成本 Description quality drives match accuracy and false-trigger cost**（描述精炼 + 含触发词 → 命中准、成本低；反之易误判或被迫整读正文）。**触发 Skill 仅能用注册清单里的「确切 name」**——字母前缀 + 插件态用 `plugin:skill` 全名；测试 / 训练记忆里的 Skill 名一律**不准猜、不准拼**，只能用注入清单中的实名。Trigger a Skill only with the exact name in the registry list — letter prefix + plugin form use the full `plugin:skill` name; names from testing/training memory are never guessed or invented.
- **Execute agent（子代理）注册维度 Registration dimension**：能否用 Skill **取决于执行体自身是否注册了 Skill 工具**，与文件是否存在于磁盘无关。Whether you can use a Skill depends on whether the executing agent itself has a Skill tool registered — unrelated to whether its file exists on disk. 纪律两条 Two disciplines：①**委托任务是 Skill 能力范围的，先核对该子代理已注册 Skill 工具**；未注册则改用带 Skill 的 agent 类型或**留在主会话执行**，不把 Skill 依赖任务委托给无 Skill 的 agent（如 `browser_use` 这类无 Skill 工具的 agent）。When a delegated task falls within a Skill's capability, first verify that sub-agent has a Skill tool registered; if not, switch to an agent that does or run it in the main session — never delegate Skill-dependent work to one without the tool. ②委托后子代理自身也按本模块的加载顺序执行，主会话不在子代理之外重复装载同一 Skill（省 token）。After delegating, the sub-agent follows the same load order; the main session does not re-load the same Skill on top of it. 此为通用纪律，记入 `rules.md` §28。Recorded in `rules.md` §28.
- **平台差异 Platform differences**（承 `platform-adaptation.md` §1/§2）：Trae 经上下文注入可用清单、正文按需；Claude Code 需要 Skill 先注册到 `.claude/skills/` 才能被解析（**文件在 ≠ 能用，依赖平台解析**）；Cursor / Windsurf 等按平台机制。加载纪律须按所论证平台与「是否已注册可发现」适配。Trae injects the list via system reminder and reads the body on demand; Claude Code requires registration under `.claude/skills/` before parsing (**file present ≠ usable; depends on platform parsing**); others follow their own mechanism.
- **注册 vs 使用分离 Registration vs. use separation**：创建 / 注册 / 更新 Skill 属**元能力**（规则类走 `rules.md` §38 六步流程）；本模块只管**「已注册 Skill 的使用加载纪律」**，两者不混。Creating/registering is meta-capability; this module only governs the load discipline for already-registered Skills.
- **弱模型 / 技能库过大的处理 Weak models / oversized libraries**：即便只注入 description，几十个 Skill 的 name+description 全量常驻也可能冲破弱模型上下文 → 弱模型下调小可发现清单（平台层过滤 / 只保核心）、依赖精准 description 避免误触发。Even name+description resident in full can break a weak model's context → shrink the discoverable list and rely on precise descriptions.

## 1. 何时用 / 何时不用 Skill · When to use / when NOT to use a Skill

- **用 Use**：能提升专业能力、任务属 Skill 能力范围（写作 / 分析 / 前端 / 支付 / 文档 / 数据等）。When it raises professional capability and the task falls within the Skill's scope.
- **不用 NOT use**：**弱模型 / 上下文受限时 Weak models / context-constrained**——Skill 全文会冲破上下文限制，改为精简加载或不用，只保留主流程核心（判级 / 红线 / 必问）。The full text blows the context; load it lean or not at all. 不习惯或尚未理解 Skill 使用的用户，先引导其认识 Skill 能提升大模型专业能力，但**弱模型可能不需要 Skill**——强行加载会冲破上下文，需按 §5 判定取舍。A weak model may not need Skills — forcing a load blows the context; judge per §5.

## 2. 本地 Skill 优先，渐进式加载使用 · Local Skills first, progressive loading

- 有本地 / 工作区 Skill → **优先按渐进式加载使用**（先主 SKILL.md → references 按需），**不重复自研**，不重复引入已注册的重复项。Load it progressively (main SKILL.md → references on demand); don't re-hand-roll and don't re-import an already-registered duplicate.

## 3. 本地无 Skill 时的获取流程 · Getting a Skill when none is local

1. **先问用户 Ask the user first**（`platform-adaptation.md` 第 4 节提问降级链 the asking-tool downgrade chain）二选一：是否需要寻找**权威 Skill 源**安装 / 本机是否有**其他 Skill 安装目录**可复用。Ask whether to look for an authoritative Skill source to install, or whether the machine has another Skill-install directory to reuse.
2. **权威源判定 Authoritative-source judgment**：一手源（官方仓库 / registry / skills 生态）> 实证源（stars / 维护 / 采用）> 社区口碑；**安装必走 `security.md` 开源安装强制校验流程（1.5 节 6 步）**。Any install must pass the mandatory open-source install vetting in `security.md`.
3. **本机其他目录复用 Reuse another local directory**：先按能力 / 描述筛选，**确认已在平台注册可发现后再渐进式读取**，不重复引入；未注册则按平台机制登记。Filter by capability/description, read progressively only after confirming it is registered & discoverable; register per the platform if not.

## 4. 渐进式读取 vs 强制完整读取（分类标准）· Progressive vs. forced full read (classification)

- **默认：渐进式读取 Progressive by default**——读 Skill 主文件（SKILL.md / SKILL），references 按当前步骤按需读；不预载全部引用，上下文预算不浪费。Read the main file; read `references/` on demand; never preload all references.
- **强制完整读取（不走渐进式）的 3 类例外 Force full read — 3 exceptions**：
  1. **核心治理 / 工作流类 Skill Core governance / workflow Skills**——流程门禁不可跳（本 Skill 自身即此类）。The process gate cannot be skipped.
  2. **前端 / UI / 设计类 Skill 一律强制完整读取 Front-end / UI / design always force a full read**——**无条件强制完整读，即使上下文充足 / 用户明确无预算限制也不减少**；因设计类依赖完整规范 / 约束，渐进易遗漏组件规范、设计 token、可用性 / 可访问性规则导致产出不合规。Unconditional: not reduced even when context is ample or the user sets no budget limit; design depends on the complete spec.
  3. **用户明确允许无预算限制 The user explicitly allows no budget limit**——直接整读；若属前端类本就已是无条件整读（见 2）。Read in full directly.
- **不需完整读取的 No full read needed**：工具型 / 辅助型 / 按需触发型 Skill → 渐进式。Tool-like / helper / trigger-on-demand Skills are progressive.
- **前端 / UI / 设计类 Skill 示例（仅作类别举例的通用实名 Front-end/UI/design examples, illustrative）**，触发即完整读取其 SKILL.md 与所需 references：`frontend-design` / `frontend-skill` / `html-report` / `html-deck` / `canvas-design` / `web-artifacts-builder` / `shadcn` / `web-design-guidelines` / `theme-factory` / `brand-guidelines` 等。When triggered, read their SKILL.md and needed references in full.

## 5. 弱模型 / 上下文受限处理 · Weak-model / context-constrained handling

- **判定（不做硬阈值，定性）**：模型能力弱，或上下文将耗尽 → **只加载能打动任务的最小核心**，重 Skill 拆成子任务 / 新会话执行。Load only the minimal core that moves the task; split heavy Skills into subtasks / new sessions.
- 决策留痕（reason 记入任务记录）。Log the decision and reason into the task record.

## 6. Skill 描述（description）质量纪律 · Skill description quality discipline

- 描述应**精炼、含明确触发词**，使 Agent 仅凭 description 即可高准度判定命中——降低误触发与整读正文的成本。Concise and carrying clear trigger words, so the agent can judge the hit with high accuracy from the description alone.
- 描述概要与实际能力**不符（夸大 / 过时）是匹配失误与上下文浪费的头号成因 Description mismatch is the #1 cause of match errors**；发现 Skill 说明与实现不符时诚实标注。Honestly flag when docs don't match implementation.

## 7. Skill 与 MCP / 工具的关系（能力边界）· Skill vs. MCP / tools (capability boundary)

- Skill 可能携带 tools / MCP（按平台机制暴露）；触发 Skill 即解锁其工具，使用纪律与分级 / 留痕 / 成本规则一致（`rules.md` §28/§29）。A Skill may carry tools/MCP; triggering it unlocks them, and usage follows the same triage/record/cost rules as tools.
- Skill 能力缺失时按 `security.md` / `workflows.md`「能力缺失降级」降级，不阻塞。When a Skill's capability is missing, follow the capability-loss degradation — degrade, don't block.