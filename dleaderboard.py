import pygame
from pygame.locals import *
import os
import time
import csv

pygame.init()

os.environ['SDL_VIDEO_CENTERED'] = "True"

width, height = 1200,600
screen = pygame.display.set_mode((width,height))

background = pygame.image.load('background.PNG')
background = pygame.transform.scale(background, (1200,600))

menu = True

leaderboard = []
leaderboard_name = []

with open('dleaderboards.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count != 0:
            leaderboard.append(row[1])
            leaderboard_name.append(row[0])
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

'''with open('fileName.csv', 'w') as f:
    for x in range(len(leaderboard)):
        f.write(leaderboard[x],)
        f.write( leaderboard_name[x])'''

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
    lightning = pygame.image.load('lightning' + lframe[lcount] + '.png')
    lightning = pygame.transform.scale(lightning,lframe_size)
    lightning2 = pygame.image.load('lightning' + lframe[lcount2] + '.png')
    lightning2 = pygame.transform.scale(lightning2,lframe_size)
    screen.blit(lightning, (300,-20))
    screen.blit(lightning2, (800,-100))
    screen.blit(lightning, (1000,0))
    screen.blit(lightning2, (100,-50))
    screen.blit(kweku, (100,300))
    screen.blit(joh, (width - 375,300))
    return lcount,lcount2,fcount

while menu:

    click = False
    mouse = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.MOUSEBUTTONUP:
            click = True
    
    screen.blit(background,(0,0))

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
            import background

    else:
        font = pygame.font.Font('Road_Rage.ttf',30)
        text = font.render('back', True, (255,100,200),(0))
        textRect = text.get_rect()
        textRect.center = (100, 550)
        screen.blit(text,textRect)

    pygame.display.update()
