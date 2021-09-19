from dataclasses import dataclass
from bindings.csw.ellipsoidal_csref_type import EllipsoidalCsrefType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class UsesEllipsoidalCs(EllipsoidalCsrefType):
    """
    Association to the ellipsoidal coordinate system used by this CRS.
    """
    class Meta:
        name = "usesEllipsoidalCS"
        namespace = "http://www.opengis.net/gml"
