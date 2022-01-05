from dataclasses import dataclass
from bindings.csw.spherical_cstype import SphericalCstype

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class SphericalCs(SphericalCstype):
    class Meta:
        name = "SphericalCS"
        namespace = "http://www.opengis.net/gml"
