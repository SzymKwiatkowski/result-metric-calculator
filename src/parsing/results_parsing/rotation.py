"""Detection rotation wrapping class"""


class Rotation:
    def __init__(self, rotation: list):
        self.x = rotation[0]
        self.y = rotation[1]
        self.z = rotation[2]
        self.w = rotation[3]