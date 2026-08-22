#!/usr/bin/env python3
"""
Snaply AI-OS Orchestrator v3.0.0
The brain that runs all agents 24/7.
"""

import time
import signal
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from base_agent import BaseAgent
from moderator_agent import ModeratorAgent
from security_agent import SecurityAgent
from backup_agent import BackupAgent
from email_agent import EmailAgent
from telegram_agent import TelegramAgent
from appeal_agent import AppealAgent
from self_heal_agent import SelfHealAgent
from content_agent import ContentAgent
from analytics_agent import AnalyticsAgent
from growth_agent import GrowthAgent
from support_agent import SupportAgent


class Orchestrator:
    def __init__(self):
        self.agents = []
        self.running = False

        self.agents = [
            ModeratorAgent(interval_seconds=8),
            SecurityAgent(interval_seconds=10),
            BackupAgent(interval_seconds=900),
            EmailAgent(interval_seconds=30),
            TelegramAgent(interval_seconds=3600),
            AppealAgent(interval_seconds=45),
            SelfHealAgent(interval_seconds=30),
            ContentAgent(interval_seconds=3600),
            AnalyticsAgent(interval_seconds=3600),
            GrowthAgent(interval_seconds=7200),
            SupportAgent(interval_seconds=20),
        ]

    def start(self):
        print("=" * 60)
        print("  Snaply AI-OS v3.0.0 — Starting...")
        print("  Mode: Mock (free, no API keys required)")
        print("  Agents:", len(self.agents))
        print("=" * 60)

        for agent in self.agents:
            agent.start()

        self.running = True
        print("\nAll agents online. Press Ctrl+C to stop.\n")

        try:
            while self.running:
                for agent in self.agents:
                    agent.tick()
                time.sleep(2)
        except KeyboardInterrupt:
            self.stop()

    def stop(self):
        print("\nShutting down Snaply AI-OS...")
        self.running = False
        for agent in self.agents:
            agent.stop()
        print("All agents stopped. Goodbye.")

    def status(self):
        print("\n--- Agent Status ---")
        for agent in self.agents:
            s = agent.status()
            print(f"  {s['name']:12} | runs: {s['run_count']:4} | last: {s['last_run']}")


def main():
    orch = Orchestrator()

    def handle_signal(sig, frame):
        orch.stop()
        sys.exit(0)

    signal.signal(signal.SIGINT, handle_signal)
    signal.signal(signal.SIGTERM, handle_signal)

    orch.start()


if __name__ == "__main__":
    main()
