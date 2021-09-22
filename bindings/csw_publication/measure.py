from dataclasses import dataclass
from bindings.csw_publication.measure_type import MeasureType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class Measure(MeasureType):
    class Meta:
        name = "measure"
        namespace = "http://www.opengis.net/gml"
