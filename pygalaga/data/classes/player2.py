from ..classes import player
import pygame as pg

class Player2(player.Player):
    def __init__(self, pos, width, height, speed):
        super().__init__(pos, width, height, speed)

    def move(self, keys):
        # check if the `d` key is pressed
        if keys[pg.K_d]:#.get(pg.K_d, False):
            self.move_right()

        # check if the `a` key is pressed
        if keys[pg.K_a]:#.get(pg.K_a, False):
            self.move_left()

        # check if the `w` key is pressed
        if keys[pg.K_w]:#.get(pg.K_w, False):
            self.move_up()

        # check if the `s` key is pressed
        if keys[pg.K_s]:#.get(pg.K_s, False):
            self.move_down()

    def took_shot(self, keys):
        return keys[pg.K_LSHIFT]#.get(pg.K_LSHIFT, False)