import pygame
from settings import Settings

class Interactable:
    def __init__(self, Xcord, useKey, ai_game):
        self.Xcord = Xcord
        self.useKey = useKey

        """Initialize the ship and set its starting position."""
        self.settings = Settings()
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.bottomright = self.screen_rect.bottomright

        
    
class Store(Interactable):
    def __init__(self, Xcord, useKey, ai_game):
        super().__init__(Xcord, useKey, ai_game)

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)

class Mining(Interactable):
    def __init__(self, Xcord, useKey, ai_game):
        super().__init__(Xcord, useKey, ai_game)

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
        
