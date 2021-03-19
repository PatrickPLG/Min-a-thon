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

        self.black=(0,0,0)
        self.myFontBig = pygame.font.SysFont("Times New Roman", 36)
        self.myFont = pygame.font.SysFont("Times New Roman", 18)
        #self.display_gold = 

        self.random_sequence = []
        self.user_sequence = []


    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._update_screen()
            self._check_events()
            self.player.update()
            
            self.run_sequence_game = False
            

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
                        self.run_sequence_game = True
                        self.sequence_game()
                        
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.player.moving_right = False
                if event.key == pygame.K_LEFT:
                    self.player.moving_left = False

    def sequence_game(self):
        self.random_sequence = random.sample(self.list, 3)
        self._update_screen()
        self.user_sequence = []
        print(self.random_sequence)
        while self.run_sequence_game == True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    key = pygame.key.name(event.key)
                    if len(self.user_sequence) != 3:
                        self.user_sequence.append(key)
                    print(self.user_sequence)
                    if len(self.user_sequence) == 3:
                        if self.user_sequence == self.random_sequence:
                            self.player.mine()
                            print(self.player.gold)
                            self.run_sequence_game = False
                        else:
                            print("Passer ikke")
                            print(self.player.gold)
                            self.run_sequence_game = False
                            #https://stackoverflow.com/questions/55757109/how-to-display-text-for-2-seconds-in-pygame
                    
                elif event.type == pygame.QUIT:
                    sys.exit()
    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        
        self.mine.blitme()
        self.screen.blit(self.myFontBig.render("Gold: "+str(self.player.gold), 1, self.black), (self.settings.screen_width/2, self.settings.screen_height/2))
        self.screen.blit(self.myFont.render("Sequence: "+str(self.random_sequence), 1, self.black), (30, 650))
        self.store.blitme()
        self.player.blitme()
        pygame.display.flip()
        

        


if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = MinAThon()
    ai.run_game()
