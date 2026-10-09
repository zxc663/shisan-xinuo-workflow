# A 组蒸馏 · 设计品味系（7 Skill）

> 蒸馏纪律：只收代码级可操作机制，每条带出处；判例形态=问题→候选→裁决→理由。研读日期 2026-09-21。

### taste-skill / design-taste-frontend（C:\Users\zxc66\.zcode\skills\taste-skill\SKILL.md，1207 行）
- 一句话定位：Anti-slop 前端技能——先读 brief 推断设计方向，三旋钮（VARIANCE/MOTION/DENSITY）参数化全部规则，60+ 项机械 Pre-Flight 清单作出码前最后一道门。
- 核心机制：Brief 推断先于一切（Design Read 一行输出，歧义只问一个问题，:13-39）；三旋钮门控全部规则+信号→旋钮推断表（:47-76）；真 vs 假设计系统映射（企业级 brief 必装官方包 Fluent/Carbon/Polaris，「Do not invent CSS for things that have an official package」:86-118）；AI-Tell 判定表+二值化禁令（em-dash 零容忍，:595-701）；Pre-Flight 60+ 项逐格打勾，任一格不可诚实打勾即未完成（:910-979）。
- 可蒸馏增量：
  - 判定表：CTA 同一意图全页唯一标签（:227）；hero 文本元素 ≤4 且禁 trust-strip（:239-245）；bento 格子数=内容数（:250）；eyebrow ≤ ceil(节数/3)（:253-257）；「Motion claimed = motion shown」（:963）；loading/empty/error 三态强制（:971）
  - 门禁：机械可数检查可脚本化；「单选框任一不可诚实打勾即 Fail」收尾措辞
  - 注册表字段：Block Library frontmatter=`dial_compatibility{variance,motion,density}/when_to_use/not_for/stack`（:863-876），每 block 独立文件、可独立渲染、必过 Pre-Flight（:888-892）
  - 反借口：「模型历史上无视 used sparingly——改写成零容忍二元规则」（:701 直接明说）；「Never assume a library exists，先查 package.json」（:157）
  - 附赠：重设计协议「先审计再动手」+「永不静默改动 URL/导航标签/表单字段名/法务文案」（:794-831）
- 问题域映射：①强（2.A 表=业界共识→官方包查询表）②强（One system per project；禁手抄官方 CSS；禁导官方 tokens 再覆盖 90%，:102-104）③中（交互全状态循环）④中（motion claimed=shown 是雏形）。

### anti-ui-slop（C:\Users\zxc66\.agents\skills\anti-ui-slop\SKILL.md，59 行）
- 一句话定位：薄壳调度技能——「产品既有组件/tokens 永远高于本 skill」为纲，按场景加载唯一 playbook，收尾渲染检查一次。
- 核心机制：产品优先级条款（brief/既有 UI/组件/tokens 永远 outrank 本 skill，:37）；前置强制盘点既有组件/tokens/视觉语言「extend them instead of inventing」（:27-28）；单一 playbook 加载制（6 个 reference 二选一，:41-50）；硬 Finish gate（渲染检查 clipping/overlap/变形/不可达/inert interactions，:57-58）；真实性条款「Never claim it is connected without an actual host result」（:33）。
- 可蒸馏增量：门禁「inert interactions（惰性交互）」=④官方措辞；render-and-inspect-once 单轮验证制；前置盘点清单=注册表使用入口；反借口「未经宿主实际返回不得声称已连接」。
- 问题域映射：②强（extend not invent）④强（inert interactions+不得虚假声称）①③弱。

### emil-design-eng（C:\Users\zxc66\.agents\skills\emil-design-eng\SKILL.md，675 行）
- 一句话定位：Emil Kowalski 设计工程哲学——动画四问决策框架+组件微细节+性能规则，强制 Before/After/Why 三列表格输出审查结果。
- 核心机制：审查必须落 markdown 表 |Before|After|Why| 禁清单式（:40-60）；动画四问（该不该动按频率 100+/天永不动→目的→easing→时长 UI<300ms，:62-145）；键盘触发动作永不加动画（:77-79）；微细节判定表（:215-288）；收尾 Review Checklist 10 行 issue→fix 全表（:658-675）。
- 可蒸馏增量（判定表可直接搬）：`transition: all`→指定属性；`scale(0)`→`scale(0.95)+opacity`；UI 元素 ease-in→ease-out；popover origin→触发器（modal 豁免）；键盘动作有动画→删；>300ms→150-250ms；hover 无 media query→补 `@media (hover:hover)`；进出同速→出场快于进场（:658-675 全表）。
- 反借口：「目的是好看+用户高频看到→不加动画」（:93）；"It feels creative is NOT a reason"。
- 问题域映射：③强（感知性能/`:active` 反馈/可中断动画=反假快正面技术）①弱（个人哲学非共识表）②无关④弱。

### frontend-design（C:\Users\zxc66\.agents\skills\frontend-design\SKILL.md，56 行，Anthropic 官方）
- 一句话定位：设计负责人技能——先钉主题/受众/页面唯一职责，两遍式（先 token 方案→对照 brief 自批→再写码），主打「别像模板货」。
- 核心机制：先钉主题（:13）；AI 三大默认样式集群校准（cream+serif+terracotta / near-black+acid-green / broadsheet=「合法但非选择」，:31）；两遍式流程+「换个相似 prompt 会不会得到同样产出」自批（:33-35）；signature element 大胆只花一处（:43）；UX 写作纪律（:49-55）。
- 可蒸馏增量：判定表：按钮动词与后续 toast/状态文案同词根（:51）；错误文案三要素「出了什么+怎么修」（:53）；结构编号只在真有序时用（:21）。门禁想法：「与假想 baseline 对比自批」反模板元门禁。反借口：「brief 原话永远赢，包括它点名要三大默认样式之一时」（:31 末）。
- 问题域映射：③中（错误出路+文案一致）①弱②无关④弱。

