# 🤖 Snaply AI-OS v2.0.0

**The Self-Running AI Brain of Snaply Platform**

---

## What This Is

Snaply AI-OS is the 24/7 autonomous operating system that runs Snaply.

It handles:
- Content moderation (AI scans every post, comment, story)
- User appeals (automated review, Tier 1-3)
- Email delivery (all 13 email types)
- Security monitoring (login attacks, threats)
- Continuous backup (every 15 minutes)
- Self-healing (auto-restore if platform goes down)
- Telegram alerts (hourly reports)
- Admin panel (your secret control center)

---

## 8 AI Agents Working Together

| Agent | Role | Interval |
|---|---|---|
| Moderator Agent | Scans all content, removes violations | Every 5s |
| Security Agent | Blocks attacks, monitors logins | Continuous |
| Backup Agent | Saves everything to 4 locations | Every 15 min |
| Email Agent | Sends all 13 email types | On trigger |
| Telegram Agent | Sends reports and alerts | Hourly |
| Appeal Agent | Auto-reviews Tier 1-2 appeals | On submission |
| Self-Heal Agent | Detects failure, restores instantly | Every 30s |
| Orchestrator | Runs all agents, never stops | Forever |

---

## If Platform Goes Down

1. Self-Heal detects DOWN in 30 seconds
2. Auto-restores from latest backup
3. Platform back online in under 2 minutes
4. Telegram alert sent

**Zero data loss. Zero downtime.**

---

## How to Start

```bash
cd snaply-ai-os/agents
./orchestrator.sh    # Runs forever
```

---

&copy; 2026 Snaply AI-OS