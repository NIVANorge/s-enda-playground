from dataclasses import dataclass, field
from typing import Optional
from bindings.csw_publication.compass_point_enumeration import CompassPointEnumeration

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class CompassPoint:
    class Meta:
        namespace = "http://www.opengis.net/gml"

    value: Optional[CompassPointEnumeration] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
