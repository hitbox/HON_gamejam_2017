import random

from assets import *
from enemy_sprites import Enemy
from events import *
from pickups import Pickup
from player_sprites import *
from scene import *
from values import *

def new_game_init(player, background):
    background.rect.x = -500
    background.rect.y = -500
    score = 0

    player.stats['health'] = INIT_PLAYER_STATS['health']
    player.stats['level'] = INIT_PLAYER_STATS['level']
    player.stats['exp'] = INIT_PLAYER_STATS['exp']
    player.stats['damage'] = INIT_PLAYER_STATS['damage']

    player.death_spawned = False
    player.invincible = False

    for i in range(15):
        enemy = Enemy(skull_frames, skull_damage_frames, skull_death_frames,
                      INIT_SKULL_STATS, random.randint(-350,1350),
                      random.randint(-350,1350), 300, 0)
        enemies.append(enemy)
        enemy_sprite_group.add(enemy)

    for i in range(30):
        enemy = Enemy(slime_frames, slime_damage_frames, slime_death_frames,
                      INIT_SLIME_STATS, random.randint(-350,1350),
                      random.randint(-350,1350), 300, 1)
        enemies.append(enemy)
        enemy_sprite_group.add(enemy)

    for i in range(50):
        pickup = Pickup(exp_frames, random.randint(-350,1350),
                        random.randint(-350,1350), 300)
        pickup_sprite_group.add(pickup)

def game_end():
    enemies.clear()

    player_attack_group.empty()
    enemy_sprite_group.empty()
    pickup_sprite_group.empty()
    decor_sprite_group.empty()
