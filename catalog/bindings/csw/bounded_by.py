from dataclasses import dataclass
from bindings.csw.bounding_shape_type import BoundingShapeType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class BoundedBy(BoundingShapeType):
    class Meta:
        name = "boundedBy"
        namespace = "http://www.opengis.net/gml"
