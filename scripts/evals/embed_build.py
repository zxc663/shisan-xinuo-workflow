# -*- coding: utf-8 -*-
"""embed_build.py · details 嵌入索引构建（Q5 嵌入层，2026-09-28 裁决批）
依赖本地 Ollama (127.0.0.1:11434) + 已拉取嵌入模型（默认 bge-m3）。
产出缓存 references/detail-embeddings.cache.json（gitignore 本地件，不随包分发——
detail_lookup 语义兜底层运行时按需读取；无缓存/无 Ollama 时 lookup 行为完全不变）。
用法: python scripts/evals/embed_build.py [--model bge-m3]
"""
import io, sys, json, re, socket, base64, struct
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
ROOT = Path(__file__).resolve().parents[2]
DETAILS = ROOT / 'skill' / 'shisan-xinuo-workflow' / 'references' / 'details.md'
CACHE = DETAILS.parent / 'detail-embeddings.cache.json'


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


def post_json(path, obj, timeout=120):
    body = json.dumps(obj).encode('utf-8')
    s = socket.create_connection(('127.0.0.1', 11434), timeout=timeout)
    req = (b'POST ' + path.encode('ascii') + b' HTTP/1.1\r\n'
           b'Host: 127.0.0.1:11434\r\n'
           b'Content-Type: application/json\r\n'
           b'Content-Length: ' + str(len(body)).encode('ascii') + b'\r\n'
           b'Connection: close\r\n\r\n' + body)
    s.sendall(req)
    buf = b''
    while True:
        chunk = s.recv(65536)
        if not chunk:
            break
        buf += chunk
    s.close()
    head, _, payload = buf.partition(b'\r\n\r\n')
    if b'Transfer-Encoding: chunked' in head:
        payload = _dechunk(payload)
    return json.loads(payload.decode('utf-8'))


def parse_entries(t):
    starts = [(m.start(), int(m.group(1))) for m in re.finditer(r'^(\d{1,3})\. ', t, re.M)]
    out = {}
    for i, (pos, num) in enumerate(starts):
        end = starts[i + 1][0] if i + 1 < len(starts) else len(t)
        out[num] = t[pos:end].strip()
    return out


def main():
    model = 'bge-m3'
    if '--model' in sys.argv:
        model = sys.argv[sys.argv.index('--model') + 1]
    t = DETAILS.read_text(encoding='utf-8')
    entries = parse_entries(t)
    cache = {'model': model, 'dim': None, 'entries': {}}
    if CACHE.exists():
        try:
            cache = json.loads(CACHE.read_text(encoding='utf-8'))
            if cache.get('model') != model:
                cache = {'model': model, 'dim': None, 'entries': {}}
        except Exception:
            pass
    todo = [n for n, txt in entries.items() if str(n) not in cache['entries']]
    print('entries:', len(entries), '| cached:', len(entries) - len(todo), '| to embed:', len(todo))
    for k, num in enumerate(sorted(todo)):
        vec = post_json('/api/embeddings', {'model': model, 'prompt': entries[num][:700]})['embedding']
        if cache['dim'] is None:
            cache['dim'] = len(vec)
        cache['entries'][str(num)] = base64.b64encode(struct.pack('<%df' % len(vec), *vec)).decode('ascii')
        if (k + 1) % 25 == 0 or k + 1 == len(todo):
            CACHE.write_text(json.dumps(cache), encoding='utf-8')
            print('progress', k + 1, '/', len(todo), flush=True)
    CACHE.write_text(json.dumps(cache), encoding='utf-8')
    print('saved:', CACHE, '| dim:', cache['dim'], '| total:', len(cache['entries']))


if __name__ == '__main__':
    main()
