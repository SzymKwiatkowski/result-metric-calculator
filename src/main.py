"""Main script"""
import numpy as np
import argparse
from pathlib import Path

from utils.helpers import load_json
from parsing.results_parsing.results_parser import ResultsParser
from parsing.annotation_parsing.annotation_parser import AnnotationParser
from matcher import Matcher

from nuscenes.eval.detection.constants import TP_METRICS


def main(args):
    """Main executable script"""
    results = load_json(args.result_file)
    annotations = load_json(args.annotations)
    nuscenes_path = Path(args.nuscenes_path)
    min_precision = 0.1
    min_recall = 0.1

    results_parser = ResultsParser(results, nuscenes_path)
    annotation_parser = AnnotationParser(annotations)

    matcher = Matcher(annotation_parser, results_parser)
    metrics_collection, precision, conf = matcher.run_eval()

    prec = np.copy(precision)
    prec = prec[round(100 * min_recall) + 1:]  # Clip low recalls. +1 to exclude the min recall bin.
    prec -= min_precision  # Clip low precision
    prec[prec < 0] = 0
    ap = float(np.mean(prec)) / (1.0 - min_precision)
    ac = float(np.mean(conf))

    tp_results = {}

    for metric_name in TP_METRICS:
        tp = float(np.mean(np.array([float(np.mean(np.array(metric[metric_name]))) for metric in metrics_collection])))
        tp_results[metric_name] = tp

    vals = list(tp_results.values())[:3]
    nds = (np.mean(np.array([np.clip(1 - value, 0, 1)
                                    for value in vals])))/(len(vals)*1.0)
    print("average precision: {:.4f}".format(ap))
    print("average confidence: {:.4f}".format(ac))
    print("nds: {:.4f}".format(nds))
    print(tp_results)


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
