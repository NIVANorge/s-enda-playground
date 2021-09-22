from dataclasses import dataclass
from bindings.csw_publication.coordinate_system_axis_type import CoordinateSystemAxisType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class CoordinateSystemAxis(CoordinateSystemAxisType):
    class Meta:
        namespace = "http://www.opengis.net/gml"
