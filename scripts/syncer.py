#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
shisan-xinuo-workflow sync-skill 三路合并更新器（v1.17）
协议（用户拍板 2026-08-30）：
- user-notes/（用户规则目录）与 memory/（skill 自身落盘）与 *.bak-* 永不碰；
- 上游（源库 skill/）整体覆盖：SKILL.md / references/* / templates/*；
- 副本内非源库文件（如 references/personal-playbook.md）→ 一次性迁移进 user-notes/；
- 每次更新：体检 diff → 备份 .bak-<ts> → 合并 → 变更清单（stdout + 两份 task-log）。

用法：python syncer.py [--dry] [--src <path>] [--dest <path>]
"""
import argparse, difflib, os, shutil, sys, time
from datetime import datetime

SIBLINGS_EXCLUDE = {"user-notes", "memory", "templates"}  # templates 在源库有,覆盖;memory 覆盖不到(DES 无)

def log_dir(dest):
    n = os.path.join(dest, "user-notes")
    os.makedirs(n, exist_ok=True)
    return n

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry", action="store_true")
    REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    ap.add_argument("--src", default=os.path.join(REPO_ROOT, "skill", "shisan-xinuo-workflow"))
    ap.add_argument("--dest", default=os.path.expanduser(r"~\.agents\skills\shisan-xinuo-workflow"))
    a = ap.parse_args()
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    fmt = datetime.now().strftime("%Y%m%d-%H%M%S")

    # 1) 体检：副本中非源库文件（用户内容）
    local_files = []
    for root, dirs, fs in os.walk(a.dest):
        rel = os.path.relpath(root, a.dest)
        for name in fs:
            r = os.path.normpath(os.path.join(rel, name)).replace("\\", "/")
            if r.startswith("user-notes/") or r.startswith("memory/") or ".bak-" in r:
                continue
            local_files.append(r)
    user_owned = [f for f in local_files if not os.path.exists(os.path.join(a.src, f))]
    print(f"[体检] 副本中上游无对应文件（=用户/本地内容）: {user_owned or '无'}")

    # 2) 备份
    backup = a.dest.rstrip("/\\") + f".bak-{fmt}"
    if not a.dry and not os.path.exists(backup):
        shutil.copytree(a.dest, backup)
        print(f"[备份] {backup}")
    else:
        print(f"[备份] (dry|已存在) {backup if a.dry else 'skip'}")

    # 3) 迁移 personal-playbook 等 → user-notes/
    migrated = []
    for f in user_owned:
        if not f:
            continue
        target = os.path.join(log_dir(a.dest), os.path.basename(f))
        if not a.dry:
            shutil.move(os.path.join(a.dest, f), target)
        migrated.append(f"{f} -> user-notes/{os.path.basename(f)}")
        # 同步删掉源库侧同名(不存在则无事)
        srcsame = os.path.join(a.src, f)
        if not os.path.exists(srcsame):
            pass
    print(f"[迁移] {migrated or '无'}")

    # 4) 上游覆盖（排除 user-notes/memory/.bak）
    changed = []
    for root, dirs, fs in os.walk(a.src):
        rel = os.path.relpath(root, a.src)
        if a.dry:
            break
        for d in list(dirs):
            if d in {"user-notes", "memory"}:
                dirs.remove(d)
        for name in fs:
            sfile = os.path.join(root, name)
            dfile = os.path.join(a.dest, rel, name) if rel != "." else os.path.join(a.dest, name)
            os.makedirs(os.path.dirname(dfile) or a.dest, exist_ok=True)
            if not os.path.exists(dfile):
                changed.append(f"+ {os.path.relpath(dfile, a.dest)}")
            elif open(sfile, "rb").read() != open(dfile, "rb").read():
                changed.append(f"~ {os.path.relpath(dfile, a.dest)}")
            shutil.copy2(sfile, dfile)

    # 5) 变更清单
    lines = [f"# sync-skill {ts}", "", "## 上游变更", *[f"- {c}" for c in changed or ["(dry) 无列示"]],
             "", "## 保留本地（user-notes/ 等未动）", "- user-notes/ (含迁移件)", "- memory/ (skill 自身 task-log)", "- .bak-*"]
    out = "\n".join(lines)
    if not a.dry:
        syncfile = os.path.join(log_dir(a.dest), f"sync-log-{fmt}.md")
        open(syncfile, "w", encoding="utf-8").write(out)
        # 源库侧：仓库根 = <src> 上两级；副本侧：DEST/memory (skill 自身落盘区, v1.17 G5)
        repo = os.path.abspath(os.path.join(a.src, "..", ".."))
        srclog = os.path.join(repo, "memory", "task-log")
        os.makedirs(srclog, exist_ok=True)
        open(os.path.join(srclog, f"skill-update-{fmt}.md"), "w", encoding="utf-8").write(out.replace("# sync-skill ", "# skill 更新 · "))
        destmem = os.path.join(a.dest, "memory", "task-log")
        os.makedirs(destmem, exist_ok=True)
        open(os.path.join(destmem, f"skill-update-{fmt}.md"), "w", encoding="utf-8").write(out.replace("# sync-skill ", "# skill 更新(副本) · "))
    print(out)
    print(f"\n[done] exit=0  (dry={a.dry})")
    return 0

if __name__ == "__main__":
    sys.exit(main())
