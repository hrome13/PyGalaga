import pygame as pg
from ..classes import enemy, player1, player2, projectile


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


def collides(obj1, obj2):
    # Detect if two objects collide
    if obj1.top > obj2.top and obj1.top < obj2.bottom:
        return (obj1.left > obj2.left and obj1.left < obj2.right) or (obj1.right < obj2.right and obj1.right > obj2.left)
    elif obj1.bottom < obj2.bottom and obj1.bottom > obj2.top:
        return (obj1.left > obj2.left and obj1.left < obj2.right) or (obj1.right < obj2.right and obj1.right > obj2.left)


def play_game(num_players):

    # set up the screen
    screen = pg.display.set_mode((400, 300), pg.RESIZABLE)

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
        pg.quit()
        return

    # initialize the list of projectiles
    projectiles = []

    # initialize the list of enemies
    enemy_pos = [[50, 0], [100,0],[150, 0], [200, 0], [250, 0], [300, 0], [350, 0]]
    enemies = []
    for pos in enemy_pos:
        enemies.append(enemy.Enemy(pos, enemy_width, enemy_height))

    # initialize the game loop
    running = True
    
    while running:

        # check for events
        for event in pg.event.get():
            # check if the event is the X button 
            if event.type == pg.QUIT:
                # if it is, stop the loop
                running = False

            # check if a key is pressed
            elif event.type == pg.KEYDOWN:
                keys = pg.key.get_pressed()
                # check if a player shot
                for player in players:
                    if player.took_shot(keys):
                        # if it is, create a new projectile at the player's position
                        projectiles.append(projectile.Projectile([player.left + player_width/2 - projectile_width/2, player.top], 
                                                    projectile_width, projectile_height, projectile_speed))
                        pg.mixer.music.load('resources/soundeffects/pew.mp3')
                        pg.mixer.music.play()

        # get the state of the keys
        keys = pg.key.get_pressed()

        # move the players
        for player in players:
            player.move(keys)

        # fill the screen with white
        screen.fill(white)

        # move the projectiles, checking if they hit enemies
        for projectile_ in projectiles:
            projectile_.move()
            if projectile_.bottom < 0:
                projectiles.remove(projectile_)
            for enemy_ in enemies:
                if collides(projectile_, enemy_):
                    pg.mixer.music.load('resources/soundeffects/Explosions/Short/sfx_exp_short_hard6.wav')
                    pg.mixer.music.play()
                    enemies.remove(enemy_)
                    projectiles.remove(projectile_)
                    if len(enemies) == 0:
                        return "win"

        # draw each player on the screen
        for player in players:
            pg.draw.rect(screen, blue, pg.Rect(player.left, player.top, player_width, player_height))

        # draw each projectile on the screen
        for projectile_ in projectiles:
            pg.draw.rect(screen, black, pg.Rect(projectile_.left, projectile_.top, projectile_width, projectile_height))
        
        # draw each enemy on the screen
        for enemy_ in enemies:
            for player in players:
                if collides(enemy_, player):
                    return "loss"
            pg.draw.rect(screen, red, pg.Rect(enemy_.left, enemy_.top, enemy_width, enemy_height))

        # update the display
        pg.display.update()

    # quit Pygame
    pg.quit()