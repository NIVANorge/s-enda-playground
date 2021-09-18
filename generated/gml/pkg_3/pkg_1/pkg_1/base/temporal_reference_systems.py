from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional
from xsdata.models.datatype import XmlDate, XmlTime
from generated.gml.pkg_3.pkg_1.pkg_1.base.dictionary import DefinitionType
from generated.gml.pkg_3.pkg_1.pkg_1.base.gml_base import (
    ReferenceType,
    StringOrRefType,
)
from generated.gml.pkg_3.pkg_1.pkg_1.base.temporal import (
    RelatedTimeType,
    TimeInstantPropertyType,
    TimeIntervalLengthType,
    TimePeriodPropertyType,
    TimePositionType,
)
from generated.gml.pkg_3.pkg_1.pkg_1.base.temporal_topology import TimeNodePropertyType
from generated.xlink import (
    ActuateType,
    ShowType,
    TypeType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class AbstractTimeReferenceSystemType(DefinitionType):
    """A value in the time domain is measured relative to a temporal reference
    system.

    Common types of reference systems include calendars, ordinal
    temporal reference systems, and temporal coordinate systems (time
    elapsed since some epoch, e.g. UNIX time).
    """
    domain_of_validity: Optional[str] = field(
        default=None,
        metadata={
            "name": "domainOfValidity",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )


@dataclass
class TimeCalendarEraType(DefinitionType):
    """In every calendar, years are numbered relative to the date of a
    reference event that defines a calendar era.

    In this implementation, we omit the back-pointer "datingSystem".

    :ivar reference_event: Name or description of a mythical or historic
        event which fixes the position of the base scale of the calendar
        era.
    :ivar reference_date: Date of the referenceEvent expressed as a date
        in the given calendar. In most calendars, this date is the
        origin (i.e., the first day) of the scale, but this is not
        always true.
    :ivar julian_reference: Julian date that corresponds to the
        reference date. The Julian day numbering system is a temporal
        coordinate system that has an origin earlier than any known
        calendar, at noon on 1 January 4713 BC in the Julian proleptic
        calendar. The Julian day number is an integer value; the Julian
        date is a decimal value that allows greater resolution.
        Transforming calendar dates to and from Julian dates provides a
        relatively simple basis for transforming dates from one calendar
        to another.
    :ivar epoch_of_use: Period for which the calendar era was used as a
        basis for dating.
    """
    reference_event: Optional[StringOrRefType] = field(
        default=None,
        metadata={
            "name": "referenceEvent",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )
    reference_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "referenceDate",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    julian_reference: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "julianReference",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )
    epoch_of_use: Optional[TimePeriodPropertyType] = field(
        default=None,
        metadata={
            "name": "epochOfUse",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )


@dataclass
class TimeOrdinalEraType(DefinitionType):
    """Ordinal temporal reference systems are often hierarchically structured
    such that an ordinal era at a given level of the hierarchy includes a
    sequence of shorter, coterminous ordinal eras.

    This captured using the member/group properties. Note that in this
    schema, TIme Ordinal Era is patterned on TimeEdge, which is a
    variation from ISO 19108. This is in order to fulfill the
    requirements of ordinal reference systems based on eras delimited by
    named points or nodes, which are common in geology, archeology, etc.
    This change is subject of a change proposal to ISO

    :ivar related_time:
    :ivar start:
    :ivar end:
    :ivar extent:
    :ivar member: An Era may be composed of several member Eras. The
        "member" element implements the association to the Era at the
        next level down the hierarchy.  "member" follows the standard
        GML property pattern whereby its (complex) value may be either
        described fully inline, or may be the target of a link carried
        on the member element and described fully elsewhere, either in
        the same document or from another service.
    :ivar group: In a particular Time System, an Era may be a member of
        a group.  The "group" element implements the back-pointer to the
        Era at the next level up in the hierarchy. If the hierarchy is
        represented by describing the nested components fully in the
        their nested position inside "member" elements, then the parent
        can be easily inferred, so the group property is unnecessary.
        However, if the hierarchy is represented by links carried on the
        "member" property elements, pointing to Eras described fully
        elsewhere, then it may be useful for a child (member) era to
        carry an explicit pointer back to its parent (group) Era.
    """
    related_time: List[RelatedTimeType] = field(
        default_factory=list,
        metadata={
            "name": "relatedTime",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    start: Optional[TimeNodePropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )
    end: Optional[TimeNodePropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )
    extent: Optional[TimePeriodPropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    member: List["TimeOrdinalEraPropertyType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    group: Optional[ReferenceType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )


@dataclass
class TimeCalendarEra(TimeCalendarEraType):
    class Meta:
        namespace = "http://www.opengis.net/gml"


@dataclass
class TimeCoordinateSystemType(AbstractTimeReferenceSystemType):
    """
    A temporal coordinate system is based on a continuous interval scale
    defined in terms of a single time interval.
    """
    origin_position: Optional[TimePositionType] = field(
        default=None,
        metadata={
            "name": "originPosition",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    origin: Optional[TimeInstantPropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    interval: Optional[TimeIntervalLengthType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )


@dataclass
class TimeOrdinalEra(TimeOrdinalEraType):
    class Meta:
        namespace = "http://www.opengis.net/gml"


@dataclass
class TimeReferenceSystem(AbstractTimeReferenceSystemType):
    """
    Abstract element serves primarily as the head of a substitution group for
    temporal reference systems.
    """
    class Meta:
        name = "_TimeReferenceSystem"
        namespace = "http://www.opengis.net/gml"


@dataclass
class TimeCalendarEraPropertyType:
    time_calendar_era: Optional[TimeCalendarEra] = field(
        default=None,
        metadata={
            "name": "TimeCalendarEra",
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
class TimeCoordinateSystem(TimeCoordinateSystemType):
    class Meta:
        namespace = "http://www.opengis.net/gml"


@dataclass
class TimeOrdinalEraPropertyType:
    time_ordinal_era: Optional[TimeOrdinalEra] = field(
        default=None,
        metadata={
            "name": "TimeOrdinalEra",
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
class TimeCalendarType(AbstractTimeReferenceSystemType):
    """A calendar is a discrete temporal reference system that provides a basis
    for defining temporal position to a resolution of one day.

    A single calendar may reference more than one calendar era.

    :ivar reference_frame: Link to the CalendarEras that it uses as a
        reference for dating.
    """
    reference_frame: List[TimeCalendarEraPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "referenceFrame",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "min_occurs": 1,
        }
    )


@dataclass
class TimeOrdinalReferenceSystemType(AbstractTimeReferenceSystemType):
    """
    In an ordinal reference system the order of events in time can be well
    established, but the magnitude of the intervals between them can not be
    accurately determined (e.g. a stratigraphic sequence).
    """
    component: List[TimeOrdinalEraPropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "min_occurs": 1,
        }
    )


@dataclass
class TimeCalendar(TimeCalendarType):
    class Meta:
        namespace = "http://www.opengis.net/gml"


@dataclass
class TimeOrdinalReferenceSystem(TimeOrdinalReferenceSystemType):
    class Meta:
        namespace = "http://www.opengis.net/gml"


@dataclass
class TimeCalendarPropertyType:
    time_calendar: Optional[TimeCalendar] = field(
        default=None,
        metadata={
            "name": "TimeCalendar",
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
class TimeClockType(AbstractTimeReferenceSystemType):
    """A clock provides a basis for defining temporal position within a day.

    A clock must be used with a calendar in order to provide a complete
    description of a temporal position within a specific day.

    :ivar reference_event: Name or description of an event, such as
        solar noon or sunrise, which fixes the position of the base
        scale of the clock.
    :ivar reference_time: time of day associated with the reference
        event expressed as a time of day in the given clock. The
        reference time is usually the origin of the clock scale.
    :ivar utc_reference: 24 hour local or UTC time that corresponds to
        the reference time.
    :ivar date_basis:
    """
    reference_event: Optional[StringOrRefType] = field(
        default=None,
        metadata={
            "name": "referenceEvent",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )
    reference_time: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "referenceTime",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )
    utc_reference: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "utcReference",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )
    date_basis: List[TimeCalendarPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "dateBasis",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )


@dataclass
class TimeClock(TimeClockType):
    class Meta:
        namespace = "http://www.opengis.net/gml"


@dataclass
class TimeClockPropertyType:
    time_clock: Optional[TimeClock] = field(
        default=None,
        metadata={
            "name": "TimeClock",
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
