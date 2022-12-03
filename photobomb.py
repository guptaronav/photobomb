from colors import *
import os
import sys
import pygame
import math
import time
import random
from pygame.locals import *
pygame.display.set_caption("Photobomb")
WIDTH = 1500
HEIGHT = 900
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)

def show_text(self, msg, x, y, color, size):
        tin = pygame.font.Font('font/IndianPoker.ttf', size)
        msgobj = tin.render(msg, False, color)
        SCREEN.blit(msgobj, (x, y))



class Photobomb:
    def __init__(self):
        self.startbg=pygame.image.load(r'startingbg.jpg').convert_alpha()
a=pygame.image.load(r'startingbg.jpg').convert_alpha()
while True:
    SCREEN.blit(a,(0,0))
    pygame.display.flip()