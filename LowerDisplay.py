import pygame
import FullBoard
import math

class LowerDisplay:

    def __init__(self, gamescreen, width):
        self.GameScreen = gamescreen
        self.width = width
        self.height = 50
        pygame.font.init()
        white = (255, 255, 255) 
        blue = (0, 0, 128) 
        self.font = pygame.font.Font('freesansbold.ttf', math.floor(self.height/2))
        self.turnText = self.font.render("Player 1's turn.", True, blue, white)
        

    def draw(self, height):
        self.GameScreen.blit(self.turnText, (math.floor(self.width/3), height-60))

    def changeTurn(self, turn):
        white = (255, 255, 255)
        blue = (0, 0, 128) 
        if turn == 0:
            self.turnText = self.font.render("Player 1's turn.", True, blue, white)
        elif turn == 1:
            self.turnText = self.font.render("Player 2's turn.", True, blue, white)