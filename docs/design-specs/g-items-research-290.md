# G 清单 4 点调研档（2.9 修正批前置调研 · 2026-09-15）

> 依据：roadtest-v272-plan.md §6.3「修订批施工前先跑 4 项调研（G01/G04/G05/G09，≤90min）再落条文」。
> 本文=调研底稿（出处/证据），条文施工落 references/ 时只写规则本身（维护纪律：史料不入正文）。

## G01 项目文档成文规范 → Diátaxis（已调研 2026-09-15）

- **行业基准（已核实）**：Diátaxis 官方四象限——tutorial（学习导向）/how-to（目标导向）/reference（信息导向）/explanation（理解导向）；两轴=技能习得 vs 技能应用 × 学习 vs 信息。关键实践：**不混型（不把四种写进一份文档）优先于覆盖全四象限**（Python 官方社区采纳讨论同结论）。arc42=重架构文档模板，agent 写项目文档场景过重，仅作重型架构档注记不立条。
- **证据**：diataxis.fr（官方）＋discuss.python.org 采纳讨论＋ubuntu.com 采纳记。
- **条文落点草案**：details 新条（文档域）——项目文档按 Diátaxis 分型：README=快速上手（What/Install/Usage，tutorial+reference 混合最小集但各节单型）；docs/ 按型分文件（how-to/reference/explanation 不混写）；一份文档只服务一种阅读意图，混合内容拆文件；文档与代码同批提交（承接 rules #36 扩展）。
- **模板挂接**：新项目最小文档集=README+docs/project-info.md+docs/design-specs/（涉设计时）——与 #284 设计档前置承接，优先走 templates/ 承载（face G n=13 项目级承载有效实证）。

## G04 依赖选型与版本策略 → 锁文件（已调研 2026-09-15）

- **行业基准（已核实）**：**应用必提交 lockfile**（package-lock.json/pnpm-lock.yaml/uv.lock/Pipfile.lock/poetry.lock/Cargo.lock）；CI 用严格安装（npm ci/cargo build --locked/poetry install 默认尊重锁）；lockfile diff 纳入 review（防供应链投毒与意外升级）；**库（library）例外**——npm 生态传统省略（消费方自解析依赖树），Cargo 现代建议库也提交；manifest 保留 SemVer 范围（^/~），锁文件钉精确版本+完整性哈希。
- **证据**：stackoverflow.com 基准问答＋oneuptime.com 2026-01 指南＋dev.to 语义化版本实践风险分析＋cyberphinix.de 格式对比。
- **条文落点草案**：details 新条（依赖域）——引入依赖前 ≥2 候选四行对比（功能/维护活跃/体积/许可）落设计档；应用项目 lockfile 必提交、CI 严格安装模式；库项目可豁免但须显式声明；版本范围禁裸 `*`；lockfile diff 独立可辨识（不与功能改动混提）；升级走独立小任务。

## G05 应用安全基线 → OWASP Top 10:2025（已调研 2026-09-15 · 榜单已换代）

- **重大更新（已核实官网）**：**OWASP Top 10:2025 已正式发布**（top10.owasp.org/2025），v272-plan §6.2 G05 草案所引 2021 版已过时。2025 榜单：
  A01 Broken Access Control｜A02 Security Misconfiguration（⬆）｜**A03 Software Supply Chain Failures（新入）**｜A04 Cryptographic Failures｜A05 Injection｜A06 Insecure Design｜A07 Authentication Failures｜A08 Software or Data Integrity Failures｜A09 Security Logging and Alerting Failures｜**A10 Mishandling of Exceptional Conditions（新入）**。
  2021→2025 变化：SSRF、Vulnerable and Outdated Components 移出（供应链条目吸收）；A10「异常条件处理失当」新入=与本项目「空 catch 零容忍/日志三件套」直接互证（外部权威榜单背书）。
- **证据**：top10.owasp.org/2025（官方榜单全名）＋fastly.com/cybersecuritynews.com/qualys.com 变化解读三源一致。
- **条文落点草案**：security.md 新节（应用安全域）——L2-F 涉用户输入/认证/存储/外部调用必过 OWASP 2025 十项一行自查；默认参数化查询（A05）；输出转义（XSS 并入 A02/A06 面）；会话 cookie HttpOnly+Secure（A07）；依赖引入承接既有 security.md §1.5（A03 供应链）；异常必须处置禁空 catch（A10，与注入核心 TOP 呼应）；访问控制默认拒绝（A01）。

## G09 性能预算 → Core Web Vitals（已调研 2026-09-15）

- **行业基准（已核实）**：LCP ≤2.5s｜**INP ≤200ms**（2024-03 正式替代 FID）｜CLS ≤0.1——均为真实用户 75 分位口径；2026 年阈值无变化（web.dev/articles/vitals 官方）。needs-improvement 区间：LCP 2.5-4.0s/INP 200-500ms/CLS 0.1-0.25。
- **证据**：web.dev（官方）＋developers.google.com/search 文档＋nitropack.io 2026 指南——三源一致无阈值变动。
- **条文落点草案**：details 新条（性能域）——UI 项目设计档附性能预算三行（LCP≤2.5s/INP≤200ms/CLS≤0.1）并进验收标准；CLI/exe 项目=扫描耗时上限+内存上限两行；预算未达标=验收不通过（与「验收 3-5 条可验证」承接）。

## 施工挂接总表

| G 点 | 调研态 | 条文去向 | 承载文件 |
|---|---|---|---|
| G01 | 已调研 | 文档域新条 | references/details.md + templates/bootstrap 承接 |
| G04 | 已调研 | 依赖域新条 | references/details.md |
| G05 | 已调研（榜单换代 2021→2025） | 应用安全域新节 | references/security.md |
| G09 | 已调研（INP 替 FID 口径确认） | 性能域新条 | references/details.md |
