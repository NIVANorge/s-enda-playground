from dataclasses import dataclass
from bindings.csw.linear_ring_type import LinearRingType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class LinearRing(LinearRingType):
    class Meta:
        namespace = "http://www.opengis.net/gml"
