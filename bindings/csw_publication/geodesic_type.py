from dataclasses import dataclass
from bindings.csw_publication.geodesic_string_type import GeodesicStringType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class GeodesicType(GeodesicStringType):
    """A Geodesic consists of two distinct positions joined by a geodesic
    curve.

    The control points of a Geodesic shall lie on the geodesic between
    its start point and end points. Between these two points, a geodesic
    curve defined from ellipsoid or geoid model used by the co-ordinate
    reference systems may be used to interpolate other positions. Any
    other point in the controlPoint array must fall on this geodesic.
    """
