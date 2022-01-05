from dataclasses import dataclass
from bindings.wfs.query_type import QueryType

__NAMESPACE__ = "http://www.opengis.net/wfs/2.0"


@dataclass
class Query(QueryType):
    class Meta:
        namespace = "http://www.opengis.net/wfs/2.0"
