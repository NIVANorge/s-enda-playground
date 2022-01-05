from dataclasses import dataclass, field
from typing import Optional
from bindings.wfs.sort_order_type import SortOrderType

__NAMESPACE__ = "http://www.opengis.net/fes/2.0"


@dataclass
class SortPropertyType:
    value_reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "ValueReference",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
            "required": True,
        }
    )
    sort_order: Optional[SortOrderType] = field(
        default=None,
        metadata={
            "name": "SortOrder",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
        }
    )
