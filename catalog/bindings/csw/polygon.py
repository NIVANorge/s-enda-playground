from dataclasses import dataclass
from bindings.csw.polygon_type import PolygonType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class Polygon(PolygonType):
    class Meta:
        namespace = "http://www.opengis.net/gml"
