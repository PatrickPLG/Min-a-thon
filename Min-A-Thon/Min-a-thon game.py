import sys
import pygame
import random
import string
from settings import Settings
from Player import Player
from interactable import Store, Mining


class MinAThon:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        
        self.mine = Mining('pygame.K_e', self)
        self.store = Store('pygame.K_r', self)
        self.player = Player(self)
        self.list = list(string.ascii_lowercase)

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
                if self.player.rect.colliderect(self.mine):
                    if event.key == pygame.K_e:
                        random_sequence = random.sample(self.list, 3)
                        print(random_sequence)
                        print(p)
                        self.player.mine()
                        print(self.player.gold)
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.player.moving_right = False
                if event.key == pygame.K_LEFT:
                    self.player.moving_left = False


    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        
        self.mine.blitme()
        self.store.blitme()
        self.player.blitme()
        pygame.display.flip()
        

        


if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = MinAThon()
    ai.run_game()
