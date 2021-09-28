from dataclasses import dataclass, field
from typing import Optional
from bindings.wfs.temporal_operands_type import TemporalOperandsType
from bindings.wfs.temporal_operators_type import TemporalOperatorsType

__NAMESPACE__ = "http://www.opengis.net/fes/2.0"


@dataclass
class TemporalCapabilitiesType:
    class Meta:
        name = "Temporal_CapabilitiesType"

    temporal_operands: Optional[TemporalOperandsType] = field(
        default=None,
        metadata={
            "name": "TemporalOperands",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
            "required": True,
        }
    )
    temporal_operators: Optional[TemporalOperatorsType] = field(
        default=None,
        metadata={
            "name": "TemporalOperators",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
            "required": True,
        }
    )
