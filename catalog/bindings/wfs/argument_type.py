from dataclasses import dataclass, field
from typing import Optional
from xml.etree.ElementTree import QName
from bindings.wfs.metadata import Metadata

__NAMESPACE__ = "http://www.opengis.net/fes/2.0"


@dataclass
class ArgumentType:
    metadata: Optional[Metadata] = field(
        default=None,
        metadata={
            "name": "Metadata",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows/1.1",
        },
    )
    type: Optional[QName] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
            "required": True,
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
