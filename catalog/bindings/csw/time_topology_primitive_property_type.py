from dataclasses import dataclass, field
from typing import Optional
from bindings.csw.abstract_time_primitive_type import (
    TimeEdge,
    TimeNode,
    TimeTopologyPrimitive,
)
from bindings.csw.actuate_type import ActuateType
from bindings.csw.show_type import ShowType
from bindings.csw.type_type import TypeType

__NAMESPACE__ = "http://www.opengis.net/gml"


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
        },
    )
    time_node: Optional[TimeNode] = field(
        default=None,
        metadata={
            "name": "TimeNode",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    time_topology_primitive: Optional[TimeTopologyPrimitive] = field(
        default=None,
        metadata={
            "name": "_TimeTopologyPrimitive",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    type: TypeType = field(
        init=False,
        default=TypeType.SIMPLE,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    role: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        },
    )
    arcrole: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    show: Optional[ShowType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    actuate: Optional[ActuateType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    remote_schema: Optional[str] = field(
        default=None,
        metadata={
            "name": "remoteSchema",
            "type": "Attribute",
            "namespace": "http://www.opengis.net/gml",
        },
    )
