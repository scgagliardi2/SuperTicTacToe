import pygame
import math
import SingleBoard

class Board:

    def __init__(self):
        self.title = 'Super Tic Tac Toe'
        self.height = 700
        self.width = 600
        # set window title
        pygame.display.set_caption(self.title)
        # create game display window
        self.GameScreen = pygame.display.set_mode((self.width, self.height))
        # load 9 boards
        self.tl = SingleBoard.SingleBoard(self.GameScreen, self.width, self.height)
        self.tm = SingleBoard.SingleBoard(self.GameScreen, self.width, self.height)
        self.tr = SingleBoard.SingleBoard(self.GameScreen, self.width, self.height)
        self.ml = SingleBoard.SingleBoard(self.GameScreen, self.width, self.height)
        self.mm = SingleBoard.SingleBoard(self.GameScreen, self.width, self.height)
        self.mr = SingleBoard.SingleBoard(self.GameScreen, self.width, self.height)
        self.bl = SingleBoard.SingleBoard(self.GameScreen, self.width, self.height)
        self.bm = SingleBoard.SingleBoard(self.GameScreen, self.width, self.height)
        self.br = SingleBoard.SingleBoard(self.GameScreen, self.width, self.height)
        

    def draw(self):
        self.tl.draw(0, 0)
        self.tm.draw(self.width/3, 0)
        self.tr.draw(self.width/1.5, 0)
        self.ml.draw(0, self.width/3)
        self.mm.draw(self.width/3, self.width/3)
        self.mr.draw(self.width/1.5, self.width/3)
        self.bl.draw(0, self.width/1.5)
        self.bm.draw(self.width/3, self.width/1.5)
        self.br.draw(self.width/1.5, self.width/1.5)
    
    def playableArea(self):
        pass

    def placeMove(self, turn, loc):
        if turn == 0:
            O = pygame.image.load('Images/O.jpg')
            x = self.tl.boardArray['tl'][1]
            y = self.tl.boardArray['tl'][2]
            self.tl.boardArray['tl'] = ('o', x, y)
        elif turn == 1:
            X = pygame.image.load('Images/X.jpg')
            x = self.tl.boardArray['tl'][1]
            y = self.tl.boardArray['tl'][2]
            self.tl.boardArray['tl'] = ('x', x, y)

    def checkArea(self, area):
        pass

    def checkWin(self):
        pass

    def getLocation(self, pos):
        x = math.floor(pos[0])
        y = math.floor(pos[1])
        rndPos = [x, y]
        return rndPos