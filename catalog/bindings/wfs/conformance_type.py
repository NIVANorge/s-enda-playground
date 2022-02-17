from dataclasses import dataclass, field
from typing import List
from bindings.wfs.domain_type import DomainType

__NAMESPACE__ = "http://www.opengis.net/fes/2.0"


@dataclass
class ConformanceType:
    constraint: List[DomainType] = field(
        default_factory=list,
        metadata={
            "name": "Constraint",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
            "min_occurs": 1,
        },
    )
