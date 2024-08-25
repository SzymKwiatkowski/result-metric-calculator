"""Detection size wrapping class"""
import numpy as np


class Size:
    def __init__(self, size: list):
        self.x = size[0]
        self.y = size[1]
        self.z = size[2]

    def to_numpy(self):
        return np.array([self.x, self.y, self.z])