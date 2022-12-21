import pygame

class Player:
    def __init__(self, pos, width, height, speed):
        self.pos = pos
        self.left = pos[0]
        self.right = pos[0] + width
        self.top = pos[1]
        self.bottom = pos[1] + height
        self.speed = speed

    def pos(self):
        return self.pos

    def left(self):
        return self.left

    def right(self):
        return self.right

    def top(self):
        return self.top

    def bottom(self):
        return self.bottom

    def speed(self):
        return self.speed

    def update_speed(self, new_speed):
        self.speed = new_speed