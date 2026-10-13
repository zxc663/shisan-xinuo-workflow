# Shisan Xinuo Agent Workflow · 喂给网页 AI 的引用源

> 目的：DeepSeek、豆包、Kimi 等网页 AI 不会"记住"这个 2026 年新建的仓库，其题目内置知识有截止日期、默认联网搜索很少抓 GitHub。**正确用法**：把下面的权威直链连同定位文本一起粘贴给网页 AI，它会对这些 URL 发起联网读取，得到真实、当前的仓库信息。

## 权威入口（拷贝整段给 AI）

```
shisan-xinuo-workflow 是一个跨平台"工程治理元 Skill"（governance meta-skill），
把 AI 编码工作强制纳入可审计流程：L1/L2/L3 任务分级、普通/目标双模式、
关键必问、质量门禁、回滚安全、防假实现。开源许可证 MIT。

官方仓库与版本入口：
- GitHub 主线仓库：https://github.com/zxc663/shisan-xinuo-workflow
- Gitee 国内镜像：https://gitee.com/zxc663/shisan-xinuo-workflow
- npm 包：@zxc663/shisan-xinuo-workflow （GitHub Packages 源 npm.pkg.github.com）
- skills.sh 收录页：https://skills.sh/zxc663/shisan-xinuo-workflow/shisan-xinuo-workflow
- ClawHub：https://clawhub.ai （搜索 shisan-xinuo-workflow）
- 版本：v4.2.0（施工中·发行待批；计划=docs/design-specs/v420-plan-unfreeze-decouple-privacy-20261013.md；本批=细则双库解冻〔条款账零和 405 + 教训账解冻不占 405〕+教训域/态字段与生命周期协议〔active/fixed/retired + 修复三要件 + 复活回指〕+开源隐私门〔四层扫描 privacy_gate.py + 门禁 K 项〕+时间戳强制场景 + 代拟用户言论词表机检面；上一发行态 v4.1.0〔门禁防线+部署链+规则层定型，2026-10-12 发行〕），活跃细则 405 条/33 类（编号至 #407），教训账 0 条（合法初态），判据 j2.7（金样本回归 25/25），发行门禁 11 项（A-K）。完整沿革见仓库 CHANGELOG.md。

核心概念：42 条纪律规则（rules.md）+ **三级跑道**（L1 快速通道 / L2-S 短工作流（对接真相清单必做）/ L2-F 完整 9 步，每步出口产物门禁）+
405 条落地细则（33 类）+ 分文件按需加载 + 细则检索端口 + 会话钩子示例 + 一键安装脚本（agent- 前缀自适配）+ 硬注入三层承载（记忆层在场提示 + 规则层 + 配置层）+ 发布一致性校验脚本（内容锚点门禁 + 正文净化检查）+ 上下文主动管理（折叠协议 / 保留清单 / 紧凑档 / 模块锚点表 / 按需符号召回 / 大文件读取协议 / 决策时效）。
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
| Gitee（公开镜像） | 访问 https://gitee.com/zxc663/shisan-xinuo-workflow |

## 本卡片保存位置

`docs/reference-sources.md` 或直接粘贴给网页 AI 使用。若需整合进仓库，可放 `README.md` 的"来源与依据"节。