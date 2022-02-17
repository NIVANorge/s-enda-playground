from dataclasses import dataclass, field
from typing import List
from bindings.wfs.base_request_type import BaseRequestType

__NAMESPACE__ = "http://www.opengis.net/wfs/2.0"


@dataclass
class DescribeStoredQueriesType(BaseRequestType):
    stored_query_id: List[str] = field(
        default_factory=list,
        metadata={
            "name": "StoredQueryId",
            "type": "Element",
            "namespace": "http://www.opengis.net/wfs/2.0",
        },
    )
