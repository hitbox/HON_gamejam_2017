import pygame
from assets import *
from values import *



def display_health(health ,screen):
    loc = [10, 10]
    offset = 30
    full_hearts = int(health/2)
    half_hearts = health % 2
    empty_hearts = int((INIT_PLAYER_STATS['health'] / 2) - full_hearts - half_hearts)



    for _ in range(0, full_hearts):
        screen.blit(pygame.image.load(full_heart_img), loc)
        loc[0] += offset

    for _ in range(0, half_hearts):
        screen.blit(pygame.image.load(half_heart_img), loc)
        loc[0] += offset

    #print(str(full_hearts) + str(half_hearts) + str(empty_hearts))
    for _ in range(0, empty_hearts):
        screen.blit(pygame.image.load(empty_heart_img), loc)
        loc[0] += offset

def display_exp_bar(exp, screen):

    exp_divisions = 20
    loc = [280, 10]
    exp_ticks = exp % exp_divisions
    for _ in range(0, exp_ticks):
        screen.blit(pygame.image.load(exp_fill_img), loc)
        loc[0] += 28 -4

    loc = [270, 10]
    screen.blit(pygame.image.load(exp_left_img), loc)
    loc[0] += 10
    for _ in range(0, exp_divisions):
        screen.blit(pygame.image.load(exp_middle_img), loc)
        loc[0] += 28 -4

    loc[0] -= 19
    screen.blit(pygame.image.load(exp_right_img), loc)
