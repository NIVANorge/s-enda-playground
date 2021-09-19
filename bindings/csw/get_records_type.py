from dataclasses import dataclass, field
from typing import List, Optional
from bindings.csw.abstract_query import AbstractQuery
from bindings.csw.distributed_search_type import DistributedSearchType
from bindings.csw.query import Query
from bindings.csw.request_base_type import RequestBaseType
from bindings.csw.result_type import ResultType

__NAMESPACE__ = "http://www.opengis.net/cat/csw/2.0.2"


@dataclass
class GetRecordsType(RequestBaseType):
    """The principal means of searching the catalogue.

    The matching catalogue entries may be included with the response.
    The client may assign a requestId (absolute URI). A distributed
    search is performed if the DistributedSearch element is present and
    the catalogue is a member of a federation. Profiles may allow
    alternative query expressions.
    """
    distributed_search: Optional[DistributedSearchType] = field(
        default=None,
        metadata={
            "name": "DistributedSearch",
            "type": "Element",
            "namespace": "http://www.opengis.net/cat/csw/2.0.2",
        }
    )
    response_handler: List[str] = field(
        default_factory=list,
        metadata={
            "name": "ResponseHandler",
            "type": "Element",
            "namespace": "http://www.opengis.net/cat/csw/2.0.2",
        }
    )
    query: Optional[Query] = field(
        default=None,
        metadata={
            "name": "Query",
            "type": "Element",
            "namespace": "http://www.opengis.net/cat/csw/2.0.2",
        }
    )
    abstract_query: Optional[AbstractQuery] = field(
        default=None,
        metadata={
            "name": "AbstractQuery",
            "type": "Element",
            "namespace": "http://www.opengis.net/cat/csw/2.0.2",
        }
    )
    other_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
        }
    )
    request_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "requestId",
            "type": "Attribute",
        }
    )
    result_type: ResultType = field(
        default=ResultType.HITS,
        metadata={
            "name": "resultType",
            "type": "Attribute",
        }
    )
    output_format: str = field(
        default="application/xml",
        metadata={
            "name": "outputFormat",
            "type": "Attribute",
        }
    )
    output_schema: Optional[str] = field(
        default=None,
        metadata={
            "name": "outputSchema",
            "type": "Attribute",
        }
    )
    start_position: int = field(
        default=1,
        metadata={
            "name": "startPosition",
            "type": "Attribute",
        }
    )
    max_records: int = field(
        default=10,
        metadata={
            "name": "maxRecords",
            "type": "Attribute",
        }
    )
