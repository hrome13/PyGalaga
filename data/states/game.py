import pygame as pg

from ..classes import enemy, player1, player2, projectile


def collides(obj1, obj2):
    # Detect if two objects collide
    if obj1.top > obj2.top and obj1.top < obj2.bottom:
        return (obj1.left > obj2.left and obj1.left < obj2.right) or (obj1.right < obj2.right and obj1.right > obj2.left)
    elif obj1.bottom < obj2.bottom and obj1.bottom > obj2.top:
        return (obj1.left > obj2.left and obj1.left < obj2.right) or (obj1.right < obj2.right and obj1.right > obj2.left)


def play_game():

    # initialize Pygame
    # pg.init()

    # pg.mixer.pre_init()

    #then instantiate and start your controller
    # pg.mixer.init()

    # set up the screen
    screen = pg.display.set_mode((400, 300), pg.RESIZABLE)

    # set the title of the window
    # pg.display.set_caption('PyGalaga')

    # define colors
    black = (0, 0, 0)
    green = (40, 200, 150)
    blue = (30, 50, 200)
    white = (255, 255, 255)
    red = (255, 0, 0)

    # initialize the player's position
    player_pos = [[250, 250], [150, 250]]
    player_width = 10
    player_height = 10
    player_speed = 0.1
    player1_ = player1.Player1(player_pos[0], player_width, player_height, player_speed)
    player2_ = player2.Player2(player_pos[1], player_width, player_height, player_speed)
    players = [player1_, player2_]

    # initialize the list of projectiles
    projectiles = []
    projectile_height = 9
    projectile_width = 3
    projectile_speed = 0.5

    # initialize the list of enemies
    enemy_pos = [[50, 0], [100,0],[150, 0], [200, 0], [250, 0], [300, 0], [350, 0]]
    enemy_width = 20
    enemy_height = 10
    enemies = []
    for pos in enemy_pos:
        enemies.append(enemy.Enemy(pos, enemy_width, enemy_height))

    # initialize the game loop
    running = True
    
    while running:
        player1_, player2_ = players

        # check for events
        for event in pg.event.get():
            # check if the event is the X button 
            if event.type == pg.QUIT:
                # if it is, stop the loop
                running = False

            # check if a key is pressed
            elif event.type == pg.KEYDOWN:
                keys = pg.key.get_pressed()
                # check if the space bar is pressed
                if player1_.took_shot(keys):
                    # if it is, create a new projectile at player1's position
                    projectiles.append(projectile.Projectile([player1_.left + player_width/2 - projectile_width/2, player1_.top], 
                                                projectile_width, projectile_height, projectile_speed))
                    pg.mixer.music.load('resources/soundeffects/pew.mp3')
                    pg.mixer.music.play()
                # check if the left shift key is pressed
                if player2_.took_shot(keys):
                    # if it is, create a new projectile at player2's position
                    projectiles.append(projectile.Projectile([player2_.left + player_width/2 - projectile_width/2, player2_.top], 
                                                projectile_width, projectile_height, projectile_speed))
                    pg.mixer.music.load('resources/soundeffects/pew.mp3')
                    pg.mixer.music.play()

        # get the state of the keys
        keys = pg.key.get_pressed()

        # PLAYER 1 MOVEMENT
        player1_.move(keys)

        # PLAYER 2 MOVEMENT
        player2_.move(keys)

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
        pg.draw.rect(screen, blue, pg.Rect(player1_.left, player1_.top, player_width, player_height))
        pg.draw.rect(screen, green, pg.Rect(player2_.left, player2_.top, player_width, player_height))

        # draw each projectile on the screen
        for projectile_ in projectiles:
            pg.draw.rect(screen, black, pg.Rect(projectile_.left, projectile_.top, projectile_width, projectile_height))
        
        # draw each enemy on the screen
        for enemy_ in enemies:
            if collides(enemy_, player1_) or collides(enemy_, player2_):
                return "loss"
            pg.draw.rect(screen, red, pg.Rect(enemy_.left, enemy_.top, enemy_width, enemy_height))

        # update the display
        pg.display.update()


    # # quit Pygame
    pg.quit()