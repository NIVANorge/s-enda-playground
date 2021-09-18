from dataclasses import dataclass, field
from typing import List, Optional
from generated.gml.pkg_3.pkg_1.pkg_1.base.basic_types import MeasureType
from generated.gml.pkg_3.pkg_1.pkg_1.base.direction import DirectionPropertyType
from generated.gml.pkg_3.pkg_1.pkg_1.base.feature import (
    AbstractFeatureType,
    FeatureCollectionType,
    Location,
    PriorityLocation,
)
from generated.gml.pkg_3.pkg_1.pkg_1.base.gml_base import (
    AbstractGmltype,
    StringOrRefType,
)
from generated.gml.pkg_3.pkg_1.pkg_1.base.temporal import ValidTime

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class DataSource(StringOrRefType):
    class Meta:
        name = "dataSource"
        namespace = "http://www.opengis.net/gml"


@dataclass
class Status(StringOrRefType):
    class Meta:
        name = "status"
        namespace = "http://www.opengis.net/gml"


@dataclass
class AbstractTimeSliceType(AbstractGmltype):
    """A timeslice encapsulates the time-varying properties of a dynamic
    feature--it must be extended to represent a timestamped projection of a
    feature.

    The dataSource property describes how the temporal data was
    acquired.
    """
    valid_time: Optional[ValidTime] = field(
        default=None,
        metadata={
            "name": "validTime",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )
    data_source: Optional[DataSource] = field(
        default=None,
        metadata={
            "name": "dataSource",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )


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
        }
    )
    location: Optional[Location] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    speed: Optional[MeasureType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    bearing: Optional[DirectionPropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    acceleration: Optional[MeasureType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    elevation: Optional[MeasureType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    status: Optional[Status] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )


@dataclass
class TimeSlice(AbstractTimeSliceType):
    class Meta:
        name = "_TimeSlice"
        namespace = "http://www.opengis.net/gml"


@dataclass
class MovingObjectStatus(MovingObjectStatusType):
    class Meta:
        namespace = "http://www.opengis.net/gml"


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


@dataclass
class TrackType(HistoryPropertyType):
    """
    The track of a moving object is a sequence of specialized timeslices
    that indicate the status of the object.
    """


@dataclass
class History(HistoryPropertyType):
    class Meta:
        name = "history"
        namespace = "http://www.opengis.net/gml"


@dataclass
class Track(TrackType):
    class Meta:
        name = "track"
        namespace = "http://www.opengis.net/gml"


@dataclass
class DynamicFeatureCollectionType(FeatureCollectionType):
    """
    A dynamic feature collection may possess a history and/or a timestamp.
    """
    valid_time: Optional[ValidTime] = field(
        default=None,
        metadata={
            "name": "validTime",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    track: Optional[Track] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    history: Optional[History] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    data_source: Optional[DataSource] = field(
        default=None,
        metadata={
            "name": "dataSource",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )


@dataclass
class DynamicFeatureType(AbstractFeatureType):
    """
    A dynamic feature may possess a history and/or a timestamp.
    """
    valid_time: Optional[ValidTime] = field(
        default=None,
        metadata={
            "name": "validTime",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    track: Optional[Track] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    history: Optional[History] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    data_source: Optional[DataSource] = field(
        default=None,
        metadata={
            "name": "dataSource",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
