import pygame
import math
import FullBoard
import XORect


class SingleBoard:

    def __init__(self, width, x, y):
        self.width = math.floor(width/3)-10
        self.x0 = x + 5
        self.y0 = y + 3
        self.xf = self.x0 + self.width
        self.yf = self.y0 + self.width
        self.rectangle = pygame.Rect(self.x0, self.y0, self.width, self.width)
        self.background = pygame.Surface((self.width, self.width))
        self.isPlayable = True
        self.color = (255, 255, 255)
        self.winner = 'e'
        self.XORectArray = {
            'tl': XORect.XORect(self.width, self.width*(0.03), self.width*(0.03), self.x0, self.y0, self.color),
            'tm': XORect.XORect(self.width, self.width*(0.365), self.width*(0.03), self.x0, self.y0, self.color),
            'tr': XORect.XORect(self.width, self.width*(0.70), self.width*(0.03), self.x0, self.y0, self.color),
            'ml': XORect.XORect(self.width, self.width*(0.03), self.width*(0.365), self.x0, self.y0, self.color),
            'mm': XORect.XORect(self.width, self.width*(0.365), self.width*(0.365), self.x0, self.y0, self.color),
            'mr': XORect.XORect(self.width, self.width*(0.70), self.width*(0.365), self.x0, self.y0, self.color),
            'bl': XORect.XORect(self.width, self.width*(0.03), self.width*(0.70), self.x0, self.y0, self.color),
            'bm': XORect.XORect(self.width, self.width*(0.365), self.width*(0.70), self.x0, self.y0, self.color),
            'br': XORect.XORect(self.width, self.width*(0.70), self.width*(0.70), self.x0, self.y0, self.color)
        }

    def draw(self, surface):
        surface.blit(self.background, (self.x0, self.y0))
        self.background.fill(self.color)
        black = (0, 0, 0)
        pygame.draw.line(self.background, black, (0, math.floor(
            self.width/3)), (self.width, math.floor(self.width/3)), 2)
        pygame.draw.line(self.background, black, (0, math.floor(
            self.width/1.5)), (self.width, math.floor(self.width/1.5)), 2)
        pygame.draw.line(self.background, black, (math.floor(
            self.width/3), 0), (math.floor(self.width/3), self.width), 2)
        pygame.draw.line(self.background, black, (math.floor(
            self.width/1.5), 0), (math.floor(self.width/1.5), self.width), 2)
        for item in self.XORectArray:
            self.XORectArray[item].draw(surface)

    def setAsUnplayableArea(self, turn):
        self.isPlayable = False
        self.winner = turn
        if turn == 'o':
            self.color = (0, 0, 255)
        if turn == 'x':
            self.color = (255, 0, 0)

    def getRects(self):
        rectArray = []
        for item in self.XORectArray:
            rectArray.append(self.XORectArray[item].getRect())
        return rectArray

    def checkWin(self):
        if self.XORectArray['tl'].value == self.XORectArray['tm'].value and self.XORectArray['tl'].value == self.XORectArray['tr'].value and self.XORectArray['tl'].value != 'e':
            self.setAsUnplayableArea(self.XORectArray['tl'].value)
        elif self.XORectArray['ml'].value == self.XORectArray['mm'].value and self.XORectArray['ml'].value == self.XORectArray['mr'].value and self.XORectArray['ml'].value != 'e':
            self.setAsUnplayableArea(self.XORectArray['ml'].value)
        elif self.XORectArray['bl'].value == self.XORectArray['bm'].value and self.XORectArray['bl'].value == self.XORectArray['br'].value and self.XORectArray['bl'].value != 'e':
            self.setAsUnplayableArea(self.XORectArray['bl'].value)
        elif self.XORectArray['tl'].value == self.XORectArray['ml'].value and self.XORectArray['tl'].value == self.XORectArray['bl'].value and self.XORectArray['tl'].value != 'e':
            self.setAsUnplayableArea(self.XORectArray['tl'].value)
        elif self.XORectArray['tm'].value == self.XORectArray['mm'].value and self.XORectArray['tm'].value == self.XORectArray['bm'].value and self.XORectArray['tm'].value != 'e':
            self.setAsUnplayableArea(self.XORectArray['tm'].value)
        elif self.XORectArray['tr'].value == self.XORectArray['mr'].value and self.XORectArray['tr'].value == self.XORectArray['br'].value and self.XORectArray['tr'].value != 'e':
            self.setAsUnplayableArea(self.XORectArray['tr'].value)
        elif self.XORectArray['tl'].value == self.XORectArray['mm'].value and self.XORectArray['tl'].value == self.XORectArray['br'].value and self.XORectArray['tl'].value != 'e':
            self.setAsUnplayableArea(self.XORectArray['tl'].value)
        elif self.XORectArray['tr'].value == self.XORectArray['mm'].value and self.XORectArray['tr'].value == self.XORectArray['bl'].value and self.XORectArray['tr'].value != 'e':
            self.setAsUnplayableArea(self.XORectArray['tr'].value)
