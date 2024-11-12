# An event is an action that is performed by the user in order to get the desired result.
# pygame.event.get()    => get events from the queue

# KEYDOWN: When a key is pressed down
# KEYUP: When the key is released



import pygame

pygame.init()

screen = pygame.display.set_mode((600,400))
pygame.display.set_caption("Session 03 - Python - Pygame")

icon = pygame.image.load('./Session03/icon.jpg')
pygame.display.set_icon(icon)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            
    screen.fill("aqua")
    
    
    
    
    
    pygame.display.flip()