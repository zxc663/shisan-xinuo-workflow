# verify-release.ps1 使用文档

发布前一致性 / 泄漏门禁校验（**P0 机制**）。修复「多版本 SKILL 靠自律同步、静默漂移」的结构短板——发布前必跑，任一项不过即退出码 1，阻止带缺陷/泄漏的发布物外发。

## 位置与运行

```
D:\Agent工作流启动包\shisan-xinuo-workflow\scripts\verify-release.ps1
```

```powershell
# PowerShell
powershell -NoProfile -ExecutionPolicy Bypass -File scripts\verify-release.ps1

# 指定项目根（可选；默认取脚本上一级）
powershell -ExecutionPolicy Bypass -File scripts\verify-release.ps1 -Root D:\Agent工作流启动包\shisan-xinuo-workflow

# 跳过泄漏检测（仅查结构/版本/hooks）
powershell -ExecutionPolicy Bypass -File scripts\verify-release.ps1 -SkipLeak
```

只读、非破坏性，不改动任何文件。

## 校验项（A–D）

| 项 | 检查内容 | 通过标准 |
|---|---|---|
| **A 结构指纹** | 三语通用版（en / zh / bi）相对文件清单对称性 | `Compare-Object` 双侧无差异，文件完全同组 |
| **B hooks 层** | 每版 `templates/hooks/` 三件套 | `session-start.sh`+`session-end.sh`+`hooks.example.json` 齐全，且 JSON 同时声明 `SessionStart` 与 `SessionEnd` |
| **C 版本一致** | 三语 `metadata.version` 与 `package.json` | 三版版本号相等，且等于 `package.json version` |
| **D 泄漏红线** | 发布物范围内 | 无外部机密绝对路径 / 无令牌原文（ghp_/gho_/github_pat_）/ 无发布物内引用个人版路径 |

**结构指纹口径**：三语是翻译版，内容字节必然不同，因此一致性比的是**文件清单结构**而非整树 sha256；字节比对会永远误报。

## 退出码

| 码 | 含义 |
|---|---|
| 0 | 全部通过，可安全发布 |
| 1 | 至少一项失败（打印 FAIL 明细） |
| 2 | 参数/路径错误（Root 不存在） |

## 预期当前输出

修复 v1.9.1 后当前应全 PASS：

```
[PASS] A 结构指纹三语一致   (22 文件完全对称)
[PASS] B hooks 三层齐全(en/zh/bi)   (start/end/json + SessionStart+End)
[PASS] C 三语版本一致   (en=1.9.1 zh=1.9.1 bi=1.9.1)
[PASS] C 与 package.json 一致   (1.9.1)
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

- **正向**：当前三语一致 → 7 项全 PASS，退出 0
- **负向**：临时把双语版 `version` 改 `1.9.9` → 脚本正确 FAIL「C 三语版本一致」「C 与 package.json 一致」两项，退出 1；还原后恢复 PASS

## 原理 / 迭代背景

- 成因（经验库 #11）：Skill 含 4 个 SKILL 版本，改单版后靠自律同步其余版，发布链仅做泄密防护、无一致性校验，漂移无人拦截（v1.9.1 中英文 SessionEnd 钩子即因缺该校验而漏同步）。
- 落点（设计决策 #24）：本地 PowerShell 门禁（本仓仍手动发布，先本地强制，退出码便于日后套 CI）。