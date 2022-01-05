from dataclasses import dataclass
from bindings.csw.multi_curve_type import MultiCurveType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class MultiCurve(MultiCurveType):
    class Meta:
        namespace = "http://www.opengis.net/gml"
