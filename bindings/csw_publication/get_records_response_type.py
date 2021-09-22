from dataclasses import dataclass, field
from typing import Optional
from bindings.csw_publication.request_status_type import RequestStatusType
from bindings.csw_publication.search_results_type import SearchResultsType

__NAMESPACE__ = "http://www.opengis.net/cat/csw/2.0.2"


@dataclass
class GetRecordsResponseType:
    """The response message for a GetRecords request.

    Some or all of the matching records may be included as children of
    the SearchResults element. The RequestId is only included if the
    client specified it.
    """
    request_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "RequestId",
            "type": "Element",
            "namespace": "http://www.opengis.net/cat/csw/2.0.2",
        }
    )
    search_status: Optional[RequestStatusType] = field(
        default=None,
        metadata={
            "name": "SearchStatus",
            "type": "Element",
            "namespace": "http://www.opengis.net/cat/csw/2.0.2",
            "required": True,
        }
    )
    search_results: Optional[SearchResultsType] = field(
        default=None,
        metadata={
            "name": "SearchResults",
            "type": "Element",
            "namespace": "http://www.opengis.net/cat/csw/2.0.2",
            "required": True,
        }
    )
    version: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
