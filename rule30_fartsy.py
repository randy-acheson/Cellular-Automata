import pygame
from pygame.locals import *
import numpy
import time
import random

def gate1(a, b, c):
    if (a and not (b or c)): return True
    else: return False

# rule 30
def update_cell(row):
    mid = screen_rect.centerx
    leftbound = mid-row
    rightbound = mid+row+1
    if rightbound < screen_rect.right:
        for i in range(leftbound, rightbound):
            test = 0x000000
            left_color = pix_array[i-1][row-1]
            center_color = pix_array[i][row-1]
            right_color = pix_array[i+1][row-1]
            left = left_color != test
            center = center_color != test
            right = right_color != test
            avg = (left_color*left + center_color*center + right_color*right)\
                  / (left + center + right)
            if (gate1(left, center, right)
                or (right and not (center or left))
                or (center and not (left or right))
                or (center and right and not left)):
                pix_array[i][row] = avg
            else:
                pix_array[i][row] = 0x000000
                #pix_array[i][row] = (random.randint(0, 16777215))


pygame.init()
scr_width = 1366
scr_height = 768
screen = pygame.display.set_mode((scr_width, scr_height), pygame.FULLSCREEN)
screen_rect = screen.get_rect()

background = pygame.Surface(screen.get_size()).convert()
background.fill(0xffffff)
screen.blit(background, (0, 0))
pix_array = pygame.surfarray.pixels2d(background)
pix_array[screen_rect.centerx-1][1] = 0xff0000
pix_array[screen_rect.centerx][1] = 0x00ff00
pix_array[screen_rect.centerx+1][1] = 0x0000ff
del pix_array
pygame.display.update()

running = True
go = True
while running:

    for event in pygame.event.get():
        if (event.type == KEYDOWN and event.key == K_RETURN) or event.type == QUIT:
            running = False
    if go:
        for i in range(2, screen_rect.height - 1):
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
