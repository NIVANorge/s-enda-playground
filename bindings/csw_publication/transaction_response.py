from dataclasses import dataclass
from bindings.csw_publication.transaction_response_type import TransactionResponseType

__NAMESPACE__ = "http://www.opengis.net/cat/csw/2.0.2"


@dataclass
class TransactionResponse(TransactionResponseType):
    class Meta:
        namespace = "http://www.opengis.net/cat/csw/2.0.2"
