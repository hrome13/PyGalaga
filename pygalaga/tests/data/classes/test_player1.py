import unittest
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
    
    def test_move_left():
        pass

    def test_move_right():
        pass

    def test_move_up():
        pass

    def test_move_down():
        pass

    def test_move_no_keys_pressed():
        pass

    def test_move_other_keys_pressed():
        pass

    def test_move_two_opposite_directions():
        pass

    def test_move_two_perpendicular_directions():
        pass

    def test_move_three_directions():
        pass

    def test_move_all_directions():
        pass

    def test_took_shot_no_keys_pressed():
        pass

    def test_took_shot_other_keys_pressed():
        pass

    def test_took_shot_spacebar_pressed():
        pass