### impeccable（C:\Users\zxc66\.agents\skills\impeccable\SKILL.md，80 行+40 reference+100+ 脚本；与 .zcode 副本 diff 一致）
- 一句话定位：设计总控平台 v4——24 子命令路由+四模式+脚本化反模式检测器（hooks 编辑后自动跑）+有界验证收尾。
- 核心机制：有界验证（一轮批量检查→一批修复→最多一轮确认→停止，:12）；Setup 脚本链（context.mjs 加载 PRODUCT.md/DESIGN.md，:16-18）；**编辑后自动门禁**（hooks 跑 detector：antipattern registry 与 regex/static-html/browser/visual 多引擎分离+inline-ignores，:76）；四模式按「访客成功长什么样」选（:26-33）；craft-floor「defaults, not bans」（清单默认禁但 brief 可赢回，唯一硬禁 eyebrow）。
- 可蒸馏增量：门禁脚本架构蓝本（registry 与引擎分离+hook 自动跑+doctor/staleness 漂移管理）；注册表机制（extract/document 命令=「从既有代码盘点组件入库」流程化）；判定表（同尺寸 icon+标题+文字卡片=懒容器、嵌套卡片永远错、渐变文字、emoji 当图标、monospace 装技术感、硬偏移阴影）；反借口（"Reaching for one when the axis is free means you were not deciding"）。
- 问题域映射：②强（extract/document）④强（detector+harden+bounded verify）①中③中。

### ux-feature-design（C:\Users\zxc66\.zcode\skills\ux-feature-design\SKILL.md，110 行；与 .agents 副本一致）
- 一句话定位：中文功能体验设计/审查——每条规则标注研究出处+自动获取优先+六态齐全+可评分审查+用户原声库验收。
- 核心机制：权威依据表 11 项全带出处（Baymard/NNGroup/GOV.UK/Nielsen/AntD…，:10-27）；自动获取十二类+决策树（:31,47-58）；六态强制禁「转圈到底/点了没反应」（:33-34）；一票否决反面模式七条（JSON 化配置/手填 ID/逗号分隔多值/重复配置入口/placeholder 当标签/错误无出路/本可自动获取却手填，:94-104）；评分审查（旅程30+表单40+状态20+人性化10=100 分，:78,109）。
- 可蒸馏增量：判定表「错误无出路」（:103）=③直接判定项；「点了没反应」专项+click-path-audit（:74,91）=④直接判定项；字段表必含「自动获取方式」列（:62,108）；**user-voices.md 用户原声库**（「还要我自己查 IP/域名？」「这一坨 JSON 是给人填的吗？」）+验收标准=「修复后这句话还会不会出现」（:58）——反借口表与门禁二合一的最强参照。
- 问题域映射：①强（出处化规则）③强④强②弱。

### ui-ux-pro-max（C:\Users\zxc66\.agents\skills\ui-ux-pro-max\SKILL.md，215 行+data/ 22 CSV+scripts/）
- 一句话定位：本地可检索设计情报库——79 样式/192 配色/119 UX 准则/22 技术栈全落 CSV+Python 检索脚本+设计系统可持久化。
- 核心机制：十类规则优先级表（Accessibility CRITICAL→Charts LOW，:16-31）；**data/ux-guidelines.csv 十列 schema**=`No,Category,Issue,Platform,Description,Do,Don't,Code Example Good,Code Example Bad,Severity`——判定表即用字段设计；`--persist` 生成 MASTER.md+pages 覆盖，已存在跳过、`--force` 须显式授权防静默丢弃决策（:88-110）；stack 检测强制（:71）；零结果不编造（:169-172）；数据契约测试套件（scripts/tests/ 9 文件）。
- 问题域映射：①强（119 条 Do/Don't 正反例=机器可检索的共识）②中③部分④部分。

## A 组总蒸馏

**最强 3 机制**：
1. **ux-feature-design 的「出处化规则+一票否决+用户原声验收」**——四问题域命中率最高；原声库把反借口表和验收门禁合二为一。
2. **ui-ux-pro-max+impeccable 的「三层落地工程」**——CSV 十列判定表 schema+MASTER.md 账本（--force 显式授权）+antipattern registry 多引擎检测器架构=三层结构现成蓝本。
3. **taste-skill 的「二值化禁令+机械可数门禁」**——模型无视 "used sparingly"，必须零容忍二元规则；把主观品味翻译成可数检查（计数/差集）是「判定表→门禁脚本」的方法论桥梁。

**重叠**：AI-tell 禁令三处重复（taste/impeccable/frontend-design）→合并一张判定表去重；反借口条款散落四处→集中成表配驳斥语。

**冲突与裁决**：①纯风格禁令（em-dash）不可冒充共识→判定表分「业界共识」与「本 Skill 风格」两栏；②taste 60 项全跑 vs impeccable 有界验证→门禁设计为一次性脚本批量跑；③anti-ui-slop「既有约束赢」vs taste「反默认」→优先级：有既有组件/设计系统走保守复用（②），greenfield 才启用反模板。
