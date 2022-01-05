from dataclasses import dataclass
from bindings.csw.distance_buffer_type import DistanceBufferType

__NAMESPACE__ = "http://www.opengis.net/ogc"


@dataclass
class Dwithin(DistanceBufferType):
    class Meta:
        name = "DWithin"
        namespace = "http://www.opengis.net/ogc"
