"""Main script"""
import argparse
from pathlib import Path

from utils.helpers import load_json
from parsing.results_parsing.results_parser import ResultsParser
from parsing.annotation_parsing.annotation_parser import AnnotationParser
from matcher import Matcher


def main(args):
    """Main executable script"""
    results = load_json(args.result_file)
    annotations = load_json(args.annotations)
    nuscenes_path = Path(args.nuscenes_path)

    results_parser = ResultsParser(results, nuscenes_path)
    annotation_parser = AnnotationParser(annotations)
    frame = annotation_parser.get_samples_frames()[0]
    detection_result = results_parser.results[list(results_parser.results.keys())[0]]

    matcher = Matcher(annotation_parser, results_parser)
    matcher.run_eval()

    pass


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='ProgramName',
        description='What the program does',
        epilog='Text at the bottom of help')
    parser.add_argument('-r', '--result-file', action='store', default='data/results_nusc_petr_melex.json')
    parser.add_argument('-a', '--annotations', action='store', default='data/annotations.json')
    parser.add_argument('-n', '--nuscenes-path', action='store', default='data/nuscenes')
    parser.add_argument('-t', '--threshold', action='store', default=0.5)
    args_parsed = parser.parse_args()
    main(args_parsed)
