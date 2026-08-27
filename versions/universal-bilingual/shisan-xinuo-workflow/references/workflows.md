# 分类型工作流与质量门禁 · Task-Type Workflows & Quality Gates（中英双语 · Bilingual）

加载时机：开始与下列任务类型匹配的工作、或 SKILL.md 引用具体流程时。When to load: when starting work matching one of the task types below, or when SKILL.md cites a workflow. 每个流程都是清单，逐项打勾。Each flow is a checklist — track progress against it.

## 0. 前置与总纲 · Prelude & master（强制流程 mandatory）

> **前置选择 Prelude selector**：0.0 澄清（起点：目标/现状模糊）→ 0.1 总纲（每任务必走）→ 0.2 联网调研（第 4 步细节）→ 0.3 产品完善度诊断（触发式：反复审查/存量不足）→ 0.4 强制双调研（规划前必过）。0.3 与 0.4 互补：0.3 定位存量缺陷，0.4 保证新规划质量。Clarification (start) → master (every task) → survey (step-4 details) → diagnosis (triggered) → dual survey (pre-planning gate).

### 0.0 状态澄清 · Status clarification

**触发词 Triggers**：理不清 / 项目太乱 / 现状不明 / 不知道从哪下手 / 帮我梳理 / 下一步怎么办 / 要不要做 X。can't sort this out / where do I start / what's next / should I do X；或主流程第 1 步发现现状模糊。

- [ ] 1. 共情框定 Empathize & frame：一句话复述处境与卡住的感觉，声明进入澄清对话
- [ ] 2. 首问 First question：从最高杠杆点切入（「最终想要的结果 / 什么在阻挡你」）
- [ ] 3. 逐层深挖 Drill：按回答追问（因果链 3-5 层、约束与假设、障碍转真问题），每轮 1-2 个
- [ ] 4. 抛出线索 Offer leads：给出线索 / 假设请用户验证
- [ ] 5. 收敛结构化 Converge：产出【澄清纪要：目标 / 现状 / 约束 / 卡点】
- [ ] 6. 共同规划 Plan together：结构化行动规划，确认后回主流程第 1 步

### 0.1 强制总纲主流程 · Mandatory master sequence（11 步，出口产物门禁）

每步出口产物见 SKILL.md §2.2；进入下一步前上一步产物必须存在；无法产出的步须在任务记录写明理由。Exit artifacts in SKILL.md §2.2; the previous step's artifact must exist first; record reasons for legitimate skips.

**判级速查 Triage quick reference（10 秒定论，一句话即止，禁止展开论证）**：L3 封闭清单（仅 6 项，清单外一律不是 L3）：密钥/权限｜数据删除｜数据或服务迁移｜对外发布｜架构选型｜超预算破坏性操作；L1 速判：改名、文案、格式、单行修改等可逆小改动直接做；L2：新功能、多文件、跨模块，记录后做；10 秒判不了级默认按 L2 直接推进，判级结论一句话即止、不追问用户、不展开分析。Closed list of 6 for L3 (nothing outside is ever L3); L1 = reversible small changes, just do them; cannot triage in 10s → default L2, one-sentence verdict, no arguing. **判级 ≠ 理解确认 Triage ≠ understanding confirmation**：判级可快、一句话定论，但目标/边界/方向有歧义、理解不尽确定时，普通模式也必问清楚再推进。Triage can be fast, but when goal/boundaries/direction are ambiguous or understanding is not fully certain, normal mode asks to clarify before proceeding.

- [ ] 1. 接收指令 Receive（任务本质一句话 essence）
- [ ] 2. 经验库必读 Experience log first（命中记录 hit record）
- [ ] 3. 调研实际资源 Survey actual resources（现状事实清单 status fact list）
- [ ] 4. 联网调研·必须 Online survey (mandatory)（市面方案调研记录 market solution survey record）
- [ ] 5. 复用调研·铁律 Reuse survey (iron law)（复用结论 reuse conclusion）
- [ ] 6. 复述理解 Restate understanding（用户确认 user confirmation）
- [ ] 7. 疑问必问 Ask on doubt（提问记录 ask record）
- [ ] 8. 产品视角 + 约束 + 分级 + 回滚点 Product-view + triage + rollback（分级 + 回滚点记录）
- [ ] 9. 规划与验收文档 Plan & acceptance doc（规划验收文档）
- [ ] 10. 执行 Execute（执行记录 execution record）
- [ ] 11. 自查与归档 Self-check & archive（验证结果 + 归档 verification + archive）

