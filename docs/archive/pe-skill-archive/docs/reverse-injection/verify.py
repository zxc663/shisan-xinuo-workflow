#!/usr/bin/env python3
"""反向注入实证 harness —— 候选 12（C7 契约 recovery 行 ↔ 转换双向对账）、候选 13（C6 引用完整性）、
结构化错误态（C4 识别不再只靠名启发式）。

判读纪律（来自 docs/closed-loop-report.md §3 的教训）：证据必须含
  ① 命令原文  ② 变异 diff  ③ 真实退出码  —— 三者缺一，本 harness 判失败。

期望（硬断言，任一不满足即 exit 1）：
  对照组           : exit 0（契约一致放行）
  A 抽 RETRY_EXPORT: exit 1 且命中 C7 正向（承诺落空）
  B 抽全部出边     : exit 1 且命中 C2 + C4 + C7 正向（门禁设计域内有效，三重）
  C 删态留悬空入边 : exit 1 且命中 C6（引用完整性）
  D 抽 DISMISS     : exit 1 且命中 C4 + C7 正向（结构化错误态识别起效）

用法：
  python verify.py --gate <statechart-gate.py> [--source <试验仓 favorites.json>] [--out EVIDENCE.md]

安全写法：所有被执行的路径先经 _checked_file 校验（存在性 + 后缀白名单 + resolve），
子进程一律使用参数列表与 shell=False；展示用的命令串只用于证据留档。
"""
from __future__ import annotations

import argparse
import copy
import difflib
import hashlib
import json
import shlex
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
DEFAULT_SOURCE = "D:/产品工程闭环实验/docs/contracts/favorites.json"


