# hooks 模板 · 多平台说明（模板非运行时）

本目录是**配置示例**，不是捆绑运行时：本 Skill 保持零脚本，钩子可选、且受平台门控。复制后按平台适配，不原地编辑。

## 三件套（Claude Code 可用）

- `session-start.example.sh` —— 会话启动横幅（重新锚定纪律：判级 / 双模式 / 密钥红线 / 回滚 / 留档）
- `session-end.example.sh` —— 会话收尾横幅（最终验证 / 任务记录 / 记忆同步 / 密钥红线 / 显式清理）
- `hooks.example.json` —— Claude Code 配置：`SessionStart` / `SessionEnd` 各挂一条 `bash <script>` 命令

## 多平台可用性（2026-08-31 实测口径）

| 平台 | hooks 支持 | 使用方式 | 备注 |
|---|---|---|---|
| Claude Code | ✅ 支持 | 把 `hooks.example.json` 内容并入 `~/.claude/settings.json`（或独立 `hooks.json`）；Windows 下 .sh 需 bash（Git Bash / WSL），脚本路径按实际调整 | 最成熟的钩子承载平台 |
| WorkBuddy | ⚠️ 待实测 | 若 `settings.json` 支持 hooks 则同 Claude 模式；否则以 `BOOTSTRAP.md` 作启动锚定（平台机制要求时） | 实测后按真实结果标注 |
| Codex | ⚠️ 待实测 | `~/.codex/config.toml` 事件/hooks 支持按版本确认；不支持则如实标「平台可选」 | 不清洗 config.toml 既有字段 |
| Trae / Cursor / Windsurf / ZCode | ⚠️ 视版本 | 规则文件/全局设置已覆盖；hooks 属可选加固 | 依赖应用版本能力 |

**统一原则**：模板给的是**可将纪律自动锚定的示例**；hook 脚本不可用时，降级为「规则文件 + 注入核心已在场」即可——hooks 是加固面，不是必需面；本目录文件不参与运行时，发布前仅校验结构齐全（verify-release B 项）。