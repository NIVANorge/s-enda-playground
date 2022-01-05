from dataclasses import dataclass
from bindings.gmd.abstract_topology_type import AbstractTopologyType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class AbstractTopology(AbstractTopologyType):
    class Meta:
        namespace = "http://www.opengis.net/gml"
