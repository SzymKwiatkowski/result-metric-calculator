"""Detection translation wrapping class"""
import numpy as np


class Translation:
    def __init__(self, translation: list):
        self.x = translation[0]
        self.y = translation[1]
        self.z = translation[2]

    def to_numpy(self):
        return np.array([self.x, self.y, self.z])
