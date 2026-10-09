# D 组调研 · 同类相似项目（外部竞品/同类品）

> 研读日期 2026-09-21。目的：校验产品工程 Skill 的差异化是否成立，吸收同类已验证的做法。

## 1. Nutlope/hallmark（Together AI）——最直接同类

**定位**：给 Claude Code/Cursor/Codex 的反 AI-slop 设计技能——「refuses to look AI-generated」。
**机制**：
- **四动词产品化**：默认 build（选宏观结构+套规则集+交稿前跑 slop test）/ `hallmark audit <target>`（对既有代码按反模式打分，出 punch list 不改码）/ `hallmark redesign`（抛结构保内容与品牌重建）/ `hallmark study <截图|URL>`（提取心仪设计 DNA：宏观结构/字体配对/色彩锚，拒像素克隆，可产出 portable `design.md` 交接给其他 AI 工具）。
- **20 预置主题 + 57 道 slop-test gates + pre-emit self-critique**（交付前自我批评一轮）；「refuses the on-distribution defaults every LLM was trained into」（拒绝训练分布里的默认审美）。
- Custom 分支：brief 带无主题可配的创意意图时从零设计，同一 57 门禁，协议在 `custom-theme.md`。
- 结构：SKILL.md + references/ + docs/recipes.md（实例）+ docs/study-examples.md；安装 `npx skills add nutlope/hallmark`；每页 CSS 注释盖 macrostructure 戳。
**对照我们**：强=视觉 slop 防护、主题分发、**audit/study 动词化命令**（audit=对既有代码打分出清单，正是 registry-gate 的产品化形态；study=从人类欣赏的设计提取 DNA 再落地，是「审美单源=人类投票」的工程化）；**缺**=项目既有组件注册表、跨会话裁决账本、假理想功能/逻辑链检查、中文与工作流对接。

## 2. vercel-labs/web-interface-guidelines（862★）

**定位**：Web 界面构建准则的活文档（100+ 条，七类：Interactions/Animations/Layout/Content/Forms/Performance/Design + Vercel-specific 品牌分节）；配套 `web-design-guidelines` skill——**扫描 UI 代码产出 file:line findings**（违反条目定位到行）；另发 AGENTS.md 供项目集成使 agent 生成时即遵守。
**与本项目判定表直接互补的条目**（此前清单没有的）：
- 「No dead ends. Every screen offers a next step or recovery path.」——空态跳转按钮缺陷的业界原文表述
- 「All states designed. Empty, sparse, dense, & error states.」——六态的近亲表述
- 「Error messages guide the exit」+ 反例正例对照（"Invalid API key"→"…Generate a new key in your account settings."）——错误出路的标准范式
- 「Loading buttons 保留原标签」「spinner 150-300ms 延迟+300-500ms 最短可见防闪烁」「Confirm destructive actions / Undo 安全窗」「URL as state / deep-link everything」「Never `transition: all`」「tabular-nums」「不单靠颜色传状态（冗余状态线索）」「Links are links（导航禁用 button/div）」「Don't pre-disable submit（允许提交空表单暴露校验反馈）」
- **结构验证**：Vercel-specific 单独分节把「品牌选择」与「通用准则」隔离——与 taste-skill em-dash 教训同构，**验证我们判定表「业界共识/本 Skill 风格」两栏分离的设计**。
**对照我们**：强=静态指南密度与条目文风（粗体原则+一句做法）、file:line findings 输出、AGENTS.md 集成；**缺**=项目绑定（注册表/账本）、假功能检查、跨会话机制。

## 3. 分发与目录生态
awesome-claude-skills 三大目录（BehiSecc / travisvn ≈8.8k★ / ComposioHQ）+ rohitg00/awesome-claude-code-toolkit（135 agents/35+ skills）=同类技能的发现渠道与素材矿；skillselion/skillhub 等第三方目录已收录 vercel 的 web-design-guidelines。

## 4. 差异化校验结论（四增量全部仍然成立，且得到强化）

