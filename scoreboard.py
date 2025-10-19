import pygame.font
from pygame.sprite import Group
from ship import Ship

class ScoreBoard:
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen_rect
        self.settings = ai_game.settings
        self.stats = ai_game.stats
        self.ai_game = ai_game

        self.text_color = self.settings.palette[3]
        self.font = self.settings.font

        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        rounded_score = round(self.stats.score, -1)
        score_str = f"{rounded_score:,}"
        self.score_img = self.font.render(score_str, False, self.text_color, self.settings.palette[0])

        self.score_rect = self.score_img.get_frect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.bottom = self.screen_rect.bottom - 10

    def prep_high_score(self):
        high_score = round(self.stats.high_score, -1)
        high_score_str = f"{high_score:,}"
        self.high_score_img = self.font.render(high_score_str, False, self.text_color, self.settings.palette[0])

        self.high_score_rect = self.high_score_img.get_frect()
        self.high_score_rect.right = self.screen_rect.right - 20
        self.high_score_rect.top = self.screen_rect.top + 10

    def prep_level(self):
        level_str = str(self.stats.level)
        self.level_img = self.font.render(f"Level {level_str}", False, self.text_color, self.settings.palette[0])
        
        self.level_rect = self.level_img.get_frect()
        self.level_rect.bottom = self.screen_rect.bottom - 10
        self.level_rect.left = self.screen_rect.right - 150

    def prep_ships(self):
        self.ships = Group()
        for life in range(self.stats.ships_left):
            ship = Ship(self.ai_game)
            ship.image = pygame.transform.scale(ship.image, (32, 32))
            ship.rect.x = 10 + life * ship.rect.width
            ship.rect.y = self.screen_rect.bottom - 42
            self.ships.add(ship)

    def check_high_score(self):
        if self.stats.score > self.stats.high_score:
            self.stats.high_score_path.write_text(str(self.stats.score))
            self.stats.high_score = self.stats.score
            self.prep_high_score()

    def show_score(self):
        self.screen.blit(self.score_img, self.score_rect)
        self.screen.blit(self.high_score_img, self.high_score_rect)
        self.screen.blit(self.level_img, self.level_rect)
        self.ships.draw(self.screen)
