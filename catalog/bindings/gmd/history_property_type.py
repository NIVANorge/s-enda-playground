from dataclasses import dataclass, field
from typing import List
from bindings.gmd.abstract_time_slice import AbstractTimeSlice
from bindings.gmd.moving_object_status import MovingObjectStatus

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class HistoryPropertyType:
    moving_object_status: List[MovingObjectStatus] = field(
        default_factory=list,
        metadata={
            "name": "MovingObjectStatus",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    abstract_time_slice: List[AbstractTimeSlice] = field(
        default_factory=list,
        metadata={
            "name": "AbstractTimeSlice",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
