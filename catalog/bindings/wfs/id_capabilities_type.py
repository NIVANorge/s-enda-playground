from dataclasses import dataclass, field
from typing import List
from bindings.wfs.resource_identifier_type import ResourceIdentifierType

__NAMESPACE__ = "http://www.opengis.net/fes/2.0"


@dataclass
class IdCapabilitiesType:
    class Meta:
        name = "Id_CapabilitiesType"

    resource_identifier: List[ResourceIdentifierType] = field(
        default_factory=list,
        metadata={
            "name": "ResourceIdentifier",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
            "min_occurs": 1,
        }
    )
