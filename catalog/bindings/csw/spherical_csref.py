from dataclasses import dataclass
from bindings.csw.spherical_csref_type import SphericalCsrefType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class SphericalCsref(SphericalCsrefType):
    class Meta:
        name = "sphericalCSRef"
        namespace = "http://www.opengis.net/gml"
