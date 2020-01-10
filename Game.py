import pygame
import sys
import FullBoard

# create game clock
clock = pygame.time.Clock()

class Game:

    # FPS rate
    TickRate = 60

    def __init__(self):
        self.board = FullBoard.Board()

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
                        if self.board.checkLoc(turn, mousePos):
                            turn = 1
                            self.board.LowerDisplay.changeTurn(turn)
                            self.board.LowerDisplay.displayWarning = False
                        else:
                            self.board.LowerDisplay.displayWarning = True
                    elif turn == 1:
                        mousePos = pygame.mouse.get_pos()
                        if self.board.checkLoc(turn, mousePos):
                            turn = 0
                            self.board.LowerDisplay.changeTurn(turn)
                            self.board.LowerDisplay.displayWarning = False
                        else:
                            self.board.LowerDisplay.displayWarning = True
                elif event.type == pygame.MOUSEBUTTONUP:
                    pass
            #print(event) # uncomment to print all events to terminal

            # draw board
            self.board.draw()
            self.board.checkWin()

            # update all game graphics
            pygame.display.update()
            clock.tick(self.TickRate)


pygame.init()

NewGame = Game()
NewGame.RunGameLoop()

pygame.quit()
quit()
