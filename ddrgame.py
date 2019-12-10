import pygame
import os
import pygame
from pygame.locals import *
import random
import time

os.environ['SDL_VIDEO_CENTERED'] = "True"

pygame.init()
width, height = 600, 600
screen=pygame.display.set_mode((width, height))

keys = [False,False,False,False]

colour = (0,0,255)
size = 50
startan = 10

llsquare,lmsquare,rmsquare,rrsquare = colour,colour,colour,colour

def hit_check(timer,lltimes,lmtimes,rmtimes,rrtimes):
    for x in llhappening:
        if timer - .5 <= x <= timer + .5:
            return True
    for x in lmhappening:
        if timer - .5 <= x <= timer + .5:
            return True
    for x in rmhappening:
        if timer - .5 <= x <= timer + .5:
            return True
    for x in rrhappening:
        if timer - .5 <= x <= timer + .5:
            return True

def hit_animation():
    pygame.draw.rect(screen,llsquare,(width/4 - 100,height/20,size + 10,size + 10))
    pygame.draw.rect(screen,llsquare,(width/2 - 100,height/20,size + 10,size + 10))
    pygame.draw.rect(screen,llsquare,(width*.75 - 100,height/20,size + 10,size + 10))
    pygame.draw.rect(screen,llsquare,(width - 100,height/20,size + 10,size + 10))


start_time = time.time()
while True:

    timer = time.time() - start_time
    llsquare,lmsquare,rmsquare,rrsquare = colour,colour,colour,colour

    for event in pygame.event.get():            
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

        if event.type == KEYDOWN and event.key == K_LEFT:
            if hit_check(timer,lltimes,lmtimes,rmtimes,rrtimes):
                startan = 0

    screen.fill(0)

    pygame.draw.rect(screen,llsquare,(width/4 - 100,height/20,size,size))
    pygame.draw.rect(screen,lmsquare,(width/2 - 100,height/20,size,size))
    pygame.draw.rect(screen,rmsquare,(width*0.75 - 100,height/20,size,size))
    pygame.draw.rect(screen,rrsquare,(width - 100,height/20,size,size))

    if startan < 10:
        llsquare,lmsquare,rmsquare,rrsquare = (0,255,0),(0,255,0),(0,255,0),(0,255,0)
        hit_animation()
    
    pygame.draw.rect(screen, (255,255,255), (width/2 - 5, 0, 10, height))
    pygame.draw.rect(screen, (255,255,255), (width/4 - 5, 0, 10, height))
    pygame.draw.rect(screen, (255,255,255), (width*.75 - 5, 0, 10, height))
    pygame.draw.rect(screen, (255,255,255), (width - 5, 0, 10, height))
    pygame.draw.rect(screen, (255,255,255), (-5, 0, 10, height))

    #lltimes = [random.randint(2,20) for x in range(5)]
    lltimes = [6,9,10,18]
    llhappening = [x for x in lltimes if x <= timer]
    for x in llhappening:
        lltimes.remove(x)

    for x in range(len(lltimes)):
        pygame.draw.rect(screen,(255,255,255),(width/4 - 100,(lltimes[x] - timer)*100 + height/20,size,size))


    #lmtimes = [random.randint(2,20) for x in range(5)]
    lmtimes = [2,5,7,9]
    lmhappening = [x for x in lmtimes if x <= timer]
    for x in lmhappening:
        lmtimes.remove(x)

    for x in range(len(lmtimes)):
        pygame.draw.rect(screen,(255,255,255),(width/2 - 100,(lmtimes[x] - timer)*100 + height/20,size,size))


    #rmtimes = [random.randint(2,20) for x in range(5)]
    rmtimes = [1,3,13,17]
    rmhappening = [x for x in rmtimes if x <= timer]
    for x in rmhappening:
        rmtimes.remove(x)

    for x in range(len(rmtimes)):
        pygame.draw.rect(screen,(255,255,255),(width*.75 - 100,(rmtimes[x] - timer)*100 + height/20,size,size))


    #rrtimes = [random.randint(2,20) for x in range(5)]
    rrtimes = [1,3,10,12]
    rrhappening = [x for x in rrtimes if x <= timer]
    for x in rrhappening:
        rrtimes.remove(x)

    for x in range(len(rrtimes)):
        pygame.draw.rect(screen,(255,255,255),(width - 100,(rrtimes[x] - timer)*100 + height/20,size,size))

    font = pygame.font.Font('Road_Rage.ttf',40)
    text = font.render(str(timer), True, (255,100,200),(0))
    textRect = text.get_rect()
    textRect.center = (width/2, height/2)
    screen.blit(text,textRect)

    startan += 1
    
    pygame.display.update()
    
