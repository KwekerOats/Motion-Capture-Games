import pygame
import math
from pygame.locals import *

pygame.init()
width, height = 640, 480
screen=pygame.display.set_mode((width, height))
keys = [False, False, False, False]
playerpos =[100,100]

player = pygame.image.load('face.JPG')
player = pygame.transform.scale(player, (100, 60))

while 1:
    screen.fill(0)

    # 6.1 - Set player position and rotation
    position = pygame.mouse.get_pos()
    angle = math.atan2(position[1]-(playerpos[1]+32),position[0]-(playerpos[0]+26))
    playerrot = pygame.transform.rotate(player, 360-angle*57.29)
    playerpos1 = (playerpos[0]-playerrot.get_rect().width/2, playerpos[1]-playerrot.get_rect().height/2)
    screen.blit(playerrot, playerpos1) 


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
                keys[0]=True
            elif event.key==K_a:
                keys[1]=True
            elif event.key==K_s:
                keys[2]=True
            elif event.key==K_d:
                keys[3]=True
        if event.type == pygame.KEYUP:
            if event.key == K_w:
                keys[0]=False
            elif event.key == K_a:
                keys[1]=False
            elif event.key == K_s:
                keys[2]=False
            elif event.key == K_d:
                keys[3]=False
    if keys[0]:
        playerpos[1] -= 1
    if keys[2]:
        playerpos[1] += 1
    if keys[1]:
        playerpos[0] -= 1
    if keys[3]:
        playerpos[0] += 1
            
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
