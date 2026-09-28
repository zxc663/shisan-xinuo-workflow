# -*- coding: utf-8 -*-
"""probe_detail_lookup.py · detail_lookup 召回探针（随仓可复跑件，2026-09-16 建 / 2026-09-28 扩容）

金样本 60 例三段制：
  POS   原始 24 例（2026-09-16 基线，编号均经 details.md 实读核对）
  POS+  扩容 22 例（换措辞/口语/英文，测鲁棒召回；期望编号 2026-09-28 grep 实证）
  NEG   8 例垃圾/过泛查询（期望=诚实 0 命中；护栏=过泛阈值+2-gram 双闸）
  EXP   6 例扩写判别（查询词不在 details.md 词面，须零召回扩写层才可召回）
实现层经模块导入直测（零 subprocess）；CLI 端到端由探针使用方的真实命令证真
（detail_lookup "关键词" 每日 errpath 在用 + 评估报告附 CLI 冒烟记录）。
用法:
  python scripts/evals/probe_detail_lookup.py            # 跑 60 例出矩阵
  python scripts/evals/probe_detail_lookup.py --strict   # 非全中 exit 1（门禁用法，可选）
诚实口径：查询集为本探针自定义症状措辞，与历史路测查询集不同构——
结果只描述本查询集召回基线，不与历史数字互斥。
"""
import contextlib, importlib.util, io, os, re, sys
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
ROOT = Path(__file__).resolve().parents[2]
LOOKUP = ROOT / 'skill' / 'shisan-xinuo-workflow' / 'scripts' / 'detail_lookup.py'

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

POS_EXT = [
    ('编辑器说文件没有读过 不能编辑', 294),
    ('copy 出来的对象 字段丢了', 262),
    ('端口一直被占 交付前', 295),
    ('这个 bug 报告说修好了但没法证实', 255),
    ('接口偶尔超时 高并发 排队', 266),
    ('上下文被压缩完 接着干要干嘛', 326),
    ('今天开工之前要先做什么', 332),
    ('接手一个仓库第一步', 307),
    ('设计稿还没确认就动手写', 312),
    ('接手老项目没有任何文档', 316),
    ('新项目开工要问清楚哪些', 306),
    ('做界面前要不要找参考', 284),
    ('生产环境的限流阈值要改', 370),
    ('怎么证明不是只跑过而是跑对了', 371),
    ('半夜自动跑遇到要删数据', 369),
    ('记录文件太大了怎么处理', 372),
    ('返回的数据结构跟说好的不一样', 214),
    ('异步抛错定位不到源头', 256),
    ('接口的返回体读第二次就空了', 269),
    ('发现方向不对中途停下', 280),
    ('锁文件要不要提交', 334),
    ('lighthouse 分数怎么算好', 335),
]

NEG_CASES = [
    'xyznonexistent12345',
    'qqzzxxwoooloo',
    '哈哈哈哈哈哈',
    'asdfghjkl',
    '的',
    'wwww mmmm',
    'zzz xxx ccc',
    ' Lorem ipsum dolor',
]

EXP_CASES = [
    ('文件未读', 294),
    ('深复制丢字段', 262),
    ('端口被占用', 295),
    ('没读过就编辑', 294),
    ('deep copy 丢字段', 262),
    ('重启完还是旧版本', 229),
]


def load_impl():
    assert LOOKUP.is_file(), f'实现文件不在: {LOOKUP}'
    spec = importlib.util.spec_from_file_location('detail_lookup_impl', str(LOOKUP))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def run_case(mod, kw):
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        sys.argv = ['detail_lookup', kw]
        try:
            mod.main()
        except SystemExit:
            pass
    return buf.getvalue()


def main():
    strict = '--strict' in sys.argv
    mod = load_impl()
    rows = {'pos': [], 'neg': [], 'exp': []}
    stat = {'pos': [0, 0], 'neg': [0, 0], 'exp': [0, 0]}  # [pass, total]

    def check(kind, kw, expect):
        out = run_case(mod, kw)
        ids = [int(x) for x in re.findall(r'#(\d{1,3})', out)]
        ok = (len(ids) == 0) if expect == 0 else (expect in ids)
        first = ids[0] if ids else None
        rows[kind].append({'kw': kw, 'expect': expect, 'hit': ok, 'first': first})
        stat[kind][0] += 1 if ok else 0
        stat[kind][1] += 1
        print(f"{'PASS' if ok else 'FAIL'}  [{kind}]  {kw:<30}  期望 {expect if expect else '0命中'}  首命中 {first}")

    for kw, expect in CASES + POS_EXT:
        check('pos', kw, expect)
    for kw in NEG_CASES:
        check('neg', kw, 0)
    for kw, expect in EXP_CASES:
        check('exp', kw, expect)

    p, n, e = stat['pos'], stat['neg'], stat['exp']
    print(f'\n正例召回 {p[0]}/{p[1]} ｜ 负例误报 {n[1]-n[0]}/{n[1]}（须=0）｜ 扩写召回 {e[0]}/{e[1]}')
    if strict and (p[0] != p[1] or n[0] != n[1] or e[0] != e[1]):
        print('STRICT FAIL: 非全中')
        sys.exit(1)


if __name__ == '__main__':
    main()
