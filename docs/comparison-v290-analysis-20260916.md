# 对比分析：shisan-xinuo-workflow v2.9.0 vs 同类项目与同类 Skill（2026-09-16）

> 方法与局限：一手页面级调研（GitHub README / 官方 docs，抓取日 2026-09-16），非源码级深读；11 家外部样本+本项目；样本偏英文主流生态，国产 agent 平台规则面未采样（注入点表已覆盖的 Trae/WorkBuddy 侧以本机实测为准）。星标数字为页面自述。
> 承接：docs/audit-v290-review-20260916.md §四（四家初对标）——本报告扩样本至 11 家并升级为全维矩阵；原 C1/C2/C3 缺口结论经新样本**加严证实**（见 §四）。

## 一、样本分类学（外部 11 家 → 四类；本项目横跨三类）

| 类 | 样本 | 一句话特征 |
|---|---|---|
| A 方法论框架（重流程） | superpowers（obra）、spec-kit（GitHub，137k★）、BMAD-METHOD（53.1k★）、PRP（Wirasm/prp，2.2k★） | 把 SDLC 阶段做成强制技能/命令：TDD/系统化调试、constitution→specify→plan→implement→converge、多代理敏捷、PRP 一次通过包 |
| B 规则承载（重知识注入） | AGENTS.md 标准（60k+ 项目，Linux Foundation 治理）、Cursor rules、Kiro steering、Aider conventions | 静态知识文件＋平台原生加载机制（四态/条件加载/优先级规则） |
| C 标准与生态 | Agent Skills 标准（agentskills.io＋anthropics/skills，176.5k★）、Claude Code 官方 Skill 规范 | SKILL.md 规范：frontmatter/渐进披露三层/<500 行/description 1536 字符截断 |
| D 工具链（重分发同步） | rulesync（dyoshikawa，1.4k★）、本项目 scripts（syncer/deploy_injection/verify-release/facts_sync） | 单一事实源 → 多平台配置生成/校验/同步 |

**本项目定位**：横跨 B（注入核心常驻）＋A（三级跑道流程）＋D（同步/门禁/对账工具链）的「纪律治理元 Skill」——样本中无同型；且为**唯一中文版**。

## 二、六维快评矩阵（●成熟 ◐部分 ○缺；常驻成本列=每会话固定开销）

| 样本 | 流程强制 | 触达/消费机制 | 验证与证据 | 记忆/留档 | 跨平台 | 规则治理代谢 |
|---|---|---|---|---|---|---|
| **本项目 v2.9.0** | ◐ 三级跑道+L3 封闭清单 | **● 硬注入+hooks 三通道+每轮再触达+报错必经 TOP** | ◐ GATE 可重跑+verify 7 项+路测 v1-v11（工件不随仓） | ● agent-log 一档制四区+归档轮转 | ◐ 5 平台注入+双副本 syncer | **● 防棘轮+双击晋升+facts_sync 口径对账+字符预算门禁** |
| superpowers | ● TDD/调试/评审强制 | ◐ bootstrap+post-compaction hook（平台支持时） | **● 独立 evals 仓回归** | ◐ 设计/计划文档 | ● ~14 平台插件 | ◐ 写作 skill 规范+PR 流程 |
| spec-kit | ● 六阶段+converge 收敛循环 | ○ 靠人按序调用 | ◐ 人审门+bug verdict | ◐ .specify/memory+constitution | ◐ 多 agent 集成 | ◐ 模板可定制 |
| BMAD | ◐ 分阶段角色化 | ○ | ◐ 测试架构师扩展 | ● durable context | ◐ npx skills 安装 | ◐ doctor 自修 |
| PRP | ● PRD→plan→implement→review | ○ | ● validation gate+`--validate` exit0+自主 loop | ● ~/.prp/ 工件仓 | ◐ Claude Code 插件 | ◐ meta-skill |
| rulesync | ○（不管流程） | ○（只做配置分发） | ○ | ○ | **● ~45 工具×8 配置类** | ◐ import/generate/fetch 单一事实源 |
| Kiro steering | ○（知识面） | ● 平台原生：always/fileMatch/manual/auto 四态 | ◐ hooks 自动化 | ◐ steering+AGENTS.md | ○ 单平台 | ◐ 「review like code」倡导 |
| Cursor rules | ○ | ● always/auto-glob/agent-selected/manual 四态 | ○ | ○ | ○ 单平台 | ◐ <500 行+「重复犯错才加规则」 |
| AGENTS.md 标准 | ○ | ● 平台原生最近文件优先 | ○ | ○ | ● 事实标准 | ○（living doc，无机制） |
| Aider conventions | ○ | ◐ --read/config 显式加载 | ○ | ○ | ○ 单工具 | ○ |
| 官方 Skill 规范 | ○ | ● 平台原生三层披露 | ◐ skill-doctor 成本审计 | ○ | ◐ Agent Skills 标准 | ◐ 防过长倡导 |

