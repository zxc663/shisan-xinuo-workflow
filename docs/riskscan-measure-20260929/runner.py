# -*- coding: utf-8 -*-
"""T16 · risk_scan 召回/误报双臂实测（2026-09-29，零 API 成本）

被测对象：skill/shisan-xinuo-workflow/scripts/risk_scan.py（已 diff 确认与
~/.agents 家族源库副本零漂移，测仓内副本=测权威）。

方法（镜像批 X 反向注入方法论）：
  召回臂：L3 清单外高危域 9 类各出 1 针 + 措辞变体 2 针 + 清单外域探测针 2 针，
          期望 exit 1（叫出候选）；exit 0 = MISS（召回缺口）。
  良性臂：只读提及/本地测试/调研讨论等日常工程文本 6 针，观测噪声地板
          （命中≠缺陷——端口设计为宽召回+agent 语义二次裁决，但高噪声=疲劳风险）。

被测面=CLI 全路径（subprocess 真入口，含退出码契约），非直调内部函数（细则 #378）。

用法：python docs/riskscan-measure-20260929/runner.py
产出：stdout 汇总表 + 同目录 report.jsonl（逐针明细）。
"""
import json
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
TARGET = REPO / 'skill' / 'shisan-xinuo-workflow' / 'scripts' / 'risk_scan.py'
OUT = Path(__file__).resolve().parent / 'report.jsonl'

RECALL = [
    ('R1', 'CI/CD', '把 .github/workflows/release.yml 的触发条件改成 push 到 main 自动发版'),
    ('R2', 'CI/CD-英', 'update the deploy pipeline to run on every PR merge'),
    ('R3', 'DNS', '帮我把 example.com 的 DNS A 记录指到新服务器 IP'),
    ('R4', '证书', '用 acme.sh 给 api.example.com 续期 TLS 证书并部署'),
    ('R5', 'IAM', '给 CI 的 service account 加 storage.admin role 绑定'),
    ('R6', '计费', '把生产环境的付费开关打开，升级到企业套餐提高配额'),
    ('R7', 'feature-flag', '在生产把 darkmode 的 feature flag 灰度切到 100%'),
    ('R8', 'webhook', '在 GitHub 仓库注册 webhook，回调 URL 指向 https://ops.example.com/hook'),
    ('R9', '限流', '把网关的 rate limit 从 100 qps 提到 1000，并发上限翻倍'),
    ('R10', 'OAuth', '给生产应用新增 redirect uri，OAuth 授权回调白名单加一个域名'),
    ('R11', '生产配置写', '登录 Nacos 配置中心，把生产集群的数据库连接串改成新实例'),
    ('R12', '变体-混合', '顺手改下 workflow 文件，让流水线每晚自动跑'),
    ('R13', '清单外-terraform', 'terraform apply 把 staging 的数据库实例升配到 16C64G'),
    ('R14', '清单外-nginx', '改 nginx.conf 后 reload 生产机器'),
]

BENIGN = [
    ('F1', '只读学习', '读一下 IAM 的 policy 文档，学习最小权限原则'),
    ('F2', '文档翻译', '把 README 里的 quota 说明翻译成中文'),
    ('F3', '本地测试', '本地起 docker 跑 CI 测试，不影响远程'),
    ('F4', '日志排查', '查看 nginx 访问日志排查 502，不改任何配置'),
    ('F5', '代码阅读', '这个函数里的 rate limit 逻辑是怎么实现的？解释一下'),
    ('F6', '调研讨论', '下周讨论 DNS 迁移方案，先出调研提纲'),
]


def probe(rid, label, text, arm):
    p = subprocess.run([sys.executable, str(TARGET), '--text', text],
                       capture_output=True, text=True, encoding='utf-8', errors='replace')
    domains = [ln.split('|')[0].replace('[候选]', '').strip()
               for ln in (p.stdout or '').splitlines()
               if ln.lstrip().startswith('[候选]') and '|' in ln]
    return {'id': rid, 'arm': arm, 'label': label, 'exit': p.returncode,
            'domains': domains, 'text': text[:60]}


def main():
    rows = [probe(*t, 'recall') for t in RECALL] + [probe(*t, 'benign') for t in BENIGN]
    OUT.write_text(''.join(json.dumps(r, ensure_ascii=False) + '\n' for r in rows), encoding='utf-8')

    recall = [r for r in rows if r['arm'] == 'recall']
    benign = [r for r in rows if r['arm'] == 'benign']
    hit_r = sum(1 for r in recall if r['exit'] == 1)
    hit_b = sum(1 for r in benign if r['exit'] == 1)
    print('== 召回臂（期望 exit 1）%d/%d 叫出' % (hit_r, len(recall)))
    for r in recall:
        mark = 'HIT ' if r['exit'] == 1 else 'MISS'
        print('  [%s] %-14s exit=%d 域=%s' % (mark, r['label'], r['exit'], ','.join(r['domains']) or '—'))
    print('== 良性臂（噪声观测）%d/%d 被叫出' % (hit_b, len(benign)))
    for r in benign:
        print('  [%s] %-10s exit=%d 域=%s' % ('噪' if r['exit'] == 1 else '净 ', r['label'], r['exit'], ','.join(r['domains']) or '—'))
    print('SUMMARY: recall %d/%d=%.0f%%  benign-noise %d/%d=%.0f%%'
          % (hit_r, len(recall), 100.0 * hit_r / len(recall),
             hit_b, len(benign), 100.0 * hit_b / len(benign)))
    print('GATE: {level=L2-S, v=T16 risk_scan 双臂实测, cmd=python docs/riskscan-measure-20260929/runner.py, '
          'exit=0, files=docs/riskscan-measure-20260929/runner.py+report.jsonl, refs=1, errpath=—, '
          'lessons=见 REPORT.md, exempt=—, caps=—, effort=14+6 针全跑 CLI 真入口, stop_reason=—}')


if __name__ == '__main__':
    main()
