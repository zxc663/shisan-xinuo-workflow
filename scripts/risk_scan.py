# -*- coding: utf-8 -*-
"""risk_scan.py · L3 清单外高危域机检端口（细则 #370）

为什么存在：L3 封闭清单只有 6 项（可测试性靠「不扩项」换来），但真实高危操作按
影响面分布——CI/CD、DNS、IAM、计费、feature flag、webhook、限流、OAuth 回调、
生产配置写等清单外域，命中时同样必须至少按 L3 停点问询。本脚本把这条执行层枚举
变成可机检端口，避免「靠 agent 自己想起来」。

用法：
    python scripts/risk_scan.py --text "把 CI workflow 的触发条件改成 push 任意分支"
    python scripts/risk_scan.py --paths ".github/workflows/verify-release.yml,scripts/deploy_injection.py"
    echo "…" | python scripts/risk_scan.py --stdin

输出：逐域命中行 + VERDICT。
退出码：0=无候选域（可直接按常规判级）；1=有候选域（至少按 L3 停点：列动作清单→结束回合等确认）；
        2=用法错误。
边界：关键词机检是**召回端口不是判级权威**——判级权威仍是 SKILL §2.2 封闭清单；
      本脚本只负责把清单外高危域叫出来，是否真按 L3 处理由 agent 结合语义判断并留痕。
"""
import argparse
import os
import re
import sys

# 域 → 关键词（中文 + 英文形态；大小写不敏感）
DOMAINS = [
    ('CI/CD 与流水线', ['ci/cd', 'workflow', 'github actions', '流水线', '构建流水线', 'pipeline', 'deploy pipeline', 'release job']),
    ('DNS / 域名 / 证书', ['dns', '域名', 'nameserver', 'ns 记录', '证书', 'certificate', 'tls 证书', 'ssl']),
    ('IAM 与权限策略', ['iam', '权限策略', 'policy', 'role 绑定', 'rbac', 'oidc', 'service account', '最小权限调整']),
    ('计费与配额', ['billing', '计费', '账单', '配额', 'quota', '付费开关', '套餐']),
    ('生产 feature flag / 灰度', ['feature flag', '灰度', 'canary 开关', '开关切换', 'targeting rule']),
    ('第三方 webhook / 回调注册', ['webhook', '回调注册', 'callback url', '订阅端点']),
    ('限流 / 熔断阈值', ['rate limit', '限流', '熔断阈值', 'qps', '并发上限', 'quota limit']),
    ('OAuth / SSO 回调白名单', ['oauth', 'sso', 'redirect uri', '回调白名单', 'redirect_url', '授权回调']),
    ('生产配置中心写操作', ['配置中心', 'config center', 'apollo', 'nacos', '生产配置写入', '环境变量注入生产']),
]

MAX_EXCERPT = 80


def scan_chunks(chunks):
    """chunks = [(来源, 文本)]；返回 [(域, 来源, 关键词, 摘录)]。"""
    hits = []
    for src, text in chunks:
        low = (text or '').lower()
        if not low:
            continue
        for domain, keys in DOMAINS:
            for k in keys:
                if k.lower() in low:
                    m = re.search(re.escape(k.lower()), low)
                    start = max(0, (m.start() if m else 0) - 20)
                    excerpt = text[start:start + MAX_EXCERPT].replace('\n', ' ')
                    hits.append((domain, src, k, excerpt))
                    break
    return hits


def main():
    ap = argparse.ArgumentParser(description='L3 清单外高危域机检端口（细则 #370）')
    ap.add_argument('--text', default='', help='直接扫描的文本（如任务描述/改动摘要）')
    ap.add_argument('--paths', default='', help='逗号分隔的文件路径（逐个读文本扫描）')
    ap.add_argument('--stdin', action='store_true', help='从标准输入读取文本')
    a = ap.parse_args()

    chunks = []
    if a.text:
        chunks.append(('--text', a.text))
    if a.stdin:
        chunks.append(('--stdin', sys.stdin.read()))
    for p in [x.strip() for x in a.paths.split(',') if x.strip()]:
        if not os.path.exists(p):
            print('[SKIP] 路径不存在: %s' % p)
            continue
        try:
            with open(p, encoding='utf-8', errors='replace') as f:
                chunks.append((p, f.read()))
        except OSError as e:
            print('[SKIP] 读取失败 %s: %s' % (p, e))
    if not chunks:
        print('用法: python scripts/risk_scan.py --text "…" | --paths a,b | --stdin')
        return 2

    hits = scan_chunks(chunks)
    print('== risk_scan（清单外高危域机检）==')
    if not hits:
        print(' 无候选域')
        print('VERDICT: PASS（无候选域；判级仍按 SKILL §2.2 封闭清单）')
        return 0
    seen = set()
    for domain, src, key, excerpt in hits:
        line = '%s | %s | 命中「%s」| %s' % (domain, src, key, excerpt)
        if line in seen:
            continue
        seen.add(line)
        print(' [候选] ' + line)
    print('VERDICT: HIT(%d) — 命中即至少按 L3 停点：先列动作清单 → 结束回合等确认（细则 #370；清单外域）'
          % len(seen))
    return 1


if __name__ == '__main__':
    sys.exit(main())
