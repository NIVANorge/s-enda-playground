from dataclasses import dataclass, field
from typing import Optional
from bindings.wfs.additional_operators_type import AdditionalOperatorsType

__NAMESPACE__ = "http://www.opengis.net/fes/2.0"


@dataclass
class ExtendedCapabilitiesType:
    class Meta:
        name = "Extended_CapabilitiesType"

    additional_operators: Optional[AdditionalOperatorsType] = field(
        default=None,
        metadata={
            "name": "AdditionalOperators",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
        }
    )
