'''
Created on Jan 23, 2016

@author: clayton
'''
import pygame


from piece import Piece

class King(Piece):
    
    def __init__(self, pos, grid, player):
        Piece.__init__(self, pos, grid, player)
        if self.player.colour == 0:
            self.img = pygame.image.load("images/wking.png").convert_alpha()
        else:
            self.img = pygame.image.load("images/bking.png").convert_alpha()
        
        self.rect = self.img.get_rect()
        self.rect.x, self.rect.y = self.pos.x, self.pos.y
    