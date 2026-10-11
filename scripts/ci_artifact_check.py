# -*- coding: utf-8 -*-
"""交付物验证（A-12⑦/A-13②/F-54）：zip 面断言→解压检查→源库哈希对照→版本一致。
CI（artifact-check job）与本机两用；检查对象=真交付物，非源库面。
用法：python scripts/ci_artifact_check.py [--zip <zip 路径>]（默认 dist/shisan-xinuo-workflow-v<ver>.zip）
退出码：0=全过；1=任一断言失败；2=前置缺失（zip 不存在）。
断言面：必要文件在场 / 零 .mimosa（2026-10-11 污染修复回归锚） / 源库↔zip 逐文件 SHA256 /
版本三面一致（package.json = SKILL frontmatter = zip 文件名）。
"""
import argparse, hashlib, json, re, sys, zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

REQUIRED = [
    "skill/shisan-xinuo-workflow/SKILL.md",
    "skill/shisan-xinuo-workflow/references/injection-core.md",
    "skill/shisan-xinuo-workflow/references/details.md",
    "skill/shisan-xinuo-flows/SKILL.md",
    "skill/shisan-xinuo-roles/SKILL.md",
    "skill/shisan-xinuo-product/SKILL.md",
    "skill/shisan-xinuo-product/scripts/spec-trace-gate.py",
    "skill/shisan-xinuo-single/SKILL.md",
    "scripts/gate_audit.py",
    "scripts/risk_scan.py",
    "scripts/deploy_injection.py",
    "scripts/syncer.py",
    "scripts/verify-release.ps1",
    "scripts/install-skill.ps1",
    "README.md",
    "LICENSE",
    "package.json",
]


def sha(b):
    return hashlib.sha256(b).hexdigest()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--zip", default="", help="zip 路径（默认按 package.json 版本拼 dist 名）")
    a = ap.parse_args()
    ver = json.loads((ROOT / "package.json").read_text(encoding="utf-8"))["version"]
    want_name = f"shisan-xinuo-workflow-v{ver}.zip"
    zp = Path(a.zip) if a.zip else ROOT / "dist" / want_name
    if not zp.exists():
        print(f"E: zip 不存在: {zp}（先跑 pwsh scripts/build-dist.ps1）")
        return 2
    probs = []
    z = zipfile.ZipFile(str(zp))
    names = [n for n in z.namelist() if not n.endswith("/")]
    nameset = set(names)

    if zp.name != want_name:
        probs.append(f"zip 文件名版本不一致: {zp.name} vs package.json {ver}")

    missing = [r for r in REQUIRED if r not in nameset]
    if missing:
        probs.append(f"zip 缺必要文件 {len(missing)} 项: {missing[:6]}")

    mim = [n for n in names if ".mimosa" in n]
    if mim:
        probs.append(f"zip 含 .mimosa 本地数据 {len(mim)} 项（发行物净化红线，2026-10-11 修复回归锚）: {mim[:3]}")

    mismatch, compared = [], 0
    for n in sorted(names):
        src = ROOT / n
        if not src.is_file():
            continue
        compared += 1
        if sha(z.read(n)) != sha(src.read_bytes()):
            mismatch.append(n)
    if mismatch:
        probs.append(f"源库↔zip 哈希不一致 {len(mismatch)} 项: {mismatch[:5]}")

    sk = z.read("skill/shisan-xinuo-workflow/SKILL.md").decode("utf-8")
    m = re.search(r"(?m)^\s*version:\s*([0-9]+\.[0-9]+\.[0-9]+)", sk)
    if not m:
        probs.append("zip 内 SKILL.md 无 frontmatter 版本行")
    elif m.group(1) != ver:
        probs.append(f"SKILL frontmatter 版本 {m.group(1)} ≠ package.json {ver}")

    print(f"compared={compared} mismatch={len(mismatch)} mimosa={len(mim)} zip={zp.name}")
    if probs:
        print("ARTIFACT-CHECK FAIL:")
        for p in probs:
            print(" -", p)
        return 1
    print(f"ARTIFACT-CHECK PASS: ver={ver} compared={compared}（源库↔zip 逐文件 SHA256 一致）")
    return 0


if __name__ == "__main__":
    sys.exit(main())
