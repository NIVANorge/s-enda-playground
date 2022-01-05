from dataclasses import dataclass
from bindings.ows.wgs84_bounding_box_type import Wgs84BoundingBoxType

__NAMESPACE__ = "http://www.opengis.net/ows/2.0"


@dataclass
class Wgs84BoundingBox(Wgs84BoundingBoxType):
    class Meta:
        name = "WGS84BoundingBox"
        namespace = "http://www.opengis.net/ows/2.0"
