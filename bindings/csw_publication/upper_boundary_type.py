from dataclasses import dataclass, field
from typing import Optional
from bindings.csw_publication.expression import Expression
from bindings.csw_publication.function_type import (
    Add,
    Div,
    Function,
    Mul,
    Sub,
)
from bindings.csw_publication.literal import Literal
from bindings.csw_publication.property_name import PropertyName

__NAMESPACE__ = "http://www.opengis.net/ogc"


@dataclass
class UpperBoundaryType:
    literal: Optional[Literal] = field(
        default=None,
        metadata={
            "name": "Literal",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        }
    )
    function: Optional[Function] = field(
        default=None,
        metadata={
            "name": "Function",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        }
    )
    property_name: Optional[PropertyName] = field(
        default=None,
        metadata={
            "name": "PropertyName",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        }
    )
    div: Optional[Div] = field(
        default=None,
        metadata={
            "name": "Div",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        }
    )
    mul: Optional[Mul] = field(
        default=None,
        metadata={
            "name": "Mul",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        }
    )
    sub: Optional[Sub] = field(
        default=None,
        metadata={
            "name": "Sub",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        }
    )
    add: Optional[Add] = field(
        default=None,
        metadata={
            "name": "Add",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        }
    )
    expression: Optional[Expression] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        }
    )
