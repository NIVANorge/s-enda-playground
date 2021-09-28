from dataclasses import dataclass
from bindings.wfs.transaction_response_type import TransactionResponseType

__NAMESPACE__ = "http://www.opengis.net/wfs/2.0"


@dataclass
class TransactionResponse(TransactionResponseType):
    class Meta:
        namespace = "http://www.opengis.net/wfs/2.0"
