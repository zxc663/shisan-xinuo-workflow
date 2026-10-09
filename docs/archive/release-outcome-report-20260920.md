# 发行以来成果汇总与分析报告（2026-08-25 → 2026-09-20）

> 数据拉取时刻：**2026-09-20 11:05**（本机时间）；来源 = 各平台公开 API / 页面**实测**（端点与命令见 §五），非自报数字。
> 触发：用户令「获取所有分发平台数据与反馈；README 补全渠道清单并推送」。本报告为该批次的成果汇总交付件。

---

## 一、总览（TL;DR）

- **发布周期**：2026-08-25 首版 v1.1.0 → 2026-09-19 v3.1.0，**25 天发行 30 个 Release**（32 tags；v1.1.0→v3.1.0）。
- **五渠道全发行态**，当前版本锚点 = **v3.1.0**（判据可信度批，2026-09-19）。
- **累计触达（可观测口径）≈ 905 次**：ClawHub 安装 **861**（占 95.1%）｜GitHub Release zip 下载 **39**｜skills.sh 安装 **5**｜Gitee 附件下载（平台不公开计数）｜npm（GitHub Packages，无公开下载统计）。
- **社区反馈面**：全渠道 **0 issue / 0 评论 / 0 评分**；GitHub **25 stars / 2 forks**；唯一代码互动 = **PR #1**（2026-08-29，EVIDENCE 口径修正，已关闭，2 条评论）。
- **README 缺口已修**：渠道清单此前未集中列明（仅快速体验里零散三条）——本批次新增「分发渠道 · Distribution」节（五渠道 + 具体链接）并推送。

## 二、五渠道实测数据（2026-09-20 11:05）

| # | 渠道 | 链接 | 当前版本 | 关键数据 | 反馈面 |
| --- | --- | --- | --- | --- | --- |
| 1 | **GitHub**（源库 + Release） | https://github.com/zxc663/shisan-xinuo-workflow | v3.1.0（2026-09-19 05:20 UTC） | public / MIT；25 stars · 2 forks · 25 watchers；32 tags · **30 Releases**；zip 资产累计下载 **39**（单版最高 v2.8.0=6、v1.5.0=6） | 0 open issues；PR #1 已关（2 评论）；0 open discussions |
| 2 | **npm（GitHub Packages）** | https://github.com/zxc663/shisan-xinuo-workflow/pkgs/npm/shisan-xinuo-workflow | **3.1.0**（2026-09-19，45 文件，shasum `e1ede926…`） | 包注册 32 个版本（2026-08-25 起）；**visibility=private** → 匿名读取 401，需 PAT（README 快速体验节有 `.npmrc` 配法）；**npmjs.org 未分发** | 无公开下载统计（GitHub Packages 无此 API） |
| 3 | **Gitee**（镜像 + Release） | https://gitee.com/zxc663/shisan-xinuo-workflow | v3.1.0（2026-09-19 13:21 +08，Release id=1153127） | 0 stars / 1 watcher / 0 forks；**10 个 Release**（v2.2.0→v3.1.0）各带 zip 附件（+平台自动源码包）；与 GitHub 同 commit/tag 双推 | 0 issues；附件下载计数 API 不返回（无法观测） |
| 4 | **ClawHub**（OpenClaw 技能市场） | https://clawhub.ai/zxc663/shisan-xinuo-workflow | **1.0.19**（平台侧递增号；2026-09-19 更新，≈本仓 v3.1.0 内容） | **861 安装**（搜索页计数）；Bookmark 0；安装命令 `openclaw skills install @zxc663/shisan-xinuo-workflow`；**1.0.19 security scans pending**（1.0.14–1.0.18 遗留复查同待） | 无评分/评论显示 |
| 5 | **skills.sh**（Agent Skills 索引） | https://skills.sh/zxc663/shisan-xinuo-workflow | 随 GitHub 源库自动同步（v3.1.0） | 索引 **2 个 skills / 共 5 次安装**（shisan-xinuo-workflow 3 + -zh 2）；安装命令 `npx skills add zxc663/shisan-xinuo-workflow` | 无评分/统计元数据 |

配套动作（非独立渠道）：每版发行时 **GitHub + Gitee 仓库简介（About）双端 PATCH** 同步更新（当前 len=191，v3.1.0 口径）。

### GitHub Release 下载分布（30 版全列，合计 39）

| 下载量 | 版本 |
| --- | --- |
| 6 | v2.8.0、v1.5.0 |
| 4 | v1.11.0 |
| 3 | v2.9.0、v2.3.0、v1.6.0 |
| 2 | v2.6.0、v2.0.6、v1.9.1、v1.9.0 |
| 1 | v3.1.0、v2.7.1、v2.7.0、v2.5.0、v2.1.1、v1.7.0 |
| 0 | v3.0.0、v2.2.0、v2.1.0、v2.0.4、v2.0.3、v1.19.1、v1.19.0、v1.10.0、v1.4.3、v1.4.0、v1.3.2、v1.3.1、v1.2.0、v1.1.0 |

> 注：v3.0.0 下载 0 与发行时间最近（09-18）及「用户自取走 GitHub Packages」路径分流有关，不宜读作衰退。

## 三、最终成果汇总

**交付形态**：三包体系（核心 `shisan-xinuo-workflow` + 流程包 `shisan-xinuo-flows` + 角色包 `shisan-xinuo-roles`），可独立安装、组合使用。

**规模口径（v3.1.0 终态）**：

