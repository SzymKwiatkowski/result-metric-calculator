"""Annotations typed class"""
import numpy as np

from parsing.annotation_parsing.dimension import Dimension
from parsing.annotation_parsing.rotation import Rotation
from parsing.annotation_parsing.position import Position


class Annotation:
    def __init__(self, annotation):
        self.dimensions = Dimension(annotation['dimensions'])
        self.rotation = Rotation(annotation['rotation'])
        self.yaw = annotation['yaw']
        self.category_id = annotation['category_id']
        self.position = Position(annotation['position'])
