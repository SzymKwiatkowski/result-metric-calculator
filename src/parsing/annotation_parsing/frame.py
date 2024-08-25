"""Frame wrapping class"""

from parsing.annotation_parsing.annotation import Annotation


# pylint: disable=R0903
class Frame:
    """Frame wrapping class"""
    def __init__(self, frame: dict):
        """initialize frame class"""
        self.annotations = [Annotation(annotation) for annotation in frame['annotations']]
        self.timestamp = frame['timestamp']
