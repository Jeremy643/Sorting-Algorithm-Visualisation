import pygame


class Graph:
    """
    The graph represents the data before, during and after the sorting process.

    We use our graph object to draw a graph in the correct region of the window, plot
    data on the graph, sort the data in a visual way and then, finally, represent the
    result of the sort on the given data.

    Attribute:
    win (Surface): The surface to which we will display data.
    """

    def __init__(self, win):
        self.win = win
    
    def update(self):
        """
        Refresh the display of the correct region on the window.

        This will be used to update any changes that may occur that are relevent to the
        graph portion of the window.
        """
        pass