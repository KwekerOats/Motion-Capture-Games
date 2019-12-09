import pygame
from pygame.locals import *
import os
import time
from mpu6050 import mpu6050
import math
import smbus

os.environ['SDL_VIDEO_CENTERED'] = "True"

pygame.init()
width, height = 1200, 600
screen=pygame.display.set_mode((width, height))

backdrop = pygame.image.load('mountain range.png')
backdrop = pygame.transform.scale(backdrop, (10000,600))
player = pygame.image.load('mario back.png')
player = pygame.transform.scale(player, (2000,1000))
playerpos =[550,400]

roadwidth = 100
x = 100
view = 0
pview = 0

road = []

sensor = mpu6050(0x68)

for _ in range(100):
    for x in range(100):
        road.append(0)
    for x in range(0,250):
        road.append(x)
    for x in range(50):
        road.append(250)
    for x in range(250,0,-1):
        road.append(x)
    for x in range(50):
        road.append(0)
    for x in range(0,-250,-1):
        road.append(x)
    for x in range(50):
        road.append(-250)
    for x in range(-250,0):
        road.append(x)

y = 50
iy =0
speed = 0
keys = [False,False,False,False]
vibrate = 2
speedchange = -4
p = pygame.time.get_ticks()
while True:

    x_orientation = sensor.get_gyro_data(x)
    y_orientation = sensor.get_gyro_data(y)
    
    for event in pygame.event.get():            
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
            
        if event.type == pygame.KEYDOWN:
            if event.key==K_a and keys[3] == False:
                player = pygame.image.load('mario left.png')
                player = pygame.transform.scale(player, (200,200))
                keys[1]=True
            elif event.key==K_d and keys[1] == False:
                keys[3]=True
                player = pygame.image.load('mario left.png')
                player = pygame.transform.flip(player, True, False)
                player = pygame.transform.scale(player, (200,200))
        if event.type == pygame.KEYUP:
            if event.key == K_a and keys[3] == False:
                player = pygame.image.load('mario back.png')
                player = pygame.transform.scale(player, (2000,1000))
                keys[1]=False
            elif event.key == K_d and keys[1] == False:
                player = pygame.image.load('mario back.png')
                player = pygame.transform.scale(player, (2000,1000))
                keys[3]=False

    if keys[1]:
        view += 7
        pview += 2
    if keys[3]:
        view -= 7
        pview -= 2

    if y_orientation >= 1:
        keys[1] = True
    elif y_orientation <= -1:
        keys[3] = True
    else:
        keys[1],keys[3] = False,False


    vibrate = -vibrate
    playerpos[1] += vibrate
        
    screen.fill(0)
    y = road[iy]
    iy += 1
    speed += speedchange

    view += road[iy]/25

    rwidth = 25
    screen.blit(backdrop, (-(y/2) - 1000 + (pview*2),0 - 135))

    
    for x in range(1,400):
        turn = (x - 400)*-1
        speed += 1
        
        pygame.draw.rect(screen, (40,255,120), (0,200 + x,view + width/2 - rwidth/2 + ((width/2 - rwidth / 2)* ((turn/100000) * y)),1),0)
        pygame.draw.rect(screen, (255,200,120), (view + width/2 + rwidth/2 + ((width/2 - rwidth / 2)* ((turn/100000) * y)),200 + x,10000,1),0)
        pygame.draw.rect(screen, (50,50,50), (view + width/2 - rwidth/2 + ((width/2 - rwidth / 2)* ((turn/100000) * y)),200 + x,rwidth + turn/3,1),0)
        pygame.draw.rect(screen, (150,150,150), (view + width/2 - rwidth/2 + ((width/2 - rwidth / 2)* ((turn/100000) * y)),200 + x,(rwidth + turn/3)/20,1),0)
        pygame.draw.rect(screen, (150,150,150), (view + width/2 - rwidth/2 + ((width/2 - rwidth / 2)* ((turn/100000) * y)) + (rwidth + turn/3) - (rwidth + turn/3)/20,200 + x,(rwidth + turn/3)/20,1),0)
        if speed%20 != 0 and speed%20 != 1 and speed%20 != 2 and speed%20 != 3 and speed%20 != 4 and speed%20 != 5 and speed%20 != 6:
            pygame.draw.rect(screen, (200,200,200), (view + width/2 - rwidth/2 + ((width/2 - rwidth / 2)* ((turn/100000) * y)) + (rwidth + turn/3)/2 - (rwidth + turn/3)/40,200 + x,(rwidth + turn/3)/20,1),0)
        if speed%40 == 0:
            pygame.draw.rect(screen, (50,50,50), (view + width/2 - rwidth/2 + ((width/2 - rwidth / 2)* ((turn/100000) * y)),200 + x,(rwidth + turn/3)/20,100),0)
            pygame.draw.rect(screen, (50,50,50), (view + width/2 - rwidth/2 + ((width/2 - rwidth / 2)* ((turn/100000) * y)) + (rwidth + turn/3) - (rwidth + turn/3)/20,200 + x,(rwidth + turn/3)/20,10),0)


        rwidth += 3

    speedchange = -4
    if view >= 550 or view <= -550:
        time.sleep(.01)
        '''add timer on'''
    screen.blit(player,playerpos)

    roadwidth = 100
    x = 100
    
    font = pygame.font.Font('Road_Rage.ttf',50)
    text = font.render(str((pygame.time.get_ticks() - p)/1000), True, (255,255,255),(0))
    textRect = text.get_rect()
    textRect.center = (width/2, 100)
    screen.blit(text,textRect)

    pygame.display.update()
