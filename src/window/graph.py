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
    sorting_index (int): Index of the data element that is being sorted.
    checking_index (int): Index of the data value being compared with the current value being sorted.
    """

    def __init__(self, win):
        self.win = win
        self.data = []
        self.sorting_index = None
        self.checking_index1 = None
        self.checking_index2 = None
    
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

    def _draw_data(self):
        bar_width = PLOT_WIDTH // len(self.data)

        width_counter = PLOT_X
        index = 0
        for dp in self.data:
            if index == self.sorting_index:
                colour = GREEN
            elif index == self.checking_index1 or index == self.checking_index2:
                colour = RED
            else:
                colour = BLUE

            pygame.draw.rect(self.win, colour, (width_counter, PLOT_HEIGHT - dp + PLOT_Y, bar_width, dp))
            pygame.draw.rect(self.win, BLACK, (width_counter, PLOT_HEIGHT - dp + PLOT_Y, bar_width, dp), 2)
            width_counter += bar_width
            index += 1
    
    def _increase_index(self, left):
        new_left = []

        for l in left:
            index, value = l
            new_left.append((index + 1, value))
        
        return new_left
    
    def _find_minimum(self, index):
        """
        Finds the minimum value in data from the specified index to the end.

        Parameter:
        index (int): Index to start looking for the minimum value.

        Return:
        min_index (int): Index of the minimum value in data from the specified index.
        """

        minimum = float('inf')
        min_index = None
        i = index
        for d in self.data[index:]:
            if d < minimum:
                # highlight the current minimum value
                self.sorting_index = i
                self.update()

                minimum = d
                min_index = i
            i += 1
        
        return min_index
    
    def reset_sorting_indices(self):
        self.sorting_index = None
        self.checking_index1 = None
        self.checking_index2 = None

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
        for i in range(1, len(self.data)):
            curr = self.data[i]

            self.sorting_index = i
            self.update()

            for j in reversed(range(0, i)):
                self.checking_index1 = j
                self.update()

                if self.data[j] <= curr:
                    self.data.insert(j + 1, curr)
                    break
                elif j == 0:
                    self.data.insert(0, curr)
                    
            del self.data[i + 1]

            self._reset_sorting_indices()
    
    def quicksort(self, arr, low, high):
        if len(arr) == 1:
            return arr
        
        if low < high:
            p = self.partition(low, high)
            self.quicksort(self.data, low, p - 1)
            self.quicksort(self.data, p + 1, high)
    
    def partition(self, low, high):
        """
        Splits the data list into partitions.

        This method is used by the quicksort algorithm.

        Parameters:
        low (int): Index of the start of the partition.
        high (int): Index of the end of the partition.
        """

        pivot = self.data[high]
        self.sorting_index = high
        self.update()
        i = low - 1
        self.checking_index2 = i
        for j in range(low, high):
            self.checking_index1 = j
            self.update()
            if self.data[j] <= pivot:
                i += 1
                self.checking_index2 = i
                self.data[i], self.data[j] = self.data[j], self.data[i]
        self.data[i + 1], self.data[high] = self.data[high], self.data[i + 1]
        return i + 1
    
    def mergesort(self, sl):
        if len(sl) == 1:
            return sl

        left = self.mergesort(sl[:len(sl)//2])
        right = self.mergesort(sl[len(sl)//2:])

        return self.merge(left, right)
    
    def merge(self, left, right):
        """
        Combine two lists to get a sorted list.

        Parameters:
        left (tuple): Holds the index and then the actual value.
        right (tuple): Holds the index and then the actual value.
        """

        merged_arr = []

        while len(left) > 0 and len(right) > 0:
            self.sorting_index = right[0][0]
            self.checking_index1 = left[0][0]
            self.update()
            
            if left[0][1] <= right[0][1]:
                merged_arr.append(left.pop(0))
            else:
                ri = right.pop(0)
                old_index = ri[0]
                ri = (left[0][0], ri[1])
                left = self._increase_index(left)
                merged_arr.append(ri)

                self.data.insert(ri[0], ri[1])
                del self.data[old_index + 1]
                self.update()
        
        if len(left) == 0:
            merged_arr.extend(right)
        elif len(right) == 0:
            merged_arr.extend(left)
        
        return merged_arr
    
    def selection_sort(self):
        """
        Find the minimum value in the unsorted part of the list and move it to the end of the sorted part of the list.
        """

        index = 0
        while index < len(self.data):
            self.checking_index1 = index

            min_index = self._find_minimum(index)
            self.data[index], self.data[min_index] = self.data[min_index], self.data[index]
            index += 1
    
    def update(self):
        """
        Refresh the display of the correct region on the window.

        This will be used to update any changes that may occur that are relevent to the
        graph portion of the window.
        """
        self.draw()
        pygame.display.update()