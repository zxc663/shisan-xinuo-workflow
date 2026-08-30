# 发行执行清单（v1.18.0）——区分「本仓已备」与「你在另一端执行」

> 本 Agent 无发行 MCP：**外部发布动作由你在另一平台执行**（L3 红线：命令清单先行、由你确认后逐条执行）。本仓严禁代为推送。

## A. 本仓已备（随 git 提交，不 push）
- [x] 版本锁 1.18.0（package.json / SKILL frontmatter / README 徽章）
- [x] README.md 重构（8 节：定位意图/安装适配/执行路径/治理件/参考层/自更新合并/真实数据/发行验证）
- [x] CHANGELOG.md（v1.9→v1.18）
- [x] docs/reference-sources.md（v1.18 版本行 + 三语增补制说明）
- [x] scripts/syncer.py · scripts/verify-release.ps1
- [x] dist/shisan-xinuo-workflow-v1.18.0.zip（skill 全量 + README + CHANGELOG + scripts + RELEASE-CHECKLIST）
- [x] EVIDENCE.md §七 更新（0 命中→触达后转有 + 成本真账指向）
- [ ] versions/ 三语增补同步（随本 commit 完成；增补制，非全量重写——README 已如实标注）

## B. 你在另一端执行（按序）
1. **快检**：`python scripts/verify-release.ps1`（或对应验证）→ 资产清单核对绿。
2. **GitHub**：`git tag v1.18.0` → push tag → Release 附 `dist/…zip` + CHANGELOG 摘要。
3. **npm**：`npm publish`（@zxc663/shisan-xinuo-workflow）——先 `npm version 1.18.0` 已锁定。
4. **Gitee**：同步主线 + 发布镜像（对应 Release）。
5. **skills.sh / ClawHub**：上传台账入口（zip 路径 + 版本号 + README 链接）。
6. **回执**：把各渠道产物 URL 回填到本文件中「回执」节（或 task-log），供审计。

## 回执（发行完成后填）
| 渠道 | 产物/URL | 时间 |
|---|---|---|
| GitHub | | |
| npm | | |
| Gitee | | |
| skills.sh | | |
| ClawHub | | |
