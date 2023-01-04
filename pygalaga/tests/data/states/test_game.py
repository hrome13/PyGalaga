import unittest
from pygalaga.data.classes.player import Player
from pygalaga.data.states.game import collides,  play_game

class TestGame(unittest.TestCase):
    def test_collides_1_all_in_2_x(self):
        pos1 = [10, 10]
        pos2 = [11, 12]
        width1, height1 = 10, 10
        width2, height2 = 3, 7
        speed = 1
        obj1 = Player(pos1, width1, height1, speed)
        obj2 = Player(pos2, width2, height2, speed)

        result = collides(obj1, obj2)
        self.assertTrue(result)

    def test_collides_1_partly_in_2_x(self):
        pos1 = [10, 10]
        pos2 = [9, 12]
        width1, height1 = 10, 10
        width2, height2 = 3, 7
        speed = 1
        obj1 = Player(pos1, width1, height1, speed)
        obj2 = Player(pos2, width2, height2, speed)

        result = collides(obj1, obj2)
        self.assertTrue(result)

    def test_collides_1_all_in_2_y(self):
        pos1 = [10, 10]
        pos2 = [12, 11]
        width1, height1 = 10, 10
        width2, height2 = 7, 3
        speed = 1
        obj1 = Player(pos1, width1, height1, speed)
        obj2 = Player(pos2, width2, height2, speed)

        result = collides(obj1, obj2)
        self.assertTrue(result)

    def test_collides_1_partly_in_2_y(self):
        pos1 = [10, 10]
        pos2 = [12, 9]
        width1, height1 = 10, 10
        width2, height2 = 7, 3
        speed = 1
        obj1 = Player(pos1, width1, height1, speed)
        obj2 = Player(pos2, width2, height2, speed)

        result = collides(obj1, obj2)
        self.assertTrue(result)

    def test_collides_2_all_in_1_x(self):
        pos1 = [10, 10]
        pos2 = [11, 12]
        width1, height1 = 10, 10
        width2, height2 = 3, 7
        speed = 1
        obj1 = Player(pos1, width1, height1, speed)
        obj2 = Player(pos2, width2, height2, speed)

        result = collides(obj2, obj1)
        self.assertTrue(result)

    def test_collides_2_partly_in_1_x(self):
        pos1 = [10, 10]
        pos2 = [9, 12]
        width1, height1 = 10, 10
        width2, height2 = 3, 7
        speed = 1
        obj1 = Player(pos1, width1, height1, speed)
        obj2 = Player(pos2, width2, height2, speed)

        result = collides(obj2, obj1)
        self.assertTrue(result)

    def test_collides_2_all_in_1_y(self):
        pos1 = [10, 10]
        pos2 = [12, 11]
        width1, height1 = 10, 10
        width2, height2 = 7, 3
        speed = 1
        obj1 = Player(pos1, width1, height1, speed)
        obj2 = Player(pos2, width2, height2, speed)

        result = collides(obj2, obj1)
        self.assertTrue(result)

    def test_collides_2_partly_in_1_y(self):
        pos1 = [10, 10]
        pos2 = [12, 9]
        width1, height1 = 10, 10
        width2, height2 = 7, 3
        speed = 1
        obj1 = Player(pos1, width1, height1, speed)
        obj2 = Player(pos2, width2, height2, speed)

        result = collides(obj2, obj1)
        self.assertTrue(result)

    def test_collides_false(self):
        pos1 = [10, 10]
        pos2 = [22, 22]
        width1, height1 = 10, 10
        width2, height2 = 7, 3
        speed = 1
        obj1 = Player(pos1, width1, height1, speed)
        obj2 = Player(pos2, width2, height2, speed)

        result = collides(obj1, obj2)
        self.assertFalse(result)

    def test_play_game_one_player_win(self):
        pass

    def test_play_game_one_player_loss(self):
        pass

    def test_play_game_two_player_win(self):
        pass

    def test_play_game_two_player_loss(self):
        pass

    def test_play_game_wrong_num_players(self):
        pass