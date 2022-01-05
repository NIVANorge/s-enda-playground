from dataclasses import dataclass
from bindings.wfs.bounding_box_type import BoundingBoxType

__NAMESPACE__ = "http://www.opengis.net/ows/1.1"


@dataclass
class BoundingBox(BoundingBoxType):
    class Meta:
        namespace = "http://www.opengis.net/ows/1.1"
