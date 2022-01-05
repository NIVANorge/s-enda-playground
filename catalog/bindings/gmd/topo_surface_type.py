from dataclasses import dataclass, field
from typing import List, Optional
from bindings.gmd.abstract_topology_type import AbstractTopologyType
from bindings.gmd.aggregation_type import AggregationType
from bindings.gmd.container_property_type import DirectedFace

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class TopoSurfaceType(AbstractTopologyType):
    directed_face: List[DirectedFace] = field(
        default_factory=list,
        metadata={
            "name": "directedFace",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "min_occurs": 1,
        }
    )
    aggregation_type: Optional[AggregationType] = field(
        default=None,
        metadata={
            "name": "aggregationType",
            "type": "Attribute",
        }
    )
