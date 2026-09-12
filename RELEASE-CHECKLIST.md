# 发行执行清单（v2.7.1）——补丁版发行完成（2026-09-12 全渠道：GitHub/Gitee/npm/ClawHub/About 文案同步；Gitee v2.5.0/v2.6.0/v2.7.0 补发完成）

> 本 Agent 无发行 MCP：外部发布动作经用户批准后，由本会话按既定令牌供给机制逐渠道执行（L3 红线已满足：命令清单先行、经用户批准）。
> **版本沿革**：v2.6.0 已全渠道发行（2026-09-09，Gitee 侧推后；回执见 项目信息.md §五 与 CHANGELOG）。**v2.7.0 = 全程批次定稿（2026-09-12 已发行 GitHub 侧；Gitee 侧暂缓）**：条款六销项 + 注入核心瘦身 5,991 字符 + hooks 纪律包注入 + 判例审入（活跃 314 条）+ 路测 v5/v6/v7/v8（无头面注入断裂发现 + 必问底线十维 + 修正效力验证 + 接手全景）+ 必问十维扩充 + 评审与接手批（#312-316）+ 复杂度减法批（project-rules 压缩 / GATE 一行式 / 降采样合法化）+ 口径净化批（头部 314 全仓同步 / README 重构 + 架构图 v2.7 口径重绘）+ 真会话回归 S0/S7。
> **待办前置**：Gitee API 令牌 2026-09-12 已轮换（32-hex 有效）→ v2.5.0/v2.6.0/v2.7.0/v2.7.1 四版已补发完成；**残留待办 = ClawHub scans 复查 + GitHub classic PAT 轮换**。

## A. 本仓已备（随 git 提交）
- [x] 版本锁 2.7.0（package.json / SKILL frontmatter / README 徽章与版本历史行 / docs/project-info / reference-sources / AGENTS.md 基线行 / 项目信息 §六·三 About 口径 314）
- [x] 内容 v2.7.0 全量：批 0 基线冻结（tag `pre-v270-redesign`）+ 批 1 条款六销项（GATE 9 字段单源 / errpath 事后化 / lookup 修复模板 / 状态行 / 微轮次豁免 / 记忆路由）+ 批 2 注入瘦身（11,560→5,203 字符，在场提示 ×1 单源）+ 批 3 hooks 纪律包（SessionStart + PostToolUseFailure，机证三通道）+ 批 4 数据工具面（判例审入 #296-#305 / #180 归档并入 #232 / syncer 旧锚清扫 / Trae 旧锚已清）+ 批 5 收口（本清单雏形）+ 路测 v6 修正批（必问底线 + #306-311）+ 必问十维扩充（#306）/ 评审与接手批（#307 场景化 / #312-316，活跃 309→314）+ 复杂度减法批（project-rules 2.4K→1.08K / GATE 一行式定版 / 降采样合法化，条款 314 不变）+ 口径净化批（头部 313→314 全仓同步 / #315 去重 / 三级同步链修复 / README 大重构）
- [x] 承载点口径（活跃 314 条/17 类 全仓一致；#295 预留槽 / #180 归档占号不计入）
- [x] verify-release 6/6 PASS（base=2.7.0，F 项 316 编号全覆盖，核心字符 5,991≤6,000，零泄漏）
- [x] dist/shisan-xinuo-workflow-v2.7.0.zip（已打包 + Set-diff 双检：249,132B / 46 项；架构图重绘+README 同步后复打）
- [x] 五副本重部署 v2.7.0（备份 `.bak-20260912-pre-v2.7.0`，--check --version 严格 5/5 PASS count=314）+ syncer 双副本 exit=0（.agents 主 + .workbuddy --dest）
- [x] 真会话回归 S0/S7（computer-use 交互新会话：注入在场 v2.7.0 + hooks 纪律包双通道机证 + GATE 9 字段行为化）+ 无头冒烟对照
- [x] **提交 main（本地 commit）** ← 全程批次 commit 已落（e2e0f56 最新）；**push 单独批准**

