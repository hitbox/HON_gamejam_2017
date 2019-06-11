import pygame
from pygame.locals import *
from sys import exit
from values import *
from events import *
from assets import *
from player_sprites import *
from enemy_sprites import *
from scene import *
from game_ui import *
from pickups import *
from map_gen import *
from decor import *

user_end = False

clock = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)

pygame.font.init()
stats_font = pygame.font.SysFont('Comic Sans', 30)

#set the current scene
scene_id = 0

current_end_game_time = 0

player = Player(player_front_frames, player_back_frames, player_right_frames,
                player_left_frames, player_invincible_frames_front,
                player_invincible_frames_back, player_invincible_frames_right,
                player_invincible_frames_left, INIT_PLAYER_STATS,
                (SCREEN_SIZE[0]/2) - 10, (SCREEN_SIZE[1]/2) - 15, 200)

#initialize title screen
title_screen_buttons = [
    Button((300, 275),startbutton_img, 1), Button((300, 375), quitbutton_img, -1)
]
title_menu = Menu(screen, title_background_img, title_screen_buttons)

game_over_screen_buttons = [
    Button((300, 275), retrybutton_img, 1), Button((300, 375), quitbutton_img, -1)
]
game_over = Menu(screen, title_background_img, game_over_screen_buttons)
current_menu = title_menu
#initialize level 1 background
level1_background = GameBackground(level1_background_img, player.stats, -1000, -1000)

background_sprite_group.add(level1_background)
ally_sprite_group.add(player)

game_speed = .4
while True:
    dt = clock.tick(FPS)

    scene_id, user_end = handle_events(scene_id, player, level1_background, current_menu)
    if player.death_spawned:
        user_end = True
    stats_display = stats_font.render(str(player.stats['level']), False, (255,255,255))
    score_display = stats_font.render('Score: ' + str(score), False, (0,0,0))
    score_display_white = stats_font.render('Final Score: ' + str(score), False, (255,255,255))
    if scene_id == 0:
        current_menu.display(screen)
        if current_menu == game_over:
            screen.blit(score_display_white, (580, 580))
    elif scene_id == 2:
        game_over.display(screen)

    elif scene_id == 1:
        score = player.stats['health'] * player.stats['exp']
        level1_background.stats = player.stats
        level1_background.update(game_speed)

        enemy_sprite_group.update(game_speed, dt, level1_background.x_change,
                                  level1_background.y_change, player.rect.x,
                                  player.rect.y)
        pickup_sprite_group.update(game_speed, dt, level1_background.x_change,
                                   level1_background.y_change)
        decor_sprite_group.update(game_speed, dt, level1_background.x_change,
                                  level1_background.y_change)
        player.update(game_speed, dt)

        if player.current_attack is not None:
            player.current_attack.update(dt)

        background_sprite_group.draw(screen)
        pickup_sprite_group.draw(screen)
        decor_sprite_group.draw(screen)
        enemy_sprite_group.draw(screen)
        if current_end_game_time == 0:
            ally_sprite_group.draw(screen)
        player_attack_group.draw(screen)

        rect = screen.get_rect()
        subrect = rect.inflate(-200, -200)
        tmp = pygame.Surface(subrect.size)
        tmp.blit(screen.subsurface(subrect), (0, 0))
        pygame.transform.scale(tmp, rect.size, screen)

        screen.blit(hud_bar_img, (0,0))
        screen.blit(stats_display, (210,15))
        screen.blit(score_display, (670, 580))
        display_health(player.stats['health'], screen)
        display_exp_bar(player.stats['exp'], screen)

        if not debug:
            if player.stats['health'] == 0 or user_end:
                if current_end_game_time >= END_GAME_TIME:
                    current_end_game_time = 0
                    user_end = False
                    scene_id = 0
                    game_end()
                    current_menu = game_over
                else:
                    current_end_game_time += dt

    pygame.display.update()
