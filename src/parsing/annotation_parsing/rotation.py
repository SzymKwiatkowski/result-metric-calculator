"""Rotation wrapping class"""


class Rotation:
    def __init__(self, rotation):
        self.x = rotation['qx']
        self.y = rotation['qy']
        self.z = rotation['qz']
        self.w = rotation['qw']