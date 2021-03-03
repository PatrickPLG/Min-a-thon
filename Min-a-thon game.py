import sys
import pygame
from settings import Settings
from Player import Player


class MinAThon:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        self.player = Player(self)

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self.player.update()
            self._update_screen()

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.player.moving_right = True
                if event.key == pygame.K_LEFT:
                    self.player.moving_left = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.player.moving_right = False
                if event.key == pygame.K_LEFT:
                    self.player.moving_left = False


    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.player.blitme()
        pygame.display.flip()

        


if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = MinAThon()
    ai.run_game()