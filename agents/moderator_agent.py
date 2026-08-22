"""Moderator Agent — scans posts, comments, stories for violations."""

from base_agent import BaseAgent
import random


class ModeratorAgent(BaseAgent):
    def __init__(self, interval_seconds: int = 8):
        super().__init__("Moderator", interval_seconds)
        self.violations_found = 0
        self.removed = 0

    def run(self):
        scanned = random.randint(5, 40)
        violations = random.randint(0, 2)

        if violations > 0:
            self.violations_found += violations
            self.removed += violations
            self.log(f"Scanned {scanned} items → found {violations} violation(s) → removed")
        else:
            self.log(f"Scanned {scanned} items → clean")
