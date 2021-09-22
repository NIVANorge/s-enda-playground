from dataclasses import dataclass, field
from typing import List, Optional
from bindings.csw_publication.insert_result_type import InsertResultType
from bindings.csw_publication.transaction_summary_type import TransactionSummaryType

__NAMESPACE__ = "http://www.opengis.net/cat/csw/2.0.2"


@dataclass
class TransactionResponseType:
    """The response for a transaction request that was successfully completed.

    If the transaction failed for any reason, a service exception report
    indicating a TransactionFailure is returned instead.
    """
    transaction_summary: Optional[TransactionSummaryType] = field(
        default=None,
        metadata={
            "name": "TransactionSummary",
            "type": "Element",
            "namespace": "http://www.opengis.net/cat/csw/2.0.2",
            "required": True,
        }
    )
    insert_result: List[InsertResultType] = field(
        default_factory=list,
        metadata={
            "name": "InsertResult",
            "type": "Element",
            "namespace": "http://www.opengis.net/cat/csw/2.0.2",
        }
    )
    version: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