## 三、逐维判定（领先/对齐/落后＋证据）

**领先维度 3 项（样本中独有或最强）**
1. **触达/消费机制**：没有任何一家做「错误时刻推送（PostToolUseFailure+post_tool_guard）＋每轮再触达（UserPromptSubmit）＋报错必经 TOP＋在场锚点」。Kiro/Cursor 的条件加载是「知识按需到场」，不是「纪律被强制消费」；superpowers 的 bootstrap 在压缩后依赖平台 hook 支持。本方案把触达做成五层承载＋机证（deploy 探针/锚点断言），这是 README 定调「触达=提示词边界」的兑现面。
2. **规则治理与代谢**：双击晋升制＋防棘轮双向（删减合法鼓励）＋2 干净周期降级＋facts_sync 单源对账（承载点白名单断言）＋注入核心字符预算双口径门禁（5945≤6000）＋时点快照豁免——11 家样本中，规则文件自身的「对账/代谢/预算」机制为零家（Cursor 只倡导 <500 行，AGENTS.md 无长度指导）。
3. **可审计交付工件**：GATE 9 字段单行（cmd/exit/files/refs/errpath 可重跑）＋会话状态面取证行——spec-kit/PRP 的 verdict/gate 是流程级，本项目把证据压到每次任务块粒度。

**对齐维度 4 项**
4. 渐进披露：T1 注入核心/T2 症状检索/T3 领域查询 ＝ 官方三层披露等价；SKILL.md 383 行<500 合规，description 远短于 1536。
5. durable context：agent-log 一档制（状态段/教训/偏好/流水＋归档轮转＋记忆路由裁决）≈ BMAD durable context 且形态更收敛（单文件四区）。
6. 流程强制形态：L2-F 9 步＋出口产物门禁 ≈ spec-kit/PRP 阶段化；差异在收敛闭环（见落后 1）。
7. 分发深度：deploy_injection（先备份/合并不覆盖/锚点单源/写入后探针/--check 取 package.json 堵假绿）在「注入内容管理」上深于 rulesync 的纯文件生成；广度则明显窄（见落后 3）。

**落后维度 3 项（＝审查报告 C1/C2/C3 的加严证实）**
1. **行为评测自动化（C1，差距最大）**：superpowers 有独立 evals 仓做技能行为回归；PRP 把「可执行验证命令＋exit0 权威判据＋自主 loop（默认 3 周期/10 迭代）」做成产品形态。本项目路测 v1-v11 判分工件全在仓库外（D:/roadtest-v11），npm description 卖点「探针 24/24」不可随仓复跑——「纪律被验证」维度整体落后。
2. **机器收敛闭环（C2）**：spec-kit converge（迭代至 Converged）与 PRP `--validate "<cmd>"`（exit 0=通过）提供了机器可判的收敛语义；本项目走查「允许多轮」无判据字段。借鉴成本极低：GATE cmd 字段语义天然就是收敛判据载体。
3. **条件触达与分发广度（C3 扩展）**：Cursor 四态规则（auto-glob 按文件域自动附载）与 Kiro fileMatch 是平台级「按域自动触达」，本项目症状索引是模型手动等价物；rulesync 单一事实源已覆盖 ~45 工具×8 配置类（含 hooks/permissions/subagents），本项目 syncer 仅 5 平台×2 面（skill 副本+记忆层）。**新风险观察：rulesync 支持矩阵已列 ZCode——同用户双同步通道并存面出现**；定位上不竞合（本项目=内容产品，rulesync=管道工具），观察即可。

