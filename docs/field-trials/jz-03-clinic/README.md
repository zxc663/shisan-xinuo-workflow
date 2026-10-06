# jz-03-clinic · 试金石卡运行手册

- 卡号：jz-03（WS2 周期 #3）
- 领域：医院挂号（资源冲突预约 / 多页 IA / 前后端混合）
- 夹具：`brief.md` + `product/`（契约 6 件）+ `src/components/`（组件 6）+ `src/api/appointments.py`（后端 5 端点）

## 复跑命令（仓库根执行）

```bash
S=skill/shisan-xinuo-product/scripts
F=docs/field-trials/jz-03-clinic

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

同 jz-01/jz-02（README §判分协议）：exit 真值 + 逃逸两分（声明边界 vs 真缺口）+ 回流带正反自测 + n=1 方向性。
