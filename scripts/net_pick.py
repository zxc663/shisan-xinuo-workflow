#!/usr/bin/env python3
"""net_pick.py · 外网通道测速择快（G7/T11，2026-09-29）。

背景：红海 33210 是唯一外网通道且速率 1MB/s↔67KB/s 波动（gap-list G7 网络单点）。
本脚本对同一目标 URL 并发测三条通道，输出速率表+胜者，供 winget/curl/git 挑通道：
  direct   直连（不走代理）
  redsea   本地代理 127.0.0.1:33210（默认，可 --proxy 覆盖）
  ghproxy  gh-proxy.com 前缀镜像（仅对 github 域目标有意义）

用法：
  python scripts/net_pick.py                       # 默认目标 raw.githubusercontent.com 小文件
  python scripts/net_pick.py --url <URL> --max-kb 512 --timeout 15
退出码：0=至少一条通道成功（胜者打在 WINNER 行）；1=全败。
诚实边界：单目标单次采样，速率瞬时值非均值——重要决策请 --repeat 3 取中位。
"""
from __future__ import annotations

import argparse
import statistics
import sys
import time
import urllib.request

DEFAULT_URL = "https://raw.githubusercontent.com/git/git/master/README.md"
GHPROXY_PREFIX = "https://gh-proxy.com/"


def timed_fetch(url: str, proxies: dict, timeout: float, max_bytes: int) -> tuple[int, float]:
    """返回 (bytes, 秒)；失败抛异常。"""
    op = urllib.request.build_opener(urllib.request.ProxyHandler(proxies))
    req = urllib.request.Request(url, headers={"User-Agent": "net_pick/1"})
    t0 = time.time()
    n = 0
    with op.open(req, timeout=timeout) as r:
        while n < max_bytes:
            chunk = r.read(65536)
            if not chunk:
                break
            n += len(chunk)
    return n, max(time.time() - t0, 0.001)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--url", default=DEFAULT_URL)
    ap.add_argument("--proxy", default="http://127.0.0.1:33210", help="红海本地代理（默认 33210）")
    ap.add_argument("--max-kb", type=int, default=256, help="每通道最大下载量（KB，测速封顶）")
    ap.add_argument("--timeout", type=float, default=12.0)
    ap.add_argument("--repeat", type=int, default=1, help="每通道重复次数（>1 取中位速率）")
    a = ap.parse_args()

    channels = [
        ("direct", a.url, {}),
        ("redsea", a.url, {"http": a.proxy, "https": a.proxy}),
        ("ghproxy", GHPROXY_PREFIX + a.url, {}),
    ]
    results: list[tuple[str, float, int]] = []  # (name, KB/s 中位, bytes)
    for name, url, proxies in channels:
        rates, total = [], 0
        for _ in range(max(1, a.repeat)):
            try:
                n, dt = timed_fetch(url, proxies, a.timeout, a.max_kb * 1024)
                rates.append(n / dt / 1024.0)
                total = n
            except Exception as e:  # noqa: BLE001
                print(f"  {name:<8} FAIL: {type(e).__name__}: {e}")
                rates = []
                break
        if rates:
            med = statistics.median(rates)
            results.append((name, med, total))
            print(f"  {name:<8} {med:9.1f} KB/s  ({total} bytes × {len(rates)} 次)")
    if not results:
        print("WINNER: —（全通道失败）")
        return 1
    winner, rate, _ = max(results, key=lambda x: x[1])
    print(f"WINNER: {winner} ({rate:.1f} KB/s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
