from dataclasses import dataclass, field
from typing import Optional, Union
from xml.etree.ElementTree import QName
from bindings.wfs.resolve_value_type import ResolveValueType
from bindings.wfs.star_string_type import StarStringType

__NAMESPACE__ = "http://www.opengis.net/wfs/2.0"


@dataclass
class PropertyName:
    class Meta:
        namespace = "http://www.opengis.net/wfs/2.0"

    value: Optional[QName] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    resolve: ResolveValueType = field(
        default=ResolveValueType.NONE,
        metadata={
            "type": "Attribute",
        }
    )
    resolve_depth: Union[int, StarStringType] = field(
        default=StarStringType.VALUE,
        metadata={
            "name": "resolveDepth",
            "type": "Attribute",
        }
    )
    resolve_timeout: int = field(
        default=300,
        metadata={
            "name": "resolveTimeout",
            "type": "Attribute",
        }
    )
    resolve_path: Optional[str] = field(
        default=None,
        metadata={
            "name": "resolvePath",
            "type": "Attribute",
        }
    )
