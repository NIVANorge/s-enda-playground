from dataclasses import dataclass, field
from typing import List, Optional
from bindings.csw.delete_type import DeleteType
from bindings.csw.insert_type import InsertType
from bindings.csw.request_base_type import RequestBaseType
from bindings.csw.update_type import UpdateType

__NAMESPACE__ = "http://www.opengis.net/cat/csw/2.0.2"


@dataclass
class TransactionType(RequestBaseType):
    """Users may insert, update, or delete catalogue entries.

    If the verboseResponse attribute has the value "true", then one or
    more csw:InsertResult elements must be included in the response.
    """
    insert: List[InsertType] = field(
        default_factory=list,
        metadata={
            "name": "Insert",
            "type": "Element",
            "namespace": "http://www.opengis.net/cat/csw/2.0.2",
            "sequential": True,
        }
    )
    update: List[UpdateType] = field(
        default_factory=list,
        metadata={
            "name": "Update",
            "type": "Element",
            "namespace": "http://www.opengis.net/cat/csw/2.0.2",
            "sequential": True,
        }
    )
    delete: List[DeleteType] = field(
        default_factory=list,
        metadata={
            "name": "Delete",
            "type": "Element",
            "namespace": "http://www.opengis.net/cat/csw/2.0.2",
            "sequential": True,
        }
    )
    verbose_response: bool = field(
        default=False,
        metadata={
            "name": "verboseResponse",
            "type": "Attribute",
        }
    )
    request_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "requestId",
            "type": "Attribute",
        }
    )
