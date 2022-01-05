from dataclasses import dataclass, field
from typing import List
from bindings.gmd.abstract_gridded_surface import AbstractGriddedSurface
from bindings.gmd.abstract_parametric_curve_surface import AbstractParametricCurveSurface
from bindings.gmd.abstract_surface_patch import AbstractSurfacePatch
from bindings.gmd.cone import Cone
from bindings.gmd.cylinder import Cylinder
from bindings.gmd.polygon_patch import PolygonPatch
from bindings.gmd.rectangle import Rectangle
from bindings.gmd.sphere import Sphere
from bindings.gmd.triangle import Triangle

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class SurfacePatchArrayPropertyType:
    """
    gml:SurfacePatchArrayPropertyType is a container for a sequence of surface
    patches.
    """
    sphere: List[Sphere] = field(
        default_factory=list,
        metadata={
            "name": "Sphere",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "sequential": True,
        }
    )
    cylinder: List[Cylinder] = field(
        default_factory=list,
        metadata={
            "name": "Cylinder",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "sequential": True,
        }
    )
    cone: List[Cone] = field(
        default_factory=list,
        metadata={
            "name": "Cone",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "sequential": True,
        }
    )
    abstract_gridded_surface: List[AbstractGriddedSurface] = field(
        default_factory=list,
        metadata={
            "name": "AbstractGriddedSurface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "sequential": True,
        }
    )
    abstract_parametric_curve_surface: List[AbstractParametricCurveSurface] = field(
        default_factory=list,
        metadata={
            "name": "AbstractParametricCurveSurface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "sequential": True,
        }
    )
    rectangle: List[Rectangle] = field(
        default_factory=list,
        metadata={
            "name": "Rectangle",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "sequential": True,
        }
    )
    triangle: List[Triangle] = field(
        default_factory=list,
        metadata={
            "name": "Triangle",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "sequential": True,
        }
    )
    polygon_patch: List[PolygonPatch] = field(
        default_factory=list,
        metadata={
            "name": "PolygonPatch",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "sequential": True,
        }
    )
    abstract_surface_patch: List[AbstractSurfacePatch] = field(
        default_factory=list,
        metadata={
            "name": "AbstractSurfacePatch",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "sequential": True,
        }
    )
