from dataclasses import dataclass, field
from typing import Optional
from bindings.csw_publication.property_name import PropertyName
from bindings.csw_publication.sort_order_type import SortOrderType

__NAMESPACE__ = "http://www.opengis.net/ogc"


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