| 我们的增量 | 同类现状 | 结论 |
|---|---|---|
| 组件注册表+出处链 | anti-ui-slop 只有一句「extend them」原则；shadcn registry 是通用分发非项目绑定 | 成立，且 registry-gate 可借 hallmark `audit` 命令形态产品化 |
| 跨会话裁决账本（写回协议） | 全场空白（hallmark/vercel 均无状态） | 成立，最独特 |
| 假理想功能/逻辑链门禁 | 仅 anti-ui-slop 一句 inert interactions Finish 检查，无系统化 | 成立，先发优势明显 |
| 与工作流纪律对接（GATE/复述/能力检索） | 无人做 agent 纪律与设计品味的合流 | 成立 |
| 新增借鉴 | hallmark 四动词（audit/study 特别值得）、vercel file:line findings 输出与 AGENTS.md 集成、vercel 条目文风与 20+ 条互补判定、No dead ends 等表述 | 并入判定表与命令设计 |

## 5. 对方向档的修订（增补进 direction.md 的三点）
1. 判定表新增「业界共识」来源：vercel-labs/web-interface-guidelines（100+ 条，七类）——与 ux-feature-design/ui-ux-pro-max 并列为出处源。
2. 命令形态借鉴 hallmark：门禁不只是脚本，做成 `audit`（出 punch list）/`study`（从人类指定设计提取 DNA 进注册表）两类动词。
3. 交付物可携带「portable design.md」交接形态（hallmark study 同款）——跨工具/跨会话交接的现成范式。

## 6. DietrichGebert/ponytail 上游原仓库深读（2026-09-21，用户直供链接）

**定位**：本机 ponytail Skill（B 组已蒸馏其规则文本；本机=单文件 SKILL.md 6.7KB，~/.zcode/skills，无 ~/.agents 副本）的上游完整产品——「Makes your AI agent think like the laziest senior dev in the room. The best code is the code you never wrote.」规则文本只是它的一小部分；上游=规则+hooks 注入架构+命令族+基准+账本。**本机副本蒸馏时漏掉的恰是最值钱的四件**：

**基准方法论（同类中首个给 Skill 做对照实验的）**：真实 Claude Code headless 会话编辑真实仓库（tiangolo/full-stack-fastapi-template，FastAPI+React），12 张 feature ticket，同 agent 带/不带 Skill 对照，n=4，**以 git diff 计分**：ponytail LOC -54%/tokens -22%/cost -20%/time -27%/安全 100%；对照组 caveman（纯简短散文）LOC -20% 但 tokens +7%；裸「YAGNI+一行流」提示 LOC -33% 但**安全掉到 95%**（砍掉了 guard）——证明安全性来自阶梯的白名单条款（验证/错误处理/安全/a11y 永不在砍削名单），光喊极简口号不给白名单就会掉安全。最大削减恰落在真实 over-build 陷阱（date picker 404→23 行、color picker 287→23 行，均以原生 input 替代组件）；已极简的代码削减≈0。**修正史**：早期 single-shot 基准报 80-94% 被 issue #126 挑战（裸模型基线用散文填充答案=对话基线伪影），公开修正为 agentic 数字并保留旧数据标注 artifact——诚实测量的活样本，与本 Skill「不假实现」红线同构。

**七级阶梯的精确形态**（比本机副本多两条关键条款）：①阶梯在理解问题**之后**运行而非代替理解——「先读要改的代码、追真实流，再选档」；「Lazy about the solution, never about reading」（对方案懒，对阅读绝不懒）②规则从来不是「最少 token」，是「只写任务需要的，且永不砍验证/错误处理/安全/无障碍」——代码小因为必要，不是 golf。

**产品形态**：
- **hooks always-on 注入**：UserPromptSubmit 每轮注入规则集+PreToolUse 注入 subagent（PONYTAIL_SUBAGENT_MATCHER 正则控范围）+模式 lite/full/ultra/off——**不靠 description 概率触发=衰减链第 1 级（不触发）与第 4 级（仪式化）的已验证工程解**；20 平台适配矩阵（AGENTS.md 为所有平台的指令兜底）。
- **六命令族**：`/ponytail-review`（diff 查过度工程，交回删除清单）/`audit`（全仓不只 diff）/`debt`（收获 ponytail: 注释进 ledger，「防 later 变 never」）/`gain`（测量记分板）/`help`。
- **ponytail: 注释**：`<!-- ponytail: browser has one -->`——代码内一行标注「为什么没写」，debt 命令定期收割入账本=**裁决账本的最小实现样例**（写回协议的轻量形态）。
- **check-rule-copies.js**：多平台规则副本一致性门禁（改规则文本跑 npm test 即查漂移）——多副本治理的工程化。

