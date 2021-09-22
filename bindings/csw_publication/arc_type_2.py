from dataclasses import dataclass, field
from typing import List, Optional
from bindings.csw_publication.actuate_type import ActuateType
from bindings.csw_publication.show_type import ShowType
from bindings.csw_publication.title_3 import Title3
from bindings.csw_publication.type_type import TypeType

__NAMESPACE__ = "http://www.w3.org/1999/xlink"


@dataclass
class ArcType2:
    """
    :ivar title:
    :ivar type:
    :ivar arcrole:
    :ivar title_attribute:
    :ivar show:
    :ivar actuate:
    :ivar from_value:
    :ivar to: from and to have default behavior when values are missing
    """
    class Meta:
        name = "arcType"

    title: List[Title3] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    type: TypeType = field(
        init=False,
        default=TypeType.ARC,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "required": True,
        }
    )
    arcrole: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        }
    )
    title_attribute: Optional[str] = field(
        default=None,
        metadata={
            "name": "title",
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    show: Optional[ShowType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    actuate: Optional[ActuateType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    from_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "from",
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    to: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
