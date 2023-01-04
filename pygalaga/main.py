from data.states.game import play_game
from data.states.menu import display_menu
from data.states.gameover import win_screen, lose_screen

num_players = display_menu()
if num_players > 0:
    game_result = play_game(num_players)
    if game_result == "win":
        win_screen()
        print("You won!")
    elif game_result == "loss":
        lose_screen()
        print("You lost!")