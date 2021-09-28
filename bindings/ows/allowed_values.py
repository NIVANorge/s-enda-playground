from dataclasses import dataclass, field
from typing import List
from bindings.ows.range import Range

__NAMESPACE__ = "http://www.opengis.net/ows/2.0"


@dataclass
class AllowedValues:
    """List of all the valid values and/or ranges of values for this quantity.

    For numeric quantities, signed values should be ordered from
    negative infinity to positive infinity.
    """
    class Meta:
        namespace = "http://www.opengis.net/ows/2.0"

    value: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Value",
            "type": "Element",
        }
    )
    range: List[Range] = field(
        default_factory=list,
        metadata={
            "name": "Range",
            "type": "Element",
        }
    )
