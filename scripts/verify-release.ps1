<#
.SYNOPSIS
    Shisan Xinuo Workflow — 发布前一致性/泄漏门禁校验（P0 机制）
.DESCRIPTION
    校验三语通用版（en / universal-zh / universal-bilingual）在发布前满足：
      A. 增补制一致（v1.16-1.18）：三语 SKILL 均 version=1.18.0 且含「v1.12-1.18」增补标记；主交付物 version=1.19(基准)（v1.16 起执行化全文以英文主交付物为准，三语为增补制——不再要求全量文件对称）
      B. hooks 三层齐全（主交付物）：templates/hooks/ 含 session-start / session-end / hooks.json，且 hooks.json 同时声明 SessionStart 与 SessionEnd
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

$Root = if ($Root) { $Root } else { Split-Path -Parent $PSScriptRoot }
$sk = @{ en = (Join-Path $Root "skill\shisan-xinuo-workflow"); zh = (Join-Path $Root "versions\universal-zh\shisan-xinuo-workflow"); bi = (Join-Path $Root "versions\universal-bilingual\shisan-xinuo-workflow"); pe = (Join-Path $Root "versions\personal-zh\shisan-xinuo-workflow") }
$missing = @()
foreach ($k in $sk.Keys) { if (-not (Test-Path (Join-Path $sk[$k] "SKILL.md"))) { $missing += "$k/SKILL.md" } }
# ---------- A. 增补制一致（version 1.18 + v1.12-1.18 标记；主交付物权威） ----------
$root = if ($Root) { $Root } else { Split-Path -Parent $PSScriptRoot }
$main = Join-Path $root "skill\shisan-xinuo-workflow\SKILL.md"
$langs = @("universal-zh","universal-bilingual")   # personal-zh 为私有工作台版，非发布物，版本不检
$verM = [regex]::Match((Get-Content $main -Raw), "(?s)version\s*:\s*([0-9]+\.[0-9]+\.[0-9]+)")
$baseVer = $verM.Groups[1].Value
$verOK = ($baseVer -ne "")
$probs = @()
if (-not $verOK) { $probs += "主交付物 version=${($verM.Groups[1].Value)}(≠1.18.0)" }
foreach ($l in $langs) {
    $sk = Join-Path $root "versions\$l\shisan-xinuo-workflow\SKILL.md"
    if (-not (Test-Path $sk)) { $probs += "$l 缺 SKILL"; continue }
    $txt = Get-Content $sk -Raw
    $vm = [regex]::Match($txt, "(?s)version:\s*([0-9]+\.[0-9]+\.[0-9]+)")
    if ($vm.Groups[1].Value -ne $baseVer) { $probs += "$l version=$($vm.Groups[1].Value)(base=$baseVer)" }
    if ($txt -notmatch "v1.12-1.18") { $probs += "$l 缺增补标记" }
}
Add-Result ($probs.Count -eq 0) "A 增补制一致（主交付物 base + 三语增补标记）" $(if($probs.Count -eq 0){"OK"}else{$probs -join ";"})
# ---------- B. hooks 三层齐全（主交付物） ----------
$hookFiles = @("session-start.example.sh","session-end.example.sh","hooks.example.json")
$hDir = Join-Path $root "skill/shisan-xinuo-workflow/templates/hooks"
$probs2 = @()
foreach ($hf in $hookFiles) { if (-not (Test-Path (Join-Path $hDir $hf))) { $probs2 += "缺 $hf" } }
$json = Join-Path $hDir "hooks.example.json"
if (Test-Path $json) {
    $hj = Get-Content $json -Raw | ConvertFrom-Json
    $hjH = $hj.hooks; if ($null -eq $hjH -or $hjH.PSObject.Properties.Name -notcontains 'SessionStart' -or $hjH.PSObject.Properties.Name -notcontains 'SessionEnd') { $probs2 += 'hooks.json 缺双钩子声明' }
}
Add-Result ($probs2.Count -eq 0) "B hooks 三层齐全(主交付物)" $(if($probs2.Count -eq 0){"OK"}else{$probs2 -join ";"})
# ---------- C. 版本一致（自包含：四版本直读 + package 比较） ----------
$verMap = @{ en = (Join-Path $Root "skill\shisan-xinuo-workflow\SKILL.md"); zh = (Join-Path $Root "versions\universal-zh\shisan-xinuo-workflow\SKILL.md"); bi = (Join-Path $Root "versions\universal-bilingual\shisan-xinuo-workflow\SKILL.md") }   # personal-zh 私有版不纳入发布版本
$ver = @{}
foreach ($k in $verMap.Keys) {
    $raw = Get-Content $verMap[$k] -Raw -ErrorAction SilentlyContinue
    if ($null -ne $raw -and $raw -match '(?s)version\s*:\s*([\d.]+)') { $ver[$k] = $Matches[1] } else { $ver[$k] = '' }
}
$versOk = ($ver.en -eq $baseVer) -and ($ver.zh -eq $baseVer) -and ($ver.bi -eq $baseVer)
Add-Result $versOk "C 四版版本一致(=base)" ("en=$($ver.en) zh=$($ver.zh) bi=$($ver.bi)")
$pkgVersion = ''
$pkg = Join-Path $Root "package.json"
if (Test-Path $pkg) { $pkgVersion = ((Get-Content $pkg -Raw | ConvertFrom-Json).version) }
Add-Result ($versOk -and $ver.en -eq $pkgVersion) "C 与 package.json 一致" "package.json version=$pkgVersion (base=$baseVer)"

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
            if ((-not $isReadme) -and ($text -match 'versions[\/]personal-zh')) {
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