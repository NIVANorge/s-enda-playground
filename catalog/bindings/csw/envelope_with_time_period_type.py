from dataclasses import dataclass, field
from typing import List
from bindings.csw.envelope_type import EnvelopeType
from bindings.csw.time_position import TimePosition

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class EnvelopeWithTimePeriodType(EnvelopeType):
    """
    Envelope that includes also a temporal extent.
    """

    time_position: List[TimePosition] = field(
        default_factory=list,
        metadata={
            "name": "timePosition",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "min_occurs": 2,
            "max_occurs": 2,
        },
    )
    frame: str = field(
        default="#ISO-8601",
        metadata={
            "type": "Attribute",
        },
    )
