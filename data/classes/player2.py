from ..classes import player
import pygame

class Player2(player.Player):
    def __init__(self, pos, width, height, speed):
        super().__init__(pos, width, height, speed)

    def move(self, keys):
        # check if the `d` key is pressed
        if keys[pygame.K_d]:
            player.move_right()

        # check if the `a` key is pressed
        if keys[pygame.K_a]:
            player.move_left()

        # check if the `w` key is pressed
        if keys[pygame.K_w]:
            player.move_up()

        # check if the `s` key is pressed
        if keys[pygame.K_s]:
            player.move_down()

    def took_shot(self, keys):
        return keys[pygame.K_LSHIFT]