# jz-07-cronrunner · 定时任务管理器试金石（WS2 周期 #15）

- 卡号：jz-07（WS2 周期 #15）｜来源：fixture-ideas-20260930.md #119
- 领域：定时任务管理（cron 态机 / 失败恢复 / 运行历史）
- 夹具：15 件——`brief.md` + `product/`（object/goal/statechart/contract/bindings/ia 六件）+ `src/components/`（组件 5）+ `src/api/tasks.js` + `product/comps.txt`/`backs.txt` 手写清单
- 差异化：**双回流卡**（frontend-lint COMPONENT_EXCLUDE 子串误伤 + l0-l5 C13 累计组合形，均 jz-07 首跑暴露）+ statechart 夹具设计 bug 自获（SAVE→idle 致 C3×4 连报）+ 三问①/E6 语义走查实战

## 复跑命令（仓库根执行；frontend-lint `--ext` 为逗号串单值参数，.vue/.js 分两跑）

```bash
S=skill/shisan-xinuo-product/scripts
F=docs/field-trials/jz-07-cronrunner

python $S/product-object-gate.py --file $F/product/object.json
python $S/l0-l5-gate.py --goal $F/product/goal.json --ia $F/product/ia.json
python $S/statechart-gate.py --file $F/product/statechart.json --contract $F/product/contract.json
python $S/spec-trace-gate.py --file $F/product/bindings.json \
    --components $F/product/comps.txt --backends $F/product/backs.txt
python $S/spec-trace-extract.py --src $F/src/components --api $F/src/api \
    --out-components $F/product/comps.txt --out-backends $F/product/backs.txt  # 会覆盖手写清单，验证用
python $S/registry-gate.py --path $F/src --scope components
python $S/frontend-lint-gate.py --path $F/src/components --ext .vue
python $S/frontend-lint-gate.py --path $F/src --ext .js
python $S/a11y-gate.py --path $F/src/components
```

## 预期结果（2026-09-30 回流后基线）

| 门禁 | exit | findings |
|------|------|----------|
| product-object | 1 | P1×1 |
| l0-l5 | 0 | warn×1（L0-C13 组合形「累计执行次数破十万」） |
| statechart+contract | 1 | 5 项（C6 disabled 悬空 / C2 failed / C3 history / C4 / C7 paused 承诺落空） |
| spec-trace | 1 | 4 项（T1 行2 缺 evidence / T4 CronField 孤儿无连带 / T5 POST /tasks 带连带 / T6 run-now 幽灵） |
| registry | 1 | 4×缺归因头（CronField 带头放行） |
| frontend-lint .vue | 1 | R3 TaskHistory + R1 TaskList + R5-W×2 |
| frontend-lint .js | 1 | R4 空 catch |
| a11y | 1 | A2×2 + A3「▶」×1 |

## 判分协议

同前六卡：exit 真值 + 逃逸两分（判定域内→回流 checker 带 #407 反向自测；语义评审域→人工走查记录）+ 夹具修正留痕 + 六卡回归零漂移。详见 SCORECARD.md。

## 语义走查（人工域，非机检）

- 三问①（interaction-bridge §4）：editing 态放弃路径缺席——出边只有 SAVE 成功出路；正对照 confirming.ABORT / running.CANCEL。
- E6：brief 原子需求 6「失败要通知我」对 capabilities / contract / bindings 三层逐条对账——全缺，且 object.json L4 adjudicated 已写明通知出路=L4→capability 断链。
