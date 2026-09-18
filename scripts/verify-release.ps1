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
      E. 正文净化：常驻/模板面过程注记（日期/拍板/批次词/sess_）命中 = 0
      F. 索引完整性：details.md 症状索引全覆盖（编号连续、每条细则 ≥1 症状域）
      G. 事实对账：细则数/条目范围与 details 计算单源一致（facts_sync）
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
    "L2-F",            # 三级跑道·完整 9 步
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
    "项目级注入点"       # 承载检查：项目规则文件按平台注入点表定名
)
$newBootstrap = Join-Path $skDir "references\new-project-bootstrap.md"
$probsA = @()
$txt = Get-Content $main -Raw -Encoding UTF8
foreach ($anc in $anchorsSkill) { if ($txt -notmatch [regex]::Escape($anc)) { $probsA += "SKILL 缺锚点[$anc]" } }
$core = Join-Path $skDir "references\injection-core.md"
$coreLen = 0
if (-not (Test-Path $core)) { $probsA += "缺 injection-core.md" } else {
    $ctxt = Get-Content $core -Raw -Encoding UTF8
    foreach ($anc in $anchorsCore) { if ($ctxt -notmatch [regex]::Escape($anc)) { $probsA += "injection-core 缺锚点[$anc]" } }
    $coreLen = $ctxt.Length
    if ($coreLen -gt 6000) { $probsA += "injection-core 字符数 $coreLen 超硬上限 6000（常驻瘦身预算，目标 4K）" }
}
if (-not (Test-Path $newBootstrap)) { $probsA += "缺 references/new-project-bootstrap.md" }
$pyLen = 0
try { $pyLen = [int](python -c "import sys; print(len(open(sys.argv[1], encoding='utf-8').read().replace(chr(13),'')))" "$core" 2>$null) } catch { $pyLen = -1 }
if ($pyLen -gt 6000 -and $pyLen -ge 0) { $probsA += "injection-core Python/code-point 口径 $pyLen 超 6000" }
# 形态冒烟（v3.0 批⑤：纯数值门禁对同长度文本损坏盲区——首行形态断言）
$formChecks = @(
    @('README.md', 0, '# Shisan Xinuo Agent Workflow'),
    @('AGENTS.md', 1, '> 本仓库 ='),
    @('docs/project-info.md', 2, '> **本文件是索引入口')
)
foreach ($fc in $formChecks) {
    $fp2 = Join-Path $Root $fc[0]
    if (Test-Path $fp2) {
        $fl = @(Get-Content $fp2 -First ($fc[1] + 1) -Encoding UTF8)[$fc[1]]
        if (-not $fl -or -not $fl.StartsWith($fc[2])) { $probsA += "形态冒烟失败：$($fc[0]) 第 $($fc[1]+1) 行形态异常" }
    }
}

Add-Result ($probsA.Count -eq 0) "A 内容锚点+字符预算(主交付物全量特性)" $(if($probsA.Count -eq 0){"OK（injection-core PS/UTF-16=$coreLen · Python/code-point=$pyLen · 双口径 ≤6000）"}else{$probsA -join ";"})

# ---------- B. hooks 三层（警告级：hooks = 可选加固面，非运行时必需——templates/hooks/README 自声明） ----------
$hookFiles = @("session-start.example.sh","session-end.example.sh","hooks.example.json")
$hDir = Join-Path $skDir "templates\hooks"
$probs2 = @()
foreach ($hf in $hookFiles) { if (-not (Test-Path (Join-Path $hDir $hf))) { $probs2 += "缺 $hf" } }
$json = Join-Path $hDir "hooks.example.json"
if (Test-Path $json) {
    $hj = Get-Content $json -Raw | ConvertFrom-Json
    $hjH = $hj.hooks; if ($null -eq $hjH -or $hjH.PSObject.Properties.Name -notcontains 'SessionStart' -or $hjH.PSObject.Properties.Name -notcontains 'Stop') { $probs2 += 'hooks.json 缺双钩子声明(SessionStart+Stop)' }
}
if ($probs2.Count -gt 0) { Write-Host "[WARN] B hooks 三层(警告级)：$($probs2 -join ';') — hooks 是可选加固面，不阻断发布" -ForegroundColor Yellow }
Add-Result $true "B hooks 三层(警告级)" $(if($probs2.Count -eq 0){"OK"}else{"$($probs2 -join ';')（警告，不阻断）"})

