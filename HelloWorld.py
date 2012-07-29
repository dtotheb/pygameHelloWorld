#!/usr/bin/python
import sys
import pygame
from pygame.locals import *

#setup pygame
pygame.init()

#setup the window
windowSurface = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption('Hello World!')

#setup the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

#setup the fonts
basicFont = pygame.font.SysFont(None, 48)

#setup the text
text = basicFont.render('Hello World!', True, WHITE, BLUE)
textRect = text.get_rect()
textRect.centerx = windowSurface.get_rect().centerx
textRect.centery = windowSurface.get_rect().centery

windowSurface.fill(WHITE)

pygame.draw.polygon(windowSurface, RED,
    ((146, 0),
     (291, 106),
     (236, 277),
     (56, 277),
     (0, 106))
    )

windowSurface.blit(text, textRect)

pygame.display.update()

#run the game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
