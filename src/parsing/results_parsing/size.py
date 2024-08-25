"""Detection size wrapping class"""
import numpy as np


# pylint: disable=R0903
class Size:
    """Detection size wrapping class"""
    def __init__(self, size: list):
        """Detection size wrapping class"""
        self.x = size[0]
        self.y = size[1]
        self.z = size[2]

    def to_numpy(self):
        """Convert detection size to numpy array"""
        return np.array([self.x, self.y, self.z])
