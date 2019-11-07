import pygame
from pygame.locals import *
import os
import time

pygame.init()

os.environ['SDL_VIDEO_CENTERED'] = "True"

width, height = 1200,600
screen = pygame.display.set_mode((width,height))

background = pygame.image.load('background.PNG')
background = pygame.transform.scale(background, (1200,600))
menu_car = pygame.image.load('poster car.PNG')
menu_car_pos = [-280,450]
menu_car = pygame.transform.scale(menu_car, (280,140))

lcount = 0
lcount2 = 4

def effects(lcount,lcount2):
    lframe_size = [50,350]
    lframe = ['1','2','3','2','3','2','1','1','2','1','1','2','1','2','1']
    if lcount < len(lframe) - 1:
        lcount += 1
    else:
        lcount = 0

    if lcount2 < len(lframe) - 1:
        lcount2 += 1
    else:
        lcount2 = 0
        
    lightning = pygame.image.load('lightning' + lframe[lcount] + '.png')
    lightning = pygame.transform.scale(lightning,lframe_size)
    lightning2 = pygame.image.load('lightning' + lframe[lcount2] + '.png')
    lightning2 = pygame.transform.scale(lightning2,lframe_size)
    screen.blit(lightning, (350,-20))
    screen.blit(lightning2, (800,-100))
    screen.blit(lightning, (1000,0))
    screen.blit(lightning2, (100,-50))
    return lcount,lcount2

menu = True
vibrate = 1
start_an = False
start_an2 = False

startpos = [width + 200,245]
helppos = [-100,startpos[1] + 225]
scorepos = [width + 100, helppos[1]]

schange = 0
change = 0

while menu:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    
    screen.blit(background,(0,0))
    screen.blit(menu_car, menu_car_pos)
    
    if menu_car_pos[0] < 440:
        menu_car_pos[0] += 20
    else:
        vibrate = -vibrate
        menu_car_pos[1] += vibrate
        start_an = True
    
    mouse = pygame.mouse.get_pos()

    if start_an and startpos[0] != 600:
        startpos[0] -= 50
    elif startpos[0] == 600:
        start_an2 = True

    if start_an2 and startpos[0] != helppos[0] + 400:
        helppos[0] += 50
        scorepos[0] -= 50
    if startpos[0] == helppos[0] + 400 and start_an2:
        if schange == 0:
            change = -1
            time.sleep(.01)
        elif schange == -5:
            change = 1
            time.sleep(.01)
        schange += change
        
        lcount,lcount2 = effects(lcount,lcount2)
    
    if startpos[0] - 150 < mouse[0] < startpos[0] + 150 and startpos[1] - 30 < mouse[1] < startpos[1] + 30:
        font = pygame.font.Font('Road_Rage.ttf',90 + schange*2)
        text = font.render('START', True, (255,100,200),(0))
        textRect = text.get_rect()
        textRect.center = (startpos[0], startpos[1])
        screen.blit(text,textRect)
    else:
        font = pygame.font.Font('Road_Rage.ttf',60)
        text = font.render('START', True, (255,100,200),(0))
        textRect = text.get_rect()
        textRect.center = (startpos[0], startpos[1])
        screen.blit(text,textRect)

    if helppos[0] - 100 < mouse[0] < helppos[0] + 100 and helppos[1] - 30 < mouse[1] < helppos[1] + 30:
        font = pygame.font.Font('Road_Rage.ttf',45 + schange)
        text = font.render('help', True, (255,255,255),(0))
        textRect = text.get_rect()
        textRect.center = (helppos[0], helppos[1])
        screen.blit(text,textRect)
    else:
        font = pygame.font.Font('Road_Rage.ttf',30)
        text = font.render('help', True, (255,255,255),(0))
        textRect = text.get_rect()
        textRect.center = (helppos[0], helppos[1])
        screen.blit(text,textRect)

    if scorepos[0] - 100 < mouse[0] < scorepos[0] + 100 and scorepos[1] - 30 < mouse[1] < scorepos[1] + 30:
        font = pygame.font.Font('Road_Rage.ttf',45 + schange)
        text = font.render('highscores', True, (255,255,255),(0))
        textRect = text.get_rect()
        textRect.center = (scorepos[0], scorepos[1])
        screen.blit(text,textRect)
    else:
        font = pygame.font.Font('Road_Rage.ttf',30)
        text = font.render('highscores', True, (255,255,255),(0))
        textRect = text.get_rect()
        textRect.center = (scorepos[0], scorepos[1])
        screen.blit(text,textRect)

    font = pygame.font.Font('Road_Rage.ttf',130)
    text = font.render('BIGBOI', True, (100,100,100),(0))
    textRect = text.get_rect()
    textRect.center = (width/2 + 5, 105)
    screen.blit(text,textRect)

    font = pygame.font.Font('Road_Rage.ttf',130)
    text = font.render('BIGBOI', True, (255,50,255),(0))
    textRect = text.get_rect()
    textRect.center = (width/2, 100)
    screen.blit(text,textRect)

    pygame.display.update()
