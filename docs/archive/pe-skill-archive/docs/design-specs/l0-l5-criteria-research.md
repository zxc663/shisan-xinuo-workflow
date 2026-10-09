# L0 / L5 判据调研档（候选池，非最终条款）

> 2026-09-24 调研子代理产出。用途：为层×判据矩阵（`docs/layer-judgement-matrix.md`）的 **L0 产品目标层（合格线缺失）** 与 **L5 信息架构层（整层空白）** 提供候选判据池。**本档是调研档（design-specs），不是条款**——最终蒸馏、定版、配门禁由主会话裁决。
> 层栈语义依据=本体 `references/layer-stack.md`：L0=「为什么做这个产品/模块、要达成什么结果」，铁律「**L0 只检查不生产**」（PE≠PI）；L5=「信息怎么组织、功能放哪、用户怎么找到」，本包定位=「只做上游检查，不冒充实现」。
> 判据风格对齐既有矩阵：**可数清单+判定程序+【机/半/人】记号**；每条带出处；「脚本能判的→建议脚本形态，纯原则→标人工裁决域」。

---

## ① 调研对象与方法

**调研对象**（每法=一句话机理+可抽取判定条目）：

| # | 方法论 | 一句话机理 | 对 L0/L5 的可抽取物 |
|---|---|---|---|
| 1 | North Star Framework（Amplitude） | 用**单一北极星指标**统一团队，下挂少量**输入指标**（metric tree），缝合客户语言/产品语言/业务语言 | 单值性、输入指标数量与结构、指标命名练习 |
| 2 | OKR（Doerr《Measure What Matters》/ whatmatters.com） | 目标（定性、鼓舞）+关键结果（**可度量可验证**、有截止期）把意图钉成二值判定 | O/KR 质量形容词、KR 二值判定测试、3-5 数量纪律、反模式 |
| 3 | Jobs-to-be-Done（Ulwick/Strategyn） | 需求表述为**无方案的稳定任务**：动词+宾语+情境限定词，跨技术与年代稳定 | job statement 语法判据、solution-free 判据 |
| 4 | HEART + Goals-Signals-Metrics（Google re:Work） | 先定用户层目标，再把目标翻译成信号、信号翻译成度量 | 目标→信号→度量的**三层链路存在性**判据 |
| 5 | 产品目标反模式（Ries 可行动指标、OKR 反模式、North Star 陷阱） | 坏目标的共同形态：不可度量/不可行动/无变化意图/虚荣指标 | 反模式检查清单（黑名单形态） |
| 6 | IA 四系统（Rosenfeld《Information Architecture》） | 信息架构=组织/标签/导航/搜索四系统的整体设计 | 四系统**存在性**判据（档级可查） |
| 7 | 八条原则（Dan Brown 2010） | IA 设计的八条原则（对象/选择/披露/示例/前门/多重分类/聚焦导航/生长） | 可二值化条目（前门/聚焦导航/多重分类）+人工裁决域条目 |
| 8 | 卡片分类（NN/g） | 用用户分组行为揭示心智模型（生成法，非验收法） | 样本量/卡数纪律、open/closed/hybrid 选型判据 |
| 9 | 导航深度广度与「三击规则」实证（Katz & Byrne 2003；Larson & Czerwinski 1998；NN/g 2019 驳文） | 点击数不是放弃原因，**迷路/失信心才是**；中等广度浅层级优于深窄层级 | 否决「≤3 clicks」硬判据；替代=迷路信号可数项 |
| 10 | Tree testing（NN/g） | 对纯层级树做「找得到吗」实测：成功率、直达性（directness）、耗时 | 实测判据形态：预定义正确答案（叶子）、两指标报告 |

**方法**：WebSearch+WebFetch 直取一手源（引文以 WebFetch 摘录为准）；**出处三档信心级**：
- **A**=一手原文直读引文（本轮实际抓到正文）
- **B**=搜索结果确认存在（标题/日期/域名/多源交叉），正文未直读
- **C**=二手转述（来源明确但非原文）

