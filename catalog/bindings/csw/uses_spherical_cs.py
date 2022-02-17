from dataclasses import dataclass
from bindings.csw.spherical_csref_type import SphericalCsrefType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class UsesSphericalCs(SphericalCsrefType):
    """
    Association to the spherical coordinate system used by this CRS.
    """

    class Meta:
        name = "usesSphericalCS"
        namespace = "http://www.opengis.net/gml"
