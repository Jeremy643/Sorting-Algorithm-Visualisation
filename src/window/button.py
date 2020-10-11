import pygame
from .constants import *


class Button:
    """
    The button is to allow the user certain amount of control over the sorting process.

    Attributes:
    win (Surface): The surface to which the button is displayed on.
    x (int): The position of the button along the width of the window.
    y (int): The position of the button along the height of the window.
    name (string): The name of the button.
    btn_outline (tuple): The colour of the outline of the button as an rgb value.
    on (boolean): The button can either be on and clickable or off and not clickable.
    """

    def __init__(self, win, x, y, name):
        self.win = win
        self.x = x
        self.y = y
        self.name = name
        self._init()
    
    def _init(self):
        self.btn_outline = BLACK
        if self.name == TYPE_SORT:
            self.on = False
        else:
            self.on = True
    
    def draw(self):
        """
        Display the buttons on the control panel.
        """

        if self.on:
            self.colour = GRAY
            self.txt_colour = BLACK
        else:
            self.colour = DARKER_GRAY
            self.txt_colour = WHITE

        pygame.draw.rect(self.win, self.colour, (self.x, self.y, BUTTON_WIDTH, BUTTON_HEIGHT))
        pygame.draw.rect(self.win, self.btn_outline, (self.x, self.y, BUTTON_WIDTH, BUTTON_HEIGHT), 2)

        pygame.font.init()
        small_txt = pygame.font.Font('freesansbold.ttf', 22)
        text_surf = small_txt.render(self.name, False, self.txt_colour)

        x_offset = (BUTTON_WIDTH - text_surf.get_width()) // 2
        y_offset = (BUTTON_HEIGHT - text_surf.get_height()) // 2
        self.win.blit(text_surf, (self.x + x_offset, self.y + y_offset))
    
    def turn_off(self):
        self.on = False
    
    def reset(self):
        """
        Returns the button back to its default setting.

        This involves changing its colour and making it clickable again.
        """

        self._init()
    
    def update(self):
        """
        Keeps the buttons up-to-date with the relevent changes that may have occured.
        """

        self.draw()