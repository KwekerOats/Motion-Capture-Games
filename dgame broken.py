import pygame
from pygame.locals import *
import os
#import smbus
import time
#import RPi.GPIO as gpio

'''PWR_M   = 0x6B
DIV   = 0x19
CONFIG       = 0x1A
GYRO_CONFIG  = 0x1B
INT_EN   = 0x38
ACCEL_X = 0x3B
ACCEL_Y = 0x3D
ACCEL_Z = 0x3F
GYRO_X  = 0x43
GYRO_Y  = 0x45
GYRO_Z  = 0x47
TEMP = 0x41
bus = smbus.SMBus(1)

Device_Address = 0x68   # device address
AxCal=0
AyCal=0
AzCal=0
GxCal=0
GyCal=0
GzCal=0

def InitMPU():
    bus.write_byte_data(Device_Address, DIV, 7)
    bus.write_byte_data(Device_Address, PWR_M, 1)
    bus.write_byte_data(Device_Address, CONFIG, 0)
    bus.write_byte_data(Device_Address, GYRO_CONFIG, 24)
    bus.write_byte_data(Device_Address, INT_EN, 1)
    time.sleep(1)

def readMPU(addr):
    high = bus.read_byte_data(Device_Address, addr)
    low = bus.read_byte_data(Device_Address, addr+1)
    value = ((high << 8) | low)
    if(value > 32768):
        value = value - 65536
    return value

def accel():
     x = readMPU(ACCEL_X)
     y = readMPU(ACCEL_Y)
     z = readMPU(ACCEL_Z)
     Ax = (x/16384.0-AxCal)
     Ay = (y/16384.0-AyCal)
     Az = (z/16384.0-AzCal)
     #print "X="+str(Ax)
     print(Ax,Ay,Az)
     time.sleep(.01)
    
def gyro():
    global GxCal
    global GyCal
    global GzCal
    x = readMPU(GYRO_X)
    y = readMPU(GYRO_Y)
    z = readMPU(GYRO_Z)
    Gx = x/131.0 - GxCal
    Gy = y/131.0 - GyCal
    Gz = z/131.0 - GzCal
    #print "X="+str(Gx)
    orientation += Gy

    if orientation <= 0:
        playerpos[0] -= .75
        player = pygame.image.load('side car.PNG')
        player = pygame.transform.scale(player, (400,400))
    if orientation >= 0:
        playerpos[0] += .75
        player = pygame.image.load('side car.PNG')
        player = pygame.transform.scale(player,(400,400))'''

#InitMPU()

os.environ['SDL_VIDEO_CENTERED'] = "True"

pygame.init()
width, height = 1200, 600
screen=pygame.display.set_mode((width, height))

keys = [False, False, False, False]
player = pygame.image.load('back car.PNG')
player = pygame.transform.scale(player, (400,400))
playerpos =[620,400]
backdrop = pygame.image.load('mountain range.PNG')
backdrop = pygame.transform.scale(backdrop, (1200,200))

roadwidth = 100
x = 100
view = 0

rdirection = []
for _ in range(0,10):
    for x in range(10):
        rdirection.append(600)
    for x in range(600,900,5):
        for _ in range(0,5):
            rdirection.append(x)
    for x in range(900,700,-5):
        for _ in range(0,5):
            rdirection.append(x)
    for x in range(700,800,5):
        for _ in range(0,5):
            rdirection.append(x)
    for x in range(800,300,-5):
        for _ in range(0,5):
            rdirection.append(x)
    for x in range(300,600,5):
        for _ in range(0,5):
            rdirection.append(x)

tcounter = 0
vibrate = 2

while True:

    while tcounter <= len(rdirection) - 300:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key==K_a:
                    keys[1]=True
                elif event.key==K_d:
                    keys[3]=True
            if event.type == pygame.KEYUP:
                player = pygame.image.load('back car.PNG')
                player = pygame.transform.scale(player, (400,400))
                if event.key == K_a:
                    keys[1]=False
                elif event.key == K_d:
                    keys[3]=False
        if keys[1]:
            view -= 7.5
            '''player = pygame.image.load('side car.PNG')
            player = pygame.transform.scale(player, (400,400))'''
        if keys[3]:
            view += 7.5
            '''player = pygame.image.load('side car.PNG')
            player = pygame.transform.scale(player, (400,400))'''

        '''while 1:
          gyro()'''

        tcounter += 1
        screen.fill(0)

        rwidth = 200
        screen.blit(backdrop, (view,0))
        for x in range(0,400):
            pygame.draw.rect(screen, (50,50,50), (rdirection[-tcounter + x] - rwidth/2 + view,200 + x,rwidth,1),0)
            pygame.draw.rect(screen, (100,255,100), (0,200 + x,rdirection[-tcounter + x] - rwidth/2 + view,1),0)
            pygame.draw.rect(screen, (100,255,100), (rdirection[-tcounter + x] + rwidth/2 + view,200 + x,width - rwidth/2 - rdirection[-tcounter + x],1),0)

            rwidth += 2.5

            
        screen.blit(player,playerpos)
        if vibrate == 2:
            vibrate = -2
            playerpos[1] += vibrate
        elif vibrate == -2:
            vibrate = 2
            playerpos[1] += vibrate
        
        pygame.display.update()

    roadwidth = 100
    x = 100
    tcounter += 500
    screen.blit(player, playerpos)
    
