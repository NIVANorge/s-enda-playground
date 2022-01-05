from dataclasses import dataclass
from bindings.wfs.describe_stored_queries_response_type import DescribeStoredQueriesResponseType

__NAMESPACE__ = "http://www.opengis.net/wfs/2.0"


@dataclass
class DescribeStoredQueriesResponse(DescribeStoredQueriesResponseType):
    class Meta:
        namespace = "http://www.opengis.net/wfs/2.0"
