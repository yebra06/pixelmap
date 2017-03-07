"""Pixelmap

Cool pixelmap of Pixels.
Last updated: March 7, 2017
"""

from pixel import Pixel


class Pixelmap:

    def __init__(self, width, height):
        """Pixelmap constructor

        :param width: Width of map in pixels.
        :param height: Height of map in pixels.
        """
        self.width = width
        self.height = height
        self.map_matrix = [[0]*self.width for _ in range(self.height)]
        for row in range(self.height):
            for col in range(self.width):
                self.map_matrix[row][col] = Pixel()

    def __str__(self):
        """Human readable pixelmap description.
        Pretty much just the matrix.

        :return: Description of pixelmap.
        """
        return str('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in self.map_matrix]))

    def __repr__(self):
        """Internal representation

        Just use str for now.
        """
        return self.__str__()
