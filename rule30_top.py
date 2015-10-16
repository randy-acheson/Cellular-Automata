import pygame
from pygame.locals import *
import numpy
import time
import random

def rule30(left, center, right):
    if ((left and not (center or right)) \
    or (right and not (center or left)) \
    or (center and not (left or right)) \
    or (center and right and not left)):
        return True
    return False

# rule 30
def update_cell(row):
    mid = screen_rect.centerx
    leftbound = mid-row
    rightbound = mid+row+1
    if rightbound < screen_rect.right:
        for i in range(0, screen_rect.width - 1):
            test = 0xffffff
            left = pix_array[i-1][row-1] != test
            center = pix_array[i][row-1] != test
            right = pix_array[i+1][row-1] != test
            if rule30(left, center, right):
                pix_array[i][row] = 0x000000
            else:
                pix_array[i][row] = 0xffffff



pygame.init()
scr_width = 1366
scr_height = 768
screen = pygame.display.set_mode((scr_width, scr_height), pygame.FULLSCREEN)
screen_rect = screen.get_rect()

background = pygame.Surface(screen.get_size()).convert()
background.fill(0xffffff)
screen.blit(background, (0, 0))
pix_array = pygame.surfarray.pixels2d(background)
for i in range (screen_rect.width/2, screen_rect.width - 1):
    pix_array[i][0] = 0x00ff00
del pix_array
pygame.display.update()

running = True
go = True
while running:

    for event in pygame.event.get():
        if (event.type == KEYDOWN and event.key == K_RETURN) or event.type == QUIT:
            running = False
    if go:
        for i in range(1, screen_rect.height - 1):
            pix_array = pygame.surfarray.pixels2d(background)
            update_cell(i)
            del pix_array
            screen.blit(background, (0, 0))
            pygame.display.update()
            for event in pygame.event.get():
                if (event.type == KEYDOWN and event.key == K_RETURN) or event.type == QUIT:
                    pygame.quit()
        go = False

pygame.quit()
