"""Frame wrapping class"""

from parsing.annotation_parsing.annotation import Annotation


class Frame:
    def __init__(self, frame: dict):
        self.annotations = [Annotation(annotation) for annotation in frame['annotations']]
        self.timestamp = frame['timestamp']