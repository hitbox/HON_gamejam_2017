import pygame
from assets import *
from values import *

class Player(pygame.sprite.Sprite):
    """
    class: controllable player object
    parameters: array front_frames, array back_frames, array left_frames, array
                right_frames, int speed, int init_x, int init_y, int ani_time
    front_frames: array of paths to images
    back_frames: array of paths to images
    right_frames: array of paths to images
    left_frames: array of paths to images
    speed: value representing the initial speed of the player
    init_x: initial x value of the spawning location of the player
    init_y: initial y value of the spawning location of the player
    ani_time: time between frames in the animation
    """

    def __init__(self, front_frames, back_frames, right_frames, left_frames,
                 stats, init_x, init_y, ani_time):
        super().__init__()
        self.stats = stats
        self.health = self.stats['health']
        self.speed = self.stats['speed']
        self.damage = self.stats['damage']
        self.exp = self.stats['exp']

        self.front_frames = front_frames
        self.back_frames = back_frames
        self.right_frames = right_frames
        self.left_frames = left_frames
        self.current_frame_set = front_frames
        self.prev_frame_set = self.current_frame_set

        self.x_change = 0
        self.y_change = 0

        self.frame_idx = 0
        self.current_frame = self.current_frame_set[0]
        self.image = pygame.image.load(self.current_frame)
        self.ani_time = ani_time
        self.current_ani_time = ani_time

        self.rect = self.image.get_rect()
        self.rect.x = init_x
        self.rect.y = init_y

        self.current_attack = None

    def animate(self, dt):
        """
        Animates the sprite by changing the displayed image.

        :param dt: time between cyclesin the main loop
        """
        if self.current_ani_time >= self.ani_time:
            self.frame_idx = (self.frame_idx + 1) % len(self.current_frame_set)
            self.current_frame = self.current_frame_set[self.frame_idx]
            self.current_ani_time = 0
            self.image = pygame.image.load(self.current_frame)
        else:
            self.current_ani_time += dt

    def update(self, game_speed, dt):
        """
        function: updates the location of the player
        parameters: float game_speed
        game_speed: base speed for all entities in the game
        """
        self.rect.x += self.x_change * game_speed
        self.rect.y += self.y_change * game_speed
        self.animate(dt)
        if not player_attack_group.sprites:
            self.current_attack = None

    def accelerate(self, direction):
        """
        Sets the x_change and y_change to + or - the players speed attribute.

        parameters: int direction
        direction: 0 to 3 value representing the for cardinal directions
        """
        if direction == 0:
            self.y_change = -self.speed
        elif direction == 1:
            self.y_change = self.speed * 1.5
        elif direction == 2:
            self.x_change = -self.speed
        elif direction == 3:
            self.x_change = self.speed * 1.5

    def assign_frame_set(self, direction):
        if direction == 0:
            self.current_frame_set = self.back_frames
        elif direction == 1:
            self.current_frame_set = self.front_frames
        elif direction == 2:
            self.current_frame_set = self.left_frames
        elif direction == 3:
            self.current_frame_set = self.right_frames

        if self.prev_frame_set != self.current_frame_set:
            frame_idx = 0;
            self.current_frame = self.current_frame_set[frame_idx]
            self.image = pygame.image.load(self.current_frame)

        self.prev_frame_set = self.current_frame_set

    def deccelerate(self, direction):
        """
        function: sets x_change or y_change to 0
        parameters: int direction
        direction: 0 to 3 value representing the for cardinal directions
        """
        if direction == 0:
            self.y_change = 0
        elif direction == 1:
            self.y_change = 0
        elif direction == 2:
            self.x_change = 0
        elif direction == 3:
            self.x_change = 0

    def update_stats(self, dhealth, dspeed, ddamage, dexp):
        """
        function: changes stats
        parameters: int dhealth, int dspeed, int ddamage, int dexp
        dhealth: desired change in health
        dspeed: desired change in speed
        ddamage: desired change in damage
        dexp: desired change in experience
        """
        self.health += dhealth
        self.speed += dspeed
        self.damage += ddamage
        self.exp += dexp

        self.stats['health'] = self.health
        self.stats['speed'] = self.speed
        self.stats['damage'] = self.damage
        self.stats['exp'] = self.exp

    def update_health(self, d):
        """
        function: changes the health stat
        parameters: int d
        d: amount to change the stat by
        """
        self.update_stats(d, 0, 0, 0)

    def update_speed(self, d):
        """
        function: changes the speed stat
        parameters: int d
        d: amount to change the stat by
        """
        self.update_stats(0, d, 0, 0)

    def update_damage(self, d):
        """
        function: changes the damage stat
        parameters: int d
        d: amount to change the stat by
        """
        self.update_stats(0, 0, d, 0)

    def update_exp(self, d):
        """
        function: changes the experience stat
        parameters: int d
        d: amount to change the stat by
        """
        self.update_stats(0, 0, 0, d)


    def stats_str(self):
        return ("Health: " + str(self.health)
         + "|Speed: " + str(self.speed)
         + "|Damage: " + str(self.damage)
         + "|Experience: " + str(self.exp))

    def attack(self, direction):
        if self.current_attack == None:
            if direction == 0:
                self.current_attack = PlayerAttack(player_attack_back_frames,
                                                   self.stats['damage'],
                                                   self.rect.x, self.rect.y -
                                                   20, PLAYER_ATTACK_TIME)
                player_attack_group.add(self.current_attack)
            elif direction == 1:
                self.current_attack = PlayerAttack(player_attack_front_frames,
                                                   self.stats['damage'],
                                                   self.rect.x, self.rect.y +
                                                   30, PLAYER_ATTACK_TIME)
                player_attack_group.add(self.current_attack)
            elif direction == 2:
                self.current_attack = PlayerAttack(player_attack_right_frames,
                                                   self.stats['damage'],
                                                   self.rect.x + 20,
                                                   self.rect.y,
                                                   PLAYER_ATTACK_TIME)
                player_attack_group.add(self.current_attack)
            elif direction == 3:
                self.current_attack = PlayerAttack(player_attack_left_frames,
                                                   self.stats['damage'],
                                                   self.rect.x - 20,
                                                   self.rect.y,
                                                   PLAYER_ATTACK_TIME)
                player_attack_group.add(self.current_attack)

