from dataclasses import dataclass
from bindings.csw_publication.expression_type import ExpressionType

__NAMESPACE__ = "http://www.opengis.net/ogc"


@dataclass
class Expression(ExpressionType):
    class Meta:
        name = "expression"
        namespace = "http://www.opengis.net/ogc"
