from dataclasses import dataclass
from bindings.wfs.abstract_adhoc_query_expression_type import (
    AbstractAdhocQueryExpressionType,
)

__NAMESPACE__ = "http://www.opengis.net/fes/2.0"


@dataclass
class AbstractAdhocQueryExpression(AbstractAdhocQueryExpressionType):
    class Meta:
        namespace = "http://www.opengis.net/fes/2.0"
