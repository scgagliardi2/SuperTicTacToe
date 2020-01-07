import pygame
import math
import FullBoard

class XORect:

    def __init__(self, gamescreen, width, x, y, color):
        # set up the background surface
        self.width = math.floor((width/3)-5)
        self.background = pygame.Surface((self.width, self.width))
        self.background = self.background.convert()
        self.background.fill(color)
        self.center = [math.floor(x), math.floor(y)]
        self.value = 'o'
        self.x1 = x-self.width + 8
        self.y1 = y-self.width + 8

    def draw(self, surface):
        surface.blit(self.background, (self.x1, self.y1))
        if self.value == 'e':
            pass
        elif self.value == "o":
            blue = (0, 0, 255)
            radius = math.floor(self.width/2-5)
            pygame.draw.circle(self.background, blue, (self.center[0], self.center[1]), radius, 2)
        elif self.value == "x":
            red = (255, 0, 0)
            pygame.draw.line(self.background, red, (self.x1, self.y1), (self.x1 + self.width, self.y1 + self.width), 2)
            pygame.draw.line(self.background, red, (self.x1 + self.width, self.y1), (self.x1, self.y1 + self.width), 2)

    def updateValue(self, turn):
        if turn == 0:
            self.value = '0'
        elif turn == 1:
            self.value = 'x'