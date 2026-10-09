# 实地轨三站装配卡（转型 R2 · D2=三站全接，2026-10-10）

> 形态：**真实开发环节收尾步骤**跑产品工程八台门禁——不是试金石、不是只读扫描；被测项目自身**不加任何机制**；真发现→SCORECARD 落本仓 `docs/field-trials/<站名>/`，候选池回流照常（周期 #8/#10/#11 同型）。

## 站 1 · 产品工程闭环实验（favorites-list）

- 基线：site-01 已扫（2026-09-30，spec-trace 39/39 正面+真发现 #1 recovery 载体缺口；`docs/field-trials/site-01-closedloop/`）。
- 收尾跑：`spec-trace`（bindings 在案直跑）→ `statechart --contract contract.transcribed.json`（已忠实转写）→ `frontend-lint --ext .js` → `a11y`。
- 注意：evidence/smoke 证据目录已整文件豁免（周期 #10）；canvas 豁免不适用（本站无 canvas）。

## 站 2 · 个人财务助手 9.20

- 基线：site-02 已扫（2026-09-30，a11y 全过+R2 canvas 判定域；`docs/field-trials/site-02-finance/`）。
- 收尾跑：`frontend-lint --ext .html`（canvas 豁免后余 7 项=人工域）→ `a11y`；statechart 接入前置=交互设计说明 §4 recovery 段忠实转写（`--probe-recovery` 可定位）。

## 站 3 · 博客工作区

- 接入前置：开工先探栈——Vue/React 文件名形态覆盖则 `registry/extract` 可用；否则 `frontend-lint`+`a11y` 先行（参数域≠能力域，先试尽参数再下域边界结论——site-01 教训在案）。

## 命令模板（从本仓根跑，各 gate `--help` 定参；jz-*/SCORECARD.md 有成例）

```bash
python skill/shisan-xinuo-product/scripts/spec-trace-gate.py --file <项目>/product/bindings.json --components <清单> --backends <清单>
python skill/shisan-xinuo-product/scripts/frontend-lint-gate.py --path <项目> --ext .js   # 或 .html/.vue
python skill/shisan-xinuo-product/scripts/a11y-gate.py --path <项目>
python skill/shisan-xinuo-product/scripts/statechart-gate.py --file <项目>/statechart.json --contract <项目>/contract.json
```

> 出口（R2）：≥2 站产出「开发中途真发现」（非复扫既有结论）；每站一行入 agent-log 流水。
