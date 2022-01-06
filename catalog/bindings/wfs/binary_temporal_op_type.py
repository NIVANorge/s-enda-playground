from dataclasses import dataclass, field
from typing import List
from bindings.wfs.expression import Expression
from bindings.wfs.function_type import Function
from bindings.wfs.literal import Literal
from bindings.wfs.temporal_ops_type import TemporalOpsType

__NAMESPACE__ = "http://www.opengis.net/fes/2.0"


@dataclass
class BinaryTemporalOpType(TemporalOpsType):
    literal: List[Literal] = field(
        default_factory=list,
        metadata={
            "name": "Literal",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
            "max_occurs": 2,
        },
    )
    function: List[Function] = field(
        default_factory=list,
        metadata={
            "name": "Function",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
            "max_occurs": 2,
        },
    )
    value_reference: List[str] = field(
        default_factory=list,
        metadata={
            "name": "ValueReference",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
            "max_occurs": 2,
        },
    )
    expression: List[Expression] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
            "max_occurs": 2,
        },
    )
    other_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
            "max_occurs": 2,
        },
    )
