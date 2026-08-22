"""Email Agent — handles outbound emails."""

from base_agent import BaseAgent
import random


class EmailAgent(BaseAgent):
    def __init__(self, interval_seconds: int = 30):
        super().__init__("Email", interval_seconds)
        self.sent = 0

    def run(self):
        if random.random() < 0.3:
            types = ["welcome", "ban_notice", "appeal_result", "password_reset", "weekly_digest"]
            email_type = random.choice(types)
            self.sent += 1
            self.log(f"Sent '{email_type}' email (total sent: {self.sent})")
        else:
            self.log("No pending emails")
