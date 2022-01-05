from dataclasses import dataclass
from bindings.wfs.wgs84_bounding_box_type import Wgs84BoundingBoxType

__NAMESPACE__ = "http://www.opengis.net/ows/1.1"


@dataclass
class Wgs84BoundingBox(Wgs84BoundingBoxType):
    class Meta:
        name = "WGS84BoundingBox"
        namespace = "http://www.opengis.net/ows/1.1"
