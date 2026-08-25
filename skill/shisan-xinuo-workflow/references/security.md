# Security & Rollback (English)

Load this file for safety red lines, secret handling, incident response, rollback procedures, and pre-publish residue scans.

## 1. Production safety red lines (6)

1. **Zero operations outside project scope.** Never delete or modify files outside the project directory (and never outside what the task authorizes). The skill folder itself is portable — when working on it, only add; do not delete or modify existing files you did not create.
2. **VCS only via git commands.** Never read/write the `.git` directory directly; operate the repository exclusively through git commands.
3. **High-risk commands use absolute paths.** `rm`, `Remove-Item`, `del` and equivalents must use explicit absolute paths for their targets; never relative paths, path variables, wildcards, or unresolved variables.
4. **One-time authorization for untracked files.** Any file not under version control: modifying or deleting it requires explicit human authorization. Authorization is valid for the current round of conversation only; historical authorization has expired.
5. **Third-party installs get a health check first.** Before installing any third-party skill, script, or dependency: static-scan for suspicious content, check combined permission paths, install with least privilege, verify in a temp directory first, and stop on clear problems. Installing less is itself a security measure.
6. **Rollback point before major changes or irreversible operations** (rule 43 — the procedure below).

## 2. Rollback-point procedure (rule 43 detail)

**When it applies:** multi-file refactors, data migrations, deletions, overwrite-style writes, schema changes, and any high-risk command.

**Git-tracked files:**
- [ ] 1. Check `git status` — worktree must be clean (or you already know what the current uncommitted state is)
- [ ] 2. Create the rollback point: `git commit` current state, or `git stash push -m "pre-<task> rollback point"`, or switch to a new branch per the concurrency rule (rule 23)
- [ ] 3. Record the rollback point (commit hash / stash id / branch name) in the task record
- [ ] 4. Only now start the change
- [ ] 5. Rollback, if needed: `git checkout <rollback hash>` / `git stash pop` / switch branch — never manually reverse-edit to "undo"

**Non-git files (configs, data, scripts outside VCS):**
- [ ] 1. Copy a snapshot first: `<file>.<date>.bak` (or a tarball of the directory)
- [ ] 2. Verify the snapshot opens / restores before proceeding
- [ ] 3. Record the snapshot path in the task record
- [ ] 4. Only now start the change

**Deployments:** prepare the rollback plan (previous artifact + restore steps) *before* releasing, and rehearse restore during the observation window if feasible.

## 3. Secrets red line (rule 30 detail)

- Never write keys / tokens / passwords into code, committed configs, ordinary docs, or chat. Machine-only secret stores (OS keychain, platform secret managers, local-only env files excluded from VCS) are the only acceptable homes.
- Least privilege: request the minimum scope; use and stop.
- Pre-commit scan: run the project's secret scanner (`gitleaks`/`trufflehog` or equivalent) before every commit; CI must run it too.
- Leak response: (1) revoke/rotate the credential immediately; (2) map the exposure (which commits/branches/remotes contain it); (3) purge or rewrite history where required; (4) record the incident and the prevention (e.g. `.gitignore` fix, pre-commit hook).

## 4. Incident & alert response (rule 31 detail)

1. **Confirm** — is it real, what is the blast radius
2. **Classify** — severity (P0 stop-the-line → P3 cosmetic)
3. **Locate** — from logs/metrics to the offending change; worst-first with the rollback point ready
4. **Dispose** — revoke / rollback / fix; production anomalies: stop the risky surface first, then repair
5. **Review** — timeline, root cause (causal chain, rule 11), prevention items into the experience log

## 5. Pre-publish residue scan (open-source releases)

Before any public push (rule 40), scan and achieve **zero hits** on:

- Personal paths (Windows `D:\…` / `C:\Users\…`, home dirs, machine names)
- Account names / real names you do not intend to publish
- Keys and token patterns (AWS/阿里云/GitHub tokens, passwords, `.env` contents, private key blocks)
- Internal references (private repo URLs, internal service hostnames, personal knowledge-file references)
- Vendor branding you do not own the rights to re-publish

Procedure: run the scan → fix or remove every hit → re-run the scan to zero → user approval → push.