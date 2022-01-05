from dataclasses import dataclass
from bindings.csw.direction_property_type import DirectionPropertyType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class Direction(DirectionPropertyType):
    class Meta:
        name = "direction"
        namespace = "http://www.opengis.net/gml"
