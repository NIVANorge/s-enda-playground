from dataclasses import dataclass, field
from typing import List, Optional
from bindings.csw.expression import Expression
from bindings.csw.expression_type import ExpressionType
from bindings.csw.literal import Literal
from bindings.csw.property_name import PropertyName

__NAMESPACE__ = "http://www.opengis.net/ogc"


@dataclass
class FunctionType(ExpressionType):
    literal: List[Literal] = field(
        default_factory=list,
        metadata={
            "name": "Literal",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        },
    )
    function: List["Function"] = field(
        default_factory=list,
        metadata={
            "name": "Function",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        },
    )
    property_name: List[PropertyName] = field(
        default_factory=list,
        metadata={
            "name": "PropertyName",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        },
    )
    div: List["Div"] = field(
        default_factory=list,
        metadata={
            "name": "Div",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        },
    )
    mul: List["Mul"] = field(
        default_factory=list,
        metadata={
            "name": "Mul",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        },
    )
    sub: List["Sub"] = field(
        default_factory=list,
        metadata={
            "name": "Sub",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        },
    )
    add: List["Add"] = field(
        default_factory=list,
        metadata={
            "name": "Add",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        },
    )
    expression: List[Expression] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class Function(FunctionType):
    class Meta:
        namespace = "http://www.opengis.net/ogc"


@dataclass
class BinaryOperatorType(ExpressionType):
    literal: List[Literal] = field(
        default_factory=list,
        metadata={
            "name": "Literal",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
            "max_occurs": 2,
        },
    )
    function: List[Function] = field(
        default_factory=list,
        metadata={
            "name": "Function",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
            "max_occurs": 2,
        },
    )
    property_name: List[PropertyName] = field(
        default_factory=list,
        metadata={
            "name": "PropertyName",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
            "max_occurs": 2,
        },
    )
    div: List["Div"] = field(
        default_factory=list,
        metadata={
            "name": "Div",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
            "max_occurs": 2,
        },
    )
    mul: List["Mul"] = field(
        default_factory=list,
        metadata={
            "name": "Mul",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
            "max_occurs": 2,
        },
    )
    sub: List["Sub"] = field(
        default_factory=list,
        metadata={
            "name": "Sub",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
            "max_occurs": 2,
        },
    )
    add: List["Add"] = field(
        default_factory=list,
        metadata={
            "name": "Add",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
            "max_occurs": 2,
        },
    )
    expression: List[Expression] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
            "max_occurs": 2,
        },
    )


@dataclass
class Add(BinaryOperatorType):
    class Meta:
        namespace = "http://www.opengis.net/ogc"


@dataclass
class Div(BinaryOperatorType):
    class Meta:
        namespace = "http://www.opengis.net/ogc"


@dataclass
class Mul(BinaryOperatorType):
    class Meta:
        namespace = "http://www.opengis.net/ogc"


@dataclass
class Sub(BinaryOperatorType):
    class Meta:
        namespace = "http://www.opengis.net/ogc"
