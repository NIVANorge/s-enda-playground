from dataclasses import dataclass, field
from typing import List
from bindings.wfs.comparison_operator_type import ComparisonOperatorType

__NAMESPACE__ = "http://www.opengis.net/fes/2.0"


@dataclass
class ComparisonOperatorsType:
    comparison_operator: List[ComparisonOperatorType] = field(
        default_factory=list,
        metadata={
            "name": "ComparisonOperator",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
            "min_occurs": 1,
        },
    )
