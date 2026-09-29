# 批 X · 五门禁反向注入报告（2026-09-29）

> 边界（计划裁决③）：本批只出**漏报率表+判据缺口清单**，不改五门禁正文；修复随发行批走。
> 方法论镜像 `docs/reverse-injection/EVIDENCE.md`（statechart 四变异先例，2026-09-23）。
> 注：该先例文件实测不在盘上（记忆漂移已记录 agent-log），本批按计划方法定义独立施工。

## 一、方法

- 对象：`shisan-xinuo-product/scripts/` 五门禁 checker（registry / product-object / l0-l5 / frontend-lint / a11y），全带 `--selftest` 且自测全 PASS。
- 手法：**先读源码找判据缺口，再定向构造变异夹具**（非随机变异）——checker 进程内 import 直调，夹具=内存 JSON（PO/LL）+ 静态文件（RG/FL/AG，`fixtures/` 16 件）。
- 驱动器 `driver.py`：零写入、零子进程、零网络（Mimosa 三次路径穿越拦截后的只读版设计）。
- 判读：want=blocked 且放行=**CONFIRMED-MISS（漏报）**；want=allowed 且拦截=**FALSE-POSITIVE（误报）**；其余=OK-CAUGHT / OK-ALLOWED。
- 运行：`python driver.py > report.jsonl`，27 例全数落档。

## 二、结果总表

**27 例 = 漏报 15 ｜ 误报 1 ｜ 正常拦截 5 ｜ 正常放行 6（其中 1 例契约内弱判据另记缺口 RG-3）**

| 门禁 | 变异针 | 漏报 | 漏报率 | 误报 | 备注 |
|---|---|---|---|---|---|
| registry-gate | 4 | 2 | 50% | 1 | 弱判据 1（marker 伪造，契约内放行） |
| product-object-gate | 4 | 3 | 75% | 0 | 1 例变异被 P2 计数混杂拦截（PO-4） |
| l0-l5-gate | 3 | 3 | 100% | 0 | 类型混淆家族三连 |
| frontend-lint-gate | 4 | 4 | 100% | 0 | 正则枚举面四连 |
| a11y-gate | 3 | 3 | 100% | 0 | 1 例属 v1 诚实边界内（AG-3） |
| **合计** | **18** | **15** | **83.3%** | **1** | 对照针 9 例全数行为符合预期 |

口径说明：变异针=18（含 3 例 want=allowed 的判据缺口观测针：rg-marker-forge、rg-node-modules-fp、ag-emoji-button）；want=blocked 变异 15 例全部漏报，唯一拦截的 po-role-enum 是变异被无关检查混杂所致（见 PO-4）。**对照针 9 例（4 blocked + 5 allowed）全部符合预期 → 门禁对「正向样例」的判别力完好，缺口全部在反向变异面。**

### 解读（诚实边界）

1. **93.8%（15/16）是定向攻击漏报率，不是随机缺陷检出率**——变异按源码缺口定向构造，代表「对抗深度」下限。
2. **`--selftest` 全 PASS 与反向注入 15 漏报并存** = 自测只盖正向样例、反向变异是盲区的直接实证。这与 2026-09-24 F2/F5（自测路径缺口）同族，建议晋升 details（同坑跨面再现）。
3. 基线豁免路径（`--write-baseline` 后新增 vs 存量）本批未测，留续批。

## 三、判据缺口清单（18 项，处置随发行批，不改正文）

### registry-gate（RG）
| # | 症状 | 根因（源码行） | 修复建议 |
|---|---|---|---|
| RG-1 | `src/ui/` 目录整体逃逸——路径不含 "component" 即永不扫描 | `component_files()` scope 过滤用 `"component" not in str(f)` 子串匹配 | 默认 scope=all 或按组件后缀+目录白名单 |
| RG-2 | `.VUE` 大写后缀逃逸 | `f.suffix not in exts` 大小写敏感 | `f.suffix.lower()` |
| RG-3 | `registry:` 文本包含即可伪造（console.log 内藏标记放行） | `MARK not in content` 纯文本包含 | 行首注释锚+格式正则；契约内弱判据，登记不升 fail |
| RG-4 | `--scope all` 报 `node_modules/` 三方件（误报） | 无 COMPONENT_EXCLUDE（lint/a11y 两门禁有） | 对齐排除表（test/node_modules/dist…） |

