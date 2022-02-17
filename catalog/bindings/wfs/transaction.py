from dataclasses import dataclass
from bindings.wfs.transaction_type import TransactionType

__NAMESPACE__ = "http://www.opengis.net/wfs/2.0"


@dataclass
class Transaction(TransactionType):
    class Meta:
        namespace = "http://www.opengis.net/wfs/2.0"
