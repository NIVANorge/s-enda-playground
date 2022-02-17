from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.opengis.net/cat/csw/2.0.2"


@dataclass
class RecordPropertyType:
    """
    :ivar name: The Name element contains the name of a property to be
        updated.  The name may be a path expression.
    :ivar value: The Value element contains the replacement value for
        the named property.
    """

    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.opengis.net/cat/csw/2.0.2",
            "required": True,
        },
    )
    value: Optional[object] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
            "namespace": "http://www.opengis.net/cat/csw/2.0.2",
        },
    )
