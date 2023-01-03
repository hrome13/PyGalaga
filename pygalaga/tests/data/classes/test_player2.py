import unittest
import pygame
from pygalaga.data.classes.player2 import Player2

class TestPlayer2(unittest.TestCase):
    """
    Test cases for move():
        - Move left (keypress is A)
        - Move right (keypress is D)
        - Move up (keypress is W)
        - Move down (keypress is S)

        - Move in two opposite directions (i.e. don't move)
        - Move in two perpendicular directions
        - Move in three directions
        - Move in all directions (i.e. don't move)

        - No keys pressed
        - Non-arrow keys pressed

    Test cases for took_shot():
        - No keys pressed
        - A key other than LSHIFT is pressed
        - LSHIFT is pressed
    """
    
    def test_move_left(self):
        pos = [20,20]
        width, height = 5, 5
        speed = 2
        player2 = Player2(pos, width, height, speed)
        keys = {pygame.K_a: True}
        player2.move(keys)

        self.assertEqual(player2.pos, [18, 20])
        self.assertEqual(player2.left, 18)
        self.assertEqual(player2.right, 23)
        self.assertEqual(player2.top, 20)
        self.assertEqual(player2.bottom, 25)

    def test_move_right(self):
        pos = [20,20]
        width, height = 5, 5
        speed = 2
        player2 = Player2(pos, width, height, speed)
        keys = {pygame.K_d: True}
        player2.move(keys)

        self.assertEqual(player2.pos, [22, 20])
        self.assertEqual(player2.left, 22)
        self.assertEqual(player2.right, 27)
        self.assertEqual(player2.top, 20)
        self.assertEqual(player2.bottom, 25)

    def test_move_up(self):
        pos = [20,20]
        width, height = 5, 5
        speed = 2
        player2 = Player2(pos, width, height, speed)
        keys = {pygame.K_w: True}
        player2.move(keys)

        self.assertEqual(player2.pos, [20, 18])
        self.assertEqual(player2.left, 20)
        self.assertEqual(player2.right, 25)
        self.assertEqual(player2.top, 18)
        self.assertEqual(player2.bottom, 23)

    def test_move_down(self):
        pos = [20,20]
        width, height = 5, 5
        speed = 2
        player2 = Player2(pos, width, height, speed)
        keys = {pygame.K_s: True}
        player2.move(keys)

        self.assertEqual(player2.pos, [20, 22])
        self.assertEqual(player2.left, 20)
        self.assertEqual(player2.right, 25)
        self.assertEqual(player2.top, 22)
        self.assertEqual(player2.bottom, 27)

    def test_move_no_keys_pressed(self):
        pos = [20,20]
        width, height = 5, 5
        speed = 2
        player2 = Player2(pos, width, height, speed)
        keys = {}
        player2.move(keys)

        self.assertEqual(player2.pos, [20, 20])
        self.assertEqual(player2.left, 20)
        self.assertEqual(player2.right, 25)
        self.assertEqual(player2.top, 20)
        self.assertEqual(player2.bottom, 25)

    def test_move_other_keys_pressed(self):
        pos = [20,20]
        width, height = 5, 5
        speed = 2
        player2 = Player2(pos, width, height, speed)
        keys = {pygame.K_RIGHT: True}
        player2.move(keys)

        self.assertEqual(player2.pos, [20, 20])
        self.assertEqual(player2.left, 20)
        self.assertEqual(player2.right, 25)
        self.assertEqual(player2.top, 20)
        self.assertEqual(player2.bottom, 25)

    def test_move_two_opposite_directions(self):
        pos = [20,20]
        width, height = 5, 5
        speed = 2
        player2 = Player2(pos, width, height, speed)
        keys = {pygame.K_w: True,
                pygame.K_s: True}
        player2.move(keys)

        self.assertEqual(player2.pos, [20, 20])
        self.assertEqual(player2.left, 20)
        self.assertEqual(player2.right, 25)
        self.assertEqual(player2.top, 20)
        self.assertEqual(player2.bottom, 25)

    def test_move_two_perpendicular_directions(self):
        pos = [20,20]
        width, height = 5, 5
        speed = 2
        player2 = Player2(pos, width, height, speed)
        keys = {pygame.K_s: True,
                pygame.K_a: True}
        player2.move(keys)

        self.assertEqual(player2.pos, [18, 22])
        self.assertEqual(player2.left, 18)
        self.assertEqual(player2.right, 23)
        self.assertEqual(player2.top, 22)
        self.assertEqual(player2.bottom, 27)

    def test_move_three_directions(self):
        pos = [20,20]
        width, height = 5, 5
        speed = 2
        player2 = Player2(pos, width, height, speed)
        keys = {pygame.K_s: True,
                pygame.K_a: True,
                pygame.K_d: True}
        player2.move(keys)

        self.assertEqual(player2.pos, [20, 22])
        self.assertEqual(player2.left, 20)
        self.assertEqual(player2.right, 25)
        self.assertEqual(player2.top, 22)
        self.assertEqual(player2.bottom, 27)

    def test_move_all_directions(self):
        pos = [20,20]
        width, height = 5, 5
        speed = 2
        player2 = Player2(pos, width, height, speed)
        keys = {pygame.K_w: True,
                pygame.K_s: True,
                pygame.K_a: True,
                pygame.K_d: True}
        player2.move(keys)

        self.assertEqual(player2.pos, [20, 20])
        self.assertEqual(player2.left, 20)
        self.assertEqual(player2.right, 25)
        self.assertEqual(player2.top, 20)
        self.assertEqual(player2.bottom, 25)

    def test_took_shot_no_keys_pressed(self):
        pos = [20,20]
        width, height = 5, 5
        speed = 2
        player2 = Player2(pos, width, height, speed)
        keys = {}

        result = player2.took_shot(keys)
        self.assertFalse(result)

    def test_took_shot_other_keys_pressed(self):
        pos = [20,20]
        width, height = 5, 5
        speed = 2
        player2 = Player2(pos, width, height, speed)
        keys = {pygame.K_0: True,
                pygame.K_SPACE: True}

        result = player2.took_shot(keys)
        self.assertFalse(result)

    def test_took_shot_spacebar_pressed(self):
        pos = [20,20]
        width, height = 5, 5
        speed = 2
        player2 = Player2(pos, width, height, speed)
        keys = {pygame.K_LSHIFT: True}

        result = player2.took_shot(keys)
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()