import pygame
from settings import Settings

class interactable:
    def __init__(self, Xcord, useKey, use_type):
        Xcord = Xcord
        useKey = useKey
        use_type = use_type
    
class store(interactable):
    def __init__(self, Xcord, useKey, use_type):
        super().__init__(Xcord, useKey, use_type)

class mining(interactable):
    def __init__(self, Xcord, useKey, use_type):
        super().__init__(Xcord, useKey, use_type)
        
        

Store2 = interactable(x,y,z,i)
Store2.interact()
