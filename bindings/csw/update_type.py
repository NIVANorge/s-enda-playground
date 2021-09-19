from dataclasses import dataclass, field
from typing import List, Optional
from bindings.csw.constraint import Constraint
from bindings.csw.record_property import RecordProperty

__NAMESPACE__ = "http://www.opengis.net/cat/csw/2.0.2"


@dataclass
class UpdateType:
    """Update statements may replace an entire record or only update part of a
    record:

    1) To replace an existing record, include a new instance of the
    record; 2) To update selected properties of an existing record,
    include a set of RecordProperty elements. The scope of the update
    statement  is determined by the Constraint element. The 'handle' is
    a local identifier for the action.
    """
    other_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
        }
    )
    record_property: List[RecordProperty] = field(
        default_factory=list,
        metadata={
            "name": "RecordProperty",
            "type": "Element",
            "namespace": "http://www.opengis.net/cat/csw/2.0.2",
        }
    )
    constraint: Optional[Constraint] = field(
        default=None,
        metadata={
            "name": "Constraint",
            "type": "Element",
            "namespace": "http://www.opengis.net/cat/csw/2.0.2",
        }
    )
    handle: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
