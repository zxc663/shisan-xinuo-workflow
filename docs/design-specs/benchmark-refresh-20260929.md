# 对标刷新 · benchmark-refresh-20260929（批 R · 只调研不施工）

> 依据：roadtest 收口批计划 §批 R。基线=docs/comparison-v290-analysis-20260916.md（十一家，09-16）。
> 本档只做 09-16 → 09-29 增量刷新与新贵侦察；每项=借鉴点/移植成本/验证法；末尾=可吸收清单（候选，未施工）。
> 检索预算：6 轮 WebSearch（1-2 轮/家），符合 L2-F 双预算纪律。

## 一、新贵四家（点名侦察对象）

### 1. OpenSpec（Fission-AI）——已上 ThoughtWorks Radar（2026-04）
- 形态：轻量 SDD 框架，`proposal → design → tasks → scenarios` 全部落仓；spec 走 PR 评审、**机器可检查**；经 slash-commands/MCP 接入 agent。`npm i -g @fission-ai/openspec`。
- 借鉴点：①「spec 可机器检查+可当 PR 评审」=交付形态成熟度标尺——本项目 verify-release 8 门禁+判据自测已是同思路，可对表补「细则机检覆盖率」可见指标（挂 G4 usage-probe 延伸）。②scenarios 与 tasks 绑定=spec-trace 双向追溯的社区同形。
- 移植成本：理念=零（已在场）；工具面=中（不引入，保持自研单源）。
- 验证法：verify-release 判据自测项数 vs 405 条细则的可机检比（一次 grep/python 统计即可出数）。

### 2. Martin Fowler SDD 综述（2025-10-15）+ 2026 跟进簇
- 主文：Understanding Spec-Driven-Development: Kiro, spec-kit（martinfowler.com）。2026 跟进：arXiv《From Code to Contract in the Age of AI Coding Assistants》(2026-01-30，SDD 原则/工作流/工具综述)；productbuilder 三模式（**spec-first / spec-anchored**）；反方：Code over Specs（2026-05，援引《Is Design Dead?》计划式 vs 演化式设计）。
- 借鉴点：①「spec-anchored（spec 与代码共演进）」=本项目 injection-core 与 references/details 共演进的学术同形，README 定位段可引「spec-anchored discipline」术语增表达力（不改口径）。②反方批评=健康度对照：本项目「概率护栏非保证」自我定位与批评方结论一致，无需改。
- 移植成本：零（术语引用级）。
- 验证法：README 定位节改动后 grep 锚点（若采纳 E 项术语）。

### 3. sebastianwessel SDD skills 包（Show HN，2026-09 下旬）
- 形态：Claude Code agent skills 合集做 spec-driven 开发（HN Show HN 数日前）；作者即 @sebastianwessel/quickjs（~900 星）作者，另有《Claude Code Skills & Hooks You Should Know》。
- 借鉴点：①「skills=流程分册」被社区独立复刻=本项目 flows 九分册形态的外部效度信号；②观察其 phases/quality gates 的 skill 内化写法（gate 写进 skill 而非 hooks）——本项目 G10 hook 路线 vs skill 内化路线的对照样本。
- 移植成本：观察项，零移植。
- 验证法：不适用（对照样本记账）。

### 4. SDD Pilot（Windsurf 生态）
- 形态：强制结构化开发阶段+质量门（ecosyste.ms 索引一处直接命中，文档稀）。
- 借鉴点：与本项目三级跑道+GATE 门禁同域；信息不足以提炼，列观察项。
- 移植成本：不适用。
- 验证法：待其文档完善后复看（候选池）。

## 二、存量刷新（09-16 报告在册对象）

### 5. GitHub Spec Kit
- 增量：~105K stars（09-16 报告时点未记星数），vendor-neutral SDD 事实标准地位强化；OpenSpec/dotdog 等工具已做 Spec-Kit 格式自动兼容。
- 借鉴点：无新增（v2.9 对比已覆盖：其 commands 形态本项目已裁定 slash=试点不推广）。
- 移植成本：不适用。

