import pygame
from assets import *
from values import *
import random as rand
from pickups import *
import math

class Enemy(pygame.sprite.Sprite):
    def __init__(self, frames, damage_frames, death_frames, stats, init_x, init_y, ani_time, move_pattern, x_change=0, y_change=0):
        super().__init__()

        self.stats = {
            'health' : stats['health'],
            'speed' : stats['speed'],
            'damage' : stats['damage'],
            'drop' : rand.randint(0, stats['drop']),
            'attack_time' : stats['attack_time']
        }
        self.current_attack_time = 0

        self.frames = frames
        self.damage_frames = damage_frames
        self.death_frames = death_frames

        self.current_frame_set = self.frames

        self.x_change = x_change
        self.y_change = y_change

        self.frame_idx = -1
        self.current_frame = self.frames[0]
        self.image = pygame.image.load(self.current_frame)
        self.ani_time = ani_time
        self.current_ani_time = 0

        self.rect = self.image.get_rect()
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.rect.x = init_x
        self.rect.y = init_y

        self.died = False
        self.dropped = False

        self.move_pattern = move_pattern


    def behave(self, game_speed, dt, background_x_change, background_y_change, player_x, player_y):

        self.move()
        self.attack(dt, player_x, player_y)

        self.rect.x += (background_x_change + self.stats['speed'] * self.x_change) * game_speed
        self.rect.y += (background_y_change + self.stats['speed'] * self.y_change) * game_speed

        if self.stats['health'] <= 0 and not self.died:

            #self.current_ani_time = 0
            self.frame_idx = 0
            self.current_frame_set = self.death_frames
            #self.kill()

        collide_dict = pygame.sprite.groupcollide(player_attack_group, enemy_sprite_group, False, False)
        for key in collide_dict.keys():
            #print(key)
            value = collide_dict[key]
            if value[0] == self:
                self.stats['health'] -= key.damage
                key.damage = 0
                #print("slime took damage")
                self.current_frame_set = self.damage_frames
        #self.rect.x += self.x_change * game_speed
        #self.rect.y += self.y_change * game_speed

        self.animate(dt)

    def attack(self, dt, player_x, player_y):
        if not self.died:
            if self.move_pattern == 0:
                distance = math.sqrt(math.pow(self.rect.x - player_x, 2) + math.pow(self.rect.y - player_y, 2))
                #print(str(distance))
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

                    enemies.append(Enemy(tar_frames, tar_damage_frames, tar_death_frames, INIT_TAR_STATS, self.rect.x, self.rect.y, 300, 2, x_mod, y_mod))
                    enemy_sprite_group.add(enemies[-1])
                else:
                    self.current_attack_time += dt

    def move(self):
        if self.move_pattern == 1:
            self.x_change = rand.randint(-1, 1)
            self.y_change = rand.randint(-1, 1)

    def animate(self, dt):
        if self.current_ani_time >= self.ani_time:
            if self.died:
                if not self.dropped:
                    for _ in range(0, self.stats['drop']):
                        pickups.append(Pickup(exp_frames, self.rect.x + rand.randint(-10, 10), self.rect.y + rand.randint(-10, 10), 300))
                        pickup_sprite_group.add(pickups[-1])
                    self.dropped = True
                self.kill()

            self.frame_idx += 1

            if self.frame_idx >= len(self.current_frame_set):
                self.frame_idx = 0
                if self.stats['health'] <= 0:
                    self.died = True

            self.current_frame = self.current_frame_set[self.frame_idx]
            self.current_ani_time = 0
            self.image = pygame.image.load(self.current_frame)
            if self.current_frame_set != self.frames:
                self.current_frame_set = self.frames

        else:
            self.current_ani_time += dt
