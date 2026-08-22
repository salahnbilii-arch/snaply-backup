"""Telegram Agent — sends reports and alerts to admin."""

from base_agent import BaseAgent
from datetime import datetime


class TelegramAgent(BaseAgent):
    def __init__(self, interval_seconds: int = 3600):
        super().__init__("Telegram", interval_seconds)
        self.reports_sent = 0

    def run(self):
        self.reports_sent += 1
        now = datetime.now().strftime("%Y-%m-%d %H:%M")
        self.log(f"Hourly report #{self.reports_sent} sent to admin Telegram ({now}) — mock")
