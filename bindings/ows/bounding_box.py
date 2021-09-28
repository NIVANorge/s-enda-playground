from dataclasses import dataclass
from bindings.ows.bounding_box_type import BoundingBoxType

__NAMESPACE__ = "http://www.opengis.net/ows/2.0"


@dataclass
class BoundingBox(BoundingBoxType):
    class Meta:
        namespace = "http://www.opengis.net/ows/2.0"