### 6. rulesync
- 增量：宣称 19+ 开发工具支持（lobehub 词条；09-16 报告口径为「45 工具已列」——两口径不同源，**不合并、分列存疑**，以 repo 官方清单为准）。Claude Code 配置转换双向。
- 借鉴点：多平台注入形态生成的第三方成熟度继续领先（本项目 deploy_injection 五平台 + syncer 三路合并为自研对应物）；无新增动作。
- 移植成本：不适用（自研保持）。

## 三、评测 harness 簇（新领域，与 probe_runner 直接对标）

### 7. Skill 评测 harness 生态（本批最高价值发现）
- MLflow 官方博客《Testing and Refining Claude Code Skills with MLflow》：**环境组装 + 无头 Claude Code 执行 + judge 评分**单次可复现运行——与本项目 probe_runner（夹具 mk + 无头 CLI + j2.5 判据 + scorecard）**同构**。
- ECC eval-harness skill / mcpmarket：「eval 是 AI 行为的单元测试」「防回归」；stackhawk：**声明行为→同提示→验证行为变化**的三步法；litmus-lab：**行为 harness 应分离 agent 与判分标准**；padiso：golden-path 回放+非确定工作流回归；LangChain《Evaluating Skills》；alphaxiv 2607.03691 harness 中间件论文。
- 借鉴点：①「行为回归基线」框架化——v330-val2 出的三数字应固化为版本级回归基线，后续每次发版重跑同矩阵对比（基础设施已在场，表述升级即可）。②「判分/被测分离」已有（机判不接收分组+独立模型盲判），可在盲测设计档补一条显式声明（引用 litmus 分离论增强严谨性表述）。
- 移植成本：低（表述与流程固化，零新代码）。
- 验证法：下个版本的 v331 矩阵跑同 21 场景，diff 三数字。

## 四、可吸收清单（候选池 · 未施工 · 待裁决）

| # | 候选 | 来源 | 成本 | 建议去向 |
| --- | --- | --- | --- | --- |
| A | 三数字固化为版本行为回归基线（v331 起每版重跑对比） | MLflow/ECC 簇 | 低 | 批 A′ 收口时在 agent-log 状态段加一行「回归基线=v330-val2」 |
| B | 盲测设计档补「判分/被测分离」显式声明 | litmus-lab | 低 | blind-eval-design.md 一段（随批 G 文档动作顺带） |
| C | 细则机检覆盖率可见指标 | OpenSpec | 中 | 挂 G4 usage-probe 延伸（候选队列） |
| D | README 定位段引「spec-anchored」术语 | Fowler 簇 | 低 | 下次 README 内容批顺带（候选队列） |
| E | arXiv 2601《From Code to Contract》精读 | Fowler 簇 | 1-2h | Q 候选队列（调研任务） |
| F | sebastianwessel gates-in-skill 写法对照观察 | HN 簇 | 零 | 候选池记账 |

## 五、来源
- OpenSpec：ThoughtWorks Radar（thoughtworks.com/radar）；github.com/Fission-AI/OpenSpec
- Fowler：martinfowler.com《Understanding Spec-Driven-Development》；arxiv.org《From Code to Contract》（2026-01）；blog.devgenius.io《Code over Specs》（2026-05）
- sebastianwessel：news.ycombinator.com Show HN；github.com/sebastianwessel
- SDD Pilot：awesome.ecosyste.ms（windsurf 标签）
- Spec Kit：github.com（~105K stars 口径来自检索摘要）
- rulesync：lobehub.com MCP 目录词条
- harness 簇：mlflow.org/blog/evaluating-skills-mlflow；github.com/affaan-m/ECC；stackhawk.com；litmus-lab.com；padiso.ai；langchain.com/blog/evaluating-skills；alphaxiv.org/abs/2607.03691

---
*批 R 完成标记：6 轮检索/6 家+1 簇，全部只调研未施工；吸收候选 6 条入池。*
