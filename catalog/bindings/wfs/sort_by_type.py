from dataclasses import dataclass, field
from typing import List
from bindings.wfs.sort_property_type import SortPropertyType

__NAMESPACE__ = "http://www.opengis.net/fes/2.0"


@dataclass
class SortByType:
    sort_property: List[SortPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "SortProperty",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
            "min_occurs": 1,
        }
    )
