<#
.SYNOPSIS
    Shisan Xinuo Workflow — 发布前一致性/泄漏门禁校验（P0 机制，v2.0 单版本）
.DESCRIPTION
    校验唯一主交付物（中文版 skill/shisan-xinuo-workflow，v2.0 起单版本、无多语版）在发布前满足：
      A. 内容锚点完整：SKILL.md 必须含全部关键特性串（L2-S / L2-F / 对接真相 / GATE: / zxc663 / 速查表 / 三级同步 / Base directory），
         injection-core.md 必须含三级跑道与对接真相（修复「版本号一致、内容实质性降级」的门禁盲区——v1.19.1 实测内容差 57% 仍 5/5 PASS）
      B. hooks 三层齐全：templates/hooks/ 含 session-start / session-end / hooks.json，且 hooks.json 同时声明 SessionStart 与 SessionEnd
      C. 版本一致：SKILL.md metadata.version == package.json version
      D. 泄漏红线：发布物范围内不出现个人版路径 / 外部机密目录 / 本仓真实路径 / 真实用户主目录 / 令牌原文（ghp_/gho_/github_pat_）
    用途：发布前必跑，任一项不过即退出码 1。本脚本只读、非破坏性，不改动任何文件。
.PARAMETER Root
    项目根目录，默认取脚本所在目录的上一级。
.PARAMETER SkipLeak
    跳过泄漏红线检测（如仅做结构/版本/钩子校验时）。
.OUTPUTS
    PASS / FAIL 逐项清单；退出码 0=全过，1=任一失败；2=参数/路径错误。
.EXAMPLE
    powershell -ExecutionPolicy Bypass -File scripts\verify-release.ps1
#>

[CmdletBinding()]
param(
    [string]$Root = "",
    [switch]$SkipLeak
)

# ---------- 路径解析 ----------
$ErrorActionPreference = "Stop"
if (-not $Root) { $Root = Split-Path -Parent $PSScriptRoot }
if (-not $PSScriptRoot) { $PSScriptRoot = Split-Path -Parent $MyInvocation.MyCommand.Path }
$Root = [System.IO.Path]::GetFullPath($Root)
if (-not (Test-Path $Root)) { Write-Host "E: Root 不存在: $Root" -ForegroundColor Red; exit 2 }

# ---------- 主交付物（唯一版本：中文 skill/） ----------
$skDir = Join-Path $Root "skill\shisan-xinuo-workflow"
$main  = Join-Path $skDir "SKILL.md"

# ---------- 状态收集 ----------
$results  = [System.Collections.Generic.List[string]]::new()
$failures = [System.Collections.Generic.List[string]]::new()
function Add-Result([bool]$ok, [string]$name, [string]$detail) {
    $results.Add([string]::Format("{0}`t{1}`t{2}", ($(if($ok){"PASS"}else{"FAIL"})), $name, $detail))
    if (-not $ok) { $failures.Add($name) }
}

if (-not (Test-Path $main)) {
    Add-Result $false "B路径存在" "缺失主交付物: $main"
    Write-Host "FAILED (缺主交付物)" -ForegroundColor Red
    exit 1
}

# ---------- A. 内容锚点（门禁修复：校验内容覆盖度，防「门禁全绿但内容降级」） ----------
$anchorsSkill = @(
    "L2-S",            # 三级跑道·短工作流
    "L2-F",            # 三级跑道·完整 11 步
    "对接真相",         # 对接真相清单
    "GATE:",           # GATE 完成块
    "zxc663",          # 彩蛋自检
    "速查表",           # §12 速查表
    "三级同步",         # 判级三级同步链声明
    "Base directory",  # 自更新验收判据
    "折叠协议",         # v2.1 上下文折叠协议（保留清单五必留 → checkpoint → 摘要 → 重载）
    "项目级注入点"      # v2.1.1 承载平台适配（项目规则文件按平台注入点表定名）
)
$anchorsCore = @(
    "L2-S", "L2-F", "对接真相", "三级同步链", "Base directory",
    "保留清单",          # v2.1 Preserver 保留清单五必留（压缩/折叠/交接前核对）
    "项目级注入点"       # v2.1.1 开工六步：项目规则文件按平台注入点表定名
)
$newBootstrap = Join-Path $skDir "references\new-project-bootstrap.md"
$probsA = @()
$txt = Get-Content $main -Raw -Encoding UTF8
foreach ($anc in $anchorsSkill) { if ($txt -notmatch [regex]::Escape($anc)) { $probsA += "SKILL 缺锚点[$anc]" } }
$core = Join-Path $skDir "references\injection-core.md"
if (-not (Test-Path $core)) { $probsA += "缺 injection-core.md" } else {
    $ctxt = Get-Content $core -Raw -Encoding UTF8
    foreach ($anc in $anchorsCore) { if ($ctxt -notmatch [regex]::Escape($anc)) { $probsA += "injection-core 缺锚点[$anc]" } }
}
if (-not (Test-Path $newBootstrap)) { $probsA += "缺 references/new-project-bootstrap.md" }
Add-Result ($probsA.Count -eq 0) "A 内容锚点(主交付物全量特性)" $(if($probsA.Count -eq 0){"OK"}else{$probsA -join ";"})

