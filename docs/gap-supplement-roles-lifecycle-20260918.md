# 缺口补充档：角色定位 / 加载后行动契约 / 批量安装精简 / 归档触发自动化（2026-09-18 · 状态：调研留档，计划待用户令）

> 主档回指：`docs/resource-utilization-gap-analysis-20260918.md`（利用率定量）。本档回答用户补充的四个维度：①审查该以什么身份/能力/维度进行（角色提示词方向）②Skill 被加载显示使用后 agent 不知道该干什么=失败 ③用户装一大堆 MCP/Skill 如何精简 ④归档/更新只靠用户下令+日期不行。
> 证据源：小黑盒民间文章一篇（web_reader 全文）+ gh api 实证（upstash/messier 证伪）+ WebSearch 四家（BMAD/Roo/Claude subagents/MetaGPT/superpowers README）+ 本仓三角色模板实测 + 20 个本地 SKILL.md 启发式抽查。

## 0. 一句话结论

四个补充维度指向**同一个结构性缺口：本工作流把「规则」建得很厚（344 细则/47 规则），但把「执行体」建得很薄**——审查没有按维度路由的角色实例（3 个模板存在但无调用路由、无能力门控、调用率未测），技能加载后大多没有「第一步干什么」的行动契约（抽查约 1/3-1/2 首屏无步骤+触发结构，且无一家定义「加载后第一产物」），精简与归档的机制条款全部依赖会话内人工执行而非事件/阈值自动触发。

## 1. 用户观点锚点与民间对照（决策史层）

用户原话（会话补充 + 聊天截图自述）：**「Skill 以后会成为知识库的一部分，再有一部分元语言提示词去根据场景来调用他们」「人设提示词还是有用的，它决定了模型会以什么样的角度去思考问题」**；外聊观点（对方）：skill 能力会逐渐变小、子智能体大厂还没搞明白、codeg 类项目可调用不同 agent 当子智能体。

