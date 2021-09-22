from dataclasses import dataclass, field
from typing import List, Optional
from bindings.csw_publication.abstract_geometric_aggregate_type import AbstractGeometricAggregateType
from bindings.csw_publication.composite_surface_type import SurfaceMember
from bindings.csw_publication.surface_members import SurfaceMembers

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class MultiSurfaceType(AbstractGeometricAggregateType):
    """
    A MultiSurface is defined by one or more Surfaces, referenced through
    surfaceMember elements.
    """
    surface_member: List[SurfaceMember] = field(
        default_factory=list,
        metadata={
            "name": "surfaceMember",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    surface_members: Optional[SurfaceMembers] = field(
        default=None,
        metadata={
            "name": "surfaceMembers",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
