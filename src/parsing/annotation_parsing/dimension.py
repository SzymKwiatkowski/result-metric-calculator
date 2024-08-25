"""Dimension wrapping class"""
import numpy as np


# pylint: disable=R0903
class Dimension:
    """Dimension wrapping class"""
    def __init__(self, dimension):
        """Initialize dimension wrapping class"""
        self.x = dimension['x']
        self.y = dimension['y']
        self.z = dimension['z']

    def to_numpy(self):
        """Convert dimension to numpy array"""
        return np.array([self.x, self.y, self.z])
