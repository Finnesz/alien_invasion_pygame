import pygame
from pygame.font import SysFont

class Button:
    def __init__(self, ai_game, msg):
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = self.screen.get_frect()

        self.width, self.height = 200, 50
        self.color = self.settings.palette[3]
        self.font = pygame.font.SysFont("smallfontregular", 48)
        
        self.button_color = self.settings.palette[1]
        self.rect = pygame.FRect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        self._prep_msg(msg)

    def _prep_msg(self, msg):
        # print("Button prep")
        self.font_img = self.font.render(msg, False, self.color)
        self.font_img_rect = self.font_img.get_frect()

        self.font_img_rect.center = self.rect.center
        # self.font_img_rect.centery += (self.font_img_rect.height) - 1
    
    def draw_button(self):
        """Draw button and then the text"""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.font_img, self.font_img_rect)

class TButton(Button):
    """Button with texture"""
    def __init__(self, ai_game, msg, img_dir):
        self.width, self.height = 200, 50

        self.texture_img = pygame.image.load(img_dir)
        self.texture_img = pygame.transform.scale(self.texture_img, (self.width, self.height))
        self.texture_rect = self.texture_img.get_frect()
        self.texture_rect.center = ai_game.screen.get_frect().center

        super().__init__(ai_game, msg) # had to put it here because Button class's _prep_msg does not recognize texture when initialized

    def _prep_msg(self, msg):
        # print("TButton prep")
        self.font_img = self.font.render(msg, False, self.color)
        self.font_img_rect = self.font_img.get_frect()
  
        self.font_img_rect.center = self.texture_rect.center 
        # self.font_img_rect.centery += (self.font_img_rect.height) - 1
    
    def draw_button(self):
        """Draw button and then the text"""
        self.screen.blit(self.texture_img, self.texture_rect)
        self.screen.blit(self.font_img, self.font_img_rect)