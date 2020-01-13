import pygame
from pygame.locals import *
import os
import random
import time
import cv2
import numpy as np
import csv

def login_signup():
    while True:
        choice = input('l for login, s for signup')
        if choice == "l":
            username = input('u')
            password = input('p')
            f = open("login.csv","r")
            for line in f:
                details = line.split(",")
                if username == details[0] and str(password)+'\n' == details[1]:
                    return username

        elif choice == 's':
            username = input()
            password = input()

            f = open("login.csv","r")
            for line in f:
                details = line.split(",")
                if username == details[0]:
                    login_signup()
            with open('login.csv', 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow((username, password))
        return username

player_name = login_signup()
print(player_name)

os.environ['SDL_VIDEO_CENTERED'] = "True"

pygame.init()
width, height = 600, 600
screen=pygame.display.set_mode((width, height))

arrow = pygame.image.load('arrow.png')
darrow = pygame.transform.scale(arrow, (50,50))
larrow = pygame.transform.rotate(darrow, -90)
rarrow = pygame.transform.rotate(darrow, 90)
uarrow = pygame.transform.rotate(darrow, 180)

colour = (0,0,255)
size = 50
startan = 10
move = 'pause'
avex2, avey2 = 0,0
calibrated = False
Game = True
h = 0
score = 0

llsquare,lmsquare,rmsquare,rrsquare = colour,colour,colour,colour

def hit_check(timer,times):
    for x in times:
        if timer - .3 <= x <= timer + .3:
            times.remove(x)
            return True

def hit_animation():
    pygame.draw.rect(screen,llsquare,(width/4 - 105,height/20,size + 10,size + 10))
    pygame.draw.rect(screen,llsquare,(width/2 - 105,height/20,size + 10,size + 10))
    pygame.draw.rect(screen,llsquare,(width*.75 - 105,height/20,size + 10,size + 10))
    pygame.draw.rect(screen,llsquare,(width - 105,height/20,size + 10,size + 10))

def miss_check(timer,lltimes,lmtimes,rmtimes,rrtimes):
    for x in lltimes:
        if timer >= x + .4:
            lltimes.remove(x)
            return True
    for x in lmtimes:
        if timer >= x + .4:
            lmtimes.remove(x)
            return True
    for x in rmtimes:
        if timer >= x + .4:
            rmtimes.remove(x)
            return True
    for x in rrtimes:
        if timer >= x + .4:
            rrtimes.remove(x)
            return True

def save_score(score,player_name):
    with open('ddr leaderboard.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow((score, player_name))

    '''with open('ddr leaderboard.csv', 'r', newline='') as file:
        score_list = list(csv.reader(file))
        for row in score_list[0,5]:
            print(row)'''

pygame.mixer.music.load('song1.wav')
miss_sound = pygame.mixer.Sound('no_sf.wav')
hit_sound = pygame.mixer.Sound('ding_sf.wav')
hit_sound2 = pygame.mixer.Sound('ooh_sf.wav')

while 1:
    pygame.mixer.Sound.play(hit_sound2)

rrtimes = []
rmtimes = []
lmtimes = []
lltimes = []

choice = []
for x in range(4,400,4):
    choice = random.randint(1,4)
    if choice == 1:
        rrtimes.append(x/5)
    elif choice == 2:
        rmtimes.append(x/5)
    elif choice == 3:
        lmtimes.append(x/5)
    else:
        lltimes.append(x/5)


cap = cv2.VideoCapture(0)

play = 0
while Game:
    pygame.display.update()
    while calibrated == False:
        try:
            #median smoothing
            '''if len(ave_x) == 5:
                for y in ave_x:
                    x += y
                ave_x2.append(x/5)
                for p in ave_y:
                    r += p
                ave_y2.append(r/4)
                if len(ave_x2) == 2:
                    if ave_x2[0] + 10 <= ave_x2[1]:
                        print('LEFT')
                    elif ave_x[0] - 10 >= ave_x2[1]:
                        print('RIGHT')
                    elif ave_y2[0] + 10 <= ave_y2[1]:
                        print('UP')
                    elif ave_y2[0] - 10 >= ave_y2[1]:
                        print('DOWN')
                    ave_x2, ave_y2 = [],[]
                ave_x = []
                ave_y = []
                x = 0
                r = 0
            ave_x.append(coord[0][0][0])
            ave_y.append(coord[0][0][1])'''

            #moving average smoothing
            try:
                t02 = t01
                p02 = p01
            except:
                move = 'connecting'
            try:
                t01 = t
                p01 = p
            except:
                move = 'connecting'
            try:
                t = t1
                p = p1
            except:
                move = 'connecting'
            try:
                t1 = t2
                p1 = p2
            except:
                move = 'connecting'
            t2 = coord[0][0][0]
            p2 = coord[0][0][1]

            avex1 = (t02+t01+t+t1+t2)/5
            avey1 = (p02+p01+p+p1+p2)/5
            if avex1 + 10 <= avex2:
                move = 'left'
            elif avex1 - 10 >= avex2:
                move = 'right'
            elif avey1 + 10 <= avey2:
                move = 'up'
            elif avey1 - 10 >= avey2:
                move = 'down'
            else:
                move = 'still'
            avex2 = avex1
            avey2 = avey1
        except:
            move = 'pause'

        _, frame = cap.read()
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        image = frame
        lower_red = np.array([20,100,100])
        upper_red = np.array([30,255,255])
        mask = cv2.inRange(image, lower_red, upper_red)  
        coord = cv2.findNonZero(mask)
        if move == 'still':
            h += 1
        else:
            h = 0            
            font = pygame.font.Font('Road_Rage.ttf',10)
            text = font.render('pls point your controller at the screen and keep it still', True, (255,100,200),(0))
            textRect = text.get_rect()
            textRect.center = (width/2, height/2)
            screen.blit(text,textRect)
        if h == 100:
            for _ in range(500):
                screen.fill(0)
                pygame.draw.circle(screen, (0,255,0), (int(width/2),int(height/2)), 20,0)
                pygame.display.update()
            calibrated = True

        try:
            pygame.draw.circle(screen, colour, (int(avex1),int(avey1)), 20,0)
            font = pygame.font.Font('Road_Rage.ttf',15)
            text = font.render(str(100-h), True, (255,100,200),(0))
            textRect = text.get_rect()
            textRect.center = (width/2, height/2)
            screen.blit(text,textRect)
        except:
            screen.fill(0)
            font = pygame.font.Font('Road_Rage.ttf',12)
            text = font.render('please point your controller at the screen and keep it still until the timer is done', True, (255,100,200),(0))
            textRect = text.get_rect()
            textRect.center = (width/2, height/2)
            screen.blit(text,textRect)
        pygame.display.update()
        screen.fill(0)

    if calibrated == True:
        play += 1
    if play == 1:
        start_time = time.time()
        #pygame.mixer.music.play()
    timer = time.time() - start_time
    if int(timer) == 85:
        save_score(score,player_name)
        Game = False

    llsquare,lmsquare,rmsquare,rrsquare = colour,colour,colour,colour

    try:
        #median smoothing
        '''if len(ave_x) == 5:
            for y in ave_x:
                x += y
            ave_x2.append(x/5)
            for p in ave_y:
                r += p
            ave_y2.append(r/4)
            if len(ave_x2) == 2:
                if ave_x2[0] + 10 <= ave_x2[1]:
                    print('LEFT')
                elif ave_x[0] - 10 >= ave_x2[1]:
                    print('RIGHT')
                elif ave_y2[0] + 10 <= ave_y2[1]:
                    print('UP')
                elif ave_y2[0] - 10 >= ave_y2[1]:
                    print('DOWN')
                ave_x2, ave_y2 = [],[]
            ave_x = []
            ave_y = []
            x = 0
            r = 0
        ave_x.append(coord[0][0][0])
        ave_y.append(coord[0][0][1])'''

        #moving average smoothing
        try:
            t02 = t01
            p02 = p01
        except:
            move = 'connecting'
        try:
            t01 = t
            p01 = p
        except:
            move = 'connecting'
        try:
            t = t1
            p = p1
        except:
            move = 'connecting'
        try:
            t1 = t2
            p1 = p2
        except:
            move = 'connecting'
        t2 = coord[0][0][0]
        p2 = coord[0][0][1]

        avex1 = (t02+t01+t+t1+t2)/5
        avey1 = (p02+p01+p+p1+p2)/5
        if avex1 + 25 <= avex2:
            move = 'left'
        elif avex1 - 15 >= avex2:
            move = 'right'
        elif avey1 + 15 <= avey2:
            move = 'up'
        elif avey1 - 15 >= avey2:
            move = 'down'
        else:
            move = 'still'
        avex2 = avex1
        avey2 = avey1
   
    except:
        move = 'pause'


    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    image = frame
    lower_red = np.array([20,100,100])
    upper_red = np.array([30,255,255])
    mask = cv2.inRange(image, lower_red, upper_red)  
    coord = cv2.findNonZero(mask)

    #cv2.imshow('frame',frame)
    #cv2.imshow('mask',mask)
    #cv2.imshow('res',res)
    
    k = cv2.waitKey(5) & 0xFF
    #cv2.destroyAllWindows()

    if move == 'left':
        times = lltimes
        if hit_check(timer,times):
            lltimes = times
            colour = (0,255,0)
            startan = 0
            pygame.mixer.Sound.play(hit_sound)
            score += 1
        elif startan >= 10:
            colour = (255,0,0)
            startan = 0
            pygame.mixer.Sound.play(miss_sound)
                
    if move == 'up':
        times = lmtimes
        if hit_check(timer,times):
            lmtimes = times
            colour = (0,255,0)
            startan = 0
            pygame.mixer.Sound.play(hit_sound2)
            score += 1
        elif startan >= 10:
            colour = (255,0,0)
            startan = 0
            pygame.mixer.Sound.play(miss_sound)

    if move == 'down':
        times = rmtimes
        if hit_check(timer,times):
            rmtimes = times
            colour = (0,255,0)
            startan = 0
            pygame.mixer.Sound.play(hit_sound)
            score += 1
        elif startan >= 10:
            colour = (255,0,0)
            startan = 0
            pygame.mixer.Sound.play(miss_sound)
                
    if move == 'right':
        times = rrtimes
        if hit_check(timer,times):
            rrtimes = times
            colour = (0,255,0)
            startan = 0
            pygame.mixer.Sound.play(hit_sound2)
            score += 1
        elif startan >= 10:
            colour = (255,0,0)
            startan = 0

    #if move == 'pause':
        #pause()

    for event in pygame.event.get():            
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

        if event.type == KEYDOWN and event.key == K_LEFT:
            times = lltimes
            if hit_check(timer,times):
                lltimes = times
                colour = (0,255,0)
                startan = 0
                pygame.mixer.Sound.play(hit_sound)
            else:
                colour = (255,0,0)
                startan = 0
                pygame.mixer.Sound.play(miss_sound)
                
        if event.type == KEYDOWN and event.key == K_UP:
            times = lmtimes
            if hit_check(timer,times):
                lmtimes = times
                colour = (0,255,0)
                startan = 0
                pygame.mixer.Sound.play(hit_sound2)
            else:
                colour = (255,0,0)
                startan = 0
                pygame.mixer.Sound.play(miss_sound)

        if event.type == KEYDOWN and event.key == K_DOWN:
            times = rmtimes
            if hit_check(timer,times):
                rmtimes = times
                colour = (0,255,0)
                startan = 0
                pygame.mixer.Sound.play(hit_sound)
            else:
                colour = (255,0,0)
                startan = 0
                pygame.mixer.Sound.play(miss_sound)
                
        if event.type == KEYDOWN and event.key == K_RIGHT:
            times = rrtimes
            if hit_check(timer,times):
                rrtimes = times
                colour = (0,255,0)
                startan = 0
                pygame.mixer.Sound.play(hit_sound2)
            else:
                colour = (255,0,0)
                startan = 0

    screen.fill(0)

    pygame.draw.rect(screen,llsquare,(width/4 - 100,height/20,size,size))
    pygame.draw.rect(screen,lmsquare,(width/2 - 100,height/20,size,size))
    pygame.draw.rect(screen,rmsquare,(width*0.75 - 100,height/20,size,size))
    pygame.draw.rect(screen,rrsquare,(width - 100,height/20,size,size))
    
    pygame.draw.rect(screen, (255,255,255), (width/2 - 5, 0, 10, height))
    pygame.draw.rect(screen, (255,255,255), (width/4 - 5, 0, 10, height))
    pygame.draw.rect(screen, (255,255,255), (width*.75 - 5, 0, 10, height))
    pygame.draw.rect(screen, (255,255,255), (width - 5, 0, 10, height))
    pygame.draw.rect(screen, (255,255,255), (-5, 0, 10, height))
    
    try:
        pygame.draw.circle(screen, (255,255,0), (int(avex1),int(avey1)), 5,0)
    except:
        null

    if startan >= 20:
        colour = (0,0,255)
    else:
        hit_animation()
    startan += 1

    for x in range(len(lltimes)):
        #pygame.draw.rect(screen,(255,255,255),(width/4 - 100,(lltimes[x] - timer)*100 + height/20,size,size))
        screen.blit(larrow, (width/4 - 100,(lltimes[x] - timer)*100 + height/20))

    for x in range(len(lmtimes)):
        #pygame.draw.rect(screen,(255,255,255),(width/2 - 100,(lmtimes[x] - timer)*100 + height/20,size,size))
        screen.blit(uarrow, (width/2 - 100,(lmtimes[x] - timer)*100 + height/20))

    for x in range(len(rmtimes)):
        #pygame.draw.rect(screen,(255,255,255),(width*.75 - 100,(rmtimes[x] - timer)*100 + height/20,size,size))
        screen.blit(darrow, (width*.75 - 100,(rmtimes[x] - timer)*100 + height/20))

    for x in range(len(rrtimes)):
        #pygame.draw.rect(screen,(255,255,255),(width - 100,(rrtimes[x] - timer)*100 + height/20,size,size))
        screen.blit(rarrow, (width - 100,(rrtimes[x] - timer)*100 + height/20))

    font = pygame.font.Font('Road_Rage.ttf',10)
    text = font.render(str("{:.0f}".format(timer)), True, (255,100,200),(0))
    textRect = text.get_rect()
    textRect.center = (width/2, height/100)
    screen.blit(text,textRect)

    font = pygame.font.Font('Road_Rage.ttf',40)
    text = font.render(str(score), True, (255,100,200),(0))
    textRect = text.get_rect()
    textRect.center = (width/2, height/2)
    screen.blit(text,textRect)

    if miss_check(timer,lltimes,lmtimes,rmtimes,rrtimes):
        colour = (255,0,0)
        startan = 0
        pygame.mixer.Sound.play(miss_sound)

    pygame.display.update()

