from dataclasses import dataclass, field
from typing import List
from bindings.wfs.stored_query_description_type import StoredQueryDescriptionType

__NAMESPACE__ = "http://www.opengis.net/wfs/2.0"


@dataclass
class DescribeStoredQueriesResponseType:
    stored_query_description: List[StoredQueryDescriptionType] = field(
        default_factory=list,
        metadata={
            "name": "StoredQueryDescription",
            "type": "Element",
            "namespace": "http://www.opengis.net/wfs/2.0",
        }
    )
