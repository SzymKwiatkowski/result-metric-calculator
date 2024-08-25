"""Class providing metrics calculation."""
import numpy as np

from parsing.annotation_parsing.annotation import Annotation
from parsing.results_parsing.detection import Detection


class Metrics:
    def __init__(self, annotation: Annotation, detection: Detection):
        self.metrics = self.calculate_metrics(annotation, detection)

    @staticmethod
    def calculate_metrics(annotation: Annotation, detection: Detection):
        trans_err = annotation.position.to_numpy() - detection.translation.to_numpy()
        scale_err = annotation.dimensions.to_numpy() - detection.size.to_numpy()
        orient_err = annotation.rotation.to_numpy() - detection.rotation.to_numpy()

        # metric_data = DetectionMetricData(
        #     recall=[0.0, 0.0, 0.0],
        #     precision=[0.0, 0.0, 0.0],
        #     attr_err=[0.0, 0.0, 0.0],
        #     vel_err=[0.0, 0.0, 0.0],
        #     confidence=detection.detection_score,
        #     trans_err=annotation.position.to_numpy() - detection.translation.to_numpy(),
        #     scale_err=annotation.dimensions.to_numpy() - detection.size.to_numpy(),
        #     orient_err=annotation.rotation.to_numpy() - detection.rotation.to_numpy(),
        # )
        #
        # metrics = {}
        # ap = calc_ap(metric_data, 0.0, 0.0)
        # metrics["ap"] = ap
        # for metric_name in TP_METRICS:
        #     tp = calc_tp(metric_data, 0.0, metric_name)
        #     metrics[metric_name] = tp

        return detection.detection_score, trans_err, scale_err, orient_err
