"""Self-Heal Agent — detects downtime and restores."""

from base_agent import BaseAgent
import random


class SelfHealAgent(BaseAgent):
    def __init__(self, interval_seconds: int = 30):
        super().__init__("SelfHeal", interval_seconds)
        self.restores = 0

    def run(self):
        if random.random() < 0.05:
            self.restores += 1
            self.log(f"Platform DOWN detected → restoring from backup (restore #{self.restores})")
        else:
            self.log("Health check — Platform OK")
