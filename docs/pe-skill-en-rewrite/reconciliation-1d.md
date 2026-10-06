# 产品工程 Skill 英文重写 · 机制对账单（批 1d 验收硬项）

> 日期：2026-09-30 ｜ 方法：逐判据 ID 精确 grep 英文仓 + 双语九台 selftest 实跑
> 中文源（母仓 `skill/shisan-xinuo-product/` v0.2.7）零变更：九台 selftest 复验全 PASS（2026-09-30 实跑留痕）
> 英文仓：`C:/Users/zxc66/Desktop/产品工程Skill`（= github.com/zxc663/product-engineering-skill）

## A. scripts 九台 · 判据 ID 逐项指认

| 台 | zh 判据 ID | en 指认 | grep 证据 |
|---|---|---|---|
| registry-gate | MARK `registry:` 归因标记 | 同 | `MARK = "registry:"` ok |
| registry-gate | 基线模式（存量豁免/只拦新增） | 同 | `write_baseline` ok |
| registry-gate | 组件目录识别+三方件排除 | 同（COMPONENT_DIRS/EXCLUDE 集合） | selftest 6/6 |
| spec-trace-extract | 组件提取（测试/故事/证据排除） | 同（升级：路径段锚定，见 E-1） | selftest 含 TaskHistory 保留断言 |
| spec-trace-extract | 三类端点（decorator/Next route.ts/inline） | 同 | selftest ok2 |
| spec-trace-gate | T1 五段齐 | 同 | grep `T1 ` ok |
| spec-trace-gate | T2 evidence 禁占位语 | 同（BAD 词表英文化，见 B） | ok |
| spec-trace-gate | T3 四元组冗余 | 同 | ok |
| spec-trace-gate | T4 UI 孤儿 | 同（含「连带」标注 chained） | ok |
| spec-trace-gate | T5 死逻辑 | 同（含 chained） | ok |
| spec-trace-gate | T6 幽灵端点 | 同（URLISH 形判+localStorage 豁免+空清单语义） | ok |
| spec-trace-gate | 参数段归一化 `{id}`→`{}` | 同（`_norm`） | selftest ok7/ok8 |
| spec-trace-gate | `NONE(<reason>)` 纯展示声明 | 同 `NONE(<reason>)` | PURE_DISPLAY ok |
| a11y-gate | A1 img 无 alt | 同 | ok |
| a11y-gate | A2 表单控件无可访问名（label-for/包裹/hidden 豁免） | 同 | ok |
| a11y-gate | A3 交互元素空内容+纯符号 | 同（"bare symbol" 报文） | ok |
| a11y-gate | A3b 伪按钮无 role | 同 | ok |
| a11y-gate | A4 html 无 lang（含空值同罪） | 同 | ok |
| a11y-gate | 基线模式 | 同 | grep `write-baseline` ok |
| frontend-lint-gate | R1 内联样式 | 同 | ok |
| frontend-lint-gate | R2 硬编码色（css/`<style>`/meta/canvas 豁免） | 同 | selftest 全分支 |
| frontend-lint-gate | R3 console.* | 同（含 table/trace/dir/count） | ok |
| frontend-lint-gate | R4 空 catch（含可选绑定形态） | 同 | ok |
| frontend-lint-gate | R5 空态 warning | 同（形态 `[R5-W]`，zh 同款，各 1 处） | grep `R5-W` en=1 zh=1 |
| frontend-lint-gate | 基线模式 | 同 | grep `write-baseline` ok |
| l0-l5-gate | L0-C1/C4/C5/C6/C7/C10/C12/C13 | 同 | grep 逐 ID ok |
| l0-l5-gate | L0-C11（单值性，复合形态 `L0-C1/C11`） | 同（zh 同形态，各 2 处） | grep `C1/C11` en=2 zh=2 |
| l0-l5-gate | L5-C1/C3/C5/C6/C10/C11 | 同 | grep 逐 ID ok |
| l0-l5-gate | 三件套豁免（local_nav_exempt） | 同 | selftest ok1 |
| l0-l5-gate | 反向变异 LL1(数字 ns)/LL2(字符串 false)/LL3(字符串 0)/LL4(文本引用不崩)/F5(键缺失) | 同（命名去批号，变异全保留） | selftest ok5/ok6/ok7/ok8 |
| product-object-gate | P1 定义存在性 | 同 | ok |
| product-object-gate | P2 主功能唯一性 | 同 | ok |
| product-object-gate | P3 层级声明+上游三形态（file:/brief:/adjudicated:） | 同 | ok |
| product-object-gate | P4 可运营性 + P4-W 维度覆盖 | 同 | selftest pw1/pw2 |
| product-object-gate | 反向 PO1-PO4 | 同（变异全保留） | selftest |
| statechart-gate | C1 initial / C2 死端 / C3 可达 / C4 错误态出路 / C5 guardDesc / C6 引用完整 | 同（英文报文） | grep 逐条 ok |
| statechart-gate | C7 双向对账（正向缺边/反向多边） | 同 | selftest ok7a/ok7b |
| statechart-gate | 错误态三源（声明 ∪ 名启发 ∪ 契约提及） | 同 | selftest c4_decl |
| statechart-gate | contract_c7_hint 跑法提醒（不 FAIL） | 同 | selftest ok_hint |
| statechart-gate | markdown recovery 探测（标题共现+恢复列表头+目录排除+上限） | 同（词表英文化，见 B） | selftest ok_p1/p2/p3 |
| statechart-gate | dict 无 target=内部转换放行 | 同 | 逻辑零变更 |
| usage-probe | HINTS 提及计数/时间窗/衰减警告 | 同（词表英文化，见 B） | selftest 计数=2 |

