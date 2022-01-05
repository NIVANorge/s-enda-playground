from dataclasses import dataclass
from bindings.csw.sphere_type import SphereType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class Sphere(SphereType):
    class Meta:
        namespace = "http://www.opengis.net/gml"
