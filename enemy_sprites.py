import pygame
from assets import *
from values import *
import random as rand

class Enemy(pygame.sprite.Sprite):
    def __init__(self, frames, damage_frames, death_frames, stats, init_x, init_y, ani_time, move_pattern):
        super().__init__()

        self.stats = {
            'health' : stats['health'],
            'speed' : stats['speed'],
            'damage' : stats['damage']
        }


        self.frames = frames
        self.damage_frames = damage_frames
        self.death_frames = death_frames

        self.current_frame_set = self.frames

        self.x_change = 0
        self.y_change = 0

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

        self.move_pattern = move_pattern


    def behave(self, game_speed, dt, background_x_change, background_y_change):

        self.move()

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

    def move(self):
        if self.move_pattern == 1:
            self.x_change = rand.randint(-1, 1)
            self.y_change = rand.randint(-1, 1)

    def animate(self, dt):
        if self.current_ani_time >= self.ani_time:
            if self.died:
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
