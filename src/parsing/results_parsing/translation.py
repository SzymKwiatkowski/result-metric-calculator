"""Detection translation wrapping class"""
import numpy as np


# pylint: disable=R0903
class Translation:
    """Translation class"""
    def __init__(self, translation: list):
        """Translation class"""
        self.x = translation[0]
        self.y = translation[1]
        self.z = translation[2]

    def to_numpy(self):
        """Convert class properties to numpy array"""
        return np.array([self.x, self.y, self.z])