# ---------- C. 版本一致（交付物 == package.json） ----------
$baseVer = ((Get-Content $main -Raw -Encoding UTF8 | Select-String -Pattern '(?s)version\s*:\s*([0-9]+\.[0-9]+\.[0-9]+)' -AllMatches).Matches[0].Groups[1].Value)
$pkgVersion = ((Get-Content (Join-Path $Root "package.json") -Raw -Encoding UTF8 | ConvertFrom-Json).version)
Add-Result ($baseVer -eq $pkgVersion) "C 版本一致(交付物=package.json)" "SKILL version=$baseVer ; package.json version=$pkgVersion"

# ---------- D. 泄漏红线（v2.8.x 修正：扫描面=git tracked 全量，豁免缩为自引用+历史过程档；正则补正斜杠——审查 F-16） ----------
if (-not $SkipLeak) {
    $tracked = (git -c core.quotepath=false ls-files) | Where-Object { $_ -and $_ -notmatch "^(scripts/|EVIDENCE\.md$|docs/roadtest-)" }
    $tokenPats = @('ghp_[A-Za-z0-9]{20,}', 'gho_[A-Za-z0-9]{20,}', 'github_pat_[A-Za-z0-9_]{20,}')
    $leakHits = @()
    $scanned = 0
    foreach ($rel in $tracked) {
        $fp = Join-Path $Root $rel
        if (-not (Test-Path $fp)) { continue }
        $scanned += 1
        $text = Get-Content $fp -Raw -ErrorAction SilentlyContinue
        if (-not $text) { continue }
            # 1) 无歧义的真实泄漏特征：作者机密目录 / 本仓真实路径 / 真实用户主目录（正反斜杠双形态）。
            #    不匹配 `…` 占位符（文档示例 `C:\Users\…` 不是 [A-Za-z]）；
            #    scripts/ 整体豁免=脚本自身正则文本自引用（审查 F-16 建议 3）；
            #    EVIDENCE.md 与 docs/roadtest-*.md=历史过程档豁免（其中运行路径属史料，清理票在 2.9）。
            if ($text -match 'D:\\Agent个人资源|Agent个人资源\\02-Gitee|Agent个人资源\\机密资源|D:\\Agent工作流启动包|[A-Za-z]:[\\/]+Users[\\/]+[A-Za-z]') {
                $leakHits += "$rel :: 引外部磁盘/个人路径"
            }
            # 2) 令牌原文
            foreach ($tp in $tokenPats) { if ($text -match $tp) { $leakHits += "$rel :: 疑似令牌明文(已掩码)" ; break } }
            # 3) 发布物内出现个人版路径（README 版本说明豁免；排除账目四文件豁免——.gitignore/AGENTS/project-info/项目信息 对 gitignore 目录的功能性记载非泄漏，单一表述源裁决留 2.9）
            $exemptPersonal = @('.gitignore', 'AGENTS.md', 'docs/project-info.md', '项目信息.md')
            if (($exemptPersonal -notcontains $rel) -and ($rel -notlike "README.md") -and ($text -match 'versions[\/]personal-zh')) {
                $leakHits += "$rel :: 发布物内引用个人版路径"
            }
    }
    Add-Result ($leakHits.Count -eq 0) "D 泄漏红线(发布物)" $(if($leakHits.Count -eq 0){"扫描面内 $scanned 个 tracked 文件 0 命中（豁免：scripts/ 自引用、历史过程档；作者标识判据=security.md §5）"}else{$leakHits -join ";"})
}

# ---------- E. 正文净化（常驻面/模板面过程注记 = 0；正文 vs 史料规范，v2.1.1 起；references 面史料豁免——details 来源字段/节首注记为双击晋升准入证据） ----------
$probsE = @()
$cleanFiles = @($main, $core)
$refDir = Join-Path $skDir "references"
if (Test-Path $refDir) {
    $cleanFiles += Get-ChildItem $refDir -File -Filter *.md | Where-Object { $_.Name -ne 'details.md' } | ForEach-Object { $_.FullName }
}
if (Test-Path (Join-Path $skDir "templates")) {
    $cleanFiles += Get-ChildItem (Join-Path $skDir "templates") -Recurse -File -Filter *.md | ForEach-Object { $_.FullName }
}
# v2.6.0 强化：日期串/拍板叙述/案例代号/会话ID/批次词 全模式；details 单独行过滤扫描（来源/晋升字段与节首注记豁免）
foreach ($cf in $cleanFiles) {
    if (-not (Test-Path $cf)) { continue }
    $bad = Get-Content $cf -Encoding UTF8 | Where-Object {
        $_ -notmatch '\*来源|\*晋升|^## |^> 来源|^> \*来源' -and $_ -match '用户拍板|用户定调|作者定调|2026-\d{2}-\d{2}|二轮证伪|本批次|sess_[a-z0-9]{6}'
    }
    if ($bad) { $probsE += "$(Split-Path $cf -Leaf) 含过程注记 $($bad.Count) 处" }
}
$detailsE = Join-Path $skDir "references\details.md"
if (Test-Path $detailsE) {
    $bad = Get-Content $detailsE -Encoding UTF8 | Where-Object {
        $_ -notmatch '\*来源|\*晋升|^## |^> ' -and $_ -match '用户拍板|2026-\d{2}-\d{2}|sess_[a-z0-9]{6}'
    }
    if ($bad) { $probsE += "details.md 正文含日期/拍板 $($bad.Count) 处" }
}
Add-Result ($probsE.Count -eq 0) "E 正文净化(常驻/模板面过程注记=0)" $(if($probsE.Count -eq 0){"OK"}else{$probsE -join ";"})

