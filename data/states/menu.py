import pygame as pg

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

# mouse button left click
LEFT = 1


# game loop
def display_menu():

    # initialize Pygame
    pg.init()

    pg.mixer.pre_init()

    #then instantiate and start your controller
    pg.mixer.init()

    # set up the screen
    screen = pg.display.set_mode((400, 300), pg.RESIZABLE)
    screen_width, screen_height = screen.get_size()

    # Define the dimensions and position of the start button
    button_width = screen_width // 2
    button_height = screen_height // 8
    button_x = (screen_width - button_width) // 2
    button_y = (screen_height - button_height) // 2

    # Create a surface for the start button
    one_player_surface = pg.Surface((button_width, button_height))
    two_player_surface = pg.Surface((button_width, button_height))

    # Fill the surface with a solid color
    one_player_surface.fill(color_light)
    two_player_surface.fill(color_light)

    # Create a rect for the start button
    one_player_rect = pg.Rect(button_x, button_y, button_width, button_height)
    two_player_rect = pg.Rect(button_x, button_y + button_height * 1.5, button_width, button_height)

    buttons = [(one_player_rect, one_player_surface), (two_player_rect, two_player_surface)]


    # defining a font
    smallfont = pg.font.SysFont('Corbel',35)
    
    # rendering a text written in
    # this font
    one_text = smallfont.render('1 Player' , True , black)
    two_text = smallfont.render('2 Players' , True , black)
    texts = [one_text, two_text]

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
                running = False
            elif event.type == pg.MOUSEBUTTONDOWN and event.button == LEFT:
                for i in range(len(buttons)):
                    button_rect, button_surface = buttons[i]
                    if button_rect.collidepoint(mouse[0], mouse[1]):
                        return i + 1

        # if mouse is hovered on a button it
        # changes to lighter shade 
        for button_rect, button_surface in buttons:
            if button_rect.collidepoint(mouse[0], mouse[1]):
                # Change the appearance of the button to give the appearance of a hover state
                button_surface.fill(color_dark)
            else:
                # Reset the appearance of the button
                button_surface.fill(color_light)
        
        # draw the buttons
        for button_rect, button_surface in buttons:
            screen.blit(button_surface, (button_rect.left, button_rect.top))

        # superimposing the text onto our button
        for i in range(len(texts)):
            text = texts[i]
            text_x = (screen_width - text.get_width()) // 2
            if i == 0:
                text_y = (screen_height - text.get_height()) // 2
            elif i == 1:
                text_y = (screen_height - text.get_height()) // 2 + button_height * 1.5
            screen.blit(text, (text_x, text_y))

        pg.display.update()
        

    # quit Pygame
    pg.quit()
    return 0