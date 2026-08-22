"""Support Agent — handles common user questions."""

from base_agent import BaseAgent
import random


class SupportAgent(BaseAgent):
    def __init__(self, interval_seconds: int = 20):
        super().__init__("Support", interval_seconds)
        self.handled = 0

    def run(self):
        if random.random() < 0.4:
            questions = [
                "How do I reset my password?",
                "Why was my post removed?",
                "How to change privacy settings?",
                "How to appeal a ban?",
                "How to delete my account?",
            ]
            q = random.choice(questions)
            self.handled += 1
            self.log(f"Handled support ticket: '{q}' (total: {self.handled})")
        else:
            self.log("No new support tickets")
