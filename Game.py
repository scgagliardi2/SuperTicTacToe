import pygame
import Board
import Player

# create game clock
clock = pygame.time.Clock()

class Game:

    # FPS rate
    TickRate = 60

    def __init__(self):
        self.board = Board.Board()

    def RunGameLoop(self):
        IsGameOver = False

        # MAIN GAME LOOP
        while not IsGameOver:

            # check for "events" like key presses and mouse clicks
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    IsGameOver = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        CastSpell1 = True
                    elif event.key == pygame.K_2:
                        CastSpell2 = True
                    elif event.key == pygame.K_3:
                        CastSpell3 = True
                    elif event.key == pygame.K_4:
                        CastSpell4 = True
                elif event.type == pygame.KEYUP:
                    pass
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pass
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
