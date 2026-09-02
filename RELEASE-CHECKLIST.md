# 发行执行清单（v2.2.0）——开工序列六步 + 承载平台适配 + 本体净化 + 决策时效（已发行 2026-09-02）

> 本 Agent 无发行 MCP：外部发布动作经用户批准后，由本会话按既定令牌供给机制逐渠道执行（L3 红线已满足：命令清单先行、经用户批准）。
> **版本沿革**：v2.0.0 / v2.0.1 / v2.0.2 为源码与口径批次（未发行）；v2.0.3、v2.0.4、v2.0.5、v2.0.6 已全渠道发行（2026-08-31）；**v2.1.0（上下文主动管理补全）与 v2.1.1（口径修正 16→17 类）已全渠道发行（2026-09-02 ×2）**；**v2.2.0（开工序列六步 + 承载平台适配 + 本体净化 + 决策时效）已全渠道发行（2026-09-02）**，详情见 项目信息.md §三·§五 与 memory/task-log；本轮发行起新增 `scripts/build-dist.ps1` 打包器。

## A. 本仓已备（随 git 提交）
- [x] 版本锁 2.2.0（package.json / SKILL frontmatter / README 徽章与版本历史行 / 项目信息 §三·§五 / docs/project-info / verify-release 锚串「项目级注入点」/ reference-sources / scripts-README 预期输出 / EVIDENCE §九（8,922 字符重测）/ AGENTS.md 路测基线）
- [x] 内容：开工序列六步（SKILL §2.0 + injection-core，复述前置纪律 §0）；承载平台适配（项目级注入点表 + `.trae-rules` 清零 + 加载即承载检查）；本体净化（正文 vs 史料规范 + 逐文件清理 + verify E 项）；决策时效（details #278/#279 + 仲裁序修正 + 混合写入门槛）
- [x] verify-release 5/5 PASS（base=2.2.0，含 E 项正文净化检查与 A 项新锚串，零泄漏）
- [x] dist/shisan-xinuo-workflow-v2.2.0.zip（重建完成，staging 暂存目录法 + Set-diff 双检 39=39，190,102B）
- [x] 提交并推送双端 main + tag v2.2.0（GitHub ✅ + Gitee ✅，8701d27）

## B. 全渠道发行回执（已执行完成 2026-09-02）
| 渠道 | 产物/URL | 状态 |
|---|---|---|
| GitHub | Release v2.2.0（id=381368172，zip 资产 id=541361374，走代理） | ✅ 已发行 |
| npm | `@zxc663/shisan-xinuo-workflow@2.2.0`（GitHub Packages，30 文件 129.7kB，shasum 1cc423d0） | ✅ 已发行 |
| Gitee | Release id=1119837 + zip 附件 id=3139662（target_commitish=main，直连） | ✅ 已发行 |
| ClawHub | `shisan-xinuo-workflow@1.0.10`（内容 v2.2.0）update submitted，pending security scans | ⏳ 待审核公开 |
| About | GitHub+Gitee 描述 PATCH v2.2.0 口径（279 条 17 类 + 六步/净化/决策时效），双端 200 | ✅ 已 PATCH |
| skills.sh | 等待遥测/爬虫收录 | ⏳ |

## C. 复用要点
- 令牌供给：GitHub/github PAT 与 Gitee token 从机密文档经正则提取注入 env，命令串与输出全程不含明文，用毕即清 env；回显仅 len/前缀。
- Gitee 建 Release 必须带 `target_commitish=main`（否则 400）；**附件上传 `POST /releases/{id}/attach_files` 用 `curl.exe -F access_token=… -F file=@…zip`**，勿用 `Invoke-RestMethod -Form`（PS7 该 multipart 文件字段会致 Gitee 返回 40001 登录失效）。
- GitHub Release 资产上传走 **uploads.github.com** + `-L`（api.github.com 该路径 404）；REST JSON body 写文件用**无 BOM UTF8**（否则 GitHub 400「Problems parsing JSON」）。
- ClawHub 发布路径 = skill 子目录（含 SKILL.md），cwd 必须切到 `skill/shisan-xinuo-workflow/`；走红海代理 `127.0.0.1:33210`。
- GitHub push/fetch/API 走代理 `http://127.0.0.1:33210`；Gitee 直连。
- 发行完成后：**GitHub classic PAT 轮换**（v2.0.3 起遗留最高优先）→ 观察约 30 分钟（含 ClawHub 1.0.9/1.0.10 审核复查）→ 回执写回本项目文件与 task-log。
- **待批项**：注入副本重部署 v2.2.0（平台全局注入文件属授权范畴）+ 技能副本 syncer 同步在发行面之外单独待批。
