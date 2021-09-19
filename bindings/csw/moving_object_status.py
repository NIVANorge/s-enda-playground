from dataclasses import dataclass
from bindings.csw.moving_object_status_type import MovingObjectStatusType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class MovingObjectStatus(MovingObjectStatusType):
    class Meta:
        namespace = "http://www.opengis.net/gml"