**顺风项**：AGENTS.md 成 Linux Foundation 治理的事实标准（本项目注入点表同向且已覆盖）；Agent Skills 标准（agentskills.io）与本 Skill frontmatter 兼容（name/description/metadata）；唯一中文版＋「标范与标本合集」定位在 11 家样本中无竞品。

## 四、结论与建议（供拍板，不施工）

- **一句话结论**：同类项目分别在「流程机器化（spec-kit/PRP）」「技能生态（anthropics/skills）」「配置分发（rulesync）」「平台原生触达（Kiro/Cursor）」上做强；本项目独占的是「**纪律被消费＋规则被治理**」两个维度——这正是其余 11 家全部缺位的部分；短板集中在「纪律被验证」（评测不随仓）与「收敛闭环」（无机器判据），且两者修复路径都已被对标证实为社区共识形态。
- 建议 1（承接 P1）：探针 fixtures+runner 随仓 `scripts/evals/`——PRP 的 validation-gate 形态说明这是共识做法，GATE cmd 字段语义与之一致。
- 建议 2（承接 P2）：收敛判据补条——借鉴 `--validate` exit0 语义，明确「GATE cmd 可重跑命令即走查收敛判据」，走防棘轮 grep 查重后入 details。
- 建议 3（承接 P2）：platform-adaptation.md 增「平台能力矩阵」，把 Cursor glob/Kiro fileMatch/ZCode 无 SessionEnd/WorkBuddy hooks 缺位等显式记档（C3）。
- 建议 4：README 对比段补 rulesync/Kiro 两个新对标（现对比表只对手写 AGENTS.md）；发行文案可加「唯一含规则口径对账器（facts_sync）的 Skill」一句。
- 建议 5：观察 rulesync 的 ZCode 目标支持与 agentskills.io 标准演进，不动手。

## 附录（2026-09-16 14:5x 追记 · 批 5 源码级补强：superpowers-evals 真身）

- 真身定位：`prime-radiant-inc/superpowers-evals`（114★，2,006 commits，TypeScript/Bun；obra/superpowers=其私有主的公开镜像）。harness 名 **Quorum**：驱动 9 个真实 coding-agent CLI（Claude/Codex/Antigravity/Gemini/Hermes/Kimi/OpenCode/Pi/Copilot）＋ **Gauntlet（LLM 判分）** ＋确定性 post-checks。
- 定位自述：「eval lab for **workflow compliance**: skill triggering, worktree behavior, subagent coordination, verification reflexes, review quality, cost-shaping」——与本 Skill「纪律被验证」维度正面同类。
- **可借鉴三形态**：①**treatment/stock 双臂内置**（conversation_routine_use 套件：同 harness/模型/effort 下「superpowers: none」对照臂 vs 处理臂，36-attempt 级样本）——正对本仓「规则有效性 A/B 未达显著」的实验缺口，对照臂已是其产品形态；②**对话式场景＋私有判据＋独立 assessor**（author 写 user-like 对话与 Acceptance Criteria，判据不进被测上下文，capture 后独立 assessor 判分）——防自评污染（对应本仓 S3 假 errpath 教训的机制化）；③**隔离 HOME＋双模式安全线**（throwaway per-run home＋静态 checks 可 CI/live evals 仅信任维护者）。
- 本仓对位：scripts/evals 判分器（rollout 逐请求结构判分）=同方向轻量第一步；差距=无对照臂自动化、判分与被测同体（自评）、无隔离环境。**结论加严**：C1 缺口的成熟形态明确为「双臂对照＋独立判分＋隔离环境」，本仓补齐顺序建议=先对照臂（每次路测强制加无规则 arm）→再判分隔离（判据预注册私有化）→隔离环境最后。
