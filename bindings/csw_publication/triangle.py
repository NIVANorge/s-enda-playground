from dataclasses import dataclass
from bindings.csw_publication.triangle_type import TriangleType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class Triangle(TriangleType):
    class Meta:
        namespace = "http://www.opengis.net/gml"
