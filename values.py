import pygame

debug = False
SCREEN_SIZE = (800, 600)
LEVEL1_SIZE = (2000,2000)
FPS = 60
score = 0
final_score = 0

PLAYER_ATTACK_TIME = 80
PLAYER_SPEED_INIT = 7

current_menu = None

END_GAME_TIME = 2800

enemies = []

INIT_PLAYER_STATS = {
    'health' : 10,
    'speed' : 5,
    'damage' : 1,
    'exp' : 0,
    'level' : 0
}

INIT_SLIME_STATS = {
    'health' : 5,
    'speed' : 2.5,
    'damage' : 2,
    'drop' : 1,
    'attack_time' : 0
}

INIT_SKULL_STATS = {
    'health' : 3,
    'speed' : 0,
    'damage' : 2,
    'drop' : 3,
    'attack_time' : 3500
}

INIT_TAR_STATS = {
    'health' : 6,
    'speed' : 6,
    'damage' : 1,
    'drop' : 0,
    'attack_time' : 0
}

ally_sprite_group = pygame.sprite.Group()
background_sprite_group = pygame.sprite.Group()
player_attack_group = pygame.sprite.Group()
enemy_sprite_group = pygame.sprite.Group()
pickup_sprite_group = pygame.sprite.Group()
decor_sprite_group = pygame.sprite.Group()
