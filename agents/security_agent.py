"""Security Agent — monitors logins and attacks."""

from base_agent import BaseAgent
import random


class SecurityAgent(BaseAgent):
    def __init__(self, interval_seconds: int = 10):
        super().__init__("Security", interval_seconds)
        self.blocked = 0

    def run(self):
        events = random.randint(0, 5)
        if events > 3:
            self.blocked += 1
            self.log(f"Suspicious activity detected → blocked attempt (total blocked: {self.blocked})")
        else:
            self.log("Security check OK — no threats")
