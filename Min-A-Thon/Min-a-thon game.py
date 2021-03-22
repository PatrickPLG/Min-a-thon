import sys
import pygame
import random
import string
from settings import Settings
from Player import Player
from interactable import Store, Mining
from autoclicker import AutoClicker

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
        
        # Text
        self.black=(0,0,0)
        self.myFontBig = pygame.font.SysFont("Times New Roman", 36)
        self.myFont = pygame.font.SysFont("Times New Roman", 18)
        
        # Autoclickers
        self.hands = AutoClicker('Hands', 20, 1.05, '1')
        self.pickaxe = AutoClicker('Pickaxe', 40, 1.2, '2')
        self.drill = AutoClicker('Drill', 60, 1.5, '3')
        self.earn = AutoClicker('Earn', 10, 2, '0')
        

        # Sequence
        self.list = list(string.ascii_lowercase)
        self.random_sequence = []
        self.user_sequence = []

        # Timer
        self.time_elapsed_since_last_action = 0
        self.clock = pygame.time.Clock()
        self.popup_clock = pygame.time.Clock()
        self.time_elapsed_since_last_popup = 0
        self.popup = False

        # Soundeffects
        self.hit1 = pygame.mixer.Sound('soundeffects/hit1.wav')
        self.hit2 = pygame.mixer.Sound('soundeffects/hit2.wav')
        self.hit3 = pygame.mixer.Sound('soundeffects/hit3.wav')
        self.hit4 = pygame.mixer.Sound('soundeffects/hit4.wav')
        self.hit5 = pygame.mixer.Sound('soundeffects/hit5.wav')
        self.wrong = pygame.mixer.Sound('soundeffects/wrong.wav')
        self.shop = pygame.mixer.Sound('soundeffects/shop.wav')

        self.random_mine_effect = []
        self.random_mine_effect.append(self.hit1)
        self.random_mine_effect.append(self.hit2)
        self.random_mine_effect.append(self.hit3)
        self.random_mine_effect.append(self.hit4)
        self.random_mine_effect.append(self.hit5)


    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._update_screen()
            self._check_events()
            self.player.update()
            self.autoclickers()
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
                    self.shop.play()
                    self.store_buy()
                    
                        
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.player.moving_right = False
                if event.key == pygame.K_LEFT:
                    self.player.moving_left = False
    def store_buy(self):
        while self.player_buying == True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    #key = pygame.key.name(event.key)
                    if event.key == pygame.K_2 and self.player.gold >= self.pickaxe.price:
                        self.player.gold -= self.pickaxe.price
                        self.pickaxe.newPrice()
                        self.pickaxe.numberOfClickers()
                        print("Bought: Pickaxe")
                        self.player_buying = False
                    if event.key == pygame.K_1 and self.player.gold >= self.hands.price:
                        self.player.gold -= self.hands.price
                        self.hands.newPrice()
                        self.hands.numberOfClickers()
                        print("Bought: Hands")
                        self.player_buying = False
                    if event.key == pygame.K_3 and self.player.gold >= self.drill.price:
                        self.player.gold -= self.drill.price
                        self.drill.newPrice()
                        self.drill.numberOfClickers()
                        print("Bought: Drill")
                        self.player_buying = False
                    if event.key == pygame.K_0 and self.player.gold >= self.earn.price:
                        self.player.gold -= self.earn.price
                        self.earn.newPrice()
                        self.earn.numberOfClickers()
                        self.player.goldmultiply()
                        print("Bought: Earn")
                        self.player_buying = False
                    else:
                        self.player_buying = False
    def autoclickers(self):
        # the following method returns the time since its last call in milliseconds
        # it is good practice to store it in a variable called 'dt'
        dt = self.clock.tick() 

        self.time_elapsed_since_last_action += dt
        # dt is measured in milliseconds, therefore 1000 ms = 1 seconds
        if self.time_elapsed_since_last_action > 1000:
            if self.pickaxe.number > 0:
                self.player.gold += self.pickaxe.multiplier
            if self.hands.number > 0:
                self.player.gold += self.hands.multiplier
            if self.drill.number > 0:
                self.player.gold += self.drill.multiplier
            self.time_elapsed_since_last_action = 0 # reset it to 0 so you can count again

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
                    #print(self.user_sequence)

                    # If the amount of keys pressed is equal to 3
                    # then the program will check if it matches 
                    # and award points using self.player.mine and return self.run_sequnce_game to False
                    if len(self.user_sequence) == 3:
                        if self.user_sequence == self.random_sequence:
                            self.player.mine()
                            random.choice(self.random_mine_effect).play()
                            self.random_sequence.clear()
                            self.run_sequence_game = False
                        else:
                            self.random_sequence.clear()
                            self.wrong.play()
                            #https://stackoverflow.com/questions/55757109/how-to-display-text-for-2-seconds-in-pygame
                            self.run_sequence_game = False
                    
                elif event.type == pygame.QUIT:
                    sys.exit()
    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        
        self.mine.blitme()
        self.screen.blit(self.myFontBig.render("Gold: "+str(round(self.player.gold,2)), 1, self.black), (self.settings.screen_width/2, self.settings.screen_height/2))
        if self.player.rect.colliderect(self.mine):
            self.screen.blit(self.myFont.render("Sequence: "+str(self.random_sequence), 1, self.black), (30, 650))
        if self.player.rect.colliderect(self.store):
            self.screen.blit(self.myFont.render("Sequence Earn | " + "Price: " + str(self.earn.price) + " | Acquired: " + str(self.earn.number) + " | Buy Key: " + str(self.earn.buykey), 1, self.black), (800, 470))
            self.screen.blit(self.myFont.render("Hands | " + "Price: " + str(self.hands.price) + " | Acquired: " + str(self.hands.number) + " | Buy Key: " + str(self.hands.buykey), 1, self.black), (800, 500))
            self.screen.blit(self.myFont.render("Pickaxe | " + "Price: " + str(self.pickaxe.price) + " | Acquired: " + str(self.pickaxe.number) + " | Buy Key: " + str(self.pickaxe.buykey), 1, self.black), (800, 530))
            self.screen.blit(self.myFont.render("Drill | " + "Price: " + str(self.drill.price) + " | Acquired: " + str(self.drill.number) + " | Buy Key: " + str(self.drill.buykey), 1, self.black), (800, 560))
        self.store.blitme()
        self.player.blitme()
        pygame.display.flip()
        

        


if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = MinAThon()
    ai.run_game()
