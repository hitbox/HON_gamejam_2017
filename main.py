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


player = Player(player_front_frames, player_back_frames, player_right_frames, player_left_frames, player_invincible_frames_front,
player_invincible_frames_back, player_invincible_frames_right, player_invincible_frames_left, INIT_PLAYER_STATS, (SCREEN_SIZE[0]/2) - 10, (SCREEN_SIZE[1]/2) - 15, 200)


#initialize the player


#initialize title screen
title_screen_buttons = [Button((300, 275),startbutton_img, 1), Button((300, 375), quitbutton_img, -1)]
title_menu = Menu(screen, title_background_img, title_screen_buttons)

game_over_screen_buttons = [Button((300, 275), retrybutton_img, 1), Button((300, 375), quitbutton_img, -1)]
game_over = Menu(screen, title_background_img, game_over_screen_buttons)
current_menu = title_menu
#initialize level 1 background
level1_background = GameBackground(level1_background_img, player.stats, -1000, -1000)

background_sprite_group.add(level1_background)
ally_sprite_group.add(player)






#print(str(all_assets))




while True:
    #print(str(scene_id))
    dt = clock.tick(FPS)
    game_speed = .4

    scene_id, user_end = handle_events(scene_id, player, level1_background, current_menu)
    #player.print_rect_loc()

    stats_display = stats_font.render(str(player.stats['level']), False, (255,255,255))
    score_display = stats_font.render('Score: ' + str(score), False, (0,0,0))
    score_display_white = stats_font.render('Final Score: ' + str(score), False, (255,255,255))
    #print('\nenemies: ' + str(enemies))
    #print(str(user_end))
    if scene_id == 0:
        current_menu.display(screen)

        if current_menu == game_over:
            screen.blit(score_display_white, (580, 580))
    if scene_id == 2:
        game_over.display(screen)

    if scene_id == 1:

        score = player.stats['health'] * player.stats['exp']

        level1_background.stats = player.stats

        level1_background.behave(game_speed)
        #enemy1.behave(game_speed, dt, level1_background.x_change, level1_background.y_change, player.rect.x, player.rect.y)
        #enemy2.behave(game_speed, dt, level1_background.x_change, level1_background.y_change, player.rect.x, player.rect.y)
        #enemy3.behave(game_speed, dt, level1_background.x_change, level1_background.y_change, player.rect.x, player.rect.y)
        for e in enemies:
            e.behave(game_speed, dt, level1_background.x_change, level1_background.y_change, player.rect.x, player.rect.y)
        for p in pickups:
            p.behave(game_speed, dt, level1_background.x_change, level1_background.y_change)
        for d in decors:
            d.behave(game_speed, dt, level1_background.x_change, level1_background.y_change)
        player.behave(game_speed, dt)

        if player.current_attack != None:
            player.current_attack.behave(dt)

        screen.fill((0,0,0))
        background_sprite_group.draw(screen)
        pickup_sprite_group.draw(screen)
        decor_sprite_group.draw(screen)
        enemy_sprite_group.draw(screen)
        ally_sprite_group.draw(screen)
        player_attack_group.draw(screen)

        #level1_background.print_rect_loc()


        screen.blit(pygame.image.load(hud_bar_img), (0,0))
        screen.blit(stats_display, (210,15))
        screen.blit(score_display, (670, 580))
        display_health(player.stats['health'], screen)
        display_exp_bar(player.stats['exp'], screen)

        if debug == False:
            #for e in pygame.event.get():
            #    if e.type == KEYDOWN:
            #        if e.key == K_SPACE:
            #            user_end = True
            if player.stats['health'] == 0 or user_end:
                user_end = False
                scene_id = 0
                game_end()
                current_menu = game_over

        #print("enemy1 health: " + str(enemy1.stats['health']) + " enemy2 health: " + str(enemy2.stats['health']))
        #collide_dict = pygame.sprite.groupcollide(player_attack_group, enemy_sprite_group, False, False)
        #for key in collide_dict.keys():
        #    print(collide_dict[key])
        #print(player_attack_group)
        #print("Slime: " + str(INIT_SLIME_STATS) + " Skull: " + str(INIT_SKULL_STATS))



    pygame.display.update()
