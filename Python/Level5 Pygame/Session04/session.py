import pygame

pygame.init()

screen = pygame.display.set_mode( (800,600) )
pygame.display.set_caption( " Session 04 " ) 

my_image = pygame.image.load('icon.jpg')

pygame.display.set_icon( my_image )

image = pygame.transform.scale ( my_image , (400,200) )

image = pygame.transform.rotate( image , 0 )

image = pygame.transform.flip( image , True , False )

image_rect = image.get_rect()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    mouse_x , mouse_y = pygame.mouse.get_pos()
    image_rect.center = (mouse_x , mouse_y)
    
    screen.fill('aqua')
    
    
    screen.blit( image, image_rect )
    # screen.blit( image , (0 , 0) )
    
    
    pygame.display.flip()