from dataclasses import dataclass, field
from typing import List, Optional
from bindings.wfs.comparison_ops_type import ComparisonOpsType
from bindings.wfs.expression import Expression
from bindings.wfs.function_type import Function
from bindings.wfs.literal import Literal

__NAMESPACE__ = "http://www.opengis.net/fes/2.0"


@dataclass
class PropertyIsLikeType(ComparisonOpsType):
    literal: List[Literal] = field(
        default_factory=list,
        metadata={
            "name": "Literal",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
            "max_occurs": 2,
        }
    )
    function: List[Function] = field(
        default_factory=list,
        metadata={
            "name": "Function",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
            "max_occurs": 2,
        }
    )
    value_reference: List[str] = field(
        default_factory=list,
        metadata={
            "name": "ValueReference",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
            "max_occurs": 2,
        }
    )
    expression: List[Expression] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
            "max_occurs": 2,
        }
    )
    wild_card: Optional[str] = field(
        default=None,
        metadata={
            "name": "wildCard",
            "type": "Attribute",
            "required": True,
        }
    )
    single_char: Optional[str] = field(
        default=None,
        metadata={
            "name": "singleChar",
            "type": "Attribute",
            "required": True,
        }
    )
    escape_char: Optional[str] = field(
        default=None,
        metadata={
            "name": "escapeChar",
            "type": "Attribute",
            "required": True,
        }
    )
    match_case: bool = field(
        default=True,
        metadata={
            "name": "matchCase",
            "type": "Attribute",
        }
    )
