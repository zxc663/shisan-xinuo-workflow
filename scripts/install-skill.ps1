<#
.SYNOPSIS
  shisan-xinuo-workflow 一键安装脚本 —— 带 agent- 前缀自适配部署到目标平台技能目录（幂等、可干跑）。

.DESCRIPTION
  从仓库 skill/ 复制（或 --Link 软链）到目标平台技能目录，并将安装名统一为
  agent-shisan-xinuo-workflow（agent- 前缀 = 技能列表按字母序置顶，便于按需注入用户发现）。
  已存在同名安装时提示，-Force 先备份到 <技能目录>\skill-backups\ 再覆盖；
  -HardInject 按 references/platform-adaptation.md 注入点表把 injection-core 核心全文写入
  平台配置文件/规则文件注入点（先备份 .bak-<ts> 再合并，含既有内容）。
  全部真实动作先打印；-Dry 只列出动作不写盘（幂等验证无副作用）。

.PARAMETER Prefix
  安装名前缀。默认 agent-。

.PARAMETER Source
  源 skill 目录。默认 <仓库根>\skill\shisan-xinuo-workflow。

.PARAMETER Platform
  目标平台：claude / codex / workbuddy / agents / cursor / trae / zcode。
  省略时自动探测本机首个已存在的技能目录。

.PARAMETER Link
  用符号链接安装而非复制（Windows 需管理员/开发者模式；失败自动降级为复制）。

.PARAMETER Force
  已存在同名安装时先备份到 skill-backups\ 再覆盖（备份位于平台扫描路径之外）。

.PARAMETER Target
  显式指定目标技能目录根（覆盖平台探测；用于精确安装或临时目录实测）。-HardInject 的注入点仍按 -Platform（省略时按探测平台）。

.PARAMETER HardInject
  安装后按平台注入点表写注入（先备份合并）。需与 -Platform 同用；省略时按探测到的平台。

.PARAMETER Dry
  只列出将要执行的动作，不写盘。

.EXAMPLE
  powershell -ExecutionPolicy Bypass -File scripts\install-skill.ps1 -Dry

.EXAMPLE
  powershell -ExecutionPolicy Bypass -File scripts\install-skill.ps1 -Platform workbuddy -Link -HardInject

.EXAMPLE
  powershell -ExecutionPolicy Bypass -File scripts\install-skill.ps1 -Platform claude -Force
#>
[CmdletBinding()]
param(
    [string]$Prefix = "agent-",
    [string]$Source = "",
    [string]$Platform = "",
    [switch]$Link,
    [switch]$Force,
    [string]$Target = "",
    [switch]$HardInject,
    [switch]$Dry
)

$ErrorActionPreference = "Stop"
$targetName = "$Prefix" + "shisan-xinuo-workflow"
$root = Split-Path -Parent $PSScriptRoot
$probeOrder = @("workbuddy", "claude", "agents", "codex", "cursor", "trae", "zcode")

# ---------- 平台 -> 技能目录 / 注入点 ----------
$skillsMap = @{
    "claude"    = @{ dir = "$HOME\.claude\skills";      inject = "" }
    "codex"     = @{ dir = "$HOME\.codex\skills";       inject = "$HOME\.codex\AGENTS.md" }
    "workbuddy" = @{ dir = "$HOME\.workbuddy\skills";   inject = "$HOME\.workbuddy\AGENTS.md" }
    "agents"    = @{ dir = "$HOME\.agents\skills";      inject = "" }
    "cursor"    = @{ dir = "$HOME\.cursor\skills";      inject = "" }
    "trae"      = @{ dir = "$HOME\.trae\skills";        inject = "$HOME\.trae-cn\user_rules\shisan-xinuo-workflow.md" }
    "zcode"     = @{ dir = "$HOME\.zcode\skills";       inject = "$HOME\.zcode\AGENTS.md" }
}

if (-not $Source) { $Source = Join-Path $root "skill\shisan-xinuo-workflow" }
if (-not (Test-Path $Source)) { Write-Error "源 skill 目录不存在：$Source"; exit 2 }

# ---------- 确定目标技能目录与平台 ----------
$skillsDir = ""
$injectFile = ""
if ($Platform) {
    $p = $Platform.ToLower()
    if (-not $skillsMap.ContainsKey($p)) { Write-Error "未知平台：$Platform（可选：claude / codex / workbuddy / agents / cursor / trae / zcode）"; exit 2 }
    $skillsDir = $skillsMap[$p].dir
    $injectFile = $skillsMap[$p].inject
} else {
    $found = @()
    foreach ($k in $probeOrder) {
        if (Test-Path $skillsMap[$k].dir) { $found += $k }
    }
    if ($found.Count -eq 0) {
        $skillsDir = "$HOME\.agents\skills"
        Write-Host "[探测] 未发现任何已存在技能目录，默认使用：$skillsDir"
    } else {
        $skillsDir = $skillsMap[$found[0]].dir
        $injectFile = $skillsMap[$found[0]].inject
        Write-Host "[探测] 候选平台：$($found -join ', ')；默认使用第一个：$skillsDir"
    }
}
$dest = Join-Path $skillsDir $targetName
if ($Target) {
    $skillsDir = $Target
    $injectFile = if ($Platform -and $skillsMap.ContainsKey($Platform.ToLower())) { $skillsMap[$Platform.ToLower()].inject } else { "" }
    $dest = Join-Path $skillsDir $targetName
}
if (Test-Path $skillsDir) { $skillsDirExists = $true } else { $skillsDirExists = $false }
if (-not $Dry -and -not $skillsDirExists) { $null = New-Item -ItemType Directory -Path $skillsDir -Force }
Write-Host "[目标] 安装名=$targetName ｜ 目标目录=$dest"

