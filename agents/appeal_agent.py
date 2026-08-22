"""Appeal Agent — auto-reviews user appeals."""

from base_agent import BaseAgent
import random


class AppealAgent(BaseAgent):
    def __init__(self, interval_seconds: int = 45):
        super().__init__("Appeal", interval_seconds)
        self.reviewed = 0

    def run(self):
        if random.random() < 0.25:
            decision = random.choice(["approved", "rejected", "escalated_to_admin"])
            self.reviewed += 1
            self.log(f"Appeal reviewed → {decision} (total: {self.reviewed})")
        else:
            self.log("No new appeals")
