from dataclasses import dataclass
from bindings.csw.circle_type import CircleType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class Circle(CircleType):
    class Meta:
        namespace = "http://www.opengis.net/gml"
