import pygame
from pygame.locals import *
import os
import random
import time
import cv2
import numpy as np
import csv

#login and sign up
def login_signup():

    def login():
        while 1:
            pause()
            mousepos = pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            screen.fill(0)
            font = pygame.font.Font('Road_Rage.ttf',25)
            text = font.render('LOGIN', True, (255,255,255),(0))
            textRect = text.get_rect()
            textRect.center = (width/8, height/10)
            screen.blit(text,textRect) 

            font = pygame.font.Font('Road_Rage.ttf',40)
            text1 = font.render(str(''.join(textbox1)), True, (255,100,200),(255,255,255))
            text1Rect = text1.get_rect()
            text1Rect.center = (usernamepos[0], usernamepos[1])
            screen.blit(text1,text1Rect)

            font = pygame.font.Font('Road_Rage.ttf',40)
            text2 = font.render(str(''.join(textbox2)), True, (255,100,200),(255,255,255))
            text2Rect = text2.get_rect()
            text2Rect.center = (passwordpos[0], passwordpos[1])
            screen.blit(text2,text2Rect)

            font = pygame.font.Font('Road_Rage.ttf',30)
            context = font.render('continue', True, (255,100,200),(0))
            contextRect = context.get_rect()
            contextRect.center = (width - width/5, height - height/5)
            screen.blit(context,contextRect)

            for event in pygame.event.get():
                if event.type == pygame.KEYUP:
                    if event.key == K_BACKSPACE:
                        if text1Rect.collidepoint(mousepos[0],mousepos[1]):
                            textbox1.pop(-1)
                        if text2Rect.collidepoint(mousepos[0],mousepos[1]):
                            textbox2.pop(-1)
                    else:
                        if text1Rect.collidepoint(mousepos[0],mousepos[1]):
                            textbox1.append(pygame.key.name(event.key))
                        elif text2Rect.collidepoint(mousepos[0],mousepos[1]):
                            textbox2.append(pygame.key.name(event.key))

                if event.type == pygame.MOUSEBUTTONUP and contextRect.collidepoint(mousepos[0],mousepos[1]):
                    password = ''.join(textbox2)
                    username = ''.join(textbox1)
                    f = open("login.csv","r")
                    for line in f:
                        details = line.split(",")
                        print(line)
                        print(details)
                        if str(username) == details[0] and str(password) + '\n' == details[1]:
                            screen.fill(0)
                            font = pygame.font.Font('Road_Rage.ttf',90)
                            text1 = font.render(str('login successful'), True, (255,100,200),(0))
                            text1Rect = text1.get_rect()
                            text1Rect.center = (width/2, height/2)
                            screen.blit(text1,text1Rect)
                            pygame.display.update()
                            time.sleep(4)
                            menu(username)
                    login_signup()

            pygame.display.update()

    def signup():
        while True:
            mousepos = pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            
            screen.fill(0)
            font = pygame.font.Font('Road_Rage.ttf',25)
            text = font.render('SIGN UP', True, (255,255,255),(0))
            textRect = text.get_rect()
            textRect.center = (width/8, height/10)
            screen.blit(text,textRect) 
        
            font = pygame.font.Font('Road_Rage.ttf',40)
            text1 = font.render(str(''.join(textbox1)), True, (255,100,200),(255,255,255))
            text1Rect = text1.get_rect()
            text1Rect.center = (usernamepos[0], usernamepos[1])
            screen.blit(text1,text1Rect)

            font = pygame.font.Font('Road_Rage.ttf',40)
            text2 = font.render(str(''.join(textbox2)), True, (255,100,200),(255,255,255))
            text2Rect = text2.get_rect()
            text2Rect.center = (passwordpos[0], passwordpos[1])
            screen.blit(text2,text2Rect)

            font = pygame.font.Font('Road_Rage.ttf',30)
            context = font.render('continue', True, (255,100,200),(0))
            contextRect = context.get_rect()
            contextRect.center = (width - width/5, height - height/5)
            screen.blit(context,contextRect)

            for event in pygame.event.get():
                if event.type == pygame.KEYUP:
                    if event.key == K_BACKSPACE:
                        if text1Rect.collidepoint(mousepos[0],mousepos[1]):
                            textbox1.pop(-1)
                        if text2Rect.collidepoint(mousepos[0],mousepos[1]):
                            textbox2.pop(-1)
                    else:
                        if text1Rect.collidepoint(mousepos[0],mousepos[1]):
                            textbox1.append(pygame.key.name(event.key))
                        elif text2Rect.collidepoint(mousepos[0],mousepos[1]):
                            textbox2.append(pygame.key.name(event.key))

                if event.type == pygame.MOUSEBUTTONUP and contextRect.collidepoint(mousepos[0],mousepos[1]):
                    username = ''.join(textbox1)
                    password = ''.join(textbox2)
                    f = open("login.csv","r")
                    for line in f:
                        details = line.split(",")
                        if username == details[0]:
                            login_signup()
                    with open('login.csv', 'a', newline='') as file:
                        writer = csv.writer(file)
                        writer.writerow(([username, password]))
                    screen.fill(0)
                    font = pygame.font.Font('Road_Rage.ttf',90)
                    text1 = font.render(str('login successful'), True, (255,100,200),(0))
                    text1Rect = text1.get_rect()
                    text1Rect.center = (width/2, height/2)
                    screen.blit(text1,text1Rect)
                    pygame.display.update()
                    time.sleep(5)
                    menu(username)

            pygame.display.update()

    os.environ['SDL_VIDEO_CENTERED'] = "True"
    width, height = 1200,600
    screen = pygame.display.set_mode((width,height))
    pygame.init()

    usernamepos = (width/2, (height/5)*2)
    passwordpos = (width/2, (height/5)*4)
    

    textbox1 = [' ']
    textbox2 = [' ']
    pointer = (0,0)
    choice = True
    while choice:
        mousepos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.fill(0)
        font = pygame.font.Font('Road_Rage.ttf',40)
        text1 = font.render('LOGIN', True, (255,100,200),(0))
        text1Rect = text1.get_rect()
        text1Rect.center = (width/4,height/2)
        screen.blit(text1,text1Rect)

        font = pygame.font.Font('Road_Rage.ttf',40)
        text2 = font.render('SIGN UP', True, (255,100,200),(0))
        text2Rect = text2.get_rect()
        text2Rect.center = (width*.75,height/2)
        screen.blit(text2,text2Rect)

        font = pygame.font.Font('Road_Rage.ttf',40)
        text3 = font.render('SIGN UP', True, (255,100,200),(0))
        text3Rect = text3.get_rect()
        text3Rect.center = (width*.5,height*.75)
        screen.blit(text3,text3Rect)


        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                if text1Rect.collidepoint(mousepos[0],mousepos[1]):
                    login()
                if text2Rect.collidepoint(mousepos[0],mousepos[1]):
                    signup()
                if text3Rect.collidepoint(mousepos[0],mousepos[1]):
                    menu('guest')
        pygame.display.update()

