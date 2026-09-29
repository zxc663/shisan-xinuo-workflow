# sync-all.ps1 · 收尾一键三连（G6/T10，2026-09-29）
# 把手动三步包成一个 fail-fast 序列（gap-list G6 副本同步靠人肉）：
#   1. syncer --family      技能副本同步（家族全包：核心+flows+roles+product）
#   2. deploy_injection     五平台注入重部署
#   3. deploy_injection --check --hash   注入验收（细则 #374 哈希面）
# 用法：
#   powershell -File scripts/sync-all.ps1          # 真跑三连
#   powershell -File scripts/sync-all.ps1 -Dry     # syncer --dry + 只跑 --check
# 诚实边界：不覆盖 WorkBuddy --dest 特例（需要时手动 syncer --dest）；发行面仍走 RELEASE-CHECKLIST。
param([switch]$Dry)
$ErrorActionPreference = "Stop"
$root = Split-Path -Parent $PSScriptRoot

function Step($name, $exe, $argList) {
    Write-Host "== $name =="
    & $exe @argList
    if ($LASTEXITCODE -ne 0) {
        Write-Host "SYNC_ALL FAIL @ $name（exit $LASTEXITCODE）——fail-fast 停止"
        exit $LASTEXITCODE
    }
}

if ($Dry) {
    Step "1/2 syncer --family --dry" python @("$root\scripts\syncer.py", "--family", "--dry")
    Step "2/2 deploy --check --hash（dry 跳过重部署）" python @("$root\scripts\deploy_injection.py", "--check", "--hash")
    Write-Host "SYNC_ALL DRY-PASS"
} else {
    $ver = (Get-Content -Raw "$root\package.json" | ConvertFrom-Json).version
    if (-not $ver) { Write-Host "SYNC_ALL FAIL @ 读版本（package.json 无 version）"; exit 1 }
    Step "1/3 syncer --family" python @("$root\scripts\syncer.py", "--family")
    Step "2/3 deploy_injection" python @("$root\scripts\deploy_injection.py", "--version", $ver)
    Step "3/3 deploy --check --hash" python @("$root\scripts\deploy_injection.py", "--check", "--hash")
    Write-Host "SYNC_ALL PASS：3 步全绿（version=$ver）"
}
