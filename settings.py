import pygame
from enums import Difficulty


class Settings:
    """To hold all the values and settings for the game."""

    def __init__(self):
        """Initializes game settings."""
        # Color palette
        self.colors = [
                        "#0e0f56", "#c13e72", "#43b1e0", "#d9c9cd",
                      ]
        self.palette = []

        for color in self.colors:
            # print(color)
            self.palette.append(pygame.Color(color))

        # Screen settings
        self.screen_width = 1200
        self.screen_height = 750
        self.bg_color = self.palette[0]

        # Ship settings
        self.ship_limit = 3

        # Bullet settings
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color = self.palette[2]
        self.bullet_bg = self.palette[2]
        self.bullet_limit = 3

        # Font settings
        self.font = pygame.font.SysFont("Noto Sans", 16)
        self.difficulty_text = {}
        self.difficulty_text_pos = {}

        for difficulty, label in [
            (Difficulty.EASY, "EASY"),
            (Difficulty.MEDIUM, "MEDIUM"),
            (Difficulty.HARD, "HARD"),
        ]:
            text = self.font.render(label, False, self.palette[3])
            self.difficulty_text[difficulty] = text
            pos = self.screen_width / 2 - text.get_width() / 2
            self.difficulty_text_pos[difficulty] = (pos, 10)            

        # Alien settings
        self.drop_down_speed = 10

        # How quickly the game speeds up
        self.speedup_scale = 1.1
        # How quickly the alien point values increase
        self.score_scale = 1.5
        self.set_difficulty = Difficulty.EASY # default is easy

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        match self.set_difficulty:
            case Difficulty.EASY: 
                self.ship_speed = 1.5
                self.bullet_speed = 2.5
                self.alien_speed = 1.0
            case Difficulty.MEDIUM:
                self.ship_speed = 2.1
                self.bullet_speed = 3.1
                self.alien_speed = 2.6
            case Difficulty.HARD:
                self.ship_speed = 2.4
                self.bullet_speed = 3.4
                self.alien_speed = 3.9

        self.alien_points = 50
        self.fleet_direction = 1 # fleet direction of 1 represents right; -1 represents left.
        
    def increase_speed(self):
        """Increase speed settings."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