**网络限制披露**（影响引用形态，如实标注）：`usabilitynews.org`（Katz & Byrne 原文）与 `rework.withgoogle.com`（HEART 官方）从本机网络不可达（curl 000，2026-09-24 实测）；`amplitude.com` 的 Playbook 章节正文为 JS 渲染不可直读（仅 introduction 可达）。相关条目降为 B/C 级并标注，未冒充一手。

---

## ② L0 产品目标层 · 候选判据表

**检查对象**：产品的目标陈述工件（目标文档/北极星声明/OKR 文档/产品对象定义中的目标段）。**检查立场**：只查「陈述成什么样算过关」（合格线），不生产目标、不裁决目标对错（对错=产品决策侧）。

### L0-A 组 · 结构判据（North Star 系）

| 编号 | 判据名 | 判定程序（可数） | 出处 | 信心级 | 建议门禁形态 |
|---|---|---|---|---|---|
| L0-C1 | **目标单值性** | 目标工件中「主结果声明」恰好 **1** 条；≥2 条且无显式主次声明 → fail；=0 → fail（即既有「是否被陈述」的加强） | Amplitude「a single metric that unites teams」；框架连接 customer/product/business 三语言 | A | 【机】grep 主指标声明句式计数（句式表需主会话定）；歧义→人工裁决 |
| L0-C2 | **输入指标存在性** | 主指标下挂 **3-5** 条输入指标（Amplitude 惯例区间）；<3 或 >5 → warning（不 fail，须显式裁决） | Amplitude North Star Playbook（章节正文不可达，结构经 `amplitude.com/north-star` 与 `/books/north-star.md` 确认；「3-5 inputs」为该框架通行口径） | B | 【机】树结构计数（指标列表条目数） |
| L0-C3 | **三语言缝合** | 陈述中同时含①用户价值词（用户能…）与②业务结果词（收入/留存/成本…）两类词汇；缺任一类 → warning | Amplitude：北极星的价值=「connecting those different perspectives」（customer/product/business 语言） | A | 【半】词表 grep 可初筛；语义归属人审 |
| L0-C4 | **KR 可二值判定** | 每条关键结果须能改写成「达成/未达成」二值（原文测试："You either meet a Key Result's requirements or you don't — there is no gray area"）；抽 N 条，不可二值者计数 >0 → fail | whatmatters.com（Doerr 官方站）OKR FAQ | A | 【半】数值+比较词形可 grep（≥/≤/=/N%+时间窗）；语义二值性人审 |
| L0-C5 | **时间窗存在** | 每条 KR 含明确截止期（原文："specific, time-bound"）；缺时间窗计数 >0 → fail | whatmatters.com | A | 【机】日期/季度正则匹配 |
| L0-C6 | **数量纪律** | 单目标下 KR 条数 ∈ **3-5**（原文："typically written with an Objective at the top and 3-5 supporting Key Results below it"）；越界 → warning | whatmatters.com | A | 【机】计数 |

### L0-B 组 · 锚定判据（JTBD / HEART 系）

| 编号 | 判据名 | 判定程序（可数） | 出处 | 信心级 | 建议门禁形态 |
|---|---|---|---|---|---|
| L0-C7 | **目标-任务锚定** | 目标陈述能回溯到 ≥1 条 job statement（动词+宾语+情境限定词三段齐全；三段缺一 → 该条无效；有效条数 =0 → fail） | Strategyn JTBD 模板："Verb + object of the verb + contextual clarifier"（例句 "Listen to music while commuting to work."） | A | 【半】三段句式可 grep 初筛；语义人审 |
| L0-C8 | **解自由性（solution-free）** | job statement 不含具体方案/技术词（判据=该陈述「survive across solutions, technologies, and decades」——换掉当前实现后陈述仍成立）；每条检 1 次，含方案词 → warning | Strategyn："Features come and go; Jobs don't" | A | 【人】（方案词表不可穷举；可给启发式词表降人工量） |
| L0-C9 | **GSM 链路存在性** | 目标→信号→度量三层链：每层目标下 signal 数 ≥1，每个 signal 下 metric 数 ≥1；任一断链 → fail（HEART 原文口径：不要求五类全覆盖，按目标选择性填三层） | Google re:Work HEART（Goals-Signals-Metrics process）——官方站本机不可达，流程经多二手源交叉确认 | B/C | 【半】链路结构计数可机检（档内分层小节）；层级语义映射人审 |

