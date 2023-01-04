from ..classes import player
import pygame as pg

class Player1(player.Player):
    def __init__(self, pos, width, height, speed):
        super().__init__(pos, width, height, speed)

    def move(self, keys):
        # check if the right arrow key is pressed
        if keys[pg.K_RIGHT]: #.get(pg.K_RIGHT, False):
            self.move_right()

        # check if the left arrow key is pressed
        if keys[pg.K_LEFT]:#.get(pg.K_LEFT, False):
            self.move_left()

        # check if the up arrow key is pressed
        if keys[pg.K_UP]:#.get(pg.K_UP, False):
            self.move_up()

        # check if the down arrow key is pressed
        if keys[pg.K_DOWN]:#.get(pg.K_DOWN, False):
            self.move_down()

    def took_shot(self, keys):
        return keys[pg.K_SPACE]#.get(pg.K_SPACE, False)