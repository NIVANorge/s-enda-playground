from dataclasses import dataclass, field
from typing import Optional
from bindings.gmd.abstract_surface_type import AbstractSurfaceType
from bindings.gmd.patches import Patches
from bindings.gmd.polygon_patches import PolygonPatches
from bindings.gmd.triangle_patches import TrianglePatches

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class SurfaceType(AbstractSurfaceType):
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
