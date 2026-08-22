"""Growth Agent — suggests growth actions and monitors trends."""

from base_agent import BaseAgent
import random

SUGGESTIONS = [
    "Encourage users to invite 3 friends this week",
    "Create a weekly challenge with rewards",
    "Boost top 3 posts of the day",
    "Add a 'Trending in your city' section",
    "Run a hashtag contest",
    "Partner with micro-influencers",
]


class GrowthAgent(BaseAgent):
    def __init__(self, interval_seconds: int = 7200):
        super().__init__("Growth", interval_seconds)

    def run(self):
        suggestion = random.choice(SUGGESTIONS)
        self.log(f"Growth suggestion: {suggestion}")
