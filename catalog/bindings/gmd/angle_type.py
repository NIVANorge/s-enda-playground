from dataclasses import dataclass
from bindings.gmd.measure_type import MeasureType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class AngleType(MeasureType):
    pass
