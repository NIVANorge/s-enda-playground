from dataclasses import dataclass, field
from typing import List, Optional
from bindings.wfs.abstract_adhoc_query_expression import AbstractAdhocQueryExpression
from bindings.wfs.abstract_query_expression import AbstractQueryExpression
from bindings.wfs.all_some_type import AllSomeType
from bindings.wfs.base_request_type import BaseRequestType
from bindings.wfs.query import Query
from bindings.wfs.stored_query import StoredQuery

__NAMESPACE__ = "http://www.opengis.net/wfs/2.0"


@dataclass
class LockFeatureType(BaseRequestType):
    stored_query: List[StoredQuery] = field(
        default_factory=list,
        metadata={
            "name": "StoredQuery",
            "type": "Element",
            "namespace": "http://www.opengis.net/wfs/2.0",
        }
    )
    query: List[Query] = field(
        default_factory=list,
        metadata={
            "name": "Query",
            "type": "Element",
            "namespace": "http://www.opengis.net/wfs/2.0",
        }
    )
    abstract_adhoc_query_expression: List[AbstractAdhocQueryExpression] = field(
        default_factory=list,
        metadata={
            "name": "AbstractAdhocQueryExpression",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
        }
    )
    abstract_query_expression: List[AbstractQueryExpression] = field(
        default_factory=list,
        metadata={
            "name": "AbstractQueryExpression",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
        }
    )
    lock_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "lockId",
            "type": "Attribute",
        }
    )
    expiry: int = field(
        default=300,
        metadata={
            "type": "Attribute",
        }
    )
    lock_action: AllSomeType = field(
        default=AllSomeType.ALL,
        metadata={
            "name": "lockAction",
            "type": "Attribute",
        }
    )
