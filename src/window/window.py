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
    type_sort (string): The type of sorting algorithm we want to run.
    """

    def __init__(self, win, type_sort):
        self.win = win
        self.type_sort = type_sort
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
            if self.type_sort == TYPE_INSERTION:
                self.graph.insertion_sort()
                self.graph.reset_sorting_indices()
            elif self.type_sort == TYPE_QUICKSORT:
                self.graph.quicksort(self.graph.data, 0, len(self.graph.data) - 1)
                self.graph.reset_sorting_indices()
            elif self.type_sort == TYPE_MERGESORT:
                data_enum = list(enumerate(self.graph.data))
                self.graph.mergesort(data_enum)
                self.graph.reset_sorting_indices()
            elif self.type_sort == TYPE_SELECTION:
                self.graph.selection_sort()
                self.graph.reset_sorting_indices()
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