from dataclasses import dataclass, field
from typing import Optional
from bindings.csw_publication.abstract_surface_type import AbstractSurfaceType
from bindings.csw_publication.patches import Patches
from bindings.csw_publication.polygon_patches import PolygonPatches
from bindings.csw_publication.triangle_patches import TrianglePatches

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class SurfaceType(AbstractSurfaceType):
    """A Surface is a 2-dimensional primitive and is composed of one or more
    surface patches.

    The surface patches are connected to one another. The orientation of
    the surface is positive ("up"). The orientation of a surface chooses
    an "up" direction through the choice of the upward normal, which, if
    the surface is not a cycle, is the side of the surface from which
    the exterior boundary appears counterclockwise. Reversal of the
    surface orientation reverses the curve orientation of each boundary
    component, and interchanges the conceptual "up" and "down" direction
    of the surface. If the surface is the boundary of a solid, the "up"
    direction is usually outward. For closed surfaces, which have no
    boundary, the up direction is that of the surface patches, which
    must be consistent with one another. Its included surface patches
    describe the interior structure of the Surface.

    :ivar triangle_patches:
    :ivar polygon_patches:
    :ivar patches: This element encapsulates the patches of the surface.
    """
    triangle_patches: Optional[TrianglePatches] = field(
        default=None,
        metadata={
            "name": "trianglePatches",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    polygon_patches: Optional[PolygonPatches] = field(
        default=None,
        metadata={
            "name": "polygonPatches",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    patches: Optional[Patches] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