### L0-C 组 · 反模式黑名单（Ries / OKR / North Star 陷阱）

| 编号 | 判据名 | 判定程序（可数） | 出处 | 信心级 | 建议门禁形态 |
|---|---|---|---|---|---|
| L0-C10 | **无目标** | 目标工件缺失或空段 → fail（既有矩阵已覆盖「是否被陈述」，此处并入合格线序列） | 矩阵 L0 行现状（`layer-judgement-matrix.md:9`） | A | 【机】工件存在性（与 product-object-gate P1 同形态） |
| L0-C11 | **多目标无主次** | ≥2 条主结果声明且无主次/分层标记 → fail（与 L0-C1 同门，双写因形态不同：C1 查陈述句式，C11 查工件结构） | Amplitude 单值性+OKR 单 Objective 结构 | A/B | 【机】结构计数 |
| L0-C12 | **不可度量主指标** | 主指标无度量口径（无数值/无比较基准）→ fail | Ries：度量「must include actionable metrics that can demonstrate cause and effect」 | A | 【半】口径字段存在性可机检；因果性人审 |
| L0-C13 | **虚荣指标作主指标** | 主指标为「只升不降的存量累计型」（总注册/总下载/总 PV）→ warning + 人工裁决（基础设施类产品累计量可合法） | Ries《The Lean Startup》vanity/actionable metrics 之辨（术语出自书第 7 章；官方 principles 页确认 actionable metrics 须「demonstrate cause and effect」） | A/B | 【人】（词形黑名单 grep 只产 warning 不 fail，防误报） |
| L0-C14 | **无变化意图（business-as-usual）** | KR 全部可由「维持现状」达成 → fail（原文反模式："OKRs should aim for change above maintaining the status quo"）；**sandbagging**（KR 达成无悬念）→ warning | whatmatters.com | A | 【人】（「无悬念」不可机判；「维持现状」可半自动初筛） |

---

## ③ L5 信息架构层 · 候选判据表

**检查对象**：IA 档/导航定义/路由与导航组件/实测报告。**检查立场**：本包 L5 只做「上游检查」（能力→架构的可判定映射与结构底线），**不生产 IA 方案**（母架构 Structure=v2 领域）——判据设计成「存在性/一致性/实测报告存在性」三轨，避免越界到设计。

### L5-A 组 · 四系统存在性（Rosenfeld 系，档级可查）

| 编号 | 判据名 | 判定程序（可数） | 出处 | 信心级 | 建议门禁形态 |
|---|---|---|---|---|---|
| L5-C1 | **组织系统声明** | IA 档中存在组织系统声明（分类主维度：主题/任务/用户/格式/时间 五选）；主维度 ≥2 且无显式主次 → warning（对应 Brown「focused navigation」） | IxDF（转述 Rosenfeld/Morville/Arango 4th ed.）："organization systems — how information is categorized and structured, allowing users to predict where to find information" | A | 【半】小节存在性可机检；维度归属人审 |
| L5-C2 | **标签一致性** | 抽样 N 个导航标签（建议 N≥10）：同义异形（同一对象两种叫法）计数 =0；≠0 → fail | IxDF："labeling systems — the way information and navigation options are represented to make them understandable and findable" | A | 【半】与术语表对账可脚本；同义判定人审（可先做精确重复+大小写变体机检） |
| L5-C3 | **导航三件套** | ①全局导航存在 ②局部导航存在（或显式豁免）③当前位置指示（面包屑/高亮，wayfinding）存在——三项计数；缺项且无豁免 → fail | IxDF："navigation systems — guide users… understand their location… and how to reach their desired information"；Brown 前门原则（≥半数访问不经首页 → 每页须可见全站结构） | A | 【机】组件/路由级 grep（导航组件存在性+面包屑组件引用） |
| L5-C4 | **搜索系统存在性** | 内容/列表型页面（页面数 >S₀，阈值主会话定）存在搜索入口，或缺省搜索有显式豁免声明；缺且无豁免 → fail | IxDF："search systems — to allow users to find specific information quickly"（内容密集型站点尤其） | A | 【机】条件触发检查（路由类型→组件存在性），豁免=账本行 |

