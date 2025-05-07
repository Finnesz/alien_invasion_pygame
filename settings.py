import pygame

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
        self.ship_speed = 1.5
        self.ship_limit = 3

        # Bullet settings
        self.bullet_speed = 5.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = self.palette[1]
        self.bullet_bg = self.palette[1]
        self.bullet_limit = 3

        # Font settings
        self.font = pygame.font.SysFont("smallfontregular", 16)
        # print(pygame.font.get_fonts())

        # Alien settings
        self.alien_speed = 1.0
        self.drop_down_speed = 10
        self.fleet_direction = 1