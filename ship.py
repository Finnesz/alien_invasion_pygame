import pygame

class Ship:
    """A class to manage the ship."""

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get its rect
        self.image = pygame.image.load("images/ship_008.png")
        self.image = pygame.transform.scale(self.image, (65, 65))
        self.rect = self.image.get_frect()  # gets the float values of rect instead of int

        # Start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        # Is the player moving to the right/left? (Movement flag)
        self.moving_right = False
        self.moving_left = False

        # Maybe add a dt attribute for independent frame movement

    def center_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom

    def update(self):
        """For handling player/ship movement, etc..."""
        # Move to the right if moving_right is true
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > self.screen_rect.left: # or self.rect.left > 0 but I prefer this because it make sense
            self.rect.x -= self.settings.ship_speed

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
