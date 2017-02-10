import pygame
from pygame.locals import *

#fuction: looks for input events and calls appropriate functions
#parameters: int scene_id, Player player
#scene_id: value representing where in the game the player is example: a menu or a game level
#player: represents an instance of the player class
#title_menu: title menu to use buttons from
def handle_events(scene_id, player, menu):

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
                    player.accelerate(0)
                if event.key == K_s:
                    player.accelerate(1)
                if event.key == K_a:
                    player.accelerate(2)
                if event.key == K_d:
                    player.accelerate(3)

            if event.type == KEYUP:
                if event.key == K_w:
                    player.deccelerate(0)
                if event.key == K_s:
                    player.deccelerate(1)
                if event.key == K_a:
                    player.deccelerate(2)
                if event.key == K_d:
                    player.deccelerate(3)

    if result < 0:
        result = 0
    return result
