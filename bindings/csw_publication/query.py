from dataclasses import dataclass
from bindings.csw_publication.query_type import QueryType

__NAMESPACE__ = "http://www.opengis.net/cat/csw/2.0.2"


@dataclass
class Query(QueryType):
    class Meta:
        namespace = "http://www.opengis.net/cat/csw/2.0.2"
