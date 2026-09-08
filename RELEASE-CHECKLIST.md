# 发行执行清单（v2.5.0）——留档一档制 + 调研前置（本地批次，待批发行）

> 本 Agent 无发行 MCP：外部发布动作经用户批准后，由本会话按既定令牌供给机制逐渠道执行（L3 红线已满足：命令清单先行、经用户批准）。
> **版本沿革**：v2.0.0 / v2.0.1 / v2.0.2 为源码与口径批次（未发行）；v2.0.3-v2.0.6 已全渠道发行（2026-08-31）；**v2.1.0 / v2.1.1 / v2.2.0 已全渠道发行（2026-09-02 ×3，v2.2.0 含 dist 39 = 39 + 注入副本重部署）；v2.3.0 已全渠道发行（2026-09-03）**——发行回执见 项目信息.md §五 与 CHANGELOG；**v2.4.0（三平台取证修补 + 细则分层蒸馏）与 v2.5.0（留档一档制 + 调研前置）为本地批次（2026-09-08），本次对外发 v2.5.0（v2.4.0 并入历史），发行面待批**。

## A. 本仓已备（随 git 提交）
- [ ] 版本锁 2.5.0（package.json / SKILL frontmatter / README 徽章与版本历史行 / 项目信息 #46·#47·§五 / docs/project-info / reference-sources / scripts-README 预期输出 / EVIDENCE §九（9,487 字符重测）/ AGENTS.md 路测基线）
- [ ] 内容 v2.4.0：场景判定不清默认按持续（先建承载兜底）；细则三层 T1/T2/T3（details 头部层级导读 + 症状索引 19 域全标注）；防棘轮元条款；消重（§3 步骤 6 与 §2.0 第 4 步同源收敛）；紧凑档窗口下限 ≥16K 转正；版本 2.3.0→2.4.0
- [ ] 内容 v2.5.0：留档一档制（跨会话留档收敛单文件 `memory/agent-log.md` 四区 + 唯一轮转档 `agent-log-archive-YYYY-MM.md`，五件套不再默认创建）；设计前先调研成熟设计（并入设计铁律/复用铁律）；templates/agent-log-template.md 新建 + workspace-memory-template.md 指针化；蒸馏版三份同批（Single 1.2.0 / Universal 1.1.0）；注入副本五处重部署 v2.5.0（备份先行，已预授权执行）
- [ ] verify-release 6/6 PASS（base=2.5.0，含 F 项索引完整性 283 全覆盖，零泄漏）
- [ ] dist/shisan-xinuo-workflow-v2.5.0.zip（发行面批准后 `scripts/build-dist.ps1` 打包 + Set-diff 双检）
- [ ] 提交并推送双端 main + tag v2.5.0（**未执行**——本地 commit 不 push，发行面另行批准）

## B. 全渠道发行回执（待用户批准后执行）
| 渠道 | 产物/URL | 状态 |
|---|---|---|
| GitHub | Release v2.5.0（附 dist zip，走代理） | ⏳ 未执行 |
| npm | `@zxc663/shisan-xinuo-workflow@2.5.0`（GitHub Packages） | ⏳ 未执行 |
| Gitee | Release tag v2.5.0 + zip 附件（直连） | ⏳ 未执行 |
| ClawHub | `shisan-xinuo-workflow@1.0.12`（内容 v2.5.0） | ⏳ 未执行 |
| About | GitHub+Gitee 描述 PATCH v2.5.0（六·二文案：283 条 17 类 + T1/T2/T3 + 一档制 + 设计前调研） | ⏳ 未执行 |
| skills.sh | 等待遥测/爬虫收录 | ⏳ |

## C. 复用要点
- 令牌供给：GitHub/github PAT 与 Gitee token 从机密文档经正则提取注入 env，命令串与输出全程不含明文，用毕即清 env；回显仅 len/前缀。
- Gitee 建 Release 必须带 `target_commitish=main`（否则 400）；**附件上传 `POST /releases/{id}/attach_files` 用 `curl.exe -F access_token=… -F file=@…zip`**，勿用 `Invoke-RestMethod -Form`（PS7 该 multipart 文件字段会致 Gitee 返回 40001 登录失效）。
- GitHub Release 资产上传走 **uploads.github.com** + `-L`；REST JSON body 写文件用**无 BOM UTF8**（否则 GitHub 400「Problems parsing JSON」）。
- ClawHub 发布路径 = skill 子目录（含 SKILL.md），cwd 必须切到 `skill/shisan-xinuo-workflow/`；走红海代理 `127.0.0.1:33210`。
- dist 打包用 `scripts/build-dist.ps1`（v2.2.0 起）+ Set-diff 双检。
- GitHub push/fetch/API 走代理 `http://127.0.0.1:33210`；Gitee 直连。
- 发行完成后：**GitHub classic PAT 轮换**（v2.0.3 起遗留最高优先）→ 观察约 30 分钟（含 ClawHub 1.0.11/1.0.12 审核复查）→ 回执写回本文件与 task-log。
- **待批项**：注入副本重部署 v2.5.0（平台全局注入文件属授权范畴，已预授权备份先行执行）+ 技能副本 syncer 同步；**通用版/三版安装取舍**（未确认，另行批）。