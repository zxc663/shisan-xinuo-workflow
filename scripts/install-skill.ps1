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

.PARAMETER MemoryFile
  硬注入第三层「记忆层」：把 references/templates/memory-anchor.md 锚点块写进该平台记忆文件
  （如 ~/.workbuddy/MEMORY.md、~/.trae-cn/memory/user_profile.md）。先备份 .bak-<ts> 再合并（追加，保留既有内容）。
  仅与 -HardInject 同用；省略 = 只写规则层 + 配置文件层（向后兼容）。

.PARAMETER Dry
  只列出将要执行的动作，不写盘。

.EXAMPLE
  powershell -ExecutionPolicy Bypass -File scripts\install-skill.ps1 -Dry

.EXAMPLE
  powershell -ExecutionPolicy Bypass -File scripts\install-skill.ps1 -Platform workbuddy -Link -HardInject -MemoryFile "$HOME\.workbuddy\MEMORY.md"

.EXAMPLE
  powershell -ExecutionPolicy Bypass -File scripts\install-skill.ps1 -Platform claude -Force
#>
[CmdletBinding()]
param(
    [string]$Prefix = "agent-",
    [string]$PackageName = "shisan-xinuo-workflow",
    [switch]$Family,
    [string]$Source = "",
    [string]$Platform = "",
    [switch]$Link,
    [switch]$Force,
    [string]$Target = "",
    [switch]$HardInject,
    [string]$MemoryFile = "",
    [switch]$Dry
)

$ErrorActionPreference = "Stop"
$targetName = "$Prefix" + $PackageName
$root = Split-Path -Parent $PSScriptRoot
$probeOrder = @("workbuddy", "claude", "agents", "codex", "cursor", "trae", "zcode")

# ---------- 多包模式（v3.0 家族 → v4.1.0 R2 · A-13/F-53 五包全装：核心包入循环，-Family 单跑不再缺核心） ----------
if ($Family) {
    $repoSkill = Join-Path (Split-Path -Parent $PSScriptRoot) "skill"
    $familyPkgs = @("shisan-xinuo-workflow", "shisan-xinuo-flows", "shisan-xinuo-roles", "shisan-xinuo-product", "shisan-xinuo-single")
    foreach ($pkg in $familyPkgs) {
        $pkgSrc = Join-Path $repoSkill $pkg
        Write-Host "`n===== family 安装: $pkg =====" -ForegroundColor Cyan
        & $PSCommandPath -Prefix $Prefix -PackageName $pkg -Source $pkgSrc -Platform $Platform -Target $Target -Dry:$Dry -Force:$Force
        if ($LASTEXITCODE -ne 0) { throw "family 子安装失败: $pkg（exit=$LASTEXITCODE）" }
    }
    Write-Host "[family done] 五包全装完成：$($familyPkgs -join ' / ')"
    exit 0
}

