import pygame
class CTagSpecial:
    def __init__(self, special_type:str, pos:pygame.Vector2):
        self.special_type = special_type
        self.pos = pos      
        self.create_time = 0.0
        self.detonated= False
