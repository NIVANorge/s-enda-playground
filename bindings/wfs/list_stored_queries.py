from dataclasses import dataclass
from bindings.wfs.list_stored_queries_type import ListStoredQueriesType

__NAMESPACE__ = "http://www.opengis.net/wfs/2.0"


@dataclass
class ListStoredQueries(ListStoredQueriesType):
    class Meta:
        namespace = "http://www.opengis.net/wfs/2.0"
