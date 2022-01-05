from dataclasses import dataclass
from bindings.csw.coordinate_system_ref_type import CoordinateSystemRefType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class CoordinateSystemRef(CoordinateSystemRefType):
    class Meta:
        name = "coordinateSystemRef"
        namespace = "http://www.opengis.net/gml"