### L5-B 组 · 八原则可二值化条目（Brown 系）

> 八条原则中只有一部分能二值化；**不可二值化者明确归人工裁决域**，不硬造机器判据（对齐门禁哲学）。

| 编号 | 判据名 | 判定程序（可数） | 出处 | 信心级 | 建议门禁形态 |
|---|---|---|---|---|---|
| L5-C5 | **前门可达（front doors）** | 全部路由可达全局导航（逐路由检查含全局导航组件的计数=路由总数）；有孤页 → fail | Brown 原则五（principles.design 全文）："Assume at least half of visitors arrive via a page other than the homepage" | A | 【机】路由清单×导航组件引用矩阵 |
| L5-C6 | **多重分类（multiple classification）** | 查找路径类型计数 ≥2（如：浏览导航+搜索、或+标签筛选）；=1 → warning | Brown 原则六："Provide users with several ways to browse and classify the site's content" | A | 【机】路径类型存在性计数 |
| L5-C7 | **聚焦导航（focused navigation）** | 单一导航分组内不混异类对象（抽样导航分组，混类计数=0）；≠0 → warning | Brown 原则七："Don't mix apples and oranges in your navigation scheme" | A | 【人】（混类判定=语义；可按 registry 对象类型做初筛） |
| L5-C8 | **选择有度（choices）** | 单屏并列选项数超过阈值 T₀（T₀ 项目自定并留痕，**不设行业硬数**）→ warning + 显式裁决，不直接 fail | Brown 原则二："meaningful choices… tied to a specific task"（manageable，无固定数） | A | 【机+人】选项计数可机；阈值裁决留痕 |
| L5-C9 | **生长预留（growth）** | IA 档含「新内容/新能力往哪挂」的扩展声明（存在性检查）；缺失 → warning | Brown 原则八："Assume today's content is only a small fraction of what it will become tomorrow" | A | 【半】小节存在性 |
| — | 对象/披露/示例三原则 | 生命周期管理、渐进披露、类别示例——**全部人工裁决域**（无法列可数程序，明确不配脚本） | Brown 原则一/三/四（principles.design 全文） | A | 【人】（评审清单形态，不做门禁） |

### L5-C 组 · 实证与实测判据（3 次点击争议 + tree testing / 卡片分类）

| 编号 | 判据名 | 判定程序（可数） | 出处 | 信心级 | 建议门禁形态 |
|---|---|---|---|---|---|
| L5-C10 | **迷路信号替代三击** | 逐任务/逐页检查迷路信号可数项：①死端页（无出链无导航）计数=0 ②当前位置可辨（与 L5-C3③ 共用）③每步「下一步在哪」有候选。点击数**不作为判据** | Katz & Byrne 2003（3-click 广 vs 5-click 窄：成功率/满意度无差异，用户坚持至 25 clicks；时间与挫败由任务失败与导航结构驱动）；NN/g 2019 驳文「The 3-Click Rule for Navigation Is False」（2019-08-11）；NN/g：用户放弃因迷路/失信心而非点击数 | B（原文站不可达，多源交叉） | 【机】死端检测（页面级出链计数——与 L7 statechart-gate 无死端 C 系**同构可复用**） |
| L5-C11 | **tree testing 报告存在性** | 关键导航任务（清单主会话定，建议 ≥3 任务）各有一份 tree testing 报告，报告含：①预定义正确答案（**须为叶子节点**）②成功率 ③directness（直达性）三要素；缺任务或缺要素 → warning（实测属人工执行域，门禁只查工件存在性与要素齐备） | NN/g tree testing："Tells you if users were able to find the 'correct' answer, any other categories users selected, how long it took them"；directness="proxy for how confident users are in a particular path"；**NN/g 未给公认数值阈值**——阈值须项目自定留痕 | A | 【半】报告工件+要素齐备可机检（与 P3 工件存在性同形态）；阈值裁决留痕 |
| L5-C12 | **多归属显式化（polyhierarchy）** | 同一资源被 ≥2 分类归属时，IA 档有显式声明（可由 tree testing 验证必要性）；未声明 → warning | NN/g tree testing：可测 "whether duplicate placements (socks under both Footwear and Accessories) are actually needed" | A | 【半】归属矩阵对账可机检；必要性人审 |
| L5-C13 | **卡片分类方法纪律**（方法判据，非产品判据） | 执行卡片分类时：卡数 30-50；定性 ≥15 人、定量 30-50 人；验证既有 IA 用 tree testing 替代 closed sort（NN/g 明示建议）；混合式（hybrid）不推荐（预定义类目产生偏置） | NN/g card sorting（全部原文直读） | A | 【人】（方法记录审查；产物归 L5-C1/C2 的输入） |

