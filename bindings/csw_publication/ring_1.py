from dataclasses import dataclass
from bindings.csw_publication.ring_type import RingType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class Ring1(RingType):
    class Meta:
        name = "Ring"
        namespace = "http://www.opengis.net/gml"
