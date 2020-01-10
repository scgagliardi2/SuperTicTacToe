import pygame
import math
import FullBoard

class XORect:

    def __init__(self, width, x, y, a, b, color):
        self.width = math.floor((width/3)-15)
        self.x0 = a + x
        self.y0 = b + y
        self.xf = self.x0 + self.width
        self.yf = self.y0 + self.width
        self.rectangle = pygame.Rect(self.x0, self.y0, self.width, self.width)
        self.background = pygame.Surface((self.width, self.width))
        self.center = [math.floor(self.width/2), math.floor(self.width/2)]
        self.value = 'e'
        self.color = color
        self.background.fill(self.color)

    def draw(self, surface):
        surface.blit(self.background, (self.x0, self.y0))
        self.background.fill(self.color)
        if self.value == 'e':
            pass
        elif self.value == 'o':
            blue = (0, 0, 255)
            radius = math.floor(self.width/2 )
            pygame.draw.circle(self.background, blue, (self.center[0], self.center[1]), radius, 2)
        elif self.value == 'x':
            red = (255, 0, 0)
            pygame.draw.line(self.background, red, (0, 0), (self.width, self.width), 2)
            pygame.draw.line(self.background, red, (self.width, 0), (0, self.width), 2)

    def getRect(self):
        return [self, self.rectangle]