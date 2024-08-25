"""Module providing results parsing functions."""
from pathlib import Path
from utils.helpers import load_json

from parsing.results_parsing.detections_collection import DetectionsCollection


class ResultsParser:
    """Results parsing class."""
    def __init__(self, results: dict, nuscenes_path: Path):
        """Init result parsing class"""
        self.samples_path = nuscenes_path
        self.samples_file = self.load_nuscenes_samples(nuscenes_path)
        self.results = {token: DetectionsCollection(results['results'][token], self.samples_file, token)
                        for token in results['results'].keys()}

    @staticmethod
    def load_nuscenes_samples(nuscenes_path: Path):
        """Load nuscenes samples file."""
        samples_file = load_json(nuscenes_path / 'sample.json')

        return samples_file

    def get_results(self) -> dict[str, DetectionsCollection]:
        """results getter"""
        return self.results
