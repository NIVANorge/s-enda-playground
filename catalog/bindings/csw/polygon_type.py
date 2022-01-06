from dataclasses import dataclass, field
from typing import List, Optional
from bindings.csw.abstract_surface_type import AbstractSurfaceType
from bindings.csw.exterior import Exterior
from bindings.csw.inner_boundary_is import InnerBoundaryIs
from bindings.csw.interior import Interior
from bindings.csw.outer_boundary_is import OuterBoundaryIs

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class PolygonType(AbstractSurfaceType):
    """A Polygon is a special surface that is defined by a single surface
    patch.

    The boundary of this patch is coplanar and the polygon uses planar
    interpolation in its interior. It is backwards compatible with the
    Polygon of GML 2, GM_Polygon of ISO 19107 is implemented by
    PolygonPatch.
    """

    outer_boundary_is: Optional[OuterBoundaryIs] = field(
        default=None,
        metadata={
            "name": "outerBoundaryIs",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    exterior: Optional[Exterior] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    inner_boundary_is: List[InnerBoundaryIs] = field(
        default_factory=list,
        metadata={
            "name": "innerBoundaryIs",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    interior: List[Interior] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
