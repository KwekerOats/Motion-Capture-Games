import pygame
from pygame.locals import *
import os
import time

pygame.init()

os.environ['SDL_VIDEO_CENTERED'] = "True"

width, height = 1200,600
screen = pygame.display.set_mode((width,height))

ball = pygame.image.load('kweku3.PNG')
ball = pygame.transform.scale(ball

menu = True
while menu:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.MOUSEBUTTONUP:
            click = True

    mousepos = pygame.mouse.get_pos()

    startpos = [width/2,height/4]
    helppos = [width/4,(height/4)*3]
    calpos = [(width/4)*3,helppos[1]]

    font = pygame.font.FONT('Road_rage.ttf',90)
    text = font.render('PLAY', True,(255,255,255),(0))
    textRect = text.get_Rect()
    textRect.center = (startpos[0],startpos[1])
    screen.blit(text,textRect)

    if helppos[0] - 100 < mousepos[0] < helppos[0] + 100 and helppos[1] - 30 < mousepos[1] < helppos[1] + 30:
        font = pygame.font.FONT('Road_rage.ttf',45)
        text = font.render('Help', True,(0,255,255), (0))
        textRect = text.get_Rect()
        textRect.center = (helppos[0],helppos[1])
        screen.blit(text,textRect)
    else:
        font = pygame.font.FONT('Road_rage.ttf',45)
        text = font.render('Help', True,(255,255,255), (0))
        textRect = text.get_Rect()
        textRect.center = (helppos[0],helppos[1])
        screen.blit(text,textRect)

    if calpos[0] - 100 < mousepos[0] < calpos[0] + 100 and calpos[1] - 30 < mousepos[1] < calpos[1] + 30:
        text = font.render('Calibrate', True,(0,255,255),(0))
        textRect = text.get_Rect()
        textRect.center = (calpos[0],calpos[1])
        screen.blit(text,textRect)
    else:
        text = font.render('Calibrate', True,(255,255,255),(0))
        textRect = text.get_Rect()
        textRect.center = (calpos[0],calpos[1])
        screen.blit(text,textRect)
