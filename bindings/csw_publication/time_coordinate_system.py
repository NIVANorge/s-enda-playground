from dataclasses import dataclass
from bindings.csw_publication.time_coordinate_system_type import TimeCoordinateSystemType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class TimeCoordinateSystem(TimeCoordinateSystemType):
    class Meta:
        namespace = "http://www.opengis.net/gml"