**L5 关键调研结论（主会话蒸馏前必读）**：**行业不存在公认的最优深度/广度数值判据**——三击规则被实证否决（Katz & Byrne 2003；NN/g 2019），Larson & Czerwinski 1998 仅支持「中广浅层优于深窄」的方向性结论（B 级），tree testing 官方口径不设数值阈值。因此 L5 的机器化空间在**结构与工件判据**（A/C 两组），**发现性质量只能靠实测判据形态**（C11），诚实标注而不造数值假判据。

---

## ④ 与既有矩阵的缝合建议

1. **L0 行替换**（`docs/layer-judgement-matrix.md:9`）：`【空】` → `【半】L0-C1/C4/C5/C10 可机检（单值计数、KR 二值词形、时间窗正则、工件存在性）；C7/C8/C9/C13/C14 人工裁决域`。出口产物=`产品目标合格线报告`（目标工件逐条判定结果）。合格线=机检项全过 + 人工项无 fail。**边界保持**：仍不生产目标（PE≠PI），不合格 → 停下向产品决策侧要，不代拟。
2. **L5 行替换**（`layer-judgement-matrix.md:14`）：`【空】` → `【半】三轨：结构轨 L5-C3/C5/C6 可机检（导航/前门/路径计数，grep 组件与路由）；档轨 L5-C1/C2/C4 半自动；实测轨 L5-C10/C11 查报告存在性`。人工裁决域=focused navigation 混类、choices 阈值、对象/披露/示例三原则。出口产物=`IA 结构检查行 + 实测报告存在性表`。
3. **与 product-object-gate（P1-P4）同构复用**：L0-C10（工件存在性）、L5-C11（报告存在性+要素齐备）与 P3「工件声明+引用存在性」门禁形态完全同构，实现上可挂同一脚本骨架；候选 14 的工件级层声明推广时把 L0 目标工件与 L5 IA 档纳入声明面。
4. **与 statechart-gate（C1-C7）复用**：L5-C10 的死端检测与 L7 无死端判据同构（页面级出链 vs 状态级出边）——同一判定器两个粒度，避免写两套。
5. **触发拦截表增行**（`references/layer-stack.md` §3）：「放哪一栏/怎么分类/菜单叫什么」行已有 L5 追问，可在追问后加「IA 档四系统声明齐吗（L5-C1..C4）」作为自答优先的读档项；L0 触发行（「要不要做 X」的根问）可在 L0-L4 全扫描时带 L0-C1..C6 合格线。
6. **最便宜缺口排序**（对齐矩阵「最便宜的两个缺口」方法论）：①L0 陈述结构计数（纯正则/计数，零依赖）→ ②L5-C3/C5 导航与孤页机检（grep 路由与组件）→ ③L5-C11 报告存在性（工件检查，P3 形态）→ ④L0-C4 二值判定（半自动，语义人审工作量最大，最后做）。
7. **判据编号预留下游空间**：L0/L5 均留 C15+ 空位；实测轨判据未来若升格为自动走查（矩阵 L10 行「浏览器级证据」欠账闭合时），L5-C11 可升级为自动 tree-walk 形态。

---

