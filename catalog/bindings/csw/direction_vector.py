from dataclasses import dataclass
from bindings.csw.direction_vector_type import DirectionVectorType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class DirectionVector(DirectionVectorType):
    class Meta:
        namespace = "http://www.opengis.net/gml"
