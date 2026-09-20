# 贡献指南 · Contributing

> 本仓库 = 十三希诺 Agent 工作流 Skill 的源库（唯一中文版单版本化）。欢迎一切形式的核对、指正与贡献。

## 可以做什么

- **口径核对**：本项目的证据自持度高（EVIDENCE.md / docs/roadtest-scorecards/ 全部机证可重跑），欢迎对任何数字（细则条数/通过率/回执）做交叉核对——发现不一致请开 issue，附上你的核对过程（像 issue #1 那样）。
- **细则反馈**：某条款在你的平台/场景不适用或触发不良行为 → 开 issue 附会话证据。
- **平台适配**：新平台注入点/技能目录的适配经验。
- **代码**：`scripts/` 下的 harness（探针/门禁/部署/同步）与 `templates/hooks/`。

## 提交前自查

1. `powershell -File scripts/verify-release.ps1` → **8/8 ALL PASS**（含判据自测 23/23，judge j2.5）
2. `python scripts/facts_sync.py --check` → PASS（条数/类数/编号上限全仓一致）
3. 判据改动（`scripts/probe_runner.py`）必须 bump `JUDGE_VERSION` + 过 `--judge-selftest` + 在 `docs/roadtest-scorecards/JUDGELOG.md` 留变更记录；方向只许修「不识别合规形态」，收紧/放宽须先开 issue 裁决。
4. 细则改动先 grep 查重（`references/details.md` 头部防棘轮规则），新增条目必须入症状索引。
5. 正文（skill/ 下）只写规则本身 + ≤1 句为什么；出处/日期/拍板过程只入 `项目信息.md`（决策史层）。
6. 引用细则用完整前缀 `details #N`（禁裸 `#N`，与 GitHub issue 编号同形异义）。

## 语义化版本

- 规则语义变化（新条款/判级变化/判据修订）→ minor；笔误/文案 → patch；结构性重构 → major。

## 安全问题

见 [SECURITY.md](SECURITY.md)——不要在公开 issue 里发安全问题。

## 环境注意

- Windows 优先（hooks/部署脚本含 PowerShell）；`.gitattributes` 已固定文本文件 LF——请勿关闭 `core.autocrlf` 之外的行尾转换手段，保持检出与 blob 一致。
- 语言：Skill 本体仅中文；README 中文优先 + English summary；issue/PR 可中英任一。
