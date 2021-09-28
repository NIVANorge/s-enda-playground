from dataclasses import dataclass, field
from typing import List
from bindings.wfs.extension_operator_type import ExtensionOperatorType

__NAMESPACE__ = "http://www.opengis.net/fes/2.0"


@dataclass
class AdditionalOperatorsType:
    operator: List[ExtensionOperatorType] = field(
        default_factory=list,
        metadata={
            "name": "Operator",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
        }
    )
