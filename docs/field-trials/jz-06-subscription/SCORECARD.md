# jz-06-subscription · SCORECARD（WS2 周期 #6）

- 卡号：jz-06｜领域：会员订阅（计费态机 / 支付失败恢复 / 账单）
- 判分协议：同前五卡（README §判分协议）
- 首跑时间：2026-09-30 05:0x（P2 措辞修正后复跑同日）

## 一、八门禁首跑结果

| # | 门禁 | exit | findings | 判读 |
|---|------|------|----------|------|
| ① | product-object | 首跑 1→修后 **0** | P2×2（夹具措辞瑕疵）→0 | P/L 面 PASS 正对照成立（六卡首个 P 面全绿） |
| ② | l0-l5 | 0 | 0 warn | 全绿正对照（KR 带窗/C13 干净/IA 合规） |
| ③ | statechart+contract | 1 | C7 正×1+**C7 反×2** | 植入命中且超预期（见二） |
| ④ | spec-trace | 1 | T1×1+T4×1+T5×2 | T1 连带如预期 + **计划外自获真发现**（见二） |
| ⑤ | registry | 1 | 4×缺归因头 | 已知夹具形态（六卡一致） |
| ⑥ | frontend-lint | 1 | R3×1 | 首域命中（console 调试残留） |
| ⑦ | a11y | 1 | A2×1 | 首域命中（裸 select 无可访问名） |
| ⑧ | usage-probe | — | — | 非卡面门禁 |

## 二、植入→命中对照

| 植入缺陷 | 门禁判据 | 结果 |
|----------|----------|------|
| contract recovery target=`past_due`（不存在的态；实际出边到 `support_hold`） | C7 正向 | ✓ 承诺落空（实际：support_hold） |
| payment_failed 出边 RETRY_PAY→active 未登记 recovery | C7 反向 | ✓ 未登记发明 |
| （同根连带）CONTACT_SUPPORT→support_hold 与 registered 三元组 target 不符 | C7 反向 | ✓ **一缺陷三透镜**（contract 写错一处→正向落空+反向两条全拦，预期外增益） |
| bindings 第 3 行缺 evidence 键 | T1 五段不齐 | ✓ 连带 T4 BillingPortal 孤儿+T5 cancel 死逻辑（T1 行 continue→不入 used 集，绑定关系不可信即连带，语义合理） |
| **计划外**：PlanPicker 硬编码方案列表，后端 `GET /plans` 无人消费 | T5 死逻辑 | ✓ **自获真发现**——非预植入，夹具自然形态被抓（试金石价值实证） |
| UpgradeButton `console.log` | R3 | ✓ 首域 |
| PlanPicker 裸 `<select>` 无 label/aria | A2 | ✓ 首域 |
| **正对照** P 面（purpose/唯一主功能/层级 upstream/operability 双维含 fallback） | P1-P4 | ✓ 修措辞后 exit 0 零警告 |
| **正对照** L 面（KR 带窗/可度量 north_star/IA 合规+结构化 tree_tests） | L0/L5 | ✓ 0 warn |
| **正对照** statechart 其余检查（C1-C6/C4/C2/C3） | statechart | ✓ 仅 C7 三发 |

## 三、逃逸分析（两分裁决）

- **E1（判定域内）**：T1 连带 T4/T5 是「行不可信则关系不可信」的一致设计——缺 evidence 的绑定行不计入 used 集，其组件/端点另行暴露为孤儿/死逻辑。复核语义合理（绑定未主张，关系即不存在），非误报；但**一份缺陷报三条**对使用者是噪声——候选池：T1 行可标注「连带孤儿/死逻辑由本行缺段引起」提示语（体验项非正确性项）。**周期#14 已兑现**：T4/T5 报文对缺段来源附「连带」标注（selftest +ok9 四面正反：缺段来源带标注／真孤儿 C9 与真死逻辑 GET /dead 不误标；六卡回归零漂移——本卡真实夹具正反同现：POST /subscription/cancel 带标注 vs 计划外自获 GET /plans 不带）。
- **E2（判定域内）**：C7 反向把 CONTACT_SUPPORT→support_hold 也报未登记——契约确实没登记这条真实存在的恢复边（夹具故意只登记一条错的）。gate 双向对账的语义=「错误态出边必须逐条登记」，本卡暴露了**写对 recovery 也得写全**的提示需求：报错文案已带「或漏写 recovery 行」提示语，判定充分，非缺口。
- **E3（已知形态）**：registry 4×缺归因头。
- **E4（记录）**：canceled 期末生效语义（取消后保活至 period_end）只在 contract ui 文案，态机无 period_end 过渡态——gate 结构层查不了（同前两卡：语义评审域）。产品发现记录。

## 四、回流清单（本卡）

**零回流（连续第二卡）**——候选池 +1（E1 T1 连带提示语，体验级）。夹具修正 1 处（P2 措辞一致，schema 教训的措辞变体：`main_function` 必须逐字出现在 capabilities[].name——「先抄合规形态」对策已含）。
六卡回归：本轮四卡 product-object jz-01/02/03=1、jz-04=0 零漂移（jz-05 复跑已验）。

## 五、夹具教训

- 措辞一致性：`main_function` 与核心 capability name 必须**逐字相同**（P2 双判据都查）——「先读 schema」教训的第四变体：不只是键名/形态，还有**跨字段措辞一致性**。
- 计划外发现的价值：夹具写成自然形态时（硬编码方案列表），gate 抓到的真死逻辑比预植入更有说服力——试金石不是考卷对答案，是真实形态的显微镜。

## 六、复跑

见 README.md §复跑命令。
