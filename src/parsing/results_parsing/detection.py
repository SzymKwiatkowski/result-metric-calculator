"""Detection result wrapping class"""

from parsing.results_parsing.size import Size
from parsing.results_parsing.rotation import Rotation
from parsing.results_parsing.translation import Translation


# pylint: disable=R0903, R0902
class Detection:
    """Detection result wrapping class"""
    def __init__(self, detection: dict, timestamp):
        """Detection result wrapping class"""
        self.sample_token = detection['sample_token']
        self.size = Size(detection['size'])
        self.rotation = Rotation(detection['rotation'])
        self.translation = Translation(detection['translation'])
        self.detection_name = detection['detection_name']
        self.detection_score = detection['detection_score']
        self.attribute_name = detection['attribute_name']
        self.timestamp = timestamp
