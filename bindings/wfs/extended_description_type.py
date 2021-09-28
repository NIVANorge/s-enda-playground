from dataclasses import dataclass, field
from typing import List
from bindings.wfs.element import Element

__NAMESPACE__ = "http://www.opengis.net/wfs/2.0"


@dataclass
class ExtendedDescriptionType:
    element: List[Element] = field(
        default_factory=list,
        metadata={
            "name": "Element",
            "type": "Element",
            "namespace": "http://www.opengis.net/wfs/2.0",
            "min_occurs": 1,
        }
    )
