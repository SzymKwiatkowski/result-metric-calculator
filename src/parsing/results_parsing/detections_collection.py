"""Detections collection wrapping class"""

from parsing.results_parsing.detection import Detection


class DetectionsCollection:
    def __init__(self, detections, samples, token):
        sample = next((x for x in samples if x['token'] == token), None)

        self.detections = [Detection(detection, sample['timestamp']) for detection in detections]
        self.timestamp = sample['timestamp']
