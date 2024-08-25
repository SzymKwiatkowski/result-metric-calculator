"""Detections collection wrapping class"""

from parsing.results_parsing.detection import Detection


# pylint: disable=R0903
class DetectionsCollection:
    """Detections collection wrapping class"""
    def __init__(self, detections, samples, token):
        """Init wrapping class"""
        sample = next((x for x in samples if x['token'] == token), None)

        self.detections = [Detection(detection, sample['timestamp']) for detection in detections]
        self.timestamp = sample['timestamp']
