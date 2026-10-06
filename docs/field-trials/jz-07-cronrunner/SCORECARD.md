# jz-07-cronrunner · SCORECARD（WS2 周期 #15）

- 卡号：jz-07｜领域：定时任务管理器（fixture-ideas #119｜cron 态机 / 失败恢复 / 运行历史）
- 判分协议：同前六卡（README §判分协议）
- 首跑时间：2026-09-30 08:5x｜回流后复跑同日（frontend-lint 锚定修复 + l0-l5 C13 组合形 + 夹具 statechart 三处修正后）

## 一、八门禁结果（首跑→复跑）

| # | 门禁 | 首跑 | 复跑 | 判读 |
|---|------|------|------|------|
| ① | product-object | 1 | 1 | P1×1（职责句「展示…」开头，非管理性动词）✓植入命中 |
| ② | l0-l5 | 0（**C13 漏报**） | 0（1 warn） | 首跑「累计执行次数破十万」未报=**真缺口**→回流组合形后 warn ✓（双击晋升实证） |
| ③ | statechart+contract | 1（10 项） | 1（5 项） | 首跑含 C3×4 连报（夹具设计 bug）+C2 history（夹具缺出边）+C5 editing（夹具书写偏差）；**修正后 5 项=干净植入面**（C6/C2 failed/C3 history/C4/C7） |
| ④ | spec-trace | 1 | 1 | T1 第2行缺 evidence×1 + T4 孤儿（无连带标注，反面正确）×1 + T5 死逻辑（带连带标注，正面正确）×1 + T6 幽灵×1 |
| ⑤ | registry | 1 | 1 | 4×缺归因头；CronField 带 `registry: source=` 头=正对照放行 ✓ |
| ⑥ | frontend-lint | 1（R3 消失） | 1 | 首跑 R3 被 COMPONENT_EXCLUDE **子串误伤吞掉**（TaskHistory.vue 含 "story"）→锚定修复后 **R3 现形** ✓ + R1 + R5-W×2 + R4 |
| ⑦ | a11y | 1 | 1 | A2×2（TaskForm label 不关联 / CronField input 无 label）+ A3×1（RunNowButton「▶」纯符号）全命中 |
| ⑧ | usage-probe | — | — | 非卡面门禁 |

## 二、植入→命中对照

| 植入缺陷 | 门禁判据 | 结果 |
|----------|----------|------|
| responsibility「展示定时任务列表与运行记录」（非管理性动词开头） | P1 | ✓ 首域命中 |
| north_star=「累计执行次数破十万」（累计×业务量虚荣形） | L0-C13 | 首跑 ✗漏报→**回流后 ✓**（组合形判据） |
| statechart scheduled.DISABLE target=`disabled`（不存在的态） | C6 引用完整性 | ✓ 悬空拦截 |
| statechart failed 态无出边 | C2 死端 | ✓ |
| statechart history 态无入边 | C3 不可达 | ✓ |
| statechart failed 无恢复出路 | C4 | ✓ |
| contract recovery 承诺 failed --RETRY--> paused（paused 不存在） | C7 正向 | ✓ 承诺落空 |
| bindings 第 2 行 TaskForm/POST /tasks 缺 evidence | T1 五段不齐 | ✓ 连带 T5 POST /tasks 死逻辑带标注 + T4 CronField 孤儿无标注（正反面都对） |
| RunNowButton 绑 POST /tasks/{id}/run-now（backs.txt 无此端点） | T6 幽灵绑定 | ✓ |
| TaskList 内联 `:style="'color:red'"` | R1 | ✓（含三目绑定形态） |
| TaskHistory `console.log` | R3 | 首跑 ✗被 EXCLUDE 吞→**回流后 ✓现形** |
| TaskHistory/TaskList v-for 无空态 | R5-W | ✓ warning×2 |
| src/api/tasks.js `catch (e) {}` | R4 | ✓（.js 面） |
| TaskForm label 无 for 关联 + CronField 裸 input | A2 | ✓×2 |
| RunNowButton「▶」纯符号无词符无 aria-label | A3 | ✓ |
| **正对照** CronField 头部 `// registry: source=brief 原子需求 1` | registry 归因头 | ✓ 放行（其余 4 组件拦） |
| **正对照** scheduled.TRIGGER guard+guardDesc | C5 | ✓ 不报 |
| **正对照** running 态 CANCEL 出路（运行中可取消） | 三问①对照 | ✓ 语义走查用 |

## 三、计划外自获（夹具自然形态显微镜）

