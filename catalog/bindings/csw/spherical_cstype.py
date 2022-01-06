from dataclasses import dataclass
from bindings.csw.abstract_coordinate_system_type import AbstractCoordinateSystemType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class SphericalCstype(AbstractCoordinateSystemType):
    """A three-dimensional coordinate system with one distance measured from
    the origin and two angular coordinates.

    Not to be confused with an ellipsoidal coordinate system based on an
    ellipsoid "degenerated" into a sphere. A SphericalCS shall have
    three usesAxis associations.
    """

    class Meta:
        name = "SphericalCSType"
