# 行为面 scorecard 时序库

本目录存放 `scripts/probe_runner.py` 产出的机判结果（JSONL，每行=一个场景），用于**跨批次可比的行为面时序库**。

## 字段

| 字段 | 含义 |
| --- | --- |
| `loop` | 批次标签（= runner `--label`） |
| `scenario` | 场景名（19 场景矩阵 + 发布面变体 `rel-dryrun`） |
| `dir` | 探针工作目录名（仅 basename；探针根默认落系统临时目录，与仓库隔离） |
| `markers` | 判据明细（布尔信号：`stateLine` / `gate` / `caps` / `effort` / `blocked_by_discipline` / `blocked_by_env` …） |
| `gate_fields` / `gate_count` / `gate_expected` | GATE 字段解析结果（定版预期 12 字段） |
| `verdict` | `PASS` / `FAIL`（由 `expect` 判据机判，非自述） |
| `ts` | 时间戳 |

## 复跑

```bash
python scripts/probe_runner.py --label <标签> all          # 全量
python scripts/probe_runner.py --label <标签> l3-delete     # 指定场景
```

## 基线说明（历史口径）

- **v2.9.0 基线**：52 探针 51 PASS（98.1%），产生于 v2.9.0 注入副本（夜班监控工作区，非本目录；分析见 `EVIDENCE.md` §三十三 与缺口分析报告）。
- **v3.0 场景矩阵**：19 场景 18/19 PASS + 双击复采（同样来自夜班监控工作区）。
- **v3.0.0 注入副本冒烟**：本目录 `smoke.jsonl`（2/2 PASS，`gate_fields=12/12`）。

> 复测口径见 `RELEASE-CHECKLIST.md` H 节（部署后 A/B 复测：同夹具、同判据、改善/持平/退化三态显式标注）。
