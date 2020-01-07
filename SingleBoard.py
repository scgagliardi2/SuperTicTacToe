import pygame
import math
import FullBoard

class SingleBoard:

    def __init__(self, gamescreen, width, height):
        self.GameScreen = gamescreen
        self.width = math.floor(width/3)
        self.height = math.floor(width/3)
        BoardImage = pygame.image.load('Images/Board.jpeg')
        self.image = pygame.transform.scale(BoardImage, (self.width, self.width))
        self.XImage = pygame.image.load('Images/X.jpg')
        self.XImage = pygame.transform.scale(self.XImage, (math.floor(self.width/5), math.floor(self.width/5)))
        self.OImage = pygame.image.load('Images/O.jpg')
        self.OImage = pygame.transform.scale(self.OImage, (math.floor(self.width/5), math.floor(self.width/5)))
        self.boardArray = {
        'tl': ('e',math.floor(self.width/7.5),math.floor(self.width/7.5)),
        'tm': ('e',math.floor(self.width/2.5),math.floor(self.width/7.5)),
        'tr': ('e',math.floor(self.width/1.5),math.floor(self.width/7.5)),
        'ml': ('e',math.floor(self.width/7.5),math.floor(self.width/2.4)),
        'mm': ('e',math.floor(self.width/2.5),math.floor(self.width/2.4)),
        'mr': ('e',math.floor(self.width/1.5),math.floor(self.width/2.4)),
        'bl': ('e',math.floor(self.width/7.5),math.floor(self.width/1.4)),
        'bm': ('e',math.floor(self.width/2.5),math.floor(self.width/1.4)),
        'br': ('e',math.floor(self.width/1.5),math.floor(self.width/1.4))}

    def draw(self, x, y):
        self.GameScreen.blit(self.image, (x, y))
        for letter in self.boardArray:
            if self.boardArray[letter][0] == 'e':
                pass
            elif self.boardArray[letter][0] == "o":
                self.image.blit(self.OImage, (self.boardArray[letter][1], self.boardArray[letter][2]))
            elif self.boardArray[letter][0] == "x":
                self.image.blit(self.XImage, (self.boardArray[letter][1], self.boardArray[letter][2]))
    
    def setAsPlayableArea(self):
        HBoardImage = pygame.image.load('Images/HighlightedBoard.jpg')
        self.image = pygame.transform.scale(HBoardImage, (self.width, self.width))

    def setAsUnplayableArea(self):
        BoardImage = pygame.image.load('Images/Board.jpeg')
        self.image = pygame.transform.scale(BoardImage, (self.width, self.width))

    def placeMove(self, turn, loc):
        pass

    def checkArea(self, area):
        pass
