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

instpos = [width/2,245]
calpos = [width/2,instpos[1] + 100]

schange = 0
change = 0

while menu:

    click = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.MOUSEBUTTONUP:
            click = True
    
    screen.blit(background,(0,0))
    
    mouse = pygame.mouse.get_pos()
        
    lcount,lcount2 = effects(lcount,lcount2)
    
    if instpos[0] - 150 < mouse[0] < instpos[0] + 150 and instpos[1] - 30 < mouse[1] < instpos[1] + 30:
        font = pygame.font.Font('Road_Rage.ttf',60)
        text = font.render('Instructions', True, (255,100,200),(0))
        textRect = text.get_rect()
        textRect.center = (instpos[0], instpos[1])
        screen.blit(text,textRect)
    else:
        font = pygame.font.Font('Road_Rage.ttf',40)
        text = font.render('Insrutctions', True, (255,100,200),(0))
        textRect = text.get_rect()
        textRect.center = (instpos[0], instpos[1])
        screen.blit(text,textRect)

    if calpos[0] - 150 < mouse[0] < calpos[0] + 150 and calpos[1] - 30 < mouse[1] < calpos[1] + 30:
        font = pygame.font.Font('Road_Rage.ttf',60)
        text = font.render('calibrate', True, (255,100,200),(0))
        textRect = text.get_rect()
        textRect.center = (calpos[0], calpos[1])
        screen.blit(text,textRect)
    else:
        font = pygame.font.Font('Road_Rage.ttf',40)
        text = font.render('calibrate', True, (255,100,200),(0))
        textRect = text.get_rect()
        textRect.center = (calpos[0], calpos[1])
        screen.blit(text,textRect)

    if 50 < mouse[0] < 150 and 530< mouse[1] < 570:
        font = pygame.font.Font('Road_Rage.ttf',45)
        text = font.render('back', True, (255,100,200),(0))
        textRect = text.get_rect()
        textRect.center = (100, 550)
        screen.blit(text,textRect)
        if click:
            import background
    else:
        font = pygame.font.Font('Road_Rage.ttf',30)
        text = font.render('back', True, (255,100,200),(0))
        textRect = text.get_rect()
        textRect.center = (100, 550)
        screen.blit(text,textRect)

    font = pygame.font.Font('Road_Rage.ttf',100)
    text = font.render('Help', True, (100,100,100),(0))
    textRect = text.get_rect()
    textRect.center = (width/2 + 5, 105)
    screen.blit(text,textRect)

    font = pygame.font.Font('Road_Rage.ttf',100)
    text = font.render('Help', True, (255,50,255),(0))
    textRect = text.get_rect()
    textRect.center = (width/2, 100)
    screen.blit(text,textRect)

    pygame.display.update()