民间同题样本（小黑盒[分享文章](https://www.xiaoheihe.cn/app/bbs/link/3cbc726e1c25)：《我给所有 AI Agent 写了一份「入职手册」，WorkBuddy/TRAE/ZCode/Qoder 通用》）五痛点与本工作流机制对照：

| 民间手册痛点 | 本工作流既有机制 | 残余缺口 |
|---|---|---|
| 路径硬编码写进长期记忆 | 细则「发现规则不发现路径」类条款 | 无自动检测 |
| 越权改动（不看项目规则就动手） | 承载检查/回指加载/接手摸底 #307 | 依赖模型自觉，无行为面探针 |
| **能力错觉**（文档说工具存在≠你有） | 子代理注入缺口实证（project-subagent-injection-gap）+「不假实现」红线 | 同源问题在民间独立复现=真痛点信号 ✔ |
| **记忆膨胀**（一次性事件/机密/IP 塞进全局记忆） | 容量上限（流水>200 行归档）、密钥绝不入档 | **无自动执行器**（见 §5） |
| **假持久化**（"我记住了"但没落盘） | 「结论立刻落盘」「绝不假实现」红线 | 写后无回读校验的普遍强制 |

民间独立收敛到同一组痛点=外部效度信号；手册的方法论（权威文件优先级链/机器信息每轮探测不持久化/本轮允许-拒绝清单/完成标准=必须真实落盘并报告）可直接进计划期比对池。

## 2. 审查的角色化：开源项目角色定位对比

**「审查该以什么身份、调用什么能力、从哪个维度」——业界答案的公因式是五要素：身份（视角人设）× 能力（工具门控）× 维度（审查清单）× 出口契约（结构化输出）× 路由（何时调谁）。**

| 项目 | 角色集 | 身份载体 | 能力门控 | 出口契约 | 来源 |
|---|---|---|---|---|---|
| [BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | Analyst/PM/Architect/SM/Dev/QA(Test Architect)/UX 全 SDLC 虚拟团队 | 具名 persona（Mary/John/Winston/Quinn）+ 可定制层 + 清单模板 | 按模块加载（v6 模块化） | 每角色绑定文档产物（PRD/架构文档/故事/E2E） | [官方 docs](https://docs.bmad-method.org/reference/skills-and-agents/) |
| [MetaGPT](https://github.com/foundationagents/metagpt) | ProductManager→Architect→PM→Engineer→QA 五角色 SOP 流水线 | Role 类 + `_watch` 订阅（上游产物驱动下游角色） | 订阅机制=只看自己该看的消息 | 顺序产物链（PRD→设计→代码→测试） | [ICLR 论文](https://arxiv.org/html/2308.00352v6) |
| [Roo Code modes](https://roocodeinc.github.io/Roo-Code/basic-usage/using-modes) | Code/Architect/Ask/Debug/Orchestrator + 自定义 | 模式=行为指令集 | **per-mode 工具权限**（读/写/命令/浏览器/MCP 白名单——最彻底） | 模式切换即工具面切换 | 官方 docs |
| [Claude Code subagents](https://code.claude.com/docs/en/agent-sdk/subagents) | .claude/agents/*.md 用户自定义 | frontmatter: name/description/system prompt | **`tools` 字段白名单** + 独立上下文窗口 | description=主代理调度路由（when to use） | 官方 docs |
| [obra/superpowers](https://github.com/obra/superpowers) | spec→plan→**subagent-driven development**（每任务派子代理+审查内嵌循环） | 计划写给「热情但无判断力的初级工程师」=身份降级假设 | 子代理隔离上下文 | TDD 红/绿、YAGNI、DRY 纪律内嵌 | README 实测 |
| 本环境 judge（第一方实例） | 视觉验收判定者 | 「THE single visual acceptance pass」 | read-only+指定工具 | **逐页 JSON verdict（pass/fail+证据）** | 本会话在场的活样本 |
| **本仓三模板**（`skill/shisan-xinuo-workflow/templates/agents/`） | critic（对抗式评审）/risk-reviewer（风险两模式）/security-auditor（L3+推送前） | 身份句+触发时机（description） | **✗ 无工具门控概念**（平台子代理无 tools 字段机制→只能 prompt 声明降级） | 发现/待澄清/残余风险/结论+严重度 ✔ | 本地实测 |

**缺口判定（对照五要素）**：本仓模板身份✔维度✔出口契约✔，**能力门控✗（平台限制，降级方案未写明）、路由✗（何时调谁只有 SKILL §13 一行提及，无「症状→角色」dispatch 矩阵）、调用率未测（无任何真实调用记录在案——不得假绿，标注未测）**。
**用户判断「缺的不是规则而是实践开发问题」的机制解释**：details 344 条=**事后**教训库（踩过什么坑），三角色=**事前**审查体，但实践开发高频维度（构建失败/契约不匹配/测试假绿/前端渲染/性能劣化/并发竞态）没有对应角色实例——规则回答「过去错在哪」，没有人回答「现在该派谁、查什么、按什么顺序」。角色提示词=把审查维度**人格化为可路由的执行体**，方向成立。

## 3. 加载后行动契约（load-then-what）：「显示使用了却不知道干什么」= 失败

- 本地抽查（20 个用户级 SKILL.md，启发式：首屏 3000 字符内「编号步骤」×「触发词/祈使句」双条件）：**PASS 50%-70%（两口径，启发式噪声大，取区间）**；WEAK 侧含 ui-ux-pro-max/frontend-design/emil-design-eng/cms-skill-collection 等。方法局限如实声明：只测「有步骤+触发词」，未测语义可执行性。
- **结构性发现（比比例更重要）**：抽查范围内**没有任何技能定义「加载后第一产物」**——加载后 agent 该先输出什么、以什么格式向用户确认理解，唯一有此契约的是本工作流自身（状态行+开工四步+GATE）。其余技能是「参考书」（需要时查）而非「程序」（加载即执行序列）——这两类技能的生命周期应当不同，但平台一律按参考书对待。
- 业界对照：Anthropic [Agent Skills](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills) 渐进披露三层（元数据常驻→SKILL.md 按需→附带文件）；Claude Code subagent 的 description 字段专职 when-to-use 路由——**「被选中后干什么」业界同样没有统一契约**，这是空白带也是机会带。
- 失败判定草案（供计划期）：技能被加载后 10 秒内 agent 无法说出「我现在要做的第一个动作+出口产物」=该次加载失败；判据落到正文结构（①触发确认 ②首动作 ③出口产物三件齐备）。

## 4. 装了一大堆怎么精简：平台机制实证 + 治理规则候选

**平台机制（zcode-configuration-guide 实测抓取，全部原生支持）**：

| 机制 | 路径 | 对精简的意义 |
|---|---|---|
| workspace 级 skills | `<repo>/.zcode/skills/`、`<repo>/.agents/skills/` | 项目专用技能下沉到项目，全局清单变短 |
| 同名遮蔽（先到先得） | user → workspace `.zcode` → workspace `.agents` → plugins | 可用同名精简版在项目级遮蔽重型版 |
| **skill/command disable overrides** | `~/.zcode/cli/config.json` | **不删文件、按名单停用**——零调用 29 条的直接出口 |
| workspace 级 MCP | `<repo>/.zcode/config.json → mcp.servers` | 09-17 裁剪档已知；本项目级迁移的正式机制 |
| 插件开关 | config `enabledPlugins` | computer-use 等 D 档悬案的出口 |

**治理规则候选（结合主档利用率数据）**：准入=新装技能/MCP 默认「试用 30 天」；退出=零调用超期→disable overrides 名单（可逆，不删）；常驻预算线（工具定义 >10K tok / 10+ 工具才值得常驻——Anthropic Tool Search 阈值判据的借用）；清单双列去重（anti-ui-slop/scrollcraft/ui-ux-pro-max 三对，删一侧）。参照 Cursor rules 的 attach 分级（Always/Auto/Manual/Glob，背景知识未深证）做「常驻/按需/手动」三级设计。

## 5. 归档/更新触发自动化：不能只靠用户下令+日期

**现状盘点**：本工作流已有正确的**触发条件**（流水>200 行归档/教训>150 行轮转/同坑≥3 次晋升/2 个干净周期降级/容量上限），但**全部依赖「下一个会话读档时人工发现并执行」**——无人触发就无限期滞留；日期型巡检（如夜班 cron）本质还是「人下令的周期」。
**平台可用执行器（已实证存在）**：hooks 7 事件（Stop/SessionStart/PostToolUse 已在本仓用起来——post_tool_guard/top_push 先例）、CronCreate 定时自动化（3.0 loop 探针 runner 先例）、OffPeak 闲时任务、auto-memory 平台自动写。
**方向映射（触发三型）**：事件驱动（Stop hook 做收尾审计：GATE 在场/流水追加/超限迁移）、阈值驱动（尺寸/零调用天数/命中计数越过线即在下一会话开工项注入「待归档」任务）、周期驱动（cron 低频巡检兜底）——「用户下令」从主路径降级为异常路径。民间手册「记忆维护原则」六条（替换过时事实/权威文档在场才留指针/一次性事件不晋升/每轮重读项目状态/用户纠正优先）可作条款比对池。

## 6. 待拍板/计划输入（增量，并入主档 §7）

1. 角色体系：是否把三模板扩成「症状→角色」dispatch 矩阵（构建/契约/测试/前端/性能维度要不要新增角色 vs 三角色分维清单扩展）；能力门控的平台降级方案（prompt 声明式）；角色调用率是否纳入路测探针。
2. 行动契约：SKILL.md 正文「首屏三件套」（触发确认/首动作/出口产物）是否立为写作门禁（verify-release 新检查项候选）；对 44 装机技能是否出整改名单。
3. 精简：disable overrides 首批名单（零调用 29 条裁哪些）；三对双列删哪侧；computer-use D 档终裁。
4. 自动化：Stop hook 收尾审计要不要上（本仓 hooks 基建现成）；阈值触发的具体线值。
5. 证伪记录（防后续误引）：`upstash/agent-prompts` **gh 实证 404 不存在**；「messier 提示词仓库」搜索未命中真实对象；「codeg」字面最接近 clauxel/codeg-agent-workspace-mcp（⭐0，存疑）——截图提及项目均未核实到可靠实体，计划期不得作为依据引用。

## 来源清单

- 小黑盒文章：《我给所有 AI Agent 写了一份「入职手册」》 [分享链接](https://www.xiaoheihe.cn/app/bbs/link/3cbc726e1c25)（web_reader 全文抓取）
- [BMAD-METHOD docs: Skills and Agents](https://docs.bmad-method.org/reference/skills-and-agents/) / [GitHub](https://github.com/bmad-code-org/BMAD-METHOD)
- [MetaGPT GitHub](https://github.com/foundationagents/metagpt) / [ICLR 2024 论文](https://arxiv.org/html/2308.00352v6)
- [Roo Code: Using Modes](https://roocodeinc.github.io/Roo-Code/basic-usage/using-modes)
- [Claude Code Docs: Subagents](https://code.claude.com/docs/en/agent-sdk/subagents)
- [obra/superpowers README](https://github.com/obra/superpowers)（gh api 实测）
- 本地实证：`skill/shisan-xinuo-workflow/templates/agents/`（critic/risk-reviewer/security-auditor）、zcode-configuration-guide SKILL.md（Scopes 表）、20 个 SKILL.md 启发式扫描（脚本内嵌本档 §3 口径）
