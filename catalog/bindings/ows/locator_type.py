from dataclasses import dataclass, field
from typing import List, Optional
from bindings.ows.title_2 import Title2
from bindings.ows.type_type import TypeType

__NAMESPACE__ = "http://www.w3.org/1999/xlink"


@dataclass
class LocatorType:
    """
    :ivar title:
    :ivar type:
    :ivar href:
    :ivar role:
    :ivar title_attribute:
    :ivar label: label is not required, but locators have no particular
        XLink function if they are not labeled.
    """

    class Meta:
        name = "locatorType"

    title: List[Title2] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    type: TypeType = field(
        init=False,
        default=TypeType.LOCATOR,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "required": True,
        },
    )
    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "required": True,
        },
    )
    role: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        },
    )
    title_attribute: Optional[str] = field(
        default=None,
        metadata={
            "name": "title",
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    label: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
