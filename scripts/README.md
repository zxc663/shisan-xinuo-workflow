# 维护脚本使用文档（verify-release.ps1 + syncer.py）

仓库维护工具：**发布前一致性/泄漏门禁校验**（P0 机制）+ **Skill 自更新三路合并器**。二者都是仓库维护工具，不属于 skill 包交付物（不随 npm/skills.sh 发布）。

## 一、verify-release.ps1（发布门禁）

发布前一致性 / 泄漏门禁校验（**P0 机制**）。修复「多版本 SKILL 靠自律同步、静默漂移」的结构短板——发布前必跑，任一项不过即退出码 1，阻止带缺陷/泄漏的发布物外发。

### 位置与运行

```powershell
# PowerShell
powershell -NoProfile -ExecutionPolicy Bypass -File scripts\verify-release.ps1

# 指定项目根（可选；默认取脚本上一级）
powershell -ExecutionPolicy Bypass -File scripts\verify-release.ps1 -Root <仓库根绝对路径>

# 跳过泄漏检测（仅查结构/版本/hooks）
powershell -ExecutionPolicy Bypass -File scripts\verify-release.ps1 -SkipLeak
```

只读、非破坏性，不改动任何文件。

### 校验项（A–D，v2.0 单版本口径）

| 项 | 检查内容 | 通过标准 |
|---|---|---|
| **A 内容锚点** | 主交付物 `skill/…/SKILL.md` 含全部关键特性串：`L2-S` / `L2-F` / `对接真相` / `GATE:` / `zxc663` / `速查表` / `三级同步` / `Base directory`；`references/injection-core.md` 含 `L2-S` / `L2-F` / `对接真相` / `三级同步链` / `Base directory`；`references/new-project-bootstrap.md` 存在 | 锚点零缺失（**门禁修复：校验内容覆盖度，不再只比对版本号**——v1.19.1 实测内容差 57% 仍 5/5 PASS 是其直接成因） |
| **B hooks 三层** | 主交付物 `templates/hooks/` 三件套 | `session-start.example.sh`+`session-end.example.sh`+`hooks.example.json` 齐全，且 JSON 同时声明 `SessionStart` 与 `SessionEnd` |
| **C 版本一致** | `SKILL.md metadata.version` == `package.json version` | 两处相等（v2.0 起无多语版，三版一致性校验随多版删除而取消） |
| **D 泄漏红线** | 发布物范围（`skill/` + README/package.json/LICENSE + `scripts/`） | 无作者机密目录路径 / 无本仓真实绝对路径 / 无真实用户主目录路径（`C:\Users\<名>…`）/ 无令牌原文（ghp_/gho_/github_pat_）/ 发布物内无个人版路径引用（README 版本说明豁免；占位符 `…` 属文档示例，不算泄漏） |

### 退出码

| 码 | 含义 |
|---|---|
| 0 | 全部通过，可安全发布 |
| 1 | 至少一项失败（打印 FAIL 明细） |
| 2 | 参数/路径错误（Root 不存在） |

### 预期当前输出

v2.0.2 单版本配置下当前应全 PASS：

```
[PASS] A 内容锚点(主交付物全量特性)   (OK)
[PASS] B hooks 三层齐全(主交付物)   (OK)
[PASS] C 版本一致(交付物=package.json)   (SKILL version=2.0.2 ; package.json version=2.0.2)
[PASS] D 泄漏红线(发布物)   (0 泄漏)
```

### 何时必跑

- **每次发布前**（GitHub Release / npm publish / ClawHub publish）。
- 改动涉及 `metadata.version`、`templates/hooks/`、SKILL.md 关键特性、或任何内容重构后。

### 接入 CI

`.github/workflows/verify-release.yml` 已在仓库内（PR + tag push 触发，windows runner）。本地等价命令：

```yaml
- name: Verify release consistency
  shell: pwsh
  run: pwsh scripts/verify-release.ps1
```

### 可靠性验证（正/负向）

脚本交付时已做双向验证，防止"假实现"：

- **正向**：当前内容锚点齐全、版本一致、无泄漏 → 全项 PASS，退出 0
- **负向**：临时删 SKILL.md 里一个锚点（如 `对接真相`）→ 脚本正确 FAIL「A 内容锚点」，退出 1；还原后恢复 PASS

### 原理 / 迭代背景

