# jz-01-ledger · 试金石卡运行手册

- 卡号：jz-01（WS2 周期 #1 首卡）
- 领域：个人记账（CRUD 密集 + 月度统计 + 分类）
- 夹具：`brief.md`（模拟输入）+ `product/`（六件契约工件）+ `src/`（组件 5 + 后端 1）
- 产物立场：现实中等水平——功能齐、能用，但按「交付即忘」的赶工节奏写

## 复跑命令（仓库根执行）

```bash
S=skill/shisan-xinuo-product/scripts
F=docs/field-trials/jz-01-ledger

# ① 产品对象 P1-P4
python $S/product-object-gate.py --file $F/product/object.json
# ② L0 目标 + L5 信息架构
python $S/l0-l5-gate.py --goal $F/product/goal.json --ia $F/product/ia.json
# ③ 态机 C1-C7（含契约对账）
python $S/statechart-gate.py --file $F/product/statechart.json --contract $F/product/contract.json
# ④ 绑定清单提取（components/backends 两清单）
python $S/spec-trace-extract.py --src $F/src/components --api $F/src/api \
    --out-components $F/product/comps.txt --out-backends $F/product/backs.txt
# ⑤ 三方绑定追溯 T1-T5
python $S/spec-trace-gate.py --file $F/product/bindings.json \
    --components $F/product/comps.txt --backends $F/product/backs.txt
# ⑥ 组件归因
python $S/registry-gate.py --path $F/src --scope components
# ⑦ 前端 lint R1-R4
python $S/frontend-lint-gate.py --path $F/src/components
# ⑧ 可达性 A1-A4
python $S/a11y-gate.py --path $F/src/components
```

usage-probe（第 8 台）不适用于本卡：它监控的是 Skill 自身使用率，不是被测产物。

## 判分协议

1. 八台各记 exit 码与命中条目（SCORECARD.md）。
2. **逃逸分析**：以领域评审视角枚举夹具中真实存在的产品工程缺陷，逐条标注「被哪台抓住 / 逃逸」。
3. 逃逸项分两类：声明边界内豁免（如 axe 人工域）= 不回流；**边界内的真实缺口 = 回流候选**（判定表行 / checker 规则 / 六问 wording）。
4. 本卡 n=1，结论只做方向性，不做比例主张。

## 诚实性声明

夹具作者与门禁作者同源（都是本包维护者），存在「知道规则所以不教学式反写」的自觉，但无法完全消除作者污染——这是合成试金石的结构性威胁面，登记在卡；缓解=后续实地轨（既有项目只读跑门禁）提供无污染对照。
