import pygame
from assets import *
from values import *

class Enemy(pygame.sprite.Sprite):
    def __init__(self, frames, stats, init_x, init_y, ani_time):
        super().__init__()

        self.stats = stats

        self.frames = frames

        self.x_change = 0
        self.y_change = 0

        self.frame_idx = 0
        self.current_frame = self.frames[0]
        self.image = pygame.image.load(self.current_frame)
        self.ani_time = ani_time
        self.current_ani_time = 0

        self.rect = self.image.get_rect()
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.rect.x = init_x
        self.rect.y = init_y

    def behave(self, game_speed, dt, background_x_change, background_y_change):

        self.rect.x += background_x_change * game_speed
        self.rect.y += background_y_change * game_speed

        if self.stats['health'] <= 0:
            self.kill()

        collide_dict = pygame.sprite.groupcollide(player_attack_group, enemy_sprite_group, False, False)
        for value in collide_dict.values():
            if value[0] == self:
                self.stats['health'] -= 1
                print("slime took damage")
        #self.rect.x += self.x_change * game_speed
        #self.rect.y += self.y_change * game_speed

        self.animate(dt)

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
