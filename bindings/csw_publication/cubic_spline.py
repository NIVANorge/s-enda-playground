from dataclasses import dataclass
from bindings.csw_publication.cubic_spline_type import CubicSplineType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class CubicSpline(CubicSplineType):
    class Meta:
        namespace = "http://www.opengis.net/gml"
