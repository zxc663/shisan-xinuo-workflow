# 发行执行清单（v2.0.6）——项目承载 + 授权边界修复批次全渠道发行

> 本 Agent 无发行 MCP：外部发布动作经用户批准后，由本会话按既定令牌供给机制逐渠道执行（L3 红线已满足：命令清单先行、经用户批准）。
> **版本沿革**：v2.0.0 / v2.0.1 / v2.0.2 为源码与口径批次（未发行）；v2.0.3、v2.0.4 已全渠道发行（2026-08-31）；v2.0.5（路测回流批次）与 v2.0.6（项目承载+授权边界批次）为本地批次（本台账为 **v2.0.6 发行面**），详情见 项目信息.md §五 与 memory/task-log。

## A. 本仓已备（随 git 提交）
- [x] 版本锁 2.0.6（package.json / SKILL frontmatter / README 徽章与版本历史行 / CHANGELOG v2.0.6 行 / 项目信息 §三·§五 / reference-sources / scripts-README 预期输出 / EVIDENCE §九·§七）
- [x] 项目承载 + 授权边界修复源码（本地 commit 56ee989，**未推送**）：部署第五层「项目承载检查」、授权边界分级（项目内写文件=自动动作）、§2.5 触发存在性判定、开工四动作写死、Base directory 根因现场修复（`.bak-*` 迁 skill-backups/）
- [x] 本机注入副本 ×4 重部署 v2.0.6（先备份，含在场提示）
- [x] verify-release 4/4 PASS（base=2.0.6，零泄漏）
- [x] dist/shisan-xinuo-workflow-v2.0.6.zip（staging 暂存目录法重建，Set-diff 双检）
- [ ] 提交并推送双端 main（origin GitHub / gitee Gitee，本地 85 commits vs 远端 78，领先 7）；tag v2.0.6 待推

## B. 全渠道发行回执（待用户批准后执行）
| 渠道 | 产物/URL | 状态 |
|---|---|---|
| GitHub | Release v2.0.6（附 dist v2.0.6.zip，走代理） | ⏳ 待批 |
| npm | `@zxc663/shisan-xinuo-workflow@2.0.6`（GitHub Packages） | ⏳ 待批 |
| Gitee | Release tag v2.0.6 + zip 附件（直连） | ⏳ 待批 |
| ClawHub | `shisan-xinuo-workflow@1.0.7`（内容 v2.0.6） | ⏳ 待批 |
| About | GitHub+Gitee 仓库描述 PATCH v2.0.6 | ⏳ 待批 |
| skills.sh | 等待遥测/爬虫收录 | ⏳ |

## C. 复用要点
- 令牌供给：GitHub/github PAT 与 Gitee token 从机密文档经正则提取注入 env，命令串与输出全程不含明文，用毕即清 env；回显仅 len/前缀。
- Gitee 建 Release 必须带 `target_commitish=main`（否则 400）；**附件上传 `POST /releases/{id}/attach_files` 用 `curl.exe -F access_token=… -F file=@…zip`**，勿用 `Invoke-RestMethod -Form`（PS7 该 multipart 文件字段会致 Gitee 返回 40001 登录失效）。
- ClawHub 发布路径= skill 子目录（含 SKILL.md）；走红海代理 `127.0.0.1:33210`。
- GitHub push/fetch/API 走代理 `http://127.0.0.1:33210`；Gitee 直连。
- 发行完成后：**GitHub classic PAT 轮换**（v2.0.3 起遗留最高优先：重新生成 → 更新 D:\Agent个人资源\机密资源\02-Gitee与GitHub.txt → 旧作废）→ 观察约 30 分钟（含 ClawHub 1.0.6/1.0.7 审核复查）→ 回执写回本项目文件与 task-log。
