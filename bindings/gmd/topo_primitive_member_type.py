from dataclasses import dataclass, field
from typing import Optional, Union
from bindings.gmd.abstract_topo_primitive import AbstractTopoPrimitive
from bindings.gmd.actuate_value import ActuateValue
from bindings.gmd.container_property_type import (
    Edge,
    Face,
    Node,
    TopoSolid,
)
from bindings.gmd.nil_reason_enumeration_value import NilReasonEnumerationValue
from bindings.gmd.show_value import ShowValue

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class TopoPrimitiveMemberType:
    topo_solid: Optional[TopoSolid] = field(
        default=None,
        metadata={
            "name": "TopoSolid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    face: Optional[Face] = field(
        default=None,
        metadata={
            "name": "Face",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    edge: Optional[Edge] = field(
        default=None,
        metadata={
            "name": "Edge",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    node: Optional[Node] = field(
        default=None,
        metadata={
            "name": "Node",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    abstract_topo_primitive: Optional[AbstractTopoPrimitive] = field(
        default=None,
        metadata={
            "name": "AbstractTopoPrimitive",
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
