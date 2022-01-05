from dataclasses import dataclass, field
from typing import List
from bindings.csw.comparison_operator_type import ComparisonOperatorType

__NAMESPACE__ = "http://www.opengis.net/ogc"


@dataclass
class ComparisonOperatorsType:
    comparison_operator: List[ComparisonOperatorType] = field(
        default_factory=list,
        metadata={
            "name": "ComparisonOperator",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
            "min_occurs": 1,
        }
    )
