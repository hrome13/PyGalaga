import unittest
from pygalaga.data.classes.player import Player

class TestPlayer(unittest.TestCase):
    def test_move_left(self):
        pos = [20,20]
        width, height = 5, 5
        speed = 2
        player = Player(pos, width, height, speed)
        player.move_left()

        self.assertEqual(player.pos, [18, 20])
        self.assertEqual(player.left, 18)
        self.assertEqual(player.right, 23)
        self.assertEqual(player.top, 20)
        self.assertEqual(player.bottom, 25)

    def test_move_right(self):
        pos = [20,20]
        width, height = 5, 5
        speed = 2
        player = Player(pos, width, height, speed)
        player.move_right()

        self.assertEqual(player.pos, [22, 20])
        self.assertEqual(player.left, 22)
        self.assertEqual(player.right, 27)
        self.assertEqual(player.top, 20)
        self.assertEqual(player.bottom, 25)

    def test_move_up(self):
        pos = [20,20]
        width, height = 5, 5
        speed = 2
        player = Player(pos, width, height, speed)
        player.move_up()

        self.assertEqual(player.pos, [20, 18])
        self.assertEqual(player.left, 20)
        self.assertEqual(player.right, 25)
        self.assertEqual(player.top, 18)
        self.assertEqual(player.bottom, 23)

    def test_move_down(self):
        pos = [20,20]
        width, height = 5, 5
        speed = 2
        player = Player(pos, width, height, speed)
        player.move_down()

        self.assertEqual(player.pos, [20, 22])
        self.assertEqual(player.left, 20)
        self.assertEqual(player.right, 25)
        self.assertEqual(player.top, 22)
        self.assertEqual(player.bottom, 27)

if __name__ == '__main__':
    unittest.main()