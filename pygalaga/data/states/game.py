import pygame as pg
from ..classes import enemy, player1, player2, projectile
import os

sound_library = {}

# define colors
black = (0, 0, 0)
green = (40, 200, 150)
blue = (30, 50, 200)
white = (255, 255, 255)
red = (255, 0, 0)

# player attributes
player_width = 10
player_height = 10
player_speed = 0.1

# projectile attributes
projectile_height = 9
projectile_width = 3
projectile_speed = 0.5

# enemy attributes
enemy_width = 20
enemy_height = 10
enemy_speed = player_speed // 2


def collides(obj1, obj2):
    """Detect if two objects collide"""

    # li = top left of obji
    # ri = bottom right of obji
    l1 = obj1.left, obj1.top
    r1 = obj1.right, obj1.bottom
    l2 = obj2.left, obj2.top
    r2 = obj2.right, obj2.bottom

    # if rectangle has area 0, no overlap
    if l1[0] == r1[0] or l1[1] == r1[1] or r2[0] == l2[0] or l2[1] == r2[1]:
        return False
     
    # If one rectangle is on left side of other
    if l1[0] > r2[0] or l2[0] > r1[0]:
        return False
 
    # If one rectangle is above other
    if r1[1] < l2[1] or r2[1] < l1[1]:
        return False
 
    return True

def load_sounds():
    """Load all sounds from subdirectories in a dictionary"""

    global sound_library

    for name in os.listdir('pygalaga/resources/used'):

        if name.endswith('.wav') or name.endswith('.mp3'):
            key = name[:-4]
            sound_library[key] = pg.mixer.Sound(f'pygalaga/resources/used/{name}')


def play_game(num_players):

    global sound_library

    load_sounds()

    # set up the screen
    screen = pg.display.set_mode((400, 300), pg.RESIZABLE)

    # play the game music
    pg.mixer.Sound('pygalaga/resources/used/02 Eggy Toast - Ghost.mp3').play(loops = -1)

    if num_players == 1:
        player_pos = [screen.get_width() // 2, (screen.get_height() * 4) // 5]
        player1_ = player1.Player1(player_pos, player_width, player_height, player_speed)
        players = [player1_]
    elif num_players == 2:
        player_pos = [[250, 250], [150, 250]]
        player1_ = player1.Player1(player_pos[0], player_width, player_height, player_speed)
        player2_ = player2.Player2(player_pos[1], player_width, player_height, player_speed)
        players = [player1_, player2_]
    else:
        print(f"Number of players ({num_players}) not implemented.")
        pg.mixer.fadeout(500)
        pg.quit()
        return

    # initialize the list of projectiles
    projectiles = []

    # initialize the list of enemies
    enemy_pos = [[50, 0], [100,0],[150, 0], [200, 0], [250, 0], [300, 0], [350, 0]]
    enemies = []
    for pos in enemy_pos:
        enemies.append(enemy.Enemy(pos, enemy_width, enemy_height, enemy_speed))

    # initialize the game loop
    status = "playing"
    
    while status is "playing":

        # check for events
        for event in pg.event.get():
            # check if the event is the X button 
            if event.type == pg.QUIT:
                # if it is, stop the loop
                status = "quit"
                break

            # check if a key is pressed
            elif event.type == pg.KEYDOWN:
                keys = pg.key.get_pressed()
                # check if a player shot
                for player in players:
                    if player.took_shot(keys):
                        # if it is, create a new projectile at the player's position
                        projectiles.append(projectile.Projectile([player.left + player_width/2 - projectile_width/2, player.top], 
                                                    projectile_width, projectile_height, projectile_speed))
                        sound_library['pew'].play()

        # get the state of the keys
        keys = pg.key.get_pressed()

        # move the players
        for player_ in players:
            player_.move(keys)

        # fill the screen with white
        screen.fill(white)

        # move the projectiles, checking if they hit enemies
        for projectile_ in projectiles:
            projectile_.move()
            if projectile_.bottom < 0:
                projectiles.remove(projectile_)
            for enemy_ in enemies:
                if collides(projectile_, enemy_) or collides(enemy_, projectile_):
                    sound_library['sfx_exp_short_hard6'].play()

                    enemies.remove(enemy_)
                    projectiles.remove(projectile_)

                    # win if you shoot all enemies
                    if len(enemies) == 0:
                        status = "win"
                        break

        # draw each player on the screen
        for i in range(len(players)):
            player_ = players[i]
            if i == 0:
                color = blue
            elif i == 1:
                color = green
            else:
                color = black
            pg.draw.rect(screen, color, pg.Rect(player_.left, player_.top, player_width, player_height))

        # draw each projectile on the screen
        for projectile_ in projectiles:
            pg.draw.rect(screen, black, pg.Rect(projectile_.left, projectile_.top, projectile_width, projectile_height))
        
        # draw each enemy on the screen
        for enemy_ in enemies:
            for player_ in players:
                if collides(enemy_, player_) or collides(player_, enemy_):
                    status = "loss"
                    break

            pg.draw.rect(screen, red, pg.Rect(enemy_.left, enemy_.top, enemy_width, enemy_height))

        # update the display
        pg.display.update()

    if status is "quit":
        pg.quit()
        return
    else:
        pg.mixer.fadeout(500)
        return status