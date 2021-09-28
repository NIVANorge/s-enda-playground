from dataclasses import dataclass, field
from typing import List
from bindings.wfs.temporal_operator_type import TemporalOperatorType

__NAMESPACE__ = "http://www.opengis.net/fes/2.0"


@dataclass
class TemporalOperatorsType:
    temporal_operator: List[TemporalOperatorType] = field(
        default_factory=list,
        metadata={
            "name": "TemporalOperator",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
            "min_occurs": 1,
        }
    )
