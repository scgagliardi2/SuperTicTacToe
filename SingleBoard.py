import pygame
import math
import FullBoard
import XORect

class SingleBoard:

    def __init__(self, width):
        self.width = math.floor(width/3)-10
        # set up the background surface
        self.background = pygame.Surface((self.width, self.width))
        self.background = self.background.convert()
        self.color = (255, 255, 255)
        self.background.fill(self.color)
        self.XORectArray = {
        'tl': XORect.XORect(self.background, self.width, self.width/5, self.width/5, self.color),
        'tm': XORect.XORect(self.background, self.width, self.width/2.5, self.width/5, self.color),
        #'tr': XORect.XORect(self.background, self.width, self.width/1.5, self.width/7.4, self.color),
        #'ml': XORect.XORect(self.background, self.width, self.width/7.5, self.width/2.4, self.color),
        #'mm': XORect.XORect(self.background, self.width, self.width/2.5, self.width/2.4, self.color),
        #'mr': XORect.XORect(self.background, self.width, self.width/1.5, self.width/2.4, self.color),
        #'bl': XORect.XORect(self.background, self.width, self.width/7.5, self.width/1.5, self.color),
        #'bm': XORect.XORect(self.background, self.width, self.width/2.5, self.width/1.5, self.color),
        #'br': XORect.XORect(self.background, self.width, self.width/1.5, self.width/1.5, self.color)
        }

    def draw(self, surface, x, y):
        surface.blit(self.background, (x, y))
        black = (0, 0, 0)
        pygame.draw.line(self.background, black, (0, math.floor(self.width/3)), (self.width, math.floor(self.width/3)), 2)
        pygame.draw.line(self.background, black, (0, math.floor(self.width/1.5)), (self.width, math.floor(self.width/1.5)), 2)
        pygame.draw.line(self.background, black, (math.floor(self.width/3), 0), (math.floor(self.width/3), self.width), 2)
        pygame.draw.line(self.background, black, (math.floor(self.width/1.5), 0), (math.floor(self.width/1.5), self.width), 2)
        for item in self.XORectArray:
            self.XORectArray[item].draw(self.background)
    
    def setAsPlayableArea(self):
        self.color = (144, 238, 144)

    def setAsUnplayableArea(self):
        self.color = (255, 255, 255)

    def placeMove(self, turn, loc):
        pass

    def checkArea(self, area):
        pass