- 成因（经验库 #11）：Skill 含多个 SKILL 版本，改单版后靠自律同步其余版，发布链仅做泄密防护、无一致性校验，漂移无人拦截（v1.9.1 中英文 SessionEnd 钩子即因缺该校验而漏同步）。
- 落点（设计决策 #24）：本地 PowerShell 门禁（本仓仍手动发布，先本地强制，退出码便于日后套 CI）。
- **门禁盲区修复（2026-08-30 v2.0）**：v1.19.1 的 A 项只比对版本号 + 增补标记字符串，第三方审计实测「内容差 57% 仍 5/5 PASS」。v2.0 起改为**内容锚点校验**——关键特性必须物理出现在主交付物中，从机制上杜绝「版本号对、内容降级」。
- **泄漏面迭代（2026-08-30）**：D 项此前仅匹配特定外部机密目录、且不扫描 `scripts/`，导致 `syncer.py` 与脚本文档中的本仓工作目录路径漏检；后加宽为通用磁盘绝对路径并纳入 `scripts/` 后，又出现自引用误报（脚本自身的正则、文档示例 `C:\Users\…` 均命中）。最终改为**无歧义的具体泄漏特征**（作者机密目录 / 本仓真实路径 / 真实用户主目录 `C:\Users\<名>` / 令牌 / 发布物内个人版路径引用），`…` 占位符属文档示例不视为泄漏，规避自引用循环。

## 二、syncer.py（Skill 自更新三路合并器）

`skill/shisan-xinuo-workflow/references/injection-core.md` 的「Skill 自更新协议」对应的执行器。把仓库 `skill/`（唯一中文版主交付物）同步到本机 Skill 安装目录。

### 位置与运行

```powershell
# 仓库根下运行；默认 src=仓库 skill/shisan-xinuo-workflow，dest=~\.agents\skills\shisan-xinuo-workflow
python scripts\syncer.py

# 干跑（列出全部变更，不写盘；不崩于任何状态）
python scripts\syncer.py --dry

# 指定源 / 目标 / 备份目录（三路合并练习）
python scripts\syncer.py --src <源库 skill 路径> --dest <目标副本路径> --backup-dir <备份根路径>
```

### 协议要点（用户拍板 2026-08-30；红线，代码里真实执行）

- `user-notes/`（用户规则）与 `memory/`（skill 自身落盘）与 `*.bak-*` **永不碰**（巡检跳过、覆盖时从 os.walk 剔除、变更清单显式声明）。
- 上游（源库 `skill/`）整体覆盖：SKILL.md / references/* / templates/*；源权威（判级块 / 红线 / 必问协议）上游胜；不可解冲突 → 保留本地 + 清单标 `CONFLICT`。
- 副本内非源库文件（如 `references/personal-playbook.md`）→ 一次性迁移进 `user-notes/`，此后手动改副本一律写 `user-notes/`。

### v2.0 修复（实测驱动，2026-08-30）

1. **首次安装必崩修复**：目标目录不存在时，v1.19.1 直接 `shutil.copytree` 抛 `FileNotFoundError`——现改为跳过备份、直接创建并全量复制（exit=0）；README 安装路径与默认 dest 不一致时不再崩。
2. **备份目录外置（WorkBuddy 实测缺陷）**：v1.19.1 备份在 `<dest>.bak-<ts>`（skill 目录同级）——**落在平台扫描路径内**，平台把备份目录收录为第二个同名 Skill 并选中旧版（症状：升级成功但行为完全没变，平台加载 v1.11.0）。现默认备份到 **`<dest 的上级父目录>/skill-backups/<名>.bak-<ts>`**（扫描路径之外），可用 `--backup-dir` 覆盖；验收以**平台加载时的 Base directory** 为准，不是文件版本号。
3. **死代码清理**：删除未使用的 `SIBLINGS_EXCLUDE` 与空 `pass` 分支。
4. **dry-run 语义修正**：`break` 移出 `os.walk` 循环——干跑现在列出全部预期变更，而非固定输出「无列示」。
5. **路径输出**：完成时打印解析到的 src/dest 与验收提示（Base directory 判据）。

### 与 README 安装路径的关系

README 的安装方式（`npx skills add` / 各平台技能目录）可能把副本装在非默认位置——请用 `--dest` 显式指定，或让首次安装分支兜底（不存在 → 全量创建）。