def sha16(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()[:16]


def _checked_file(raw: str, suffixes: tuple[str, ...]) -> Path:
    """校验路径：必须存在、是普通文件、且后缀在白名单内；返回解析后的绝对路径。"""
    q = Path(raw).expanduser().resolve()
    if not q.is_file():
        raise SystemExit(f"FAIL: 路径不存在或不是文件：{q}")
    if q.suffix.lower() not in suffixes:
        raise SystemExit(f"FAIL: 仅接受 {'/'.join(suffixes)} 文件：{q}")
    return q


def run_gate(gate: Path, sc: Path, contract: Path | None) -> tuple[str, int, str]:
    """以参数列表方式执行门禁（无 shell、无字符串拼接）；返回 (展示用命令原文, 退出码, 输出)。"""
    argv = [sys.executable, "--", str(gate), "--file", str(sc)]
    if contract is not None:
        argv += ["--contract", str(contract)]
    p = subprocess.run(argv, capture_output=True, text=True, encoding="utf-8",
                       errors="replace", shell=False, check=False)
    return shlex.join(argv), p.returncode, ((p.stdout or "") + (p.stderr or "")).strip()


def unified_diff(base: dict, variant: dict) -> str:
    a = json.dumps(base, ensure_ascii=False, indent=2).splitlines(keepends=True)
    b = json.dumps(variant, ensure_ascii=False, indent=2).splitlines(keepends=True)
    d = list(difflib.unified_diff(a, b, fromfile="favorites.statechart.json", tofile="mutant.json", n=2))
    return "".join(d) if d else "(无差异)"


def build_variants(sc: dict) -> dict[str, dict]:
    vs: dict[str, dict] = {}
    a = copy.deepcopy(sc)
    a["states"]["export_failed"]["on"].pop("RETRY_EXPORT")
    vs["A 抽单条恢复转换（RETRY_EXPORT）"] = a

    b = copy.deepcopy(sc)
    b["states"]["export_failed"]["on"] = {}
    vs["B 抽 export_failed 全部出边（强变异）"] = b

    c = copy.deepcopy(sc)
    c["states"].pop("export_failed")  # exporting 的 EXPORT_FAIL 边仍在 → 悬空入边
    vs["C 删除整个 export_failed 态（留悬空入边）"] = c

    d = copy.deepcopy(sc)
    d["states"]["permission_denied"]["on"] = {}
    vs["D 抽权限态唯一出路（DISMISS）"] = d
    return vs


EXPECT = {
    "对照组（原文件）": (0, []),
    "A 抽单条恢复转换（RETRY_EXPORT）": (1, ["C7 正向", "RETRY_EXPORT"]),
    "B 抽 export_failed 全部出边（强变异）": (1, ["C2", "C4", "C7 正向"]),
    "C 删除整个 export_failed 态（留悬空入边）": (1, ["C6", "export_failed"]),
    "D 抽权限态唯一出路（DISMISS）": (1, ["C4", "C7 正向", "DISMISS"]),
}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--gate", required=True, help="statechart-gate.py 路径")
    ap.add_argument("--source", default=DEFAULT_SOURCE, help="试验仓原始 statechart（仅用于同源校验，只读）")
    ap.add_argument("--out", default=str(HERE / "EVIDENCE.md"))
    a = ap.parse_args()

    gate = _checked_file(a.gate, (".py",))
    base_p = _checked_file(str(HERE / "favorites.statechart.json"), (".json",))
    contract = _checked_file(str(HERE / "favorites.contract.json"), (".json",))
    sc = json.loads(base_p.read_text(encoding="utf-8"))
    vs = build_variants(sc)

    lines: list[str] = []
    ok_all = True
    src_note = "（源文件不可达，跳过同源校验）"
    try:
        src_p = _checked_file(a.source, (".json",))
        src_note = f"源= `{src_p}`｜sha256[:16]= `{sha16(src_p)}`（与本地副本一致={sha16(src_p) == sha16(base_p)}）"
    except SystemExit:
        pass

    lines.append(f"# 反向注入实证（自动生成，勿手改——重跑：`python {Path(__file__).name} --gate <gate>`）\n")
    lines.append(f"- 语料：`favorites.statechart.json`（11 态/26 边，sha256[:16]= `{sha16(base_p)}`）；{src_note}")
    lines.append("- 契约：`favorites.contract.json`（转录自 试验仓 `favorites.contract.md` §③:44-46 + 附注:48）")
    lines.append(f"- 门禁：`{gate}`\n")

    with tempfile.TemporaryDirectory(prefix="reverse-injection-") as td_raw:
        td = Path(td_raw).resolve()
        for name, obj in vs.items():
            lines.append(f"\n## {name}\n")
            lines.append("```diff")
            lines.append(unified_diff(sc, obj).rstrip())
            lines.append("```\n")
            vp = td / "mutant.json"
            vp.write_text(json.dumps(obj, ensure_ascii=False, indent=2), encoding="utf-8")
            shown, rc, out = run_gate(gate, vp, contract)
            exp_rc, exp_marks = EXPECT[name]
            missed = [m for m in exp_marks if m not in out]
            ok = (rc == exp_rc) and not missed
            ok_all &= ok
            lines.append(f"- 命令原文：`{shown}`")
            lines.append(f"- 退出码：`{rc}`（期望 `{exp_rc}`）")
            lines.append(f"- 期望命中：{exp_marks or '（无，要求全绿）'}｜未命中：{missed or '无'}")
            lines.append(f"- 判读：**{'PASS' if ok else 'FAIL'}**")
            lines.append("- 输出：")
            lines.append("```")
            lines.append(out if out else "(空)")
            lines.append("```")

        lines.append("\n## 对照组（原文件 + 契约）\n")
        shown, rc, out = run_gate(gate, base_p, contract)
        ok = rc == EXPECT["对照组（原文件）"][0]
        ok_all &= ok
        lines.append("- 变异 diff：无（对照组）")
        lines.append(f"- 命令原文：`{shown}`")
        lines.append(f"- 退出码：`{rc}`（期望 `0`）")
        lines.append(f"- 判读：**{'PASS' if ok else 'FAIL'}**")
        lines.append("- 输出：")
        lines.append("```")
        lines.append(out if out else "(空)")
        lines.append("```")

        lines.append("\n## 对照组（原文件，无契约参数）\n")
        shown2, rc2, out2 = run_gate(gate, base_p, None)
        lines.append(f"- 命令原文：`{shown2}`")
        lines.append(f"- 退出码：`{rc2}`（期望 `0`——C7 未启用时退化为结构检查）")
        lines.append(f"- 判读：**{'PASS' if rc2 == 0 else 'FAIL'}**")
        ok_all &= rc2 == 0

    lines.append("\n## 总结\n")
    lines.append(f"- 硬断言：**{'全部通过' if ok_all else '存在失败项'}**（失败即 harness exit 1）")
    if ok_all:
        lines.append("- 结论：「缺失可检出」在**行级（C7 正向）与引用级（C6）**获得反向注入实证；"
                     "态级由 B 组三重命中（C2+C4+C7）佐证；对照组两态（含/不含契约）均全绿。")
    else:
        lines.append("- 结论：未获实证，见上方 FAIL 项。")
    out_path = Path(a.out).resolve()
    out_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"harness: {'PASS' if ok_all else 'FAIL'} → 证据写入 {out_path}")
    return 0 if ok_all else 1


if __name__ == "__main__":
    sys.exit(main())
