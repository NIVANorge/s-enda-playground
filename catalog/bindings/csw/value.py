from dataclasses import dataclass
from bindings.csw.measure_type import MeasureType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class Value(MeasureType):
    """
    Numeric value of an operation parameter, with its associated unit of
    measure.
    """
    class Meta:
        name = "value"
        namespace = "http://www.opengis.net/gml"
