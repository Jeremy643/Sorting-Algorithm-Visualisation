import pygame
from .button import Button
from .constants import *
from random import randint


class Control:
    """
    The control represents the panel that allows the user to make certain decisions about the sorting process.

    Attributes:
    win (Surface): The surface to which we will be displaying data to.
    gen_btn (Button): The button that generates random data to be sorted.
    sort_btn (Button): The button that initiates the sort of the generated data.
    reset_btn (Button): The button that resets the graph and control panel back to the default setting.
    buttons (List): A list of all of the buttons on the control panel.
    selected_btn (Button): Holds the button that the user selected.
    generated (boolean): Tells us if we have generated data to be sorted.
    """

    def __init__(self, win):
        self.win = win
        self.gen_btn = Button(self.win, GEN_BTN_X, GEN_BTN_Y, TYPE_GEN)
        self.sort_btn = Button(self.win, SORT_BTN_X, SORT_BTN_Y, TYPE_SORT)
        self.reset_btn = Button(self.win, RESET_BTN_X, RESET_BTN_Y, TYPE_RESET)
        self.buttons = {TYPE_GEN: self.gen_btn, TYPE_SORT: self.sort_btn, TYPE_RESET: self.reset_btn}
        self.selected_btn = None
        self.generated = False

    def get_data(self, number=100):
        """
        Get a random list of numbers.

        Parameter:
        number (int): The number of data points in the list, defualt of a 1000.
        """

        data = []
        lower = 10
        upper = PLOT_HEIGHT

        for i in range(number):
            rand_val = randint(lower, upper)
            data.append(rand_val)

        return data
    
    def draw(self):
        pygame.draw.rect(self.win, DARK_GRAY, (GRAPH_WIDTH, 0, CONTROL_WIDTH, CONTROL_HEIGHT))
        pygame.draw.rect(self.win, BLACK, (GRAPH_WIDTH, 0, CONTROL_WIDTH, CONTROL_HEIGHT), 2)
    
    def select(self, pos):
        """
        Selects something on the control panel.

        Parameter:
        pos (tuple): The coordinates on the window that were selected.

        Return:
        boolean: True if a button was selected, False otherwise.
        """

        x, y = pos
        for btn in self.buttons.values():
            if btn.x <= x <= btn.x + BUTTON_WIDTH and btn.y <= y <= btn.y + BUTTON_HEIGHT:
                self.selected_btn = btn

                if btn.name == TYPE_GEN:
                    self.generated = True
                    self.buttons[TYPE_SORT].on = True
                elif btn.name == TYPE_SORT and self.generated:
                    self.turn_off([self.buttons[TYPE_RESET]])
                elif btn.name == TYPE_RESET:
                    self.reset()

                return True
        
        return False
    
    def turn_off(self, btns=[]):
        """
        Turn off the buttons on the control panel.

        If buttons are given then these are not switched off.

        Parameter:
        btns (List): Buttons to be ignored and not switched off.
        """

        for btn in self.buttons.values():
            if btn in btns:
                continue
            else:
                btn.turn_off()
    
    def reset(self, btns=[]):
        """
        Resets the control panel back to its default setting.

        If no specific buttons are given to reset then all are, otherwise only the specified.

        Parameter:
        btns (List): Holds the specific buttons to be reset. Default is an empty list.
        """

        self.generated = False

        if not btns:
            # empty list - all buttons are reset
            for btn in self.buttons.values():
                btn.reset()
        else:
            # reset buttons given
            for btn in btns:
                btn.reset()
    
    def update(self):
        """
        Refresh the display of the correct region on the window.

        This will be used to update any changes that may occur that are relevent to the
        control portion of the window.
        """

        self.draw()

        for btn in self.buttons.values():
            btn.update()
        
        pygame.display.update()