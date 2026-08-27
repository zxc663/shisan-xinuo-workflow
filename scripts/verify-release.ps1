<#
.SYNOPSIS
    Shisan Xinuo Workflow — 发布前一致性/泄漏门禁校验（P0 机制）
.DESCRIPTION
    校验三语通用版（en / universal-zh / universal-bilingual）在发布前满足：
      A. 结构指纹一致：三版 SKILL 相对文件清单完全对称（Compare-Object 无差异）
      B. hooks 三层齐全：每版 templates/hooks/ 含 session-start / session-end / hooks.json，
         且 hooks.json 同时声明 SessionStart 与 SessionEnd
      C. 版本一致：三版 SKILL.md 的 metadata.version 相等，且 == package.json version
      D. 泄漏红线：发布物范围内不出现个人版路径 / memory / 令牌原文（ghp_/gho_/github_pat_）
    用途：修复"靠自律同步多版、静默漂移"的结构短板——每次发布前必跑，任一项不过即退出码 1。
    本脚本只读、非破坏性，不改动任何文件。
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

# ---------- 待校验版本（主版 + 两个通用版） ----------
$sk = @{
    "en" = Join-Path $Root "skill\shisan-xinuo-workflow"
    "zh" = Join-Path $Root "versions\universal-zh\shisan-xinuo-workflow"
    "bi" = Join-Path $Root "versions\universal-bilingual\shisan-xinuo-workflow"
}

# ---------- 状态收集 ----------
$results  = [System.Collections.Generic.List[string]]::new()
$failures = [System.Collections.Generic.List[string]]::new()
function Add-Result([bool]$ok, [string]$name, [string]$detail) {
    $results.Add([string]::Format("{0}`t{1}`t{2}", ($(if($ok){"PASS"}else{"FAIL"})), $name, $detail))
    if (-not $ok) { $failures.Add($name) }
}

# 缺失任一版直接判失败
$missing = $sk.GetEnumerator() | Where-Object { -not (Test-Path $_.Value) } | ForEach-Object { $_.Key }
if ($missing.Count -gt 0) {
    Add-Result $false "B路径存在" "缺失版: $($missing -join ',')"
}

