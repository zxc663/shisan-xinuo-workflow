$ErrorActionPreference = "Stop"
$root = Split-Path -Parent $PSScriptRoot
$ts = Get-Date -Format "yyyyMMdd-HHmmss"
$src = Join-Path $root "dist"
$staging = Join-Path $env:TEMP ("xinuo-dist-staging-" + $ts)
$ver = (Get-Content (Join-Path $root "package.json") -Raw | ConvertFrom-Json).version
Write-Host "版本 = $ver"

# 1) 根系发布文件
$rootFiles = @("CHANGELOG.md","EVIDENCE.md","LICENSE","package.json","README.md","RELEASE-CHECKLIST.md")

# 2) 待复制清单（相对 root，正斜杠）
$roots = @("CHANGELOG.md","EVIDENCE.md","LICENSE","package.json","README.md","RELEASE-CHECKLIST.md")
$scripts = Get-ChildItem (Join-Path $root "scripts") -File | ForEach-Object { "scripts/" + $_.Name }
$docs    = Get-ChildItem (Join-Path $root "docs") -File | Where-Object { $_.Name -match 'reference-sources' } | ForEach-Object { "docs/" + $_.Name }
$skill   = Get-ChildItem (Join-Path $root "skill") -Recurse -File -ErrorAction SilentlyContinue | Where-Object { $_.FullName -notmatch '\\.git' } | ForEach-Object { ($_.FullName.Substring($root.Length + 1)).Replace('\','/') }
$all = ($roots + $scripts + $docs + $skill) | Sort-Object -Unique

Write-Host "待复制: $($all.Count) 项"

# 3) 复制进 staging（保留相对结构）
New-Item -ItemType Directory -Path $staging -Force | Out-Null
foreach ($rel in $all) {
    $s = Join-Path $root ($rel.Replace('/','\'))
    $d = Join-Path $staging ($rel.Replace('/','\'))
    if (-not (Test-Path $s)) { Write-Error "缺失源: $s" }
    $null = New-Item -ItemType Directory -Path (Split-Path $d -Parent) -Force
    Copy-Item $s $d -Force
}
Write-Host "暂存完成: $staging"

# 4) 双检清单（staging 与 期望清单，正斜杠归一后 Set 相等）
$stageList = Get-ChildItem $staging -Recurse -File | ForEach-Object { ($_.FullName.Substring($staging.Length + 1)).Replace('\','/') } | Sort-Object
$expectList = ($all | Sort-Object)
$diff1 = @($expectList | Where-Object { $_ -notin $stageList })
$diff2 = @($stageList | Where-Object { $_ -notin $expectList })
if ($diff1.Count -ne 0 -or $diff2.Count -ne 0) {
    Write-Error "Set-diff 不符: expect 多余=$(($diff1 -join ';')) stage 多余=$(($diff2 -join ';'))"
}
Write-Host "Set-diff 双检: $($stageList.Count)=$($expectList.Count) 一致"

# 5) 压缩
$zip = Join-Path $src ("shisan-xinuo-workflow-v" + $ver + ".zip")
if (Test-Path $zip) { Remove-Item $zip -Force }
Compress-Archive -Path (Join-Path $staging "*") -DestinationPath $zip
Remove-Item $staging -Recurse -Force
Write-Host "zip: $zip  size=$((Get-Item $zip).Length)  entries=$($stageList.Count)"
Write-Host "DONE"