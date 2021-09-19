from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "http://www.opengis.net/cat/csw/2.0.2"


@dataclass
class InsertType:
    """Submits one or more records to the catalogue.

    The representation is defined by the application profile. The handle
    attribute may be included to specify a local identifier for the
    action (it must be unique within the context of the transaction).
    """
    other_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
        }
    )
    type_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "typeName",
            "type": "Attribute",
        }
    )
    handle: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