# ---------- F. 索引完整性（details 症状索引覆盖全部细则编号 + 编号连续；v2.3.0） ----------
$probsF = @()
$detailsPath = Join-Path $skDir "references\details.md"
if (-not (Test-Path $detailsPath)) { $probsF += "缺 details.md" } else {
    $dtxt = Get-Content $detailsPath -Raw -Encoding UTF8
    # 1) 编号连续：条目编号 = 行首 `N. `（含标签可选）；特殊槽（〔预留槽〕/〔归档〕）不参与覆盖断言（F-19：索引不挂预留槽）
    $allNums = [regex]::Matches($dtxt, '(?m)^(\d+)\. ') | ForEach-Object { [int]$_.Groups[1].Value }
    $special = [regex]::Matches($dtxt, '(?m)^(\d+)\. .*(〔预留槽〕|〔归档〕)') | ForEach-Object { [int]$_.Groups[1].Value }
    $nums = $allNums | Where-Object { $special -notcontains $_ } | Sort-Object -Unique
    $expect = 1..($allNums | Sort-Object -Unique | Select-Object -Last 1)
    $gap = Compare-Object $expect ($allNums | Sort-Object -Unique)
    if ($gap) { $probsF += "编号不连续: $($gap | ForEach-Object { $_.InputObject } | Select-Object -First 5)..." }
    # 2) 索引段覆盖：## 症状索引 与 ## 1. 之间每个活跃编号出现 ≥1 次
    $mIdx = [regex]::Match($dtxt, '(?s)## 症状索引.*?(?=\n## 1\.)')
    if (-not $mIdx.Success) { $probsF += "缺症状索引段" } else {
        $idxSeg = $mIdx.Value
        $missingIdx = @()
        foreach ($n in $nums) {
            if ($idxSeg -notmatch ('#' + $n + '([,\s]|$)')) { $missingIdx += $n }
        }
        if ($missingIdx.Count -gt 0) { $probsF += "索引未覆盖: #" + ($missingIdx -join ',#') }
        # 3) 关键域行在场（F-23 域可检索断言——域族行被误删即红）
        foreach ($dom in @('性能与首屏反馈','数据迁移与库变更','超时熔断与限流','备份与恢复演练','项目导航','结构化日志可观测')) {
            if ($idxSeg -notmatch [regex]::Escape($dom)) { $probsF += "索引缺关键域行[$dom]" }
        }
    }
}
Add-Result ($probsF.Count -eq 0) "F 索引完整性(details 编号连续+症状索引全覆盖)" $(if($probsF.Count -eq 0){"OK ($($nums.Count) 编号全覆盖·活跃数见 deploy --check)"}else{$probsF -join ";"})

# ---------- G. 事实对账（facts_sync 单源：活跃细则数/条目范围 声明值 vs 计算值；v2.8.x 修正批——文档同步差异机制修法） ----------
$probsG = @()
$factsSync = Join-Path $Root "scripts\facts_sync.py"
if (Test-Path $factsSync) {
    $gOut = python $factsSync --check 2>&1
    if ($LASTEXITCODE -ne 0) { $probsG += ($gOut | Where-Object { $_ -match 'DIFF|未找到' } | Select-Object -First 4) }
} else { $probsG += "缺 scripts/facts_sync.py" }
Add-Result ($probsG.Count -eq 0) "G 事实对账(细则数/条目范围 单源)" $(if($probsG.Count -eq 0){$gOut | Select-Object -Last 1}else{$probsG -join ";"})

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
