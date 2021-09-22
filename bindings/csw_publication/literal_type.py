from dataclasses import dataclass, field
from typing import List
from bindings.csw_publication.expression_type import ExpressionType

__NAMESPACE__ = "http://www.opengis.net/ogc"


@dataclass
class LiteralType(ExpressionType):
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
