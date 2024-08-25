"""Detection rotation wrapping class"""
import numpy as np


# pylint: disable=R0903
class Rotation:
    """Detection rotation wrapping class"""
    def __init__(self, rotation: list):
        """Detection rotation wrapping class"""
        self.x = rotation[0]
        self.y = rotation[1]
        self.z = rotation[2]
        self.w = rotation[3]

    def to_numpy(self):
        """Converts detection rotation to numpy array"""
        return np.array([self.x, self.y, self.z, self.w])
