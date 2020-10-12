import pygame
from .constants import *


class Graph:
    """
    The graph represents the data before, during and after the sorting process.

    We use our graph object to draw a graph in the correct region of the window, plot
    data on the graph, sort the data in a visual way and then, finally, represent the
    result of the sort on the given data.

    Attribute:
    win (Surface): The surface to which we will display data.
    data (List): The data to be sorted.
    """

    def __init__(self, win):
        self.win = win
        self.data = []
    
    def _draw_graph(self):
        pygame.draw.rect(self.win, BLACK, (PLOT_X, PLOT_Y, PLOT_WIDTH, PLOT_HEIGHT), 2)

        jump = 50
        label = 0

        for i in reversed(range(jump, PLOT_HEIGHT + jump, jump)):
            pygame.font.init()
            txt = pygame.font.Font('freesansbold.ttf', 20)
            txt_surf = txt.render(f'{label}', False, BLACK)
            label += jump

            txt_rect = txt_surf.get_rect()
            txt_rect.right = 40
            txt_rect.y = i

            self.win.blit(txt_surf, txt_rect)
        
        # label = jump
        # for i in range(jump, PLOT_WIDTH + jump, jump):
        #     pygame.font.init()
        #     txt = pygame.font.Font('freesansbold.ttf', 20)
        #     txt_surf = txt.render(f'{label}', False, BLACK)
        #     label += jump

        #     txt_rect = txt_surf.get_rect()
        #     txt_rect.y = PLOT_HEIGHT + (PLOT_Y + 10)
        #     txt_rect.x = i

        #     self.win.blit(txt_surf, txt_rect)

    def _draw_data(self):
        bar_width = PLOT_WIDTH // len(self.data)

        width_counter = PLOT_X
        for dp in self.data:
            pygame.draw.rect(self.win, BLUE, (width_counter, PLOT_HEIGHT - dp + PLOT_Y, bar_width, dp))
            pygame.draw.rect(self.win, BLACK, (width_counter, PLOT_HEIGHT - dp + PLOT_Y, bar_width, dp), 2)
            width_counter += bar_width

    def set_data(self, data):
        self.data = data
    
    def reset_data(self):
        self.data = []
    
    def draw(self):
        # fill and outline
        pygame.draw.rect(self.win, WHITE, (0, 0, GRAPH_WIDTH, GRAPH_HEIGHT))
        pygame.draw.rect(self.win, BLACK, (0, 0, GRAPH_WIDTH, GRAPH_HEIGHT), 2)

        # graph
        self._draw_graph()

        if self.data:
            # draw data on the graph
            self._draw_data()
    
    def insertion_sort(self):
        pass
    
    def update(self):
        """
        Refresh the display of the correct region on the window.

        This will be used to update any changes that may occur that are relevent to the
        graph portion of the window.
        """
        self.draw()
        pygame.display.update()