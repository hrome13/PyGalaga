from data.states.game import play_game
from data.states.menu import display_menu
from data.states.gameover import win_screen, lose_screen
import pygame as pg

if display_menu():
    game_result = play_game()
    if game_result == "win":
        win_screen()
        print("You won!")
    elif game_result == "loss":
        lose_screen()
        print("You lost!")