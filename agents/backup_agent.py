"""Backup Agent — periodic backups."""

from base_agent import BaseAgent
from datetime import datetime


class BackupAgent(BaseAgent):
    def __init__(self, interval_seconds: int = 900):
        super().__init__("Backup", interval_seconds)
        self.backup_count = 0

    def run(self):
        self.backup_count += 1
        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.log(f"Backup #{self.backup_count} completed → snaply_backup_{ts}.zip (mock)")
