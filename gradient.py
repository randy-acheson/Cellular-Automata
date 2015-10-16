import pygame
from pygame.locals import *
import numpy
import time
import random

WEIGHT = 1

def rule30(left, center, right):
    if ((left and not (center or right)) \
    or (right and not (center or left))):
        return True
    return False

# rule 30
def update_cell(row):
    mid = screen_rect.centerx
    leftbound = mid-row
    rightbound = mid+row+1
    if rightbound < screen_rect.right:
        for i in range(leftbound, rightbound):
            left_color = pix_array[i-1][row-1]
            center_color = pix_array[i][row-1]
            right_color = pix_array[i+1][row-1]
            test = 0xffffff
            left = left_color != test
            center = center_color != test
            right = right_color != test

            red_avg = (WEIGHT*left*(left_color & 0xff0000) + WEIGHT*center*(center_color & 0xff0000)
            + WEIGHT*right*(right_color & 0xff0000)) / (3)
            green_avg = (WEIGHT*left*(left_color & 0xff00) + WEIGHT*center*(center_color & 0xff00)
                + WEIGHT*right*(right_color & 0xff00)) / (3)
            blue_avg = (WEIGHT*left*(left_color & 0xff) + WEIGHT*center*(center_color & 0xff)
                + WEIGHT*right*(right_color & 0xff)) / (3)
            avg = red_avg + green_avg + blue_avg
            pix_array[i][row] = avg


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
pix_array[screen_rect.centerx][1] = 0xff0000
pix_array[screen_rect.centerx+1][1] = 0xff0000
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
