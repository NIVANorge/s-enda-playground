from dataclasses import dataclass, field
from typing import List
from bindings.wfs.spatial_operator_type import SpatialOperatorType

__NAMESPACE__ = "http://www.opengis.net/fes/2.0"


@dataclass
class SpatialOperatorsType:
    spatial_operator: List[SpatialOperatorType] = field(
        default_factory=list,
        metadata={
            "name": "SpatialOperator",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
            "min_occurs": 1,
        }
    )
