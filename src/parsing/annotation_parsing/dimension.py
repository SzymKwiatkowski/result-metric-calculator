"""Dimension wrapping class"""
import numpy as np


class Dimension:
    def __init__(self, dimension):
        self.x = dimension['x']
        self.y = dimension['y']
        self.z = dimension['z']

    def to_numpy(self):
        return np.array([self.x, self.y, self.z])