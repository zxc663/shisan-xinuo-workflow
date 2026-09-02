# 发行执行清单（v2.3.0）——场景化 + 写作重构 + Steer/Parallel + 回指理解强制 + 审计修复（已全渠道发行 2026-09-03）

> 本 Agent 无发行 MCP：外部发布动作经用户批准后，由本会话按既定令牌供给机制逐渠道执行（L3 红线已满足：命令清单先行、经用户批准）。
> **版本沿革**：v2.0.0 / v2.0.1 / v2.0.2 为源码与口径批次（未发行）；v2.0.3-v2.0.6 已全渠道发行（2026-08-31）；**v2.1.0 / v2.1.1 / v2.2.0 已全渠道发行（2026-09-02 ×3，v2.2.0 含 dist 39=39 + 注入副本重部署，commit 8701d27）**——发行回执见 项目信息.md §五 与 CHANGELOG；**v2.3.0 已全渠道发行（2026-09-03）**。

## A. 本仓已备（随 git 提交）
- [ ] 版本锁 2.3.0（package.json / SKILL frontmatter / README 徽章与版本历史行 / 项目信息 #44·§五 / docs/project-info / reference-sources / scripts-README 预期输出 / EVIDENCE §九（9,212 字符重测 + SKILL 全载成本账）/ AGENTS.md 路测基线）
- [ ] 内容：场景化（#283 单发豁免）；写作重构（§10 总纲 + AGENTS.md 维护纪律 + workflows 日期裁决）；Steer #280 / Parallel #281；回指强制段 + 每消息严谨分析（#282）；审计修复 1-7（症状索引表 + F 项门禁 / 标签统一 17 中文 / 取证命令唯一权威源 / TOP 换血 #228·#229 / GATE errpath / E 项定位明示 + B 项警告级 / 彩蛋降档 + 成本账 / 矛盾裁决）
- [ ] verify-release 6/6 PASS（base=2.3.0，含 F 项索引完整性 283 全覆盖，零泄漏）
- [x] dist/shisan-xinuo-workflow-v2.3.0.zip（**已重建 2026-09-03：39=39，198,652B**——发行面批准后 `scripts/build-dist.ps1` 打包 + Set-diff 双检）
- [ ] 提交并推送双端 main + tag v2.3.0（**未执行**——本地 commit 不 push，发行面另行批准）

## B. 全渠道发行回执（待用户批准后执行）
| 渠道 | 产物/URL | 状态 |
|---|---|---|
| GitHub | Release v2.3.0（附 dist zip，走代理） | ✅ 2026-09-03 |
| npm | `@zxc663/shisan-xinuo-workflow@2.3.0`（GitHub Packages） | ✅ 2026-09-03 |
| Gitee | Release tag v2.3.0 + zip 附件（直连） | ✅ 2026-09-03 |
| ClawHub | `shisan-xinuo-workflow@1.0.11`（内容 v2.3.0） | ✅ 2026-09-03 |
| About | GitHub+Gitee 描述 PATCH v2.3.0（六·二文案：283 条 17 类 + 场景化/纠偏/并行/审计修复） | ✅ 2026-09-03 |
| skills.sh | 等待遥测/爬虫收录 | ⏳ |

## C. 复用要点
- 令牌供给：GitHub/github PAT 与 Gitee token 从机密文档经正则提取注入 env，命令串与输出全程不含明文，用毕即清 env；回显仅 len/前缀。
- Gitee 建 Release 必须带 `target_commitish=main`（否则 400）；**附件上传 `POST /releases/{id}/attach_files` 用 `curl.exe -F access_token=… -F file=@…zip`**，勿用 `Invoke-RestMethod -Form`（PS7 该 multipart 文件字段会致 Gitee 返回 40001 登录失效）。
- GitHub Release 资产上传走 **uploads.github.com** + `-L`；REST JSON body 写文件用**无 BOM UTF8**（否则 GitHub 400「Problems parsing JSON」）。
- ClawHub 发布路径 = skill 子目录（含 SKILL.md），cwd 必须切到 `skill/shisan-xinuo-workflow/`；走红海代理 `127.0.0.1:33210`。
- dist 打包用 `scripts/build-dist.ps1`（v2.2.0 起新增）+ Set-diff 双检。
- GitHub push/fetch/API 走代理 `http://127.0.0.1:33210`；Gitee 直连。
- 发行完成后：**GitHub classic PAT 轮换**（v2.0.3 起遗留最高优先）→ 观察约 30 分钟（含 ClawHub 1.0.10/1.0.11 审核复查）→ 回执写回本项目文件与 task-log。
- **待批项**：注入副本重部署 v2.3.0（平台全局注入文件属授权范畴）+ 技能副本 syncer 同步在发行面之外单独待批。
