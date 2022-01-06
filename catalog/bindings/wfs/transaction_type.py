from dataclasses import dataclass, field
from typing import List, Optional
from bindings.wfs.abstract_transaction_action import AbstractTransactionAction
from bindings.wfs.all_some_type import AllSomeType
from bindings.wfs.base_request_type import BaseRequestType
from bindings.wfs.delete import Delete
from bindings.wfs.insert import Insert
from bindings.wfs.native import Native
from bindings.wfs.replace import Replace
from bindings.wfs.update import Update

__NAMESPACE__ = "http://www.opengis.net/wfs/2.0"


@dataclass
class TransactionType(BaseRequestType):
    native: List[Native] = field(
        default_factory=list,
        metadata={
            "name": "Native",
            "type": "Element",
            "namespace": "http://www.opengis.net/wfs/2.0",
            "sequential": True,
        },
    )
    delete: List[Delete] = field(
        default_factory=list,
        metadata={
            "name": "Delete",
            "type": "Element",
            "namespace": "http://www.opengis.net/wfs/2.0",
            "sequential": True,
        },
    )
    replace: List[Replace] = field(
        default_factory=list,
        metadata={
            "name": "Replace",
            "type": "Element",
            "namespace": "http://www.opengis.net/wfs/2.0",
            "sequential": True,
        },
    )
    update: List[Update] = field(
        default_factory=list,
        metadata={
            "name": "Update",
            "type": "Element",
            "namespace": "http://www.opengis.net/wfs/2.0",
            "sequential": True,
        },
    )
    insert: List[Insert] = field(
        default_factory=list,
        metadata={
            "name": "Insert",
            "type": "Element",
            "namespace": "http://www.opengis.net/wfs/2.0",
            "sequential": True,
        },
    )
    abstract_transaction_action: List[AbstractTransactionAction] = field(
        default_factory=list,
        metadata={
            "name": "AbstractTransactionAction",
            "type": "Element",
            "namespace": "http://www.opengis.net/wfs/2.0",
            "sequential": True,
        },
    )
    lock_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "lockId",
            "type": "Attribute",
        },
    )
    release_action: AllSomeType = field(
        default=AllSomeType.ALL,
        metadata={
            "name": "releaseAction",
            "type": "Attribute",
        },
    )
    srs_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "srsName",
            "type": "Attribute",
        },
    )
