from ..classes import player
import pygame

class Player1(player.Player):
    def __init__(self, pos, width, height, speed):
        super().__init__(pos, width, height, speed)

    def move(self, keys):
        # check if the right arrow key is pressed
        if keys[pygame.K_RIGHT]:
            self.move_right()

        # check if the left arrow key is pressed
        if keys[pygame.K_LEFT]:
            self.move_left()

        # check if the up arrow key is pressed
        if keys[pygame.K_UP]:
            self.move_up()

        # check if the down arrow key is pressed
        if keys[pygame.K_DOWN]:
            self.move_down()

    def took_shot(self, keys):
        return keys[pygame.K_SPACE]