"""Content Agent — generates post/story ideas and content."""

from base_agent import BaseAgent
import random

IDEAS = [
    "Share a behind-the-scenes story",
    "Ask users: What made you smile today?",
    "Post a motivational quote with image",
    "Highlight a trending hashtag",
    "Create a poll about weekend plans",
    "Feature user-generated content",
    "Announce a small platform update",
]


class ContentAgent(BaseAgent):
    def __init__(self, interval_seconds: int = 3600):
        super().__init__("Content", interval_seconds)
        self.ideas_generated = 0

    def run(self):
        idea = random.choice(IDEAS)
        self.ideas_generated += 1
        self.log(f"New content idea #{self.ideas_generated}: {idea}")
