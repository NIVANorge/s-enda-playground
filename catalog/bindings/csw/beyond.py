from dataclasses import dataclass
from bindings.csw.distance_buffer_type import DistanceBufferType

__NAMESPACE__ = "http://www.opengis.net/ogc"


@dataclass
class Beyond(DistanceBufferType):
    class Meta:
        namespace = "http://www.opengis.net/ogc"
