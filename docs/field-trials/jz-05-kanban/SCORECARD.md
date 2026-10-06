# jz-05-kanban · SCORECARD（WS2 周期 #5）

- 卡号：jz-05｜领域：团队看板（拖拽状态 / 错误态出路 / 纯展示 NONE 形态）
- 判分协议：同前四卡（README §判分协议）
- 首跑时间：2026-09-30 04:5x（object.json schema 修正后复跑同日）

## 一、八门禁首跑结果

| # | 门禁 | exit | findings | 判读 |
|---|------|------|----------|------|
| ① | product-object | 1 | 首跑 14 项→**修夹具后 P1×1**+W P4-W | P1 purpose 缺失=设计植入；首跑 14 项=夹具 schema 瑕疵（见五） |
| ② | l0-l5 | 0 | W C13×1 | 植入命中（虚荣主指标 warn 不 fail，selftest ok3 形态真实夹具复现）；IA 全绿（结构化 tree_tests 跨形态验证） |
| ③ | statechart+contract | **0** | 0 | **正对照成立（五卡首例全绿态机）**：guard 带 guardDesc 合规形态/blocked type:error 有出路/C7 双向一致 |
| ④ | spec-trace | 1 | T3×1 | 植入命中；`{task_id}`/`{id}` 第四域零误报；NONE(纯展示) 放行 |
| ⑤ | registry | 1 | 4×缺归因头 | 已知夹具形态（五卡一致） |
| ⑥ | frontend-lint | 1 | R1+R2+R4 | 三连全接（一行内联样式同吃 R1/R2 两判据） |
| ⑦ | a11y | 1 | A1×1 | **首域覆盖命中**（img 无 alt，前四卡未植入域） |
| ⑧ | usage-probe | — | — | 非卡面门禁（同前四卡） |

## 二、植入→命中对照（设计植入 7 缺陷全接 = 7/7）

| 植入缺陷 | 门禁判据 | 结果 |
|----------|----------|------|
| object.json 缺 purpose 键 | P1 存在性 | ✓ |
| goal north_star=「累计注册用户破万」 | L0-C13 虚荣词表（累计注册） | ✓ warn 不 fail |
| bindings 第 3/5 行同四元组重复 | T3 冗余行 | ✓ |
| TaskCard `<img>` 无 alt | A1 | ✓ |
| TaskCard `style="background: #f9f9f9"` | R1+R2 | ✓ 两判据各计 |
| TaskCard `catch (e) {}` | R4 空 catch | ✓ |
| **正对照** statechart+contract 全绿（C5 guardDesc/C4/C7 双向） | statechart | ✓ exit 0 |
| **正对照** ColumnHeader NONE(纯展示) | T6 豁免/used_backends 不收 | ✓ |
| **正对照** `{task_id}` vs `{id}` 参数变体 | T5/T6 归一化 | ✓ 零误报（第四域） |
| **正对照** ia.json 结构化 tree_tests 四要素齐 | L5-C11 | ✓ 无警告不崩（jz-04 回流第三形态验证） |

## 三、逃逸分析（两分裁决）

- **E1（判定域内）**：P4-W 词表口径——operability 已答「数据来源+谁管理」两维，仍报「仅覆盖 1 个管理维度」（词表按来源/权限/备份/恢复/fallback 族计数，「谁管理」不入表）。warn 级人工裁决域且方向正确（权限/备份/fallback 确未答），非缺口。
- **E2（判定域内→候选池双击苗头）**：**取消/中断转换未建模 gate 静默**——dragging 只有 DROP 出边；用户按 ESC/拖到列外松手（dragend≠drop）则 UI 状态泄漏，态机结构合法全绿。与 jz-04 E2（reveal-once 丢弃语义）**同族**：两卡连续曝「放弃/中断路径」是产品语义盲区而结构检查天然查不到 → 入候选池：取消/中断转换覆盖检查（语义评审清单项，非 checker 代码缺口）。
  - **周期#12 清单项落地+走查演练 ✅**：interaction-bridge §4 新增「放弃路径三问」（能否放弃/放弃后回落/放弃后果）——对 dragging 态实走：①ESC/列外松手无建模（guardDesc 仅覆盖「同列投放视为取消」，dragend≠drop 形态缺席）→ **三问①命中本卡 E2 原缺陷**，清单项有效性验证成立（人工域验证形态=走查演练非机检）。
- **E3（已知形态）**：registry 4×缺归因头=夹具不带 `registry: source=` 头，五卡一致。

## 四、回流清单（本卡）

**零回流**——五卡首例。前四卡七缺口回流后，本卡新域（A1/T3/C13/P1）未再曝 checker 真缺口；候选池语义层积累 +1（E2 取消/中断族）。
夹具修正 2 处（schema 对齐，非 gate 缺口）：object.json capabilities/operability/layers 三段首写凭记忆失真（14 误报）→ 抄 jz-04 合规形态重写；修正后 P1 唯一命中。
四卡回归：product-object jz-01/02/03 exit=1（植入仍在）jz-04 exit=0 零漂移。

## 五、夹具教训

- **「先读 schema」教训三犯**：jz-02（bindings 五段）/jz-04（ia 键名）/jz-05（object 三段）——每卡换新工件就忘。对策升级：**新工件首写前必须 Read 前卡同名片或 gate 源码**，凭记忆=必错；本卡已把 object.json 修正是「抄合规形态」而非「猜 schema」。
- fail-open 家族对照：jz-04 的 ia 崩溃把夹具瑕疵一起吞；本卡 product-object **fail-loud 报了 14 项**反而立刻暴露夹具 schema 瑕疵——两相对照，fail-loud 的诊断价值实证。

## 六、复跑

见 README.md §复跑命令。
