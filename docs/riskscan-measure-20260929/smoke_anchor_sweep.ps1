# install-skill.ps1 F-26 块冒烟（harness：变量桩定，逐字复刻替换块，fixture 带旧锚）
$ErrorActionPreference = 'Stop'
$root = Split-Path -Parent (Split-Path -Parent $PSScriptRoot)   # harness 位于 docs/x/ 下（比安装器深一层）：仓库根
$ts = '20260929-060000'
$MemoryFile = Join-Path $env:TEMP "mem-smoke-$ts.md"
[System.IO.File]::WriteAllText($MemoryFile, "# 记忆`n`n## 在场提示 · 工作流 Skill 现已在场（v3.2.0 硬注入）`n旧锚内容`n`n## 用户偏好`n内容")

$prev = [System.IO.File]::ReadAllText($MemoryFile)
$cleanedVersions = @()

# ---- 以下逐字 = install-skill.ps1 替换块 ----
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
# ---- 替换块结束 ----

$ok = ($prev -notmatch '在场提示') -and ($prev -match '用户偏好') -and ($cleanedVersions[0] -eq 'v3.2.0')
Write-Host ("SMOKE-PS: {0} ｜ cleanedVersions={1}" -f $(if ($ok) { 'PASS' } else { 'FAIL' }), ($cleanedVersions -join ','))
Write-Host "--- cleaned ---"; Write-Host $prev
Remove-Item $MemoryFile -ErrorAction SilentlyContinue
exit $(if ($ok) { 0 } else { 1 })
