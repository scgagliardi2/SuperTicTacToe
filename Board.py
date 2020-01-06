import pygame
import math

class Board:

    def __init__(self):
        self.title = 'Super Tic Tac Toe'
        self.height = 900
        self.width = 900
        # set window title
        pygame.display.set_caption(self.title)
        # create game display window
        self.GameScreen = pygame.display.set_mode((self.width, self.height))
        # load board
        BoardImage = pygame.image.load('Images/Board.jpeg')
        self.tl = pygame.transform.scale(BoardImage, (300, 300))
        self.tm = pygame.transform.scale(BoardImage, (300, 300))
        self.tr = pygame.transform.scale(BoardImage, (300, 300))
        self.ml = pygame.transform.scale(BoardImage, (300, 300))
        self.mm = pygame.transform.scale(BoardImage, (300, 300))
        self.mr = pygame.transform.scale(BoardImage, (300, 300))
        self.bl = pygame.transform.scale(BoardImage, (300, 300))
        self.bm = pygame.transform.scale(BoardImage, (300, 300))
        self.br = pygame.transform.scale(BoardImage, (300, 300))
        self.gameArray = [[['e' for col in range(3)] for row in range(3)] for area in range(9)]

    def draw(self):
        self.GameScreen.blit(self.tl, (0, 0))
        self.GameScreen.blit(self.tm, (0, 300))
        self.GameScreen.blit(self.tr, (0, 600))
        self.GameScreen.blit(self.ml, (300, 0))
        self.GameScreen.blit(self.mm, (300, 300))
        self.GameScreen.blit(self.mr, (300, 600))
        self.GameScreen.blit(self.bl, (600, 0))
        self.GameScreen.blit(self.bm, (600, 300))
        self.GameScreen.blit(self.br, (600, 600))
    
    def playableArea(self):
        pass

    def placeMove(self, turn, loc):
        if turn == 0:
            O = pygame.image.load('Images/O.jpg')
            O = pygame.transform.scale(O, (60, 60))
            self.tl.blit(O, (loc[0], loc[1]))
        elif turn == 1:
            X = pygame.image.load('Images/X.jpg')
            X = pygame.transform.scale(X, (60, 60))
            self.mm.blit(X, (loc[0], loc[1]))
        pass

    def checkArea(self, area):
        pass

    def checkWin(self):
        pass

    def getLocation(self, pos):
        x = math.floor(pos[0])
        y = math.floor(pos[1])
        rndPos = [x, y]
        return rndPos
        ''' if pos[0] > 800:
            if pos[1] > 800:
                return [8][2][2]
            elif 800 >= pos[1] > 700:
                return [8][1][2]
            elif 700 >= pos[1] > 600:
                return [8][0][2]
            elif 600 >= pos[1] > 500:
                return [7][2][2]
            elif 500 >= pos[1] > 400:
                return [7][1][2]
            elif 400 >= pos[1] > 300:
                return [7][0][2]
            elif 300 >= pos[1] > 200:
                return [6][2][2]
            elif 200 >= pos[1] > 100:
                return [6][1][2]
            elif 100 >= pos[1]:
                return [6, 0, 2]
        elif 800 >= pos[0] > 700:
            if pos[1] > 800:
                return [8][2][2]
            elif 800 >= pos[1] > 700:
                return [8][1][2]
            elif 700 >= pos[1] > 600:
                return [8][0][2]
            elif 600 >= pos[1] > 500:
                return [7][2][2]
            elif 500 >= pos[1] > 400:
                return [7][1][2]
            elif 400 >= pos[1] > 300:
                return [7][0][2]
            elif 300 >= pos[1] > 200:
                return [6][2][2]
            elif 200 >= pos[1] > 100:
                return [6][1][2]
            elif 100 >= pos[1]:
                return [6][0][2] '''
