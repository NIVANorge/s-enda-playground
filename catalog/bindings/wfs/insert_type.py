from dataclasses import dataclass, field
from typing import List, Optional
from bindings.wfs.abstract_transaction_action_type import AbstractTransactionActionType

__NAMESPACE__ = "http://www.opengis.net/wfs/2.0"


@dataclass
class InsertType(AbstractTransactionActionType):
    other_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
        },
    )
    input_format: str = field(
        default="application/gml+xml; version=3.2",
        metadata={
            "name": "inputFormat",
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
