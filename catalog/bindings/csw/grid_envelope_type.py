from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class GridEnvelopeType:
    """Provides grid coordinate values for the diametrically opposed corners of
    an envelope that bounds a section of grid.

    The value of a single coordinate is the number of offsets from the
    origin of the grid in the direction of a specific axis.
    """
    low: List[int] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
            "tokens": True,
        }
    )
    high: List[int] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
            "tokens": True,
        }
    )
