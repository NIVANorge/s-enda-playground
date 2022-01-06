from dataclasses import dataclass, field
from typing import List
from bindings.gmd.abstract_surface import AbstractSurface
from bindings.gmd.composite_surface_type import (
    CompositeSurface,
    OrientableSurface,
)
from bindings.gmd.polygon import Polygon
from bindings.gmd.polyhedral_surface import PolyhedralSurface
from bindings.gmd.surface import Surface
from bindings.gmd.tin import Tin
from bindings.gmd.triangulated_surface import TriangulatedSurface

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class SurfaceArrayPropertyType:
    """gml:SurfaceArrayPropertyType is a container for an array of surfaces.

    The elements are always contained in the array property, referencing
    geometry elements or arrays of geometry elements via XLinks is not
    supported.
    """

    composite_surface: List[CompositeSurface] = field(
        default_factory=list,
        metadata={
            "name": "CompositeSurface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "sequential": True,
        },
    )
    orientable_surface: List[OrientableSurface] = field(
        default_factory=list,
        metadata={
            "name": "OrientableSurface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "sequential": True,
        },
    )
    tin: List[Tin] = field(
        default_factory=list,
        metadata={
            "name": "Tin",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "sequential": True,
        },
    )
    triangulated_surface: List[TriangulatedSurface] = field(
        default_factory=list,
        metadata={
            "name": "TriangulatedSurface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "sequential": True,
        },
    )
    polyhedral_surface: List[PolyhedralSurface] = field(
        default_factory=list,
        metadata={
            "name": "PolyhedralSurface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "sequential": True,
        },
    )
    surface: List[Surface] = field(
        default_factory=list,
        metadata={
            "name": "Surface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "sequential": True,
        },
    )
    polygon: List[Polygon] = field(
        default_factory=list,
        metadata={
            "name": "Polygon",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "sequential": True,
        },
    )
    abstract_surface: List[AbstractSurface] = field(
        default_factory=list,
        metadata={
            "name": "AbstractSurface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "sequential": True,
        },
    )
    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
