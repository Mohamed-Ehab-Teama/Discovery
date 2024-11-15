
import pygame

pygame.init()

screen = pygame.display.set_mode((400,400))
pygame.display.set_caption("Session 03")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            
        if event.type == pygame.KEYDOWN:
            key = pygame.key.name( event.key )
            print ( key , " is pressed " )
        
        if event.type == pygame.KEYUP:
            key = pygame.key.name (event.key)
            print ( key , " is Released ")
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 :
                print ( "Left Click Pressed" , event.pos )
            if event.button == 3:
                print ( "Right Click Pressed" , event.pos)
                
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1 :
                print ( "Left Click Released" , event.pos )
            if event.button == 3:
                print ( "Right Click Released" , event.pos)
                
        if event.type == pygame.MOUSEMOTION:
            x , y = event.pos
            print ( x,y, event.pos )
                  
            
            
            
    
    screen.fill('aqua')
    
    pygame.display.flip()