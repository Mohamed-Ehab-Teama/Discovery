# An event is an action that is performed by the user in order to get the desired result.
# pygame.event.get()    => get events from the queue
# pygame.event.get : retrieves all the events from the event queue and returns them as a list. 
# This method is useful for handling multiple events in a single loop iteration

# KEYDOWN : When a key is pressed down
# KEYUP : When the key is released

# pygame.MOUSEBUTTONDOWN : when a mouse button is pressed.
# pygame.MOUSEBUTTONUP : when a mouse button is released.
# pygame.MOUSEMOTION : when the mouse is moved.



import pygame

pygame.init()

screen = pygame.display.set_mode((600,400))
pygame.display.set_caption("Session 03 - Python - Pygame")

icon = pygame.image.load('icon.jpg')
pygame.display.set_icon(icon)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            
        if event.type == pygame.KEYDOWN:
            key = pygame.key.name(event.key)
            print (key, "Key is pressed")
        if event.type == pygame.KEYUP:
            key = pygame.key.name(event.key)
            print (key, "Key is released")
            
        # Detect mouse button down (click)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                mouse_button = "Left Click"
            elif event.button == 3:  # Right mouse button
                mouse_button = "Right Click"
            print(f"Mouse Button Down: {mouse_button} at {event.pos}")
        
        # Detect mouse button up (release)
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:  # Left mouse button
                mouse_button = None
            print(f"Mouse Button Up at {event.pos}")
        
        # Detect mouse movement
        if event.type == pygame.MOUSEMOTION:
            mouse_x, mouse_y = event.pos
            print(f"Mouse Moved to {mouse_x}, {mouse_y}")
            
            
            
    screen.fill("aqua")
    
    
    
    
    
    pygame.display.flip()