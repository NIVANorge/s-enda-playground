from dataclasses import dataclass
from bindings.csw_publication.point_property_type import PointPropertyType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class Position(PointPropertyType):
    class Meta:
        name = "position"
        namespace = "http://www.opengis.net/gml"
