# site-01 实地轨首扫评分卡 · 产品工程闭环实验（只读）

- **被测**：`D:\产品工程闭环实验`（favorites-list 收藏清单，原生 JS 单文件 app.js 741 行 + docs/ 五键 bindings.json 39 行 + contracts/favorites.{json,contract.md}）——2026-09 初的闭环实验项目，先于产品包 v0.2.x 载体规范成型。
- **约束**：被测项目只读一行不改；全部测量产物落本仓 `docs/field-trials/site-01-closedloop/`。
- **日期**：2026-09-30 05:1x（WS2 周期#7 实地轨首扫）
- **方法**：七台机检 + 忠实转写复跑；判定口径=「工具域边界」与「项目缺陷」与「跑法假阳」三分离。

## 一、七台结果总表

| 门禁 | 结果 | 判定 |
|---|---|---|
| spec-trace | **39/39 行全 PASS（exit 0）** | 正面证据：手工五键 bindings 质量实证，T1-T6 零违例 |
| statechart | 初跑 C7 反向 ×2 → **忠实转写后复跑全绿（exit 0）** | 见 §二：真发现 #1（非项目结构缺陷） |
| frontend-lint | 默认 ext 扫 0 → **`--ext .js` 复跑 4 项（exit 1）** | R1×1 真发现 + R3×3 判定域候选（§三） |
| a11y | 扫 1 文件（app.js）全 PASS | 正面；n=1 |
| product-object | N/A（项目无 L0-L6 载体六件套） | 历史原因：先于载体规范；非缺陷（§四） |
| l0-l5 | N/A（无 ia.json / 北极星档） | 同上 |
| registry / extract | 0 项 | **真域边界**：registry 组件注册表概念不适用原生 JS；extract 提取语法三形态（装饰器 / `"GET /path"` 字面量 / Next route）不覆盖函数名后端（doAdd/doSoftDelete/setAdmin），组件提取=Vue/React 文件名枚举——0 是语法域边界非后缀问题（`--ext .js` 复跑仍 0） |

## 二、真发现 #1：recovery 语义无机器可读载体（C7 盲窗）

- **现象**：初跑 C7 报 export_failed 两条转换「未登记」。排查发现**双重根因**：
  1. 跑法假阳成分：初跑把 statechart 文件本身误传 `--contract`（registered=∅）——方法论错误，如实记录；
  2. **真载体缺口**：项目 recovery 语义完备但**只存在于 `favorites.contract.md` §③「错误态 recovery 行」markdown 表格**（三行：RETRY_EXPORT→exporting / ABORT→list / DISMISS→list），无任何机器可读 JSON。即使跑法正确也无 `--contract` 可传——C7 反向对账在此项目**天然盲窗**。
- **闭环验证**：按忠实转写 protocol 把 §③ 三行转写为本仓 `product/contract.transcribed.json`（含 `_provenance` 来源注记），复跑 `statechart-gate --contract` → **exit 0 全绿**。证明：项目 statechart 与人工契约实际一致（结构面健康），且「转写即闭环」路径可行。
- **候选回流（规范面，非 checker 面）**：SKILL/契约模板应明确「recovery 须有机器可读载体（contract.json `recovery` 键），markdown 契约不构成 C7 对账输入」——已入候选池，本周期不施工（探测式 warning 有误报风险，待设计）。

## 三、frontend-lint `--ext .js` 复跑 4 项裁决

| 项 | 位置 | 裁决 |
|---|---|---|
| R1 内联样式 | app.js:602（progress-fill width 动态拼接） | **真发现**：与本仓此前人工手查同一处，交叉验证一致 |
| R3 console ×3 | docs/evidence/smoke-core.js:14/15/627 | **判定域候选**：这些是冒烟证据脚本的输出本体（`SMOKE RESULT` 报告），非交付产物调试残留。候选池：R3 测试/证据目录（test/evidence/spec）豁免约定——需防误放行设计，本周期不施工 |

- **方法论修正记录**：「0 扫描=工具域边界」的初判被复跑**部分推翻**——frontend-lint 是参数域（`--ext` 可传 .js），非能力域。公平测量必须先试参数再下域边界结论。此教训与 extract 形成对照（extract 复跑仍 0 = 真语法域边界）。

## 四、适用面观察（n=1 如实记录）

- 产品包七台对**存量原生 JS 项目**的覆盖：spec-trace/statechart/frontend-lint/a11y 四台有效（其中两台需参数适配）；product-object/l0-l5 两台因载体档缺失 N/A（需先建档）；registry/extract 两台语法域不适用。
- **周期#11 回访（recovery 探针实测）**：`--probe-recovery docs` 收紧判据后命中 1 档=`contracts/favorites.contract.md`「③ 错误态 recovery 行」——首版单词判据曾 2/5 精度（EVIDENCE.md 调试标题误报），收紧为标题「语义词×状态域词」共现后零误报（`probe-recovery.txt`）。探测→忠实转写→C7 对账路径闭环。
- 推广面含义：存量项目接入的**前置成本=契约载体建档**（bindings/statechart/contract.json），产品包的「跑道产物」定位在存量项目上退化为「半自动」——这是推广文档/模板面的课题，非本周期缺陷。

## 五、GATE

GATE: {level=L2-F, v=site-01 实地轨首扫（只读）, cmd=python skill/shisan-xinuo-product/scripts/statechart-gate.py --file "$B/docs/contracts/favorites.json" --contract docs/field-trials/site-01-closedloop/product/contract.transcribed.json, exit=0（C7 复跑全绿；frontend-lint 复跑 exit=1 抓 4 项为预期发现）, files=docs/field-trials/site-01-closedloop/（SCORECARD+contract.transcribed.json+三份复跑输出+两份提取空表）, refs=details #255（env-death 不判负，循环侧适用）/#294（Read 后 Edit ×2）/MSYS 路径陷阱（参数位置自动转换 vs 字符串内不转——gate 参数路径可读、python -c 内嵌路径 FileNotFoundError 实证）, errpath=C7 初跑假阳→误传 statechart 为 contract→忠实转写复跑闭环；frontend-lint 0 扫描→--ext .js 复跑推翻「域边界」初判→4 项真发现+3 项判定域候选；python -c /d/ 路径→MSYS 只转参数位不转字符串→bash 参数传 C:/ 或仓内相对路径, lessons=①公平测量先试尽参数再下域边界结论（frontend-lint 参数域 vs extract 语法域对照实证）②recovery 机器可读载体缺失=C7 盲窗根因，转写即闭环③存量项目接入前置成本=契约建档, exempt=product-object/l0-l5 两台 N/A（载体缺失，历史原因）；registry/extract 域边界 n=1 不外推；a11y 仅 1 文件（app.js 单文件项目）, caps=七台机检全跑（statechart/spec-trace/frontend-lint/a11y/registry/extract/spec-trace-extract）+loop 进度核查, effort=复跑三台（statechart/frontend-lint/extract）+源码级域边界取证（extract 规则面逐行）+忠实转写含 provenance, stop_reason=—}
