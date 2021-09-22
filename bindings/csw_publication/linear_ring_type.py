from dataclasses import dataclass, field
from typing import List, Optional
from bindings.csw_publication.abstract_ring_type import AbstractRingType
from bindings.csw_publication.coord import Coord
from bindings.csw_publication.coordinates import Coordinates
from bindings.csw_publication.point_property import PointProperty
from bindings.csw_publication.point_rep import PointRep
from bindings.csw_publication.pos import Pos
from bindings.csw_publication.pos_list import PosList

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class LinearRingType(AbstractRingType):
    """
    A LinearRing is defined by four or more coordinate tuples, with linear
    interpolation between them; the first and last coordinates must be
    coincident.

    :ivar pos:
    :ivar point_property:
    :ivar point_rep: Deprecated with GML version 3.1.0. Use
        "pointProperty" instead. Included for backwards compatibility
        with GML 3.0.0.
    :ivar pos_list:
    :ivar coordinates: Deprecated with GML version 3.1.0. Use "posList"
        instead.
    :ivar coord: Deprecated with GML version 3.0 and included for
        backwards compatibility with GML 2. Use "pos" elements instead.
    """
    pos: List[Pos] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "min_occurs": 4,
            "sequential": True,
        }
    )
    point_property: List[PointProperty] = field(
        default_factory=list,
        metadata={
            "name": "pointProperty",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "min_occurs": 4,
            "sequential": True,
        }
    )
    point_rep: List[PointRep] = field(
        default_factory=list,
        metadata={
            "name": "pointRep",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "min_occurs": 4,
            "sequential": True,
        }
    )
    pos_list: Optional[PosList] = field(
        default=None,
        metadata={
            "name": "posList",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    coordinates: Optional[Coordinates] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    coord: List[Coord] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
