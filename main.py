import pygame
from pygame.locals import *
from sys import exit
from values import *
from events import *
from assets import *
from sprites import *
from scene import *

clock = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)

#set the current scene
scene_id = 0

#initialize the player
player = Player(player_img, PLAYER_SPEED_INIT, 100, 100)

#initialize title screen
title_screen_buttons = [Button((200, 200),startbutton_img), Button((200, 300), quitbutton_img)]
title_menu = Menu(title_background_img, title_screen_buttons)

#initialize level 1 background
level1_background = GameBackground(level1_background_img)

#make ally sprite group
ally_sprite_group = pygame.sprite.Group()
ally_sprite_group.add(player)

while True:

    dt = clock.tick(FPS)
    game_speed = float(dt)/64

    handle_events(scene_id, player)
    #player.print_rect_loc()

    if scene_id == 1:
        player.behave(game_speed)
        level1_background.display(screen)
        ally_sprite_group.draw(screen)
    if scene_id == 0:
        title_menu.display(screen)

    pygame.display.update()
