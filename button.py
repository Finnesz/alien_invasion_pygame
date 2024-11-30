import pygame.font

class Button:
    def __init__(self, ai_game, msg, bg_color=None, texture=None):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_frect()

        self.width, self.height = 200, 50
        self.color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)
        
        if bg_color:
            self.bg_color = bg_color
            self.rect = pygame.FRect(0, 0, self.width, self.height)
            self.rect.center = self.screen_rect.center
        elif texture:
            self.texture = pygame.image.load(texture)
            self.texture = pygame.transform.scale(self.texture, (self.width, self.height))
            self.texture_rect = self.texture.get_frect()
            self.texture_rect.center = self.screen_rect.center

        self._prep_msg(msg)

    def _prep_msg(self, msg):
        self.font_img = self.font.render(msg, True, self.color)