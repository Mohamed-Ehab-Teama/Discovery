import pygame

pygame.init()

screen = pygame.display.set_mode( (400,400) )
pygame.display.set_caption( 'Sesion 02 PYGAME' )

icon = pygame.image.load('Yamamoto .jpg')
pygame.display.set_icon(icon)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            
    screen.fill('aqua')
    
    pygame.draw.circle(screen, 'black', (200,200), 200 , 2 )
    pygame.draw.line(screen, "black", (200,200) , (200,0), 4 )
    pygame.draw.line(screen, "black", (200,200) , (360,320), 4 )
    pygame.draw.line(screen, "black", (200,200) , (40, 320), 4 )
    
    # pygame.draw.line(screen, 'black', (600,0) , (0,500), 15)
    # pygame.draw.line(screen, "red", (0,0), (600,500), 15 )
    # pygame.draw.line(screen, 'blue', (300,0), (300,500), 15)
    # pygame.draw.line(screen, 'orange', (0,250), (600,250), 15)
    
    # pygame.draw.rect(screen, 'red', (50,50,300,200), 5, 0, 50, 50, 120, 120 )
    
    # pygame.draw.circle(screen, "yellow", (250,250), 100, 10, True, False, True)
    
    # pygame.draw.polygon(screen, "red", [ (20,50), (100,120), (250,300), (10,150) ], 10)
    
    
    pygame.display.flip()