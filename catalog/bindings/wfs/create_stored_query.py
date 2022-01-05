from dataclasses import dataclass
from bindings.wfs.create_stored_query_type import CreateStoredQueryType

__NAMESPACE__ = "http://www.opengis.net/wfs/2.0"


@dataclass
class CreateStoredQuery(CreateStoredQueryType):
    class Meta:
        namespace = "http://www.opengis.net/wfs/2.0"
