from dataclasses import dataclass, field
from typing import Optional
from bindings.csw_publication.topo_volume import TopoVolume

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class TopoVolumePropertyType:
    topo_volume: Optional[TopoVolume] = field(
        default=None,
        metadata={
            "name": "TopoVolume",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )
