from dataclasses import dataclass, field
from typing import Optional
from bindings.gmd.abstract_geometric_primitive_type import (
    AbstractGeometricPrimitiveType,
)
from bindings.gmd.coordinates import Coordinates
from bindings.gmd.pos import Pos

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class PointType(AbstractGeometricPrimitiveType):
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
