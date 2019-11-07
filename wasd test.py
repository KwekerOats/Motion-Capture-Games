import pygame
from pygame.locals import *

pygame.init()
width, height = 640, 480
screen=pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
keys = [False, False, False, False]
playerpos =[100,100]

player = pygame.image.load('face.JPG')
player = pygame.transform.scale(player, (100, 60))

while 1:
    clock.tick(30)
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
    if keys[0] == True:
        print('1 working')
    if keys[2] == True:
        print('3 working')
    if keys[1] == True:
        print('2 working')
    if keys[3] == True:
        print('4 working')
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
            
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        pygame.display.update()
