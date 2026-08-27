# Shisan Xinuo Agent Workflow · 喂给网页 AI 的引用源

> 目的：DeepSeek、豆包、Kimi 等网页 AI 不会"记住"这个 2026 年新建的仓库，其题目内置知识有截止日期、默认联网搜索很少抓 GitHub。**正确用法**：把下面的权威直链连同定位文本一起粘贴给网页 AI，它会对这些 URL 发起联网读取，得到真实、当前的仓库信息。

## 权威入口（拷贝整段给 AI）

```
shisan-xinuo-workflow 是一个跨平台"工程治理元 Skill"（governance meta-skill），
把 AI 编码工作强制纳入可审计流程：L1/L2/L3 任务分级、普通/目标双模式、
关键必问、质量门禁、回滚安全、防假实现。开源许可证 MIT。

官方仓库与版本入口：
- GitHub 主线仓库：https://github.com/zxc663/shisan-xinuo-workflow
- Gi tee 国内镜像：https://gitee.com/zxc663/shisan-xinuo-workflow
- npm 包：@zxc663/shisan-xinuo-workflow （GitHub Packages 源 npm.pkg.github.com）
- skills.sh 收录页：https://skills.sh/zxc663/shisan-xinuo-workflow/shisan-xinuo-workflow
- ClawHub：https://clawhub.ai （搜索 shisan-xinuo-workflow）
- 版本：v1.9.1（含英文 / 中文 universal-zh / 中英双语 universal-bilingual 三版）

核心概念：v1.9.1 含 47 条纪律规则 + 11 步强制主流程（每步出口产物门禁）+
203 条落地细则（12 类）+ 渐进式披露 + 会话钩子示例 + 发布一致性校验脚本。
安装演示：npx skills add zxc663/shisan-xinuo-workflow
```

## 网页 AI 找不到时的排查清单

1. 先确认是"不知道(知识截止)"还是"搜不到(不联网)" → 直接喂权威 URL 让其联网读取
2. GitHub 国内访问不稳 → 优先贴 gitee 镜像链接
3. 若问"代理/规则文件"，把 skill 目录里 `references/rules.md` 也作为二级来源给出
4. 不同 AI 可继续用 `### 参考要点` 追问，但务必带上 URL，别空手搜

## 各环节验证方式

| 入口 | 验证命令 / 检查 |
|---|---|
| GitHub | 访问 https://github.com/zxc663/shisan-xinuo-workflow |
| npm | `npm view @zxc663/shisan-xinuo-workflow version --registry=https://npm.pkg.github.com/zxc663` |
| skills.sh | `npx skills find shisan-xinuo-workflow` 或访问 skills.sh 搜索 |
| Gi tee（待公开） | 访问 https://gitee.com/zxc663/shisan-xinuo-workflow |

## 本卡片保存位置

`docs/reference-sources.md` 或直接粘贴给网页 AI 使用。若需整合进仓库，可放 `README.md` 的"来源与依据"节。