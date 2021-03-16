import pygame
from settings import Settings
from Player import Player

class Interactable:
    def __init__(self, useKey, ai_game):
        self.useKey = useKey

        """Initialize the ship and set its starting position."""
        self.settings = Settings()
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get its rect.
        
        #self.rect = self.image.get_rect()

        

        
    
class Store(Interactable):
    def __init__(self, useKey, ai_game):
        super().__init__(useKey, ai_game)
        self.image = pygame.image.load('images/shop.png')
        self.rect = self.image.get_rect()
        # Start each new ship at the bottom center of the screen.
        self.rect.bottomright = self.screen_rect.bottomright

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)

class Mining(Interactable):
    def __init__(self, useKey, ai_game):
        super().__init__(useKey, ai_game)
        # Start each new ship at the bottom center of the screen.
        
        self.image = pygame.image.load('images/pixelcave.png')
        self.rect = self.image.get_rect()
        self.rect.bottomleft = self.screen_rect.bottomleft
        

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
        
