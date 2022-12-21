from ..classes import player
import pygame

class Player2(player.Player):
    def __init__(self, pos, width, height, speed):
        super().__init__(pos, width, height, speed)

    def move(self, keys):
        # check if the right arrow key is pressed
        if keys[pygame.K_d]:
            # if it is, move the player to the right
            self.pos[0] += self.speed
            self.left += self.speed
            self.right += self.speed
        # check if the left arrow key is pressed
        if keys[pygame.K_a]:
            # if it is, move the player to the left
            self.pos[0] -= self.speed
            self.left -= self.speed
            self.right -= self.speed
        # check if the up arrow key is pressed
        if keys[pygame.K_w]:
            # if it is, move the player up
            self.pos[1] -= self.speed
            self.top -= self.speed
            self.bottom -= self.speed
        # check if the down arrow key is pressed
        if keys[pygame.K_s]:
            # if it is, move the player down
            self.pos[1] += self.speed
            self.top += self.speed
            self.bottom += self.speed

    def took_shot(self, keys):
        return keys[pygame.K_LSHIFT]