from dataclasses import dataclass, field
from typing import List
from bindings.csw.abstract_topology_type import AbstractTopologyType
from bindings.csw.container_property_type import DirectedEdge

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class TopoCurveType(AbstractTopologyType):
    """The end Node of each directedEdge of a TopoCurveType is the start Node
    of the next directedEdge of the TopoCurveType in document order.

    The TopoCurve type and element represent a homogeneous topological
    expression, a list of directed edges, which if realised are
    isomorphic to a geometric curve primitive. The intended use of
    TopoCurve is to appear within a line feature instance to express the
    structural and geometric relationships of this line to other
    features via the shared edge definitions.
    """
    directed_edge: List[DirectedEdge] = field(
        default_factory=list,
        metadata={
            "name": "directedEdge",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "min_occurs": 1,
        }
    )