### product-object-gate（PO）
| # | 症状 | 根因 | 修复建议 |
|---|---|---|---|
| PO-1 | `main_function:""` → P2 三检查全跳过 | `if main_fn and …` falsy 短路 | 键存在性与非空单独查 |
| PO-2 | 责任句 `（展示看板数据）` 全角括号包裹绕过禁用动词 | `startswith(("展示","显示"))` 仅前缀 | 禁用动词在句首 N 字内 search |
| PO-3 | `purpose:123` 数字穿透存在性检查 | `str(obj.get(...))` 类型混杂 | isinstance(str) 显式校验 |
| PO-4 | ROLES 枚举定义从未使用（死代码）；本批变异（role="隐藏功能"）被「核心任务数=0」的 P2 计数混杂拦截，枚举严格性缺口无法由该变异隔离观测 | `ROLES` 定义后未引用 | `role not in ROLES` 显式 fail，或删 ROLES 防误导 |

### l0-l5-gate（LL）
| # | 症状 | 根因 | 修复建议 |
|---|---|---|---|
| LL-1 | `north_star:123` 跳过全部声明检查 | 非 None/list/str 分支即静默通过（F5 同族未盖类型面） | isinstance 分支落 fail |
| LL-2 | `global_nav:"false"` 字符串 truthy 判真 | 直接真值判断 | 显式 bool 校验（isinstance(bool) 或字面量集合） |
| LL-3 | `exits:"0"` 字符串绕过死端判定 | `p.get("exits",0)==0` 对 str 恒 False | 数值化容错 `int()` + 类型异常落 warning |

### frontend-lint-gate（FL）
| # | 症状 | 根因 | 修复建议 |
|---|---|---|---|
| FL-1 | 单引号内联样式 `style='…'` 逃逸 | R1 只认 `style="`/`:style="`/`style={{` | 加 `style='`/`:style='` 变体 |
| FL-2 | `console.table/trace/dir/count` 逃逸 | R3 枚举缺 log/debug/info/warn/error 之外成员 | 枚举改 `console\.\w+` 排除合法成员白名单 |
| FL-3 | ES2019 optional catch binding `catch { }` 逃逸 | R4 强制 `catch\s*\([^)]*\)` | 加无参变体 `catch\s*\{\s*\}` |
| FL-4 | `RGB(1,2,3)` 大写逃逸 | R2 无 IGNORECASE（CSS 函数名不区分大小写） | `rgba?\(` 加 re.I（保留十六进制段原样） |

### a11y-gate（AG）
| # | 症状 | 根因 | 修复建议 |
|---|---|---|---|
| AG-1 | 空 `<label><input></label>` 放行（label 无文本=无可访问名） | 包裹豁免只看 depth>0 不查 label 文本 | 豁免前提=label 去子标签后非空 |
| AG-2 | `lang=""` 有键无值放行 | A4 只查键存在 | 值非空校验 |
| AG-3 | emoji-only 按钮放行，读屏可达名存疑 | 文本非空即过（v1 诚实边界内设计） | 登记 axe 完整审计待做项，不升 fail |

## 四、工件与复跑

- 驱动器：`driver.py`（27 CASES 单表定义）；夹具：`fixtures/`（01-05 RG、17-22 FL、23-27 AG，16 件静态文件）；逐例判定：`report.jsonl`（27 行 JSONL）。
- 复跑：`cd docs/reverse-injection-gates-20260929 && python driver.py`。
- 施工教训：Mimosa 三拦 driver 写盘版（tempfile+动态路径+write 模式）→ 只读驱动器+静态夹具+stdout 重定向放行；首跑 TypeError（`json.loads(json.dumps(po({})) | {…})` 中 `|` 误绑内层 str）→ 改 `po()` 变异构造器直写，py_compile 复验通过。

GATE: {level=L2-F, v=批X五门禁反向注入, cmd=cd docs/reverse-injection-gates-20260929 && python driver.py, exit=0, files=driver.py+fixtures/16件+report.jsonl+REPORT.md, refs=details #255/#348/F2同族×3, errpath=Mimosa三拦写盘驱动→只读版+静态夹具；TypeError \|优先级→po()构造器+compile复验; lessons=自测全PASS≠反向防御（15漏报并存）; 类型混杂（str()/truthy/==0）=PO/LL/LL三面共同缺口家族; exempt=基线豁免路径未测（留续批）+定向变异非随机采样, caps=零外部能力（纯本地python）, effort=先读五源码逐行→27定向夹具→驱动器三版迭代过审, stop_reason=—, ev=invariant（对照针9例判别力验证+正反双向判定）}
