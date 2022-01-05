from dataclasses import dataclass, field
from typing import Optional
from bindings.csw.ring_1 import Ring1

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class RingPropertyType:
    """
    Encapsulates a ring to represent properties in features or geometry
    collections.
    """
    ring: Optional[Ring1] = field(
        default=None,
        metadata={
            "name": "Ring",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )
