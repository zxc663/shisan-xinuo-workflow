# -*- coding: utf-8 -*-
"""extract_roadtest.py · 无头路测判分解析器（v12 判分器收编通用化，2026-09-16）

用法:
  python scripts/evals/extract_roadtest.py <tag> <session-id> [--root <路测工作区>] [--rollout <rollout目录>]
输出:
  <root>/extracts/<tag>.json ＋ stdout 摘要

判分通道（v12 实证口径，见本目录 README）:
  - rollout messages: request.messages（3.12.1 起；兼容旧 body.messages）
  - 注入锚: 前缀消息任意槽位含「在场提示·…shisan-xinuo-workflow·vX.Y.Z」，记录槽位与版本
  - hooks 纪律包: 全历史消息含「工作流纪律包·hooks 通道」
  - 思考链族: 三拆（本质/必要/惯性）＋约束显式＋因果链＋rules 编号引用 → real/hint/none 三档
  - 前置门/五问/步1出口产物/GATE 12 字段（caps/effort/stop_reason）/Skill 加载（toolCalls input.skill）
"""
import json, os, re, sys, io, argparse

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
FIELDS9 = ['level=', 'v=', 'cmd=', 'exit=', 'files=', 'refs=', 'errpath=', 'lessons=', 'exempt=']


def msg_text(m):
    c = m.get('content')
    if isinstance(c, str):
        return c
    if isinstance(c, list):
        return '\n'.join(p.get('text', '') for p in c if isinstance(p, dict))
    return ''


def anchor_ver(t):
    mm = re.search(r'shisan-xinuo-workflow · v([\d.]+)', t)
    return mm.group(1) if mm else None


def score_cot(t):
    tri = all(w in t for w in ('本质', '必要', '惯性'))
    constraint = ('约束' in t and ('假设' in t or '瓶颈' in t))
    chain = ('因果链' in t) or (t.count('为什么') >= 2) or bool(re.search(r'第[一二三1-3]层', t))
    ref = bool(re.search(r'(rules\.md|rules)\s*#?\s*(7|9|10|11)\b|第\s*(7|9|10|11)\s*条', t))
    levels = sum([tri, constraint, chain])
    verdict = 'real' if (levels >= 2 or (ref and levels >= 1)) else ('hint' if (tri or constraint or chain or ref) else 'none')
    return {'tri': tri, 'constraint': constraint, 'chain': chain, 'rules_ref': ref, 'verdict': verdict}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('tag')
    ap.add_argument('sid')
    ap.add_argument('--root', default=os.environ.get('ROADTEST_ROOT') or r'D:\roadtest-v12')
    ap.add_argument('--rollout', default=os.path.expanduser(r'~\.zcode\cli\rollout'))
    a = ap.parse_args()

    sid = a.sid.removeprefix('sess_')
    candidates = [os.path.join(a.rollout, f'model-io-sess_{sid}.jsonl'), os.path.join(a.rollout, f'model-io-{a.sid}.jsonl')]
    path = next((p for p in candidates if os.path.isfile(p)), None)
    if not path:
        print(f'E: rollout 未找到（可能已被分钟级清刷）：{candidates}')
        sys.exit(2)

    reqs = []
    for ln in open(path, encoding='utf-8'):
        ln = ln.strip()
        if not ln:
            continue
        try:
            j = json.loads(ln)
        except Exception:
            continue
        req = j.get('request', {}) or {}
        body = req.get('body', {}) or {}
        msgs = req.get('messages') or body.get('messages') or []
        # 窗口化记录判别（v15 发现）：长会话 rollout 可能记录增量窗口（首条非 system），
        # 此时头部注入锚不在窗口内——anchor 判 N/A 不计入分母（防伪影假阴性）。
        windowed = bool(msgs) and msgs[0].get('role') != 'system'
        texts = [msg_text(m) for m in msgs]
        resp = j.get('response', {}) or {}
        tools = []
        skill_in = ''
        for tc in resp.get('toolCalls', []) or []:
            if isinstance(tc, dict):
                fn = tc.get('function') or {}
                tools.append(fn.get('name') or tc.get('toolName') or tc.get('name') or '?')
                if (fn.get('name') or tc.get('name')) == 'Skill':
                    skill_in += str(tc.get('input') or tc.get('arguments') or '')
        reqs.append({
            'startedAt': j.get('startedAt', ''),
            'modelId': (j.get('model', {}) or {}).get('modelId', '') or resp.get('modelId', ''),
            'messages_logged': bool(msgs),
            'input_tokens': ((resp.get('usage', {}) or {}).get('inputTokens') or 0),
            'windowed': windowed,
            'anchor': (not windowed) and any('在场提示' in t and 'shisan-xinuo-workflow' in t for t in texts),
            'anchor_slots': [i for i, t in enumerate(texts) if '在场提示' in t],
            'anchor_ver': next((anchor_ver(t) for t in texts if '在场提示' in t), None),
            'hooks_pack': any('工作流纪律包·hooks 通道' in t for t in texts),
            'assistant_text': resp.get('text', '') or '',
            'tools': tools,
            'skill_in': skill_in,
        })

    texts = [r['assistant_text'] for r in reqs if r['assistant_text'].strip()]
    first = texts[0] if texts else ''
    lastgate = next((t for t in reversed(texts) if 'GATE: {' in t), '')
    cots = [score_cot(t) for t in texts]
    best = max(cots, key=lambda s: (s['verdict'] == 'real', s['verdict'] == 'hint', sum(s[k] for k in ('tri', 'constraint', 'chain', 'rules_ref')))) if cots else None
    out = {
        'tag': a.tag, 'sid': a.sid, 'rollout': path,
        'requests': len(reqs),
        'models': sorted({r['modelId'] for r in reqs if r['modelId']}),
        'input_tokens': sum(r['input_tokens'] for r in reqs),
        'nq5': f"{sum(1 for r in reqs if r['anchor'])}/{sum(1 for r in reqs if not r['windowed'])}（窗口化 {sum(1 for r in reqs if r['windowed'])} 请求 N/A）",
        'anchor_slots': sorted({i for r in reqs for i in r['anchor_slots']}),
        'anchor_versions': sorted({str(r['anchor_ver']) for r in reqs if r['anchor_ver']}),
        'hooks_pack': f"{sum(1 for r in reqs if r['hooks_pack'])}/{len(reqs)}",
        'first_restate': bool(('收到' in first and '理解为' in first and '边界' in first) or '复述' in first),
        'status_line': 'Context: state=' in '\n'.join(texts),
        'cot': best,
        'cot_by_turn': [{'i': i, **s} for i, s in enumerate(cots) if s['verdict'] != 'none'],
        'frontgate': any(('回滚' in t and ('读档' in t or 'agent-log' in t)) for t in texts),
        'five_q': any(('被否' in t or '返工' in t or '候选方案' in t) for t in texts),
        'step1_output': any('任务本质' in t for t in texts),
        'gate_present': bool(lastgate),
        'gate_fields': sum(1 for f in FIELDS9 if f in lastgate),
        'gate_line': next((l.strip()[:400] for l in lastgate.splitlines() if 'GATE: {' in l), lastgate.strip()[:400]) if lastgate else '',
        'tools_seen': sorted({t for r in reqs for t in r['tools']}),
        'skill_loaded': any('shisan-xinuo-workflow' in r['skill_in'] for r in reqs),
    }
    ex = os.path.join(a.root, 'extracts')
    os.makedirs(ex, exist_ok=True)
    json.dump(out, open(os.path.join(ex, f'{a.tag}.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(f"[{a.tag}] reqs={out['requests']} NQ5={out['nq5']} anchor_v={out['anchor_versions']} hooks={out['hooks_pack']} skill_loaded={out['skill_loaded']}")
    print(f"  restate={out['first_restate']} status={out['status_line']} frontgate={out['frontgate']} five_q={out['five_q']} step1={out['step1_output']}")
    print(f"  CoT={out['cot']}  GATE={out['gate_present']}({out['gate_fields']}/9)")
    print(f"  → {os.path.join(ex, a.tag + '.json')}")


if __name__ == '__main__':
    main()
