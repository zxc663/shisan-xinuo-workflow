# 安全政策 · Security Policy

## 报告漏洞

**不要在公开 issue 里报告安全问题。** 请使用 GitHub 的 [私有安全报告](https://github.com/zxc663/shisan-xinuo-workflow/security/advisories/new)（Security Advisories），或通过维护者 GitHub 主页的个人资料渠道联系。

## 范围

- `scripts/` 下所有可执行脚本（探针 harness / 门禁 / 部署 / 同步）——特别是 `deploy_injection.py`（平台注入面）与 hooks 模板（每会话执行的命令通道）。
- `templates/hooks/`——hooks 以宿主进程权限执行，任何注入形状都算安全面。
- 发布物（`dist/*.zip`、npm 包、ClawHub 包）与安装脚本（`scripts/install-skill.ps1`）。

## 已知设计边界（非漏洞，如实声明）

- 本 Skill 的探针 harness 默认把被测会话置于**无工具权限限制**的 yolo 模式（`--prompt` 面不设防）——这是行为面的测量条件，只应指向临时目录夹具，不得指向真实项目。
- 门禁的泄漏红线（D 项）覆盖发布物内令牌/个人路径模式，但不构成机密防泄漏的替代品——密钥管理仍以 [references/security.md](skill/shisan-xinuo-workflow/references/security.md) 的红线为准。

## 支持版本

- 仅最新 minor 线（当前 **v3.1.x**）。