# ---------- 备份（已存在时，-Force 才覆盖）----------
$backupRoot = Join-Path $skillsDir "skill-backups"
$backup = Join-Path $backupRoot ("{0}.bak-{1}" -f $targetName, (Get-Date -Format "yyyyMMdd-HHmmss"))
if (Test-Path $dest) {
    if (-not $Force) {
        Write-Warning "目标已存在：$dest（如需覆盖请加 -Force；-Force 会先备份到 $backupRoot——平台扫描路径之外，符合 syncer 备份外置纪律）"
        exit 1
    }
    if ($Dry) { Write-Host "[干跑] 备份现有安装 → $backup" }
    else {
        $null = New-Item -ItemType Directory -Path $backupRoot -Force
        Copy-Item -Path $dest -Destination $backup -Recurse -Force
        Write-Host "[备份] $backup"
    }
}

# ---------- 复制 / 软链 ----------
if ($Dry) {
    $mode = if ($Link) { "软链" } else { "复制" }
    Write-Host "[干跑] $mode $Source`n        → $dest"
} elseif ($Link) {
    try {
        $null = New-Item -ItemType SymbolicLink -Path $dest -Target $Source
        Write-Host "[链接] $dest  →  $Source"
    } catch {
        Write-Warning "软链创建失败（需管理员权限或开发者模式）：$($_.Exception.Message)；降级为复制。"
        Copy-Item -Path $Source -Destination $dest -Recurse -Force
        Write-Host "[复制] $dest"
    }
} else {
    Copy-Item -Path $Source -Destination $dest -Recurse -Force
    Write-Host "[复制] $dest"
}

# ---------- 硬注入（可选；按 platform-adaptation 注入点表）----------
if ($HardInject) {
    $core = Join-Path $Source "references\injection-core.md"
    if (-not (Test-Path $core)) { Write-Warning "[注入] 源缺少 references\injection-core.md，跳过注入（安装已完成）。"; return }
    if (-not $injectFile) {
        $pn = if ($Platform) { $Platform } else { "未指定" }
        Write-Host "[注入] 平台 $pn 无标准注入点（本脚本未登记），跳过注入（安装已完成）。"
    } else {
        $ts = Get-Date -Format "yyyyMMdd-HHmmss"
        if ($Dry) {
            Write-Host "[干跑] 备份注入点 → $injectFile.bak-$ts ；写入 injection-core 至 $injectFile"
        } else {
            $coreText = Get-Content -Raw -Encoding UTF8 $core
            $header = @"
# 全局 Agent 工作流核心（十三希诺工作流 · 每会话强制生效）—— v2.0+ 安装脚本注入
> 平台：$($Platform.ToLower())（$targetName 安装于 $target）
> 注入来源：$Source\references\injection-core.md
> 更新协议：python scripts\syncer.py（三路合并，备份落 skill-backups/·平台扫描路径外）｜验收判据：平台加载时的 Base directory，不是文件版本号
> 注入时间：$(Get-Date -Format "yyyy-MM-dd HH:mm:ss") ｜ 写入前备份：$injectFile.bak-$ts
---
"@
            $prev = ""
            if (Test-Path $injectFile) {
                Copy-Item -Path $injectFile -Destination "$injectFile.bak-$ts" -Force
                $prev = Get-Content -Raw -Encoding UTF8 $injectFile
                Write-Host "[注入] 备份既有注入点 → $injectFile.bak-$ts"
            }
            $sep = if ($prev.Trim().Length -gt 0) { "`n`n---`n" } else { "" }
            Set-Content -Path $injectFile -Value ($prev.TrimEnd() + $sep + $header + $coreText) -Encoding UTF8
            Write-Host "[注入] $(if ($prev.Trim().Length -gt 0) { '合并（既有内容保留在上方）' } else { '新建' }) → $injectFile"
        }
    }
}

# ---------- 验收 ----------
Write-Host ""
Write-Host "[完成] 安装目录：$dest"
Write-Host "[验收] 平台加载时的 Base directory 应指向：$dest（不是文件版本号；若平台扫描到 skill-backups\ 目录，请确认其位于扫描路径之外）"
Write-Host "[提示] 安装名已带 $Prefix 前缀 → SKILL.md §3 第 0 步安装名前缀自检将静默通过；无前缀安装会收到一行适配提示。"
exit 0