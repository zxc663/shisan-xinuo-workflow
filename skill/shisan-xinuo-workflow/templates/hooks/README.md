# hooks 模板 · 多平台说明（模板非运行时）

本目录是**配置示例**，不是捆绑运行时：钩子面保持零捆绑脚本（hooks 可选、受平台门控；scripts/detail_lookup.py 为唯一随包分发的标准库只读检索工具，非钩子运行时）。复制后按平台适配，不原地编辑。

## 三件套（Claude Code 可用）

- `session-start.example.sh` —— 会话启动横幅（重新锚定纪律：判级 / 双模式 / 密钥红线 / 回滚 / 留档）
- `session-end.example.sh` —— 会话收尾横幅（最终验证 / 任务记录 / 记忆同步 / 密钥红线 / 显式清理）
- `hooks.example.json` —— 插件/通用形状示例：`SessionStart` / `Stop` 各挂一条 `bash <script>` 命令（注意 ZCode 实测：ZCode 无 `SessionEnd` 事件，会话结束事件名为 `Stop`）
- `hooks.example.config.json` —— **配置文件形状示例**（`hooks.events.<Event>` 必须为「组数组」，组=`{matcher?, hooks:[…]}`；必须 `enabled: true` 才生效）

## 多平台可用性（实测口径）

| 平台 | hooks 支持 | 使用方式 | 备注 |
|---|---|---|---|
| Claude Code | ✅ 支持 | 把 `hooks.example.json` 内容并入 `~/.claude/settings.json`（或独立 `hooks.json`）；Windows 下 .sh 需 bash（Git Bash / WSL），脚本路径按实际调整 | 最成熟的钩子承载平台 |
| WorkBuddy | ⚠️ 待实测 | 若 `settings.json` 支持 hooks 则同 Claude 模式；否则以 `BOOTSTRAP.md` 作启动锚定（平台机制要求时） | 实测后按真实结果标注 |
| Codex | ⚠️ 待实测 | `~/.codex/config.toml` 事件/hooks 支持按版本确认；不支持则如实标「平台可选」 | 不清洗 config.toml 既有字段 |
| ZCode | ✅ 支持（实测 v3.11.2 / CLI 0.16.5） | 用户级 `~/.zcode/cli/config.json` 顶层 `hooks` 段；7 事件=SessionStart/UserPromptSubmit/PreToolUse/PermissionRequest/PostToolUse/PostToolUseFailure/Stop；Windows 推荐 `process` 型（无 shell 参数向量） | **坑（实测 F17）**：事件名写错或形状照抄插件形 → schema 校验**整文件静默失效**（config.file.invalid），其他配置一并失联；`--max-turns`/`--settings` 在该版 help 中列出但解析器未实现 |
| Trae / Cursor / Windsurf | ⚠️ 视版本 | 规则文件/全局设置已覆盖；hooks 属可选加固 | 依赖应用版本能力 |

**统一原则**：模板给的是**可将纪律自动锚定的示例**；hook 脚本不可用时，降级为「规则文件 + 注入核心已在场」即可——hooks 是加固面，不是必需面；本目录文件不参与运行时，发布前仅校验结构齐全（verify-release B 项）。