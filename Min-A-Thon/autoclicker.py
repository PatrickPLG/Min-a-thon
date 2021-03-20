import pygame
from settings import Settings

class AutoClicker():
    def __init__(self, name, price, multiplier, buykey):
      self.name = name
      self.price = price
      self.number = 0
      self.multiplier = multiplier #* float(self.number)
      self.buykey = buykey

    def newPrice(self):
        self.price = self.price * 2
    
    def numberOfClickers(self):
        self.number += 1
        self.multiplier = self.multiplier + self.number

    