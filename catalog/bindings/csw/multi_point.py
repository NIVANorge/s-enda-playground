from dataclasses import dataclass
from bindings.csw.multi_point_type import MultiPointType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class MultiPoint(MultiPointType):
    class Meta:
        namespace = "http://www.opengis.net/gml"
