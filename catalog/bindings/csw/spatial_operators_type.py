from dataclasses import dataclass, field
from typing import List
from bindings.csw.spatial_operator_type import SpatialOperatorType

__NAMESPACE__ = "http://www.opengis.net/ogc"


@dataclass
class SpatialOperatorsType:
    spatial_operator: List[SpatialOperatorType] = field(
        default_factory=list,
        metadata={
            "name": "SpatialOperator",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
            "min_occurs": 1,
        }
    )
