import pygame
import math
from pygame.locals import *

pygame.init()
width, height = 640, 480
screen=pygame.display.set_mode((width, height))
keys = [False, False, False, False, False, False, False, False]
playerpos =[100,100]
player2pos =[200,200]

player = pygame.image.load('Red car.PNG')
player = pygame.transform.scale(player, (50,100))
player2 = pygame.image.load('blue car.PNG')
player2 = pygame.transform.scale(player2, (50,100))

while 1:
    screen.fill(0)

    position = player2pos
    angle = math.atan2(position[1]-(playerpos[1]+32),position[0]-(playerpos[0]+26))
    playerrot = pygame.transform.rotate(player, 360-angle*57.29)
    playerpos1 = (playerpos[0]-playerrot.get_rect().width/2, playerpos[1]-playerrot.get_rect().height/2)
    screen.blit(playerrot, playerpos1)


    position = playerpos
    angle = math.atan2(position[1]-(player2pos[1]+32),position[0]-(player2pos[0]+26))
    player2rot = pygame.transform.rotate(player2, 360-angle*57.29)
    player2pos1 = (player2pos[0]-player2rot.get_rect().width/2, player2pos[1]-player2rot.get_rect().height/2)
    screen.blit(player2rot, player2pos1) 
    
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key==K_UP:
                keys[0]=True
            elif event.key==K_LEFT:
                keys[1]=True
            elif event.key==K_DOWN:
                keys[2]=True
            elif event.key==K_RIGHT:
                keys[3]=True
        if event.type == pygame.KEYUP:
            if event.key == K_UP:
                keys[0]=False
            elif event.key == K_LEFT:
                keys[1]=False
            elif event.key == K_DOWN:
                keys[2]=False
            elif event.key == K_RIGHT:
                keys[3]=False

        if event.type == pygame.KEYDOWN:
            if event.key==K_w:
                keys[4]=True
            elif event.key==K_a:
                keys[5]=True
            elif event.key==K_s:
                keys[6]=True
            elif event.key==K_d:
                keys[7]=True
        if event.type == pygame.KEYUP:
            if event.key == K_w:
                keys[4]=False
            elif event.key == K_a:
                keys[5]=False
            elif event.key == K_s:
                keys[6]=False
            elif event.key == K_d:
                keys[7]=False
    if keys[0]:
        playerpos[1] -= .5
    if keys[2]:
        playerpos[1] += .5
    if keys[1]:
        playerpos[0] -= .5
    if keys[3]:
        playerpos[0] += .5
    if keys[4]:
        player2pos[1] -= .5
    if keys[6]:
        player2pos[1] += .5
    if keys[5]:
        player2pos[0] -= .5
    if keys[7]:
        player2pos[0] += .5
            
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
