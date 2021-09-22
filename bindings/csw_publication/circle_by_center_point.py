from dataclasses import dataclass
from bindings.csw_publication.circle_by_center_point_type import CircleByCenterPointType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class CircleByCenterPoint(CircleByCenterPointType):
    class Meta:
        namespace = "http://www.opengis.net/gml"
