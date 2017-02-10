import pygame
from pygame.locals import *
from sys import exit
from values import *
from events import *
from assets import *
from sprites import *

clock = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)

#set the current scene
scene = 1

#initialize the player
player = Player(player_img, PLAYER_SPEED_INIT, 100, 100)
ally_sprite_group = pygame.sprite.Group()
ally_sprite_group.add(player)

background = pygame.image.load(background_img).convert()

while True:

    dt = clock.tick(FPS)
    game_speed = float(dt)/64

    handle_events(scene, player)
    player.behave(game_speed)
    player.print_rect_loc()

    screen.blit(background,(0,0))
    ally_sprite_group.draw(screen)


    pygame.display.update()
