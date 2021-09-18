from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional
from generated.gml.pkg_3.pkg_1.pkg_1.base.gml_base import ReferenceType
from generated.gml.pkg_3.pkg_1.pkg_1.base.temporal import (
    AbstractTimeComplexType,
    AbstractTimePrimitiveType,
    TimeInstantPropertyType,
    TimePeriodPropertyType,
)
from generated.xlink import (
    ActuateType,
    ShowType,
    TypeType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


class SuccessionType(Enum):
    """Feature succession is a semantic relationship derived from evaluation of
    observer, and Feature Substitution, Feature Division and Feature Fusion are
    defined as associations between previous features and next features in the
    temporal context. Successions shall be represented in either following two
    ways.

    * define a temporal topological complex element as a feature element
    * define an association same as temporal topological complex between features.
    """
    SUBSTITUTION = "substitution"
    DIVISION = "division"
    FUSION = "fusion"
    INITIATION = "initiation"


@dataclass
class AbstractTimeTopologyPrimitiveType(AbstractTimePrimitiveType):
    """
    The element "complex" carries a reference to the complex containing this
    primitive.
    """
    complex: Optional[ReferenceType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )


@dataclass
class TimeEdgePropertyType:
    """A time edge property can either be any time edge element encapsulated in
    an element of this type or an XLink reference to a remote time edge element
    (where remote includes elements located elsewhere in the same document).

    Note that either the reference or the contained element must be
    given, but not both or none.
    """
    time_edge: Optional["TimeEdge"] = field(
        default=None,
        metadata={
            "name": "TimeEdge",
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
class TimeNodeType(AbstractTimeTopologyPrimitiveType):
    """
    Type declaration of the element "TimeNode".
    """
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
class TimeTopologyPrimitive(AbstractTimeTopologyPrimitiveType):
    """
    This abstract element acts as the head of the substitution group for
    temporal topology primitives.
    """
    class Meta:
        name = "_TimeTopologyPrimitive"
        namespace = "http://www.opengis.net/gml"


@dataclass
class TimeNode(TimeNodeType):
    """"TimeNode" is a zero dimensional temporal topology primitive, expresses
    a position in topological time, and is a start and an end of time edge,
    which represents states of time.

    Time node may be isolated. However, it cannot describe the ordering
    relationships with other primitives. An isolated node may not be an
    element of any temporal topology complex.
    """
    class Meta:
        namespace = "http://www.opengis.net/gml"


@dataclass
class TimeNodePropertyType:
    """A time node property can either be any time node element encapsulated in
    an element of this type or an XLink reference to a remote time node element
    (where remote includes elements located elsewhere in the same document).

    Note that either the reference or the contained element must be
    given, but not both or none.
    """
    time_node: Optional[TimeNode] = field(
        default=None,
        metadata={
            "name": "TimeNode",
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
class TimeEdgeType(AbstractTimeTopologyPrimitiveType):
    """
    Type declaration of the element "TimeEdge".
    """
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
    """TimeEdge is one dimensional temporal topology primitive, expresses a
    state in topological time.

    It has an orientation from its start toward the end, and its
    boundaries shall associate with two different time nodes.
    """
    class Meta:
        namespace = "http://www.opengis.net/gml"


@dataclass
class TimeTopologyPrimitivePropertyType:
    """A time topology primitive property can either hold any time topology
    complex element eor carry an XLink reference to a remote time topology
    complex element (where remote includes elements located elsewhere in the
    same document).

    Note that either the reference or the contained element must be
    given, but not both or none.
    """
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
class TimeTopologyComplexType(AbstractTimeComplexType):
    """
    A temporal topology complex.
    """
    primitive: List[TimeTopologyPrimitivePropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "min_occurs": 1,
        }
    )


@dataclass
class TimeTopologyComplex(TimeTopologyComplexType):
    """This element represents temporal topology complex.

    It shall be the connected acyclic directed graph composed of time
    nodes and time edges.
    """
    class Meta:
        namespace = "http://www.opengis.net/gml"


@dataclass
class TimeTopologyComplexPropertyType:
    """A time topology complex property can either be any time topology complex
    element encapsulated in an element of this type or an XLink reference to a
    remote time topology complex element (where remote includes elements
    located elsewhere in the same document).

    Note that either the reference or the contained element must be
    given, but not both or none.
    """
    time_topology_complex: Optional[TimeTopologyComplex] = field(
        default=None,
        metadata={
            "name": "TimeTopologyComplex",
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
