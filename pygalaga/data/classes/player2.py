from ..classes import player
import pygame

class Player2(player.Player):
    def __init__(self, pos, width, height, speed):
        super().__init__(pos, width, height, speed)

    def move(self, keys):
        # check if the `d` key is pressed
        if keys.get(pygame.K_d, False):
            self.move_right()

        # check if the `a` key is pressed
        if keys.get(pygame.K_a, False):
            self.move_left()

        # check if the `w` key is pressed
        if keys.get(pygame.K_w, False):
            self.move_up()

        # check if the `s` key is pressed
        if keys.get(pygame.K_s, False):
            self.move_down()

    def took_shot(self, keys):
        return keys.get(pygame.K_LSHIFT, False)