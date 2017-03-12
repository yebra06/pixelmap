"""Pixel

A pixel data structure with it's own uid that makes a Pixelmap.
Last updated: March 11, 2017
"""

from itertools import count


class Pixel:
    new_id = count(1)

    def __init__(self, data=None):
        """Pixel constructor"""
        self.id = next(self.new_id)
        self.data = data

    def __str__(self):
        return str(self.data)
