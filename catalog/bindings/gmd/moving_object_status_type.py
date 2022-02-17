from dataclasses import dataclass, field
from typing import Optional
from bindings.gmd.abstract_time_slice_type import AbstractTimeSliceType
from bindings.gmd.direction_property_type import DirectionPropertyType
from bindings.gmd.geometry_array_property_type import GeometryPropertyType
from bindings.gmd.location import Location
from bindings.gmd.location_name import LocationName
from bindings.gmd.location_reference import LocationReference
from bindings.gmd.measure_type import MeasureType
from bindings.gmd.pos import Pos
from bindings.gmd.priority_location import PriorityLocation
from bindings.gmd.status import Status
from bindings.gmd.status_reference import StatusReference

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class MovingObjectStatusType(AbstractTimeSliceType):
    position: Optional[GeometryPropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    pos: Optional[Pos] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    location_name: Optional[LocationName] = field(
        default=None,
        metadata={
            "name": "locationName",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    location_reference: Optional[LocationReference] = field(
        default=None,
        metadata={
            "name": "locationReference",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
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
    status_reference: Optional[StatusReference] = field(
        default=None,
        metadata={
            "name": "statusReference",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
