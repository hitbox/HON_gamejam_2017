import pygame

class Decor(pygame.sprite.Sprite):

    def __init__(self, spawn_frames, image, init_x, init_y, ani_time):
        super().__init__()

        self.spawn_frames = spawn_frames
        self.frame_idx = 0
        self.current_frame = self.spawn_frames[self.frame_idx]
        self.image = self.current_frame
        self.ani_time = ani_time
        self.current_ani_time = 0
        self.spawning = True

        self.final_image = image

        self.rect = self.image.get_rect()
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.rect.x = init_x
        self.rect.y = init_y

    def update(self, game_speed, dt, background_x_change, background_y_change):
        self.rect.x += background_x_change * game_speed
        self.rect.y += background_y_change * game_speed
        if self.spawning:
            self.spawn(dt)

    def spawn(self, dt):
        if self.current_ani_time >= self.ani_time:

            self.frame_idx += 1

            if self.frame_idx >= len(self.spawn_frames):
                self.spawning = False
                self.image = self.final_image


            self.current_ani_time = 0
            if self.spawning:
                self.current_frame = self.spawn_frames[self.frame_idx]
                self.image = self.current_frame

        else:
            self.current_ani_time += dt
