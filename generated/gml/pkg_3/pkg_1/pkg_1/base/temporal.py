from dataclasses import dataclass, field
from decimal import Decimal
from enum import Enum
from typing import List, Optional, Union
from xsdata.models.datatype import XmlDate, XmlDateTime, XmlDuration, XmlPeriod, XmlTime
from generated.gml.pkg_3.pkg_1.pkg_1.base.gml_base import AbstractGmltype
from generated.gml.pkg_3.pkg_1.pkg_1.base.temporal_topology import (
    TimeEdge,
    TimeNode,
    TimeTopologyPrimitive,
)
from generated.xlink import (
    ActuateType,
    ShowType,
    TypeType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


class RelatedTimeTypeRelativePosition(Enum):
    BEFORE = "Before"
    AFTER = "After"
    BEGINS = "Begins"
    ENDS = "Ends"
    DURING = "During"
    EQUALS = "Equals"
    CONTAINS = "Contains"
    OVERLAPS = "Overlaps"
    MEETS = "Meets"
    OVERLAPPED_BY = "OverlappedBy"
    MET_BY = "MetBy"
    BEGUN_BY = "BegunBy"
    ENDED_BY = "EndedBy"


class TimeIndeterminateValueType(Enum):
    """
    This enumerated data type specifies values for indeterminate positions.
    """
    AFTER = "after"
    BEFORE = "before"
    NOW = "now"
    UNKNOWN = "unknown"


class TimeUnitTypeValue(Enum):
    YEAR = "year"
    DAY = "day"
    HOUR = "hour"
    MINUTE = "minute"
    SECOND = "second"


@dataclass
class Duration:
    """This element is an instance of the primitive xsd:duration simple type to
    enable use of the ISO 8601 syntax for temporal length (e.g. P5DT4H30M).

    It is a valid subtype of TimeDurationType according to section
    3.14.6, rule 2.2.4 in XML Schema, Part 1.
    """
    class Meta:
        name = "duration"
        namespace = "http://www.opengis.net/gml"

    value: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class AbstractTimeObjectType(AbstractGmltype):
    """
    The abstract supertype for temporal objects.
    """


@dataclass
class TimeIntervalLengthType:
    """This type extends the built-in xsd:decimal simple type to allow
    floating-point values for temporal length.

    According to  the ISO 11404 model you have to use positiveInteger
    together with appropriate values for radix and factor. The
    resolution of the time interval is to one radix ^(-factor) of the
    specified time unit (e.g. unit="second", radix="10", factor="3"
    specifies a resolution of milliseconds). It is a subtype of
    TimeDurationType.
    """
    value: Optional[Decimal] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    unit: Optional[Union[str, TimeUnitTypeValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"other:\w{2,}",
        }
    )
    radix: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    factor: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class TimePositionType:
    """Direct representation of a temporal position.

    Indeterminate time values are also allowed, as described in ISO
    19108. The indeterminatePosition attribute can be used alone or it
    can qualify a specific value for temporal position (e.g. before
    2002-12, after 1019624400). For time values that identify position
    within a calendar, the calendarEraName attribute provides the name
    of the calendar era to which the date is referenced (e.g. the Meiji
    era of the Japanese calendar).
    """
    value: Union[XmlDate, XmlPeriod, XmlTime, XmlDateTime, str, Decimal] = field(
        default=""
    )
    frame: str = field(
        default="#ISO-8601",
        metadata={
            "type": "Attribute",
        }
    )
    calendar_era_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "calendarEraName",
            "type": "Attribute",
        }
    )
    indeterminate_position: Optional[TimeIndeterminateValueType] = field(
        default=None,
        metadata={
            "name": "indeterminatePosition",
            "type": "Attribute",
        }
    )


@dataclass
class AbstractTimeComplexType(AbstractTimeObjectType):
    """
    The abstract supertype for temporal complexes.
    """


