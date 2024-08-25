"""Module providing results parsing functions."""
from pathlib import Path
from utils.helpers import load_json

from parsing.results_parsing.detections_collection import DetectionsCollection


class ResultsParser:
    def __init__(self, results: dict, nuscenes_path: Path):
        self.samples_path = nuscenes_path
        self.samples_file, self.samples_data_file = self.load_nuscenes_samples(nuscenes_path)
        self.results = {token: DetectionsCollection(results['results'][token], self.samples_file, token)
                        for token in results['results'].keys()}

    @staticmethod
    def load_nuscenes_samples(nuscenes_path: Path):
        samples_file = load_json(nuscenes_path / 'sample.json')
        samples_data_file = load_json(nuscenes_path / 'sample_data.json')

        return samples_file, samples_data_file

    def get_results(self) -> dict[str, DetectionsCollection]:
        return self.results
