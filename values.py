import pygame

SCREEN_SIZE = (800, 600)
LEVEL1_SIZE = (2000,2000)
FPS = 60

PLAYER_SPEED_INIT = 7

INIT_PLAYER_STATS = {
    'health' : 10,
    'speed' : 5,
    'damage' : 1,
    'exp' : 0
}

INIT_SLIME_STATS = {
    'health' : 5,
    'speed' : 2.5,
    'damage' : 1
}

INIT_SKULL_STATS = {
    'health' : 3,
    'speed' : 0,
    'damage' : 1
}

PLAYER_ATTACK_TIME = 80

ally_sprite_group = pygame.sprite.Group()
background_sprite_group = pygame.sprite.Group()
player_attack_group = pygame.sprite.Group()
enemy_sprite_group = pygame.sprite.Group()
