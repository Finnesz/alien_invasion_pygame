import sys
import pygame
from time import sleep

from settings import Settings
from game_stats import GameStats
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, ad create game resources."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.stats = GameStats(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

        # Start alien invasion in an inactive state.
        self.game_active = False

    def run_game(self):
        """Start the main game loop for the game."""
        while True:
            self._check_events()

            if self.game_active:
                self.ship.update()
                self._update_bullet()
                self._update_aliens()

            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullet_limit:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullet(self):
        self.bullets.update()

        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        self._bullet_alien_collision()

    def _bullet_alien_collision(self):
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

        if not self.aliens:
            # Destroy existing bullets
            self.bullets.empty()
            self._create_fleet()

    def _create_fleet(self):
        alien = Alien(self)
        alien_width = alien.rect.width
        alien_height = alien.rect.height

        current_x = alien.rect.x + (alien_width/2)
        current_y = alien.rect.y

        while current_y < (self.settings.screen_height - (6 * alien_height)):
            while current_x < (self.settings.screen_width - alien_width):
                self._create_alien(current_x, current_y)
                current_x += alien_width * 2

            current_x = alien.rect.x + (alien_width/2)
            current_y += alien_height * 2

    def _create_alien(self, x_position, y_position):
        new_alien = Alien(self)
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)

    def _check_fleet_edge(self):
        """Checks if an alien is hitting the (left/right) edge of the screen."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _check_aliens_bottom(self):
        """Check if one of the aliens hit the bottom of the screen."""
        for alien in self.aliens:
            if alien.rect.bottom >= self.settings.screen_height:
                self._ship_hit()
                break

    def _change_fleet_direction(self):
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.drop_down_speed
        self.settings.fleet_direction *= -1

    def _ship_hit(self):
        """When the ship is hit make the player try again."""
        # Lose one life
        if self.stats.ships_left > 0:
            self.stats.ships_left -= 1

            # Remove the bullets and aliens
            self.bullets.empty()
            self.aliens.empty()

            # Reposition the assets
            self._create_fleet()
            self.ship.center_ship()

            # Pause
            sleep(0.5)
        else:
            self.game_active = False

    def _update_aliens(self):
        """Update alien movement."""
        self._check_fleet_edge()
        self.aliens.update()

        # Look for aliens hitting the ship
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        # Look for aliens hitting the bottom of the ship
        self._check_aliens_bottom()

    def _update_screen(self):
        """Update images on screen, and flip to the new screen."""
        # Redraw the screen during each pass through the loop
        self.screen.fill(self.settings.bg_color)

        self.screen.blit(self.settings.font.render(f"{self.clock.get_fps():.0f}", True, (255, 255, 255)), (0, 0))

        # Draw ship
        self.ship.blitme()

        # Draw bullets
        for bullet in self.bullets:
            bullet.draw_bullet()

        # Draw aliens
        self.aliens.draw(self.screen)

        # Make the most recently drawn screen visible
        pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance, and run the game
    ai = AlienInvasion()
    ai.run_game()
