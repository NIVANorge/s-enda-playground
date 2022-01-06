from dataclasses import dataclass, field
from typing import List, Optional
from bindings.gmd.abstract_surface_patch_type import AbstractSurfacePatchType
from bindings.gmd.exterior import Exterior
from bindings.gmd.interior import Interior
from bindings.gmd.surface_interpolation_type import SurfaceInterpolationType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class PolygonPatchType(AbstractSurfacePatchType):
    exterior: Optional[Exterior] = field(
        default=None,
        metadata={
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
    interpolation: SurfaceInterpolationType = field(
        init=False,
        default=SurfaceInterpolationType.PLANAR,
        metadata={
            "type": "Attribute",
        },
    )
