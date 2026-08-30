# 发行执行清单（v2.0.3）——前缀自适配 + 平台配置文件层批次全渠道发行

> 本 Agent 无发行 MCP：外部发布动作经用户批准后，由本会话按既定令牌供给机制逐渠道执行（L3 红线已满足：命令清单先行、经用户批准）。
> **版本跳档说明（2026-08-31）**：发行面从 **v1.19.1 直跳 v2.0.3**——v2.0.0 / v2.0.1 / v2.0.2 均为源码与口径批次（未对外发行，用户拍板跳过），详情见 项目信息.md §五 与 memory/task-log/2026-08-31-v2.0.3-批次计划.md。

## A. 本仓已备（随 git 提交）
- [x] 版本锁 2.0.3（package.json / SKILL frontmatter / README 徽章与版本历史行 / CHANGELOG v2.0.3 行 / 项目信息 §三·§五 / reference-sources / scripts-README 预期输出 / EVIDENCE §九重测）
- [x] scripts/install-skill.ps1 新增（agent- 前缀自适配一键安装，正反向实测通过：临时目录安装 / 二次存在提示 / -Force 备份覆盖 / -Dry 干跑）+ scripts/README 〇节文档
- [x] SKILL §3 第 0 步安装名前缀自检 + 注入点承载面句；platform-adaptation §2.1 平台配置文件层（逐项实测标注）；templates/hooks/README.md 多平台说明
- [x] 本机配置层全激活：~/.codex AGENTS.md 重写 v2.0.3（原 v1.19.1 英文旧版）、注入副本 ×4 重部署（~/.zcode、~/.trae-cn、~/.workbuddy、~/.codex）、部署副本 ×2 syncer 同步（~/.agents/skills、~/.workbuddy/skills），均先备份 `.bak-20260831-pre-v203`
- [x] verify-release 4/4 PASS（base=2.0.3，零泄漏）
- [x] dist/shisan-xinuo-workflow-v2.0.3.zip（staging 暂存目录法重建，Set-diff 双检）
- [x] 提交 <COMMIT>（A 批次源码+口径+台账），GitHub/Gitee 双端 main + tag v2.0.3 待推送

## B. 全渠道发行回执（2026-08-31，待执行）
| 渠道 | 产物/URL | 状态 |
|---|---|---|
| GitHub | https://github.com/zxc663/shisan-xinuo-workflow/releases/tag/v2.0.3 （附 dist v2.0.3.zip） | ⏳ |
| npm | `@zxc663/shisan-xinuo-workflow@2.0.3`（GitHub Packages，latest） | ⏳ |
| Gitee | https://gitee.com/zxc663/shisan-xinuo-workflow/releases （tag v2.0.3 + zip 附件） | ⏳ |
| ClawHub | `shisan-xinuo-workflow@1.0.5`（pending scans，内容 v2.0.3） | ⏳ |
| skills.sh | 等待遥测/爬虫收录 | ⏳ |

## C. 复用要点
- 令牌供给：GitHub/github PAT 与 Gitee token 从机密文档经正则提取注入 env，命令串与输出全程不含明文，用毕即清 env；回显仅 len/前缀。
- Gitee 建 Release 必须带 `target_commitish=main`（否则 400）；**附件上传 `POST /releases/{id}/attach_files` 用 `curl.exe -F access_token=… -F file=@…zip`**，勿用 `Invoke-RestMethod -Form`（PS7 该 multipart 文件字段会致 Gitee 返回 40001 登录失效）。
- ClawHub 发布路径= skill 子目录（含 SKILL.md）；走红海代理 `127.0.0.1:33210`。
- GitHub push/fetch 走代理 `git -c "http.https://github.com.proxy=http://127.0.0.1:33210"`；Gitee 直连。
- 发行完成后：About 双端 PATCH v2.0.3（Gitee 带 name）→ 观察约 30 分钟 → **GitHub classic PAT 轮换**（重新生成 → 更新 D:\Agent个人资源\机密资源\02-Gitee与GitHub.txt → 旧作废）→ 回执写回本项目文件与 task-log。