# ---------- 平台 -> 技能目录 / 注入点 ----------
# 路径口径对齐（F-28）：技能目录以本机活体 Base directory 为准（zcode/agents 共用 $HOME\.agents\skills——
# 与 syncer.py --dest 默认、deploy_injection.py SKILL_SRC 派生同源；前缀由 -Prefix 参数控制，非目录差异）
$skillsMap = @{
    "claude"    = @{ dir = "$HOME\.claude\skills";      inject = "" }
    "codex"     = @{ dir = "$HOME\.codex\skills";       inject = "$HOME\.codex\AGENTS.md" }
    "workbuddy" = @{ dir = "$HOME\.workbuddy\skills";   inject = "$HOME\.workbuddy\AGENTS.md" }
    "agents"    = @{ dir = "$HOME\.agents\skills";      inject = "" }
    "cursor"    = @{ dir = "$HOME\.cursor\skills";      inject = "" }
    "trae"      = @{ dir = "$HOME\.trae\skills";        inject = "$HOME\.trae-cn\user_rules\shisan-xinuo-workflow.md" }
    "zcode"     = @{ dir = "$HOME\.agents\skills";      inject = "$HOME\.zcode\AGENTS.md" }
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

# ---------- 事务清单（v4.1.0 R2 · A-14/F-58：步骤状态 PASS/FAIL/NOT_RUN/PARTIAL+末尾 overall 判定） ----------
$script:tx = New-Object System.Collections.Generic.List[string]
function Add-TxStep { param($Step, $State, $Note = "") $script:tx.Add(("{0,-8} {1}  {2}" -f $State, $Step, $Note)) }
function Show-Tx {
    $overall = "PASS"
    foreach ($line in $script:tx) {
        if ($line -match "^\s*FAIL") { $overall = "FAIL" }
        elseif (($line -match "^\s*PARTIAL") -and ($overall -ne "FAIL")) { $overall = "PARTIAL" }
    }
    Write-Host "`n[事务] 安装步骤清单（A-14）："
    $script:tx | ForEach-Object { Write-Host "  $_" }
    Write-Host ("[事务] overall = {0}" -f $overall)
    if ($overall -eq "FAIL") { Write-Host "[事务] 失败步骤请对照上方输出处理；已完成步骤见清单（不做自动回滚——回滚动作本身也可能失败，F-58 轻量版裁决）" }
    return $overall
}

# ---------- 备份（已存在时，-Force 才覆盖；备份名含毫秒防同秒重装覆盖 F-63）----------
$backupRoot = Join-Path $skillsDir "skill-backups"
$backup = Join-Path $backupRoot ("{0}.bak-{1}" -f $targetName, (Get-Date -Format "yyyyMMdd-HHmmss-fff"))
if (Test-Path $dest) {
    if (-not $Force) {
        Write-Warning "目标已存在：$dest（如需覆盖请加 -Force；-Force 会先备份到 $backupRoot——平台扫描路径之外，符合 syncer 备份外置纪律）"
        Add-TxStep "安装" "FAIL" "目标已存在且未指定 -Force"
        Show-Tx
        exit 1
    }
    Write-Host "[注意] -Force 覆盖为合并语义：旧版独有文件可能残留在目标目录（Copy-Item 递归覆盖异名保留；不直接删除旧目录=防误删本地内容，F-60）"
    if ($Dry) { Write-Host "[干跑] 备份现有安装 → $backup" }
    else {
        $null = New-Item -ItemType Directory -Path $backupRoot -Force
        Copy-Item -Path $dest -Destination $backup -Recurse -Force
        Write-Host "[备份] $backup"
    }
}

# ---------- 复制 / 软链（-Link 降级复制后统一验收 F-62）----------
$installedVia = "复制"
if ($Dry) {
    $mode = if ($Link) { "软链" } else { "复制" }
    Write-Host "[干跑] $mode $Source`n        → $dest"
    Add-TxStep "安装" "DRY" "干跑未写盘"
} elseif ($Link) {
    try {
        $null = New-Item -ItemType SymbolicLink -Path $dest -Target $Source
        $installedVia = "软链"
        Write-Host "[链接] $dest  →  $Source"
    } catch {
        Write-Warning "软链创建失败（需管理员权限或开发者模式）：$($_.Exception.Message)；降级为复制。"
        Copy-Item -Path $Source -Destination $dest -Recurse -Force
        $installedVia = "复制（软链降级）"
        Write-Host "[复制] $dest"
    }
} else {
    Copy-Item -Path $Source -Destination $dest -Recurse -Force
    Write-Host "[复制] $dest"
}
if (-not $Dry) {
    # 统一验收（软链/复制同判据，F-62）：SKILL.md 必须在
    if (Test-Path (Join-Path $dest "SKILL.md")) {
        Add-TxStep "安装" "PASS" "$installedVia → $dest"
    } else {
        Add-TxStep "安装" "FAIL" "$installedVia 后缺 SKILL.md（验收不过）"
    }
}

# ---------- 硬注入（可选；v4.1.0 R2 · F-66 统一语义：改调 deploy_injection.py 同一区块合并实现） ----------
if ($HardInject) {
    $core = Join-Path $Source "references\injection-core.md"
    if (-not (Test-Path $core)) {
        # A-14 三态：请求了 -HardInject 但源缺核心文件 = FAIL（不再静默跳过——请求与结果必须一致，F-59）
        Write-Error "[注入] 指定了 -HardInject 但源缺少 references\injection-core.md → 注入层 FAIL（安装本体已完成，见事务清单）"
        Add-TxStep "注入" "FAIL" "源缺 injection-core.md（请求与结果不一致，F-59 修复）"
    } elseif (-not $injectFile) {
        # A-14 三态：指定 -HardInject 但平台无登记注入点 = PARTIAL（明确告知只完成部分）
        $pn = if ($Platform) { $Platform } else { "未指定" }
        Write-Warning "[注入] 平台 $pn 无标准注入点（本脚本未登记）→ 注入层 PARTIAL（Skill 安装本体已完成）"
        Add-TxStep "注入" "PARTIAL" "平台 $pn 无登记注入点，仅完成安装层"
    } elseif ($Dry) {
        $vjson = Get-Content -Raw -Encoding UTF8 (Join-Path $root "package.json") | ConvertFrom-Json
        Write-Host "[干跑] 调用 scripts\deploy_injection.py --only $Platform --version $($vjson.version)（区块合并+备份，统一语义 F-66）"
        Add-TxStep "注入" "DRY" "干跑未写盘"
    } else {
        $vjson = Get-Content -Raw -Encoding UTF8 (Join-Path $root "package.json") | ConvertFrom-Json
        $deployScript = Join-Path $root "scripts\deploy_injection.py"
        Write-Host "[注入] 统一语义入口：python deploy_injection.py --only $Platform --version $($vjson.version)（区块合并·用户内容保留·写后断言）"
        $py = if (Get-Command python -ErrorAction SilentlyContinue) { "python" } else { "py" }
        try {
            & $py $deployScript --only $Platform --version $vjson.version --hash
            if ($LASTEXITCODE -ne 0) {
                Add-TxStep "注入" "FAIL" "deploy_injection exit=$LASTEXITCODE（详见上方逐项输出）"
            } else {
                Add-TxStep "注入" "PASS" "deploy_injection 区块合并完成+hash 验收过"
            }
        } catch {
            Add-TxStep "注入" "FAIL" "无法调用 python（$($_.Exception.Message)）；注入层未写"
        }
    }
} elseif ($MemoryFile) {
    # A-14 预检：-MemoryFile 未与 -HardInject 同用=只装 Skill，明确告知记忆层未写（防误以为已三层）
    Write-Warning "[预检] 指定了 -MemoryFile 但未指定 -HardInject → 本次只装 Skill（记忆层/规则层均未写入，F-62 家族防误解）"
    Add-TxStep "注入" "PARTIAL" "请求了 -MemoryFile 但未请求 -HardInject（三层未写；安装本体已完成）"
} else {
    Add-TxStep "注入" "NOT_RUN" "未请求 -HardInject（只装 Skill=合法 PASS 态，A-14 三态）"
}

# ---------- 记忆层（硬注入第三层；-HardInject -MemoryFile 时）----------
if ($MemoryFile -and $HardInject) {
        # readme 说明：硬注入 = 记忆层 + 规则层 + 配置文件层三层（SKILL.md §3 / platform-adaptation §2.2）
        $anchor = Join-Path $Source "templates\memory-anchor.md"
        if (-not (Test-Path $anchor)) {
            Write-Warning "[记忆] 源缺少 templates\memory-anchor.md，跳过记忆层（安装/规则层已完成）。"
        } else {
            $ts = Get-Date -Format "yyyyMMdd-HHmmss"
            if ($Dry) {
                Write-Host "[干跑] 备份记忆文件 → $MemoryFile.bak-$ts ；写入 memory-anchor 锚点块至 $MemoryFile（在场提示首行）"
            } else {
                $anchorText = Get-Content -Raw -Encoding UTF8 $anchor
                # 提取模板中代码块内的锚点（首行为在场提示）；避免把模板说明注释写进记忆文件
                $m = [regex]::Match($anchorText, '(?s)```markdown\r?\n(.*?)\r?\n```')
                if ($m.Success) { $anchorBody = $m.Groups[1].Value } else { $anchorBody = $anchorText }
                # 版本占位替换（对齐 syncer：模板 vX.Y.Z → 源 SKILL.md frontmatter 版本，防占位符落盘）
                $skFront = Get-Content -Raw -Encoding UTF8 (Join-Path $Source "SKILL.md")
                $vm = [regex]::Match($skFront, '(?m)^\s*version:\s*([0-9]+\.[0-9]+\.[0-9]+)')
                if ($vm.Success) { $anchorBody = $anchorBody.Replace("vX.Y.Z", "v$($vm.Groups[1].Value)") }
                else { Write-Warning "[记忆] SKILL.md 未解析到版本号，锚点保留 vX.Y.Z 占位" }
                $prev = ""
                $cleanedVersions = @()
                if (Test-Path $MemoryFile) {
                    Copy-Item -Path $MemoryFile -Destination "$MemoryFile.bak-$ts" -Force
                    $prev = Get-Content -Raw -Encoding UTF8 $MemoryFile
                    Write-Host "[记忆] 备份既有记忆文件 → $MemoryFile.bak-$ts"
                    # 旧锚清扫（F-26 单实现）：判据单源=scripts\anchor_sweep.py（syncer.py 同调此实现，禁再手抄第二份）；
                    # 跨 shell 走文件介质（#401：中文正文禁管道/stdin 传递）
                    $anchorScript = Join-Path $root "scripts\anchor_sweep.py"
                    $tmpIn = Join-Path $env:TEMP "anchor-prev-$ts.md"
                    $tmpOut = Join-Path $env:TEMP "anchor-clean-$ts.md"
                    $tmpJson = Join-Path $env:TEMP "anchor-stats-$ts.json"
                    [System.IO.File]::WriteAllText($tmpIn, $prev)
                    python $anchorScript --sweep $tmpIn --out $tmpOut --json $tmpJson
                    if ($LASTEXITCODE -ne 0) { Write-Error "anchor_sweep 清扫失败（exit=$LASTEXITCODE）"; exit 1 }
                    $prev = [System.IO.File]::ReadAllText($tmpOut)
                    $swStats = [System.IO.File]::ReadAllText($tmpJson) | ConvertFrom-Json
                    $cleanedVersions = @($swStats.versions)
                    if ($swStats.removed -gt 0) {
                        Write-Host "[记忆清扫留痕] 本块将删除 $($swStats.removed) 行（预览前 5 行，完整内容见备份）："
                        $swStats.preview | ForEach-Object { Write-Host "  - $_" }
                    }
                    Remove-Item $tmpIn, $tmpOut, $tmpJson -ErrorAction SilentlyContinue
                }
                $sep = if ($prev.Trim().Length -gt 0) { "`n`n---`n" } else { "" }
                Set-Content -Path $MemoryFile -Value ($prev.TrimEnd() + $sep + $anchorBody) -Encoding UTF8
                $cleanTag = if ($cleanedVersions.Count -gt 0) { "；旧锚清扫 $($cleanedVersions.Count) 块[$($cleanedVersions -join ',')]" } else { "" }
                Write-Host "[记忆] $(if ($prev.Trim().Length -gt 0) { '合并（既有内容保留在上方）' } else { '新建' }) → $MemoryFile$cleanTag"
                Write-Host "[记忆] 在场提示已写入首行 —— 新会话读到即识别「工作流 Skill 现已在场」"
                Add-TxStep "记忆" "PASS" "$MemoryFile$cleanTag"
            }
        }
        if (-not (Test-Path (Join-Path $Source "templates\memory-anchor.md"))) { Add-TxStep "记忆" "FAIL" "源缺 memory-anchor.md" }
}

# ---------- 验收 ----------
Write-Host ""
Write-Host "[完成] 安装目录：$dest（安装方式=$installedVia）"
Write-Host "[验收] 平台加载时的 Base directory 应指向：$dest（不是文件版本号；若平台扫描到 skill-backups\ 目录，请确认其位于扫描路径之外）"
if ($MemoryFile -and $HardInject) { Write-Host "[三层] 硬注入三层状态：记忆层=$($MemoryFile) ｜ 规则层=$(if ($injectFile) { $injectFile } else { 'deploy_injection 按平台表' }) ｜ 配置文件层=$(if ($injectCfgFile) { $injectCfgFile } else { '无（平台不支持/未指定）' })" }
Write-Host "[提示] 安装名已带 $Prefix 前缀 → SKILL.md §3 第 0 步安装名前缀自检将静默通过；无前缀安装会收到一行适配提示。"
if (-not $Family) {
    $null = Show-Tx   # 事务清单+overall（A-14）；-Family 由子进程各自输出
}
exit 0
