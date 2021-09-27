from dataclasses import dataclass, field
from typing import List, Optional
from bindings.gmd.abstract_topology_type import AbstractTopologyType
from bindings.gmd.aggregation_type import AggregationType
from bindings.gmd.container_property_type import DirectedTopoSolid

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class TopoVolumeType(AbstractTopologyType):
    directed_topo_solid: List[DirectedTopoSolid] = field(
        default_factory=list,
        metadata={
            "name": "directedTopoSolid",
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
