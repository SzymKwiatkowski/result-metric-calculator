"""Class providing metrics calculation."""
from parsing.annotation_parsing.annotation import Annotation
from parsing.results_parsing.detection import Detection


class Metrics:
    """Class providing metrics calculation."""
    def __init__(self, annotation: Annotation, detection: Detection):
        self.metrics = self.calculate_metrics(annotation, detection)

    @staticmethod
    def calculate_metrics(annotation: Annotation, detection: Detection):
        """
        @param annotation: Annotation
        @param detection: Detection
        @return: tuple[float, float, float, float]
        """
        trans_err, scale_err, orient_err = Metrics.calculate_errors(annotation, detection)
        return detection.detection_score, trans_err, scale_err, orient_err

    @staticmethod
    def calculate_errors(annotation: Annotation, detection: Detection):
        """
        @param annotation: Annotation
        @param detection: Detection
        @return: tuple[float, float, float]
        """
        trans_err = annotation.position.to_numpy() - detection.translation.to_numpy()
        scale_err = annotation.dimensions.to_numpy() - detection.size.to_numpy()
        orient_err = annotation.rotation.to_numpy() - detection.rotation.to_numpy()

        return trans_err, scale_err, orient_err
