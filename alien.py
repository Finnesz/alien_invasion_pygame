import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self, ai_game):
        super().__init__()

        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # alien image and rect
        self.image = pygame.image.load("images/enemy.png")
        self.image = pygame.transform.scale(self.image, (60, 60))
        # self.image = pygame.transform.rotate(self.image, 180)
        self.rect = self.image.get_frect()

        # placement for alien
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        # print(f"Width: {self.rect.width} Height: {self.rect.height}")

    def check_edges(self):
        screen_rect = self.screen.get_frect()
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= screen_rect.left)

    def update(self):
        self.rect.x += self.settings.alien_speed * self.settings.fleet_direction