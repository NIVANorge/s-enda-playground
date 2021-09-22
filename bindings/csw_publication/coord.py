from dataclasses import dataclass
from bindings.csw_publication.coord_type import CoordType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class Coord(CoordType):
    """Deprecated with GML 3.0 and included for backwards compatibility with
    GML 2.

    Use the "pos" element instead.
    """
    class Meta:
        name = "coord"
        namespace = "http://www.opengis.net/gml"