def leaderboards(username):
    width, height = 1200,600
    screen = pygame.display.set_mode((width,height))

    leaderboard = []
    leaderboard_name = []

    with open('ddr leaderboard.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count != 0:
                leaderboard.append(row[0])
                leaderboard_name.append(row[1])
                line_count += 1
            else:
                line_count += 1
        csv_file.close()
            
    count = 0
    i = 0
    p = 0
    while p != len(leaderboard):
        j = i + 1
        if leaderboard[i] < leaderboard[j]:             
            savenum = leaderboard[j]
            leaderboard[j] = leaderboard[i]
            leaderboard[i] = savenum
            savenum_name = leaderboard_name[j]
            leaderboard_name[j] = leaderboard_name[i]
            leaderboard_name[i] = savenum_name
            p = 0
        else:
            p += 1
        i += 1
        if i == len(leaderboard) - 1:
            i = 0
        count += 1

    lcount = 0
    lcount2 = 4
    fcount = 0

    def effects(lcount,lcount2,fcount):
        lframe_size = [50,350]
        lframe = ['1','2','3','2','3','2','1','1','2','1','1','2','1','2','1']
        fframe = ['1','2','3','4','5','6','7','6','5','4','3','2',]
        if lcount < len(lframe) - 1:
            lcount += 1
        else:
            lcount = 0

        if lcount2 < len(lframe) - 1:
            lcount2 += 1
        else:
            lcount2 = 0

        if fcount < len(fframe) - 1:
            fcount += 1
        else:
            fcount = 0
    
        kweku = pygame.image.load('kweku' + fframe[fcount] + '.png')
        kweku = pygame.transform.scale(kweku,(200,200))
        joh = pygame.image.load('joh' + fframe[fcount] + '.png')
        joh = pygame.transform.scale(joh,(200,200))
        screen.blit(kweku, (100,300))
        screen.blit(joh, (width - 375,300))
        return lcount,lcount2,fcount

    while menu:
        pygame.init()

        click = False
        mouse = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEBUTTONUP:
                click = True

        screen.fill(0)

        lcount,lcount2,fcount = effects(lcount,lcount2,fcount)

        font = pygame.font.Font('Road_Rage.ttf',100)
        text = font.render('leaderboards', True, (100,100,100),(0))
        textRect = text.get_rect()
        textRect.center = (width/2 + 5, 105)
        screen.blit(text,textRect)

        font = pygame.font.Font('Road_Rage.ttf',100)
        text = font.render('leaderboards', True, (255,50,255),(0))
        textRect = text.get_rect()
        textRect.center = (width/2, 100)
        screen.blit(text,textRect)

        font = pygame.font.Font('Road_Rage.ttf',30)
        text = font.render(leaderboard_name[0], True, (255,255,255),(0))
        textRect = text.get_rect()
        textRect.center = (width/2 - 150 , 200)
        screen.blit(text,textRect)

        font = pygame.font.Font('Road_Rage.ttf',30)
        text = font.render(leaderboard_name[1], True, (255,255,255),(0))
        textRect = text.get_rect()
        textRect.center = (width/2 - 150 , 250)
        screen.blit(text,textRect)

        font = pygame.font.Font('Road_Rage.ttf',30)
        text = font.render(leaderboard_name[2], True, (255,255,255),(0))
        textRect = text.get_rect()
        textRect.center = (width/2 - 150 , 300)
        screen.blit(text,textRect)

        font = pygame.font.Font('Road_Rage.ttf',30)
        text = font.render(leaderboard_name[3], True, (255,255,255),(0))
        textRect = text.get_rect()
        textRect.center = (width/2 - 150 , 350)
        screen.blit(text,textRect)
    
        font = pygame.font.Font('Road_Rage.ttf',30)
        text = font.render(leaderboard_name[4], True, (255,255,255),(0))
        textRect = text.get_rect()
        textRect.center = (width/2 - 150 , 400)
        screen.blit(text,textRect)

        font = pygame.font.Font('Road_Rage.ttf',30)
        text = font.render(leaderboard_name[5], True, (255,255,255),(0))
        textRect = text.get_rect()
        textRect.center = (width/2 - 150 , 450)
        screen.blit(text,textRect)

        font = pygame.font.Font('Road_Rage.ttf',30)
        text = font.render(leaderboard[0], True, (255,255,255),(0))
        textRect = text.get_rect()
        textRect.center = (width/2 + 100 , 200)
        screen.blit(text,textRect)

        font = pygame.font.Font('Road_Rage.ttf',30)
        text = font.render(leaderboard[1], True, (255,255,255),(0))
        textRect = text.get_rect()
        textRect.center = (width/2 + 100 , 250)
        screen.blit(text,textRect)

        font = pygame.font.Font('Road_Rage.ttf',30)
        text = font.render(leaderboard[2], True, (255,255,255),(0))
        textRect = text.get_rect()
        textRect.center = (width/2 + 100 , 300)
        screen.blit(text,textRect)

        font = pygame.font.Font('Road_Rage.ttf',30)
        text = font.render(leaderboard[3], True, (255,255,255),(0))
        textRect = text.get_rect()
        textRect.center = (width/2 + 100 , 350)
        screen.blit(text,textRect)
    
        font = pygame.font.Font('Road_Rage.ttf',30)
        text = font.render(leaderboard[4], True, (255,255,255),(0))
        textRect = text.get_rect()
        textRect.center = (width/2 + 100 , 400)
        screen.blit(text,textRect)

        font = pygame.font.Font('Road_Rage.ttf',30)
        text = font.render(leaderboard[5], True, (255,255,255),(0))
        textRect = text.get_rect()
        textRect.center = (width/2 + 100 , 450)
        screen.blit(text,textRect)

        if 50 < mouse[0] < 150 and 530< mouse[1] < 570:
            font = pygame.font.Font('Road_Rage.ttf',45)
            text = font.render('back', True, (255,100,200),(0))
            textRect = text.get_rect()
            textRect.center = (100, 550)
            screen.blit(text,textRect)
            if click:
                menu(username)

        else:
            font = pygame.font.Font('Road_Rage.ttf',30)
            text = font.render('back', True, (255,100,200),(0))
            textRect = text.get_rect()
            textRect.center = (100, 550)
            screen.blit(text,textRect)

        pygame.display.update()



def game(username):
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

    def save_score(score,username):
        with open('ddr leaderboard.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow((score, username))

        menu()

    def pause():
        pause = pygame.Surface(300,300)
        pause.set_alpha(150)
        pause.fill((255,255,255))
    
        font = pygame.font.Font('Road_Rage.ttf',50)
        text = font.render('Resume', True, (0,0,255),(0))
        textRect = text.get_rect()
        textRect.center = (400, 300)    
    
        font = pygame.font.Font('Road_Rage.ttf',50)
        text2 = font.render('calibrate', True, (0,0,255),(0))
        textRect2 = text2.get_rect()
        textRect2.center = (200, 300)

        font = pygame.font.Font('Road_Rage.ttf',50)
        text3 = font.render('restart', True, (0,0,255),(0))
        textRect3 = text3.get_rect()
        textRect3.center = (300, 400)

        while 1:
            screen.fill(0)
            mousepos = pygame.mouse.get_pos()
            screen.blit(pause,(150,150))
            screen.blit(text,textRect)
            screen.blit(text2,textRect2)

            for event in pygame.event.get():
                if  event.type == pygame.MOUSEBUTTONUP and text2Rect.collidepoint(mousepos[0],mousepos[1]):
                    return
                elif event.type == pygame.MOUSEBUTTONUP and textRect.collidepoint(mousepos[0],mousepos[1]):
                    while 1:
                        try:
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
                            pause()

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

    def pause():
        pause = pygame.Surface((300,300))
        pause.set_alpha(50)
        pause.fill((255,255,255))
    
        font = pygame.font.Font('Road_Rage.ttf',20)
        text = font.render('Resume', True, (0,0,255),(0))
        textRect = text.get_rect()
        textRect.center = (400, 300)    
    
        font = pygame.font.Font('Road_Rage.ttf',20)
        text2 = font.render('calibrate', True, (0,0,255),(0))
        textRect2 = text2.get_rect()
        textRect2.center = (200, 300)
        
        cap = cv2.VideoCapture(0)

        while 1:
            screen.fill(0)
            mousepos = pygame.mouse.get_pos()
            screen.blit(pause,(150,150))
            screen.blit(text,textRect)
            screen.blit(text2,textRect2)
            screen.blit(text3,text3Rect)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP and textRect.collidepoint(mousepos[0],mousepos[1]):
                    return
                elif event.type == pygame.MOUSEBUTTONUP and text3Rect.collidepoint(mousepos[0],mousepos[1]):
                    game(username)
                elif event.type == pygame.MOUSEBUTTONUP and text2Rect.collidepoint(mousepos[0],mousepos[1]):
                    while 1:
                        try:
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
                            pause()

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


    def end_game(score):
        for _ in range(100):
            screen.fill(0)
            if score >= 80:
                font = pygame.font.Font('Road_Rage.ttf',90)
                text = font.render(str("That was Awesome"), True, (255,100,200),(0))
                textRect = text.get_rect()
                textRect.center = (width/2, height/2)
                screen.blit(text,textRect)
            elif score >= 60:
                font = pygame.font.Font('Road_Rage.ttf',40)
                text = font.render(str("meh"), True, (255,100,200),(0))
                textRect = text.get_rect()
                textRect.center = (width/2, height/2)
                screen.blit(text,textRect)
            elif score <= 59:
                font = pygame.font.Font('Road_Rage.ttf',40)
                text = font.render(str("you're kinda trash"), True, (255,100,200),(0))
                textRect = text.get_rect()
                textRect.center = (width/2, height/2)
                screen.blit(text,textRect)


            font = pygame.font.Font('Road_Rage.ttf',40)
            text = font.render(str('you got ', score), True, (255,100,200),(0))
            textRect = text.get_rect()
            textRect.center = (width/2, (height/2) + 100)
            screen.blit(text,textRect)

    pygame.mixer.music.load('song1.wav')
    miss_sound = pygame.mixer.Sound('no_sf.wav')
    hit_sound = pygame.mixer.Sound('ding_sf.wav')
    hit_sound2 = pygame.mixer.Sound('ooh_sf.wav')

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
            pygame.mixer.music.play()
        timer = time.time() - start_time
        if int(timer) == 85:
            end_game()
            save_score(score,username)
            Game = False
            menu()

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
                move = 'connected'
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
            connection = True
   
        except:
            try:
                if connection:
                    print(1)
                    pause()
                    print(2)
            except:
                move = ' '
            move = 'disconnected'


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

def menu(username):
    menu = True
    os.environ['SDL_VIDEO_CENTERED'] = "True"

    width, height = 1200,600
    screen = pygame.display.set_mode((width,height))
    pygame.init()
    pygame.mixer.music.load('menu music.wav')
    pygame.mixer.music.play(-1)

    startpos = (width/2, height/4)
    scorepos = (width/4, (height/4)*3)
    helppos = ((width/4)*3, (height/4)*3)

    pointer = (0,0)

    cap = cv2.VideoCapture(0)
    while menu:
        screen.fill(0)
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


            pointer = ((t+t1+t2)/1.5, (p+p1+p2)/2)
        except:
            move = 0

        _, frame = cap.read()
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        image = frame
        lower_red = np.array([20,100,100])
        upper_red = np.array([30,255,255])
        mask = cv2.inRange(image, lower_red, upper_red)  
        coord = cv2.findNonZero(mask)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        font = pygame.font.Font('Road_Rage.ttf',90)
        text = font.render('START', True, (255,100,200),(0))
        textRect = text.get_rect()
        textRect.center = (startpos[0], startpos[1])
        screen.blit(text,textRect)

        font = pygame.font.Font('Road_Rage.ttf',45)
        text = font.render('help', True, (255,255,255),(0))
        textRect = text.get_rect()
        textRect.center = (helppos[0], helppos[1])
        screen.blit(text,textRect)        
        
        font = pygame.font.Font('Road_Rage.ttf',45)
        text = font.render('leaderboards', True, (255,255,255),(0))
        textRect = text.get_rect()
        textRect.center = (scorepos[0], scorepos[1])
        screen.blit(text,textRect)
        
        font = pygame.font.Font('Road_Rage.ttf',25)
        text = font.render(str(username), True, (255,255,255),(0))
        textRect = text.get_rect()
        textRect.center = (width/8, height/10)
        screen.blit(text,textRect)        
        
        if startpos[0] - 150 < pointer[0] < startpos[0] + 150 and startpos[1] - 30 < pointer[1] < startpos[1] + 30:
            start_time += 1
            pygame.draw.rect(screen, (255,255,255), (startpos[0],startpos[1],60,10))
            pygame.draw.rect(screen, (0,0,255), (startpos[0], startpos[1], start_time*1.5, 10))
            if start_time == 40:
                game(username)
        else:
            start_time = 0

        if scorepos[0] - 100 < pointer[0] < scorepos[0] + 100 and scorepos[1] - 30 < pointer[1] < scorepos[1] + 30:
            lb_time += 1
            pygame.draw.rect(screen, (255,255,255), (scorepos[0],scorepos[1],60,10))
            pygame.draw.rect(screen, (0,0,255), (scorepos[0], scorepos[1], lb_time*1.5, 10))
            if lb_time == 40:
                leaderboards(username)
        else:
            lb_time = 0

        if helppos[0] - 100 < pointer[0] < helppos[0] + 100 and helppos[1] - 30 < pointer[1] < helppos[1] + 30:
            help_time += 1
            pygame.draw.rect(screen, (255,255,255), (helppos[0],helppos[1],60,10))
            pygame.draw.rect(screen, (0,0,255), (helppos[0], helppos[1], help_time*1.5, 10))
            if help_time == 40:
                helppage()
        else:
            help_time = 0

        pygame.draw.circle(screen, (255,255,0), (int(pointer[0]),int(pointer[1])), 5,0)

        pygame.display.update()

game('test')
login_signup()