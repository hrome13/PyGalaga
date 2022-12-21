import pygame as pg


# game loop
def display_menu():

    # initialize Pygame
    pg.init()

    pg.mixer.pre_init()

    #then instantiate and start your controller
    pg.mixer.init()


    # light shade of the button
    color_light = (170,170,170)
    
    # dark shade of the button
    color_dark = (100,100,100)

    # define colors
    black = (0, 0, 0)
    green = (40, 200, 150)
    blue = (30, 50, 200)
    white = (255, 255, 255)
    red = (255, 0, 0)
    LEFT = 1

    # set up the screen
    screen = pg.display.set_mode((400, 300), pg.RESIZABLE)
    screen_width, screen_height = screen.get_size()

    # Define the dimensions and position of the start button
    button_width = screen_width // 2
    button_height = screen_height // 8
    button_x = (screen_width - button_width) // 2
    button_y = (screen_height - button_height) // 2

    # Create a surface for the start button
    button_surface = pg.Surface((button_width, button_height))

    # Create a rect for the start button
    button_rect = pg.Rect(button_x, button_y, button_width, button_height)

    # Fill the surface with a solid color
    button_surface.fill(color_light)

    # stores the width of the
    # screen into a variable
    width = screen.get_width()
    
    # stores the height of the
    # screen into a variable
    height = screen.get_height()


    # defining a font
    smallfont = pg.font.SysFont('Corbel',35)
    
    # rendering a text written in
    # this font
    text = smallfont.render('Start' , True , black)
    text_width, text_height = text.get_size()
    print(text.get_size())

    # set the title of the window
    pg.display.set_caption('PyGalaga')

    running = True

    screen.fill(white)

    
    while running:
        mouse = pg.mouse.get_pos()

        # check for events
        for event in pg.event.get():
            state = pg.mouse.get_pressed()
            if event.type == pg.QUIT:
                # if it is, stop the loop
                return False
            elif event.type == pg.MOUSEBUTTONDOWN and event.button == LEFT:
                if button_rect.collidepoint(mouse[0], mouse[1]):
                    return True

        # if mouse is hovered on a button it
        # changes to lighter shade 
        if button_rect.collidepoint(mouse[0], mouse[1]):
            # Change the appearance of the button to give the appearance of a hover state
            button_surface.fill(color_dark)
        else:
            # Reset the appearance of the button
            button_surface.fill(color_light)
        
        # draw the button
        screen.blit(button_surface, (button_x, button_y))

        # superimposing the text onto our button
        text_x = (screen_width - text_width) // 2
        text_y = (screen_height - text_height) // 2
        # print(text_x, text_y, button_x, button_y)
        screen.blit(text, (text_x, text_y))


        pg.display.update()
        


    # # quit Pygame
    # pg.quit()