# ---------- A. 结构指纹一致 ----------
function Get-RelFileSet([string]$dir) {
    if (-not (Test-Path $dir)) { return @() }
    return (Get-ChildItem -Path $dir -Recurse -File -ErrorAction SilentlyContinue) |
        ForEach-Object { $_.FullName.Substring($dir.Length + 1).Replace('\','/') } | Sort-Object
}
$sets = @{}
foreach ($k in $sk.Keys) { $sets[$k] = @(Get-RelFileSet $sk[$k]) }
if ($missing.Count -eq 0) {
    $base = "en"
    $diffs = @()
    foreach ($k in @("zh","bi")) {
        $c = Compare-Object $sets[$base] $sets[$k]
        foreach ($d in $c) {
            $side = if ($d.SideIndicator -eq '<=') { "仅EN有" } else { "仅$k有" }
            $diffs += "$side :: $($d.InputObject)"
        }
    }
    Add-Result ($diffs.Count -eq 0) "A 结构指纹三语一致" $(if($diffs.Count -eq 0){"22 文件完全对称 (en/zh/bi)"}else{$diffs -join ";"})
}

# ---------- B. hooks 三层齐全 + JSON 双钩子 ----------
$hookFiles = @("session-start.example.sh","session-end.example.sh","hooks.example.json")
foreach ($k in $sk.Keys) {
    $hDir = Join-Path $sk[$k] "templates\hooks"
    $probs = @()
    if (Test-Path $hDir) {
        foreach ($hf in $hookFiles) { if (-not (Test-Path (Join-Path $hDir $hf))) { $probs += "缺 $hf" } }
        $json = Join-Path $hDir "hooks.example.json"
        if ((Test-Path $json) -and $probs.Count -eq 0) {
            try {
                $cfg = Get-Content $json -Raw | ConvertFrom-Json
                if (-not $cfg.hooks.SessionStart) { $probs += "JSON 无 SessionStart" }
                if (-not $cfg.hooks.SessionEnd)   { $probs += "JSON 无 SessionEnd" }
            } catch { $probs += "JSON 解析失败: $($_.Exception.Message)" }
        }
    } else { $probs += "hooks 目录缺失" }
    Add-Result ($probs.Count -eq 0) "B hooks 三层齐全($k)" $(if($probs.Count -eq 0){"start/end/json + SessionStart+End 就位"}else{$probs -join ";"})
}

# ---------- C. 版本一致 ----------
function Get-SkillVersion([string]$dir) {
    if (-not (Test-Path (Join-Path $dir "SKILL.md"))) { return "" }
    $raw = Get-Content (Join-Path $dir "SKILL.md") -Raw
    if ($raw -match '(?m)(?s)^\s*metadata\s*:\s*\r?\n\s*version\s*:\s*([\d.]+)') { return $Matches[1] }
    return ""
}
if ($missing.Count -eq 0) {
    $ver = @{}
    foreach ($k in $sk.Keys) { $ver[$k] = Get-SkillVersion $sk[$k] }
    $versOk = ($ver.zh -eq $ver.bi) -and ($ver.en -eq $ver.zh)
    Add-Result $versOk "C 三语版本一致" ("en=$($ver.en) zh=$($ver.zh) bi=$($ver.bi)")
    $pkgVersion = ""
    $pkg = Join-Path $Root "package.json"
    if (Test-Path $pkg) { $pkgVersion = ((Get-Content $pkg -Raw | ConvertFrom-Json).version) }
    Add-Result ($versOk -and ($versOk -and $ver.en -eq $pkgVersion)) "C 与 package.json 一致" "package.json version=$pkgVersion"
}

# ---------- D. 泄漏红线（发布物范围） ----------
if (-not $SkipLeak) {
    # 发布物 = 三语通用版 + 根级交付文件（.gitignore 已屏蔽 personal-zh / memory）
    $leakPaths = @(
        (Join-Path $Root "skill"),
        (Join-Path $Root "versions\universal-zh"),
        (Join-Path $Root "versions\universal-bilingual"),
        (Join-Path $Root "README.md"),
        (Join-Path $Root "package.json"),
        (Join-Path $Root "LICENSE")
    )
    $tokenPats = @('ghp_[A-Za-z0-9]{20,}', 'gho_[A-Za-z0-9]{20,}', 'github_pat_[A-Za-z0-9_]{20,}')
    $leakHits = @()
    foreach ($lp in $leakPaths) {
        if (-not (Test-Path $lp)) { continue }
        Get-ChildItem -Path $lp -Recurse -File -ErrorAction SilentlyContinue | ForEach-Object {
            $rel = $_.FullName.Substring($Root.Length + 1)
            $text = Get-Content $_.FullName -Raw -ErrorAction SilentlyContinue
            # 1) 外部个人机密路径（D:\Agent个人资源\机密资源 等）——绝对路径泄漏
            if ($text -match 'D:\\Agent个人资源|机密资源\\02-Gitee|Agent个人资源\\机密资源') {
                $leakHits += "$rel :: 引外部机密文件路径"
            }
            # 2) 令牌原文
            foreach ($tp in $tokenPats) { if ($text -match $tp) { $leakHits += "$rel :: 疑似令牌明文(已掩码)" ; break } }
            # 3) 发布物内出现 personal-zh 目录实际内容（非 README 版本矩阵提及）
            $isReadme = $rel -eq "README.md" -or $rel -eq "项目信息.md"
            if ((-not $isReadme) -and ($text -match 'personal-zh|personal/')) {
                $leakHits += "$rel :: 发布物内引用个人版路径"
            }
        }
    }
    Add-Result ($leakHits.Count -eq 0) "D 泄漏红线(发布物)" $(if($leakHits.Count -eq 0){"0 泄漏"}else{$leakHits -join ";"})
}

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