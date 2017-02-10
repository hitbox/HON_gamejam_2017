import pygame

#class: controllable player object
#parameters: String image, int speed, int init_x, int init_y
#image: the path to the image
#speed: value representing the initial speed of the player
#init_x: initial x value of the spawning location of the player
#init_y: initial y value of the spawning location of the player
class Player(pygame.sprite.Sprite):
    def __init__(self, image, speed, init_x, init_y):
        super().__init__()

        self.speed = speed
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.rect.x = init_x
        self.rect.y = init_y
        self.x_change = 0
        self.y_change = 0

#function: updates the location of the player
#parameters: float game_speed
#game_speed: base speed for all entities in the game
    def behave(self, game_speed):
        self.rect.x += self.x_change * game_speed
        self.rect.y += self.y_change * game_speed

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
