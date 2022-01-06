from dataclasses import dataclass, field
from typing import Optional, Union
from bindings.csw.envelope import Envelope
from bindings.csw.envelope_with_time_period import EnvelopeWithTimePeriod
from bindings.csw.null_enumeration_value import NullEnumerationValue

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class BoundingShapeType:
    """
    Bounding shape.
    """

    envelope_with_time_period: Optional[EnvelopeWithTimePeriod] = field(
        default=None,
        metadata={
            "name": "EnvelopeWithTimePeriod",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    envelope: Optional[Envelope] = field(
        default=None,
        metadata={
            "name": "Envelope",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    null: Optional[Union[str, NullEnumerationValue]] = field(
        default=None,
        metadata={
            "name": "Null",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "pattern": r"other:\w{2,}",
        },
    )
