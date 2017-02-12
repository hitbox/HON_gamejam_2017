import pygame
from pygame.locals import *
from map_gen import *

#class: background image instance
#parameters: tuple loc, String image
#loc: x,y coordinate location for the image to be displayed on the screen
#image: path to the image location
class Scene():
    def __init__(self, loc, image):
        self.loc = loc
        self.image = pygame.image.load(image).convert_alpha()

#function: displays images
#parameters: pygame.display screen
#screen: screen to display the image on
    def display(self, screen):
        screen.blit(self.image, self.loc)

#class: button instance
#parameters: tuple loc, String image
#loc: x,y coordinate location for the image to be displayed on the screen
#image: path to the image location
#function: integer number representing the function of the buttton see "activat" below
class Button(Scene):
    def __init__(self, loc, image, function):
        super().__init__(loc, image)
        self.function = function

#function: displays images and returns pygame rect objects
#parameters: pygame.display screen
#screen: screen to display the image on
    def display(self, screen):
        return screen.blit(self.image, self.loc)

#function: performs a button function
    def activate(self, player, background):
        if self.function == -1:
            exit()
        elif self.function == 1:
            new_game_init(player, background)
            return 1
        else:
            return 0

#class: menu instance
#parameters: String image, Button array buttons, tuple loc
#screen: pygame surface to set the clickables on
#image: path to the image location
#buttons: array of instances of buttons
#loc: x,y coordinate location for the image to be displayed on the screen, displays at top left corner by default
class Menu(Scene):
    def __init__(self, screen, image, buttons, loc=(0,0)):
        super().__init__(loc, image)

        self.buttons = buttons
        self.clickables = []
        self.set_clickables(screen)

#function: displays images
#parameters: pygame.display screen
#screen: screen to display the image on
    def display(self, screen):
        screen.blit(self.image, self.loc)
        self.display_buttons(screen)

#function: displays buttons
#parameters: pygame.display screen
#screen: screen to display the image on
    def display_buttons(self, screen):
        for b in self.buttons:
            b.display(screen)

#function: creates an array of clickable rects
#parameters: pygame.display screen
#screen: screen to display the images on
    def set_clickables(self, screen):
        for b in self.buttons:
            self.clickables.append(b.display(screen))
