from dataclasses import dataclass
from bindings.csw.ellipsoid_type import EllipsoidType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class Ellipsoid(EllipsoidType):
    class Meta:
        namespace = "http://www.opengis.net/gml"
