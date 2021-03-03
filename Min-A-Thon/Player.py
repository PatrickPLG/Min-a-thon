import pygame
from settings import Settings


class Player:
    """A class to manage the ship."""
    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        self.settings = Settings()
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        # Movement flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ship's position based on the movement flag."""
        if (self.moving_right and self.rect.x <= self.settings.screen_width - 60):
            self.rect.x += 1
            print("right")
        if (self.moving_left and self.rect.x >= 0):
            self.rect.x -= 1
            print("left")





    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
