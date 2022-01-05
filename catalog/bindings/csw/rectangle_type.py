from dataclasses import dataclass, field
from typing import Optional
from bindings.csw.abstract_surface_patch_type import AbstractSurfacePatchType
from bindings.csw.exterior import Exterior
from bindings.csw.outer_boundary_is import OuterBoundaryIs
from bindings.csw.surface_interpolation_type import SurfaceInterpolationType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class RectangleType(AbstractSurfacePatchType):
    """Represents a rectangle as a surface with an outer boundary consisting of
    a linear ring.

    Note that this is a polygon (subtype) with no inner boundaries. The
    number of points in the linear ring must be five.

    :ivar outer_boundary_is:
    :ivar exterior: Constraint: The Ring shall be a LinearRing and must
        form a rectangle; the first and the last position must be co-
        incident.
    :ivar interpolation: The attribute "interpolation" specifies the
        interpolation mechanism used for this surface patch. Currently
        only planar surface patches are defined in GML 3, the attribute
        is fixed to "planar", i.e. the interpolation method shall return
        points on a single plane. The boundary of the patch shall be
        contained within that plane.
    """
    outer_boundary_is: Optional[OuterBoundaryIs] = field(
        default=None,
        metadata={
            "name": "outerBoundaryIs",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    exterior: Optional[Exterior] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    interpolation: SurfaceInterpolationType = field(
        init=False,
        default=SurfaceInterpolationType.PLANAR,
        metadata={
            "type": "Attribute",
        }
    )
