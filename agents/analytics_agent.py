"""Analytics Agent — engagement and stats reports."""

from base_agent import BaseAgent
import random


class AnalyticsAgent(BaseAgent):
    def __init__(self, interval_seconds: int = 3600):
        super().__init__("Analytics", interval_seconds)

    def run(self):
        posts = random.randint(10, 200)
        likes = random.randint(50, 2000)
        comments = random.randint(5, 300)
        new_users = random.randint(0, 40)
        self.log(
            f"Stats → Posts: {posts} | Likes: {likes} | Comments: {comments} | New users: {new_users}"
        )
