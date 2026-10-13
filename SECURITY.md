# 安全政策 · Security Policy

## 报告漏洞

**不要在公开 issue 里报告安全问题。** 请使用 GitHub 的 [私有安全报告](https://github.com/zxc663/shisan-xinuo-workflow/security/advisories/new)（Security Advisories），或通过维护者 GitHub 主页的个人资料渠道联系。

## 范围

- `scripts/` 下所有可执行脚本（探针 harness / 门禁 / 部署 / 同步）——特别是 `deploy_injection.py`（平台注入面）与 hooks 模板（每会话执行的命令通道）。
- `templates/hooks/`——hooks 以宿主进程权限执行，任何注入形状都算安全面。
- 发布物（`dist/*.zip`、npm 包、ClawHub 包）与安装脚本（`scripts/install-skill.ps1`）。

## 敏感度分级（privacy_gate 判据）

隐私门 `scripts/privacy_gate.py` 按敏感度分三级，判据 = **该信息能否反查到具体个人或定位到具体机器**：

| 级别 | 内容 | 门禁判定 | 说明 |
|---|---|---|---|
| **高敏** | QQ 邮箱（可反查个人）、机密目录路径、令牌明文 | **block**（发行阻断） | 门建成前存量已清洗：全历史 528×`a13sino@qq.com` → `zxc663@users.noreply.github.com`（2026-10-13 `git filter-repo` 重写，本地已完成，force push 待批） |
| **中敏** | 本机 Windows 用户名（家目录形态 = 盘符 + `Users` + 用户名） | **block** | 可定位到具体机器；门禁按**平台形态**匹配（盘符 `:` + 反斜杠 + `Users` + 反斜杠 + 用户名），不匹配独立账号 token |
| **低敏** | 笔名「十三希诺」、GitHub 账号名（`github.com/<acct>`、npm/clawhub 包名） | **warn**（如实报告不阻断） | 发布身份/门面需要——`package.json` author 保留笔名是设计裁决；账号名出现在安装命令与仓库 URL 中属正常分发形态 |

**伪造样本白名单**：门禁负向测试注入的假身份（家目录路径 + `fake`/`example`/`sample`/`test`/`dummy` 前缀的用户名）降级为 warn 并标注「伪造样本·门禁负向注入」——它证明门禁在测，不构成泄漏。真实用户名不在白名单内。

**统一占位符**：`<user>` / `<EMAIL_REDACTED>` / `%USERPROFILE%` / `<REPO>`。文档与示例一律用占位符，禁写真值。

**处理顺序**：发现真凭据（令牌/密码）永远是「**先吊销，再清理**」——清理不解除已泄漏凭据的暴露面，必须先轮换/撤销。

## 四层扫描面

| 层 | 扫描对象 | 覆盖的缺口 |
|---|---|---|
| 1 | git tracked 文本（105 文件） | 身份维度：邮箱 / 家目录 / 机密目录 / 令牌 |
| 2 | `git log --all` 全历史（author/committer/message） | 历史身份——文本扫描扫不到 |
| 3 | `package.json` 的 `author`/`contributors`/`maintainers`/`repository` | 发行物元数据（在 dist 打包面内） |
| 4 | 未跟踪二进制（截图等） | **清单化人工过窗**——机器不全查，只出清单；确认截图内无 IDE 用户名/路径/窗口标题/通知内容 |

层 4 现状：仓库根 16 张未跟踪验证截图**不进发行物**（`build-dist` 的 `$roots` 不含根级散落二进制），但发行前须人工过窗。门禁对此只出清单，不自动放行也不自动删除。

## 已知设计边界（非漏洞，如实声明）

- 本 Skill 的探针 harness 默认把被测会话置于**无工具权限限制**的 yolo 模式（`--prompt` 面不设防）——这是行为面的测量条件，只应指向临时目录夹具，不得指向真实项目。
- 门禁的泄漏红线（D 项）覆盖发布物内令牌/个人路径模式，但不构成机密防泄漏的替代品——密钥管理仍以 [references/security.md](skill/shisan-xinuo-workflow/references/security.md) 的红线为准。

## 支持版本

- 仅最新 minor 线（当前 **v3.1.x**）。
