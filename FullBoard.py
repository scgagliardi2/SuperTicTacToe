import pygame
import sys
import math
import SingleBoard
import LowerDisplay


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
        self.singleBoardArray = {'tl': SingleBoard.SingleBoard(self.width, 0, 0),
                                 'tm': SingleBoard.SingleBoard(self.width, self.width/3, 0),
                                 'tr': SingleBoard.SingleBoard(self.width, self.width/1.5, 0),
                                 'ml': SingleBoard.SingleBoard(self.width, 0, self.width/3),
                                 'mm': SingleBoard.SingleBoard(self.width, self.width/3, self.width/3),
                                 'mr': SingleBoard.SingleBoard(self.width, self.width/1.5, self.width/3),
                                 'bl': SingleBoard.SingleBoard(self.width, 0, self.width/1.5),
                                 'bm': SingleBoard.SingleBoard(self.width, self.width/3, self.width/1.5),
                                 'br': SingleBoard.SingleBoard(self.width, self.width/1.5, self.width/1.5)}
        self.LowerDisplay = LowerDisplay.LowerDisplay(
            self.GameScreen, self.width)
        BoardImage = pygame.image.load('Images/LargeBoard.jpg')
        self.image = pygame.transform.scale(
            BoardImage, (self.width, self.width))
        self.image = self.image.convert()

    def draw(self):
        self.GameScreen.fill((255, 255, 255))
        self.GameScreen.blit(self.image, (0, 0))
        for board in self.singleBoardArray:
            self.singleBoardArray[board].draw(self.GameScreen)
        pygame.draw.line(self.GameScreen, (0, 0, 0),
                         (0, self.height-70), (self.width, self.height-70), 3)
        self.LowerDisplay.draw(self.height)

    def placeMove(self, turn, box):
        if turn == 0:
            box.value = 'o'
        if turn == 1:
            box.value = 'x'

    def checkLoc(self, turn, loc):
        for item in self.singleBoardArray:
            board = self.singleBoardArray[item]
            if board.isPlayable:
                for box in board.getRects():
                    if box[1].collidepoint(loc):
                        if box[0].value == 'e':
                            self.placeMove(turn, box[0])
                            return True
                        else:
                            return False
                    else:
                        pass
            else:
                pass
        return False

    def checkWin(self):
        pass
