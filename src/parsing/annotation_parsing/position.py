"""Position wrapping class"""
import numpy as np


class Position:
    def __init__(self, position: dict):
        self.x = position['x']
        self.y = position['y']
        self.z = position['z']

    def to_numpy(self) -> np.ndarray:
        return np.array([self.x, self.y, self.z])
