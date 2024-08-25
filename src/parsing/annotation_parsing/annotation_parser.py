"""Module providing annotation parsing functions."""

from parsing.annotation_parsing.frame import Frame


class AnnotationParser:
    def __init__(self, annotations: dict):
        self.annotations = annotations
        self.samples = annotations["dataset"]["samples"]
        self._samples_frames = self.get_sample_annotations(self.samples[0])

    @staticmethod
    def get_sample_annotations(sample) -> list[Frame]:
        return [Frame(frame) for frame in sample["labels"]['ground-truth']['attributes']['frames']]

    def get_samples_frames(self) -> list[Frame]:
        return self._samples_frames
