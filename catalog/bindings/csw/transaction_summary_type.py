from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.opengis.net/cat/csw/2.0.2"


@dataclass
class TransactionSummaryType:
    """Reports the total number of catalogue items modified by a transaction
    request (i.e, inserted, updated, deleted).

    If the client did not specify a requestId, the server may assign one
    (a URI value).
    """

    total_inserted: Optional[int] = field(
        default=None,
        metadata={
            "name": "totalInserted",
            "type": "Element",
            "namespace": "http://www.opengis.net/cat/csw/2.0.2",
        },
    )
    total_updated: Optional[int] = field(
        default=None,
        metadata={
            "name": "totalUpdated",
            "type": "Element",
            "namespace": "http://www.opengis.net/cat/csw/2.0.2",
        },
    )
    total_deleted: Optional[int] = field(
        default=None,
        metadata={
            "name": "totalDeleted",
            "type": "Element",
            "namespace": "http://www.opengis.net/cat/csw/2.0.2",
        },
    )
    request_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "requestId",
            "type": "Attribute",
        },
    )
