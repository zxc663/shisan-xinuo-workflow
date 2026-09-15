# -*- coding: utf-8 -*-
"""probe_detail_lookup.py · detail_lookup 召回探针（随仓可复跑件，2026-09-16）

24 用例＝症状关键词 → 期望细则编号（编号均经 details.md 实读核对）。
用法:
  python scripts/evals/probe_detail_lookup.py            # 跑 24 用例出矩阵
  python scripts/evals/probe_detail_lookup.py --strict   # 非全中 exit 1（门禁用法，可选）
诚实口径：查询集为本探针自定义症状措辞，与历史路测（v6 24/24）查询集不同构——
结果只描述本查询集召回基线，不与历史数字互斥。
"""
import json, os, re, subprocess, sys, io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOKUP = os.path.join(ROOT, 'scripts', 'detail_lookup.py')

CASES = [
    ('Edit 文件冲突 not been read', 294),
    ('命名直觉 信封解包 ApiResponse', 233),
    ('改共享包 旧 dist 类型', 228),
    ('常驻进程 旧 dist 端口', 229),
    ('响应形态 分层断言 2xx 信封', 214),
    ('统一错误契约 code data null', 163),
    ('异步栈 丢调用点', 256),
    ('响应体 只消费一次', 269),
    ('深拷贝 undefined 键 丢弃', 262),
    ('Promise.race 快慢 负载形状', 266),
    ('不复现 判定 举证 对照组', 255),
    ('上下文折叠 保留清单 五必留', 272),
    ('紧凑档 短上下文 窗口比例', 273),
    ('模块锚点表 repo map', 275),
    ('决策化石 历史否决 重开', 279),
    ('每轮复述 一行 理解校验', 325),
    ('压缩接续 compact 重载 Skills', 326),
    ('开工前置门 调研基准 回滚点', 332),
    ('长驻进程 端口归零 交付收尾', 295),
    ('依赖锁文件 选型', 334),
    ('性能预算 Web Vitals', 335),
    ('文档分型 Diátaxis', 333),
    ('多环境配置', 340),
    ('结构化日志 可观测', 341),
]


def main():
    strict = '--strict' in sys.argv
    rows, hits = [], 0
    for kw, expect in CASES:
        p = subprocess.run([sys.executable, LOOKUP, kw], capture_output=True, encoding='utf-8', errors='replace')
        out = (p.stdout or '') + (p.stderr or '')
        ids = [int(x) for x in re.findall(r'#(\d{1,3})', out)]
        # 期望细则在命中列表（含修复模板行）即算召回
        ok = expect in ids
        first = ids[0] if ids else None
        rows.append({'kw': kw, 'expect': expect, 'hit': ok, 'first': first, 'exit': p.returncode})
        hits += 1 if ok else 0
        print(f"{'PASS' if ok else 'FAIL'}  {kw:<28} 期望 #{expect}  首命中 #{first}")
    print(f'\n召回 {hits}/{len(CASES)}')
    if strict and hits != len(CASES):
        print('STRICT FAIL: 非全中')
        sys.exit(1)
    if '--json' in sys.argv:
        ex = os.path.join(ROOT, 'scripts', 'evals')
        json.dump({'hits': hits, 'total': len(CASES), 'rows': rows},
                  open(os.path.join(ex, 'probe_detail_lookup.last.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)


if __name__ == '__main__':
    main()
