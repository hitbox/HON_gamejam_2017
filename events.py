import pygame

from decor import Decor
from values import *
from assets import *

def handle_events(scene_id, player, background, menu):
    """
    fuction: looks for input events and calls appropriate functions
    parameters: int scene_id, Player player
    scene_id: value representing where in the game the player is example: a menu or a game level
    player: represents an instance of the player class
    title_menu: title menu to use buttons from
    """
    strike_sound = pygame.mixer.Sound(strike_sound_path)
    player_death_sound = pygame.mixer.Sound(player_death_sound_path)

    result = scene_id
    end = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

        if scene_id == 0:
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    for c, b in zip(menu.clickables, menu.buttons):
                        if c.collidepoint(pygame.mouse.get_pos()):
                            result = b.activate(player, background)

        elif scene_id == 1:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    player.assign_frame_set(0)
                    background.accelerate(1)
                elif event.key == pygame.K_s:
                    player.assign_frame_set(1)
                    background.accelerate(0)
                elif event.key == pygame.K_a:
                    player.assign_frame_set(2)
                    background.accelerate(3)
                elif event.key == pygame.K_d:
                    player.assign_frame_set(3)
                    background.accelerate(2)
                elif event.key == pygame.K_UP:
                    strike_sound.play()
                    player.attack(0)
                elif event.key == pygame.K_DOWN:
                    strike_sound.play()
                    player.attack(1)
                elif event.key == pygame.K_RIGHT:
                    strike_sound.play()
                    player.attack(2)
                elif event.key == pygame.K_LEFT:
                    strike_sound.play()
                    player.attack(3)
                elif event.key == pygame.K_SPACE:
                    if not end:
                        player_death_sound.play()
                        decor = Decor(player_death_frames,
                                      player_death_final_img, player.rect.x,
                                      player.rect.y - 90, 350)
                        decors.append(decor)
                        decor_sprite_group.add(decor)
                        player.death_spawned = True
                    end = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    background.deccelerate(1)
                elif event.key == pygame.K_s:
                    background.deccelerate(0)
                elif event.key == pygame.K_a:
                    background.deccelerate(3)
                elif event.key == pygame.K_d:
                    background.deccelerate(2)

    if result < 0:
        result = 0
    return result, end
