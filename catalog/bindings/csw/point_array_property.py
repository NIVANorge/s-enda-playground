from dataclasses import dataclass
from bindings.csw.point_array_property_type import PointArrayPropertyType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class PointArrayProperty(PointArrayPropertyType):
    class Meta:
        name = "pointArrayProperty"
        namespace = "http://www.opengis.net/gml"
