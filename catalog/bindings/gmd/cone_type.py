from dataclasses import dataclass, field
from bindings.gmd.abstract_gridded_surface_type import AbstractGriddedSurfaceType
from bindings.gmd.curve_interpolation_type import CurveInterpolationType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class ConeType(AbstractGriddedSurfaceType):
    horizontal_curve_type: CurveInterpolationType = field(
        init=False,
        default=CurveInterpolationType.CIRCULAR_ARC3_POINTS,
        metadata={
            "name": "horizontalCurveType",
            "type": "Attribute",
        },
    )
    vertical_curve_type: CurveInterpolationType = field(
        init=False,
        default=CurveInterpolationType.LINEAR,
        metadata={
            "name": "verticalCurveType",
            "type": "Attribute",
        },
    )
