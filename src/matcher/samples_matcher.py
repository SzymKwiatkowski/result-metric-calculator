"""Sample matcher class"""
import numpy as np

from parsing import ResultsParser, AnnotationParser
from parsing.results_parsing.detection import Detection
from parsing.annotation_parsing.annotation import Annotation

from utils.math import center_distance, scale_iou, yaw_diff
from utils.metrics import Metrics


class Matcher:
    def __init__(self, annotation_parser: AnnotationParser, results_parser: ResultsParser):
        self.annotation_parser = annotation_parser
        self.results_parser = results_parser

    def run_eval(self):
        frames = self.annotation_parser.get_samples_frames()
        frames_stamps = np.array([frame.timestamp for frame in frames], dtype=np.int64)
        metric_data_list = []

        # Do the actual matching.
        tp = []  # Accumulator of true positives.
        fp = []  # Accumulator of false positives.
        conf = []  # Accumulator of confidences.

        for key, detections_collection in self.results_parser.get_results().items():
            diff_stamps = frames_stamps.copy()[frames_stamps < detections_collection.timestamp] \
                          - detections_collection.timestamp
            frame_idx = diff_stamps.argmin(axis=0)

            frame = frames[frame_idx]

            npos = len([1 for gt in frame.annotations if gt.category_id == 1])

            match_data = {'trans_err': [],
                          'vel_err': [],
                          'scale_err': [],
                          'orient_err': [],
                          'attr_err': [],
                          'conf': []}

            for detection in detections_collection.detections:
                annotation = self._match_annotation(frame.annotations, detection)
                detection_score, trans_err, scale_err, ori_err = Metrics.calculate_metrics(annotation, detection)
                #  Update tp, fp and confs.
                tp.append(1)
                fp.append(0)
                conf.append(detection.detection_score)
                match_data['trans_err'].append(center_distance(annotation.position.to_numpy(),
                                                               detection.translation.to_numpy()))
                # REMOVE because it's not provided
                # match_data['vel_err'].append(velocity_l2(gt_box_match, pred_box))
                match_data['scale_err'].append(1 - scale_iou(annotation.dimensions.to_numpy(),
                                                             detection.size.to_numpy()))

                # Barrier orientation is only determined up to 180 degree. (For cones orientation is discarded later)
                period = np.pi if detection.detection_name == 'barrier' else 2 * np.pi
                match_data['orient_err'].append(yaw_diff(annotation.rotation.to_numpy(),
                                                         detection.rotation.to_numpy(),
                                                         period=period))

                # REMOVE because it's not provided
                # match_data['attr_err'].append(1 - attr_acc(gt_box_match, pred_box))
                match_data['conf'].append(detection.detection_score)

                metric_data_list.append(match_data)

        tp = np.cumsum(tp).astype(float)
        fp = np.cumsum(fp).astype(float)
        conf = np.array(conf)

        # Calculate precision and recall.
        prec = tp / (fp + tp)
        rec = tp / float(npos)

        rec_interp = np.linspace(0, 1, 101)  # 101 steps, from 0% to 100% recall.
        prec = np.interp(rec_interp, rec, prec, right=0)
        conf = np.interp(rec_interp, rec, conf, right=0)

        return metric_data_list, prec, conf

    def _match_annotation(self, annotations: list[Annotation], detection: Detection) -> Annotation:
        ann = np.array([self._calc_distance(annotation, detection) for annotation in annotations])

        return annotations[ann.argmin(axis=0)]

    @staticmethod
    def _calc_distance(annotation, detection):
        return np.sqrt(np.sum(np.square(annotation.position.to_numpy() - detection.translation.to_numpy())))