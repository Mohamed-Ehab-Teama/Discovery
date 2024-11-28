# 1. Displaying Text:
    # Use pygame.font.Font to create a font object  
        # myFont = pygame.font.Font(None, 50)  :  Default font, size 50
    # render to create a text surface.
        # text = myFont.render("Hello, Pygame!", True, WHITE)
    # Draw the text surface on the screen using screen.blit.
        # screen.blit(text, (100, 100))

# The collidepoint method in Pygame is a useful function for detecting whether a specific point is inside a rectangle. 
# This method is part of the pygame.Rect class, which is used to store and manipulate rectangular areas in Pygame.


# ---------------------------------------------------------------------------------


# import pygame

# pygame.init()

# screen = pygame.display.set_mode( (600,400) )
# pygame.display.set_caption ( " Session 05 - Python - Pygame " )

# # Create Font object
# myFont = pygame.font.Font( None, 50)

# # Render text
# myText = myFont.render( "Welcome to PyGame", 0, "gold" )

# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
            
#     screen.fill('aqua')
    
#     screen.blit( myText, (0,0) )
    
#     pygame.display.flip()
    
# ---------------------------------------------------------------------------------

# 2. Creating a Simple Text Input Box
    # Text Input Box:
        # Create a rectangle for the input box and toggle its "active" state based on mouse clicks.
        # Append keyboard input to a string and render it inside the input box.
        
# import pygame

# pygame.init()

# screen = pygame.display.set_mode( (600,400) )
# pygame.display.set_caption ( " Session 05 - Python - Pygame " )

# # Create Font object
# myFont = pygame.font.Font( None, 50)
# # Create Rectangle box
# inputBox = pygame.Rect(100,100,300,50)
# # create the input text as an empty text
# inputText = ""
# # create variable for the input_text active or not
# active = False


# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
            
#         # Handle mouse click to activate input box
#         if event.type == pygame.MOUSEBUTTONDOWN:
#             active = inputBox.collidepoint(event.pos)
            
#         # Handle keyboard input
#         if event.type == pygame.KEYDOWN and active:
#             if event.key == pygame.K_BACKSPACE:
#                 inputText = inputText[:-1]          # Remove last character
#             else:
#                 inputText += event.unicode          # Add typed character
            
#     screen.fill('aqua')
    
#     # Draw the input box
#     pygame.draw.rect ( screen, 'red', inputBox, 3 )
#     textSurface = myFont.render( inputText, True , 'black')
#     screen.blit( textSurface , ( inputBox.x + 5 , inputBox.y + 5 ) )
    
    
#     pygame.display.flip()
    
# ---------------------------------------------------------------------------------

import pygame

# Initialize Pygame
pygame.init()

# Set up the window
screen = pygame.display.set_mode((500, 300))
pygame.display.set_caption("Text as Button")

# Colors and font
myFont = pygame.font.Font(None, 40)

# Button properties
button_rect = pygame.Rect(150, 100, 200, 50)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Detect button click
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):
                print("Button clicked!")

    # Fill the screen
    screen.fill((0, 0, 0))

    # Change button color on hover
    mouse_pos = pygame.mouse.get_pos()
    color = 'green' if button_rect.collidepoint(mouse_pos) else 'gold'
    pygame.draw.rect(screen, color, button_rect)

    # Draw button text
    button_text = myFont.render("Click Me", True, 'white')
    screen.blit(button_text, (button_rect.x + 50, button_rect.y + 10))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
