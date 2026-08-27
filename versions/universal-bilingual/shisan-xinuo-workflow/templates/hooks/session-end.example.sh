#!/bin/bash
# shisan-xinuo-workflow · session-end banner (EXAMPLE — copy & adapt)
# Purpose: re-anchor the agent's closing responsibilities when a session ends.
# Used by hooks.example.json (Claude Code SessionEnd). Optional & platform-gated.

echo "=== shisan-xinuo-workflow · SESSION END — WRAP-UP ==="
echo ""
echo "1. Final verification + honest self-check: label every result DONE vs TODO/UNVERIFIED — never fake completion."
echo "2. Record the session: memory/task-log/<YYYY-MM-DD>-<name>.md  (understanding -> acceptance -> decision -> result)."
echo "3. Sync workspace memory: state.md / experience.md / preferences.md under the project memory dir."
echo "4. Secrets red line: do NOT read / write / echo tokens, keys or credentials here or anywhere (no exfil)."
echo "5. Destructive ops: only after an explicit rollback point + user confirmation; record the rollback note."
echo "6. Cleanup (temp files / background jobs), if any: do it EXPLICITLY and only where confirmed safe — never auto-delete."
echo "Full closing rules: see the shisan-xinuo-workflow skill (rules.md / retrospective-template.md)."
echo "==========================================================="