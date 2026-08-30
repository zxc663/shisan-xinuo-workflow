# 发行执行清单（v2.0.4）——三层承载化 + 取证命令修复批次全渠道发行

> 本 Agent 无发行 MCP：外部发布动作经用户批准后，由本会话按既定令牌供给机制逐渠道执行（L3 红线已满足：命令清单先行、经用户批准——2026-08-31 用户消息「v2.0.4 发行面（npm/GitHub Release 等）批准」）。
> **版本沿革**：v2.0.0 / v2.0.1 / v2.0.2 为源码与口径批次（未发行）；v2.0.3 已全渠道发行（2026-08-31）；v2.0.4 为**发行面最新**（本台账），详情见 项目信息.md §五 与 memory/task-log。

## A. 本仓已备（随 git 提交）
- [x] 版本锁 2.0.4（package.json / SKILL frontmatter / README 徽章与版本历史行 / CHANGELOG v2.0.4 行 / 项目信息 §三·§五 / reference-sources / scripts-README 预期输出 / EVIDENCE §九·§七）
- [x] 三层承载化 + 取证命令修复源码（1a91db1，已推 GitHub/Gitee main）：记忆层在场提示锚点（templates/memory-anchor.md）、SKILL §3 三层语义 + 步骤 1.5、install-skill.ps1 `-MemoryFile`、syncer.py `--memory-target`、取证命令修复（SKILL §11 / workflows / details 引用规范）、EVIDENCE §七复测
- [x] 本机三层实测注入：WorkBuddy MEMORY.md + Trae user_profile.md 记忆层锚点、注入副本 ×4 重部署 v2.0.4（含在场提示）、USER.md 标识确认 zxc663、部署副本 ×2 syncer 同步——均备份 `.bak-20260831-pre-v204` / skill-backups/
- [x] verify-release 4/4 PASS（base=2.0.4，零泄漏，重跑确认）
- [x] dist/shisan-xinuo-workflow-v2.0.4.zip（staging 暂存目录法重建，Set-diff 双检）
- [x] 提交 1a91db1（A–D 源码+口径），GitHub/Gitee 双端 main 已推送；tag v2.0.4 待推送

## B. 全渠道发行回执（2026-08-31，已执行）
| 渠道 | 产物/URL | 状态 |
|---|---|---|
| GitHub | https://github.com/zxc663/shisan-xinuo-workflow/releases/tag/v2.0.4 （附 dist v2.0.4.zip） | ✅ |
| npm | `@zxc663/shisan-xinuo-workflow@2.0.4`（GitHub Packages，latest） | ✅ |
| Gitee | https://gitee.com/zxc663/shisan-xinuo-workflow/releases （tag v2.0.4 + zip 附件） | ✅ |
| ClawHub | `shisan-xinuo-workflow@1.0.6`（pending scans，内容 v2.0.4） | ✅ 待公开 |
| About | GitHub+Gitee 仓库描述 PATCH v2.0.4（200/200） | ✅ |
| skills.sh | 等待遥测/爬虫收录 | ⏳ |

## C. 复用要点
- 令牌供给：GitHub/github PAT 与 Gitee token 从机密文档经正则提取注入 env，命令串与输出全程不含明文，用毕即清 env；回显仅 len/前缀。
- Gitee 建 Release 必须带 `target_commitish=main`（否则 400）；**附件上传 `POST /releases/{id}/attach_files` 用 `curl.exe -F access_token=… -F file=@…zip`**，勿用 `Invoke-RestMethod -Form`（PS7 该 multipart 文件字段会致 Gitee 返回 40001 登录失效）。
- ClawHub 发布路径= skill 子目录（含 SKILL.md）；走红海代理 `127.0.0.1:33210`。
- GitHub push/fetch/API 走代理 `http://127.0.0.1:33210`；Gitee 直连。
- 发行完成后：**GitHub classic PAT 轮换**（v2.0.3 遗留最高优先：重新生成 → 更新 D:\Agent个人资源\机密资源\02-Gitee与GitHub.txt → 旧作废）→ 观察约 30 分钟（含 ClawHub 1.0.6 审核复查）→ 回执写回本项目文件与 task-log。