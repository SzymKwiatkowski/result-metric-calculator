"""Rotation wrapping class"""
import numpy as np


class Rotation:
    def __init__(self, rotation):
        self.x = rotation['qx']
        self.y = rotation['qy']
        self.z = rotation['qz']
        self.w = rotation['qw']

    def to_numpy(self):
        return np.array([self.x, self.y, self.z, self.w])