### 0.2 联网调研·详细查询清单与可信依据 · Online survey — what & how, and trust signals

> 目的：收集**可验证可信信号**，以本地实测兜底。权威分级：一手源（官方文档 / 官方仓库 / spec）> 实证源（stars / 下载量 / 维护 / 被采用）> 社区口碑（评论 / 已知坑）> 榜单热度（仅被发现度参考）。Collect verifiable trust signals; authority tiers: first-hand > empirical > community > listing heat (discoverability only).

**查什么 What to check（逐项 tick each）**：

- [ ] 1. 候选盘点：GitHub 搜索 / registry / awesome 列表，3-5 个候选。Candidate inventory (3-5).
- [ ] 2. 实证信号：stars / forks / 贡献者 / 最近 release / 维护活跃度 / 依赖数 / 周下载量。Empirical signals.
- [ ] 3. 采用证据：被知名项目依赖 / 使用、实际案例。Adoption evidence.
- [ ] 4. 官方文档与示例：README / 文档 / demo / API 是否合需求。Official docs & examples.
- [ ] 5. 社区口碑：开发者评论（HN / Reddit / Discord / issues）、已知坑。Community feedback & known pitfalls.
- [ ] 6. 许可与安全：license、CVE / advisories、依赖树风险。License & security.
- [ ] 7. 本地实测（最铁）：临时目录安装 → 最小 demo → 实测验证。Local verification (the iron judge).
- [ ] 8. 结论留档：对比表 + 推荐 + 理由。Record the conclusion.

**权威性说明 Authority note**：每日最火 / skills 榜单基于安装遥测，只代表被发现度，不代表质量；质量靠 2/3/4/5 证据 + 第 7 步实测判定。Rankings are discoverability, not quality; quality needs evidence + local verification.

### 0.3 产品完善度诊断 · Product-polish diagnosis（反复审查 / 存量不足时先走 run first on repeated-review triggers）

**触发 Triggers**：反复要求审查 / 存量项目反复不足 /「知道不够好但说不清」。Keep asking to review; a lasting sense of insufficiency; "know it's not good enough but can't say why".

**视角切换 Viewpoint switch**：产品视角而非工程师视角——先问「模块本质为用户解决什么、体验应是什么」。Product view first: what does this module solve for the user, what should the experience be.

- [ ] 1. 逐模块拆解本质需求 + 目标体验。Decompose: essential need + target experience.
- [ ] 2. 五问定位缺陷维度（可多维度）Five-question location：
      ① 功能逻辑 Feature logic（缺失/冗余/不自洽/边界/是否真解决问题）
      ② 代码耦合 Code coupling（是否阻碍产品迭代、边界清晰）
      ③ 界面 UI（视觉统一/设计规范/层级/对比度间距）
      ④ 人性化互动流程 Humanized flow（路径/步骤/反馈/认知负担/兜底）
      ⑤ 其他 Other（信息架构导航/三态/性能感知/A11y 多端/文案/品牌一致）
- [ ] 3. 产出《产品完善度诊断报告》：本质需求/现状/缺陷定位/严重度/优先级。Produce the diagnosis report.
- [ ] 4. 与用户确认结论与优先级。Confirm priorities with the user.
- [ ] 5. 回总纲主流程执行（第 8 步门禁产物）。Return to the master sequence.

### 0.4 强制双调研与规划 · Mandatory dual survey & planning（每个任务规划前必过 before every planning）

> 双调研是规划质量门禁：工程师 + 产品经理双视角后才产出详细规划文档。Dual survey = engineer + product-manager views before any detailed plan.

- [ ] 1. **工程师调研 Engineer survey**：代码实况 / 技术可行性 / 复用盘点。Code reality, feasibility, reuse.
- [ ] 2. **产品经理调研 Product-manager survey**：本质需求 / 设计是否完备 / 体验·UI·交互是否符合定位品牌 / 同类对比 / 风险。Essential need, design completeness, positioning fit, risks.
- [ ] 3. 定位「规划缺口」：功能逻辑 / 设计规划 / UI / 交互 / 技术可行性 / 其他。Locate planning gaps.
- [ ] 4. 产出**详细规划文档**：目标边界 / 双调研结论 / 功能清单优先级 / 验收标准 / 风险回滚点。Detailed plan doc.
- [ ] 5. 用户确认后进入执行（第 9 步门禁产物）。Proceed after confirmation.

## 1. 新项目 / 新功能开发（15 步） · New feature / new project (15 steps)

