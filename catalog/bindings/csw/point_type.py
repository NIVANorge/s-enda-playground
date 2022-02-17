from dataclasses import dataclass, field
from typing import Optional
from bindings.csw.abstract_geometric_primitive_type import (
    AbstractGeometricPrimitiveType,
)
from bindings.csw.coord import Coord
from bindings.csw.coordinates import Coordinates
from bindings.csw.pos import Pos

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class PointType(AbstractGeometricPrimitiveType):
    """
    A Point is defined by a single coordinate tuple.

    :ivar pos:
    :ivar coordinates: Deprecated with GML version 3.1.0 for coordinates
        with ordinate values that are numbers. Use "pos" instead. The
        "coordinates" element shall only be used for coordinates with
        ordinates that require a string representation, e.g. DMS
        representations.
    :ivar coord: Deprecated with GML version 3.0. Use "pos" instead. The
        "coord" element is included for backwards compatibility with GML
        2.
    """

    pos: Optional[Pos] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    coordinates: Optional[Coordinates] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    coord: Optional[Coord] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