class GameBackground(pygame.sprite.Sprite):
    """
    class: game background instance
    parameters: String image, tuple loc
    image: path to the image location
    loc: x,y coordinate location for the image to be displayed on the screen
    """

    def __init__(self, image, stats, init_x, init_y):
        super().__init__()
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.x = init_x
        self.rect.y = init_y
        self.x_change = 0
        self.y_change = 0
        self.stats = stats

    def update(self, game_speed):
        """
        Updates the location of the player.

        parameters: float game_speed
        game_speed: base speed for all entities in the game
        """
        self.rect.x += self.x_change * game_speed
        self.rect.y += self.y_change * game_speed

        if self.rect.x > 350:
            self.rect.x = 350
        if self.rect.x < -1550:
            self.rect.x = -1550
        if self.rect.y > 255:
            self.rect.y = 255
        if self.rect.y < -1645:
            self.rect.y = -1645

    def accelerate(self, direction):
        """
        Sets the x_change and y_change to + or - the players speed attribute.

        parameters: int direction
        direction: 0 to 3 value representing the for cardinal directions
        """
        if direction == 0:
            self.y_change = -self.stats['speed']
        if direction == 1:
            self.y_change = self.stats['speed']
        if direction == 2:
            self.x_change = -self.stats['speed']
        if direction == 3:
            self.x_change = self.stats['speed']

    def deccelerate(self, direction):
        """
        Sets x_change or y_change to 0.
        parameters: int direction
        direction: 0 to 3 value representing the for cardinal directions
        """
        if direction == 0:
            self.y_change = 0
        if direction == 1:
            self.y_change = 0
        if direction == 2:
            self.x_change = 0
        if direction == 3:
            self.x_change = 0


class PlayerAttack(pygame.sprite.Sprite):

    def __init__(self, frames, damage, init_x, init_y, ani_time):
        super().__init__()
        self.frames = frames
        self.damage = damage
        self.current_frame = frames[0]
        self.image = pygame.image.load(self.current_frame)
        self.rect = self.image.get_rect()
        self.rect.x = init_x
        self.rect.y = init_y
        self.ani_time = ani_time
        self.frame_idx = 0
        self.current_ani_time = 0

    def update(self, dt):
        if self.current_ani_time >= self.ani_time:
            self.frame_idx += 1
            if self.frame_idx == len(self.frames):
                self.frame_idx -= 1
                self.kill()
            self.current_frame = self.frames[self.frame_idx]
            self.current_ani_time = 0
            self.image = pygame.image.load(self.current_frame)
        else:
            self.current_ani_time += dt
