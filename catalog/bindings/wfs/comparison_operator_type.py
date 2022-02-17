from dataclasses import dataclass, field
from typing import Optional, Union
from bindings.wfs.comparison_operator_name_type_value import (
    ComparisonOperatorNameTypeValue,
)

__NAMESPACE__ = "http://www.opengis.net/fes/2.0"


@dataclass
class ComparisonOperatorType:
    name: Optional[Union[str, ComparisonOperatorNameTypeValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"extension:\w{2,}",
        },
    )
