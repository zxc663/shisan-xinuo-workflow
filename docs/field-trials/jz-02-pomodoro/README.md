# jz-02-pomodoro · 试金石卡运行手册

- 卡号：jz-02（WS2 周期 #2）
- 领域：番茄钟计时器（计时态机 / 单页 / 纯前端）
- 夹具：`brief.md` + `product/`（契约 6 件）+ `src/components/`（组件 4，无后端目录）

## 复跑命令（仓库根执行）

```bash
S=skill/shisan-xinuo-product/scripts
F=docs/field-trials/jz-02-pomodoro

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

注：`--api $F/src/api` 指向不存在目录（纯前端卡），extract 对不存在路径跳过、backs 为空——这是故意形态（测「幽灵端点绑定」是否被抓）。

## 判分协议

同 jz-01（README §判分协议）：exit 真值 + 逃逸分析（声明边界 vs 真缺口两分）+ 回流带正反自测 + n=1 方向性。
