# 1 - Creating Sound Effects
    # pygame.mixer.Sound("file.wav"): Loads a short sound effect.
    # .play(): Plays the loaded sound.

        # Load sound effect
        # sound_effect = pygame.mixer.Sound("click_sound.wav")

        # Play sound when the mouse is clicked
                # if event.type == pygame.MOUSEBUTTONDOWN:
                #     sound_effect.play()


# 2 - Playing Background Music

    # pygame.mixer.music.load(): Loads the background music file.
    # .play(-1): Starts the music in a loop. Replace -1 with 1 to play it once.
    # .stop(): Stops the music.

        # Load and play background music
        # pygame.mixer.music.load("background_music.mp3")
        # pygame.mixer.music.play(-1)  # Loop indefinitely
        
        # Stop the music
        # pygame.mixer.music.stop()
        
import pygame

pygame.init()

screen = pygame.display.set_mode( (600,500) )
pygame.display.set_caption( " Session 06 - Pygame " )

my_sound = pygame.mixer.Sound('Yokoso.mp3')       # load Sound
pygame.mixer.music.load('Yokoso.mp3')             # load Music
pygame.mixer.music.play(-1)                       # play Music ( if -1 : play infity times )

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            
        # Play Sound
        if event.type == pygame.MOUSEBUTTONDOWN:
            my_sound.play()

            
            
    screen.fill('orange')
    
    pygame.display.flip()

# Stop the music and quit
# pygame.mixer.music.stop()
# pygame.quit()