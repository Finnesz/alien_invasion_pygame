import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Create a bullet object at the ship's current position."""

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color
        self.bg_color = self.settings.bullet_bg

        # Create a bullet rect at (0, 0) and then set corrent position.
        self.rect = pygame.FRect(0, 0, self.settings.bullet_width + 4, self.settings.bullet_height + 4)
        self.bg_rect = pygame.FRect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midbottom = ai_game.ship.rect.midtop
        self.rect.x += 1
        self.bg_rect.center = self.rect.center

    def update(self):
        self.rect.y -= self.settings.bullet_speed
        self.bg_rect.y -= self.settings.bullet_speed

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
        pygame.draw.rect(self.screen, self.bg_color, self.bg_rect)
