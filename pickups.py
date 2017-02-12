import pygame
from assets import *
from values import *
import random as rand

class Pickup(pygame.sprite.Sprite):
    def __init__(self, frames, init_x, init_y, ani_time):
        super().__init__()
        self.frames = frames

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

    def animate(self, dt):
        if self.current_ani_time >= self.ani_time:

            self.frame_idx += 1

            if self.frame_idx >= len(self.frames):
                self.frame_idx = 0

            self.current_frame = self.frames[self.frame_idx]
            self.current_ani_time = 0
            self.image = pygame.image.load(self.current_frame)

        else:
            self.current_ani_time += dt

    def behave(self, game_speed, dt, background_x_change, background_y_change):

        self.rect.x += background_x_change * game_speed
        self.rect.y += background_y_change * game_speed

        collide_dict = pygame.sprite.groupcollide(ally_sprite_group, pickup_sprite_group, False, False)
        for key in collide_dict.keys():
            #print(key)
            value = collide_dict[key]
            if value[0] == self:
                key.update_exp(1)
                self.kill()
        #self.rect.x += self.x_change * game_speed
        #self.rect.y += self.y_change * game_speed

        self.animate(dt)
