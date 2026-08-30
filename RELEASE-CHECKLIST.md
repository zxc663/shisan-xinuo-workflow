# 发行执行清单（v1.19.1）——复核第三方审计 F-1/2/3/5/6 后升版全渠道重发

> 本 Agent 无发行 MCP：外部发布动作经用户批准后，由本会话按既定令牌供给机制逐渠道执行（L3 红线已满足：命令清单先行、经用户批准）。
> **注（2026-08-30）**：本台账归属 v1.19.1 全渠道发行；**v2.0.0 为源码 + 口径 + 门禁批次（未对外发布）**，详见 项目信息.md §五 与 memory/task-log/2026-08-30-中文版单版本化重构.md。

## A. 本仓已备（随 git 提交）
- [x] 版本锁 1.19.1（package.json / SKILL frontmatter 三语 / README 徽章）
- [x] CHANGELOG.md（v1.9→v1.19.1，新增 v1.19.1 行）
- [x] 项目信息.md 发布记录表补 v1.19.1 行
- [x] scripts/syncer.py · scripts/verify-release.ps1（F-2/F-3/F-6 修复 + 泄漏扫描收敛）
- [x] dist/shisan-xinuo-workflow-v1.19.1.zip（暂存目录法重建，排除 personal-zh，75 文件+2 空目录，293.7KB）
- [x] verify-release 门禁 ALL PASS（base=1.19.1）+ 负向注入 `C:\Users\fakeuser` 正确 FAIL
- [x] 提交 06e37df（F-fix）+ 84fadb6（升版口径），GitHub/Gitee 双端 main + tag v1.19.1 同步

## B. 全渠道发行回执（2026-08-30，已执行）
| 渠道 | 产物/URL | 状态 |
|---|---|---|
| GitHub | https://github.com/zxc663/shisan-xinuo-workflow/releases/tag/v1.19.1 （附 dist v1.19.1.zip） | ✅ |
| npm | `@zxc663/shisan-xinuo-workflow@1.19.1`（GitHub Packages，latest，70 文件 194.8kB，shasum ad6f436…） | ✅ |
| Gitee | https://gitee.com/zxc663/shisan-xinuo-workflow/releases （Release id=1004434，zip 附件 id=3119299） | ✅ |
| ClawHub | `shisan-xinuo-workflow@1.0.4`（pending security scans，内容 v1.19.1） | ✅ 待公开 |
| skills.sh | 等待遥测/爬虫收录 | ⏳ |

## C. 复用要点
- 令牌供给：GitHub/github PAT 与 Gitee token 从机密文档经正则提取注入 env，命令串与输出全程不含明文，用毕即清 env；回显仅 len/前缀。
- Gitee 建 Release 必须带 `target_commitish=main`（否则 400）；**附件上传 `POST /releases/{id}/attach_files` 用 `curl.exe -F access_token=… -F file=@…zip`**，勿用 `Invoke-RestMethod -Form`（PS7 该 multipart 文件字段会致 Gitee 返回 40001 登录失效）。
- ClawHub 发布路径= skill 子目录（含 SKILL.md，`versions\universal-zh` 根不含会报 "SKILL.md required"）；走红海代理 `127.0.0.1:33210`。