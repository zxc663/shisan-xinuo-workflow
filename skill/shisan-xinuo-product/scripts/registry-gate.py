#!/usr/bin/env python3
"""registry-gate · 门禁④：组件归因检查（检查「查没查、归因没归因」，不定义组件）。

规则：组件目录下的组件文件必须携带 registry 归因标记——
  `registry: <名> source=<上游库@版本>` 或 `registry: <名> 自研归因=<为什么上游无解>`
缺失 → 列出文件 → 退出码 1（补归因后重跑）。

基线模式（存量项目接入）：首跑 `--write-baseline` 记录当时文件清单（存量豁免）；
此后每次对比基线，只拦「基线外新增且无标记」的文件——新组件必须归因，存量不追溯。
用法：python registry-gate.py --path <组件目录> [--include components] [--write-baseline] [--baseline <file>]
      python registry-gate.py --selftest
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

MARK = "registry:"
DEFAULT_BASELINE = ".registry-baseline.json"


def component_files(path: Path, scope: str, exts: list[str]) -> list[Path]:
    out: list[Path] = []
    for f in sorted(path.rglob("*")):
        if f.suffix not in exts or not f.is_file():
            continue
        if scope == "components" and "component" not in str(f).lower():
            continue
        out.append(f)
    return out


def scan(path: Path, scope: str, exts: list[str], baseline: Path | None, write_baseline: bool) -> tuple[list[str], str]:
    files = component_files(path, scope, exts)
    all_rel = [str(f.relative_to(path)) for f in files]
    if write_baseline:
        baseline.write_text(json.dumps({"files": all_rel}, ensure_ascii=False, indent=1), encoding="utf-8")
        return [], f"基线已写入 {baseline}（{len(all_rel)} 个存量文件豁免）"
    known: set[str] = set()
    if baseline and baseline.exists():
        known = set(json.loads(baseline.read_text(encoding="utf-8")).get("files", []))
    missing = [rel for rel, f in zip(all_rel, files) if rel not in known and MARK not in f.read_text(encoding="utf-8", errors="ignore")]
    return missing, f"检查 {len(all_rel)} 个组件文件（基线豁免 {len(known)} 个）"


def selftest() -> int:
    import tempfile
    with tempfile.TemporaryDirectory() as d:
        root = Path(d)
        comp = root / "src" / "components"
        comp.mkdir(parents=True)
        (comp / "Old.vue").write_text("<template/>", encoding="utf-8")
        bl = root / DEFAULT_BASELINE
        # 1) 基线写入：存量 Old.vue 豁免
        missing, msg = scan(comp, "components", [".vue"], bl, write_baseline=True)
        ok1 = missing == [] and "1 个存量" in msg
        # 2) 新增无标记组件 → 拦
        (comp / "New.vue").write_text("export default () => <div/>", encoding="utf-8")
        missing, _ = scan(comp, "components", [".vue"], bl, write_baseline=False)
        ok2 = missing == ["New.vue"]
        # 3) 新增带标记 → 放行
        (comp / "New.vue").write_text("// registry: New 自研归因=上游无解\nexport default () => <div/>", encoding="utf-8")
        missing, _ = scan(comp, "components", [".vue"], bl, write_baseline=False)
        ok3 = missing == []
        print(f"selftest: 基线存量豁免={ok1} 新增无标记被拦={ok2} 新增带标记放行={ok3}")
        return 0 if ok1 and ok2 and ok3 else 1


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--path", default="src")
    ap.add_argument("--ext", default=",".join([".vue", ".tsx", ".jsx"]))
    ap.add_argument("--scope", choices=["components", "all"], default="components",
                    help="components=仅组件目录（默认）；all=全部匹配文件")
    ap.add_argument("--baseline", default=None)
    ap.add_argument("--write-baseline", action="store_true")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        return selftest()
    path = Path(a.path)
    if not path.exists():
        print(f"FAIL: 路径不存在 {path}")
        return 1
    baseline = Path(a.baseline) if a.baseline else path / DEFAULT_BASELINE
    missing, msg = scan(path, a.scope, [e.strip() for e in a.ext.split(",")], baseline, a.write_baseline)
    print(msg)
    if missing:
        print(f"FAIL: {len(missing)} 个新增组件缺 registry 归因标记（{MARK} source=…/自研归因=…）：")
        for m in missing:
            print("  ✗", m)
        return 1
    print("OK: 归因检查通过")
    return 0


if __name__ == "__main__":
    sys.exit(main())
