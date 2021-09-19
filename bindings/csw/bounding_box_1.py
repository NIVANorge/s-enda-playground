from dataclasses import dataclass
from bindings.csw.bounding_box_type import BoundingBoxType

__NAMESPACE__ = "http://www.opengis.net/ows"


@dataclass
class BoundingBox1(BoundingBoxType):
    class Meta:
        name = "BoundingBox"
        namespace = "http://www.opengis.net/ows"