- [ ] 1. 开工自检（平台已适配、规则文件生效）Startup self-check (platform adapted, rule file active)
- [ ] 2. 通读项目规则与对应分类型流程 Read project rules and the relevant task-type flow
- [ ] 3. 读项目文档（目标 / 架构 / 模块 / 测试基线）Read project docs (goals, architecture, modules, test baseline)
- [ ] 4. 复述理解：目标 / 边界 / 验收 Restate understanding: goal / boundaries / acceptance
- [ ] 5. 第一性原理分析任务本质 First-principles analysis of the essence
- [ ] 6. 把目标障碍转化为真问题 Convert goal obstacles into the real problem
- [ ] 7. 识别约束与隐性假设并验证 Identify and verify constraints & assumptions
- [ ] 8. 产品视角判定功能必要性 Product view: is the feature necessary
- [ ] 9. 复用决策链（五问）Reuse decision chain (five questions)
- [ ] 10. 自研前调研现成开源轮子 Research open-source wheels before self-building
- [ ] 11. 需求不明确处追问 Follow-up questions for ambiguity
- [ ] 12. 写 3-5 条可验证验收标准 Write 3-5 verifiable acceptance criteria
- [ ] 13. 写计划（项目用 TDD 则同步写测试）Plan (TDD where the project uses it)
- [ ] 14. 实现 Implement
- [ ] 15. 验证 + 门禁 + 审查 + 文档同批提交 + 验收 + 更新文档日志 Verify, gates, review, commit code+docs, confirm acceptance, update docs/log

## 2. Bug 修复与问题排查（7 步） · Bug fix & troubleshooting (7 steps)

- [ ] 1. 按症状关键词搜经验库（强制；命中按「解决 / 预防」执行）Search the experience log by symptom keywords (mandatory)
- [ ] 2. 未命中再检索开发日志 / 任务记录 Miss? Also search dev log / task records
- [ ] 3. 复现问题 Reproduce
- [ ] 4. 定位根因：系统化调试 + 因果链（3-5 层，逐环验证）Root-cause: systematic debugging + causal chain (verify each link)
- [ ] 5. 写回归测试 Write a regression test
- [ ] 6. 最小修复 Minimal fix
- [ ] 7. 验证全绿；记录踩坑（重复 / 高返工成本者入经验库）Verify all green; record the pitfall

## 3. UI / 设计重构 · UI / design rework

- [ ] 1. 产品视角评审（品牌三问 + 用户旅程：发现 → 判断 → 信任 → 连接）Product-view review (brand 3 questions; journey: discover → judge → trust → connect)
- [ ] 2. 读项目设计规范与组件复用清单 Read the design spec and component reuse list
- [ ] 3. 查组件复用（五问），未命中再自研并记录理由 Check reuse (five questions); self-build + record the reason if missed
- [ ] 4. 视觉审查（截图 / 视觉工具）Visual review (screenshots / vision tool)
- [ ] 5. 按规范实现（白名单护栏）Implement per spec (whitelist guardrails)
- [ ] 6. 双视口截图验证 Verify in both viewport widths
- [ ] 7. 可访问性与性能检查 Accessibility & performance checks
- [ ] 8. 记录到项目重构文档 Record in the project rework doc

## 4. 部署与运维 · Deploy & operations

- [ ] 1. 本地构建 Local build
- [ ] 2. 打包上传 Package and upload
- [ ] 3. 服务器解压 + 迁移 + 进程重载 Unpack + migrate + reload process
- [ ] 4. 准备回滚预案（第 43 条）Prepare the rollback plan (rule 43)
- [ ] 5. 健康检查与告警接入 Health checks and alert wiring
- [ ] 6. 发布审批 + 观察期（约 30 分钟）Publish approval + ~30 min observation
- [ ] 7. 告警响应：确认 → 分级 → 定位 → 处置 → 复盘 Alert response: confirm → classify → locate → dispose → review
- [ ] 8. 周期备份恢复演练 Backup/restore drill
- [ ] 9. 记录部署文档 Record the deployment

## 5. 文档与交接 · Documentation & handover

- [ ] 1. 权威文档与代码同批提交 Update authoritative docs with code
- [ ] 2. 新引用外部资源当次登记参考资源文档 Register newly referenced external resources
- [ ] 3. 更新交接清单 Update the handover checklist
- [ ] 4. 记录经验教训 Record lessons learned
- [ ] 5. 自查口径一致 Self-check consistency of key numbers
- [ ] 6. 归档检查（等价物前置，第 37 条）Archive check (equivalence precondition, rule 37)

