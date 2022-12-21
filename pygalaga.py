from data.states.game import play_game
from data.states.menu import display_menu
from data.states.gameover import win_screen, lose_screen

if display_menu():
    if play_game():
        win_screen()
        print("You won!")
    else:
        lose_screen()
        print("You lost!")