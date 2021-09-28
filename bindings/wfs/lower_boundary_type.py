from dataclasses import dataclass, field
from typing import Optional
from bindings.wfs.expression import Expression
from bindings.wfs.function_type import Function
from bindings.wfs.literal import Literal

__NAMESPACE__ = "http://www.opengis.net/fes/2.0"


@dataclass
class LowerBoundaryType:
    literal: Optional[Literal] = field(
        default=None,
        metadata={
            "name": "Literal",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
        }
    )
    function: Optional[Function] = field(
        default=None,
        metadata={
            "name": "Function",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
        }
    )
    value_reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "ValueReference",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
        }
    )
    expression: Optional[Expression] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
        }
    )
