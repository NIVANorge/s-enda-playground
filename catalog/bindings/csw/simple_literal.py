from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "http://purl.org/dc/elements/1.1/"


@dataclass
class SimpleLiteral:
    """This is the default type for all of the DC elements.

    It defines a complexType SimpleLiteral which permits mixed content
    but disallows child elements by use of minOcccurs/maxOccurs.
    However, this complexType does permit the derivation of other types
    which would permit child elements. The scheme attribute may be used
    as a qualifier to reference an encoding scheme that describes the
    value domain for a given property.
    """

    scheme: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )
