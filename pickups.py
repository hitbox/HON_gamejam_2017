import pygame

from assets import exp_sound_path
from values import ally_sprite_group, pickup_sprite_group

class Pickup(pygame.sprite.Sprite):

    def __init__(self, frames, init_x, init_y, ani_time):
        super().__init__()
        self.frames = frames

        self.frame_idx = -1
        self.current_frame = self.frames[0]
        self.image = self.current_frame

        self.ani_time = ani_time
        self.current_ani_time = 0

        self.rect = self.image.get_rect()
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.rect.x = init_x
        self.rect.y = init_y

        self.exp_sound = pygame.mixer.Sound(exp_sound_path)

    def animate(self, dt):
        if self.current_ani_time >= self.ani_time:
            self.frame_idx = (self.frame_idx + 1) % len(self.frames)
            self.current_frame = self.frames[self.frame_idx]
            self.current_ani_time = 0
            self.image = self.current_frame
        else:
            self.current_ani_time += dt

    def update(self, game_speed, dt, background_x_change, background_y_change):
        self.rect.x += background_x_change * game_speed
        self.rect.y += background_y_change * game_speed

        collide_dict = pygame.sprite.groupcollide(ally_sprite_group,
                                                  pickup_sprite_group, False,
                                                  False)
        for key in collide_dict.keys():
            value = collide_dict[key]
            if value[0] == self:
                self.exp_sound.play()
                key.update_exp(1)
                self.kill()

        self.animate(dt)
