from dataclasses import dataclass
from bindings.wfs.abstract_query_expression_type import AbstractQueryExpressionType

__NAMESPACE__ = "http://www.opengis.net/fes/2.0"


@dataclass
class AbstractQueryExpression(AbstractQueryExpressionType):
    class Meta:
        namespace = "http://www.opengis.net/fes/2.0"
