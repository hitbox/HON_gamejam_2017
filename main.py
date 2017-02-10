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
current_menu = None
#initialize the player
player = Player(player_front_frames, player_back_frames, player_right_frames, player_left_frames, PLAYER_SPEED_INIT, 100, 100, 200)

#initialize title screen
title_screen_buttons = [Button((200, 200),startbutton_img, 1), Button((200, 300), quitbutton_img, -1)]
title_menu = Menu(screen, title_background_img, title_screen_buttons)
current_menu = title_menu
#initialize level 1 background
level1_background = GameBackground(level1_background_img)

#make ally sprite group
ally_sprite_group = pygame.sprite.Group()
ally_sprite_group.add(player)

while True:
    #print(str(scene_id))
    dt = clock.tick(FPS)
    game_speed = float(dt)/64

    scene_id = handle_events(scene_id, player, current_menu)
    #player.print_rect_loc()

    if scene_id == 0:
        title_menu.display(screen)
    if scene_id == 1:
        player.behave(game_speed, dt)
        level1_background.display(screen)
        ally_sprite_group.draw(screen)


    pygame.display.update()