## ⑤ 被否候选与理由

| 被否候选 | 否决理由 | 处置 |
|---|---|---|
| **「≤3 次点击」作为 L5 硬判据** | 实证否决：Katz & Byrne 2003（3 vs 5 clicks 无差异、坚持 25 clicks）；NN/g 2019 驳文；用户放弃的因果是迷路/失信心非点击数 | 改用 L5-C10 迷路信号（死端+位置可辨），点击数不入判据 |
| **Miller 7±2 作为导航项数硬上限** | 工作记忆容量与菜单项数是不同构念，IA 实证无固定值支持；Brown 原文亦只要求 manageable | L5-C8 阈值项目自定+显式裁决（warning 不 fail） |
| **HEART 五类全覆盖作为 L0 判据** | HEART 是 UX 度量框架（用户体验层），且原文明示按目标选择性填；L0 是产品目标层，全查=层错位 | 只取 GSM 链路存在性（L0-C9），五类不强制 |
| **OKR 3-5 数量直接作 L0 fail 线** | L0 目标工件≠OKR 文档；数量是惯例非质量本质，硬 fail 会误伤单指标极简目标 | 降为 warning（L0-C6）；保留 KR 二值性与时间窗两条形态判据为 fail 线（L0-C4/C5） |
| **卡片分类作为 L5 验收判据** | NN/g 原文明示：卡片分类是揭示心智模型的**生成法**，验收 IA 应使用 tree testing（closed sort 也不如 tree testing） | 只收方法纪律（L5-C13），验收走 L5-C11 |
| **「北极星必须是比率不是计数」入表** | 该判据在 Amplitude Playbook 章节正文中，但章节 JS 渲染不可直读——一手引文缺失，**不写无法核验的条款** | 列为待验证（见未解决问题 1），主会话可人工读原文后裁决 |
| **虚荣指标词形机检直接 fail** | 累计型指标对基础设施/平台类产品可合法；词形黑名单误报率高 | L5 同款问题防在先：L0-C13 仅 warning+人工裁决 |
| **为 L5 定「最优深度=N 层」数值判据** | 行业无公认数值（见 §3 结论）；造数=假判据 | 结构轨+实测轨替代，数值留项目自定 |

---

## 未解决问题清单（移交主会话）

1. Amplitude Playbook Chapter 2/4 正文（checklist 原文、输入指标性质、陷阱清单）SPA 不可直读——「3-5 inputs」「rate not count」等细节未第一手核验，L0-C2 区间与被否候选第 6 条待人工读原文定版。
2. `usabilitynews.org`（Katz & Byrne 2003）与 `rework.withgoogle.com`（HEART 官方）本机网络不可达——两处只能以 B/C 级引用，若需一手引文须换网络环境。
3. NN/g 三击驳文（2019-08-11）存在性经搜索确认，但精确 URL slug 未验证（`/articles/three-click-rule/` 实测 404）——引用时建议以「NN/g, 2019, nngroup.com」域名级标注。
4. **L0 合格线的边界裁决**：C4（KR 二值性）、C5（时间窗）是否越界到「生产目标」——建议主会话按「检查陈述形态 vs 产出内容」划线：形态合规性=本包可查，内容对错=产品决策侧。
5. tree testing 阈值缺省值（成功率/directness 多少算过）：行业无公认数，是「项目自定留痕」还是给一个保守缺省（如成功率 ≥80% 作 warning 线）——需主会话定政策。
6. L5 判据与母架构 Structure=v2 的归属切分：本文 A/C 组哪些进本包门禁、哪些只留档给 v2——需对照 `docs/product-architecture.md` 裁决。

---

*出处汇总（本轮实际核验的一手可达源）：whatmatters.com OKR FAQ｜strategyn.com JTBD 模板｜principles.design 八原则｜ixdf.org IA 四系统（转述 Rosenfeld/Morville/Arango 4th ed., O'Reilly 2015）｜nngroup.com tree testing 与 card sorting 两文｜theleanstartup.com/principles｜amplitude.com/north-star 与 /books/north-star（introduction）。B/C 级源与不可达披露见 §①。*
