from dataclasses import dataclass
from bindings.csw_publication.measure_type import MeasureType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class Result(MeasureType):
    """
    A quantitative result defined by the evaluation procedure used, and
    identified by the measureDescription.
    """
    class Meta:
        name = "result"
        namespace = "http://www.opengis.net/gml"
