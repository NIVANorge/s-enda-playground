from dataclasses import dataclass, field
from typing import Optional
from bindings.csw.abstract_time_slice_type import AbstractTimeSliceType
from bindings.csw.direction_property_type import DirectionPropertyType
from bindings.csw.location import Location
from bindings.csw.measure_type import MeasureType
from bindings.csw.priority_location import PriorityLocation
from bindings.csw.status import Status

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class MovingObjectStatusType(AbstractTimeSliceType):
    """This type encapsulates various dynamic properties of moving objects
    (points, lines, regions).

    It is useful for dealing with features whose geometry or topology
    changes over time.
    """

    priority_location: Optional[PriorityLocation] = field(
        default=None,
        metadata={
            "name": "priorityLocation",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    location: Optional[Location] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    speed: Optional[MeasureType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    bearing: Optional[DirectionPropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    acceleration: Optional[MeasureType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    elevation: Optional[MeasureType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    status: Optional[Status] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
