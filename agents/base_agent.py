"""
Base Agent for Snaply AI-OS
All agents inherit from this class.
"""

import time
import logging
from abc import ABC, abstractmethod
from datetime import datetime
from pathlib import Path

LOG_DIR = Path(__file__).parent.parent / "logs"
LOG_DIR.mkdir(exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(name)s | %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler(LOG_DIR / "snaply_ai_os.log", encoding="utf-8"),
    ],
)


class BaseAgent(ABC):
    def __init__(self, name: str, interval_seconds: int = 60):
        self.name = name
        self.interval = interval_seconds
        self.running = False
        self.last_run = None
        self.run_count = 0
        self.logger = logging.getLogger(name)

    def log(self, msg: str):
        self.logger.info(msg)

    def start(self):
        self.running = True
        self.log(f"{self.name} started (interval={self.interval}s)")

    def stop(self):
        self.running = False
        self.log(f"{self.name} stopped")

    def should_run(self) -> bool:
        if not self.running:
            return False
        if self.last_run is None:
            return True
        return (time.time() - self.last_run) >= self.interval

    def tick(self):
        if self.should_run():
            try:
                self.run()
                self.last_run = time.time()
                self.run_count += 1
            except Exception as e:
                self.log(f"ERROR: {e}")

    @abstractmethod
    def run(self):
        pass

    def status(self) -> dict:
        return {
            "name": self.name,
            "running": self.running,
            "run_count": self.run_count,
            "last_run": datetime.fromtimestamp(self.last_run).isoformat() if self.last_run else None,
            "interval": self.interval,
        }
