import pygame as pg

LEFT = 1

# define colors
black = (0, 0, 0)
green = (40, 200, 150)
blue = (30, 50, 200)
white = (255, 255, 255)
red = (255, 0, 0)

def win_screen():
    # set up the screen
    screen = pg.display.set_mode((400, 300), pg.RESIZABLE)

    # set the title of the window
    pg.display.set_caption('Winner :D')

    # defining a font
    smallfont = pg.font.SysFont('Corbel',45)
    
    # render victory text
    text = smallfont.render('Congrats! You won!' , True , black)

    # fill screen with white
    screen.fill(white)

    # get the rectangle for the text surface
    text_rect = text.get_rect()

    # center the text on the screen
    text_rect.center = (screen.get_width() // 2, screen.get_height() // 2)

    # blit the text surface onto the screen
    screen.blit(text, text_rect)

    pg.display.update()

    running = True

    while running:

        # check for events
        for event in pg.event.get():
            if event.type == pg.QUIT:
                # if it is, stop the loop
                running = False
    
    pg.quit()
    return

def lose_screen():
    # set up the screen
    screen = pg.display.set_mode((400, 300), pg.RESIZABLE)

    # set the title of the window
    pg.display.set_caption('Loser :(')

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