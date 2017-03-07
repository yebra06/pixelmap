"""Pixel

A pixel data structure with it's own uid that makes a Pixelmap.
Last updated: March 7, 2017
"""

from itertools import count


class Pixel:
    new_id = count(1)

    def __init__(self):
        """Pixel constructor"""
        self.id = next(self.new_id)

    def __str__(self):
        return str(self.id)

    def __repr__(self):
        return self.__str__()
