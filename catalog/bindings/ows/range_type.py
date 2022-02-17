from dataclasses import dataclass, field
from typing import Optional
from bindings.ows.range_closure_value import RangeClosureValue

__NAMESPACE__ = "http://www.opengis.net/ows/2.0"


@dataclass
class RangeType:
    """A range of values of a numeric parameter.

    This range can be continuous or discrete, defined by a fixed spacing
    between adjacent valid values. If the MinimumValue or MaximumValue
    is not included, there is no value limit in that direction.
    Inclusion of the specified minimum and maximum values in the range
    shall be defined by the rangeClosure.

    :ivar minimum_value:
    :ivar maximum_value:
    :ivar spacing: Shall be included when the allowed values are NOT
        continuous in this range. Shall not be included when the allowed
        values are continuous in this range.
    :ivar range_closure: Shall be included unless the default value
        applies.
    """

    minimum_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "MinimumValue",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows/2.0",
        },
    )
    maximum_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "MaximumValue",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows/2.0",
        },
    )
    spacing: Optional[str] = field(
        default=None,
        metadata={
            "name": "Spacing",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows/2.0",
        },
    )
    range_closure: RangeClosureValue = field(
        default=RangeClosureValue.CLOSED,
        metadata={
            "name": "rangeClosure",
            "type": "Attribute",
            "namespace": "http://www.opengis.net/ows/2.0",
        },
    )
