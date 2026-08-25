# 分类型工作流与质量门禁 · Task-Type Workflows & Quality Gates（中英双语 · Bilingual）

加载时机：开始与下列任务类型匹配的工作、或 SKILL.md 引用具体流程时。When to load: when starting work matching one of the task types below, or when SKILL.md cites a workflow. 每个流程都是清单，逐项打勾。Each flow is a checklist — track progress against it.

## 0. 任务主流程——调研驱动（任何任务类型前先执行）· Task operating sequence — research-driven (run before ANY task type)

- [ ] 1. 接收指令；第一性原理理解（本质 / 必要 / 惯性）。Receive; first-principles understanding (essence / required / inertia).
- [ ] 2. 按症状 / 关键词检索经验库；命中 → 按「解决 / 预防」执行。Search the experience log by symptom/keyword; hit → execute per "solve / prevent".
- [ ] 3. 调研实际资源：真实代码（现状证据：消费方 / 常量 / 开关 + 文件行号结论）、环境、工作区、可用 Skill / MCP。Survey actual resources: real code (status evidence), environment, workspace, available skills & MCP.
- [ ] 4. 降级：环境 / 能力 / 工具 / Skill / MCP 不可用 → 联网调研、加载所需 Skill、记录降级。Degraded: unavailable → research online, load needed skill, record fallback.
- [ ] 5. 复用调研：本地项目 → 同类 / 已知项目资源（复用五问）；自研时记录结论。Reuse survey: local → similar projects (five-question chain); record conclusions.
- [ ] 6. 向用户复述理解（目标 / 边界 / 验收）；确认对齐。Restate understanding; confirm alignment.
- [ ] 7. 疑问或方向偏移 → 提问并结束回合等待。Ask on doubt or direction drift; end the turn and wait.
- [ ] 8. 产品视角审查 + 约束 / 假设 + 定级 L1/L2/L3 + 准备回滚点（规则 43）。Product-view + constraints + triage + rollback point.
- [ ] 9. 规划与验收文档：3-5 条可验证标准；目标模式加预算与文件边界。Plan & acceptance doc; goal mode adds budgets + file boundaries.
- [ ] 10. 按分级执行（目标模式：按计划自主、节点记录、超预算自动停）。Execute per triage (goal mode: autonomous per plan).
- [ ] 11. 自查与归档：最小验证 → 自查 → 文档同批 → 双写知识 → 提交附说明。Self-check & archive: verification → self-check → docs with code → dual-write → commit with note.

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

- [ ] 1. 识别触发点 Recognize the trigger (direction / architecture / scope / conflict)
- [ ] 2. 决策简报：理解 + 选项对比 + 优缺点 + 后果 + 推荐（TOC：先约束与假设再比方案）Build the decision brief (understanding, options, pros/cons, consequences, recommendation)
- [ ] 3. 提问并结束回合等待 Ask via asking tool or text protocol; end the turn and wait
- [ ] 4. 按确认方向执行 Execute the confirmed direction
- [ ] 5. 复盘并记录决策 Review and record the decision

## 7. 目标模式 · 无人值守 · Goal mode / unattended

- [ ] 1. 确认目标与模式 Confirm goal and mode
- [ ] 2. 执行前写计划与风险评级入任务记录（时间 / 轮次 / 花费预算；按文件边界拆子任务）Write plan + risk rating into the task record (budgets; split by file boundaries)
- [ ] 3. 按 L1/L2/L3 分级决策（SKILL.md 第 4 节）Triage decisions by L1/L2/L3 (SKILL.md §4)
- [ ] 4. 自主执行、全程记录；超预算自动停 Execute autonomously, record everything; stop past budget
- [ ] 5. 复盘交付 + 待确认清单；提交推送附说明 Retrospective + open-questions list; commit with explanation

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
- **安全 Safety**：每次提交前密钥扫描（CI 强制）；泄露应急：撤销轮换 → 排查泄露面 → 记录复盘。Secret scan before every commit; leak: revoke/rotate → map exposure → record.
- **周期 Periodic**：每月依赖维护 / 工作流回顾 / 记忆维护；每季度技能审计 + 文档对账。Monthly deps / workflow / memory; quarterly skill audit & doc reconciliation.

## 工具与技能策略（通用） · Tools & skills strategy (generic)

- 每次任务最多加载 1-3 个技能，先按目录筛选。Load at most 1-3 skills per task, filtered by catalog first.
- 无技能不阻塞：通用能力 + 官方文档兜底，降级留痕。No skill does not block: general capability + official docs; record the fallback.
- 反复需要（2-3 次）的能力按工作流 9 沉淀为新技能。Repeated needs (2-3×) become new skills via workflow 9.