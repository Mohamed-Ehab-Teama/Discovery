# pygame is a free, open source library in python which is used for developing many visual multimedia application such as video games etc.

# Python vs Unity
# That depends on the type of game you want to develop. If you are a beginner in game development, you can create a simple 2D game, such as flip-flop, and for that, you should choose Pygame. On the other hand, if you aim to develop advanced games, then you should go for Unity.

# Why PyGame?

        # - Easy to Learn: PyGame is straightforward and beginner-friendly. It abstracts many of the complex parts of game development, letting you focus on building your game.
        # - Cross-Platform: Games made with PyGame can run on Windows, Mac, and Linux without any changes to your code.
        # - Active: There’s a large and helpful community of developers using PyGame. You can find tons of tutorials, examples, and forums where you can ask questions and share your projects.

# To install Pygame, open the command prompt and give the command as shown below:
    # pip install pygame
    # pip3 install pygame

# --------------------------------------------------------------------
    #                           Start Code

    # import pygame library
import pygame

    # Initialize PyGame
pygame.init()

    # Set up the game window
        # screen = pygame.display.set_mode((screen_width, screen_height))
screen = pygame.display.set_mode( (800,600) )
pygame.display.set_caption('First Game')
    # To Add Icon
myIcon = pygame.image.load('Yamamoto .jpg')
pygame.display.set_icon(myIcon)

    # Set the frame rate
clock = pygame.time.Clock()

    # Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            
    # Fill the screen with a color
    screen.fill( ('violet') )

    # Update the display
    pygame.display.flip()

    # Cap the frame rate at 60 frames per second
    clock.tick(60)
    
    
#  Illustration:
# 1- Importing Libraries: 
    # We start by importing 'pygame' and 'sys'. 
    # The "pygame" library is what we’ll use to create the game, 
    # while "sys" helps us cleanly exit the program when needed.

# 2- Initializing PyGame: 
    # The line pygame.init() is crucial. it sets up all the modules that PyGame needs to run. 
    # You should always call this at the beginning of your PyGame projects.

# 3- Creating the Game Window: 
    # We use 'pygame.display.set_mode()' to create a window with a width of 800 pixels and a height of 600 pixels. This is where everything in our game will be displayed. 
    # 'The pygame.display.set_caption()' function lets us set the title of the window to something meaningful, like "Simple Shooter Game".

# 4- Setting Up the Frame Rate: 
    # The clock = pygame.time.Clock() line creates a clock object that helps us control how fast the game runs. 
    # By setting the frame rate to 60 frames per second, we ensure that the game runs smoothly.

# 5- Main Game Loop: 
    # The while True loop is the heart of our game. It keeps running, allowing us to update the game and check for events like closing the window. 
    
    # Inside this loop:
        # 1- Event Handling: 
            # We use pygame.event.get() to check if the player wants to quit the game. 
            # If they do, we call pygame.quit() to clean up and sys.exit() to exit the program.
        # 2- Drawing the Background: 
            # The screen.fill((0, 0, 0)) line fills the screen with black, essentially clearing it for the next frame.
        # 3- Updating the Display: 
            # Finally, pygame.display.flip() updates the window to show whatever we’ve drawn.