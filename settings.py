import pygame

class Settings:
    """To hold all the values and settings for the game."""

    def __init__(self):
        """Initializes game settings."""

        # Screen settings
        self.screen_width = 1200
        self.screen_height = 750
        self.bg_color = (120, 120, 120)

        # Ship settings
        self.ship_speed = 1.5
        self.ship_limit = 3

        # Bullet settings
        self.bullet_speed = 5.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (100, 150, 255)
        self.bullet_bg = (250, 250, 255)
        self.bullet_limit = 3

        # Font settings
        self.font = pygame.font.SysFont("Ubuntu Mono, Regular", 16)

        # Alien settings
        self.alien_speed = 1.0
        self.drop_down_speed = 10
        self.fleet_direction = 1
