from dataclasses import dataclass, field
from typing import List
from bindings.csw_publication.abstract_topology_type import AbstractTopologyType
from bindings.csw_publication.container_property_type import DirectedTopoSolid

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class TopoVolumeType(AbstractTopologyType):
    """The TopoVolume type and element represent a homogeneous topological
    expression, a set of directed TopoSolids, which if realised are isomorphic
    to a geometric solid primitive.

    The intended use of TopoVolume is to appear within a 3D solid
    feature instance to express the structural and geometric
    relationships of this solid to other features via the shared
    TopoSolid definitions.  . Note the orientation assigned to the
    directedSolid has no meaning in three dimensions. It is preserved
    for symmetry with the preceding types and elements.
    """
    directed_topo_solid: List[DirectedTopoSolid] = field(
        default_factory=list,
        metadata={
            "name": "directedTopoSolid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "min_occurs": 1,
        }
    )