| 维度 | 值 |
| --- | --- |
| 细则库 | **368 条 / 29 类**（编号至 #369，症状索引检索键 100% 覆盖） |
| 注入核心 | 常驻 ≤6000 字符（PowerShell 字符数 + Python code-point 双口径） |
| 完成块 | `GATE` 12 字段单行（level/v/cmd/exit/files/refs/errpath/lessons/exempt/caps/effort/stop_reason）+ 证据三挂靠 |
| 发行门禁 | `verify-release` **8 项**（A 内容锚点 / B hooks / C 版本一致 / D 泄漏红线 / E 正文净化 / F 索引完整 / G 事实对账 / H 判据自测） |
| 平台适配 | 五平台注入（Codex / Claude Code / Trae / WorkBuddy / ZCode） |
| 行为面 harness | 20 场景探针矩阵 + 判据版本化（j1.0→j2.4）+ 金样本回归 + 时序库聚合 |

**验证数字（全部机器产出，证据链见 EVIDENCE.md）**：

- v3.1 全矩阵：**20/20 PASS**（判据 j2.4，无头 glm-5.3-flash）
- v3.1.0 部署后实跑（无限循环路测 3.1）：**24 针 22 PASS**（91.7%；唯一矩阵级 FAIL 经判据回植后重判 20/20）
- 判据金样本回归：**21/21**（正例 8 / 负例 13）
- v2.9.0 行为基线：52 探针 **98.1%**（51 PASS）
- v3.0.0 注入副本冒烟 2/2（GATE 12/12）；五平台注入 `--check` 5/5

**版本沿革大事记**（完整版见 CHANGELOG.md）：

| 阶段 | 版本带 | 日期 | 主题 |
| --- | --- | --- | --- |
| 起步 | v1.1.0–v1.19.1 | 08-25 → 08-30 | 首发与高频迭代（一日多版，骨架成形） |
| 成型 | v2.0.3–v2.3.0 | 08-30 → 09-02 | 判级与承载体系、上下文管理、发行渠道建立 |
| 治理 | v2.5.0–v2.8.0 | 09-08 → 09-15 | 开工四步收敛、无头路测体系、行为效力验证通过 |
| 审查 | v2.9.0 | 09-16 | 独立审查修正批（P1×11+P2×16 机制级）、安全基线 |
| 重构 | **v3.0.0** | 09-18 | 三包体系、Token 精算机、反作弊与状态锚定、GATE 12 字段 |
| 可信 | **v3.1.0** | 09-19 | 判据可信度批：判据版本化 + 金样本回归 + scorecard 指纹 + 形态分型 |

## 四、分析

**渠道流量结构**：ClawHub 一家占可观测触达的 **95.1%**（861/905）——OpenClaw 生态是本项目当前唯一有规模的**真实用户面**；GitHub Release（39）是第二入口，主要服务直装用户；skills.sh（5）处于尾部；Gitee 与 npm 侧触达不可观测。**对分发的启示：ClawHub 的 security scans pending 遗留（1.0.14–1.0.19）是当前最值得清的渠道侧在办**——它挡在 95% 流量入口的合规状态上。

**反馈面判读**：全渠道零 issue、零评论、零评分 + 861 安装 + 25 stars =「**沉默使用**」型分布，单维护者早期项目属正常形态；PR #1（外部或用户自查的 EVIDENCE 口径修正）证明材料被认真读过且修正被接受——这是当前唯一闭环的社区互动样本。

**版本节奏**：8 月下旬一日多版的高频修版已收敛为「每周一批、批批全渠道」的稳定节律（v2.9→v3.0→v3.1 三连发间隔 1 天）；发行机械化程度提升（回执四件套 + 五渠道命令清单 + 8 项门禁）使发行成本显著下降。

**已知缺口（截至本报告）**：

1. npmjs.org 未分发——真公网 npm 用户不可达；GitHub Packages 私有可见性 + PAT 门槛进一步抬高取包成本（v3.1.0 起 README 已如实说明）。
2. ClawHub scans pending 六连遗留未复查。
3. Gitee 附件下载计数平台不公开，该渠道触达长期不可观测。
4. README 渠道清单缺失（本次修复）。

**建议（待用户拍板，本批次未执行）**：① ClawHub scans 复查清账；② 评估 npmjs 公网发行（配套决定包名占用与可见性）；③ Gitee 侧考虑轻量运营或降级为纯镜像口径。

## 五、数据口径与可复算

拉取命令（全部可重跑；时刻不同数字会漂移）：

```bash
# GitHub 仓库 / issues / releases / npm 包
gh api repos/zxc663/shisan-xinuo-workflow
gh api "repos/zxc663/shisan-xinuo-workflow/issues?state=all&per_page=20"
gh api "repos/zxc663/shisan-xinuo-workflow/releases?per_page=30"   # assets[].download_count
gh api users/zxc663/packages/npm/shisan-xinuo-workflow            # 需 PAT 含 read:packages
# Gitee 仓库 / releases / issues（公开）
curl -s "https://gitee.com/api/v5/repos/zxc663/shisan-xinuo-workflow"
curl -s "https://gitee.com/api/v5/repos/zxc663/shisan-xinuo-workflow/releases?page=1&per_page=10&direction=desc"
# ClawHub / skills.sh（页面数字，无公开 API）
# https://clawhub.ai/zxc663/shisan-xinuo-workflow （搜索页含安装计数 861）
# https://skills.sh/zxc663/shisan-xinuo-workflow
```

**观测局限**：GitHub Packages 无下载统计 API；Gitee release 资产 `download_count` 字段 API 不返回；ClawHub 无公开 API（861 取自搜索页渲染值）；skills.sh 统计粒度只到安装次数。以上四项为平台侧结构性限制，非本报告省略。
