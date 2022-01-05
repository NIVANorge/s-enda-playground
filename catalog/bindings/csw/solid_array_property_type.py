from dataclasses import dataclass, field
from typing import List
from bindings.csw.composite_solid_type import CompositeSolid
from bindings.csw.solid_1 import Solid1
from bindings.csw.solid_2 import Solid2

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class SolidArrayPropertyType:
    """A container for an array of solids.

    The elements are always contained in the array property, referencing
    geometry elements or arrays of geometry elements is not supported.
    """
    solid: List[Solid1] = field(
        default_factory=list,
        metadata={
            "name": "Solid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "sequential": True,
        }
    )
    composite_solid: List[CompositeSolid] = field(
        default_factory=list,
        metadata={
            "name": "CompositeSolid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "sequential": True,
        }
    )
    opengis_net_gml_solid: List[Solid2] = field(
        default_factory=list,
        metadata={
            "name": "_Solid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "sequential": True,
        }
    )
