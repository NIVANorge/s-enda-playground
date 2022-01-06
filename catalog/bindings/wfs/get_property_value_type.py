from dataclasses import dataclass, field
from typing import Optional, Union
from bindings.wfs.abstract_adhoc_query_expression import AbstractAdhocQueryExpression
from bindings.wfs.abstract_query_expression import AbstractQueryExpression
from bindings.wfs.base_request_type import BaseRequestType
from bindings.wfs.query import Query
from bindings.wfs.resolve_value_type import ResolveValueType
from bindings.wfs.result_type_type import ResultTypeType
from bindings.wfs.star_string_type import StarStringType
from bindings.wfs.stored_query import StoredQuery

__NAMESPACE__ = "http://www.opengis.net/wfs/2.0"


@dataclass
class GetPropertyValueType(BaseRequestType):
    stored_query: Optional[StoredQuery] = field(
        default=None,
        metadata={
            "name": "StoredQuery",
            "type": "Element",
            "namespace": "http://www.opengis.net/wfs/2.0",
        },
    )
    query: Optional[Query] = field(
        default=None,
        metadata={
            "name": "Query",
            "type": "Element",
            "namespace": "http://www.opengis.net/wfs/2.0",
        },
    )
    abstract_adhoc_query_expression: Optional[AbstractAdhocQueryExpression] = field(
        default=None,
        metadata={
            "name": "AbstractAdhocQueryExpression",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
        },
    )
    abstract_query_expression: Optional[AbstractQueryExpression] = field(
        default=None,
        metadata={
            "name": "AbstractQueryExpression",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
        },
    )
    value_reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "valueReference",
            "type": "Attribute",
            "required": True,
        },
    )
    resolve_path: Optional[str] = field(
        default=None,
        metadata={
            "name": "resolvePath",
            "type": "Attribute",
        },
    )
    start_index: int = field(
        default=0,
        metadata={
            "name": "startIndex",
            "type": "Attribute",
        },
    )
    count: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    result_type: ResultTypeType = field(
        default=ResultTypeType.RESULTS,
        metadata={
            "name": "resultType",
            "type": "Attribute",
        },
    )
    output_format: str = field(
        default="application/gml+xml; version=3.2",
        metadata={
            "name": "outputFormat",
            "type": "Attribute",
        },
    )
    resolve: ResolveValueType = field(
        default=ResolveValueType.NONE,
        metadata={
            "type": "Attribute",
        },
    )
    resolve_depth: Union[int, StarStringType] = field(
        default=StarStringType.VALUE,
        metadata={
            "name": "resolveDepth",
            "type": "Attribute",
        },
    )
    resolve_timeout: int = field(
        default=300,
        metadata={
            "name": "resolveTimeout",
            "type": "Attribute",
        },
    )
