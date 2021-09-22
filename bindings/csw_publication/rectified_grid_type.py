from dataclasses import dataclass, field
from typing import List, Optional
from bindings.csw_publication.grid_type import GridType
from bindings.csw_publication.point_property_type import PointPropertyType
from bindings.csw_publication.vector_type import VectorType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class RectifiedGridType(GridType):
    """
    A rectified grid has an origin and vectors that define its post locations.
    """
    origin: Optional[PointPropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )
    offset_vector: List[VectorType] = field(
        default_factory=list,
        metadata={
            "name": "offsetVector",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "min_occurs": 1,
        }
    )
