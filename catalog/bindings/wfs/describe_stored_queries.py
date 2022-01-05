from dataclasses import dataclass
from bindings.wfs.describe_stored_queries_type import DescribeStoredQueriesType

__NAMESPACE__ = "http://www.opengis.net/wfs/2.0"


@dataclass
class DescribeStoredQueries(DescribeStoredQueriesType):
    class Meta:
        namespace = "http://www.opengis.net/wfs/2.0"
