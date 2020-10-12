import pygame
from .graph import Graph
from .control import Control
from .constants import *


class Window:
    """
    This class is used to represent the entire surface/window we are displaying onto.

    Attributes:
    win (Surface): The surface we are displaying onto.
    graph (Graph): An object to represent the section of the overall window that will display
                   the graph.
    control (Control): An object to represent the remaining part of the overall window that allows
                       the user to control various parts of the graph.
    """

    def __init__(self, win):
        self.win = win
        self.graph = Graph(self.win)
        self.control = Control(self.win)
    
    def select(self, pos):
        """
        Select something on the window.

        Parameter:
        pos (tuple): The coordinates of the click on the window.

        Return:
        boolean: True if a button on the control panel is selected, False otherwise.
        """
        x, y = pos

        if 0 <= x <= GRAPH_WIDTH:
            # the user can't select anything on the graph
            return False
        
        succ = self.control.select(pos)
        if self.control.selected_btn == self.control.gen_btn:
            data = self.control.get_data()
            self.graph.set_data(data)
        elif self.control.selected_btn == self.control.sort_btn:
            self.graph.insertion_sort()
        elif self.control.selected_btn == self.control.reset_btn:
            self.graph.reset_data()

        return succ
    
    def update(self):
        """
        Update the window.

        This method updates the window by updating both parts within it.
        """

        self.graph.update()
        self.control.update()
        pygame.display.update()