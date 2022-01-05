from dataclasses import dataclass
from bindings.wfs.list_stored_queries_response_type import ListStoredQueriesResponseType

__NAMESPACE__ = "http://www.opengis.net/wfs/2.0"


@dataclass
class ListStoredQueriesResponse(ListStoredQueriesResponseType):
    class Meta:
        namespace = "http://www.opengis.net/wfs/2.0"
