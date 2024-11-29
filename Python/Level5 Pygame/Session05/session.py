import pygame

pygame.init()

screen = pygame.display.set_mode( (900,400) )
pygame.display.set_caption ( " Session 05 - Python - Pygame " )

myFont = pygame.font.Font ( None, 40 )
inputBox = pygame.Rect(100,100,600,80)
inputText = ""
active = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            active = inputBox.collidepoint(event.pos)
            
        if event.type == pygame.KEYDOWN and active:
            if event.key == pygame.K_BACKSPACE:
                inputText = inputText[:-1]
            else:
                inputText += event.unicode
            
            
            
    screen.fill('aqua')
    
    pygame.draw.rect( screen, " black", inputBox, 8 )
    newText = myFont.render ( inputText, True, "blue" )
    screen.blit ( newText , (inputBox.x + 15, inputBox.y + 15) )
    
    pygame.display.flip()