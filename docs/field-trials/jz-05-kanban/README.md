# jz-05-kanban · 试金石卡运行手册

- 卡号：jz-05（WS2 周期 #5）
- 领域：团队看板（拖拽状态 / 错误态出路 / 纯展示组件 NONE 形态）
- 夹具：`brief.md` + `product/`（契约 6 件）+ `src/components/`（组件 4）+ `src/api/boards.py`（后端 4 端点）
- 差异化：statechart+contract 设计为**全绿正对照**（前四卡首例 exit 0）；植入面=A1 img 无 alt（首域覆盖）/R1+R2/R4/T3 冗余行/C13 虚荣指标/P1 purpose 缺失；`{task_id}` 参数变体第四域回归

## 复跑命令（仓库根执行）

```bash
S=skill/shisan-xinuo-product/scripts
F=docs/field-trials/jz-05-kanban

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

同前四卡：exit 真值 + 逃逸两分 + 回流带正反自测 + n=1 方向性。
