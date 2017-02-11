import pygame
from pygame.locals import *

#fuction: looks for input events and calls appropriate functions
#parameters: int scene_id, Player player
#scene_id: value representing where in the game the player is example: a menu or a game level
#player: represents an instance of the player class
#title_menu: title menu to use buttons from
def handle_events(scene_id, player, background, menu):

    result = scene_id

    for event in pygame.event.get():
        #print(event)

        if event.type == QUIT:
            exit()

        if scene_id == 0:
            if event.type == MOUSEBUTTONUP:
                if event.button == 1:
                    for c,b in zip(menu.clickables, menu.buttons):
                        if c.collidepoint(pygame.mouse.get_pos()):
                            result = b.activate()

        if scene_id == 1:
            if event.type == KEYDOWN:
                if event.key == K_w:
                    player.assign_frame_set(0)
                    background.accelerate(1)
                if event.key == K_s:
                    player.assign_frame_set(1)
                    background.accelerate(0)
                if event.key == K_a:
                    player.assign_frame_set(2)
                    background.accelerate(3)
                if event.key == K_d:
                    player.assign_frame_set(3)
                    background.accelerate(2)
                    
                if event.key == K_UP:
                    player.attack(0)
                if event.key == K_DOWN:
                    player.attack(1)
                if event.key == K_RIGHT:
                    player.attack(2)
                if event.key == K_LEFT:
                    player.attack(3)

            if event.type == KEYUP:
                if event.key == K_w:
                    background.deccelerate(1)
                if event.key == K_s:
                    background.deccelerate(0)
                if event.key == K_a:
                    background.deccelerate(3)
                if event.key == K_d:
                    background.deccelerate(2)

    if result < 0:
        result = 0
    return result
