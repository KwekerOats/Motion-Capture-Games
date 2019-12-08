import pygame
import os
import pygame
from pygame.locals import *
import os
import time

os.environ['SDL_VIDEO_CENTERED'] = "True"

pygame.init()
width, height = 600, 600
screen=pygame.display.set_mode((width, height))

keys = [False,False,False,False]

colour = (255,0,0)
size = 50
startan = 10

llsquare,lmsquare,rmsquare,rrsquare = colour,colour,colour,colour

def hit_check(timer,lltimes):
    for x in happening:
        if timer - .5 <= x <= timer + .5:
            return True

def hit_animation():
    pygame.draw.rect(screen,llsquare,(width/4 - 100,height/20,size + 10,size + 10))


start_time = time.time()
while True:

    timer = time.time() - start_time
    llsquare,lmsquare,rmsquare,rrsquare = colour,colour,colour,colour

    for event in pygame.event.get():            
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

        if event.type == KEYDOWN and event.key == K_LEFT:
            print(timer)
            print(happening)
            if hit_check(timer,lltimes):
                startan = 0

    screen.fill(0)

    pygame.draw.rect(screen,llsquare,(width/4 - 100,height/20,size,size))
    pygame.draw.rect(screen,lmsquare,(width/2 - 100,height/20,size,size))
    pygame.draw.rect(screen,rmsquare,(width*0.75 - 100,height/20,size,size))
    pygame.draw.rect(screen,rrsquare,(width - 100,height/20,size,size))

    if startan < 10:
        llsquare = (0,255,0)
        hit_animation()
    
    pygame.draw.rect(screen, (255,255,255), (width/2 - 5, 0, 10, height))
    pygame.draw.rect(screen, (255,255,255), (width/4 - 5, 0, 10, height))
    pygame.draw.rect(screen, (255,255,255), (width*.75 - 5, 0, 10, height))
    pygame.draw.rect(screen, (255,255,255), (width - 5, 0, 10, height))
    pygame.draw.rect(screen, (255,255,255), (-5, 0, 10, height))

    lltimes = [1, 4, 5, 7]
    happening = [x for x in lltimes if x <= timer]
    for x in happening:
        lltimes.remove(x)

    for x in range(len(lltimes)):
        pygame.draw.rect(screen,(255,255,255),(width/4 - 100,(lltimes[x] - timer)*100 + height/20,size,size))

    font = pygame.font.Font('Road_Rage.ttf',40)
    text = font.render(str(timer), True, (255,100,200),(0))
    textRect = text.get_rect()
    textRect.center = (width/2, height/2)
    screen.blit(text,textRect)

    startan += 1
    
    pygame.display.update()
    
