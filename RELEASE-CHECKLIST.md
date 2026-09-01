# 发行执行清单（v2.1.0）——上下文主动管理补全批次（2026-09-02 已全渠道发行）

> 本 Agent 无发行 MCP：外部发布动作经用户批准后，由本会话按既定令牌供给机制逐渠道执行（L3 红线已满足：命令清单先行、经用户批准）。
> **版本沿革**：v2.0.0 / v2.0.1 / v2.0.2 为源码与口径批次（未发行）；v2.0.3、v2.0.4、v2.0.5、v2.0.6 已全渠道发行（2026-08-31，v2.0.5/v2.0.6 内容随 v2.0.6 一并发行）；**v2.1.0（上下文主动管理补全批次）已于 2026-09-02 全渠道发行**，详情见 项目信息.md §三·§五 与 memory/task-log。

## A. 本仓已备（随 git 提交）
- [x] 版本锁 2.1.0（package.json / SKILL frontmatter / README 徽章与版本历史行 / 项目信息 §三·§五 / docs/project-info / verify-release 锚串 / reference-sources / scripts-README 预期输出 / EVIDENCE §九·§七）
- [x] 上下文主动管理补全源码（本地 commit 151834c + 补强批次 75ac1b7，2026-09-01）：保留清单+折叠协议（injection-core 关键条款 + SKILL §12 P8）、紧凑档（details #273）、大文件读取协议（#274）、模块锚点表（#275 + docs/project-info 锚词列示范）、按需符号召回协议 + 模块依赖关系表（#276）、local-model-glossary.md（10 术语）、README 客户端能力边界声明与四客户端联用建议
- [x] verify-release 4/4 PASS（base=2.1.0，含新增锚串「折叠协议/保留清单」，零泄漏）——补强批次后已重跑通过（2026-09-02）
- [x] dist/shisan-xinuo-workflow-v2.1.0.zip（2026-09-02 重建完成：38 项 Set-diff 双检 38=38，187,627B）
- [x] 双端 main + tag v2.1.0 已推送（0257d79..c770879，2026-09-02）

## B. 全渠道发行回执（2026-09-02 已执行完成）
| 渠道 | 产物/URL | 状态 |
|---|---|---|
| GitHub | Release v2.1.0（id=380670147，zip 资产 539842185，187,627B，走代理） | ✅ |
| npm | `@zxc663/shisan-xinuo-workflow@2.1.0`（30 文件 125.5 kB，shasum d901e05b…，GitHub Packages） | ✅ |
| Gitee | Release tag v2.1.0（id=1107269）+ zip 附件（id=3132188，直连） | ✅ |
| ClawHub | `shisan-xinuo-workflow@1.0.8`（内容 v2.1.0） | ✅ pending scans 待公开 |
| About | GitHub+Gitee 仓库描述 PATCH v2.1.0（六·一文案，200/200） | ✅ |
| skills.sh | 等待遥测/爬虫收录 | ⏳ |

## C. 复用要点
- 令牌供给：GitHub/github PAT 与 Gitee token 从机密文档经正则提取注入 env，命令串与输出全程不含明文，用毕即清 env；回显仅 len/前缀。
- Gitee 建 Release 必须带 `target_commitish=main`（否则 400）；**附件上传 `POST /releases/{id}/attach_files` 用 `curl.exe -F access_token=… -F file=@…zip`**，勿用 `Invoke-RestMethod -Form`（PS7 该 multipart 文件字段会致 Gitee 返回 40001 登录失效）。
- ClawHub 发布路径= skill 子目录（含 SKILL.md）；走红海代理 `127.0.0.1:33210`。
- GitHub push/fetch/API 走代理 `http://127.0.0.1:33210`；Gitee 直连。
- 发行完成后：**GitHub classic PAT 轮换**（v2.0.3 起遗留最高优先：重新生成 → 更新 D:\Agent个人资源\机密资源\02-Gitee与GitHub.txt → 旧作废）→ 观察约 30 分钟（含 ClawHub 1.0.7/1.0.8 审核复查）→ 回执写回本项目文件与 task-log。
- **v2.1.0 特有前置**：注入副本重部署（平台全局注入文件属授权范畴）与技能副本同步（syncer.py）在发行面之外单独待批。
