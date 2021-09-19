from dataclasses import dataclass
from bindings.csw.point_type import PointType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class Point(PointType):
    class Meta:
        namespace = "http://www.opengis.net/gml"
