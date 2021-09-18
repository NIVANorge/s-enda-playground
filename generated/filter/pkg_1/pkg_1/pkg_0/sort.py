from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional
from generated.filter.pkg_1.pkg_1.pkg_0.expr import PropertyName

__NAMESPACE__ = "http://www.opengis.net/ogc"


class SortOrderType(Enum):
    DESC = "DESC"
    ASC = "ASC"


@dataclass
class SortPropertyType:
    property_name: Optional[PropertyName] = field(
        default=None,
        metadata={
            "name": "PropertyName",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
            "required": True,
        }
    )
    sort_order: Optional[SortOrderType] = field(
        default=None,
        metadata={
            "name": "SortOrder",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        }
    )


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


@dataclass
class SortBy(SortByType):
    class Meta:
        namespace = "http://www.opengis.net/ogc"
