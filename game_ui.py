import pygame
from assets import empty_heart_img, exp_middle_img, exp_fill_img, exp_left_img, exp_right_img, full_heart_img, half_heart_img
from values import INIT_PLAYER_STATS

def display_health(health ,screen):
    loc = [10, 10]
    offset = 30
    full_hearts = int(health/2)
    half_hearts = health % 2
    empty_hearts = int((INIT_PLAYER_STATS['health'] / 2) - full_hearts - half_hearts)

    for _ in range(0, full_hearts):
        screen.blit(full_heart_img, loc)
        loc[0] += offset

    for _ in range(0, half_hearts):
        screen.blit(half_heart_img, loc)
        loc[0] += offset

    for _ in range(0, empty_hearts):
        screen.blit(empty_heart_img, loc)
        loc[0] += offset

def display_exp_bar(exp, screen):
    exp_divisions = 20
    loc = [280, 10]
    exp_ticks = exp % exp_divisions
    for _ in range(0, exp_ticks):
        screen.blit(exp_fill_img, loc)
        loc[0] += 28 -4

    loc = [270, 10]
    screen.blit(exp_left_img, loc)
    loc[0] += 10
    for _ in range(0, exp_divisions):
        screen.blit(exp_middle_img, loc)
        loc[0] += 28 -4

    loc[0] -= 19
    screen.blit(exp_right_img, loc)
