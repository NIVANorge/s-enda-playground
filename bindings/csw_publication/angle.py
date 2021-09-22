from dataclasses import dataclass
from bindings.csw_publication.measure_type import MeasureType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class Angle(MeasureType):
    class Meta:
        name = "angle"
        namespace = "http://www.opengis.net/gml"
