"""Pixelmap

Cool pixelmap of Pixels.
Last updated: March 11, 2017
"""

from .pixel import Pixel


class Pixelmap:

    def __init__(self, cols, rows, default_val=None):
        """Pixelmap constructor

        :param cols: Width of map in pixels.
        :param rows: Height of map in pixels.
        :param default_val: Default value for pixels.
        """
        assert cols >= 0, 'Invalid Pixelmap width'
        assert rows >= 0, 'Invalid Pixelmap height'
        self.cols = cols
        self.rows = rows
        self.map_matrix = [[0]*self.cols for _ in range(self.rows)]
        for row in range(self.rows):
            for col in range(self.cols):
                self.map_matrix[row][col] = Pixel(default_val)

    def num_cols(self):
        return self.cols

    def num_rows(self):
        return self.rows

    def __str__(self):
        """Human readable pixelmap description.
        Pretty much just the matrix.

        :return: Description of pixelmap.
        """
        return str('\n'.join([''.join(['{:6}'.format(str(item)) for item in row]) for row in self.map_matrix]))
