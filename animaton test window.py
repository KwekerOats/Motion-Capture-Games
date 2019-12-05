import pygame
from pygame.locals import *
import os
import time

os.environ['SDL_VIDEO_CENTERED'] = "True"

pygame.init()
width, height = 1200, 600
screen=pygame.display.set_mode((width, height))

backdrop = pygame.image.load('mountain range.PNG')
backdrop = pygame.transform.scale(backdrop, (2000,300))

roadwidth = 100
x = 100
view = 0

rdirection = []
for _ in range(0,10):
    for x in range(10000):
        rdirection.append(600)

road = []
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
    '''for x in range(150):
        road.append(0)
    for x in range(0,250,2):
        road.append(x)
    for x in range(100):
        road.append(250)
    for x in range(250,0,-1):
        road.append(x)
    for x in range(10):
        road.append(0)
    for x in range(0,-180,-3):
        road.append(x)
    for x in range(-180,-90):
        road.append(x)
    for x in range(-90,-250,-4):
        road.append(x)
    for x in range(70):
        road.append(-250)
    for x in range(-250,0,1):
        road.append(x)'''

tcounter = 0
y = 50
down = True
iy =0
while True:

    while tcounter <= len(rdirection) - 300:
        tcounter += 1
        screen.fill(0)
        y = road[iy]
        iy += 1

        rwidth = 25
        screen.blit(backdrop, (-(y/2) - 250,-50))
        for x in range(1,400):
            turn = (x - 400)*-1

            pygame.draw.rect(screen, (40,255,120), (0,200 + x,600 + rwidth/2 + ((rdirection[-tcounter] + rwidth / 2)* ((turn/100000) * y)),1),0)
            pygame.draw.rect(screen, (255,200,120), (600 + rwidth/2 + ((rdirection[-tcounter] - rwidth / 2)* ((turn/100000) * y)),200 + x,10000,1),0)
            pygame.draw.rect(screen, (50,50,50), (600 - rwidth/2 + ((rdirection[-tcounter] - rwidth / 2)* ((turn/100000) * y)),200 + x,rwidth + turn/3,1),0)

            rwidth += 3
        
        pygame.display.update()

    roadwidth = 100
    x = 100
    tcounter += 500
