from colors import *
import os
import sys
import pygame
import math, time, random
import random
from pygame.locals import *
pygame.display.set_caption("Photobomb")
WIDTH = 1500
HEIGHT = 900
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)

class Photobomb:
    def __init__(self):
        self.buffer=100
        self.startbg=pygame.image.load(r'startingbg.jpg').convert_alpha()
        self.font = pygame.font.Font('font/CoffeeTin.ttf', 150)
        self.font2 = pygame.font.Font('font/IndianPoker.ttf', 75)
        self.font2.set_bold(True)
        self.startText = self.font2.render("Ready to Photobomb?", 1, (randcol()))
        self.startSize = self.font2.size("Ready to Photobomb?")
        self.start_up_init()

    def show_text(self, msg, x, y, color, size):
        tin = pygame.font.Font('font/IndianPoker.ttf', size)
        msgobj = tin.render(msg, False, color)
        SCREEN.blit(msgobj, (x, y))

    def start_up_init(self):
        # Initialize things at startup
        print("Starting up")
        self.startButton = self.font2.render(" Start ", 1, black)
        self.startButtonSize = self.font2.size(" Start ")
        self.startButtonLoc = (WIDTH/2 - self.startButtonSize[0]/2, HEIGHT/3 - self.startButtonSize[1]/2)
        self.startButtonRect = pygame.Rect(self.startButtonLoc, self.startButtonSize)
        self.startButtonRectOutline = pygame.Rect(self.startButtonLoc, self.startButtonSize)
        self.startLoc = (WIDTH/2 - self.startSize[0]/2, self.buffer)
        self.state = 0

    def main(self):
        if self.state == 0:
            self.show_splash_screen()
        elif self.state == 1:
            self.play()
        elif self.state == 2:
             self.results()

    def show_splash_screen(self):
        global SCREEN, WIDTH, HEIGHT
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.VIDEORESIZE:
                SCREEN = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                WIDTH = event.w
                HEIGHT = event.h
                self.start_up_init()
            # when the user clicks the start button, change to the playing state
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouseRect = pygame.Rect(event.pos, (1, 1))
                    if mouseRect.colliderect(self.startButtonRect):
                        self.state = 1
                        self.play_init()
                        return
            SCREEN.blit(self.startbg,(0,0))
            # draw the start button
            pygame.draw.rect(SCREEN, green, self.startButtonRect)
            pygame.draw.rect(SCREEN, black, self.startButtonRectOutline, 2)
            SCREEN.blit(self.startButton, self.startButtonLoc)
            SCREEN.blit(self.startText, self.startLoc)
            pygame.display.flip()

    def play_init(self):
        # create the new variables
        self.round = 0
        
#############################################################
if __name__ == "__main__":
    os.environ['SDL_VIDEO_CENTERED'] = '1'  # center SCREEN
    pygame.init()
    pygame.display.set_caption("Photo Bomb")
    SCREEN = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
    Runit = Photobomb()
    Myclock = pygame.time.Clock()
    while 1:
        Runit.main()
        Myclock.tick(64)