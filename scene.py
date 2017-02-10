import pygame
from pygame.locals import *

#class: background image instance
#parameters: tuple loc, String image
#loc: x,y coordinate location for the image to be displayed on the screen
#image: path to the image location
class Scene():
    def __init__(self, loc, image):
        self.loc = loc
        self.image = pygame.image.load(image).convert()

#function: displays images
#parameters: pygame.display screen
#screen: screen to display the image on
    def display(self, screen):
        screen.blit(self.image, self.loc)

#class: button instance
#parameters: tuple loc, String image
#loc: x,y coordinate location for the image to be displayed on the screen
#image: path to the image location
class Button(Scene):
    def __init__(self, loc, image):
        super().__init__(loc, image)

#class: menu instance
#parameters: String image, Button array buttons, tuple loc
#image: path to the image location
#buttons: array of instances of buttons
#loc: x,y coordinate location for the image to be displayed on the screen, displays at top left corner by default
class Menu(Scene):
    def __init__(self, image, buttons, loc=(0,0)):
        super().__init__(loc, image)
        self.buttons = buttons

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

#class: game background instance
#parameters: String image, tuple loc
#image: path to the image location  
#loc: x,y coordinate location for the image to be displayed on the screen
class GameBackground(Scene):
    def __init__(self, image, loc=(0,0)):
        super().__init__(loc, image)
