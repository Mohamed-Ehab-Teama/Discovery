import pygame

pygame.init()

screen = pygame.display.set_mode( (500,450) )
pygame.display.set_caption(' Session 01 Introduction ')

myIcon = pygame.image.load('Yamamoto .jpg')
pygame.display.set_icon( myIcon )

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            
    screen.fill( 'gold' )

    pygame.display.flip()