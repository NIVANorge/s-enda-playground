from dataclasses import dataclass, field
from typing import List, Optional
from generated.gml.pkg_3.pkg_1.pkg_1.base.basic_types import SignType
from generated.gml.pkg_3.pkg_1.pkg_1.base.geometry_basic0d1d import (
    CurveProperty,
    PointProperty,
)
from generated.gml.pkg_3.pkg_1.pkg_1.base.geometry_basic2d import SurfaceProperty
from generated.gml.pkg_3.pkg_1.pkg_1.base.gml_base import AbstractGmltype
from generated.xlink import (
    ActuateType,
    ShowType,
    TypeType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class AbstractTopologyType(AbstractGmltype):
    pass


@dataclass
class ContainerPropertyType:
    face: Optional["Face"] = field(
        default=None,
        metadata={
            "name": "Face",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    topo_solid: Optional["TopoSolid"] = field(
        default=None,
        metadata={
            "name": "TopoSolid",
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
class DirectedEdgePropertyType:
    edge: Optional["Edge"] = field(
        default=None,
        metadata={
            "name": "Edge",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    orientation: SignType = field(
        default=SignType.VALUE,
        metadata={
            "type": "Attribute",
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
class DirectedFacePropertyType:
    face: Optional["Face"] = field(
        default=None,
        metadata={
            "name": "Face",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    orientation: SignType = field(
        default=SignType.VALUE,
        metadata={
            "type": "Attribute",
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
class DirectedNodePropertyType:
    node: Optional["Node"] = field(
        default=None,
        metadata={
            "name": "Node",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    orientation: SignType = field(
        default=SignType.VALUE,
        metadata={
            "type": "Attribute",
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
class DirectedTopoSolidPropertyType:
    topo_solid: Optional["TopoSolid"] = field(
        default=None,
        metadata={
            "name": "TopoSolid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    orientation: SignType = field(
        default=SignType.VALUE,
        metadata={
            "type": "Attribute",
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
class IsolatedPropertyType:
    node: Optional["Node"] = field(
        default=None,
        metadata={
            "name": "Node",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    edge: Optional["Edge"] = field(
        default=None,
        metadata={
            "name": "Edge",
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
class Topology(AbstractTopologyType):
    class Meta:
        name = "_Topology"
        namespace = "http://www.opengis.net/gml"


@dataclass
class Container(ContainerPropertyType):
    class Meta:
        name = "container"
        namespace = "http://www.opengis.net/gml"


@dataclass
class DirectedEdge(DirectedEdgePropertyType):
    class Meta:
        name = "directedEdge"
        namespace = "http://www.opengis.net/gml"


@dataclass
class DirectedFace(DirectedFacePropertyType):
    class Meta:
        name = "directedFace"
        namespace = "http://www.opengis.net/gml"


@dataclass
class DirectedNode(DirectedNodePropertyType):
    class Meta:
        name = "directedNode"
        namespace = "http://www.opengis.net/gml"


@dataclass
class DirectedTopoSolid(DirectedTopoSolidPropertyType):
    class Meta:
        name = "directedTopoSolid"
        namespace = "http://www.opengis.net/gml"


@dataclass
class Isolated(IsolatedPropertyType):
    class Meta:
        name = "isolated"
        namespace = "http://www.opengis.net/gml"


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
class TopoComplexProperty(TopoComplexMemberType):
    class Meta:
        name = "topoComplexProperty"
        namespace = "http://www.opengis.net/gml"


@dataclass
class AbstractTopoPrimitiveType(AbstractTopologyType):
    isolated: List[Isolated] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    container: Optional[Container] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )


@dataclass
class TopoCurveType(AbstractTopologyType):
    """The end Node of each directedEdge of a TopoCurveType is the start Node
    of the next directedEdge of the TopoCurveType in document order.

    The TopoCurve type and element represent a homogeneous topological
    expression, a list of directed edges, which if realised are
    isomorphic to a geometric curve primitive. The intended use of
    TopoCurve is to appear within a line feature instance to express the
    structural and geometric relationships of this line to other
    features via the shared edge definitions.
    """
    directed_edge: List[DirectedEdge] = field(
        default_factory=list,
        metadata={
            "name": "directedEdge",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "min_occurs": 1,
        }
    )


@dataclass
class TopoPointType(AbstractTopologyType):
    """The intended use of TopoPoint is to appear within a point feature to
    express the structural and possibly geometric relationships of this point
    to other features via shared node definitions.

    Note the orientation assigned to the directedNode has no meaning in
    this context. It is preserved for symmetry with the types and
    elements which follow.
    """
    directed_node: Optional[DirectedNode] = field(
        default=None,
        metadata={
            "name": "directedNode",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )


@dataclass
class TopoSurfaceType(AbstractTopologyType):
    """The TopoSurface type and element represent a homogeneous topological
    expression, a set of directed faces, which if realised are isomorphic to a
    geometric surface primitive.

    The intended use of TopoSurface is to appear within a surface
    feature instance to express the structural and possibly geometric
    relationships of this surface to other features via the shared face
    definitions.
    """
    directed_face: List[DirectedFace] = field(
        default_factory=list,
        metadata={
            "name": "directedFace",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "min_occurs": 1,
        }
    )


@dataclass
class TopoVolumeType(AbstractTopologyType):
    """The TopoVolume type and element represent a homogeneous topological
    expression, a set of directed TopoSolids, which if realised are isomorphic
    to a geometric solid primitive.

    The intended use of TopoVolume is to appear within a 3D solid
    feature instance to express the structural and geometric
    relationships of this solid to other features via the shared
    TopoSolid definitions.  . Note the orientation assigned to the
    directedSolid has no meaning in three dimensions. It is preserved
    for symmetry with the preceding types and elements.
    """
    directed_topo_solid: List[DirectedTopoSolid] = field(
        default_factory=list,
        metadata={
            "name": "directedTopoSolid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "min_occurs": 1,
        }
    )


@dataclass
class EdgeType(AbstractTopoPrimitiveType):
    """There is precisely one positively directed and one negatively directed
    node in the boundary of every edge.

    The negatively and positively directed nodes correspond to the start
    and end nodes respectively. The optional coboundary of an edge is a
    circular sequence of directed faces which are incident on this edge
    in document order. Faces which use a particular boundary edge in its
    positive orientation appear with positive orientation on the
    coboundary of the same edge. In the 2D case, the orientation of the
    face on the left of the edge is "+"; the orientation of the face on
    the right on its right is "-". An edge may optionally be realised by
    a 1-dimensional (curve) geometric primitive.
    """
    directed_node: List[DirectedNode] = field(
        default_factory=list,
        metadata={
            "name": "directedNode",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "min_occurs": 2,
            "max_occurs": 2,
        }
    )
    directed_face: List[DirectedFace] = field(
        default_factory=list,
        metadata={
            "name": "directedFace",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    curve_property: Optional[CurveProperty] = field(
        default=None,
        metadata={
            "name": "curveProperty",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )


@dataclass
class FaceType(AbstractTopoPrimitiveType):
    """. The topological boundary of a face consists of a set of directed edges. Note that all edges associated with a Face, including dangling and interior edges, appear in the boundary.  Dangling and interior edges are each referenced by pairs of directedEdges with opposing orientations.  The optional coboundary of a face is a pair of directed solids which are bounded by this face. If present, there is precisely one positively directed and one negatively directed solid in the coboundary of every face. The positively directed solid corresponds to the solid which lies in the direction of the positively directed normal to the face in any geometric realisation.  A face may optionally be realised by a 2-dimensional (surface) geometric primitive."""
    directed_edge: List["DirectedEdge"] = field(
        default_factory=list,
        metadata={
            "name": "directedEdge",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "min_occurs": 1,
        }
    )
    directed_topo_solid: List[DirectedTopoSolid] = field(
        default_factory=list,
        metadata={
            "name": "directedTopoSolid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "max_occurs": 2,
        }
    )
    surface_property: Optional[SurfaceProperty] = field(
        default=None,
        metadata={
            "name": "surfaceProperty",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )


@dataclass
class NodeType(AbstractTopoPrimitiveType):
    """Its optional co-boundary is a set of connected directedEdges.

    The orientation of one of these dirEdges is "+" if the Node is the
    "to" node of the Edge, and "-" if it is the "from" node.
    """
    directed_edge: List[DirectedEdge] = field(
        default_factory=list,
        metadata={
            "name": "directedEdge",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    point_property: Optional[PointProperty] = field(
        default=None,
        metadata={
            "name": "pointProperty",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )


@dataclass
class TopoCurve(TopoCurveType):
    class Meta:
        namespace = "http://www.opengis.net/gml"


@dataclass
class TopoPoint(TopoPointType):
    class Meta:
        namespace = "http://www.opengis.net/gml"


@dataclass
class TopoSolidType(AbstractTopoPrimitiveType):
    """The topological boundary of a TopoSolid consists of a set of directed
    faces.

    Note that all faces associated with the TopoSolid, including
    dangling faces, appear in the boundary. The coboundary of a
    TopoSolid is empty and hence requires no representation.
    """
    directed_face: List[DirectedFace] = field(
        default_factory=list,
        metadata={
            "name": "directedFace",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "min_occurs": 1,
        }
    )


@dataclass
class TopoSurface(TopoSurfaceType):
    class Meta:
        namespace = "http://www.opengis.net/gml"


@dataclass
class TopoVolume(TopoVolumeType):
    class Meta:
        namespace = "http://www.opengis.net/gml"


@dataclass
class TopoPrimitive(AbstractTopoPrimitiveType):
    """
    Substitution group branch for Topo Primitives, used by
    TopoPrimitiveArrayAssociationType.
    """
    class Meta:
        name = "_TopoPrimitive"
        namespace = "http://www.opengis.net/gml"


@dataclass
class Edge(EdgeType):
    class Meta:
        namespace = "http://www.opengis.net/gml"


@dataclass
class Face(FaceType):
    class Meta:
        namespace = "http://www.opengis.net/gml"


@dataclass
class Node(NodeType):
    class Meta:
        namespace = "http://www.opengis.net/gml"


@dataclass
class TopoCurvePropertyType:
    topo_curve: Optional[TopoCurve] = field(
        default=None,
        metadata={
            "name": "TopoCurve",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )


@dataclass
class TopoPointPropertyType:
    topo_point: Optional[TopoPoint] = field(
        default=None,
        metadata={
            "name": "TopoPoint",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )


@dataclass
class TopoSolid(TopoSolidType):
    class Meta:
        namespace = "http://www.opengis.net/gml"


@dataclass
class TopoSurfacePropertyType:
    topo_surface: Optional[TopoSurface] = field(
        default=None,
        metadata={
            "name": "TopoSurface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )


@dataclass
class TopoVolumePropertyType:
    topo_volume: Optional[TopoVolume] = field(
        default=None,
        metadata={
            "name": "TopoVolume",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )


@dataclass
class TopoPrimitiveArrayAssociationType:
    """
    This type supports embedding an array of topological primitives in a
    TopoComplex.
    """
    topo_solid: List[TopoSolid] = field(
        default_factory=list,
        metadata={
            "name": "TopoSolid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "sequential": True,
        }
    )
    face: List[Face] = field(
        default_factory=list,
        metadata={
            "name": "Face",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "sequential": True,
        }
    )
    edge: List[Edge] = field(
        default_factory=list,
        metadata={
            "name": "Edge",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "sequential": True,
        }
    )
    node: List[Node] = field(
        default_factory=list,
        metadata={
            "name": "Node",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "sequential": True,
        }
    )
    topo_primitive: List[TopoPrimitive] = field(
        default_factory=list,
        metadata={
            "name": "_TopoPrimitive",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "sequential": True,
        }
    )


@dataclass
class TopoPrimitiveMemberType:
    """
    This type supports embedding topological primitives in a TopoComplex.
    """
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
    topo_primitive: Optional[TopoPrimitive] = field(
        default=None,
        metadata={
            "name": "_TopoPrimitive",
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
class TopoCurveProperty(TopoCurvePropertyType):
    class Meta:
        name = "topoCurveProperty"
        namespace = "http://www.opengis.net/gml"


@dataclass
class TopoPointProperty(TopoPointPropertyType):
    class Meta:
        name = "topoPointProperty"
        namespace = "http://www.opengis.net/gml"


@dataclass
class TopoSurfaceProperty(TopoSurfacePropertyType):
    class Meta:
        name = "topoSurfaceProperty"
        namespace = "http://www.opengis.net/gml"


@dataclass
class TopoVolumeProperty(TopoVolumePropertyType):
    class Meta:
        name = "topoVolumeProperty"
        namespace = "http://www.opengis.net/gml"


@dataclass
class TopoPrimitiveMember(TopoPrimitiveMemberType):
    class Meta:
        name = "topoPrimitiveMember"
        namespace = "http://www.opengis.net/gml"


@dataclass
class TopoPrimitiveMembers(TopoPrimitiveArrayAssociationType):
    class Meta:
        name = "topoPrimitiveMembers"
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