## B. 全渠道发行命令清单（GitHub 侧五渠道 2026-09-12 已执行 ✅；Gitee/PAT 待办）
> 令牌供给：GitHub PAT 从机密文档（路径不写出）正则提取注入 env（`ghp_`），命令串与输出全程不含明文，用毕即清；**提取→注入→执行必须同一命令内完成**（Shell 每调用独立进程）。GitHub 全部走代理 `http://127.0.0.1:33210`。

| # | 渠道 | 命令要点 | 状态 |
|---|---|---|---|
| 1 | push | `git push origin main` + `git tag v2.7.0 <commit> && git push origin v2.7.0`（走代理） | ✅ 2026-09-12 完成（a895aae..de25335；tag v2.7.0=de25335） |
| 2 | GitHub Release | 创建 Release v2.7.0（标题+要点取 CHANGELOG 行）+ 上传 dist zip（`uploads.github.com` + `-L`；REST JSON body 无 BOM UTF8） | ✅ 完成（release id=387465622；zip 249,132B uploaded） |
| 3 | npm | `$env:GITHUB_TOKEN=<令牌>; npm publish`（仓库 `.npmrc` 的 `${GITHUB_TOKEN}` 变量引用法） | ✅ 完成（@zxc663/shisan-xinuo-workflow@2.7.0，GitHub Packages） |
| 4 | ClawHub | `shisan-xinuo-workflow@1.0.14` update submitted（内容 v2.7.0，pending security scans） | ✅ 提交成功（1.0.14，pending-publication；scans 待复查） |
| 5 | About | GitHub 侧 PATCH（**用 项目信息.md §六·三 PATCH 压缩版 241 字符 ≤350**；完整版仅作口径基准） | ✅ PATCH 成功（desc_len=241；注入核心口径已校 5,203→5,991） |
| 6 | Gitee | Release v2.7.0 + tag + About ⏳ **与 v2.5.0/v2.6.0 补发一并**（令牌轮换后） | ⏳ **暂缓**（用户 09-12 裁定；机密文档仅 32-hex 旧格式已失效，待 43 字符新令牌） |
| 7 | PAT 轮换 | 发行完成即 GitHub classic PAT 轮换（v2.0.3 起遗留最高优先） | ⏳ **待执行**（发行动作完成；用户生成新 PAT → 更新机密文档 → 旧作废） |

## C. 复用要点（v2.6.0 实证沿用）
- About description 限 350 字符（GitHub API 422）——v2.7.0 已备压缩版（§六·三）。
- dist 打包 `scripts/build-dist.ps1`（Set-diff 双检）；Release 资产上传走 `uploads.github.com` + `-L`；REST JSON body 写文件用无 BOM UTF8。
- npm publish 用 GITHUB_TOKEN 环境变量法（NODE_AUTH_TOKEN/临时 userconfig 均未生效）。
- 泄漏扫描面=与 dist 同集合；`__pycache__`/`*.pyc` 排除（H3/M 组修复沿用）。
- 验收看平台解析到的 Base directory，非文件版本号（#239）。

## D. 观察期待办（发行后）
- [ ] 发行回执写回本文件 B 表 + 项目信息.md §五 + CHANGELOG（B 表已回执 ✅；§五/CHANGELOG 同批）
- [ ] 注入副本新会话在场验收（`在场提示 · v2.7.0` 关键词；本批 S0 已真会话预验，发行后复验一次）
- [ ] ClawHub 1.0.14 security scans 通过复查（pending-publication 已提交，等扫描）
- [ ] Gitee 侧补发三版：v2.5.0 / v2.6.0 / v2.7.0（Release/tag/About，待令牌轮换——用户裁定暂缓）
- [ ] skills.sh 遥测收录核查
- [ ] WorkBuddy 侧 H0（用户侧新会话输 `zxc663` 验收）+ 面 F WorkBuddy 侧时点（等面 M H0 过）
- [x] GitHub 侧五渠道已发（push/tag/Release+zip/npm/About；2026-09-12 13:xx）
