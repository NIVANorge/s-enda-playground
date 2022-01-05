from dataclasses import dataclass, field
from typing import List
from bindings.csw.comparison_ops_type import ComparisonOpsType
from bindings.csw.expression import Expression
from bindings.csw.function_type import (
    Add,
    Div,
    Function,
    Mul,
    Sub,
)
from bindings.csw.literal import Literal
from bindings.csw.property_name import PropertyName

__NAMESPACE__ = "http://www.opengis.net/ogc"


@dataclass
class BinaryComparisonOpType(ComparisonOpsType):
    literal: List[Literal] = field(
        default_factory=list,
        metadata={
            "name": "Literal",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
            "max_occurs": 2,
        }
    )
    function: List[Function] = field(
        default_factory=list,
        metadata={
            "name": "Function",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
            "max_occurs": 2,
        }
    )
    property_name: List[PropertyName] = field(
        default_factory=list,
        metadata={
            "name": "PropertyName",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
            "max_occurs": 2,
        }
    )
    div: List[Div] = field(
        default_factory=list,
        metadata={
            "name": "Div",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
            "max_occurs": 2,
        }
    )
    mul: List[Mul] = field(
        default_factory=list,
        metadata={
            "name": "Mul",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
            "max_occurs": 2,
        }
    )
    sub: List[Sub] = field(
        default_factory=list,
        metadata={
            "name": "Sub",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
            "max_occurs": 2,
        }
    )
    add: List[Add] = field(
        default_factory=list,
        metadata={
            "name": "Add",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
            "max_occurs": 2,
        }
    )
    expression: List[Expression] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
            "max_occurs": 2,
        }
    )
    match_case: bool = field(
        default=True,
        metadata={
            "name": "matchCase",
            "type": "Attribute",
        }
    )
