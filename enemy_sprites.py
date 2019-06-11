import math
import random

import pygame

from assets import (blob_death_sound_path, exp_frames, plant1_final_img,
                    plant1_spawn_frames, plant2_final_img,
                    skull_damage_sound_path, skull_death_sound_path,
                    slime_damage_sound_path, tar_damage_frames,
                    tar_death_frames, tar_frames)
from decor import Decor
from pickups import Pickup, pickup_sprite_group
from values import (player_attack_group, enemy_sprite_group, INIT_TAR_STATS,
                    enemies, decor_sprite_group)

SKULL_MOVE = 0
SLIME_MOVE = 1

class Enemy(pygame.sprite.Sprite):

    def __init__(self, frames, damage_frames, death_frames, stats, init_x,
                 init_y, ani_time, move_pattern, x_change=0, y_change=0):
        super().__init__()

        self.stats = {
            'health' : stats['health'],
            'speed' : stats['speed'],
            'damage' : stats['damage'],
            'drop' : random.randint(0, stats['drop']),
            'attack_time' : stats['attack_time']
        }
        self.current_attack_time = 0

        self.frames = frames
        self.damage_frames = damage_frames
        self.death_frames = death_frames

        self.current_frame_set = self.frames

        self.x_change = x_change
        self.y_change = y_change

        self.frame_idx = 0
        self.current_frame = self.frames[0]
        self.image = self.current_frame
        self.ani_time = ani_time
        self.current_ani_time = 0

        self.rect = self.image.get_rect(x=init_x, y=init_y)

        self.died = False
        self.dropped = False

        self.move_pattern = move_pattern

        self.skull_damage_sound = pygame.mixer.Sound(skull_damage_sound_path)
        self.slime_damage_sound = pygame.mixer.Sound(slime_damage_sound_path)
        self.blob_death_sound = pygame.mixer.Sound(blob_death_sound_path)
        self.skull_death_sound = pygame.mixer.Sound(skull_death_sound_path)

    def update(self, game_speed, dt, background_x_change, background_y_change,
               player_x, player_y):
        self.move()
        self.attack(dt, player_x, player_y)

        self.rect.x += (background_x_change + self.stats['speed'] * self.x_change) * game_speed
        self.rect.y += (background_y_change + self.stats['speed'] * self.y_change) * game_speed

        if self.stats['health'] <= 0 and not self.died:
            self.frame_idx = 0
            self.current_frame_set = self.death_frames

        collide_dict = pygame.sprite.groupcollide(player_attack_group,
                                                  enemy_sprite_group, False,
                                                  False)
        for key in collide_dict.keys():
            value = collide_dict[key]
            if value[0] == self:
                self.stats['health'] -= key.damage
                key.damage = 0
                if self.move_pattern == SLIME_MOVE:
                    self.slime_damage_sound.play()
                elif self.move_pattern == SKULL_MOVE:
                    self.skull_damage_sound.play()
                self.current_frame_set = self.damage_frames

        self.animate(dt)

    def attack(self, dt, player_x, player_y):
        if self.died:
            return
        if self.move_pattern != SKULL_MOVE:
            return
        dx = self.rect.x - player_x
        dy = self.rect.y - player_y
        distance = math.hypot(dx, dy)
        if (self.current_attack_time >= self.stats['attack_time']) and distance <= 320:
            self.current_attack_time = 0
            x_mod = 0
            y_mod = 0
            if (player_x - self.rect.x) > 45:
                x_mod = 1
            if (player_x - self.rect.x) < -45:
                x_mod = -1
            if (player_y - self.rect.y) > 45:
                y_mod = 1
            if (player_y - self.rect.y) < -45:
                y_mod = -1
            if x_mod == 0 and y_mod == 0:
                y_mod = 1

            enemy = Enemy(tar_frames, tar_damage_frames,
                          tar_death_frames, INIT_TAR_STATS,
                          self.rect.x, self.rect.y, 300, 2, x_mod,
                          y_mod)
            enemies.append(enemy)
            enemy_sprite_group.add(enemies[-1])
        else:
            self.current_attack_time += dt

    def move(self):
        if self.move_pattern == SLIME_MOVE:
            self.x_change = random.choice([-1, 1])
            self.y_change = random.choice([-1, 1])

    def animate(self, dt):
        if self.current_ani_time < self.ani_time:
            self.current_ani_time += dt
            return

        if self.died:
            self.kill()
            if not self.dropped:
                for _ in range(self.stats['drop']):
                    pickup = Pickup(exp_frames,
                                    self.rect.x + random.randint(-10, 10),
                                    self.rect.y + random.randint(-10, 10),
                                    300)
                    pickup_sprite_group.add(pickup)
                plant_type = random.choice([
                    (plant1_spawn_frames, plant1_final_img),
                    (plant1_spawn_frames, plant2_final_img)])
                decor = Decor(*plant_type,
                              self.rect.x + random.randint(-10, 10),
                              self.rect.y + random.randint(-10, 10),
                              300)
                decor_sprite_group.add(decor)
                self.dropped = True

                if self.move_pattern == SLIME_MOVE:
                    self.blob_death_sound.play()
                elif self.move_pattern == SKULL_MOVE:
                    self.skull_death_sound.play()

        self.frame_idx = (self.frame_idx + 1) % len(self.current_frame_set)

        if self.stats['health'] <= 0:
            self.died = True

        self.current_frame = self.current_frame_set[self.frame_idx]
        self.current_ani_time = 0
        self.image = self.current_frame
        if self.current_frame_set != self.frames:
            self.current_frame_set = self.frames
