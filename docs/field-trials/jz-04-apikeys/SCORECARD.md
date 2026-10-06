# jz-04-apikeys · SCORECARD（WS2 周期 #4）

- 卡号：jz-04｜领域：API Key 管理（安全域 / reveal-once 生命周期 / 双页）
- 判分协议：同前三卡（README §判分协议）——exit 真值 + 逃逸两分 + 回流带正反自测 + n=1 方向性
- 首跑时间：2026-09-30 04:3x（回流后复跑同日）

## 一、八门禁首跑结果

| # | 门禁 | exit | findings | 判读 |
|---|------|------|----------|------|
| ① | product-object | 0 | W P4-W×1 | 设计内（可运营性单维→warn） |
| ② | l0-l5 | 0→**回流后仍 0** | 首跑 W「IA 档不可解析按未提供处理」×1→回流后 W C1/C6/C11×3 | **首跑暴露 fail-open（见 E0）** |
| ③ | statechart（含 C7 对账） | 1 | 6 项 | 植入全接（见二） |
| ④ | spec-trace | 1 | 3 项 | 植入全接+归一化零误报 |
| ⑤ | registry | 1 | 5×缺归因头 | 已知夹具形态（四卡一致，非新逃逸） |
| ⑥ | frontend-lint | 0 | 0 | 正对照：KeyTable v-else 空态未误报 R5-W ✓ |
| ⑦ | a11y | 1 | A3b×1 | 植入命中 |
| ⑧ | usage-probe | — | — | 本卡不跑（退役机制探针，非卡面门禁） |

## 二、植入→命中对照（设计植入 7 缺陷全接 = 7/7）

| 植入缺陷 | 门禁判据 | 结果 |
|----------|----------|------|
| creating.SUBMIT guard 无 guardDesc | C5 | ✓ |
| active.VIEW_USAGE → 不存在的 `usage_detail` | C6 | ✓ |
| rate_limited：`type:error` 无出边、无入口边、契约承诺 WAIT→active 落空 | C2+C3+C4+C7 **四透镜同击一缺陷簇** | ✓ |
| revoked 正确声明 `type:final` | C2 豁免梯度 | ✓ 正对照 |
| bindings evidence=「待补」 | T2 占位语 | ✓ |
| CopyButton.vue 存在但零绑定行 | T4 UI 孤儿 | ✓（extract 自动提取后比对） |
| `POST /keys/rotate` 幽灵端点（**轮换承诺未实现=安全域逃逸**） | T6 | ✓ |
| `DELETE /keys/{id}` vs 后端 `{key_id}` 参数名变体 | T5/T6 归一化 | ✓ **零误报（jz-03 回流第三域回归成立）** |
| RevealModal 遮罩 `div @click` 无 role | A3b | ✓ |
| P 门（定义/主功能/层级/可运营）设计 PASS | P1-P4 | ✓ exit 0 |
| L 门（KR 时间窗/条数/IA）设计 PASS | L0/L5 | ✓ 回流后 exit 0（3 warn 方向正确） |

## 三、逃逸分析（两分裁决）

- **E0（真缺口→已回流）**：l0-l5 IA 档不可解析 **fail-open**——`tree_tests` 为字符串时 `for t in tt` 逐字符迭代→`t.get` AttributeError→外层 except 吞掉→**整个 IA 检查按「未提供」静默跳过**（L5-C1/C3/C5/C6/C10/C11 全盲），仅一条 warning。与 goal 侧不对称（L0-C10 工件不可解析=FAIL）。jz-03 E8 候选池 + jz-04 独立复现 = **双击晋升回流**。
- **E1（候选池）**：错误态无显式入口边被 C3 拦——错误态常态由运行时事件（HTTP 429）进入，态机「错误态入口约定」缺省形态未定。本卡判真建模缺口（没说清 429 时 UI 进什么态），但豁免约定 vs 强制显式化两立均通 → 入候选池待第三卡定方向。
- **E2（判定域内）**：reveal-once 丢弃语义——用户关弹窗未复制明文则密钥永远不可恢复，态机/契约均无此路径，gate 静默（结构合法）。领域语义评审域（statechart-gate 能力边界已声明：结构检查≠语义评审）。记录为产品发现。
  - **周期#12 清单项落地+走查演练 ✅**：interaction-bridge §4「放弃路径三问」对 revealed 态实走（出边仅 ACK→active）：①关闭放弃无出路建模命中三问①；③reveal-once 关闭即永久丢弃无警示命中三问③——**清单项双问命中本卡 E2 原缺陷**，走查演练验证成立。
- **E3（判定域内）**：RevealModal 无焦点陷阱/aria-live——a11y 机器子集边界，axe 人工域。
- **E4（判定域内）**：客户端存储形安全反模式（若 bindings 写 `localStorage`）T6 按 URL 形豁免——安全语义归 security-auditor 角色。
- **E5（已知形态）**：registry 5×缺归因头=夹具不带 `registry: source=` 头，四卡一致，非新逃逸。

## 四、回流清单（本卡）

**l0-l5-gate.py 三处**（jz-03 E8 + jz-04 双击晋升）：
1. `tree_tests` 字符串引用形态：不再逐字符迭代崩溃，降「文本引用（不可机判要素）」提示，不触发缺报告警告；
2. IA 档在档不可解析：warn+放行 → **fails+exit 1**（对齐 goal 侧 L0-C10 语义，fail-loud）；
3. selftest 增 LL-4 反向变异（文本引用不崩 + 其余 L5 检查不被吞），返回条件纳入 ok8。
- 负对照样本：`product/ia-broken.sample.json`（坏 JSON）→ exit=1 FAIL 复跑命令：`python $S/l0-l5-gate.py --goal $F/product/goal.json --ia $F/product/ia-broken.sample.json`
- 九台 selftest 全 PASS；四卡交叉回归：jz-01/jz-02 零漂移（jz-02 L5-C3 与首跑记录一致）；jz-03 退出码不变但**原被吞的 IA 检查复活**——首跑漏检的设计植入 `/my` 死端页现被 L5-C10 捕获（jz-03 SCORECARD §五补注）。
- 承载点同步：SKILL §67 l0-l5 行。
- 夹具修正：jz-04 ia.json `location`→`location_indicator`（键名不符 schema 曾被解析崩溃掩盖）；jz-03 夹具保持首跑历史原样。

## 五、夹具教训

- **夹具先读 schema（jz-02 教训复用成功）**：本卡写 statechart/spec-trace 植入前先读两台门禁源码，植入全部按真实判据形态落——首跑即全命中零返工；但 ia.json 仍栽在键名（`location_indicator`），解析崩溃把键名错也一起吞了——**fail-open 掩盖的不止检查，还有夹具自身的瑕疵**。
- **管道吞退出码复踩**：`python … | tail` 后 `$?` 是 tail 的——回归取 exit 必须落文件或免管道。

## 六、复跑

见 README.md §复跑命令。
