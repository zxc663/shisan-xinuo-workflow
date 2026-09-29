# jz-01-ledger · 评分卡（WS2 周期 #1）

- 跑批时间：2026-09-30 凌晨（v3.4.0 部署后；产品包 0.2.7 准备态）
- 夹具：现实中等水平产物 14 件（brief 1 + product 契约 6 + 组件 5 + 后端 1）
- 口径：exit 码为门禁真值；findings 为门禁输出；逃逸分析=领域评审逐条对账

## 一、八门禁结果

| # | 门禁 | exit | 命中（fail / warn） | 抓住的 planted 类 |
|---|------|------|---------------------|-------------------|
| ① | product-object P1-P4 | 1 | 4 fail + 1 W* | P1 职责句「展示」开头；P2 双核心；P3 L2 悬空 + L4 缺失 |
| ② | l0-l5 | 1 | 6 fail + 4 W | L0-C12 无度量口径；L0-C5×2 缺时间窗；L5-C3 三件套缺；L5-C5 孤页 /stats；L5-C10 死端 /settings |
| ③ | statechart C1-C7（含契约） | 1 | 8 fail | C5 守卫无说明；C6 DELETE→deleted 悬空；C2 conflict 死端；C3 importing/conflict 不可达；C7 正向漂移 + 反向未登记 ×2 |
| ④ | spec-trace-extract（辅助器） | 0 | — | 5 组件 + 4 端点提取正确 |
| ⑤ | spec-trace T1-T5 | 1 | 3 fail | T2 evidence=TODO；T4 SettingsForm 孤儿；T5 DELETE 端点死逻辑 |
| ⑥ | registry 归因 | 1 | 5 fail | 5 组件全部缺 registry 标记 |
| ⑦ | frontend-lint R1-R5 | 1 | 32 fail + 2 W* | R1×16 内联样式；R2×12 硬编码色；R3×3 console；R4×1 空 catch；R5-W×2 空态缺失* |
| ⑧ | a11y A1-A4+A3b | 1 | 4 fail | A1 img 无 alt；A2 select 无可访问名；A3b×2 click-div 伪按钮* |
| — | usage-probe | N/A | — | 监控对象=Skill 自身使用率，不适用于被测夹具 |

`*` = 带星行是**本卡回流后才有的判据**（回流前实测不命中，回流后复跑命中——回流效力的直接证据）。

## 二、逃逸分析（领域评审 → 门禁对账）

夹具中真实存在、首发跑批未被任何一台抓住的缺陷：

| # | 缺陷 | 判定 | 处置 |
|---|------|------|------|
| E1 | 流水列表无空态分支（空数据时页面只剩「加载更多」死按钮）——产品包触发面点名「空态没有引导」，八台无机器判据 | **真缺口** | **已回流 R5-W**（v-for 无空态分支 → warning） |
| E2 | click-div 伪按钮 ×2（tx-row / QuickBarButton：@click 无 role 无键盘路径）——A3 只覆盖 button/a 空内容，伪按钮不在其声明边界 | **真缺口** | **已回流 A3b**（click 绑定非语义元素无 role → fail） |
| E3 | operability 只答「数据来源」一维（谁管理/权限/备份恢复/fallback 落空）——P4 只拦缺失不拦单薄 | **半缺口** | **已回流 P4-W**（管理维度 <2 → warning） |
| E4 | 金额 float 直出（无货币符号/千分位/正负语义/精度隐患） | 展示语义域——机器化脆弱，人工走查域 | 判定表行候选，不急 |
| E5 | add_tx 缺 amount 静默落 0（假成功写入） | 后端语义=测试域，产品包边界外 | 记录不回流 |
| E6 | 日期自由文本（month startswith 筛选会被「9月30日」击穿） | 数据契约域外 | 记录不回流 |
| E7 | index-as-key（:key="i"） | 框架工程质量域外 | 记录不回流 |
| E8 | loadMore 假按钮（console.log TODO） | R3×3 抓到调试残留证据；「按钮无真实行为」本身归验收三件②实机取证 | 部分覆盖，不回流 |
| E9 | canvas 图表无文本替代 | 声明边界内（axe-core 完整审计=人工域，SKILL.md 明示） | 豁免不回流 |
| E10 | fetch 裸 await 无错误出路（CategoryPicker/StatsChart） | 运行时错误出路，静态正则不可查 | 记录不回流 |

## 三、回流施工与验证

- 三处 checker 扩展：`a11y-gate` A3b（含 @click 修饰符形态）、`frontend-lint-gate` R5-W（warning 级不走基线）、`product-object-gate` P4-W；各带正向+反向自测（细则 #407 口径）。
- 九台 selftest 全 PASS（回流后整包回归，无既有判据被破坏）。
- 复跑夹具：A3b×2、R5-W×2、P4-W×1 全部命中（表中 * 行）。
- 承载点同步：product SKILL.md 强制清单 §9（A1-A4+A3b）与 scripts 清单行（R5/A3b）。
- 版本口径：产品包 0.2.7 未发行，回流并入本批，不另 bump。

## 四、诚实性声明

- 夹具作者=门禁作者（同人），「不按规则反写」是自觉而非隔离——结构性作者污染在卡（缓解=实地轨对照，见卡池计划）。
- n=1，全部结论只做方向性，不做比例主张。
- 打印帽观察：frontend-lint/a11y 违例显示上限 20 条（`fresh[:20]`），计数与 exit 不受影响——观察项非缺陷。
- Mimosa 观察行：ledger.py 两版被安全钩子拦（变量路径进 open 判路径穿越；夹具无用户输入=误报），改 pathlib 形态后放行——安全钩子无法区分夹具/生产代码，属预期代价。
