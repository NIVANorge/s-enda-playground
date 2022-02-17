from dataclasses import dataclass
from bindings.wfs.create_stored_query_response_type import CreateStoredQueryResponseType

__NAMESPACE__ = "http://www.opengis.net/wfs/2.0"


@dataclass
class CreateStoredQueryResponse(CreateStoredQueryResponseType):
    class Meta:
        namespace = "http://www.opengis.net/wfs/2.0"
