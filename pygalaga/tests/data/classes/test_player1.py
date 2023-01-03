import unittest
import pygame
from pygalaga.data.classes.player1 import Player1

class TestPlayer1(unittest.TestCase):
    """
    Test cases for move():
        - Move left (keypress is left arrow)
        - Move right (keypress is right arrow)
        - Move up (keypress is up arrow)
        - Move down (keypress is down arrow)

        - Move in two opposite directions (i.e. don't move)
        - Move in two perpendicular directions
        - Move in three directions
        - Move in all directions (i.e. don't move)

        - No keys pressed
        - Non-arrow keys pressed

    Test cases for took_shot():
        - No keys pressed
        - A key other than space-bar is pressed
        - Space-bar is pressed
    """
    
    def test_move_left(self):
        pos = [20,20]
        width, height = 5, 5
        speed = 2
        player1 = Player1(pos, width, height, speed)
        keys = {pygame.K_LEFT: True}
        player1.move(keys)

        self.assertEqual(player1.pos, [18, 20])
        self.assertEqual(player1.left, 18)
        self.assertEqual(player1.right, 23)
        self.assertEqual(player1.top, 20)
        self.assertEqual(player1.bottom, 25)

    def test_move_right(self):
        pos = [20,20]
        width, height = 5, 5
        speed = 2
        player1 = Player1(pos, width, height, speed)
        keys = {pygame.K_RIGHT: True}
        player1.move(keys)

        self.assertEqual(player1.pos, [22, 20])
        self.assertEqual(player1.left, 22)
        self.assertEqual(player1.right, 27)
        self.assertEqual(player1.top, 20)
        self.assertEqual(player1.bottom, 25)

    def test_move_up(self):
        pos = [20,20]
        width, height = 5, 5
        speed = 2
        player1 = Player1(pos, width, height, speed)
        keys = {pygame.K_UP: True}
        player1.move(keys)

        self.assertEqual(player1.pos, [20, 18])
        self.assertEqual(player1.left, 20)
        self.assertEqual(player1.right, 25)
        self.assertEqual(player1.top, 18)
        self.assertEqual(player1.bottom, 23)

    def test_move_down(self):
        pos = [20,20]
        width, height = 5, 5
        speed = 2
        player1 = Player1(pos, width, height, speed)
        keys = {pygame.K_DOWN: True}
        player1.move(keys)

        self.assertEqual(player1.pos, [20, 22])
        self.assertEqual(player1.left, 20)
        self.assertEqual(player1.right, 25)
        self.assertEqual(player1.top, 22)
        self.assertEqual(player1.bottom, 27)

    def test_move_no_keys_pressed(self):
        pos = [20,20]
        width, height = 5, 5
        speed = 2
        player1 = Player1(pos, width, height, speed)
        keys = {}
        player1.move(keys)

        self.assertEqual(player1.pos, [20, 20])
        self.assertEqual(player1.left, 20)
        self.assertEqual(player1.right, 25)
        self.assertEqual(player1.top, 20)
        self.assertEqual(player1.bottom, 25)

    def test_move_other_keys_pressed(self):
        pos = [20,20]
        width, height = 5, 5
        speed = 2
        player1 = Player1(pos, width, height, speed)
        keys = {pygame.K_w: True}
        player1.move(keys)

        self.assertEqual(player1.pos, [20, 20])
        self.assertEqual(player1.left, 20)
        self.assertEqual(player1.right, 25)
        self.assertEqual(player1.top, 20)
        self.assertEqual(player1.bottom, 25)

    def test_move_two_opposite_directions(self):
        pos = [20,20]
        width, height = 5, 5
        speed = 2
        player1 = Player1(pos, width, height, speed)
        keys = {pygame.K_UP: True,
                pygame.K_DOWN: True}
        player1.move(keys)

        self.assertEqual(player1.pos, [20, 20])
        self.assertEqual(player1.left, 20)
        self.assertEqual(player1.right, 25)
        self.assertEqual(player1.top, 20)
        self.assertEqual(player1.bottom, 25)

    def test_move_two_perpendicular_directions(self):
        pos = [20,20]
        width, height = 5, 5
        speed = 2
        player1 = Player1(pos, width, height, speed)
        keys = {pygame.K_DOWN: True,
                pygame.K_LEFT: True}
        player1.move(keys)

        self.assertEqual(player1.pos, [18, 22])
        self.assertEqual(player1.left, 18)
        self.assertEqual(player1.right, 23)
        self.assertEqual(player1.top, 22)
        self.assertEqual(player1.bottom, 27)

    def test_move_three_directions(self):
        pos = [20,20]
        width, height = 5, 5
        speed = 2
        player1 = Player1(pos, width, height, speed)
        keys = {pygame.K_DOWN: True,
                pygame.K_LEFT: True,
                pygame.K_RIGHT: True}
        player1.move(keys)

        self.assertEqual(player1.pos, [20, 22])
        self.assertEqual(player1.left, 20)
        self.assertEqual(player1.right, 25)
        self.assertEqual(player1.top, 22)
        self.assertEqual(player1.bottom, 27)

    def test_move_all_directions(self):
        pos = [20,20]
        width, height = 5, 5
        speed = 2
        player1 = Player1(pos, width, height, speed)
        keys = {pygame.K_UP: True,
                pygame.K_DOWN: True,
                pygame.K_LEFT: True,
                pygame.K_RIGHT: True}
        player1.move(keys)

        self.assertEqual(player1.pos, [20, 20])
        self.assertEqual(player1.left, 20)
        self.assertEqual(player1.right, 25)
        self.assertEqual(player1.top, 20)
        self.assertEqual(player1.bottom, 25)

    def test_took_shot_no_keys_pressed(self):
        pos = [20,20]
        width, height = 5, 5
        speed = 2
        player1 = Player1(pos, width, height, speed)
        keys = {}

        result = player1.took_shot(keys)
        self.assertFalse(result)

    def test_took_shot_other_keys_pressed(self):
        pos = [20,20]
        width, height = 5, 5
        speed = 2
        player1 = Player1(pos, width, height, speed)
        keys = {pygame.K_0: True,
                pygame.K_LEFT: True}

        result = player1.took_shot(keys)
        self.assertFalse(result)

    def test_took_shot_spacebar_pressed(self):
        pos = [20,20]
        width, height = 5, 5
        speed = 2
        player1 = Player1(pos, width, height, speed)
        keys = {pygame.K_SPACE: True}

        result = player1.took_shot(keys)
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()