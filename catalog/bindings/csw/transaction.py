from dataclasses import dataclass
from bindings.csw.transaction_type import TransactionType

__NAMESPACE__ = "http://www.opengis.net/cat/csw/2.0.2"


@dataclass
class Transaction(TransactionType):
    class Meta:
        namespace = "http://www.opengis.net/cat/csw/2.0.2"
