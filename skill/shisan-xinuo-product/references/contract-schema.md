# contract-schema · 契约 schema（Interaction / Gate / Evidence 三件）

> 2026-09-23 修正（用户裁决）。目的：把散落工件（六问/statechart/spec-trace/门禁/证据/账本）钉成**可被 Agent 消费、执行、验证、继承的契约**——有 schema 才是规范层，否则只是一堆方法论。
> **硬层/软层分界（本文件核心约束）**：硬层=机器可判定字段（态/转换/权限/恢复/门禁输入输出/证据存在性）——可 exit 1；软层=理由与权衡（意图/被否候选/裁决）——只要求可追溯，落在 `decision-ledger.md`。**禁全链 JSON 化**：为填表而填表=Token 爆炸，会杀死采用意愿。

## 1. Interaction Contract（交互契约 · 硬层）

落点：`docs/contracts/<feature>.json`（statechart 为源，本契约引用之；表格/矩阵是渲染视图）。

| 字段 | 类型 | 说明 | 判定 |
|---|---|---|---|
| feature | string | 功能句（谁/什么场景/完成什么） | 非空 |
| scope | 档0-档3 | §7 档位（由 judgement-table §风险档位判定） | 枚举 |
| promise | string[] | 承诺清单（每个交互元素一句「点了会发生什么」） | 非空 |
| six_questions | object | ①input ②timing ③success ④failure{prevent,recover,exit} ⑤undo{window,cost} ⑥persistence | **无空格**（缺项=交互债） |
| states / transitions / initial | — | 同 statechart（≥3 态；单态小件豁免） | statechart-gate |
| permissions | string[] | 谁可触发每个转换（有权限语义时必填） | 档3 必填 |
| recovery | object[] | 每个错误态的出路行，字段=`{state, action, target, note?}`（拼写即契约，门禁按此读） | 档3 必填；**C7 正向对账**：每行必须命中 statechart 对应转换（缺边=承诺落空，exit 1） |
| non_error_failures | object[] | 非错误态命名的失败出路白名单（同字段；如 `loading --LOAD_FAIL--> empty`） | 可选；**C7 反向**豁免登记——显式登记而非沉默豁免 |
| soft_ref | path | 指向软层（意图/权衡/裁决→decision-ledger 条目） | 存在性 |

## 2. Gate Contract（门禁契约 · 硬层）

落点：`scripts/*-gate.py` 的 `--help` 与 `--selftest` 输出即契约（每个门禁必须自述）。

| 字段 | 说明 |
|---|---|
| gate_id | 门禁名（registry / statechart / spec-trace / inline-style / dead-binding / a11y…） |
| scope | 触发档位（档0-档3，见 judgement-table §风险档位） |
| check | 判定内容一句（必须机器可判定） |
| input | 输入形态（路径 / 文件 / JSON） |
| output | pass/block + 退出码（0/1）——**接受谈判的判据不是门禁** |
| evidence_required | 是否要求证据存在性（取证类门禁） |
| selftest | `--selftest` 两态（拦截态 + 放行态） |

## 3. Evidence Contract（证据契约 · 硬层）

落点：设计档/交付报告的「联通行」证据列 + GATE `cmd/exit/files` 三挂靠。

| 字段 | 说明 |
|---|---|
| feature / claim | 被验证的承诺条目（对应 Interaction Contract 行） |
| evidence_type | render（截图）/ dom（DOM dump）/ command（可重跑命令+退出码）/ log |
| artifact | 证据路径（仓库内）或命令原文 |
| produced_by / verified_at | 生产方（会话/门禁）与时间戳 |
| validity | 失效条件——**改动该面即失效**，旧证据不覆盖新改动 |
| verdict | pass / fail / 未验证（未验证必须显式，禁默认通过） |

## 4. 母架构占位（未实现，防冒名）

Product Contracts 全链 = **Intent → Scope → Structure → Interaction → Runtime → Implementation → Verification**。本包**只实现 Interaction**（Gate/Evidence 为其支撑件）；其余域全部未实现——引用时须声明「未实现」，不得以方法论冒充。
迭代次序（用户 2026-09-23 裁决）：第二版 = Intent/Structure（IA）；第三版 = Runtime；Verification 随证据体系生长。**本文件只描述已落地的三件；未落地域不写字段**（防为填表而填表）。

## 5. 使用时机

- **任何档位开工前先过层级门**（`references/layer-stack.md`）：定位层→检上游→放行/回补。
- **有 recovery 行的契约**：跑 `statechart-gate.py --file <sc.json> --contract <contract.json>` 启用 C7 双向对账（缺边=承诺落空／多边=未登记发明，双向 exit 1；实证=`docs/reverse-injection/EVIDENCE.md`）。
- **档1**：口答，不落文件。
- **档2**：Interaction Contract 落 JSON（statechart 源）+ Gate/Evidence 走通。
- **档3**：三件全落 + recovery 行 + runtime evidence + regression。
- 契约与实现的漂移=缺陷（写了没按/按了没写都是**假联通**）——由 spec-trace 双向门禁拦截。
