from dataclasses import dataclass
from bindings.gmd.coordinate_system_axis_property_type import (
    CoordinateSystemAxisPropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class UsesAxis(CoordinateSystemAxisPropertyType):
    class Meta:
        name = "usesAxis"
        namespace = "http://www.opengis.net/gml"
