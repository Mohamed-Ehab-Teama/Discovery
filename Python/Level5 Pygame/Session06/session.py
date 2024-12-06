import pygame

pygame.init()


# pygame.time.wait(3000)
# pygame.time.delay(2000)

screen = pygame.display.set_mode((700,500))
pygame.display.set_caption(' Session 06 - PyGame ')


my_sound = pygame.mixer.Sound('Yokoso.mp3')
# pygame.mixer.music.load('Yokoso.mp3')
# pygame.mixer.music.play(-1)

start = pygame.time.get_ticks()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        # if event.type == pygame.MOUSEBUTTONDOWN:
        #     pygame.mixer.music.stop()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.time.delay(1000)
            my_sound.play()
        if event.type == pygame.MOUSEBUTTONUP:
            pygame.time.delay(3000)
            my_sound.stop()
            
    screen.fill('orange')
    
    time_done = ( pygame.time.get_ticks() - start ) / 1000
    
    print ( f"Time Gone : {time_done} seconds" )
    
    
    pygame.display.flip()