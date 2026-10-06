# jz-03-clinic · SCORECARD（八门禁试金石记分）

- 卡：医院挂号（资源冲突预约 / 多页 IA / 前后端混合）｜夹具=14 文件｜首跑 2026-09-30
- 诚实性：夹具作者=门禁作者（同源污染，方向性 n=1）；所有 exit 为真实运行回显。

## 一、门禁结果（首跑 → E2 回流后复跑）

| 门禁 | 首跑 | 回流后 | 命中明细 |
|---|---|---|---|
| ① product-object | FAIL 3F | 同 | P2 双核心+main_function 不一致（gate 含一致性子检查=正面发现）；P3 L4 file:docs/spec.md 悬空 ✓ |
| ② l0-l5 | FAIL 2F+1W+1W' | 同 | L0-C5 KR 缺时间窗 ×2 ✓；W=C6 KR 条数 2<3；W'=IA 档不可解析告警（gate 对畸形结构降级为「按未提供处理」——见逃逸 E8） |
| ③ statechart | FAIL 5F | 同 | C5 guard 无说明 ✓；C2 conflict/cancelled 死端 ×2 ✓（cancelled 见 E1）；C4 conflict 错误态无恢复出路 ✓；C7 契约承诺 conflict→RETRY→browsing 落空 ✓ |
| ④ usage-probe | N/A | N/A | 夹具无会话面 |
| ⑤ registry | FAIL 6F | 同 | 6 组件全未归因 ✓ |
| ⑥ frontend-lint | FAIL +2W | 同 | R1/R2 内联样式+硬编码色+console 全接；R5-W ×2 ✓（MyAppointmentList 无空态=设计；ScheduleTable 见 E3） |
| ⑦ spec-trace | FAIL 7F | FAIL 5F | T2 TODO ✓；T4 WaitingList 孤儿 ✓；**T5+T6 成对**：`POST /apointments` 拼写错=T6 ×2 + 真 `POST /appointments` 无人消费=T5 ✓——归一化后消除 `{id}`≠`{appt_id}` 双杀误报对（E2） |
| ⑧ a11y | FAIL 2F | 同 | **A3 纯符号 ✓（✕ 取消按钮——jz-02 回流件第三域再验证）**；**A3b `<td @click>` 时段格子伪按钮（新形态命中，td∈NON_INTERACTIVE）** |

- 植入→抓到：全部植入缺陷均被抓；回流前唯一误报形态=路径参数名不一致双杀（已回流修复）。

## 二、逃逸分析

| # | 逃逸/发现 | 裁决 |
|---|---|---|
| E1 | C2 报 `cancelled` 死端 | 判定域：C2 有 `type:"final"` 豁免（声明边界）；本域下「取消成功回执屏无回浏览出路」经走查确认真缺陷（contract 有回执 UI 但态机无出口转换）——gate 正确，非假阳 |
| E2 | bindings 手写 `{id}` vs 后端声明 `{appt_id}` 被同时报 T5 死逻辑+T6 幽灵（语义同端点双杀） | **真缺口→已回流 T5/T6 参数段归一化**（`_norm`：`{…}`→`{}` 后比对；自测 ok7 参数变体放行+ok8 端点真消失仍拦；jz-03 复跑 7→5 全真、jz-01/jz-02 回归零变化） |
| E3 | R5-W 引用行选静态 `th v-for`（表头） | 启发式粒度取舍：文件级 W 方向正确（同文件 weekSlots 数据列表确无空分支）；纯静态 v-for 文件属低频形态且 warning 级人工裁决——记录不改 |
| E4 | brief「字要大」老年可读性 | a11y 机器子集边界外（A1-A4+A3b=名称/alt/lang/伪按钮；字号/对比度=axe 完整审计人工域）；夹具 18-20px 散见无 token——判定域记录 |
| E5 | 候补 join 纯本地无后端 | 组件级粒度设计边界：T4 查组件∈bindings，不查组件内动作↔后端逐动作对账（行为级追溯=人工域）——记录 |
| E6 | 并发抢号无原子扣减（bookAppointment 直 append） | 后端运行时正确性域外（测试域）记录 |
| E7 | P2 双报含 main_function 一致性子检查 | 正面发现：主功能与核心任务不一致独立成项——无缺口 |
| E8 | IA 档畸形时 gate 降级「按未提供处理」告警 | 设计取舍：fail-open+显式告警优于崩溃；但畸形 IA 可掩盖结构缺陷（本卡 IA 实际合规未被深查）——候选池：IA 解析失败应列**待人工复核**项而非普通 W |

## 三、回流清单（本卡）

- T5/T6 路径参数段归一化（spec-trace-gate）：`_norm` + 归一化集合比对 + 自测 ok7/ok8——jz-03 误报对消除、jz-01/jz-02 回归零变化、selftest 8/8。

## 四、复跑

见 README.md §复跑命令。

## 五、回流后补注（2026-09-30，jz-04 周期触发）

l0-l5 fail-open 回流施工（IA 档不可解析 FAIL + tree_tests 文本引用不崩检）后本卡复跑：退出码不变（L0-C5×2 植入仍在），但原被解析崩溃吞掉的 IA 检查复活——首跑漏检的设计植入 `/my` 死端页现被 L5-C10 捕获，`location` 键名不符 schema（应为 `location_indicator`）被 L5-C3 捕获。E8 逃逸就此闭环：fail-open 已改 fail-loud，候选池「待人工复核」提案以更强形式（exit 1）落地。本卡夹具保持首跑历史原样不改。
