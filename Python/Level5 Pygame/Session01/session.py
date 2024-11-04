import pygame

pygame.init()

# Set Width and height of the game window
screen = pygame.display.set_mode( (500,400) )
# Set the Title of the game Window
pygame.display.set_caption( ' My First Game ' )

# Set Icon For the Game Window
myIcon = pygame.image.load('Yamamoto .jpg')
pygame.display.set_icon(myIcon)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    

    screen.fill( 'violet' )


    pygame.display.flip()
