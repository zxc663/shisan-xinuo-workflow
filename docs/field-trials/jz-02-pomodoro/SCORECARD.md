# jz-02-pomodoro · SCORECARD（八门禁试金石记分）

- 卡：番茄钟（计时态机域 / 单页 / 纯前端）｜夹具=12 文件｜首跑 2026-09-30
- 诚实性：夹具作者=门禁作者（同源污染，方向性 n=1）；所有 exit 为真实运行回显。

## 一、门禁结果（首跑 → 回流后复跑）

| 门禁 | 首跑 | 回流后复跑 | 命中明细（植入缺陷→抓到） |
|---|---|---|---|
| ① product-object | FAIL 2F | 同 | P1 职责句「展示」开头✓；P2 双核心✓（P3/P4 按设计通过——P4 两维合规不触发 W） |
| ② l0-l5 | FAIL 1F+2W | 同 | L5-C3 位置指示缺失且无豁免✓；W=L5-C1/C11（未植入即告警=工件性提醒，方向正确） |
| ③ statechart | FAIL 3F | 同 | C5 guard 无说明✓；C6 `stats` 悬空 target✓；C3 long_break 不可达✓（C7 recovery 一致=按设计通过） |
| ④ usage-probe | N/A | N/A | 夹具无会话面 |
| ⑤ registry | FAIL 4F | 同 | 4 组件全未归因✓ |
| ⑥ frontend-lint | FAIL 21F | 同 | R1×13+R2×8 全命中；R5-W 未触发=设计差异（StatsPanel 有 v-else 暂无——反向验证 R5-W 不滥报） |
| ⑦ spec-trace | FAIL 1F（T2） | FAIL 2F | T2 待补✓；**T6 幽灵端点×1（回流后新增命中：`GET /api/stats` ∉ 空 backs 清单）** |
| ⑧ a11y | FAIL 1F（A3b） | FAIL 5 | **A3b×1 BreakSplash 伪按钮（jz-01 回流件第二域保持命中）**；**A3 纯符号×4 TimerWidget 图标按钮（本卡新回流件首战即中）** |

- 植入→抓到合计：14 处植入缺陷，抓到 13（唯一漏网=E6 见下）。
- 回流件交叉验证：jz-01 回归复跑 spec-trace/a11y 均零新增假阳；九台 selftest 全 PASS（含 T6 空清单反向变异、A3 符号拦/放行三态）。

## 二、逃逸分析（首跑漏网/边界外逐条裁决）

| # | 逃逸 | 裁决 |
|---|---|---|
| E1 | paused 态无「放弃/取消」出路（有出边≠出路齐全；C2 只查无出边死端） | 判定域：图死端≠语义死路，语义出路齐全性=人工走查域（判定表行候选）——**周期#12/13 已兑现**：interaction-bridge §4「放弃路径三问」承载（paused=进行中态，三问①出路核查命中本例）；与 jz-04/jz-05 E2 三击同族，judgement-table #19 处置栏已回指 |
| E2 | 绑定引用不存在的端点（`GET /api/stats`，T4/T5 双向都查不到） | **真缺口→已回流 T6**（含实现自抓 bug：`if backend_list:` falsy 吞空清单，改为 `is not None`+空清单反向变异自测） |
| E3 | 图标字形按钮（▶⏸⏭ 有内容非空→旧 A3 不触发，无有效可访问名） | **真缺口→已回流 A3 纯符号变体**（内容无 `\w` 词符且无 aria-label → 拦；CJK/字母/表达式放行） |
| E4 | setInterval 每秒累积 tick（锁屏/后台节流→计时漂移） | 运行时正确性域（测试域，静态门禁边界外，记录） |
| E5 | 自定义时长无下界（0/负数直达计时器；C5 guard 在态机层声明但代码未实现） | 跨工件一致性（态机↔代码）人工域，记录 |
| E6 | brief 明确要求「完成的时候提醒我」，实现与 capability 清单双缺 | **brief 原子需求→capability 覆盖无人查**：内容级追溯=NLP 匹配误报风险，机器子集边界外→候选池方向性记录；本卡由人工走查抓出（14 植入中唯一漏网）——**周期#13 落点兑现**：interaction-bridge §1.5 主功能面盘点承载（原子需求逐条入盘点表逐条对账 capabilities），机检不可行维持 |
| E7 | north_star=「累计专注时长 10000 小时」经典虚荣态，C13 词表不含「累计+业务量」形 | 判定域设计取舍：词表保守防基础设施合法累计误报（C13 本=warning+人工裁决），记录不扩 |

## 三、夹具书写教训（回流过程沉淀）

1. **夹具先读 schema 再写**：bindings 五键（page/component/feature/backend/evidence）——首写漏 `page` 致 T1 七连「五段不齐」，是夹具错误非缺陷发现（真 agent 会按门禁 schema 写）。
2. **回流实现自抓 bug**：T6 首战未触发——`if backend_list:` 把「提供了但为空的后端清单」当 falsy 跳过，而空清单恰是幽灵端点最典型场景（纯前端夹具引用不存在 API）。修正=`is not None` 判空语义 + 空清单反向变异进自测（#407 精神：反向样本含边界值）。
3. **门禁契约即载体**：A3b/R5-W/P4-W/T6/A3 符号两卡五回流全部走「脚本+自测正反样例+SKILL §9/§67 载体行」同批落地，卡间可复跑验证。

## 四、回流清单（本卡）

- T6 幽灵端点（spec-trace-gate）：+URLISH 正则+`is not None` 判空+自测 ok5/ok6——jz-02 命中×1、jz-01 回归零新增。
- A3 纯符号变体（a11y-gate）：+可见内容无词符分支+自测 SymbolBad/SymbolLabel/SymbolText 三态 ok9——jz-02 命中×4、jz-01 回归零新增。

## 五、复跑

见 README.md §复跑命令（全部命令直跑可复现上表）。
