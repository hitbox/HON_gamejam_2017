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

clock = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)

pygame.font.init()
stats_font = pygame.font.SysFont('Comic Sans', 30)

#set the current scene
scene_id = 0
current_menu = None



#initialize the player
player = Player(player_front_frames, player_back_frames, player_right_frames, player_left_frames, player_invincible_frames_front,
player_invincible_frames_back, player_invincible_frames_right, player_invincible_frames_left, INIT_PLAYER_STATS, (SCREEN_SIZE[0]/2) - 10, (SCREEN_SIZE[1]/2) - 15, 200)

#initialize title screen
title_screen_buttons = [Button((200, 200),startbutton_img, 1), Button((200, 300), quitbutton_img, -1)]
title_menu = Menu(screen, title_background_img, title_screen_buttons)
current_menu = title_menu
#initialize level 1 background
level1_background = GameBackground(level1_background_img, player.stats, 0, 0)

enemy1 = Enemy(slime_frames, slime_damage_frames, slime_death_frames, INIT_SLIME_STATS, 500, 500, 300, 1)
enemy2 = Enemy(skull_frames, skull_damage_frames, skull_death_frames, INIT_SKULL_STATS, 540, 500, 300, 0)
enemy3 = Enemy(slime_frames, slime_damage_frames, slime_death_frames, INIT_SLIME_STATS, 200, 200, 300, 1)

for i in range(0,20):
    enemies.append(Enemy(skull_frames, skull_damage_frames, skull_death_frames, INIT_SKULL_STATS, 100 + i * 60, 600, 300, 0))
    enemy_sprite_group.add(enemies[-1])

for i in range(0,20):
    pickups.append(Pickup(exp_frames, 100 + i * 60, 150, 300))
    pickup_sprite_group.add(pickups[-1])

#make ally sprite group
enemy_sprite_group.add(enemy1)
enemy_sprite_group.add(enemy2)
enemy_sprite_group.add(enemy3)

background_sprite_group.add(level1_background)
ally_sprite_group.add(player)


while True:
    #print(str(scene_id))
    dt = clock.tick(FPS)
    game_speed = .4

    scene_id = handle_events(scene_id, player, level1_background, current_menu)
    #player.print_rect_loc()

    if scene_id == 0:
        title_menu.display(screen)
    if scene_id == 1:

        score = player.stats['health'] * player.stats['exp']

        level1_background.stats = player.stats

        level1_background.behave(game_speed)
        enemy1.behave(game_speed, dt, level1_background.x_change, level1_background.y_change, player.rect.x, player.rect.y)
        enemy2.behave(game_speed, dt, level1_background.x_change, level1_background.y_change, player.rect.x, player.rect.y)
        enemy3.behave(game_speed, dt, level1_background.x_change, level1_background.y_change, player.rect.x, player.rect.y)
        for e in enemies:
            e.behave(game_speed, dt, level1_background.x_change, level1_background.y_change, player.rect.x, player.rect.y)
        for p in pickups:
            p.behave(game_speed, dt, level1_background.x_change, level1_background.y_change)
        player.behave(game_speed, dt)

        if player.current_attack != None:
            player.current_attack.behave(dt)

        screen.fill((0,0,0))
        background_sprite_group.draw(screen)
        pickup_sprite_group.draw(screen)
        enemy_sprite_group.draw(screen)
        ally_sprite_group.draw(screen)
        player_attack_group.draw(screen)

        #level1_background.print_rect_loc()
        stats_display = stats_font.render(str(player.stats['level']), False, (255,255,255))
        score_display = stats_font.render('Score: ' + str(score), False, (0,0,0))

        screen.blit(pygame.image.load(hud_bar_img), (0,0))
        screen.blit(stats_display, (210,15))
        screen.blit(score_display, (670, 580))
        display_health(player.stats['health'], screen)
        display_exp_bar(player.stats['exp'], screen)

        #print("enemy1 health: " + str(enemy1.stats['health']) + " enemy2 health: " + str(enemy2.stats['health']))
        #collide_dict = pygame.sprite.groupcollide(player_attack_group, enemy_sprite_group, False, False)
        #for key in collide_dict.keys():
        #    print(collide_dict[key])
        #print(player_attack_group)
        #print("Slime: " + str(INIT_SLIME_STATS) + " Skull: " + str(INIT_SKULL_STATS))



    pygame.display.update()
