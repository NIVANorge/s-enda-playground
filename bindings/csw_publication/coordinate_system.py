from dataclasses import dataclass
from bindings.csw_publication.abstract_coordinate_system_type import AbstractCoordinateSystemType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class CoordinateSystem(AbstractCoordinateSystemType):
    class Meta:
        name = "_CoordinateSystem"
        namespace = "http://www.opengis.net/gml"
