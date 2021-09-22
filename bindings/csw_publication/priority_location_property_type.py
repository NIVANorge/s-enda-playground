from dataclasses import dataclass, field
from typing import Optional
from bindings.csw_publication.location_property_type import LocationPropertyType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class PriorityLocationPropertyType(LocationPropertyType):
    """
    G-XML component Deprecated in GML 3.1.0.
    """
    priority: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
