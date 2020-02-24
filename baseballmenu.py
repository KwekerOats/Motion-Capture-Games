import pygame
from pygame.locals import *
import os
import time

pygame.init()

os.environ['SDL_VIDEO_CENTERED'] = "True"

width, height = 1200,600
screen = pygame.display.set_mode((width,height))

while 1:
	pygame.key.start_text_input()
    input_rect = pygame.Rect(80,80,320,40)
    pygame.key.set_text_input_rect(input_rect)
                        _IMEEditing = False
                    continue
                
                if event.key == pygame.K_BACKSPACE:
                    if (len(_IMEText) > 0 and _IMETextPos > 0):