from pathlib import Path

class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.reset_stats()
        self.level = 1

        self.high_score_path = Path("high_score.txt")
        high_score_content = self.high_score_path.read_text()
        try:
            self.high_score = int(high_score_content)
        except:
            self.high_score = 0

    def reset_stats(self):
        """Initialize stats that can change during game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
