# 发行执行清单（v2.1.1）——口径修正补丁（2026-09-02 已全渠道发行）

> 本 Agent 无发行 MCP：外部发布动作经用户批准后，由本会话按既定令牌供给机制逐渠道执行（L3 红线已满足：命令清单先行、经用户批准）。
> **版本沿革**：v2.0.0 / v2.0.1 / v2.0.2 为源码与口径批次（未发行）；v2.0.3、v2.0.4、v2.0.5、v2.0.6 已全渠道发行（2026-08-31，v2.0.5/v2.0.6 内容随 v2.0.6 一并发行）；**v2.1.0（上下文主动管理补全批次）已于 2026-09-02 全渠道发行**；**v2.1.1（口径修正补丁：细则类数 16→17 全仓统一 + README「超长 System Prompt」本质声明）已于 2026-09-02 全渠道发行**，详情见 项目信息.md §三·§五 与 memory/task-log。

## A. 本仓已备（随 git 提交）
- [x] 版本锁 2.1.1（package.json / SKILL frontmatter / README 徽章与版本历史行 / 项目信息 §三·§五 / docs/project-info / verify-release 锚串 / reference-sources / scripts-README 预期输出 / EVIDENCE §九 / AGENTS.md）
- [x] 细则类数 16→17 全仓统一（SKILL §9 / injection-core / EVIDENCE / docs×2 / CHANGELOG / README / 项目信息 / About 描述已重 PATCH）
- [x] README 优化：新增「本仓库=一份超长 System Prompt」本质声明 + v2.1.0 已发行口径回填 + dist 提示更新
- [x] verify-release 4/4 PASS（base=2.1.1，含新增锚串「折叠协议/保留清单」，零泄漏）
- [x] dist/shisan-xinuo-workflow-v2.1.1.zip（staging 暂存目录法 + Set-diff 双检 38=38，187,627B）
- [x] 双端 main + tag v2.1.1 已推送（6090e7f..c9e348e）

## B. 全渠道发行回执（2026-09-02 已执行完成）
| 渠道 | 产物/URL | 状态 |
|---|---|---|
| GitHub | Release v2.1.1（id=380681782，zip 资产 539867510，188,784B，走代理） | ✅ |
| npm | `@zxc663/shisan-xinuo-workflow@2.1.1`（GitHub Packages） | ✅ |
| Gitee | Release tag v2.1.1（id=1107366）+ zip 附件（id=3132330，直连） | ✅ |
| ClawHub | `shisan-xinuo-workflow@1.0.9`（内容 v2.1.1） | ✅ pending scans 待公开 |
| About | GitHub+Gitee 仓库描述 PATCH（六·一 17 类文案，重 PATCH v2.1.1 口径） | ✅ |
| skills.sh | 等待遥测/爬虫收录 | ⏳ |

## C. 复用要点
- 令牌供给：GitHub/github PAT 与 Gitee token 从机密文档经正则提取注入 env，命令串与输出全程不含明文，用毕即清 env；回显仅 len/前缀。
- Gitee 建 Release 必须带 `target_commitish=main`（否则 400）；**附件上传 `POST /releases/{id}/attach_files` 用 `curl.exe -F access_token=… -F file=@…zip`**，勿用 `Invoke-RestMethod -Form`（PS7 该 multipart 文件字段会致 Gitee 返回 40001 登录失效）。
- GitHub Release 资产上传走 **uploads.github.com** + `-L`（api.github.com 该路径 404）；REST JSON body 写文件用**无 BOM UTF8**（`New-Object Text.UTF8Encoding($false)`，否则 GitHub 400「Problems parsing JSON」）。
- ClawHub 发布路径 = skill 子目录（含 SKILL.md），cwd 必须切到 `skill/shisan-xinuo-workflow/`；走红海代理 `127.0.0.1:33210`。
- GitHub push/fetch/API 走代理 `http://127.0.0.1:33210`；Gitee 直连。
- 发行完成后：**GitHub classic PAT 轮换**（v2.0.3 起遗留最高优先）→ 观察约 30 分钟（含 ClawHub 1.0.9 审核复查）→ 回执写回本项目文件与 task-log。
- **待批项**：注入副本重部署 v2.1.1（平台全局注入文件属授权范畴）与技能副本同步（syncer.py）在发行面之外单独待批。