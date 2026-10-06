# jz-06-subscription · 试金石卡运行手册

- 卡号：jz-06（WS2 周期 #6）
- 领域：会员订阅（计费态机 / 支付失败恢复路径 / 账单）
- 夹具：`brief.md` + `product/`（契约 6 件）+ `src/components/`（组件 4）+ `src/api/subscriptions.py`（后端 6 端点）
- 差异化：**C7 正反向双发**（recovery target 指向不存在态=承诺落空 + 错误态未登记出边=发明）+ T1 缺 evidence 段（连带 T5）+ A2 裸 select / R3 console 首域；P/L 面+statechart 其余检查设计 PASS

## 复跑命令（仓库根执行）

```bash
S=skill/shisan-xinuo-product/scripts
F=docs/field-trials/jz-06-subscription

python $S/product-object-gate.py --file $F/product/object.json
python $S/l0-l5-gate.py --goal $F/product/goal.json --ia $F/product/ia.json
python $S/statechart-gate.py --file $F/product/statechart.json --contract $F/product/contract.json
python $S/spec-trace-extract.py --src $F/src/components --api $F/src/api \
    --out-components $F/product/comps.txt --out-backends $F/product/backs.txt
python $S/spec-trace-gate.py --file $F/product/bindings.json \
    --components $F/product/comps.txt --backends $F/product/backs.txt
python $S/registry-gate.py --path $F/src --scope components
python $S/frontend-lint-gate.py --path $F/src/components
python $S/a11y-gate.py --path $F/src/components
```

## 判分协议

同前五卡：exit 真值 + 逃逸两分 + 回流带正反自测 + n=1 方向性。
