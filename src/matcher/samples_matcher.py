"""Sample matcher class"""
import numpy as np

from parsing import ResultsParser, AnnotationParser
from parsing.results_parsing.detection import Detection
from parsing.annotation_parsing.annotation import Annotation


class Matcher:
    def __init__(self, annotation_parser: AnnotationParser, results_parser: ResultsParser):
        self.annotation_parser = annotation_parser
        self.results_parser = results_parser

    def run_eval(self):
        frames = self.annotation_parser.get_samples_frames()
        frames_stamps = np.array([frame.timestamp for frame in frames], dtype=np.int64)
        for key, detections_collection in self.results_parser.get_results().items():
            diff_stamps = frames_stamps.copy() - detections_collection.timestamp
            frame_idx = diff_stamps.argmin(axis=0)

            frame = frames[frame_idx]
            for detection in detections_collection.detections:
                annotation = self._match_annotation(frame.annotations, detection)
                continue
            pass

    def _match_annotation(self, annotations: list[Annotation], detection: Detection) -> Annotation:
        ann = np.array([self._calc_distance(annotation, detection) for annotation in annotations])

        return annotations[ann.argmin(axis=0)]

    def _calc_distance(self, annotation, detection):
        return np.sqrt(np.sum(np.square(annotation.position.to_numpy() - detection.translation.to_numpy())))