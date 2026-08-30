#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
shisan-xinuo-workflow sync-skill 三路合并更新器（v2.0 · 单版本中文主交付物）
协议（用户拍板 2026-08-30）：
- user-notes/（用户规则目录）与 memory/（skill 自身落盘）与 *.bak-* 永不碰；
- 上游（源库 skill/，唯一中文版本）整体覆盖：SKILL.md / references/* / templates/*；
- 副本内非源库文件（如 references/personal-playbook.md）→ 一次性迁移进 user-notes/；
- 每次更新：体检 diff → 备份 .bak-<ts> → 合并 → 变更清单（stdout + 两份 task-log）。

v2.0 修复（实测驱动）：
- 首次安装必崩修复：目标目录不存在 → 跳过备份、直接创建并全量复制（exit=0）；
- 备份路径外置修复：备份默认落 <dest 的上级父目录>/skill-backups/<name>.bak-<ts>，
  ——平台扫描路径之外；避免备份目录被平台收录为第二个同名 Skill 并选中旧版（WorkBuddy 2026-08-30 实测）；
  可用 --backup-dir 覆盖；
- 空 pass 死代码删除；dry-run break 移出 os.walk（干跑列出全部变更）；
- 输出解析到的同步路径，供按「平台加载时的 Base directory」验收。

用法：python syncer.py [--dry] [--src <path>] [--dest <path>] [--backup-dir <path>]
"""
import argparse, os, re, shutil, sys, time
from datetime import datetime

# 永不碰的顶层子目录（副本侧）；巡检/覆盖时一律跳过
KEEP_DIRS = {"user-notes", "memory"}


def log_dir(dest):
    n = os.path.join(dest, "user-notes")
    os.makedirs(n, exist_ok=True)
    return n


def keep(name):
    """是否是必须保留的目录/备份目录"""
    return name in KEEP_DIRS or ".bak-" in name


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry", action="store_true")
    REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    ap.add_argument("--src", default=os.path.join(REPO_ROOT, "skill", "shisan-xinuo-workflow"))
    ap.add_argument("--dest", default=os.path.expanduser(r"~\.agents\skills\shisan-xinuo-workflow"))
    ap.add_argument("--backup-dir", default="", help="备份目录（默认：dest 的上级父目录下 skill-backups/，位于平台扫描路径之外）")
    ap.add_argument("--memory-target", default="", help="硬注入记忆层目标文件（如 ~/.workbuddy/MEMORY.md）：把 templates/memory-anchor.md 锚点块合并写入（先备份 .bak-<ts>）；留空则不写记忆层。默认行为保持纯 skill 副本同步。")
    a = ap.parse_args()
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    fmt = datetime.now().strftime("%Y%m%d-%H%M%S")

    if not os.path.isdir(a.src):
        print(f"E: 源库不存在: {a.src}")
        return 1

    print(f"[路径] 源库 src = {os.path.abspath(a.src)}")
    print(f"[路径] 副本 dest = {os.path.abspath(a.dest)}")
    print(f"[提示] 验收请以平台加载时的 Base directory 为准，而非文件版本号（v2.0 判据）。")

    first_install = not os.path.isdir(a.dest)
    if first_install and not a.dry:
        print("[首次安装] 目标目录不存在：跳过备份，直接创建并全量复制（exit=0）。")

    is_dry = {True: "yes", False: "no"}[a.dry]

    # 1) 体检：副本中非源库文件（用户内容）
    local_files = []
    if not first_install:
        for root, dirs, fs in os.walk(a.dest):
            dirs[:] = [d for d in dirs if not keep(d)]
            rel = os.path.relpath(root, a.dest)
            for name in fs:
                r = os.path.normpath(os.path.join(rel, name)).replace("\\", "/")
                if r.startswith("user-notes/") or r.startswith("memory/") or ".bak-" in r:
                    continue
                local_files.append(r)
    user_owned = [f for f in local_files if not os.path.exists(os.path.join(a.src, f))]
    print(f"[体检] 副本中上游无对应文件（=用户/本地内容）: {user_owned or '无'}")

    # 2) 备份（外置：默认 dest 的上级父目录下的 skill-backups/，位于平台扫描路径之外）
    backup = ""
    if first_install:
        print(f"[备份] (首次安装，跳过备份)")
    else:
        if a.backup_dir:
            bdir = os.path.abspath(a.backup_dir)
        else:
            bdir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(a.dest))), "skill-backups")
        backup = os.path.join(bdir, os.path.basename(a.dest.rstrip("/\\")) + f".bak-{fmt}")
        if not a.dry:
            os.makedirs(bdir, exist_ok=True)
            if os.path.exists(backup):
                print(f"[备份] (已存在，跳过) {backup}")
            else:
                shutil.copytree(a.dest, backup)
                print(f"[备份] {backup}")
        else:
            print(f"[备份] (dry) {backup}")

    # 3) 迁移 personal-playbook 等 → user-notes/
    migrated = []
    for f in user_owned:
        if not f:
            continue
        target = os.path.join(log_dir(a.dest), os.path.basename(f))
        if not a.dry and os.path.exists(os.path.join(a.dest, f)):
            shutil.move(os.path.join(a.dest, f), target)
        migrated.append(f"{f} -> user-notes/{os.path.basename(f)}")
    print(f"[迁移] {migrated or '无'}")

    # 4) 上游覆盖（排除 user-notes/memory/.bak；dry 模式只列变更不写盘）
    changed = []
    for root, dirs, fs in os.walk(a.src):
        dirs[:] = [d for d in dirs if not keep(d)]
        rel = os.path.relpath(root, a.src)
        for name in fs:
            sfile = os.path.join(root, name)
            dfile = os.path.join(a.dest, rel, name) if rel != "." else os.path.join(a.dest, name)
            if not os.path.exists(dfile):
                changed.append(f"+ {os.path.relpath(dfile, a.dest)}")
            elif open(sfile, "rb").read() != open(dfile, "rb").read():
                changed.append(f"~ {os.path.relpath(dfile, a.dest)}")
            if not a.dry:
                os.makedirs(os.path.dirname(dfile) or a.dest, exist_ok=True)
                shutil.copy2(sfile, dfile)

    # 5) 变更清单
    if first_install and not a.dry and not changed:
        changed = ["首次安装全量复制（详见 src=skill/）"]

    # 5.5) 记忆层同步（可选：--memory-target 显式指定平台记忆文件；硬注入第三层）
    mem_note = ""
    if a.memory_target:
        anchor = os.path.join(a.src, "templates", "memory-anchor.md")
        if not os.path.isfile(anchor):
            print(f"E: 源缺少 templates/memory-anchor.md: {anchor}")
            return 1
        # 提取模板中代码块内的锚点正文（首行为在场提示），避免模板头部注释落入记忆文件
        txt = open(anchor, encoding="utf-8").read()
        m = re.search(r"```markdown\r?\n(.*?)\r?\n```", txt, re.S)
        body = m.group(1) if m else txt
        mem_ts = datetime.now().strftime("%Y%m%d-%H%M%S")
        mem_bak = a.memory_target + f".bak-{mem_ts}"
        mem_prev = ""
        if os.path.exists(a.memory_target):
            if not a.dry:
                shutil.copy2(a.memory_target, mem_bak)
            mem_prev = open(a.memory_target, encoding="utf-8").read()
        sep = "\n\n---\n" if mem_prev.strip() else ""
        mem_new = mem_prev.rstrip() + sep + body
        changed.append(f"~ 记忆层@{os.path.abspath(a.memory_target)}（锚点块合并" + ("，dry" if a.dry else f"，备份 {os.path.basename(mem_bak)}") + "）")
        mem_note = f"\n## 记忆层（hard-inject 第 3 层）\n- {os.path.abspath(a.memory_target)} ← templates/memory-anchor.md\n- 在场提示首行：工作流 Skill 现已在场"
        if not a.dry:
            open(a.memory_target, "w", encoding="utf-8").write(mem_new)
            print(f"[记忆] 已合并锚点块 → {a.memory_target}（备份 {mem_bak}）")
        else:
            print(f"[记忆] (dry) 将合并锚点块 → {a.memory_target}")

    lines = [f"# sync-skill {ts}", "",
             "## 上游变更", *[f"- {c}" for c in changed or ["(dry) 无变更"]],
             mem_note,
             "", "## 保留本地（user-notes/ 等未动）", "- user-notes/ (含迁移件)", "- memory/ (skill 自身 task-log)", "- .bak-*"]
    out = "\n".join(lines)
    if not a.dry:
        syncfile = os.path.join(log_dir(a.dest), f"sync-log-{fmt}.md")
        open(syncfile, "w", encoding="utf-8").write(out)
        # 源库侧：仓库根 = <src> 上两级；副本侧：DEST/memory (skill 自身落盘区)
        repo = os.path.abspath(os.path.join(a.src, "..", ".."))
        srclog = os.path.join(repo, "memory", "task-log")
        os.makedirs(srclog, exist_ok=True)
        open(os.path.join(srclog, f"skill-update-{fmt}.md"), "w", encoding="utf-8").write(out.replace("# sync-skill ", "# skill 更新 · "))
        destmem = os.path.join(a.dest, "memory", "task-log")
        os.makedirs(destmem, exist_ok=True)
        open(os.path.join(destmem, f"skill-update-{fmt}.md"), "w", encoding="utf-8").write(out.replace("# sync-skill ", "# skill 更新(副本) · "))
    print(out)
    print(f"\n[done] exit=0  (dry={is_dry})")
    print(f"[验收] 平台解析到的 Base directory 应指向：{os.path.abspath(a.dest)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
