from dataclasses import dataclass
from bindings.gmd.point_property_type import PointPropertyType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class CenterOf(PointPropertyType):
    class Meta:
        name = "centerOf"
        namespace = "http://www.opengis.net/gml"
