# site-02 实地轨快扫评分卡 · 个人财务账单智能规划助手 9.20（只读）

- **被测**：`C:\Users\zxc66\Desktop\个人财务账单智能规划助手-9.20`（工作流跑道项目：AGENTS.md/memory/docs 八节/design-specs 全套承载；前端面=particle-tree.html 单文件 914 行）。
- **约束**：只读零写入，产物落本仓 `docs/field-trials/site-02-finance/`。
- **日期**：2026-09-30 05:3x（WS2 周期#9 实地轨第二站快扫）
- **选点说明**：博客工作区实测为空壳、ferry_web 仅剩 node_modules、ferry 为 Go 后端（域外）——存量前端应用可扫面收敛至此项目。n=2 快扫定位=site-01 发现的泛化性验证，非全量审计。

## 一、门禁结果

| 门禁 | 结果 | 裁决 |
|---|---|---|
| a11y | **exit 0 全过**（1 文件） | 正面：img alt/控件可访问名/伪按钮零违例 |
| frontend-lint `--ext .html` | exit 1，**20 项全 R2 零 R1/R3/R4** | R2 命中全部为 canvas `addColorStop()` 渐变色值——**判定域候选**（§二） |
| spec-trace/statechart/registry/extract | N/A | 无 bindings/statechart 载体（存量项目，同 site-01 接入前置成本观察）；单 html 无组件文件 |

## 二、判定域候选：R2 对 canvas 绘制参数

20 项 R2 全部形如 `grad.addColorStop(0, 'rgba(90,70,160,0.14)')`——canvas 渐变 API 的色值是**程序绘制参数**（粒子树视觉动画），不是组件样式表的 token 逃逸。R2 规则字面执行正确（`rgba?\(` 匹配），但域语义待裁决：候选池记「R2 canvas addColorStop 豁免约定」（`addColorStop\(` 调用参数内的色值降 warning 或豁免——需防「借 canvas 外衣逃 token 纪律」的误放行设计）。与 R3 证据脚本豁免（site-01）同族=判定域清单第三项。

**终态裁决（周期#10 回流后）**：R2 canvas 豁免以**双形态**落 checker——`addColorStop(` 调用行与 `strokeStyle/fillStyle` 赋值行（均为 canvas 专属 API 名，误放行面≈0）；复扫终态 **7 项**（`frontend-lint-rerun.txt`）全为 `makeGlowSprite/makeStarSprite` **自定义函数参数**——语义不可机判=**人工域**，保持拦（「借 canvas 外衣逃 token 纪律」恰由人工域边界兜住）。§四 GATE 中「20 项」为快扫时点值，终态以 rerun 为准。

## 三、同族标本第二例：错误态语义 markdown 在场、机器载体缺失（与 site-01 双击）

`docs/02-产品设计/交互设计说明.md` **§4「状态与异常总表」**= 场景/表现/恢复三列 markdown 表（5 行：数据仓空→引导卡/LLM 离线→徽章降级/调用失败→黄条+重试/重复导入→标记提示/恢复出厂→二次确认）——**与 C7 recovery 行 (state, action, target) 语义同构**，但无 statechart.json/contract.json 机器载体。

- **跨项目双击成立**：site-01（闭环实验项目 contract.md §③）+ site-02（工作流跑道项目交互说明 §4）两个独立存量项目同呈「recovery/error 语义人工面完备、机器载体缺失→错误态门禁天然盲窗」。
- **已兑现的回流**（周期#8）：SKILL §32 规范句（recovery 须有机器可读载体）+ gate 跑法提醒——本例再证其必要性；候选池「同目录 markdown recovery 语义探测式 warning」价值面加强（两个实证命中）。
- 晋升动作：本轮起「存量项目 markdown 契约语义在场/机器载体缺失」从观察项升候选池高优先。

**周期#11 探针实测**：`--probe-recovery docs` 收紧判据后命中 1 档=本节标本所在 `交互设计说明.md`（命中行恰为 §4「状态与异常总表」真标题；首版单词判据曾误报运维「备份与恢复」/迭代计划「指标与异常检测」等 3 档）——探测→忠实转写→C7 对账闭环路径可用（`probe-recovery.txt`）。

## 四、GATE

GATE: {level=L2-S, v=site-02 快扫（只读）, cmd=python skill/shisan-xinuo-product/scripts/frontend-lint-gate.py --path "$B/particle-tree.html" --ext .html, exit=1（20 项 R2=预期发现域）, files=docs/field-trials/site-02-finance/（SCORECARD+两扫描输出）, refs=details #255=1, errpath=博客项目空壳→换选点；R2 批量命中→逐条读源确认为 canvas API 形态→判定域候选非 checker bug, lessons=判定域清单第三项（R2 canvas）；同族标本第二例=markdown recovery 语义普遍存在（跨项目双击）, exempt=spec-trace/statechart/registry/extract N/A（载体缺失）；n=2 快扫非全量审计, caps=双门禁+a11y, effort=选点三探一（博客/ferry_web/ferry 排除）+交互设计档语义比对, stop_reason=—}
