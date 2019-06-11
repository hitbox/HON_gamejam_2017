import pygame

from assets import (player_attack_back_frames, player_attack_front_frames,
                    player_attack_left_frames, player_attack_right_frames,
                    player_death_final_img, player_death_frames)
from values import (INIT_PLAYER_STATS, PLAYER_ATTACK_TIME, ally_sprite_group,
                    decor_sprite_group, enemy_sprite_group,
                    player_attack_group)
from decor import Decor

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
                 front_invincible_frames, back_invincible_frames,
                 right_invincible_frames, left_invincible_frames, stats,
                 init_x, init_y, ani_time):
        super().__init__()
        self.stats = {
            'health' : stats['health'],
            'speed' : stats['speed'],
            'damage' : stats ['damage'],
            'exp' : stats['exp'],
            'level' : stats['level']
        }

        self.front_frames = front_frames
        self.back_frames = back_frames
        self.right_frames = right_frames
        self.left_frames = left_frames

        self.front_invincible_frames = front_invincible_frames
        self.back_invincible_frames = back_invincible_frames
        self.right_invincible_frames = right_invincible_frames
        self.left_invincible_frames = left_invincible_frames

        self.current_frame_set = front_frames
        self.prev_frame_set = self.current_frame_set

        self.x_change = 0
        self.y_change = 0

        self.frame_idx = 0
        self.current_frame = self.current_frame_set[0]
        self.image = self.current_frame
        self.ani_time = ani_time
        self.current_ani_time = ani_time

        self.rect = self.image.get_rect()

        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.rect.x = init_x
        self.rect.y = init_y

        self.current_attack = None

        self.invincible = False

        self.current_diretion = 1

        self.death_spawned = False


    def animate(self, dt):
        """
        function: animates the sprite by changing the displayed image
        parameters: float dt
        dt: time between cyclesin the main loop
        """
        if self.current_ani_time >= self.ani_time:
            self.frame_idx += 1

            if self.frame_idx >= len(self.current_frame_set):
                self.frame_idx = 0
                if self.current_frame_set != (self.front_frames or
                        self.back_frames or self.right_frames or
                        self.left_frames):
                    self.invincible = False
                    self.assign_frame_set(self.current_diretion)

            self.current_frame = self.current_frame_set[self.frame_idx]
            self.current_ani_time = 0
            self.image = self.current_frame

        else:
            self.current_ani_time += dt


    def update(self, game_speed, dt):
        """
        function: updates the location of the player
        parameters: float game_speed
        game_speed: base speed for all entities in the game
        """

        self.stats['level'] = int(self.stats['exp'] / 20)
        self.stats['damage'] = INIT_PLAYER_STATS['damage'] + 1 * self.stats['level']
        #self.stats['speed'] = INIT_PLAYER_STATS['speed'] + 2 * self.stats['level']

        self.rect.x += self.x_change * game_speed
        self.rect.y += self.y_change * game_speed

        if self.stats['health'] <= 0 and not self.death_spawned:
            self.death_spawned = True
            decor = Decor(player_death_frames, player_death_final_img,
                          self.rect.x, self.rect.y - 90, 350)
            decors.append(decor)
            decor_sprite_group.add(decor)

        collide_dict = pygame.sprite.groupcollide(enemy_sprite_group, ally_sprite_group, False, False)
        for key in collide_dict.keys():
            value = collide_dict[key]
            if value[0] == self and not self.invincible:
                self.update_health(-key.stats['damage'])
                self.invincible = True
                self.frame_idx = 0
                self.assign_frame_set(self.current_diretion)

        self.animate(dt)
        if player_attack_group.sprites() == []:
            self.current_attack = None

    def accelerate(self, direction):
        """
        function: sets the x_change and y_change to + or - the players speed attribute
        parameters: int direction
        direction: 0 to 3 value representing the for cardinal directions
        """
        if direction == 0:
            self.y_change = -self.speed
        elif direction == 1:
            self.y_change = self.speed
        elif direction == 2:
            self.x_change = -self.speed
        elif direction == 3:
            self.x_change = self.speed

    def assign_frame_set(self, direction):
        self.current_diretion = direction
        if direction == 0:
            if self.invincible:
                self.current_frame_set = self.back_invincible_frames
            else:
                self.current_frame_set = self.back_frames
        elif direction == 1:
            if self.invincible:
                self.current_frame_set = self.front_invincible_frames
            else:
                self.current_frame_set = self.front_frames
        elif direction == 2:
            if self.invincible:
                self.current_frame_set = self.left_invincible_frames
            else:
                self.current_frame_set = self.left_frames
        elif direction == 3:
            if self.invincible:
                self.current_frame_set = self.right_invincible_frames
            else:
                self.current_frame_set = self.right_frames

        if self.prev_frame_set != self.current_frame_set:
            frame_idx = 0;
            self.current_frame = self.current_frame_set[frame_idx]
            self.image = self.current_frame

        self.prev_frame_set = self.current_frame_set

    def deccelerate(self, direction):
        """
        function: sets x_change or y_change to 0
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

    def update_stats(self, dhealth, dspeed, ddamage, dexp):
        """
        function: changes stats
        parameters: int dhealth, int dspeed, int ddamage, int dexp
        dhealth: desired change in health
        dspeed: desired change in speed
        ddamage: desired change in damage
        dexp: desired change in experience
        """

        self.stats['health'] += dhealth
        if self.stats['health'] < 0:
            self.stats['health'] = 0
        self.stats['speed'] += dspeed
        self.stats['damage'] += ddamage
        self.stats['exp'] += dexp

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
        self.image = image
        self.rect = self.image.get_rect()
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.rect.x = init_x
        self.rect.y = init_y
        self.x_change = 0
        self.y_change = 0
        self.stats = stats

    def update(self, game_speed):
        """
        function: updates the location of the player
        parameters: float game_speed
        game_speed: base speed for all entities in the game
        """
        if self.rect.x > 350:
            self.rect.x = 350
            self.x_change = 0
            self.y_change = 0
        elif self.rect.x < -1550:
            self.rect.x = -1550
            self.x_change = 0
            self.y_change = 0
        elif self.rect.y > 255:
            self.rect.y = 255
            self.x_change = 0
            self.y_change = 0
        elif self.rect.y < -1645:
            self.rect.y = -1645
            self.x_change = 0
            self.y_change = 0
        else:
            self.rect.x += self.x_change * game_speed
            self.rect.y += self.y_change * game_speed

    def accelerate(self, direction):
        """
        function: sets the x_change and y_change to + or - the players speed attribute
        parameters: int direction
        direction: 0 to 3 value representing the for cardinal directions
        """
        if direction == 0:
            self.y_change = -self.stats['speed']
        elif direction == 1:
            self.y_change = self.stats['speed']
        elif direction == 2:
            self.x_change = -self.stats['speed']
        elif direction == 3:
            self.x_change = self.stats['speed']

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


class PlayerAttack(pygame.sprite.Sprite):

    def __init__(self, frames, damage, init_x, init_y, ani_time):
        super().__init__()
        self.frames = frames
        self.damage = damage
        self.current_frame = frames[0]
        self.image = self.current_frame
        self.rect = self.image.get_rect()
        self.rect.x = init_x
        self.rect.y = init_y
        self.ani_time = ani_time
        self.frame_idx = 0
        self.current_ani_time = 0
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def update(self, dt):
        if self.current_ani_time >= self.ani_time:
            self.frame_idx += 1

            if self.frame_idx >= len(self.frames):
                self.frame_idx -= 1
                self.kill()

            self.current_frame = self.frames[self.frame_idx]
            self.current_ani_time = 0
            self.image = self.current_frame

        else:
            self.current_ani_time += dt
