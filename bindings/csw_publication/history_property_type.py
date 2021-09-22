from dataclasses import dataclass, field
from typing import List
from bindings.csw_publication.moving_object_status import MovingObjectStatus
from bindings.csw_publication.time_slice import TimeSlice

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class HistoryPropertyType:
    """
    The history relationship associates a feature with a sequence of TimeSlice
    instances.
    """
    moving_object_status: List[MovingObjectStatus] = field(
        default_factory=list,
        metadata={
            "name": "MovingObjectStatus",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "sequential": True,
        }
    )
    time_slice: List[TimeSlice] = field(
        default_factory=list,
        metadata={
            "name": "_TimeSlice",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "sequential": True,
        }
    )
