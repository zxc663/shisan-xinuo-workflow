# -*- coding: utf-8 -*-
"""细则一键检索端口 · detail_lookup
把「打开 details.md → 找症状索引 → 定域 → 读条目」四步压成一条命令。
用法:
  python scripts/detail_lookup.py <关键词> [关键词2...]   # 关键词检索（任意命中，按命中数排序）
  python scripts/detail_lookup.py --id 233               # 按编号直查（T3）
  python scripts/detail_lookup.py --domain 前端           # 按症状域列出条目
  python scripts/detail_lookup.py --index                # 打印症状索引全表
  加 --full 输出条目全文（默认摘要 160 字）
设计: 只用标准库；输出紧凑（token 友好）；命中行可直接贴进任务记录作 errpath 证据。
语义层: references/detail-expansions.json 查询扩写（同义/英文/口语 → 词面锚），
  仅在原始词零召回时触发扩写重试（不污染良性查询）；2-gram 回退带垃圾护栏
  （全库共振 >20 条或首位覆盖率不足 → 诚实报 0，防假阳性——外部审计 E6 修复）。
"""
import io, re, sys, os, json, socket
from pathlib import Path

if getattr(sys.stdout, 'encoding', '').lower().replace('-', '') != 'utf8':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')  # 已是 utf-8 不重包（防二次包装关 buffer）
_SELF = Path(__file__).resolve()
_CANDIDATES = [
    _SELF.parent.parent / 'references' / 'details.md',                                      # 技能副本布局（scripts/ 与 references/ 同级）
    _SELF.parent.parent / 'skill' / 'shisan-xinuo-workflow' / 'references' / 'details.md',  # 源库布局（仓库根 scripts/）
]
DETAILS = next((c for c in _CANDIDATES if c.is_file()), _CANDIDATES[0])
EXPANSIONS = DETAILS.parent / 'detail-expansions.json'

# 垃圾/过泛护栏阈值：真症状不会全库共振
GENERIC_LIMIT = 100    # 单词命中条目数 ≥ 该值=过泛查询（如单字虚词）
GRAM_MAX_MATCHES = 20  # 2-gram 回退：命中条目数超过=垃圾共振，诚实报 0
GRAM_MIN_COVER = 3     # 首位条目 gram 命中数 × 该值须 ≥ 查询 grams 总数

# TOP 条目修复命令模板（命中即附处置动作行；权威源 = injection-core 错误段）
FIX_TEMPLATES = {
    294: '重新 Read 目标文件后重试 Edit/Write（写操作闭环=改写→验证落盘）',
    233: 'grep 调用点 → 读 schema/类型 → 确认包归属 → 再写（禁命名直觉）',
    228: '先重编共享包（build/tsc）→ 再跑消费方（旧 dist 是类型假象）',
    229: '先查进程 uptime 与 dist 时间戳判别 → 再走重启仪式（重建 dist→重启→health 检查）',
    214: '按响应分层断言：成功=裸数据 / 校验失败=2xx 信封 / 真 404=状态码',
    163: '统一错误契约：code≠0 才算失败；data:null 是合法成功',
    256: 'await 处包 try/catch 带上下文标签（防异步栈丢调用点）',
    270: '响应体需复用先 clone()/text() 落变量（只可消费一次）',
    262: '深拷贝语义变体：undefined 键会被丢弃，需保留用显式拷贝',
    238: '报错必经日志：catch 三件套（记日志+降级提示+审计）；空 catch 零容忍',
}


def parse():
    t = DETAILS.read_text(encoding='utf-8')
    # 症状索引: - **域名**【T2】 → #a, #b, ...
    domains = {}
    for m in re.finditer(r'- \*\*(.+?)\*\*【(T2|T3)】 → ([0-9#, ]+)', t):
        ids = [int(x) for x in re.findall(r'\d+', m.group(3))]
        domains[m.group(1)] = (m.group(2), ids)
    # 条目: 行首 NNN. 开始，至下一个条目/小节头
    starts = [(m.start(), int(m.group(1))) for m in re.finditer(r'^(\d{1,3})\. ', t, re.M)]
    entries = {}
    for i, (pos, num) in enumerate(starts):
        end = starts[i + 1][0] if i + 1 < len(starts) else len(t)
        block = t[pos:end].strip()
        entries[num] = block
    return t, domains, entries


