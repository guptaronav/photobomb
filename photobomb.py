from colors import *
import os
import sys
import pygame
import math, time, random
import random
from enum import Enum
from pygame.locals import *
pygame.display.set_caption("Photobomb")
WIDTH = 1500
HEIGHT = 900
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)

class Places(Enum):
    Hawaii, France, India = 1,2,3
class Victims(Enum):
    Shubham, Robert, Pronamee  = 1,2,3
class Photobomb:
    def __init__(self):
        self.buffer=250
        self.firstbg=pygame.image.load(r'firstbg.jpg').convert_alpha()
        self.secondbg=pygame.image.load(r'secondbg.jpeg').convert_alpha()
        self.cameraoverlay=pygame.image.load(r'cameraoverlay.png').convert_alpha()
        self.chalkFont = pygame.font.Font('font/Chalkduster.ttf', 50)
        self.chalkFont2 = pygame.font.Font('font/Chalkduster.ttf', 22)
        self.chalkFont3 = pygame.font.Font('font/Chalkduster.ttf', 35)
        self.font = pygame.font.Font('font/CoffeeTin.ttf', 150)
        self.font2 = pygame.font.Font('font/IndianPoker.ttf', 75)
        self.font2.set_bold(True)
        self.startText = self.font2.render("Ready to Photobomb?", 1, (randcol()))
        self.startSize = self.font2.size("Ready to Photobomb?")
        
        self.placeText = self.chalkFont3.render("Choose your location: ", 1, (green))
        self.placeSize = self.chalkFont3.size("Choose your location: ")
        
        self.place1 = self.chalkFont3.render(Places.Hawaii.name, 1, pygame.Color(cyan))
        self.place1Size = self.chalkFont3.size(Places.Hawaii.name)
        self.place1Loc = (700, self.buffer + 100)
        self.place1Rect = pygame.Rect((self.place1Loc[0]-30,self.place1Loc[1]),(self.place1Size[0]+30,self.place1Size[1]))
        
        self.place2 = self.chalkFont3.render(Places.France.name, 1, pygame.Color(cyan))
        self.place2Size = self.chalkFont3.size(Places.Hawaii.name)
        self.place2Loc = (900, self.buffer + 100)
        self.place2Rect = pygame.Rect((self.place2Loc[0]-30,self.place2Loc[1]),(self.place2Size[0]+30,self.place2Size[1]))
        
        self.place3 = self.chalkFont3.render(Places.India.name, 1, pygame.Color(cyan))
        self.place3Size = self.chalkFont3.size(Places.Hawaii.name)
        self.place3Loc = (1100, self.buffer + 100)
        self.place3Rect = pygame.Rect((self.place3Loc[0]-30,self.place3Loc[1]),(self.place3Size[0]+30,self.place3Size[1]))
        
        self.vicText = self.chalkFont3.render("Choose your vacation buddy: ", 1, (green))
        self.vicSize = self.chalkFont3.size("Choose your vacation buddy: ")
        
        self.vic1 = self.chalkFont3.render(Victims.Shubham.name, 1, pygame.Color(cyan))
        self.vic1Size = self.chalkFont3.size(Victims.Shubham.name)
        self.vic1Loc = (750, self.buffer + 200)
        self.vic1Rect = pygame.Rect((self.vic1Loc[0]-30,self.vic1Loc[1]),(self.vic1Size[0]+30,self.vic1Size[1]))
        
        self.vic2 = self.chalkFont3.render(Victims.Robert.name, 1, pygame.Color(cyan))
        self.vic2Size = self.chalkFont3.size(Victims.Robert.name)
        self.vic2Loc = (1000, self.buffer + 200)
        self.vic2Rect = pygame.Rect((self.vic2Loc[0]-30,self.vic2Loc[1]),(self.vic2Size[0]+30,self.vic2Size[1]))
        
        self.vic3 = self.chalkFont3.render(Victims.Pronamee.name, 1, pygame.Color(cyan))
        self.vic3Size = self.chalkFont3.size(Victims.Pronamee.name)
        self.vic3Loc = (1200, self.buffer + 200)
        self.vic3Rect = pygame.Rect((self.vic3Loc[0]-30,self.vic3Loc[1]),(self.vic3Size[0]+30,self.vic3Size[1]))
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
        self.startLoc = (WIDTH/2 - self.startSize[0]/2, 100)
        
        self.playButton = self.font2.render(" Play ", 1, black)
        self.playButtonSize = self.font2.size(" Play ")
        self.playButtonLoc = (WIDTH/2 - self.playButtonSize[0]/2, HEIGHT-self.buffer+20 - self.playButtonSize[1]/2)
        self.playButtonRect = pygame.Rect(self.playButtonLoc, self.playButtonSize)
        self.playButtonRectOutline = pygame.Rect(self.playButtonLoc, self.playButtonSize)

        self.selectedPlace=Places.Hawaii
        self.thirdbg=pygame.image.load(r'hawaii.jpeg').convert_alpha()
        self.selectedVictim=Victims.Shubham
        self.state = 0

    def main(self):
        if self.state == 0:
            self.show_splash_screen()
        elif self.state == 1:
            self.select_loc_and_victim()
        elif self.state == 2:
             self.play()
        else:
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
                        return
            SCREEN.blit(self.firstbg,(0,0))
            # draw the start button
            pygame.draw.rect(SCREEN, green, self.startButtonRect)
            pygame.draw.rect(SCREEN, black, self.startButtonRectOutline, 2)
            SCREEN.blit(self.startButton, self.startButtonLoc)
            SCREEN.blit(self.startText, self.startLoc)
            pygame.display.flip()

    def select_loc_and_victim(self):
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
            # when the user chooses the info change to the playing state
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if self.place1Rect.collidepoint(event.pos):
                        self.selectedPlace=Places.Hawaii
                        self.thirdbg=pygame.image.load(r'hawaii.jpeg').convert_alpha()
                    if self.place2Rect.collidepoint(event.pos):
                        self.selectedPlace=Places.France
                        self.thirdbg=pygame.image.load(r'france.jpeg').convert_alpha()
                    if self.place3Rect.collidepoint(event.pos):
                        self.selectedPlace=Places.India
                        self.thirdbg=pygame.image.load(r'india.jpeg').convert_alpha()
                    if self.vic1Rect.collidepoint(event.pos):
                        self.selectedVictim=Victims.Shubham
                    if self.vic2Rect.collidepoint(event.pos):
                        self.selectedVictim=Victims.Robert
                    if self.vic3Rect.collidepoint(event.pos):
                        self.selectedVictim=Victims.Pronamee
                    if self.playButtonRect.collidepoint(event.pos):
                        self.state=2
        
        SCREEN.blit(self.secondbg,(0,0))
        SCREEN.blit(self.placeText,(200,self.place1Loc[1]))
        SCREEN.blit(self.place1,self.place1Loc)
        pygame.draw.circle(SCREEN, white, (self.place1Loc[0] - 20, self.place1Loc[1] + 22), 16, 2)
        SCREEN.blit(self.place2,self.place2Loc)
        pygame.draw.circle(SCREEN, white, (self.place2Loc[0] - 20, self.place2Loc[1] + 22), 16, 2)
        SCREEN.blit(self.place3,self.place3Loc)
        pygame.draw.circle(SCREEN, white, (self.place3Loc[0] - 20, self.place3Loc[1] + 22), 16, 2)
        
        SCREEN.blit(self.vicText,(120,self.vic1Loc[1]))
        SCREEN.blit(self.vic1,self.vic1Loc)
        pygame.draw.circle(SCREEN, white, (self.vic1Loc[0] - 20, self.vic1Loc[1] + 22), 16, 2)
        SCREEN.blit(self.vic2,self.vic2Loc)
        pygame.draw.circle(SCREEN, white, (self.vic2Loc[0] - 20, self.vic2Loc[1] + 22), 16, 2)
        SCREEN.blit(self.vic3,self.vic3Loc)
        pygame.draw.circle(SCREEN, white, (self.vic3Loc[0] - 20, self.vic3Loc[1] + 22), 16, 2)
        
        pygame.draw.rect(SCREEN, green, self.playButtonRect)
        pygame.draw.rect(SCREEN, black, self.playButtonRectOutline, 2)
        SCREEN.blit(self.playButton, self.playButtonLoc)
        
        Photobomb.show_text(self,"Plan your vacation!",WIDTH/2-290,200,yellow,50)
        # pygame.draw.rect(SCREEN, white, self.place1Rect)
        # pygame.draw.rect(SCREEN, white, self.place2Rect)
        # pygame.draw.rect(SCREEN, white, self.place3Rect)
        # pygame.draw.rect(SCREEN, white, self.vic1Rect)
        # pygame.draw.rect(SCREEN, white, self.vic2Rect)
        # pygame.draw.rect(SCREEN, white, self.vic3Rect)
        
        match self.selectedPlace:
            case Places.Hawaii:
                pygame.draw.circle(SCREEN, white, (self.place1Loc[0] - 20, self.place1Loc[1] + 22), 8)
                breakpoint
            case Places.France:                
                pygame.draw.circle(SCREEN, white, (self.place2Loc[0] - 20, self.place2Loc[1] + 22), 8)
                breakpoint
            case Places.India:                
                pygame.draw.circle(SCREEN, white, (self.place3Loc[0] - 20, self.place3Loc[1] + 22), 8)
                
        match self.selectedVictim:
            case Victims.Shubham:
                pygame.draw.circle(SCREEN, white, (self.vic1Loc[0] - 20, self.vic1Loc[1] + 22), 8)
                breakpoint
            case Victims.Robert:                
                pygame.draw.circle(SCREEN, white, (self.vic2Loc[0] - 20, self.vic2Loc[1] + 22), 8)
                breakpoint
            case Victims.Pronamee:                
                pygame.draw.circle(SCREEN, white, (self.vic3Loc[0] - 20, self.vic3Loc[1] + 22), 8)
                
        pygame.display.flip()
        
    def play(self):
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
            # when the user clicks, release... the MOOOOOOOOOOOOO
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouseRect = pygame.Rect(event.pos, (1, 1))
                    if mouseRect.colliderect(self.startButtonRect):
                        self.state = 1
                        return
            SCREEN.blit(self.thirdbg,(0,0))
            SCREEN.blit(self.cameraoverlay,(0,0))
            # draw the start button
            #pygame.draw.rect(SCREEN, green, self.startButtonRect)
            #pygame.draw.rect(SCREEN, black, self.startButtonRectOutline, 2)
            #SCREEN.blit(self.startButton, self.startButtonLoc)
            #SCREEN.blit(self.startText, self.startLoc)
            pygame.display.flip()

    
#############################################################
if __name__ == "__main__":
    os.environ['SDL_VIDEO_CENTERED'] = '1'  # center SCREEN
    pygame.init()
    pygame.display.set_caption("Photobomb")
    SCREEN = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
    Runit = Photobomb()
    Myclock = pygame.time.Clock()
    while 1:
        Runit.main()
        Myclock.tick(64)