## 6. 重大决策与复杂任务 · Major decisions & complex tasks

> **必问强化 Must-ask reinforcement**：目标 / 边界 / 方向有歧义、或对需求**理解不尽确定**时，普通模式也必问（提问工具优先，无从则用结构化文本协议并**结束回合等待**）——**问清楚比问少了更重要，理解需求比模糊执行更重要**。When direction / boundaries are ambiguous or understanding of the need is not fully certain, normal mode asks too (asking tool first, else the text protocol and end the turn) — asking clearly beats asking less; understanding the need beats executing it vaguely.

- [ ] 1. 识别触发点 Recognize the trigger (direction / architecture / scope / conflict / not-fully-certain understanding)
- [ ] 2. 决策简报：理解 + 选项对比 + 优缺点 + 后果 + 推荐（TOC：先约束与假设再比方案）Build the decision brief (understanding, options, pros/cons, consequences, recommendation)
- [ ] 3. 提问并结束回合等待 Ask via asking tool or text protocol; end the turn and wait
- [ ] 4. 按确认方向执行 Execute the confirmed direction
- [ ] 5. 复盘并记录决策 Review and record the decision

## 7. 目标模式 · 无人值守 · Goal mode / unattended

- [ ] 1. 确认目标与模式 Confirm goal and mode
- [ ] 2. 执行前写计划与风险评级入任务记录（时间 / 轮次 / 花费预算；按文件边界拆子任务）Write plan + risk rating into the task record (budgets; split by file boundaries)**；回滚点本地备份优先、默认不 git push（第 45 条）rollback points use local backup first, no git push by default (rule 45)**
- [ ] 3. 按 L1/L2/L3 分级决策（SKILL.md 第 5 节）Triage decisions by L1/L2/L3 (SKILL.md §5)
- [ ] 4. 自主执行、全程记录；超预算自动停 Execute autonomously, record everything; stop past budget**；暂停仅两种情形——重大决策（L3）/ 严重阻塞问题；其余重要决策「先调研 → 按第一推荐推进 → 完整归档决策记录」；每里程碑强制落盘 task-log；本地快照就绪 → 破坏性 / 修改类操作可安全执行（L3 除外，仍暂停）Pause only in two cases — major decisions (L3) / severe blocking problems; other decisions follow "investigate → first recommendation → full archive"; every milestone forces a landing in the task log; a local snapshot ready → destructive / modification-class ops are safe to execute (L3 excepted, still pauses)**
- [ ] 5. 复盘交付 + 待确认清单；提交推送附说明 Retrospective + open-questions list; commit with explanation**（目标模式达成后用户统一决定是否推送 the user decides together whether to push after a goal-mode run)**

## 8. 多会话编排 · Multi-session orchestration

