from dataclasses import dataclass, field
from typing import List
from bindings.csw.cone import Cone
from bindings.csw.cylinder import Cylinder
from bindings.csw.gridded_surface import GriddedSurface
from bindings.csw.parametric_curve_surface import ParametricCurveSurface
from bindings.csw.polygon_patch import PolygonPatch
from bindings.csw.rectangle import Rectangle
from bindings.csw.sphere import Sphere
from bindings.csw.surface_patch import SurfacePatch
from bindings.csw.triangle import Triangle

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class SurfacePatchArrayPropertyType:
    """
    A container for an array of surface patches.
    """

    sphere: List[Sphere] = field(
        default_factory=list,
        metadata={
            "name": "Sphere",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "sequential": True,
        },
    )
    cylinder: List[Cylinder] = field(
        default_factory=list,
        metadata={
            "name": "Cylinder",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "sequential": True,
        },
    )
    cone: List[Cone] = field(
        default_factory=list,
        metadata={
            "name": "Cone",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "sequential": True,
        },
    )
    gridded_surface: List[GriddedSurface] = field(
        default_factory=list,
        metadata={
            "name": "_GriddedSurface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "sequential": True,
        },
    )
    parametric_curve_surface: List[ParametricCurveSurface] = field(
        default_factory=list,
        metadata={
            "name": "_ParametricCurveSurface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "sequential": True,
        },
    )
    rectangle: List[Rectangle] = field(
        default_factory=list,
        metadata={
            "name": "Rectangle",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "sequential": True,
        },
    )
    triangle: List[Triangle] = field(
        default_factory=list,
        metadata={
            "name": "Triangle",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "sequential": True,
        },
    )
    polygon_patch: List[PolygonPatch] = field(
        default_factory=list,
        metadata={
            "name": "PolygonPatch",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "sequential": True,
        },
    )
    surface_patch: List[SurfacePatch] = field(
        default_factory=list,
        metadata={
            "name": "_SurfacePatch",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "sequential": True,
        },
    )
