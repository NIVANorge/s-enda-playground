from dataclasses import dataclass, field
from typing import List, Optional
from bindings.wfs.resource_id import ResourceId

__NAMESPACE__ = "http://www.opengis.net/wfs/2.0"


@dataclass
class CreatedOrModifiedFeatureType:
    resource_id: List[ResourceId] = field(
        default_factory=list,
        metadata={
            "name": "ResourceId",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
            "min_occurs": 1,
        },
    )
    handle: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
