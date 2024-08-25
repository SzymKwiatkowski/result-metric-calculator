"""Module providing annotation parsing functions."""

from parsing.annotation_parsing.frame import Frame


# pylint: disable=R0903
class AnnotationParser:
    """Annotation parsing functions class."""
    def __init__(self, annotations: dict):
        """Initialize annotation parsing functions."""
        self.annotations = annotations
        self.samples = annotations["dataset"]["samples"]
        self._samples_frames = self.get_sample_annotations(self.samples[0])

    @staticmethod
    def get_sample_annotations(sample) -> list[Frame]:
        """
        @param sample: individual sample to convert
        @return frames list: list[Frame]
        """
        return [Frame(frame) for frame in sample["labels"]['ground-truth']['attributes']['frames']]

    def get_samples_frames(self) -> list[Frame]:
        """sample frames getter"""
        return self._samples_frames
