from ..classes import player
import pygame

class Player1(player.Player):
    def __init__(self, pos, width, height, speed):
        super().__init__(pos, width, height, speed)

    def move(self, keys):
        # check if the right arrow key is pressed
        print(keys)
        if keys.get(pygame.K_RIGHT, False):
            self.move_right()

        # check if the left arrow key is pressed
        if keys.get(pygame.K_LEFT, False):
            self.move_left()

        # check if the up arrow key is pressed
        if keys.get(pygame.K_UP, False):
            self.move_up()

        # check if the down arrow key is pressed
        if keys.get(pygame.K_DOWN, False):
            self.move_down()

    def took_shot(self, keys):
        return keys.get(pygame.K_SPACE, False)