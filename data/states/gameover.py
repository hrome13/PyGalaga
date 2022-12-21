import pygame as pg

LEFT = 1

def win_screen():
    # set up the screen
    screen = pg.display.set_mode((400, 300), pg.RESIZABLE)

    # set the title of the window
    pg.display.set_caption('Winner!')

    # define colors
    black = (0, 0, 0)
    green = (40, 200, 150)
    blue = (30, 50, 200)
    white = (255, 255, 255)
    red = (255, 0, 0)
    pass

def lose_screen():
    # set up the screen
    screen = pg.display.set_mode((400, 300), pg.RESIZABLE)

    # set the title of the window
    pg.display.set_caption('Loser :(')

    # define colors
    black = (0, 0, 0)
    green = (40, 200, 150)
    blue = (30, 50, 200)
    white = (255, 255, 255)
    red = (255, 0, 0)

    running = True

    while running:

        # check for events
        for event in pg.event.get():
            state = pg.mouse.get_pressed()
            if event.type == pg.QUIT:
                # if it is, stop the loop
                running = False
            elif event.type == pg.MOUSEBUTTONDOWN and event.button == LEFT:
                running = False
        
        screen.fill(white)

        pg.display.update()
    
    # quit Pygame
    pg.quit()