#!/usr/bin/python
import sys
import random
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

# Fill background

background = pygame.Surface(windowSurface.get_size())
background = background.convert()
background.fill(WHITE)


#setup the fonts
basicFont = pygame.font.SysFont(None, 48)

#setup the text
text = basicFont.render('Hello!', True, WHITE, BLUE)
textRect = text.get_rect()
textRect.center = windowSurface.get_rect().center


#display everything
def displayEverything():
    windowSurface.blit(background, (0, 0))
    windowSurface.blit(text, textRect)
    pygame.display.update()

#initial display
displayEverything()


#intial vector
def randomVector(n):
    x = random.randint(-1 * n, n)
    y = random.randint(-1 * n, n)
    return (x, y)

vector = randomVector(2)

#moves the Rect and checks for bounds
def moveStuff():
    global textRect
    global vector
    textRect.move_ip(vector)

    #figure out the size of things
    hx = textRect.width / 2
    hy = textRect.height / 2
    x = textRect.centerx
    y = textRect.centery

    maxwidth = windowSurface.get_width()
    maxheight = windowSurface.get_height()

    #check for bounds
    if x + hx >= maxwidth or x - hx <= 0:
        vector = (vector[0] * -1, vector[1])
    if y + hy >= maxheight or y - hy <= 0:
        vector = (vector[0], vector[1] * -1)


#run the game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                vector = randomVector(2)

    moveStuff()
    displayEverything()
