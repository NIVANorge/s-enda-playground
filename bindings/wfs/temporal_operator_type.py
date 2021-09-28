from dataclasses import dataclass, field
from typing import Optional, Union
from bindings.wfs.temporal_operands_type import TemporalOperandsType
from bindings.wfs.temporal_operator_name_type_value import TemporalOperatorNameTypeValue

__NAMESPACE__ = "http://www.opengis.net/fes/2.0"


@dataclass
class TemporalOperatorType:
    temporal_operands: Optional[TemporalOperandsType] = field(
        default=None,
        metadata={
            "name": "TemporalOperands",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
        }
    )
    name: Optional[Union[str, TemporalOperatorNameTypeValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"extension:\w{2,}",
        }
    )
