from dataclasses import dataclass, field
from typing import List
from bindings.wfs.resource_id import ResourceId

__NAMESPACE__ = "http://www.opengis.net/wfs/2.0"


@dataclass
class FeaturesLockedType:
    resource_id: List[ResourceId] = field(
        default_factory=list,
        metadata={
            "name": "ResourceId",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
            "min_occurs": 1,
        },
    )
