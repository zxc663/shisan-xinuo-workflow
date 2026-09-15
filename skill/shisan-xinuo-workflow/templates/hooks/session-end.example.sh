#!/bin/bash
# shisan-xinuo-workflow · session-end banner (EXAMPLE — copy & adapt)
# Purpose: re-anchor the agent's closing responsibilities when a session ends.
# Used by hooks.example.json (Claude Code SessionEnd). Optional & platform-gated.

echo "=== shisan-xinuo-workflow · SESSION END — WRAP-UP ==="
echo ""
echo "1. Final verification + honest self-check: label every result DONE vs TODO/UNVERIFIED — never fake completion."
echo "2. Record the session: one line in memory/agent-log.md flow log (change | verification(result) | unverified items)."
echo "3. Sync workspace memory: memory/agent-log.md four sections (status / lessons / preferences / flow)."
echo "4. Secrets red line: do NOT read / write / echo tokens, keys or credentials here or anywhere (no exfil)."
echo "5. Destructive ops: only after an explicit rollback point + user confirmation; record the rollback note."
echo "6. Cleanup (temp files / background jobs), if any: do it EXPLICITLY and only where confirmed safe — never auto-delete."
echo "Full closing rules: see the shisan-xinuo-workflow skill (rules.md / retrospective-template.md)."
echo "==========================================================="