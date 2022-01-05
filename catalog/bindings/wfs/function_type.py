from dataclasses import dataclass, field
from typing import List, Optional
from bindings.wfs.expression import Expression
from bindings.wfs.literal import Literal

__NAMESPACE__ = "http://www.opengis.net/fes/2.0"


@dataclass
class FunctionType:
    literal: List[Literal] = field(
        default_factory=list,
        metadata={
            "name": "Literal",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
        }
    )
    function: List["Function"] = field(
        default_factory=list,
        metadata={
            "name": "Function",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
        }
    )
    value_reference: List[str] = field(
        default_factory=list,
        metadata={
            "name": "ValueReference",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
        }
    )
    expression: List[Expression] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class Function(FunctionType):
    class Meta:
        namespace = "http://www.opengis.net/fes/2.0"
