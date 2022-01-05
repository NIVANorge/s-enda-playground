from dataclasses import dataclass, field
from typing import List, Optional
from xml.etree.ElementTree import QName
from bindings.wfs.title_2 import Title2

__NAMESPACE__ = "http://www.opengis.net/wfs/2.0"


@dataclass
class StoredQueryListItemType:
    title: List[Title2] = field(
        default_factory=list,
        metadata={
            "name": "Title",
            "type": "Element",
            "namespace": "http://www.opengis.net/wfs/2.0",
        }
    )
    return_feature_type: List[QName] = field(
        default_factory=list,
        metadata={
            "name": "ReturnFeatureType",
            "type": "Element",
            "namespace": "http://www.opengis.net/wfs/2.0",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
