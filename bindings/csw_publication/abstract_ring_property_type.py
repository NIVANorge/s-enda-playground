from dataclasses import dataclass, field
from typing import Optional
from bindings.csw_publication.linear_ring import LinearRing
from bindings.csw_publication.ring_1 import Ring1
from bindings.csw_publication.ring_2 import Ring2

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class AbstractRingPropertyType:
    """
    Encapsulates a ring to represent the surface boundary property of a
    surface.
    """
    ring: Optional[Ring1] = field(
        default=None,
        metadata={
            "name": "Ring",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    linear_ring: Optional[LinearRing] = field(
        default=None,
        metadata={
            "name": "LinearRing",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    opengis_net_gml_ring: Optional[Ring2] = field(
        default=None,
        metadata={
            "name": "_Ring",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
