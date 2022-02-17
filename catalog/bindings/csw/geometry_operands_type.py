from dataclasses import dataclass, field
from typing import List
from bindings.csw.geometry_operand_type import GeometryOperandType

__NAMESPACE__ = "http://www.opengis.net/ogc"


@dataclass
class GeometryOperandsType:
    geometry_operand: List[GeometryOperandType] = field(
        default_factory=list,
        metadata={
            "name": "GeometryOperand",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
            "min_occurs": 1,
        },
    )
