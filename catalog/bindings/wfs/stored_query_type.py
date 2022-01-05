from dataclasses import dataclass, field
from typing import List, Optional
from bindings.wfs.abstract_query_expression_type import AbstractQueryExpressionType
from bindings.wfs.parameter_type import ParameterType

__NAMESPACE__ = "http://www.opengis.net/wfs/2.0"


@dataclass
class StoredQueryType(AbstractQueryExpressionType):
    parameter: List[ParameterType] = field(
        default_factory=list,
        metadata={
            "name": "Parameter",
            "type": "Element",
            "namespace": "http://www.opengis.net/wfs/2.0",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
