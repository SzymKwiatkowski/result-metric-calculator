"""Position wrapping class"""
import numpy as np


# pylint: disable=R0903
class Position:
    """Position wrapping class"""
    def __init__(self, position: dict):
        """Initialize position"""
        self.x = position['x']
        self.y = position['y']
        self.z = position['z']

    def to_numpy(self) -> np.ndarray:
        """Convert position to numpy array"""
        return np.array([self.x, self.y, self.z])
