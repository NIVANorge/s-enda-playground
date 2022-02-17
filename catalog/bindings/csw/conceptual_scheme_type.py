from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.opengis.net/cat/csw/2.0.2"


@dataclass
class ConceptualSchemeType:
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.opengis.net/cat/csw/2.0.2",
            "required": True,
        },
    )
    document: Optional[str] = field(
        default=None,
        metadata={
            "name": "Document",
            "type": "Element",
            "namespace": "http://www.opengis.net/cat/csw/2.0.2",
            "required": True,
        },
    )
    authority: Optional[str] = field(
        default=None,
        metadata={
            "name": "Authority",
            "type": "Element",
            "namespace": "http://www.opengis.net/cat/csw/2.0.2",
            "required": True,
        },
    )
