import pygame
from pygame.locals import *

#fuction: looks for input events and calls appropriate functions
#parameters: int scene, Player player
#scene: value representing where in the game the player is example: a menu or a game level
#player: represents an instance of the player class
def handle_events(scene, player):

    for event in pygame.event.get():
        print(event)

        if event.type == QUIT:
            exit()

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
