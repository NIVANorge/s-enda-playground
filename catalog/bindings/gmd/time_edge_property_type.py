from dataclasses import dataclass, field
from typing import List, Optional, Union
from xsdata.models.datatype import XmlDuration
from bindings.gmd.abstract_time_object_type import AbstractTimeObjectType
from bindings.gmd.actuate_value import ActuateValue
from bindings.gmd.nil_reason_enumeration_value import NilReasonEnumerationValue
from bindings.gmd.reference_type import ReferenceType
from bindings.gmd.related_time_type_relative_position import RelatedTimeTypeRelativePosition
from bindings.gmd.show_value import ShowValue
from bindings.gmd.time_interval import TimeInterval
from bindings.gmd.time_position import TimePosition
from bindings.gmd.time_position_type import TimePositionType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class TimeEdgePropertyType:
    """
    gml:TimeEdgePropertyType provides for associating a gml:TimeEdge with an
    object.
    """
    time_edge: Optional["TimeEdge"] = field(
        default=None,
        metadata={
            "name": "TimeEdge",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    type: str = field(
        init=False,
        default="simple",
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
        }
    )
    arcrole: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    show: Optional[ShowValue] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    actuate: Optional[ActuateValue] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    nil_reason: Optional[Union[str, NilReasonEnumerationValue]] = field(
        default=None,
        metadata={
            "name": "nilReason",
            "type": "Attribute",
            "pattern": r"other:\w{2,}",
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
    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class TimeInstantPropertyType:
    """
    gml:TimeInstantPropertyType provides for associating a gml:TimeInstant with
    an object.
    """
    time_instant: Optional["TimeInstant"] = field(
        default=None,
        metadata={
            "name": "TimeInstant",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    type: str = field(
        init=False,
        default="simple",
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
        }
    )
    arcrole: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    show: Optional[ShowValue] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    actuate: Optional[ActuateValue] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    nil_reason: Optional[Union[str, NilReasonEnumerationValue]] = field(
        default=None,
        metadata={
            "name": "nilReason",
            "type": "Attribute",
            "pattern": r"other:\w{2,}",
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
    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class TimePrimitivePropertyType:
    """
    gml:TimePrimitivePropertyType provides a standard content model for
    associations between an arbitrary member of the substitution group whose
    head is gml:AbstractTimePrimitive and another object.
    """
    time_edge: Optional["TimeEdge"] = field(
        default=None,
        metadata={
            "name": "TimeEdge",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    time_node: Optional["TimeNode"] = field(
        default=None,
        metadata={
            "name": "TimeNode",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    abstract_time_topology_primitive: Optional["AbstractTimeTopologyPrimitive"] = field(
        default=None,
        metadata={
            "name": "AbstractTimeTopologyPrimitive",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    time_period: Optional["TimePeriod"] = field(
        default=None,
        metadata={
            "name": "TimePeriod",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    time_instant: Optional["TimeInstant"] = field(
        default=None,
        metadata={
            "name": "TimeInstant",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    abstract_time_geometric_primitive: Optional["AbstractTimeGeometricPrimitive"] = field(
        default=None,
        metadata={
            "name": "AbstractTimeGeometricPrimitive",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    abstract_time_primitive: Optional["AbstractTimePrimitive"] = field(
        default=None,
        metadata={
            "name": "AbstractTimePrimitive",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    type: str = field(
        init=False,
        default="simple",
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
        }
    )
    arcrole: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    show: Optional[ShowValue] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    actuate: Optional[ActuateValue] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    nil_reason: Optional[Union[str, NilReasonEnumerationValue]] = field(
        default=None,
        metadata={
            "name": "nilReason",
            "type": "Attribute",
            "pattern": r"other:\w{2,}",
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
    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class RelatedTimeType(TimePrimitivePropertyType):
    """gml:RelatedTimeType provides a content model for indicating the relative
    position of an arbitrary member of the substitution group whose head is
    gml:AbstractTimePrimitive.

    It extends the generic gml:TimePrimitivePropertyType with an XML
    attribute relativePosition, whose value is selected from the set of
    13 temporal relationships identified by Allen (1983)
    """
    relative_position: Optional[RelatedTimeTypeRelativePosition] = field(
        default=None,
        metadata={
            "name": "relativePosition",
            "type": "Attribute",
        }
    )


@dataclass
class AbstractTimePrimitiveType(AbstractTimeObjectType):
    related_time: List[RelatedTimeType] = field(
        default_factory=list,
        metadata={
            "name": "relatedTime",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )


@dataclass
class AbstractTimeGeometricPrimitiveType(AbstractTimePrimitiveType):
    frame: str = field(
        default="#ISO-8601",
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class AbstractTimePrimitive(AbstractTimePrimitiveType):
    """
    gml:AbstractTimePrimitive acts as the head of a substitution group for
    geometric and topological temporal primitives.
    """
    class Meta:
        namespace = "http://www.opengis.net/gml"


@dataclass
class AbstractTimeTopologyPrimitiveType(AbstractTimePrimitiveType):
    complex: Optional[ReferenceType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )


@dataclass
class AbstractTimeGeometricPrimitive(AbstractTimeGeometricPrimitiveType):
    """gml:TimeGeometricPrimitive acts as the head of a substitution group for
    geometric temporal primitives.

    A temporal geometry shall be associated with a temporal reference
    system through the frame attribute that provides a URI reference
    that identifies a description of the reference system. Following ISO
    19108, the Gregorian calendar with UTC is the default reference
    system, but others may also be used. The GPS calendar is an
    alternative reference systems in common use. The two geometric
    primitives in the temporal dimension are the instant and the period.
    GML components are defined to support these as follows.
    """
    class Meta:
        namespace = "http://www.opengis.net/gml"


@dataclass
class AbstractTimeTopologyPrimitive(AbstractTimeTopologyPrimitiveType):
    """gml:TimeTopologyPrimitive acts as the head of a substitution group for
    topological temporal primitives.

    Temporal topology primitives shall imply the ordering information
    between features or feature properties. The temporal connection of
    features can be examined if they have temporal topology primitives
    as values of their properties. Usually, an instantaneous feature
    associates with a time node, and a static feature associates with a
    time edge.  A feature with both modes associates with the temporal
    topology primitive: a supertype of time nodes and time edges. A
    topological primitive is always connected to one or more other
    topological primitives, and is, therefore, always a member of a
    topological complex. In a GML instance, this will often be indicated
    by the primitives being described by elements that are descendents
    of an element describing a complex. However, in order to support the
    case where a temporal topological primitive is described in another
    context, the optional complex property is provided, which carries a
    reference to the parent temporal topological complex.
    """
    class Meta:
        namespace = "http://www.opengis.net/gml"


@dataclass
class TimeInstantType(AbstractTimeGeometricPrimitiveType):
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
class TimeNodeType(AbstractTimeTopologyPrimitiveType):
    previous_edge: List[TimeEdgePropertyType] = field(
        default_factory=list,
        metadata={
            "name": "previousEdge",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    next_edge: List[TimeEdgePropertyType] = field(
        default_factory=list,
        metadata={
            "name": "nextEdge",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    position: Optional[TimeInstantPropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
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
class TimeInstant(TimeInstantType):
    """
    gml:TimeInstant acts as a zero-dimensional geometric primitive that
    represents an identifiable position in time.
    """
    class Meta:
        namespace = "http://www.opengis.net/gml"


@dataclass
class TimeNode(TimeNodeType):
    """A time node is a zero-dimensional topological primitive that represents
    an identifiable node in time (it is equivalent to a point in space).

    A node may act as the termination or initiation of any number of
    time edges. A time node may be realised as a geometry, its position,
    whose value is a time instant.
    """
    class Meta:
        namespace = "http://www.opengis.net/gml"


@dataclass
class TimePeriod(TimePeriodType):
    """gml:TimePeriod acts as a one-dimensional geometric primitive that
    represents an identifiable extent in time.

    The location in of a gml:TimePeriod is described by the temporal
    positions of the instants at which it begins and ends. The length of
    the period is equal to the temporal distance between the two
    bounding temporal positions. Both beginning and end may be described
    in terms of their direct position using gml:TimePositionType which
    is an XML Schema simple content type, or by reference to an
    indentifiable time instant using gml:TimeInstantPropertyType.
    Alternatively a limit of a gml:TimePeriod may use the conventional
    GML property model to make a reference to a time instant described
    elsewhere, or a limit may be indicated as a direct position.
    """
    class Meta:
        namespace = "http://www.opengis.net/gml"


@dataclass
class TimeNodePropertyType:
    """
    gml:TimeNodePropertyType provides for associating a gml:TimeNode with an
    object.
    """
    time_node: Optional[TimeNode] = field(
        default=None,
        metadata={
            "name": "TimeNode",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    type: str = field(
        init=False,
        default="simple",
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
        }
    )
    arcrole: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    show: Optional[ShowValue] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    actuate: Optional[ActuateValue] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    nil_reason: Optional[Union[str, NilReasonEnumerationValue]] = field(
        default=None,
        metadata={
            "name": "nilReason",
            "type": "Attribute",
            "pattern": r"other:\w{2,}",
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
    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class TimePeriodPropertyType:
    """
    gml:TimePeriodPropertyType provides for associating a gml:TimePeriod with
    an object.
    """
    time_period: Optional[TimePeriod] = field(
        default=None,
        metadata={
            "name": "TimePeriod",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    type: str = field(
        init=False,
        default="simple",
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
        }
    )
    arcrole: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    show: Optional[ShowValue] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    actuate: Optional[ActuateValue] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    nil_reason: Optional[Union[str, NilReasonEnumerationValue]] = field(
        default=None,
        metadata={
            "name": "nilReason",
            "type": "Attribute",
            "pattern": r"other:\w{2,}",
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
    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class TimeEdgeType(AbstractTimeTopologyPrimitiveType):
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


@dataclass
class TimeEdge(TimeEdgeType):
    """A time edge is a one-dimensional topological primitive.

    It is an open interval that starts and ends at a node. The edge may
    be realised as a geometry whose value is a time period.
    """
    class Meta:
        namespace = "http://www.opengis.net/gml"
