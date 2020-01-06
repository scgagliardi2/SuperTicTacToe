import pygame
import sys
import Board

# create game clock
clock = pygame.time.Clock()

class Game:

    # FPS rate
    TickRate = 60

    def __init__(self):
        self.board = Board.Board()

    def RunGameLoop(self):
        IsGameOver = False
        turn = 0

        # MAIN GAME LOOP
        while not IsGameOver:

            # check for "events" like key presses and mouse clicks
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if turn == 0:
                        mousePos = pygame.mouse.get_pos()
                        Loc = self.board.getLocation(mousePos)
                        self.board.placeMove(turn, Loc)
                        turn = 1
                    elif turn == 1:
                        mousePos = pygame.mouse.get_pos()
                        Loc = self.board.getLocation(mousePos)
                        self.board.placeMove(turn, Loc)
                        turn = 0
                elif event.type == pygame.MOUSEBUTTONUP:
                    pass
            # print(event) # uncomment to print all events to terminal

            # draw map background
            self.board.draw()

            # update all game graphics
            pygame.display.update()
            clock.tick(self.TickRate)


pygame.init()

NewGame = Game()
NewGame.RunGameLoop()

pygame.quit()
quit()
