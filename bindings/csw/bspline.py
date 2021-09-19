from dataclasses import dataclass
from bindings.csw.bspline_type import BsplineType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class Bspline(BsplineType):
    class Meta:
        name = "BSpline"
        namespace = "http://www.opengis.net/gml"
