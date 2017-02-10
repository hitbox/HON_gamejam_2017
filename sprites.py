import pygame

#class: controllable player object
#parameters: String image, int speed, int init_x, int init_y, int ani_time
#frames: array of paths to images
#speed: value representing the initial speed of the player
#init_x: initial x value of the spawning location of the player
#init_y: initial y value of the spawning location of the player
#ani_time: time between frames in the animation
class Player(pygame.sprite.Sprite):
    def __init__(self, frames, speed, init_x, init_y, ani_time):
        super().__init__()

        self.speed = speed
        self.frames = frames


        self.x_change = 0
        self.y_change = 0

        self.frame_idx = 0
        self.current_frame = frames[0]
        self.image = pygame.image.load(self.current_frame)
        self.ani_time = ani_time
        self.current_ani_time = ani_time

        self.rect = self.image.get_rect()
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.rect.x = init_x
        self.rect.y = init_y

#function: animates the sprite by changing the displayed image
#parameters: float dt
#dt: time between cyclesin the main loop
    def animate(self, dt):
        if self.current_ani_time >= self.ani_time:

            self.frame_idx += 1
            if self.frame_idx >= len(self.frames):
                self.frame_idx = 0

            self.current_ani_time = 0

            self.image = pygame.image.load(self.frames[self.frame_idx])
        else:
            self.current_ani_time += dt


#function: updates the location of the player
#parameters: float game_speed
#game_speed: base speed for all entities in the game
    def behave(self, game_speed, dt):
        self.rect.x += self.x_change * game_speed
        self.rect.y += self.y_change * game_speed

        self.animate(dt)

#function: sets the x_change and y_change to + or - the players speed attribute
#parameters: int direction
#direction: 0 to 3 value representing the for cardinal directions
    def accelerate(self, direction):
        if direction == 0:
            self.y_change = -self.speed
        if direction == 1:
            self.y_change = self.speed
        if direction == 2:
            self.x_change = -self.speed
        if direction == 3:
            self.x_change = self.speed

#function: sets x_change or y_change to 0
#parameters: int direction
#direction: 0 to 3 value representing the for cardinal directions
    def deccelerate(self, direction):
        if direction == 0:
            self.y_change = 0
        if direction == 1:
            self.y_change = 0
        if direction == 2:
            self.x_change = 0
        if direction == 3:
            self.x_change = 0

#function: prints the location of the player rect attribute
    def print_rect_loc(self):
        print('Rect x: ' + str(self.rect.x) + ' Rect y: ' + str(self.rect.y))