# ---------- B. hooks 三层齐全（主交付物） ----------
$hookFiles = @("session-start.example.sh","session-end.example.sh","hooks.example.json")
$hDir = Join-Path $skDir "templates\hooks"
$probs2 = @()
foreach ($hf in $hookFiles) { if (-not (Test-Path (Join-Path $hDir $hf))) { $probs2 += "缺 $hf" } }
$json = Join-Path $hDir "hooks.example.json"
if (Test-Path $json) {
    $hj = Get-Content $json -Raw | ConvertFrom-Json
    $hjH = $hj.hooks; if ($null -eq $hjH -or $hjH.PSObject.Properties.Name -notcontains 'SessionStart' -or $hjH.PSObject.Properties.Name -notcontains 'SessionEnd') { $probs2 += 'hooks.json 缺双钩子声明' }
}
Add-Result ($probs2.Count -eq 0) "B hooks 三层齐全(主交付物)" $(if($probs2.Count -eq 0){"OK"}else{$probs2 -join ";"})

# ---------- C. 版本一致（交付物 == package.json） ----------
$baseVer = ((Get-Content $main -Raw -Encoding UTF8 | Select-String -Pattern '(?s)version\s*:\s*([0-9]+\.[0-9]+\.[0-9]+)' -AllMatches).Matches[0].Groups[1].Value)
$pkgVersion = ((Get-Content (Join-Path $Root "package.json") -Raw -Encoding UTF8 | ConvertFrom-Json).version)
Add-Result ($baseVer -eq $pkgVersion) "C 版本一致(交付物=package.json)" "SKILL version=$baseVer ; package.json version=$pkgVersion"

# ---------- D. 泄漏红线（发布物范围） ----------
if (-not $SkipLeak) {
    $leakPaths = @(
        (Join-Path $Root "skill"),
        (Join-Path $Root "README.md"),
        (Join-Path $Root "package.json"),
        (Join-Path $Root "LICENSE"),
        (Join-Path $Root "scripts")
    )
    $tokenPats = @('ghp_[A-Za-z0-9]{20,}', 'gho_[A-Za-z0-9]{20,}', 'github_pat_[A-Za-z0-9_]{20,}')
    $leakHits = @()
    foreach ($lp in $leakPaths) {
        if (-not (Test-Path $lp)) { continue }
        Get-ChildItem -Path $lp -Recurse -File -ErrorAction SilentlyContinue | ForEach-Object {
            $rel = $_.FullName.Substring($Root.Length + 1)
            $text = Get-Content $_.FullName -Raw -ErrorAction SilentlyContinue
            # 1) 无歧义的真实泄漏特征：作者机密目录 / 本仓真实路径 / 真实用户主目录。
            #    不匹配 `…` 占位符（文档示例 `C:\Users\…` 不是 [A-Za-z]），
            #    也不匹配本脚本自身定义的正则文本，故无自引用误报。
            if ($text -match 'D:\\Agent个人资源|Agent个人资源\\02-Gitee|Agent个人资源\\机密资源|D:\\Agent工作流启动包|C:\\Users\\[A-Za-z]') {
                $leakHits += "$rel :: 引外部磁盘/个人路径"
            }
            # 2) 令牌原文
            foreach ($tp in $tokenPats) { if ($text -match $tp) { $leakHits += "$rel :: 疑似令牌明文(已掩码)" ; break } }
            # 3) 发布物内出现个人版路径（README 版本说明豁免）
            if (($rel -notlike "README.md") -and ($text -match 'versions[\/]personal-zh')) {
                $leakHits += "$rel :: 发布物内引用个人版路径"
            }
        }
    }
    Add-Result ($leakHits.Count -eq 0) "D 泄漏红线(发布物)" $(if($leakHits.Count -eq 0){"0 泄漏"}else{$leakHits -join ";"})
}

# ---------- E. 正文净化（常驻面/模板面过程注记 = 0；正文 vs 史料规范，v2.1.1） ----------
$probsE = @()
$cleanFiles = @($main, $core)
if (Test-Path (Join-Path $skDir "templates")) {
    $cleanFiles += Get-ChildItem (Join-Path $skDir "templates") -Recurse -File -Filter *.md | ForEach-Object { $_.FullName }
}
foreach ($cf in $cleanFiles) {
    if (-not (Test-Path $cf)) { continue }
    $t = Get-Content $cf -Raw -Encoding UTF8
    foreach ($pat in @('用户拍板','用户定调','作者定调','2026-08','2026-09')) {
        if ($t -match [regex]::Escape($pat)) { $probsE += "$(Split-Path $cf -Leaf) 含过程注记[$pat]" }
    }
}
Add-Result ($probsE.Count -eq 0) "E 正文净化(常驻/模板面过程注记=0)" $(if($probsE.Count -eq 0){"OK"}else{$probsE -join ";"})

# ---------- 汇总输出 ----------
Write-Host ""
Write-Host "=== verify-release 结果 ===" -ForegroundColor Cyan
foreach ($r in $results) {
    $parts = $r -split "`t", 3
    $mark = $parts[0]; $name = $parts[1]; $detail = if($parts.Length -gt 2){$parts[2]}else{""}
    $fg = if ($mark -eq "PASS") { "Green" } else { "Red" }
    Write-Host ("[" + $mark + "] " + $name) -ForegroundColor $fg
    if ($detail) { Write-Host ("      " + $detail) -ForegroundColor Gray }
}
Write-Host ""

if ($failures.Count -gt 0) {
    Write-Host "FAILED ($($failures.Count) 项)：$($failures -join ', ')" -ForegroundColor Red
    exit 1
} else {
    Write-Host "ALL PASS — 可安全发布。" -ForegroundColor Green
    exit 0
}
