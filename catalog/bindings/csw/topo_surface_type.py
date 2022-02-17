from dataclasses import dataclass, field
from typing import List
from bindings.csw.abstract_topology_type import AbstractTopologyType
from bindings.csw.container_property_type import DirectedFace

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class TopoSurfaceType(AbstractTopologyType):
    """The TopoSurface type and element represent a homogeneous topological
    expression, a set of directed faces, which if realised are isomorphic to a
    geometric surface primitive.

    The intended use of TopoSurface is to appear within a surface
    feature instance to express the structural and possibly geometric
    relationships of this surface to other features via the shared face
    definitions.
    """

    directed_face: List[DirectedFace] = field(
        default_factory=list,
        metadata={
            "name": "directedFace",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "min_occurs": 1,
        },
    )
