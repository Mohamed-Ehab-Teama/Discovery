import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the screen
screen = pygame.display.set_mode((800, 600))

# Load the image
image = pygame.image.load('./Session05/icon.jpg')  # Replace with your image file
image_rect = image.get_rect(center=(400, 300))

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get the current mouse position
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Scale based on horizontal mouse position
    scale_factor = (mouse_x - 400) / 200 + 1  # Basic scale factor

    # Rotate based on vertical mouse position
    rotation_angle = (mouse_y - 300) / 2  # Basic rotation angle

    # Scale and rotate the image
    scaled_image = pygame.transform.scale(image, 
                                          (int(image.get_width() * scale_factor), 
                                           int(image.get_height() * scale_factor)))
    rotated_image = pygame.transform.rotate(scaled_image, rotation_angle)
    rotated_rect = rotated_image.get_rect(center=image_rect.center)

    # Draw everything
    screen.fill((255, 255, 255))  # Clear screen
    screen.blit(rotated_image, rotated_rect)  # Draw rotated and scaled image

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
