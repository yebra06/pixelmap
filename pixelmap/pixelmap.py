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
        self.pixel_matrix = [[0] * self.cols for _ in range(self.rows)]
        for row in range(self.rows):
            for col in range(self.cols):
                self.pixel_matrix[row][col] = Pixel(default_val)

    def num_cols(self):
        """Matrix column count

        :return: Integer number of rows.
        """
        return self.cols

    def num_rows(self):
        """Matrix row count

        :return: Integer number of rows.
        """
        return self.rows

    def __len__(self):
        """Total size of pixel_matrix

        :return: Total number of pixels in matrix.
        """
        return self.cols * self.rows

    def __getitem__(self, coords):
        """Get matrix data

        :param coords: 2-tuple of row and column indexes.
        :return: Pixel data at given coordinates (xy) values.
        """
        assert len(coords) == 2, 'Invalid pixelmap subscripts'
        return self.pixel_matrix[coords[0]][coords[1]]

    def __setitem__(self, coords, data):
        """Set matrix data

        :param coords: 2-tuple of row and column indexes.
        :param data: Pixel data to be set.
        """
        assert len(coords) == 2, 'Invalid pixelmap subscripts'
        self.pixel_matrix[coords[0]][coords[1]] = data

    def __contains__(self, item):
        """Check if item in pixel_matrix

        :param item: An item a Pixel could store.
        :return: True if item is in pixel_matrix, else False.
        """
        for row in range(self.rows):
            for col in range(self.cols):
                if self.pixel_matrix[row][col] == item:
                    return True
        return False

    def __str__(self):
        """Human readable pixelmap description.
        Pretty much just the matrix.

        :return: Description of pixelmap.
        """
        return str('\n'.join([''.join(['{:6}'.format(str(item)) for item in row]) for row in self.pixel_matrix]))
