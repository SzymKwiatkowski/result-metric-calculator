"""Annotations typed class"""
from parsing.annotation_parsing.dimension import Dimension
from parsing.annotation_parsing.rotation import Rotation
from parsing.annotation_parsing.position import Position


# pylint: disable=R0903
class Annotation:
    """Annotations typed class"""
    def __init__(self, annotation):
        """Initialize annotation class"""
        self.dimensions = Dimension(annotation['dimensions'])
        self.rotation = Rotation(annotation['rotation'])
        self.yaw = annotation['yaw']
        self.category_id = annotation['category_id']
        self.position = Position(annotation['position'])
