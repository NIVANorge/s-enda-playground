from dataclasses import dataclass, field
from typing import List, Optional
from bindings.csw_publication.abstract_topology_type import AbstractTopologyType
from bindings.csw_publication.actuate_type import ActuateType
from bindings.csw_publication.show_type import ShowType
from bindings.csw_publication.topo_primitive_member import TopoPrimitiveMember
from bindings.csw_publication.topo_primitive_members import TopoPrimitiveMembers
from bindings.csw_publication.type_type import TypeType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class TopoComplexMemberType:
    """
    This Property can be used to embed a TopoComplex in a feature collection.
    """
    topo_complex: Optional["TopoComplex"] = field(
        default=None,
        metadata={
            "name": "TopoComplex",
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
class MaximalComplex(TopoComplexMemberType):
    """
    Need schamatron test here that isMaximal attribute value is true.
    """
    class Meta:
        name = "maximalComplex"
        namespace = "http://www.opengis.net/gml"


@dataclass
class SubComplex(TopoComplexMemberType):
    class Meta:
        name = "subComplex"
        namespace = "http://www.opengis.net/gml"


@dataclass
class SuperComplex(TopoComplexMemberType):
    class Meta:
        name = "superComplex"
        namespace = "http://www.opengis.net/gml"


@dataclass
class TopoComplexType(AbstractTopologyType):
    """
    This type represents a TP_Complex capable of holding topological
    primitives.
    """
    maximal_complex: Optional[MaximalComplex] = field(
        default=None,
        metadata={
            "name": "maximalComplex",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )
    super_complex: List[SuperComplex] = field(
        default_factory=list,
        metadata={
            "name": "superComplex",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    sub_complex: List[SubComplex] = field(
        default_factory=list,
        metadata={
            "name": "subComplex",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    topo_primitive_member: List[TopoPrimitiveMember] = field(
        default_factory=list,
        metadata={
            "name": "topoPrimitiveMember",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    topo_primitive_members: Optional[TopoPrimitiveMembers] = field(
        default=None,
        metadata={
            "name": "topoPrimitiveMembers",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    is_maximal: bool = field(
        default=False,
        metadata={
            "name": "isMaximal",
            "type": "Attribute",
        }
    )


@dataclass
class TopoComplex(TopoComplexType):
    class Meta:
        namespace = "http://www.opengis.net/gml"
