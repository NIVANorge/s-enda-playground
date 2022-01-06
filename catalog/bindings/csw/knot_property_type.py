from dataclasses import dataclass, field
from typing import Optional
from bindings.csw.knot_type import KnotType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class KnotPropertyType:
    """
    Encapsulates a knot to use it in a geometric type.
    """

    knot: Optional[KnotType] = field(
        default=None,
        metadata={
            "name": "Knot",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        },
    )