def load_expansions():
    try:
        return json.loads(EXPANSIONS.read_text(encoding='utf-8')).get('rules', [])
    except Exception:
        return []


def expand(args, rules):
    """零召回扩写：查询串含任一 if 词 → 收集 then 词面锚（不改原始词）。"""
    text = ' '.join(args).lower()
    added = []
    for r in rules:
        for term in r.get('if', []):
            if term.lower() in text:
                for kw in r.get('then', []):
                    if kw not in args and kw not in added:
                        added.append(kw)
                break
    return added


def _dechunk(payload):
    out = b''
    while payload:
        line, _, rest = payload.partition(b'\r\n')
        try:
            sz = int(line.strip() or b'0', 16)
        except ValueError:
            return payload
        if sz == 0:
            break
        out += rest[:sz]
        payload = rest[sz+2:]
    return out


def _semantic_boost(query, entries, top=5, floor=0.55):
    """嵌入语义兜底：仅当本地缓存（detail-embeddings.cache.json）与 Ollama(127.0.0.1:11434) 均可用时生效。
    返回 [(cos, num, text)]；归一化余弦绝对阈值 floor——垃圾/无关查询天然低于阈值→诚实 0。"""
    import base64, struct, math
    cache_p = DETAILS.parent / 'detail-embeddings.cache.json'
    if not cache_p.is_file():
        return []
    cache = json.loads(cache_p.read_text(encoding='utf-8'))
    if not cache.get('entries'):
        return []
    body = json.dumps({'model': cache.get('model', 'bge-m3'), 'prompt': query[:700]}).encode('utf-8')
    s = socket.create_connection(('127.0.0.1', 11434), timeout=20)
    req = (b'POST /api/embeddings HTTP/1.1\r\nHost: 127.0.0.1:11434\r\n'
           b'Content-Type: application/json\r\nContent-Length: ' + str(len(body)).encode('ascii') +
           b'\r\nConnection: close\r\n\r\n' + body)
    s.sendall(req)
    buf = b''
    while True:
        c = s.recv(65536)
        if not c:
            break
        buf += c
    s.close()
    head, _, payload = buf.partition(b'\r\n\r\n')
    if b'Transfer-Encoding: chunked' in head:
        payload = _dechunk(payload)
    qv = json.loads(payload.decode('utf-8')).get('embedding')
    if not qv:
        return []
    scored = []
    qn = math.sqrt(sum(a * a for a in qv)) or 1.0
    for num_s, b64 in cache['entries'].items():
        num = int(num_s)
        if num not in entries:
            continue
        arr = base64.b64decode(b64)
        vec = struct.unpack('<%df' % (len(arr) // 4), arr)
        vn = math.sqrt(sum(a * a for a in vec)) or 1.0
        cos = sum(a * b for a, b in zip(qv, vec)) / (qn * vn)
        if cos >= floor:
            scored.append((cos, num, entries[num]))
    scored.sort(key=lambda x: (-x[0], x[1]))
    return scored[:top]


def log_usage(query_args, ids):
    """G4 usage-probe（2026-09-29）：每次检索落一行 JSONL（命中 ids 或空=零命中），
    供退役候选机器判据（零命中 N 批→降级候选，只列候选不删条）。静默失败不碍检索主路。"""
    try:
        import datetime, json
        from pathlib import Path
        p = Path.home() / '.zcode' / 'cli' / 'detail-lookup-usage.jsonl'
        rec = {'ts': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
               'q': ' '.join(query_args), 'ids': [int(i) for i in ids[:12]]}
        with open(p, 'a', encoding='utf-8') as f:
            f.write(json.dumps(rec, ensure_ascii=False) + '\n')
    except Exception:
        pass


def main():
    args = [a for a in sys.argv[1:]]
    full = '--full' in args
    args = [a for a in args if a != '--full']
    t, domains, entries = parse()

    if not args:
        print(__doc__)
        return
    if args[0] == '--index':
        for name, (layer, ids) in domains.items():
            print(f'[{layer}] {name}: {len(ids)} 条')
        return
    if args[0] == '--id':
        for a in args[1:]:
            num = int(re.sub(r'\D', '', a) or 0)
            e = entries.get(num)
            print(e if e else f'#{num} 不存在（范围 1-{max(entries)}）')
        return
    if args[0] == '--domain':
        key = args[1] if len(args) > 1 else ''
        for name, (layer, ids) in domains.items():
            if key in name:
                print(f'[{layer}] {name}: {", ".join("#"+str(i) for i in ids)}')
        return

    exact = list(args)
    parts = []
    for a in args:
        parts.extend([w for w in a.split() if w and w != a])
    id2domains = {}
    for name, (layer, ids) in domains.items():
        for i in ids:
            id2domains.setdefault(i, []).append(name)

    def match(terms_exact, terms_parts):
        out = []
        for num, text in entries.items():
            hits = sum(text.count(k) for k in terms_exact) * 3 + sum(text.count(k) for k in terms_parts)
            if hits:
                out.append((hits, num, text))
        return out

    def emit(scored, mode):
        scored.sort(key=lambda x: (-x[0], x[1]))
        log_usage(args, [str(num) for _, num, _ in scored[:12]])
        head = f'{len(scored)} 命中（{mode}；errpath 证据格式: detail_lookup "{" ".join(args)}" → #{scored[0][1]}）'
        print(head)
        for hits, num, text in scored[:12]:
            doms = '/'.join(id2domains.get(num, []))
            body = text if full else text[:160].replace('\n', ' ') + ('…' if len(text) > 160 else '')
            print(f'\n#{num} [{doms}] 命中×{hits}\n{body}')
            if num in FIX_TEMPLATES:
                print(f'修复模板: {FIX_TEMPLATES[num]}')

    scored = []
    added = expand(args, load_expansions())
    terms_exact = exact + added
    scored = match(terms_exact, parts)
    if scored:
        distinct = set(terms_exact) | set(parts)
        if len(distinct) == 1 and len(scored) >= GENERIC_LIMIT:
            log_usage(args, [])
            print(f'0 命中（单词命中 {len(scored)} 条≥{GENERIC_LIMIT}=过泛查询全库共振；换具体症状关键词，可试 --index）')
            return
        mode = '按相关度排序' + (f'；扩词: {" ".join(added)}' if added else '') + (f'；分词: {" ".join(parts)}' if parts else '')
        emit(scored, mode)
        return

    # 2-gram 回退：无空格中文长句整串零召回时，按相邻二字片段命中数兜底（≥2 片段命中同一条目才出），
    # 带垃圾护栏：全库共振（>条目上限）或首位覆盖率不足 → 判垃圾诚实报 0（防假阳性，E6 修复）
    grams = set()
    for a in args:
        s = re.sub(r'\s+', '', a)
        if len(s) > 3:
            grams |= {s[i:i + 2] for i in range(len(s) - 1)}
    if grams:
        cand = []
        for num, text in entries.items():
            g = sum(1 for gr in grams if gr in text)
            if g >= 2:
                cand.append((g, num, text))
        if cand and len(cand) > GRAM_MAX_MATCHES:
            cand = []  # 全库共振判垃圾——落语义兜底层做最后一道诚实尝试
        if cand:
            cand.sort(key=lambda x: (-x[0], x[1]))
            if cand[0][0] * GRAM_MIN_COVER < len(grams):
                cand = []  # 首位覆盖率不足——落语义兜底层做最后一道诚实尝试
            else:
                emit(cand, '2-gram 回退')
                return
    # 语义兜底层（Q5 可选增强）：本地 Ollama 嵌入（socket 直连本机回环）；缓存与模型均不可用则静默跳过，行为不变
    try:
        sem = _semantic_boost(' '.join(args), entries)
        if sem:
            emit(sem, '语义召回（嵌入兜底）')
            return
    except Exception:
        pass
    log_usage(args, [])
    print(f'0 命中（关键词: {" ".join(args)}；可试 --index 换域或换关键词）')


if __name__ == '__main__':
    main()
