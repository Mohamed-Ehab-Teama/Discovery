        # Working with Images
# pygame.image.load('image.png'): Loads the image from a file.
# pygame.Surface.blit(): Draws the image (or surface) onto the screen.

# pygame.transform.rotate(image, angle): Rotates an image by the specified angle (in degrees)
# pygame.transform.scale(image, (width, height)): Scales the image to the specified width and height.

# pygame.transform.flip(image, flip_x, flip_y): Flips the image horizontally if flip_x is True, and vertically if flip_y is True.

# get_rect : Pygame creates a new rect with the size of the image and the x, y coordinates (0, 0)



import pygame

pygame.init()

screen = pygame.display.set_mode((900,600))
pygame.display.set_caption("Session 04 Task")

# Load Image
my_image = pygame.image.load('./Session05/icon.jpg')
# Set Image as Icon
pygame.display.set_icon(my_image)

# Scale Image
my_image = pygame.transform.scale( my_image, (600,400) )

# Rotate Image
my_image = pygame.transform.rotate( my_image, 0 )

# Flip the Image
my_image = pygame.transform.flip( my_image, False , False )

# Draw Rect around the image
image_rect = my_image.get_rect()



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
          
    # get Mouse Position:
    mouse_x , mouse_y = pygame.mouse.get_pos()
    # Update the image rect's center to the mouse position
    image_rect.center = (mouse_x, mouse_y)

    
    screen.fill('aqua')
    
    # screen.blit( my_image, (50,50) )
    
    # Draw the image at its new position
    screen.blit( my_image, image_rect)
    
    
    pygame.display.flip()