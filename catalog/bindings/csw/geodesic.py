from dataclasses import dataclass
from bindings.csw.geodesic_type import GeodesicType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class Geodesic(GeodesicType):
    class Meta:
        namespace = "http://www.opengis.net/gml"
