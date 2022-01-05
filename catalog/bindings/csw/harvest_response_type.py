from dataclasses import dataclass, field
from typing import Optional
from bindings.csw.acknowledgement import Acknowledgement
from bindings.csw.transaction_response import TransactionResponse

__NAMESPACE__ = "http://www.opengis.net/cat/csw/2.0.2"


@dataclass
class HarvestResponseType:
    acknowledgement: Optional[Acknowledgement] = field(
        default=None,
        metadata={
            "name": "Acknowledgement",
            "type": "Element",
            "namespace": "http://www.opengis.net/cat/csw/2.0.2",
        }
    )
    transaction_response: Optional[TransactionResponse] = field(
        default=None,
        metadata={
            "name": "TransactionResponse",
            "type": "Element",
            "namespace": "http://www.opengis.net/cat/csw/2.0.2",
        }
    )
