from dataclasses import dataclass, field
from typing import List, Optional
from xml.etree.ElementTree import QName
from bindings.csw.element_set_type import ElementSetType

__NAMESPACE__ = "http://www.opengis.net/cat/csw/2.0.2"


@dataclass
class ElementSetNameType:
    value: Optional[ElementSetType] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    type_names: List[QName] = field(
        default_factory=list,
        metadata={
            "name": "typeNames",
            "type": "Attribute",
            "tokens": True,
        }
    )
