import pygame

class ShieldBlock():
    """Makes up the shields, just a bunch of squares."""
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings # for number of shields maybe?
        self.rect = pygame.FRect(0, 0, 10, 10)

    def draw(self):
        pygame.draw.rect(self.screen, self.settings.palette[3], self.rect)