from dataclasses import dataclass, field
from typing import List, Optional
from bindings.csw.arc_2 import Arc2
from bindings.csw.locator import Locator
from bindings.csw.resource import Resource
from bindings.csw.title_2 import Title2
from bindings.csw.type_type import TypeType

__NAMESPACE__ = "http://www.w3.org/1999/xlink"


@dataclass
class Extended:
    """Intended for use as the type of user-declared elements to make them
    extended links.

    Note that the elements referenced in the content model are all
    abstract. The intention is that by simply declaring elements with
    these as their substitutionGroup, all the right things will happen.
    """

    class Meta:
        name = "extended"

    title: List[Title2] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    resource: List[Resource] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    locator: List[Locator] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    arc: List[Arc2] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    type: TypeType = field(
        init=False,
        default=TypeType.EXTENDED,
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
