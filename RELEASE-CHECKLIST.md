# 发行执行清单（v2.6.0）——流程简化 + 细则 294 + 机评路测（已发行 2026-09-09，Gitee 侧推后）

> 本 Agent 无发行 MCP：外部发布动作经用户批准后，由本会话按既定令牌供给机制逐渠道执行（L3 红线已满足：命令清单先行、经用户批准）。
> **版本沿革**：v2.0.0 / v2.0.1 / v2.0.2 为源码与口径批次（未发行）；v2.0.3-v2.0.6 已全渠道发行（2026-08-31）；**v2.1.0 / v2.1.1 / v2.2.0 已全渠道发行（2026-09-02 ×3）；v2.3.0 已全渠道发行（2026-09-03）；v2.4.0（内容并入 v2.5.0）与 v2.5.0 已于 2026-09-08 发行（GitHub/npm/ClawHub 1.0.12/About GH 侧；Gitee 侧挂起）**——发行回执见 项目信息.md §五 与 CHANGELOG；**v2.6.0 本次对外发（v2.5.0 的 Gitee 侧补发一并后置）**：**已发行 2026-09-09**——GitHub（Release + zip 资产 + main/tag v2.6.0）+ npm（`@2.6.0`）+ ClawHub（v1.0.13 pending-publication）+ About GitHub 侧；**Gitee 侧（Release/tag/About + v2.5.0 补发）推后**：待 Gitee API 令牌轮换后单独补发；CHANGELOG/README 发布面注记已回写。

## A. 本仓已备（随 git 提交）
- [x] 版本锁 2.6.0（package.json 2.6.0 / SKILL frontmatter 2.6.0 / README 徽章与版本历史行 / docs/project-info / reference-sources / EVIDENCE §九（9,723 字符实测）/ 项目信息 六·三 About 口径）
- [x] 内容 v2.6.0 全量本地批次：流程简化（开工六步→四步 / L2-F 11→9 / 更新序 6→4）+ #284 设计规范档前置 + #285 平台记忆分工 + 跨项目经验回流 #286-293 + 触达渠道修复 #294（detail_lookup 一键检索端口 + 部署工具化）+ 机评路测三场（EVIDENCE §十七-十九）+ 路测修复批次 F12-F17（detail_lookup 随包分发 / errpath 强化 / SessionStart hook / hooks 模板修正）
- [x] 正文口径净化 + 承载点口径（294 条/17 类 全仓一致）
- [x] verify-release 6/6 PASS（base=2.6.0，F 项索引完整性 294 全覆盖，零泄漏）
- [x] dist/shisan-xinuo-workflow-v2.6.0.zip（已打包 + Set-diff 双检：223,395B / 44 项 / personal=0 / memory=0）
- [x] 提交并推送 main + tag v2.6.0（commit f54e4cb → GitHub origin；Gitee 端推后）

## B. 全渠道发行回执（已批执行，2026-09-09）
| 渠道 | 产物/URL | 状态 |
|---|---|---|
| GitHub | 提交 f54e4cb + Release v2.6.0（附 dist zip） | ✅ f54e4cb..main + tag v2.6.0（走代理）；Release id=385171238 + zip 资产 id=551746289（223,395B uploaded） |
| npm | `@zxc663/shisan-xinuo-workflow@2.6.0`（GitHub Packages） | ✅ has_2.6.0=True，33 文件，Registry 复查 200 |
| Gitee | Release tag v2.6.0 + zip 附件 + v2.5.0 补发 | ⏳ 推后：用户明示本轮不做；Gitee API 令牌 401 失效 → 轮换后单独补发 |
| ClawHub | `shisan-xinuo-workflow@1.0.13`（内容 v2.6.0） | ✅ 已提交 pending-publication（待安全扫描确认） |
| About | GitHub 描述 PATCH | ✅ GitHub len=256（六·三 294 条口径，≤350 限制内压缩）；Gitee 侧 ⏳ 随补发 |
| skills.sh | 等待遥测/爬虫收录 | ⏳ |

## C. 复用要点
- 令牌供给：GitHub PAT 从机密文档 `<本机机密文档>`（路径不写出） 正则提取注入 env（`ghp_`），命令串与输出全程不含明文，用毕即清 env；回显仅 len/前缀。**本批新教训：Shell 工具每次调用为独立进程，`$env:GH_TOKEN` 不跨命令保留——凡用令牌的动作（push/Release/npm/About）必须「提取→注入→执行」同一命令内完成；首次 401 为提取污染（未 Trim），干净提取后有效（/user 200）。**
- GitHub push/Release/API 走代理 `http://127.0.0.1:33210`；Gitee 直连（本轮不做）。
- About description 限 350 字符（GitHub API 422「cannot be more than 350 characters」）——六·三文案过长时压缩核心保留（三级跑道/9 步/294 条 17 类/一档制/detail_lookup/触达端口/诚实口径）。
- dist 打包用 `scripts/build-dist.ps1`（+ Set-diff 双检）；Release 资产上传走 `uploads.github.com` + `-L`；REST JSON body 写文件用无 BOM UTF8。
- npm publish 用仓库 `.npmrc`（`${GITHUB_TOKEN}` 变量引用）→ `$env:GITHUB_TOKEN=<令牌>; npm publish`（NODE_AUTH_TOKEN/临时 userconfig 均未生效，GITHUB_TOKEN 环境变量法可行）。
- 发行完成后：**GitHub classic PAT 轮换**（v2.0.3 起遗留最高优先）→ 观察约 30 分钟（含 ClawHub 1.0.13 审核复查）→ 回执已写回本文件与 task-log。

## D. 观察期待办
- [ ] GitHub classic PAT 轮换（本批用毕即应轮换）
- [ ] ClawHub 1.0.13 security scans 通过复查
- [ ] Gitee 侧补发：v2.5.0（Release/tag/About）+ v2.6.0（Release/tag/About）待令牌轮换
- [ ] 注入副本新会话在场验收（`在场提示 · v2.6.0` 关键词）