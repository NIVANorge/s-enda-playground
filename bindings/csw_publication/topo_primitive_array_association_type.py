from dataclasses import dataclass, field
from typing import List
from bindings.csw_publication.container_property_type import (
    Edge,
    Face,
    Node,
    TopoSolid,
)
from bindings.csw_publication.topo_primitive import TopoPrimitive

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class TopoPrimitiveArrayAssociationType:
    """
    This type supports embedding an array of topological primitives in a
    TopoComplex.
    """
    topo_solid: List[TopoSolid] = field(
        default_factory=list,
        metadata={
            "name": "TopoSolid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "sequential": True,
        }
    )
    face: List[Face] = field(
        default_factory=list,
        metadata={
            "name": "Face",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "sequential": True,
        }
    )
    edge: List[Edge] = field(
        default_factory=list,
        metadata={
            "name": "Edge",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "sequential": True,
        }
    )
    node: List[Node] = field(
        default_factory=list,
        metadata={
            "name": "Node",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "sequential": True,
        }
    )
    topo_primitive: List[TopoPrimitive] = field(
        default_factory=list,
        metadata={
            "name": "_TopoPrimitive",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "sequential": True,
        }
    )
