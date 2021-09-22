from dataclasses import dataclass
from bindings.csw_publication.rectangle_type import RectangleType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class Rectangle(RectangleType):
    class Meta:
        namespace = "http://www.opengis.net/gml"
