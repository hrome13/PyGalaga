import pygame

class Projectile:
    def __init__(self, pos, width, height, speed):
        self.pos = pos
        self.left = pos[0]
        self.right = pos[0] + width
        self.top = pos[1]
        self.bottom = pos[1] + height
        self.speed = speed

    def move(self):
        self.pos[1] -= self.speed
        self.top -= self.speed
        self.bottom -= self.speed