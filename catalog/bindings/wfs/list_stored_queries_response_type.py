from dataclasses import dataclass, field
from typing import List
from bindings.wfs.stored_query_list_item_type import StoredQueryListItemType

__NAMESPACE__ = "http://www.opengis.net/wfs/2.0"


@dataclass
class ListStoredQueriesResponseType:
    stored_query: List[StoredQueryListItemType] = field(
        default_factory=list,
        metadata={
            "name": "StoredQuery",
            "type": "Element",
            "namespace": "http://www.opengis.net/wfs/2.0",
        }
    )
