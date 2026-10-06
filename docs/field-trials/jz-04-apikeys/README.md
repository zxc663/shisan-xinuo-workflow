# jz-04-apikeys · 试金石卡运行手册

- 卡号：jz-04（WS2 周期 #4）
- 领域：API Key 管理（安全域 / reveal-once 生命周期 / 双页）
- 夹具：`brief.md` + `product/`（契约 6 件）+ `src/components/`（组件 5）+ `src/api/keys.py`（后端 4 端点）

## 复跑命令（仓库根执行）

```bash
S=skill/shisan-xinuo-product/scripts
F=docs/field-trials/jz-04-apikeys

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

同前三卡：exit 真值 + 逃逸两分 + 回流带正反自测 + n=1 方向性。
