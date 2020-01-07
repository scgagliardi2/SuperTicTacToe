import pygame, sys
import math
import SingleBoard
import LowerDisplay
pygame.init()

class Board:

    def __init__(self):
        self.title = 'Super Tic Tac Toe'
        self.height = 670
        self.width = 600
        # set window title
        pygame.display.set_caption(self.title)
        # create game display window
        white = (255, 255, 255)
        self.GameScreen = pygame.display.set_mode((self.width, self.height))
        self.GameScreen.fill(white)
        # load 9 boards
        self.tl = SingleBoard.SingleBoard(self.width)
        self.tm = SingleBoard.SingleBoard(self.width)
        self.tr = SingleBoard.SingleBoard(self.width)
        self.ml = SingleBoard.SingleBoard(self.width)
        self.mm = SingleBoard.SingleBoard(self.width)
        self.mr = SingleBoard.SingleBoard(self.width)
        self.bl = SingleBoard.SingleBoard(self.width)
        self.bm = SingleBoard.SingleBoard(self.width)
        self.br = SingleBoard.SingleBoard(self.width)
        self.LowerDisplay = LowerDisplay.LowerDisplay(self.GameScreen, self.width)
        BoardImage = pygame.image.load('Images/BBoard.jpg')
        self.image = pygame.transform.scale(BoardImage, (self.width, self.width))
        

    def draw(self):
        self.GameScreen.blit(self.image, (0, 0))
        self.tl.draw(self.GameScreen, 0, 0)
        #self.tm.draw(self.GameScreen, self.width/3, 0)
        #self.tr.draw(self.GameScreen, self.width/1.5, 0)
        #self.ml.draw(self.GameScreen, 0, self.width/3)
        #self.mm.draw(self.GameScreen, self.width/3, self.width/3)
        #self.mr.draw(self.GameScreen, self.width/1.5, self.width/3)
        #self.bl.draw(self.GameScreen, 0, self.width/1.5)
        #self.bm.draw(self.GameScreen, self.width/3, self.width/1.5)
        #self.br.draw(self.GameScreen, self.width/1.5, self.width/1.5)
        pygame.draw.line(self.GameScreen, (0, 0, 0), (0, self.height-70), (self.width, self.height-70), 3)
        self.LowerDisplay.draw(self.height)
    
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

    def checkLoc(self, loc):
        #x = loc[0]
        #y = loc[1]
        #if x > (2/3)*self.width:
        pass


    def checkWin(self):
        pass

    def getLocation(self, pos):
        x = math.floor(pos[0])
        y = math.floor(pos[1])
        rndPos = [x, y]
        return rndPos