@dataclass
class AbstractTimePrimitiveType(AbstractTimeObjectType):
    """
    The abstract supertype for temporal primitives.
    """
    related_time: List["RelatedTimeType"] = field(
        default_factory=list,
        metadata={
            "name": "relatedTime",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )


@dataclass
class TimeObject(AbstractTimeObjectType):
    """
    This abstract element acts as the head of the substitution group for
    temporal primitives and complexes.
    """
    class Meta:
        name = "_TimeObject"
        namespace = "http://www.opengis.net/gml"


@dataclass
class TimeInterval(TimeIntervalLengthType):
    """
    This element is a valid subtype of TimeDurationType according to section
    3.14.6, rule 2.2.4 in XML Schema, Part 1.
    """
    class Meta:
        name = "timeInterval"
        namespace = "http://www.opengis.net/gml"


@dataclass
class TimePosition(TimePositionType):
    """
    Direct representation of a temporal position.
    """
    class Meta:
        name = "timePosition"
        namespace = "http://www.opengis.net/gml"


@dataclass
class AbstractTimeGeometricPrimitiveType(AbstractTimePrimitiveType):
    """The abstract supertype for temporal geometric primitives.

    A temporal geometry must be associated with a temporal reference
    system via URI. The Gregorian calendar with UTC is the default
    reference system, following ISO 8601. Other reference systems in
    common use include the GPS calendar and the Julian calendar.
    """
    frame: str = field(
        default="#ISO-8601",
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class TimeComplex(AbstractTimeComplexType):
    """This abstract element acts as the head of the substitution group for
    temporal complexes.

    Temporal complex is an aggregation of temporal primitives as its
    components, represents a temporal geometric complex and a temporal
    topology complex. N.B. Temporal geometric complex is not defined in
    this schema.
    """
    class Meta:
        name = "_TimeComplex"
        namespace = "http://www.opengis.net/gml"


@dataclass
class TimePrimitive(AbstractTimePrimitiveType):
    """
    This abstract element acts as the head of the substitution group for
    temporal primitives.
    """
    class Meta:
        name = "_TimePrimitive"
        namespace = "http://www.opengis.net/gml"


@dataclass
class TimeInstantType(AbstractTimeGeometricPrimitiveType):
    """
    Omit back-pointers begunBy, endedBy.
    """
    time_position: Optional[TimePosition] = field(
        default=None,
        metadata={
            "name": "timePosition",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )


@dataclass
class TimeGeometricPrimitive(AbstractTimeGeometricPrimitiveType):
    """
    This abstract element acts as the head of the substitution group for
    temporal geometric primitives.
    """
    class Meta:
        name = "_TimeGeometricPrimitive"
        namespace = "http://www.opengis.net/gml"


@dataclass
class TimeInstant(TimeInstantType):
    class Meta:
        namespace = "http://www.opengis.net/gml"


@dataclass
class TimeInstantPropertyType:
    time_instant: Optional[TimeInstant] = field(
        default=None,
        metadata={
            "name": "TimeInstant",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    type: TypeType = field(
        init=False,
        default=TypeType.SIMPLE,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    role: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        }
    )
    arcrole: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    show: Optional[ShowType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    actuate: Optional[ActuateType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    remote_schema: Optional[str] = field(
        default=None,
        metadata={
            "name": "remoteSchema",
            "type": "Attribute",
            "namespace": "http://www.opengis.net/gml",
        }
    )


@dataclass
class TimePeriodType(AbstractTimeGeometricPrimitiveType):
    begin_position: Optional[TimePositionType] = field(
        default=None,
        metadata={
            "name": "beginPosition",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    begin: Optional[TimeInstantPropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    end_position: Optional[TimePositionType] = field(
        default=None,
        metadata={
            "name": "endPosition",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    end: Optional[TimeInstantPropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    duration: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    time_interval: Optional[TimeInterval] = field(
        default=None,
        metadata={
            "name": "timeInterval",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )


@dataclass
class TimePeriod(TimePeriodType):
    class Meta:
        namespace = "http://www.opengis.net/gml"


@dataclass
class TimeGeometricPrimitivePropertyType:
    time_period: Optional[TimePeriod] = field(
        default=None,
        metadata={
            "name": "TimePeriod",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    time_instant: Optional[TimeInstant] = field(
        default=None,
        metadata={
            "name": "TimeInstant",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    time_geometric_primitive: Optional[TimeGeometricPrimitive] = field(
        default=None,
        metadata={
            "name": "_TimeGeometricPrimitive",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    type: TypeType = field(
        init=False,
        default=TypeType.SIMPLE,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    role: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        }
    )
    arcrole: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    show: Optional[ShowType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    actuate: Optional[ActuateType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    remote_schema: Optional[str] = field(
        default=None,
        metadata={
            "name": "remoteSchema",
            "type": "Attribute",
            "namespace": "http://www.opengis.net/gml",
        }
    )


@dataclass
class TimePeriodPropertyType:
    time_period: Optional[TimePeriod] = field(
        default=None,
        metadata={
            "name": "TimePeriod",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    type: TypeType = field(
        init=False,
        default=TypeType.SIMPLE,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    role: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        }
    )
    arcrole: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    show: Optional[ShowType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    actuate: Optional[ActuateType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    remote_schema: Optional[str] = field(
        default=None,
        metadata={
            "name": "remoteSchema",
            "type": "Attribute",
            "namespace": "http://www.opengis.net/gml",
        }
    )


@dataclass
class TimePrimitivePropertyType:
    time_edge: Optional[TimeEdge] = field(
        default=None,
        metadata={
            "name": "TimeEdge",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    time_node: Optional[TimeNode] = field(
        default=None,
        metadata={
            "name": "TimeNode",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    time_topology_primitive: Optional[TimeTopologyPrimitive] = field(
        default=None,
        metadata={
            "name": "_TimeTopologyPrimitive",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    time_period: Optional[TimePeriod] = field(
        default=None,
        metadata={
            "name": "TimePeriod",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    time_instant: Optional[TimeInstant] = field(
        default=None,
        metadata={
            "name": "TimeInstant",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    time_geometric_primitive: Optional[TimeGeometricPrimitive] = field(
        default=None,
        metadata={
            "name": "_TimeGeometricPrimitive",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    time_primitive: Optional[TimePrimitive] = field(
        default=None,
        metadata={
            "name": "_TimePrimitive",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    type: TypeType = field(
        init=False,
        default=TypeType.SIMPLE,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    role: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        }
    )
    arcrole: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    show: Optional[ShowType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    actuate: Optional[ActuateType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    remote_schema: Optional[str] = field(
        default=None,
        metadata={
            "name": "remoteSchema",
            "type": "Attribute",
            "namespace": "http://www.opengis.net/gml",
        }
    )


@dataclass
class RelatedTimeType(TimePrimitivePropertyType):
    relative_position: Optional[RelatedTimeTypeRelativePosition] = field(
        default=None,
        metadata={
            "name": "relativePosition",
            "type": "Attribute",
        }
    )


@dataclass
class ValidTime(TimePrimitivePropertyType):
    class Meta:
        name = "validTime"
        namespace = "http://www.opengis.net/gml"
