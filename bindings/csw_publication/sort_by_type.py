from dataclasses import dataclass, field
from typing import List
from bindings.csw_publication.sort_property_type import SortPropertyType

__NAMESPACE__ = "http://www.opengis.net/ogc"


@dataclass
class SortByType:
    sort_property: List[SortPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "SortProperty",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
            "min_occurs": 1,
        }
    )