## B. 判定词表 · 新英文判定域（非翻译，selftest 即验收）

| 词表 | zh 域 | en 新域 | 验收 |
|---|---|---|---|
| TIME_WINDOW | 2026年/Q1/30天/年底前 | ISO 日期、Q[1-4]、N days/weeks/months/years、end of Q4/2026、by <月> <年>、within N days | selftest 正反样本 |
| METRIC_FORM | 提升/达到/占比/率/人均 | improve/reduce/reach/ratio/rate/percent/count/per user + 数字/比较符 | 同 |
| VANITY | 总注册/累计…次数/时长 | total users/downloads/views；cumulative × (count/executions/clicks/views/hours/time)；**质量指标（cumulative success rate）放行** | selftest ok9 双向 |
| JOB_FORM | CJK 三段+在/当 | verb+object+while/during/when/for/without | 逻辑同构 |
| ROLES 枚举 | 核心任务/业务操作/辅助/高阶/风险操作 | core-task/business-op/auxiliary/advanced/risky | 与 references/product-object.md 角色表一致 |
| BANNED_VERB | 展示/显示（含括号包裹） | display/show/present（含词尾变体+括号/引号包裹） | selftest PO2 |
| OPER_DIM | 来源/后台/权限/备份/恢复/兜底/删除/导出 | source/admin/backend/permissions/access/backup/restore/fallback/delete/export | selftest pw1/pw2 |
| BAD 占位语 | 无/未验证/TODO/待补/暂无 | none/not verified/unverified/todo/tbd/pending/placeholder/n/a/-/— | selftest T2 |
| RECOVERY_TITLE | 异常/恢复×状态/转换 共现 | recover*/error*/fail*/exception*/retry*/fallback* × state*/transition*/matrix/table 共现 | selftest p1/p2/p3（复数形态已修：`exception\w*`） |
| RECOVERY_COL | 恢复/recovery | recover(y/ies) | selftest p3 |
| EMPTY_BRANCH | 暂无/no-data | no items/no data/no records/nothing yet/empty-state/NoData | selftest ok7w |

## C. references 9 件指认

| 件 | zh 实质 | en 指认 |
|---|---|---|
| anti-excuses.md | 12 条成对反借口+三触发机制 | 12 行成对表全保留（上游归属列保留）；danger words/level misplacement/channel attribution 三机制 |
| capability-map.md | 12 行路由矩阵+harvest 规则 | 同构重写 |
| contract-schema.md | Interaction/Gate/Evidence 三契约+使用时机 | 同构（母架构占位：只实现 Interaction） |
| decision-ledger.md | 行 schema/准入五问/写回时机 | 同构；旧项目裁决实录整块弃，换 2 条标注 illustrative 的示例行 |
| interaction-bridge.md | 三合法/五类盘点/六问表/翻译表 schema/双底双顶/放弃三问 | 同构（Nielsen 0.1/1/10s 保留） |
| judgement-table.md | 42 行 11 域+风险档位矩阵 | 42 行重编号 11 域（zh 编号混乱有重复已修）；行内引用改「域+规则名」；2 条 scoping rules 从弃判例中抽出保留（「≥3 态」只计交互态；追加功能按新能力风险定档） |
| layer-stack.md | L0-L10 层级表/三段式层级门/四纪律/拦截表 | 同构（拦截表 11 行、机器可查 P3 保留） |
| product-object.md | 六问/闭环八组/可运营性清单/角色表/JSON schema | 同构（layers 三选一 file:/brief:/adjudicated:） |
| registry.md | 行 schema/双视图/入库标记/淘汰纪律/基线模式 | 同构；zh 尾部单项目实测数据行弃（史叙） |

## D. SKILL.md 结构指认

frontmatter（name=product-engineering/version=1.0.0/license/homepage）→ §1 when to use → §2 eight-step run（0a layer gate + 0b six questions → inventory → six questions → statechart C1-C7 → matrix → acceptance preconditions → implement → acceptance trio）→ §3 dual floors dual ceilings → §4 mandatory list **10 项**（zh 九项+statechart 转正后并入，候选/转正叙事全剥）→ §5 anti-excuses 9 条内联 → §6 artifacts & nine gates 一行一角色 → §7 four tiers → §8 quick reference + Field rules 9 条（工程内容保留、判例出处剥离）。

## E. en 版顺手修复与新护栏（zh 潜伏 bug 不回改——中文源零变更约束）

- **E-1** spec-trace-extract/a11y/frontend-lint 排除升级路径段锚定（zh 裸子串曾把 TaskHistory.vue 整文件误排除）；en selftest 增 TaskHistory 保留断言。
- **E-2** a11y-gate frag 规范化 `r'\s+'`（zh `r'\\s+'` 笔误永不匹配）。
- **E-3** statechart RECOVERY_TITLE 语义词组词尾容忍（首版 `exception\b` 漏 "exceptions"，selftest 抓到后修为 `exception\w*`——重写版 selftest 抓重写版 bug 的实证）。

## F. 刻意不迁移项（clean-room 边界）

候选 N→转正叙事、转正证据链、日期定稿注、试金石/路测轮次出处、本机路径指针（D:/q、docs/reverse-injection）、decision-ledger 旧项目裁决实录、judgement-table 档位判例叙述（真规则已抽入 scoping rules）、registry 尾部单项目实测数据。规则本体+≤1 句为什么之外一律不入正文。

## G. 双语 selftest 终态（2026-09-30 实跑）

- en 九台（Desktop 仓）：9/9 PASS，exit=0
- zh 九台（母仓）：9/9 PASS，exit=0（未动证明）
