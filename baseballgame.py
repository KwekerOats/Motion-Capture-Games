import pygame
import math
import random
import time
import os
from pygame.locals import *

pygame.init()
os.environ['SDL_VIDEO_CENTERED'] = "True"
width, height = 1200, 600
screen=pygame.display.set_mode((width, height))
batpos =[width/4,(height/3)*2]
ballpos =[width/4, batpos[1]]#(height/4)*3]
ball2pos = [575,520]

ball = pygame.image.load('kweku4.PNG')
ball = pygame.transform.scale(ball, (50,100))
bat = pygame.image.load('bat.PNG')
bat = pygame.transform.scale(bat, (100,100))
ball2 = pygame.transform.scale(ball, (25,25))
#s.diamond = pygame.image.load('baseball pitch.PNG').convert()
#s.rect = b.diamond.get_rect()
#s.rect.center = (width/2,(height/4)*3)
diamond = pygame.image.load('baseball pitch.PNG')
diamond = pygame.transform.scale(diamond, (800, 600))
diamondpos = [200, 100]
game_state = True

'''def throw(ballpos):
    #ballpos[0],ballpos[1] = ballpos[0] - 1,ballpos[1] + 3
    screen.blit(ball,ballpos)
    if batpos[0] - 100 < ballpos[0] < batpos[0] + 100 and batpos[1] - 100 < ballpos[1] < batpos[1] and swing_state:
        hit(ballpos)
    pygame.display.update()
    return ballpos'''

power_val = [64,32,128]

class Fielder(object): # creates the fielders
    def __init__(self, number, pos, running):
        self.number = number
        self.pos = pos
        self.running = running

fielders = []

fielders.append(Fielder(1, [600, 350], False))
fielders.append(Fielder(2, [450, 450], False))
fielders.append(Fielder(3, [750, 450], False))
for x in range(4,8):
    fielders.append(Fielder(x, [random.randint(350,950), random.randint(100,350)], False))

def hit(ballpos,power,ball): #animation for a hit
    for _ in range(power):
        ballpos[0],ballpos[1] = ballpos[0] + 2,ballpos[1] - 4
        screen.blit(ball,ballpos)
        pygame.display.update()
    power -= power/2
    for _ in range(int(power)):
        ballpos[0],ballpos[1] = ballpos[0] + 3,ballpos[1] - 3
        screen.blit(ball,ballpos)
        pygame.display.update()
    power -= power/2
    for _ in range(int(power)):
        ballpos[0],ballpos[1] = ballpos[0] + 4,ballpos[1] - 2
        screen.blit(ball,ballpos)
        pygame.display.update()
    power -= power/2
    for _ in range(int(power)):
        ballpos[0],ballpos[1] = ballpos[0] + 5,ballpos[1] - 1
        screen.blit(ball,ballpos)
        pygame.display.update()
    power -= power/2
    for _ in range(int(power)):
        ballpos[0],ballpos[1] = ballpos[0] + 6,ballpos[1] - 1
        pygame.display.update()

    screen.fill((40,200,120))
    screen.blit(diamond, diamondpos)
    
    for x in fielders:
        pygame.draw.circle(screen, (255,0,0), (x.pos[0], x.pos[1]), 10)

    pygame.display.update()    

    speed = random.randint(1,6)# testing data
    curve = random.randint(-3,3)
    power2 = 80
    for _ in range(power2):
        ball2pos[0], ball2pos[1] = ball2pos[0] + curve, ball2pos[1] - speed
        screen.blit(ball2, ball2pos)
        if curve % 2 == 0:
            curve += curve/2
        pygame.display.update()
        time.sleep(.05)

def swing_animation(bat,mousepos): #bat swing animation
    for _ in range(2):
        bat = pygame.image.load('joh1.PNG')
        mousepos = pygame.mouse.get_pos()
        bat = pygame.transform.scale(bat, (50,100))
        screen.fill(0)

        position = mousepos
        angle = math.atan2(position[1]-(batpos[1]+32),position[0]-(batpos[0]+26))
        batrot = pygame.transform.rotate(bat, 360-angle*57.29)
        batpos1 = (batpos[0]-batrot.get_rect().width/2, batpos[1]-batrot.get_rect().height/2)
        screen.blit(batrot, batpos) 


        pygame.display.update()

while game_state: #main game loop
    
    power = 64 #random.choice(power_val)
    swing_state = False
    mousepos = pygame.mouse.get_pos()

    for event in pygame.event.get():            
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        if event.type == pygame.MOUSEBUTTONUP:
            click = True
            swing_state = True
    
    if swing_state:
        swing_animation(bat,mousepos)
    
    screen.fill(0)
    
    position = batpos
    ball_angle = math.atan2(position[1]-(batpos[1]+32),position[0]-(batpos[0]+26))

    '''playerrot = pygame.transform.rotate(player, 360-angle*57.29)
    playerpos1 = (playerpos[0]-playerrot.get_rect().width/2, playerpos[1]-playerrot.get_rect().height/2)
    screen.blit(playerrot, playerpos1)'''


    position = mousepos
    angle = math.atan2(position[1]-(batpos[1]+32),position[0]-(batpos[0]+26))
    batrot = pygame.transform.rotate(bat, 360-angle*57.29)
    batpos1 = (batpos[0]-batrot.get_rect().width/2, batpos[1]-batrot.get_rect().height/2)
    screen.blit(batrot, batpos)

    screen.blit(ball,ballpos)
    if batpos[0] - 100 < ballpos[0] < batpos[0] + 100 and batpos[1] - 100 < ballpos[1] < batpos[1] + 100 and swing_state:
        hit(ballpos,power,ball)
    
    pygame.display.update()
