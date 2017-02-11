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

pygame.font.init()
stats_font = pygame.font.SysFont('Comic Sans', 30)

#set the current scene
scene_id = 0
current_menu = None



#initialize the player
player = Player(player_front_frames, player_back_frames, player_right_frames, player_left_frames, INIT_PLAYER_STATS, (SCREEN_SIZE[0]/2) - 10, (SCREEN_SIZE[1]/2) - 15, 200)

#initialize title screen
title_screen_buttons = [Button((200, 200),startbutton_img, 1), Button((200, 300), quitbutton_img, -1)]
title_menu = Menu(screen, title_background_img, title_screen_buttons)
current_menu = title_menu
#initialize level 1 background
level1_background = GameBackground(level1_background_img, player.stats, 0, 0)

#make ally sprite group


background_sprite_group.add(level1_background)
ally_sprite_group.add(player)


while True:
    #print(str(scene_id))
    dt = clock.tick(FPS)
    game_speed = float(dt)/64

    scene_id = handle_events(scene_id, player, level1_background, current_menu)
    #player.print_rect_loc()

    if scene_id == 0:
        title_menu.display(screen)
    if scene_id == 1:

        level1_background.stats = player.stats

        level1_background.behave(game_speed)
        player.behave(game_speed, dt)
        if player.current_attack != None:
            player.current_attack.behave(dt)

        background_sprite_group.draw(screen)
        ally_sprite_group.draw(screen)
        player_attack_group.draw(screen)

        #level1_background.print_rect_loc()
        stats_display = stats_font.render(player.stats_str(), False, (0,0,0))
        screen.blit(stats_display, (0,0))

        print(player_attack_group)



    pygame.display.update()
