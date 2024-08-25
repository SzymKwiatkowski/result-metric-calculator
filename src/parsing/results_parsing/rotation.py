"""Detection rotation wrapping class"""
import numpy as np


class Rotation:
    def __init__(self, rotation: list):
        self.x = rotation[0]
        self.y = rotation[1]
        self.z = rotation[2]
        self.w = rotation[3]

    def to_numpy(self):
        return np.array([self.x, self.y, self.z, self.w])