- [ ] 1. 触发：路线图 / 交接清单标记为多会话 Trigger: roadmap / handover-list marks it multi-session
- [ ] 2. 读编排权威确认本会话序号与主题 Read the orchestration line for this session's number and topic
- [ ] 3. 每会话独立分支 + 任务记录（复述 / 风险 / 3-5 条验收）Own branch + task record per session
- [ ] 4. 开工与提交前查 `git status` 与文件修改时间；有并发改动先协调 Check git status & mtimes before starting/committing; coordinate on concurrent edits
- [ ] 5. 按本会话验收闭环 Execute and close per this session's criteria
- [ ] 6. 更新交接清单完成块与状态汇总 Update the handover checklist and status summary
- [ ] 7. 提交推送（重读 diff——只含本会话文件）、合并 Commit/push (re-read diff — only this session's files), merge
- [ ] 8. 下一会话按「下一步」继续，避免单会话超载 Continue from "Next step"; don't overload one session

## 9. 新增工作流规则（6 步，未经批准不得落盘） · Adding a new rule (6 steps, no landing without approval)

1. **采集 Collect**——列出规则索引作为去重基线。List the rule index as the dedupe baseline.
2. **分析（五问）Analyze (five questions)**——必要性 / 违规后果 / 可执行性 / 重复性 / 联动范围。Necessity / consequence / executability / duplication / ripple scope.
3. **草拟（四段模板）Draft (four-paragraph template)**——来源｜解决什么问题｜违规后果｜与现有规则关系；编号续接；标注固化日期。Source ｜ problem solved ｜ consequence ｜ relationship to existing rules; number after the current section.
4. **审批 Approve**——展示候选（含五问结论与疑似重复清单），用户可批准 / 修改 / 否决；不答复或否决 = 不落盘。Present the candidate; approve / modify / veto; no answer = no landing.
5. **落盘与复检 Land & re-check**——追加条目 → 索引检查全绿 → 同步受影响文档。Append → index check green → sync affected docs.
6. **留档提交 Record & commit**——任务记录载明五问 / 审批 / 验证；提交信息含改动与验证。Task record carries the conclusions; commit message states change + verification.

## 复用决策链（五问） · Reuse decision chain (five questions)

1. **功能是否必要？Is the feature necessary?** 产品视角先判；无真实用户价值不做。Judge from the product view; no real value → don't build.
2. **平台是否原生支持？Native support?** HTML/CSS/浏览器 API 优先（dialog、Popover、details/summary、Clipboard、scroll-behavior、`:has()`、原生拖拽……）Platform-native APIs first.
3. **现有标准库 / 组件库能否覆盖？Stdlib / component library?** 优先当前项目组件库与保留组件。Prefer the project's own libraries and kept components.
4. **已有依赖能否覆盖？Existing dependency?** 优先已装依赖，不重复安装。Prefer installed dependencies; don't install duplicates.
5. **能否用最少代码完成？Least code?** 优先组合现有组件（尽量一行级）。Prefer composing existing parts (ideally one-line-level).

全链未命中才允许自研，且必须记录调研结论与理由。Only a full miss allows self-building — record the research conclusion and reason.

## 质量门禁 · Quality gates

- **提交前 Pre-commit**：lint / type-check / 单测 + 集成（项目基线权威，基线回退拦截）/ 覆盖率（核心 ≥ 80%）/ 依赖审计（发版前）/ 提交信息（header ≤ 100）/ 文档同批（`git status` 检查）。Lint / type-check / unit+integration (project baseline is authoritative) / coverage (core ≥ 80%) / dependency audit (pre-release) / commit message (header ≤ 100 chars) / docs with code.
- **CI**：每次推送跑 lint + type-check + 护栏 + 单测 + 集成；发版加跑 E2E + 性能。Every push: lint + type-check + guardrails + unit + integration; releases add E2E + performance.
- **审查循环 Review loop**：审查者视角重读 diff（边界 / 安全 / 可读性 / 未验证项 / 复用与最少代码 / 产品视角）；失败 → 修复 → 重跑（限 3 轮）→ 仍失败停下汇报；中途变更先记录影响。Re-read the diff as a reviewer; max 3 rounds; then stop and report; record impact on mid-way requirement changes.
- **独立审查（可选子代理）Independent review (optional sub-agents)**：critic 方案评审 / risk-reviewer 风险评审 / security-auditor 安全审计模板在 `templates/agents/`，复制适配。Templates in `templates/agents/`; copy & adapt.
- **安全 Safety**：每次提交前密钥扫描（CI 强制）；泄露应急：撤销轮换 → 排查泄露面 → 记录复盘。Secret scan before every commit; leak: revoke/rotate → map exposure → record.
- **周期 Periodic**：每月依赖维护 / 工作流回顾 / 记忆维护；每季度技能审计 + 文档对账。Monthly deps / workflow / memory; quarterly skill audit & doc reconciliation.

## 工具与技能策略（通用） · Tools & skills strategy (generic)

- 每次任务最多加载 1-3 个技能，先按目录筛选，再按 `skill-usage.md` §4 读取分类加载——默认**渐进式**（先主 SKILL.md 再按需读 references）；**前端 / UI / 设计类、核心治理 / 工作流类无条件强制完整读取**（上下文充足 / 无预算限制也不减少）。Load at most 1-3 skills per task, filtered by catalog, then per the read classification in `skill-usage.md` §4 — progressive by default; front-end / UI / design and core-governance classes are unconditionally fully read.
- 无技能不阻塞；**本地无 Skill 时先问用户（`skill-usage.md` §3）**：是否寻找权威 Skill 源安装 / 本机其他 Skill 安装目录可复用，安装必走 `security.md` 校验——再降级通用能力 + 官方文档兜底，降级留痕。No skill does not block; when none is local, ask the user first (§3) — authoritative source or another local install dir, vetting per `security.md` — before degrading to general capability; record the fallback.
- 反复需要（2-3 次）的能力按工作流 9 沉淀为新技能。Repeated needs (2-3×) become new skills via workflow 9.

## 记忆文件协议（外部化长期记忆）· Memory-file protocol (externalized long-term memory)

Agent 无天生长期记忆、也无法感知上下文压缩——把会话状态外部化到随时可重读的文件。Agents have no inherent long-term memory and cannot sense compaction — externalize the session state to a re-readable file.

- **位置 / 结构 Location & structure（统一归档在项目根 `memory/`）**：任何会话（含下一个 AI）开工**先扫该目录**，不存在或缺失文件即自动创建骨架（模板 `templates/workspace-memory-template.md`）；每文件保持一屏内的精简度。Unified at the project root `memory/`; every session (incl. the next AI) scans it on start and auto-creates the missing skeleton from `templates/workspace-memory-template.md`; keep each file ≤ 1 screen.
  - `memory/state.md`——当前目标 / 已做决策 / 约束 / 进度+下一步（一屏内）。Goal ／ decisions ／ constraints ／ progress+next.
  - `memory/experience.md`——踩坑经验库（症状→根因→解决→预防）。Pitfall log (symptom→cause→fix→prevention).
  - `memory/preferences.md`——已确认偏好（技术栈/语言/风格）。Confirmed preferences.
  - `memory/task-log/`——任务记录 `YYYY-MM-DD-名称.md`。Task records (date-named).
  - 项目业务恰用 `memory/` 时，在项目规则文件内改 `.agent-records/`（唯一合法覆盖点）。Override to `.agent-records/` on business conflict (only legal override point).
- **用户偏好字段 User preferences**——维护已确认的技术栈/语言/风格，确认后立即写入、会话开始读取、同类决策复用不重复问；**用户偏好语言记入 `preferences.md`，决定模型输出的思考 / 表述使用什么语言**（未记录默认跟随会话输入语言）；**写入后主动向用户复核大类方向**，偏离按其修正。Keep confirmed choices; reuse instead of re-asking; **record the preferred language, which decides your thinking/output language** (default: follow the session's input language); **after writing, actively remind the user to re-check the broad direction** (stack / language / style) and correct on deviation. 密钥与破坏性意图绝不写入 Never secrets or destructive intent.
- **写入 Write at**：①目标确认（第 6 步）；②任务/里程碑完成；**③每项重要决策 → 决策审计归档（现象 / 依据 / 被否候选与取舍 / 选择 / 影响 / 运行状态，与 task-log 并列；目标模式尤其逐条记）every important decision → a decision-audit archive entry**；④上下文 40-60% 前；⑤会话结束归档前。
- **读取 Read at**：①会话开始；②压缩 / 重置 / 重载后——**先读再继续**；③新任务前扫一眼。Session start; after compaction/reset — **read first, then continue**; before new tasks.
- **完成后更新序 Completion update order（会话结束收尾，最小验证后依序）**：①最小验证 + 自查；②更新 `task-log/<日期>-<名称>.md`（理解→验收→决策→结果）**并为此类重要决策落盘一份决策审计归档**；③更新 `experience.md`（新踩坑或重复坑，症状→根因→解决→预防）；④更新 `preferences.md`（写入后主动复核大类方向；密钥与破坏性意图绝不写入）；⑤文档与代码同批提交，会话结束提炼 1-5 条知识点（默认 3）；**关键回滚本地备份优先、仅在需远程保护 / 交付时才 push**。① minimal verification + self-check ② update task-log (understanding→acceptance→decisions→result) plus a decision-audit archive entry for every important decision ③ update experience (new/recurring pitfalls) ④ update preferences (re-check with the user; no secrets) ⑤ ship docs+code, distill 1-5 knowledge points (default 3); rollbacks go local backup first, push only when remote protection / delivery is genuinely needed.
- **分层 Layering**：记忆文件 = 状态层 + 踩坑层；知识文档（第 11 步双写）= 学习层；完整细则仍在 Skill `references/` 按需加载，互不替代。Memory = *state* + *pitfall*; knowledge docs = *learning*; full details load on demand from `references/`. They do not replace each other.
- **压缩后显式重载顺序 Reload sequence after compaction**：用户说「重载 / 你被压缩了」或平台重置上下文 → ①重读 SKILL.md → ②重读记忆文件 → ③重读当前引用 → ④向用户复述任务与验收再继续。On reload/reset: re-read SKILL.md → memory file → needed references → restate task + acceptance, then continue.
- **提示词预算（可选）Prompt budget (optional)**：见 `templates/prompt-budget.template.md`——设置档位（nano/minimal/standard/full），只加载任务所需引用；记忆文件与任务记录保持预算内。预算指引非强制。See `templates/prompt-budget.template.md`; budgets are guidance, not enforcement.