**对 §4 差异化表的修正**：「跨会话裁决账本全场空白」需弱化——ponytail-debt 是账本（债务语义：记「为何没写」待收割）；我们的 decision-ledger 是裁决语义（记「为何这么定」直接复用）。语义不同但机制位已被占，差异化表述改为「账本机制位已有债务先例，裁决语义+设计域仍空白」。

**对本 Skill 的四条吸收（已并入 direction.md §八末）**：①三重检验升级为 ponytail 式 agentic 对照实测（真实 diff 计分+无 Skill 对照组+安全项单列）；②decision-ledger 写回采纳「ponytail: 注释+定期 harvest」轻量形态；③判定表补「阅读义务」条款（阶梯/查表在理解问题之后运行，禁跳过阅读直选档）；④caveman×ponytail 正交先例（管说的 Skill×管建的 Skill 零重叠可叠加）=工作流 Skill×产品工程 Skill 双架构的市场验证。

## 7. 联通层定向补扫（2026-09-21，中心对象改联通层后的未扫象限）

**7.1 github/spec-kit（深读，官方 spec-driven development 工具包）**——与本项目最同构的业界形态：
- 三过程：SDD（`constitution`→`specify`→`plan`→`tasks`→`implement`→`converge`）／bug-fix（`assess`→`fix`→`test`，verdict 三态 verified/partial/failed，「**Missing verification is not a successful fix**」）／idea-assess（intake→research→define→shape→decide，go/clarify/kill）。宪法每项目一次，spec→converge 每特性一轮。
- 同构点：what/why 先于 how=§八时序纪律的官方版；**constitution=厂规的项目宪法形态**；`converge`（实现→向 spec 收敛循环直到报 Converged）=spec-trace 正向门禁的同类；工件全部落盘 `.specify/`（抗压缩）；clarify/checklists/consistency 为可选质量门；多 agent（Copilot/Claude Code/Gemini CLI）。
- 缺口（差异化仍立）：通用 spec 无交互域内容（六问/六态/双底双顶）；收敛单向（spec→code），无反向发明检测（code→spec「每个元素可回指功能行」）；无品味维度；无裁决账本。
- 借鉴：converge 命名与循环形态；verdict 三态输出格式（门禁结果不二值化的中间态标注）；bug-fix 的 assess/fix/test 分离=治「顺手改」。

**7.2 Figma Code Connect（官方，figma/code-connect）**——联通层「组件卡」的业界标准形态：映射文件把 Figma 设计组件↔仓库代码组件+属性级映射，Dev Mode 出准确片段，Figma MCP 集成后喂给 AI 代码生成。**证明「映射文件」模式可行且已被市场接受**；层级差异：Code Connect=设计↔代码组件级静态映射，我们=功能语义↔交互行为级行为契约——互补不重叠。registry 组件卡=其本地化翻版。

**7.3 设计系统 lint 门禁（业界成熟形态，inline-style-gate 的先例群）**：Atlassian 官方 ESLint plugin（设计系统 props/用法规则）、eslint-plugin-panda `no-hardcoded-color`、案例研究（ofriperetz.dev）：4 条 lint 规则扫 401 组件出 144 违规、**每处颜色破坏都源自粘贴的代码**。证明：①P4 零魔数/inline-style 门禁=业界共识非我们发明；②「违规溯源到复制粘贴」与「发明视觉」病灶同源。

**7.4 可用性启发式×agent（学术前沿）**：arXiv 2026-05 论文以 computer-use agents 视角重审 Nielsen 10 启发式；ResearchGate 2025-06 同向。**「真渲染取证+启发式判定」路线有学术共振**；Nielsen 10 启发式应列为判定表「业界共识」栏出处源（与 vercel 准则并列）。

**结论：联通层组合仍无人占**——spec-kit 管通用 spec 不管交互域；Code Connect 管组件映射不管行为契约；design lint 管样式不管逻辑链；学术在验证路线但无工件化。我们的「交互域契约（六问六态双底双顶）+双向追溯+裁决账本」组合空白依旧。本轮无 direction 修订，仅出处源增补（Nielsen 启发式）。
