import pygame
from pygame.locals import *
import numpy
import time
import random

WEIGHT = 3
DIVISOR = 3

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
        for i in range(leftbound, rightbound):
            left_color = pix_array[i-1][row-1]
            #left_color = left_color[2:-1]
            center_color = pix_array[i][row-1]
            right_color = pix_array[i+1][row-1]
            test = 0x000000
            left = left_color != test
            center = center_color != test
            right = right_color != test
            #print "color", hex(left_color), hex(center_color), hex(right_color)
            #print hex(center_color & 0xff0000)

            #print "avrge", hex(red_avg), hex(green_avg), hex(blue_avg)
            if rule30(left, center, right):
                red_avg = (WEIGHT*left*(left_color & 0xff0000) + WEIGHT*center*(center_color & 0xff0000)
                + WEIGHT*right*(right_color & 0xff0000)) / DIVISOR
                green_avg = (WEIGHT*left*(left_color & 0xff00) + WEIGHT*center*(center_color & 0xff00)
                    + WEIGHT*right*(right_color & 0xff00)) / DIVISOR
                blue_avg = (WEIGHT*left*(left_color & 0xff) + WEIGHT*center*(center_color & 0xff)
                    + WEIGHT*right*(right_color & 0xff)) / DIVISOR
                avg = red_avg + green_avg + blue_avg
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
background.fill(0x000000)
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
