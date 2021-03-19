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
        pygame.display.set_caption("Min-a-thon")
        
        # inits the mine and the store with the key e and self as positional arguments
        self.mine = Mining('pygame.K_e', self)
        self.store = Store('pygame.K_e', self)

        # inits self.player as Player with self as a positional argument
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


                # Checks for player collision with the mine and if the player has pressed 'e'
                if self.player.rect.colliderect(self.mine) and event.key == pygame.K_e:
                    self.run_sequence_game = True
                    self.sequence_game()

                # Checks for player collision with the store and if the player has pressed 'e'
                if self.player.rect.colliderect(self.store) and event.key == pygame.K_e:
                    self.player_buying = True
                    self.store_buy()
                    print("store interacted with")
                        
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.player.moving_right = False
                if event.key == pygame.K_LEFT:
                    self.player.moving_left = False
    def store_buy(self):
        while self.player_buying == True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    key = pygame.key.name(event.key)

                    if event.key == pygame.K_z and self.player.gold > 0:
                        self.player.buy()
                        print(self.player.gold)
                        self.player_buying = False
                    else:
                        self.player_buying = False

    def sequence_game(self):
        # Generates an array from self.list, using three characters
        self.random_sequence = random.sample(self.list, 3)
        # Updates screen
        self._update_screen()
        # Empties user_sequence
        self.user_sequence = []
        # ~DEBUG~ prints random sequence in console
        print(self.random_sequence)

        # If the run_sequence_game is true, the game will lock the keyboard and check for keys
        while self.run_sequence_game == True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    key = pygame.key.name(event.key)
                    # If the amount of keys pressed isn't equal to 3
                    # it will append to self.user_sequence and print the sequence in console
                    if len(self.user_sequence) != 3:
                        self.user_sequence.append(key)
                    print(self.user_sequence)

                    # If the amount of keys pressed is equal to 3
                    # then the program will check if it matches 
                    # and award points using self.player.mine and return self.run_sequnce_game to False
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
