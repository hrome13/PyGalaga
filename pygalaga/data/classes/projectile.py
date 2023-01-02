import pygame

class Projectile:
    def __init__(self, pos, width, height, speed):
        self._pos = pos
        self._left = pos[0]
        self._right = pos[0] + width
        self._top = pos[1]
        self._bottom = pos[1] + height
        self._speed = speed

    @property
    def pos(self):
        return self._pos

    @property
    def left(self):
        return self._left

    @property
    def right(self):
        return self._right

    @property
    def top(self):
        return self._top

    @property
    def bottom(self):
        return self._bottom

    @property
    def speed(self):
        return self._speed

    @pos.setter
    def pos(self, pos):
        self._pos = pos

    @left.setter
    def left(self, left):
        self._left = left

    @right.setter
    def right(self, right):
        self._right = right

    @top.setter
    def top(self, top):
        self._top = top

    @bottom.setter
    def bottom(self, bottom):
        self._bottom = bottom

    @speed.setter
    def speed(self, speed):
        self._speed = speed

    def move(self):
        self.pos = [self.pos[0], self.pos[1] - self.speed]
        self.top = self.top - self.speed
        self.bottom = self.bottom - self.speed