1. **statechart SAVE→idle 设计 bug**：夹具初稿把 SAVE target 写成 idle，致 scheduled/running/failed 全部无入边，C3×4 连报——初看像 gate 误报，读图核实是**夹具自身设计错误**（保存后的任务必然进入调度态）。修正为 SAVE→scheduled 后 10 项收敛为 5 项干净植入面。C3 全可达检查的第三例真价值（jz-06 GET /plans 第二例之后）。
2. **COMPONENT_EXCLUDE 子串误伤**（本轮最大回流）：旧排除正则 `(test|spec|story|…)` 无词边界，`TaskHi·story·.vue` 文件名含 "story" 子串被**整文件排除**——R3 植入完全消失（假阴性）。History/List/Story 类命名超常见，方向=漏报非误报，危害更高。
3. **C13 累计形漏报**：裸名词表（累计用户/累计注册）不含「累计+业务量词」组合形——jz-07「累计执行次数破十万」+jz-02「累计专注时长」构成跨卡双击。

## 四、语义走查（人工域，真实读图）

- **三问①（editing 态能否放弃）命中**：editing 出边只有 SAVE（成功出路），无 CANCEL/ESC/关闭放弃出路——结构门禁查不到（有出边≠死端），语义评审域命中。正对照：confirming 有 ABORT、running 有 CANCEL。三问②连带命中（放弃后回落无建模）；三问③轻度命中（编辑丢弃无警示）。落点=judgement-table #19 处置栏已含「有出边但只有成功出路=语义死路」条目。
- **E6（brief 需求 6「失败要通知我」）三层全缺**：capabilities 5 条无通知（第一缺）+ contract recovery 只有 RETRY 无通知承诺（第二缺）+ bindings/backs 无 notify 端点（第三缺）；且 object.json 自己的 L4 adjudicated 写明「失败任务必须有重试与通知出路」——**L4→capability 断链**，双缺实锤。属内容级追溯人工走查域（§1.5：机检属 NLP 匹配误报域不建 checker），本卡实战演示成立。

## 五、逃逸分析（两分裁决）

- **E1（判定域内，已回流）**：l0-l5 C13 组合形漏报——回流 VANITY 组合形 `(累计|总共|总计)[^\n]{0,6}(次数|执行|完成|处理|点击|浏览|访问|时长)`，selftest +ok9 正反三样例（累计执行次数✓/累计专注时长✓/累计成功率放行✓）。
- **E2（判定域内，已回流）**：frontend-lint COMPONENT_EXCLUDE 子串误伤——回流路径段锚定正则（`(^|[/\\])(test|…|smoke)([/\\])` 完整目录段 / `\.d\.ts$` 后缀锚），selftest +ok10h/ok10s 反向变异（TaskHistory 不排除 ✓ / story/ 目录仍排除 ✓）。六卡回归：jz-07 复跑 R1/R4/R5-W 零漂移。
- **E3（已知形态）**：registry 4×缺归因头（七卡一致夹具形态）。
- **E4（语义评审域，记录）**：三问① editing 放弃路径缺席 + E6 通知链三层缺——人工走查完成，不建 checker（NLP 匹配误报域，§1.5 既定）。
- **E5（夹具书写偏差，修正 3 处）**：editing SAVE 缺 guardDesc（补）；history 无出边（加 BACK→scheduled，C3 无入边植入保留）；SAVE target=idle→scheduled（设计 bug）。

## 六、回流清单（本卡）

**双回流（七卡首次单卡双件）**：①frontend-lint-gate 路径段锚定+selftest 反向变异②l0-l5-gate VANITY 组合形+selftest 正反样例——两 selftest 全绿（frontend-lint 10 判据 / l0-l5 9 判据）。

**六卡回归**：frontend-lint 零漂移（jz-04=0 其余=1，与基线一致）；l0-l5 唯一差异=jz-02 C13 warn 新增「累计专注时长达到 10000 小时」——**第二双击样本回植成功**（首跑漏报→warn），预期内生效漂移；jz-05 裸名词形照旧、jz-06 全绿、jz-04 零漂移、jz-01/jz-03 exit=1 均为既有失败面（与 C13 无关）。

## 七、夹具教训

- 排除规则用子串匹配目录名时，**文件名合法子串**（History 含 story）会被整文件误排除——排除规则必须锚定路径段/后缀，不做裸子串。
- 虚荣指标判定不能只靠名词表：业务量词组合形（累计×次数/时长）是更高产的形态——「累计+数字成就」叙事天然吸引写进 north_star。
- 夹具 statechart 写错 target 反而暴露 gate 的 C3 连报能力——但**区分「gate 误报」与「夹具错误」必须真实读图**，不能见连报就判 gate 缺陷。

## 八、复跑

见 README.md §复跑命令。
