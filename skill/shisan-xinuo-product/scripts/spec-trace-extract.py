#!/usr/bin/env python3
"""spec-trace-extract v1 · 绑定清单辅助提取器（队列⑤，2026-09-24）。

用途：spec-trace-gate 的 --components/--backends 两份清单文件 historically 手工维护，
真实仓库上不可持续（HANDOVER 队列⑤）。本器从代码库自动提取两份清单：
  --components ← 扫描组件目录（.vue/.tsx/.jsx/.ts/.js，排除测试/故事/配置）
  --backends   ← 识别三类后端端点声明：
                  ① FastAPI/Flask 装饰器：@router.get("/x") / @app.post("/y")
                  ② Next.js App Router API：src/app/**/route.ts 路径→ /api/… 端点
                  ③ 通用行内声明：`GET /path` 形态字面量（service 层常见）
产物：两份「每行一个」清单文件，直接喂 spec-trace-gate（整串比对语义，见 F2 修复）。
边界：只提取「存在什么」，不做绑定（feature↔component 映射=跑道产物，人/会话 judgments）。

用法：
  python spec-trace-extract.py --src <组件目录> --api <后端目录或文件>… \
      --out-components comps.txt --out-backends backs.txt [--ext .vue,.tsx] [--selftest]
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

COMPONENT_EXTS = [".vue", ".tsx", ".jsx"]
COMPONENT_EXCLUDE = re.compile(r"(test|spec|story|stories|\.d\.ts|node_modules|\.next|dist|build)")
DECORATOR = re.compile(r"@(?:router|app|api|blueprint|bp)\.(get|post|put|delete|patch)\(\s*[\"']([^\"']+)[\"']", re.I)
INLINE_ENDPOINT = re.compile(r"[\"']((?:GET|POST|PUT|DELETE|PATCH)\s+/[^\"']+)[\"']", re.I)
PY_FILE = re.compile(r"\.(py)$")
API_ROUTE_FILE = re.compile(r"route\.(ts|js)$")


def extract_components(src: Path, exts: list[str]) -> list[str]:
    out: list[str] = []
    if not src.exists():
        return out
    for p in sorted(src.rglob("*")):
        if not p.is_file() or p.suffix not in exts:
            continue
        if COMPONENT_EXCLUDE.search(str(p)):
            continue
        out.append(p.stem)
    return sorted(set(out))


def _extract_decorators(text: str) -> list[str]:
    return [f"{m.group(1).upper()} {m.group(2)}" for m in DECORATOR.finditer(text)]


def _extract_inline(text: str) -> list[str]:
    return [m.group(1).upper().replace("  ", " ") for m in INLINE_ENDPOINT.finditer(text)]


def _extract_next_routes(root: Path) -> list[str]:
    out: list[str] = []
    for p in sorted(root.rglob("*")):
        if p.is_file() and API_ROUTE_FILE.search(p.name) and not COMPONENT_EXCLUDE.search(str(p)):
            rel = p.parent.relative_to(root)
            parts = [seg for seg in rel.parts if seg != "api"]
            dyn = re.sub(r"\[([^\]]+)\]", r"{\1}", "/".join(parts))
            out.append(f"/api/{dyn}" if parts else "/api")
    return out


def extract_backends(roots: list[Path]) -> list[str]:
    out: list[str] = []
    for root in roots:
        if not root.exists():
            continue
        if root.is_dir():
            out += _extract_next_routes(root)  # Next.js App Router route.ts → /api/* 端点
        files = [root] if root.is_file() else sorted(root.rglob("*"))
        for p in files:
            if not p.is_file():
                continue
            if API_ROUTE_FILE.search(p.name):
                continue  # 由 _extract_next_routes 按路径处理
            if COMPONENT_EXCLUDE.search(str(p)):
                continue
            try:
                text = p.read_text(encoding="utf-8", errors="ignore")
            except OSError:
                continue
            if PY_FILE.search(p.name):
                out += _extract_decorators(text)
            out += _extract_inline(text)
    return sorted(set(out))


def selftest() -> int:
    import json
    import tempfile

    with tempfile.TemporaryDirectory() as td:
        t = Path(td)
        (t / "src").mkdir()
        (t / "src" / "Alpha.vue").write_text("<template/>", encoding="utf-8")
        (t / "src" / "beta.tsx").write_text("export default ()=><div/>", encoding="utf-8")
        (t / "src" / "Alpha.test.tsx").write_text("test", encoding="utf-8")  # 应被排除
        comps = extract_components(t / "src", COMPONENT_EXTS)
        ok1 = comps == ["Alpha", "beta"]
        api = t / "api"
        api.mkdir()
        (api / "users.py").write_text(
            '@router.get("/users")\n@router.post("/users")\n', encoding="utf-8")
        (api / "svc.py").write_text('r = client.fetch("GET /stats/mini")\n', encoding="utf-8")
        (api / "users" / "route.ts").parent.mkdir(parents=True, exist_ok=True)
        (api / "users" / "route.ts").write_text("export const GET = handlers.GET\n", encoding="utf-8")
        backs = extract_backends([api])
        ok2 = "GET /users" in backs and "POST /users" in backs and "GET /STATS/MINI" in backs and "/api/users" in backs
        print(f"selftest: 组件提取(排除测试)={ok1} 端点提取(装饰器+行内)={ok2} comps={comps} backs={backs}")
        return 0 if ok1 and ok2 else 1


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--src", help="组件根目录")
    ap.add_argument("--api", nargs="*", help="后端根目录/文件（可多个：Python 装饰器+行内、Next route.ts 路径）")
    ap.add_argument("--ext", default=",".join(COMPONENT_EXTS), help="组件扩展名（逗号分隔）")
    ap.add_argument("--out-components", default="comps.txt")
    ap.add_argument("--out-backends", default="backs.txt")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        return selftest()
    if not a.src:
        print("FAIL: 需要 --src 或 --selftest")
        return 1
    comps = extract_components(Path(a.src), [e.strip() for e in a.ext.split(",")])
    backs = extract_backends([Path(p) for p in (a.api or [])])
    Path(a.out_components).write_text("\n".join(comps) + ("\n" if comps else ""), encoding="utf-8")
    Path(a.out_backends).write_text("\n".join(backs) + ("\n" if backs else ""), encoding="utf-8")
    print(f"OK: 组件 {len(comps)} 项 → {a.out_components}；端点 {len(backs)} 项 → {a.out_backends}")
    print("提醒：bindings.json（feature↔component 绑定）是跑道产物，本器不代生产——喂 gate 前先人工/会话落绑定。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
