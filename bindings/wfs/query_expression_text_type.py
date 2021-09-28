from dataclasses import dataclass, field
from typing import List, Optional
from xml.etree.ElementTree import QName

__NAMESPACE__ = "http://www.opengis.net/wfs/2.0"


@dataclass
class QueryExpressionTextType:
    return_feature_types: List[QName] = field(
        default_factory=list,
        metadata={
            "name": "returnFeatureTypes",
            "type": "Attribute",
            "required": True,
            "tokens": True,
        }
    )
    language: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    is_private: bool = field(
        default=False,
        metadata={
            "name": "isPrivate",
            "type": "Attribute",
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
