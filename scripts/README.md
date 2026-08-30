# verify-release.ps1 使用文档

发布前一致性 / 泄漏门禁校验（**P0 机制**）。修复「多版本 SKILL 靠自律同步、静默漂移」的结构短板——发布前必跑，任一项不过即退出码 1，阻止带缺陷/泄漏的发布物外发。

## 位置与运行

脚本位于 `scripts/verify-release.ps1`（仓库根下）。运行：

```powershell
# PowerShell
powershell -NoProfile -ExecutionPolicy Bypass -File scripts\verify-release.ps1

# 指定项目根（可选；默认取脚本上一级）
powershell -ExecutionPolicy Bypass -File scripts\verify-release.ps1 -Root <仓库根绝对路径>

# 跳过泄漏检测（仅查版本/增补/hooks）
powershell -ExecutionPolicy Bypass -File scripts\verify-release.ps1 -SkipLeak
```

只读、非破坏性，不改动任何文件。

## 校验项（A–D）

| 项 | 检查内容 | 通过标准 |
|---|---|---|
| **A 增补制一致** | 主交付物 `skill/…/SKILL.md` 的 `version` 为权威 base；三语（zh/bi）的 `metadata.version` 与其相等，且正文含 `v1.12-1.19` 增补标记 | 三版版本号相等，且 zh/bi 均含增补标记 |
| **B hooks 三层** | 主交付物 `templates/hooks/` 三件套 | `session-start.example.sh`+`session-end.example.sh`+`hooks.example.json` 齐全，且 JSON 同时声明 `SessionStart` 与 `SessionEnd` |
| **C 版本一致** | 三语 `metadata.version` 与 `package.json` | 三版版本号相等，且等于 `package.json version` |
| **D 泄漏红线** | 发布物范围（三语通用版 + README/package.json/LICENSE + `scripts/`） | 无作者机密目录路径 / 无本仓真实绝对路径 / 无真实用户主目录路径（`C:\Users\<名>…`）/ 无令牌原文（ghp_/gho_/github_pat_）/ 发布物内无个人版路径引用（占位符 `…` 属文档示例，不算泄漏） |

**增补制口径**：v1.16 起英文为权威、中文/双语为增补制同步，因此一致性比的是「版本号 + 增补标记」，而非要求三语字节逐行同文（增补制刻意不伪装全量同文）。

## 退出码

| 码 | 含义 |
|---|---|
| 0 | 全部通过，可安全发布 |
| 1 | 至少一项失败（打印 FAIL 明细） |
| 2 | 参数/路径错误（Root 不存在） |

## 预期当前输出

v1.19 后当前应全 PASS：

```
[PASS] A 增补制一致（主交付物 base + 三语增补标记）   (OK)
[PASS] B hooks 三层齐全(主交付物)   (OK)
[PASS] C 四版版本一致(=base)   (en=1.19.0 zh=1.19.0 bi=1.19.0)
[PASS] C 与 package.json 一致   (package.json version=1.19.0)
[PASS] D 泄漏红线(发布物)   (0 泄漏)
```

## 何时必跑

- **每次发布前**（GitHub Release / npm publish / ClawHub publish）——尤其是涉及 versions 下任一版改动的发布。
- 改动涉及 `metadata.version`、`templates/hooks/`、新增/删除任一版本文件、或任何多版本同步时。

## 接入 CI（可选）

后续可用 GitHub Actions 定时/发布前 gate：

```yaml
- name: Verify release consistency
  shell: pwsh
  run: pwsh scripts/verify-release.ps1
```

## 可靠性验证（正/负向）

脚本交付时已做双向验证，防止"假实现"：

- **正向**：当前三语一致 → 全项 PASS，退出 0
- **负向**：临时把双语版 `version` 改 `1.19.9` → 脚本正确 FAIL「C 四版版本一致」「C 与 package.json 一致」两项，退出 1；还原后恢复 PASS

## 原理 / 迭代背景

- 成因（经验库 #11）：Skill 含多个 SKILL 版本，改单版后靠自律同步其余版，发布链仅做泄密防护、无一致性校验，漂移无人拦截（v1.9.1 中英文 SessionEnd 钩子即因缺该校验而漏同步）。
- 落点（设计决策 #24）：本地 PowerShell 门禁（本仓仍手动发布，先本地强制，退出码便于日后套 CI）。
- **泄漏面迭代（2026-08-30）**：D 项此前仅匹配特定外部机密目录、且不扫描 `scripts/`，导致 `syncer.py` 与脚本文档中的本仓工作目录路径漏检；后加宽为通用磁盘绝对路径并纳入 `scripts/` 后，又出现自引用误报（脚本自身的正则、文档示例 `C:\Users\…` 均命中）。最终改为**无歧义的具体泄漏特征**（作者机密目录 / 本仓真实路径 / 真实用户主目录 `C:\Users\<名>` / 令牌 / 发布物内个人版路径引用），`…` 占位符属文档示例不视为泄漏，规避自引用循环。