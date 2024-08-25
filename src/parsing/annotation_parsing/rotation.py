"""Rotation wrapping class"""
import numpy as np


# pylint: disable=R0903
class Rotation:
    """Rotation wrapping class"""
    def __init__(self, rotation):
        self.x = rotation['qx']
        self.y = rotation['qy']
        self.z = rotation['qz']
        self.w = rotation['qw']

    def to_numpy(self):
        """convert to numpy array"""
        return np.array([self.x, self.y, self.z, self.w])
