    # Drawing shapes:
# Draw Straigh line
    # pygame.draw.line()
        # line(surface, color, start_pos, end_pos, width=1)
        
# Draw a rectangle
    # pygame.draw.rect()
        # rect(surface, color, rect, width=0, border_radius=0, border_top_left_radius=-1, border_top_right_radius=-1, border_bottom_left_radius=-1, border_bottom_right_radius=-1)
        # rect => (x,y,width,height)
    
# draw a polygon
    # pygame.draw.polygon()
        #     pygame.draw.polygon(surface , color , points, width)
    
# draw a circle
    # pygame.draw.circle()
        # pygame.draw.circle(surface, color, center, radius, width=0)

# draw an ellipse
    # pygame.draw.ellipse()
        # pygame.draw.ellipse(screen, purple, (100, 100, 200, 100))
    
# draw an elliptical arc
    # pygame.draw.arc()
        # pygame.draw.arc(surface, color, rect, start_angle, stop_angle, width)

    
# --------=============---------------================-----------=========

import pygame

pygame.init()

screen = pygame.display.set_mode( (500,400) )
pygame.display.set_caption( ' Session 02 - PyGame Tutorial ')

myIcon = pygame.image.load('Yamamoto .jpg')
pygame.display.set_icon( myIcon )


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            
    screen.fill('orange')
    
    
    # pygame.draw.line(screen, 'blue', (5,5), (150,150), width=1 )
    # pygame.draw.rect(screen, 'red', (20,0,100,50), width = 2, border_radius=50 )        # (x,y,width,height)
    # pygame.draw.circle(screen, 'white', (250,250), 90, 10)
    # pygame.draw.ellipse(screen, 'violet', (50,50,100,10))                        # (x,y,width,height)
    # pygame.draw.polygon(screen, 'black',[(0,0),(120,40),(250,180)], 2)
    # pygame.draw.arc(screen, 'Blue', (100,100,200,250), 1, 2.5, 1)
    
    pygame.display.flip()