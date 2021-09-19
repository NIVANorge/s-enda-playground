from dataclasses import dataclass
from bindings.csw.clothoid_type import ClothoidType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class Clothoid(ClothoidType):
    class Meta:
        namespace = "http://www.opengis.net/gml"
