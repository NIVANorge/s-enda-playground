from dataclasses import dataclass
from bindings.gmd.abstract_coordinate_system_type import AbstractCoordinateSystemType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class PolarCstype(AbstractCoordinateSystemType):
    class Meta:
        name = "PolarCSType"
