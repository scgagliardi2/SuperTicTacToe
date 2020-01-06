import pygame

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
        self.image = pygame.transform.scale(BoardImage, (300, 300))

    def draw(self):
        self.GameScreen.blit(self.image, (0, 0))
        self.GameScreen.blit(self.image, (0, 300))
        self.GameScreen.blit(self.image, (0, 600))
        self.GameScreen.blit(self.image, (300, 0))
        self.GameScreen.blit(self.image, (300, 300))
        self.GameScreen.blit(self.image, (300, 600))
        self.GameScreen.blit(self.image, (600, 0))
        self.GameScreen.blit(self.image, (600, 300))
        self.GameScreen.blit(self.image, (600, 600))
    
    def playableArea(self):
        pass

    def placeMove(self, player):
        pass

    def checkArea(self, area):
        pass

    def checkWin(self):
        pass
