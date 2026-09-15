# scripts/evals · 路测判分与探针随仓件（P1，2026-09-16 立）

> 目的：把「纪律被验证」的可复跑工件收进仓库（对标 superpowers-evals / PRP validation-gate 共识形态；缺口判定见 docs/audit-v290-review-20260916.md §四 C1 与 docs/comparison-v290-analysis-20260916.md §四）。
> 本目录=仓库工具层（同 facts_sync.py 定位），**不属于 skill 交付物包**（不进 dist zip，不影响发行冻结面）。

## 组成

| 文件 | 用途 |
|---|---|
| `extract_roadtest.py` | 无头路测判分解析器（rollout 逐请求解析；v12 判分器收编通用化） |
| `probe_detail_lookup.py` | detail_lookup 召回探针（24 用例关键词→期望细则编号；兑现发行面「探针 24/24」承诺的随仓可复跑件） |
| `fixtures/s-lite/` | 最小无头会话夹具（复用型：复制后跑 `zcode -p`） |

## 无头路测最小流程（v12 实证版）

```bash
# 1) 驱动（模板；prompt/fixture 按轮换）
node <ZCode>/resources/glm/zcode.cjs -p "<prompt>" --cwd <fixture> --json > runs/<tag>.out.json
# 2) 判分（会话一结束立即跑——rollout 分钟级清刷！）
python scripts/evals/extract_roadtest.py <tag> <session-id> [--root D:/roadtest-vN]
# 3) 召回探针（任意时点可重跑）
python scripts/evals/probe_detail_lookup.py
```

## 判分口径要点（v12 三发现，判分器已内建）

1. **rollout 格式（ZCode 3.12.1）**：`messages` 在 `request.messages`（不在 body）；兼容双位读取。
2. **rollout 分钟级轮转清刷**：会话结束立即 extract，「跑一个判一个」是生存必需。
3. **NQ-5 按面分治**：GUI 面=messages[0]；无头面=AGENTS.md 注入块＋SessionStart/UserPromptSubmit hooks 纪律包（槽位任意，判分器扫全前缀消息并记录槽位）。
4. 好坏同列；N 小不设通过线；结论按描述性证据落 scorecard。
