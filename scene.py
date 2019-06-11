import pygame

from map_gen import new_game_init

class Scene():
    """
    class: background image instance
    parameters: tuple loc, String image
    loc: x,y coordinate location for the image to be displayed on the screen
    image: path to the image location
    """
    def __init__(self, loc, image):
        self.loc = loc
        self.image = image

    def display(self, screen):
        """
        function: displays images
        parameters: pygame.display screen
        screen: screen to display the image on
        """
        screen.blit(self.image, self.loc)


class Button(Scene):
    """
    class: button instance
    parameters: tuple loc, String image
    loc: x,y coordinate location for the image to be displayed on the screen
    image: path to the image location
    function: integer number representing the function of the buttton see "activat" below
    """

    def __init__(self, loc, image, function):
        super().__init__(loc, image)
        self.function = function

    def display(self, screen):
        """
        function: displays images and returns pygame rect objects
        parameters: pygame.display screen
        screen: screen to display the image on
        """
        return screen.blit(self.image, self.loc)

    def activate(self, player, background):
        """
        function: performs a button function
        """
        if self.function == -1:
            exit()
        elif self.function == 1:
            new_game_init(player, background)
            return 1
        else:
            return 0

class Menu(Scene):
    """
    class: menu instance
    parameters: String image, Button array buttons, tuple loc
    screen: pygame surface to set the clickables on
    image: path to the image location
    buttons: array of instances of buttons
    loc: x,y coordinate location for the image to be displayed on the screen,
         displays at top left corner by default
    """

    def __init__(self, screen, image, buttons, loc=(0,0)):
        super().__init__(loc, image)

        self.buttons = buttons
        self.clickables = []
        self.set_clickables(screen)

    def display(self, screen):
        """
        function: displays images
        parameters: pygame.display screen
        screen: screen to display the image on
        """
        screen.blit(self.image, self.loc)
        self.display_buttons(screen)

    def display_buttons(self, screen):
        """
        function: displays buttons
        parameters: pygame.display screen
        screen: screen to display the image on
        """
        for b in self.buttons:
            b.display(screen)

    def set_clickables(self, screen):
        """
        function: creates an array of clickable rects
        parameters: pygame.display screen
        screen: screen to display the images on
        """
        for b in self.buttons:
            self.clickables.append(b.display(screen))
