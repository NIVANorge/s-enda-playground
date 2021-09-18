from dataclasses import dataclass, field
from typing import List, Optional
from generated.gml.pkg_3.pkg_1.pkg_1.base.geometry_basic0d1d import (
    AbstractGeometricPrimitiveType,
    AbstractGeometryType,
    Coord,
    Coordinates,
    PointProperty,
    PointRep,
    Pos,
    PosList,
)
from generated.gml.pkg_3.pkg_1.pkg_1.base.geometry_complexes import CompositeSurface
from generated.gml.pkg_3.pkg_1.pkg_1.base.geometry_primitives import (
    OrientableSurface,
    PolyhedralSurface,
    Ring1,
    Surface1,
    Tin,
    TriangulatedSurface,
)
from generated.xlink import (
    ActuateType,
    ShowType,
    TypeType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class AbstractRingType(AbstractGeometryType):
    """
    An abstraction of a ring to support surface boundaries of different
    complexity.
    """


@dataclass
class AbstractSurfaceType(AbstractGeometricPrimitiveType):
    """An abstraction of a surface to support the different levels of
    complexity.

    A surface is always a continuous region of a plane.
    """


@dataclass
class LinearRingType(AbstractRingType):
    """
    A LinearRing is defined by four or more coordinate tuples, with linear
    interpolation between them; the first and last coordinates must be
    coincident.

    :ivar pos:
    :ivar point_property:
    :ivar point_rep: Deprecated with GML version 3.1.0. Use
        "pointProperty" instead. Included for backwards compatibility
        with GML 3.0.0.
    :ivar pos_list:
    :ivar coordinates: Deprecated with GML version 3.1.0. Use "posList"
        instead.
    :ivar coord: Deprecated with GML version 3.0 and included for
        backwards compatibility with GML 2. Use "pos" elements instead.
    """
    pos: List[Pos] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "min_occurs": 4,
            "sequential": True,
        }
    )
    point_property: List[PointProperty] = field(
        default_factory=list,
        metadata={
            "name": "pointProperty",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "min_occurs": 4,
            "sequential": True,
        }
    )
    point_rep: List[PointRep] = field(
        default_factory=list,
        metadata={
            "name": "pointRep",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "min_occurs": 4,
            "sequential": True,
        }
    )
    pos_list: Optional[PosList] = field(
        default=None,
        metadata={
            "name": "posList",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    coordinates: Optional[Coordinates] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    coord: List[Coord] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )


@dataclass
class Ring2(AbstractRingType):
    """
    The "_Ring" element is the abstract head of the substituition group for all
    closed boundaries of a surface patch.
    """
    class Meta:
        name = "_Ring"
        namespace = "http://www.opengis.net/gml"


@dataclass
class Surface2(AbstractSurfaceType):
    """
    The "_Surface" element is the abstract head of the substituition group for
    all (continuous) surface elements.
    """
    class Meta:
        name = "_Surface"
        namespace = "http://www.opengis.net/gml"


@dataclass
class LinearRing(LinearRingType):
    class Meta:
        namespace = "http://www.opengis.net/gml"


@dataclass
class AbstractRingPropertyType:
    """
    Encapsulates a ring to represent the surface boundary property of a
    surface.
    """
    ring: Optional[Ring1] = field(
        default=None,
        metadata={
            "name": "Ring",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    linear_ring: Optional[LinearRing] = field(
        default=None,
        metadata={
            "name": "LinearRing",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    opengis_net_gml_ring: Optional[Ring2] = field(
        default=None,
        metadata={
            "name": "_Ring",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )


@dataclass
class LinearRingPropertyType:
    """
    Encapsulates a ring to represent properties in features or geometry
    collections.
    """
    linear_ring: Optional[LinearRing] = field(
        default=None,
        metadata={
            "name": "LinearRing",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )


@dataclass
class Exterior(AbstractRingPropertyType):
    """A boundary of a surface consists of a number of rings.

    In the normal 2D case, one of these rings is distinguished as being
    the exterior boundary. In a general manifold this is not always
    possible, in which case all boundaries shall be listed as interior
    boundaries, and the exterior will be empty.
    """
    class Meta:
        name = "exterior"
        namespace = "http://www.opengis.net/gml"


@dataclass
class InnerBoundaryIs(AbstractRingPropertyType):
    """Deprecated with GML 3.0, included only for backwards compatibility with
    GML 2.

    Use "interior" instead.
    """
    class Meta:
        name = "innerBoundaryIs"
        namespace = "http://www.opengis.net/gml"


@dataclass
class Interior(AbstractRingPropertyType):
    """A boundary of a surface consists of a number of rings.

    The "interior" rings seperate the surface / surface patch from the
    area enclosed by the rings.
    """
    class Meta:
        name = "interior"
        namespace = "http://www.opengis.net/gml"


@dataclass
class OuterBoundaryIs(AbstractRingPropertyType):
    """Deprecated with GML 3.0, included only for backwards compatibility with
    GML 2.

    Use "exterior" instead.
    """
    class Meta:
        name = "outerBoundaryIs"
        namespace = "http://www.opengis.net/gml"


@dataclass
class PolygonType(AbstractSurfaceType):
    """A Polygon is a special surface that is defined by a single surface
    patch.

    The boundary of this patch is coplanar and the polygon uses planar
    interpolation in its interior. It is backwards compatible with the
    Polygon of GML 2, GM_Polygon of ISO 19107 is implemented by
    PolygonPatch.
    """
    outer_boundary_is: Optional[OuterBoundaryIs] = field(
        default=None,
        metadata={
            "name": "outerBoundaryIs",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    exterior: Optional[Exterior] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    inner_boundary_is: List[InnerBoundaryIs] = field(
        default_factory=list,
        metadata={
            "name": "innerBoundaryIs",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    interior: List[Interior] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )


@dataclass
class Polygon(PolygonType):
    class Meta:
        namespace = "http://www.opengis.net/gml"


@dataclass
class PolygonPropertyType:
    """This type is deprecated with GML 3 and shall not be used.

    It is included for backwards compatibility with GML 2. Use
    SurfacePropertyType instead. A property that has a polygon as its
    value domain can either be an appropriate geometry element
    encapsulated in an element of this type or an XLink reference to a
    remote geometry element (where remote includes geometry elements
    located elsewhere in the same document). Either the reference or the
    contained element must be given, but neither both nor none.
    """
    polygon: Optional[Polygon] = field(
        default=None,
        metadata={
            "name": "Polygon",
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
class SurfaceArrayPropertyType:
    """A container for an array of surfaces.

    The elements are always contained in the array property, referencing
    geometry elements or arrays of geometry elements is not supported.
    """
    orientable_surface: List[OrientableSurface] = field(
        default_factory=list,
        metadata={
            "name": "OrientableSurface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    tin: List[Tin] = field(
        default_factory=list,
        metadata={
            "name": "Tin",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    triangulated_surface: List[TriangulatedSurface] = field(
        default_factory=list,
        metadata={
            "name": "TriangulatedSurface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    polyhedral_surface: List[PolyhedralSurface] = field(
        default_factory=list,
        metadata={
            "name": "PolyhedralSurface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    surface: List[Surface1] = field(
        default_factory=list,
        metadata={
            "name": "Surface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    composite_surface: List[CompositeSurface] = field(
        default_factory=list,
        metadata={
            "name": "CompositeSurface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    polygon: List[Polygon] = field(
        default_factory=list,
        metadata={
            "name": "Polygon",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    opengis_net_gml_surface: List[Surface2] = field(
        default_factory=list,
        metadata={
            "name": "_Surface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )


@dataclass
class SurfacePropertyType:
    """A property that has a surface as its value domain can either be an
    appropriate geometry element encapsulated in an element of this type or an
    XLink reference to a remote geometry element (where remote includes
    geometry elements located elsewhere in the same document).

    Either the reference or the contained element must be given, but
    neither both nor none.
    """
    orientable_surface: Optional[OrientableSurface] = field(
        default=None,
        metadata={
            "name": "OrientableSurface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    tin: Optional[Tin] = field(
        default=None,
        metadata={
            "name": "Tin",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    triangulated_surface: Optional[TriangulatedSurface] = field(
        default=None,
        metadata={
            "name": "TriangulatedSurface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    polyhedral_surface: Optional[PolyhedralSurface] = field(
        default=None,
        metadata={
            "name": "PolyhedralSurface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    surface: Optional[Surface1] = field(
        default=None,
        metadata={
            "name": "Surface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    composite_surface: Optional[CompositeSurface] = field(
        default=None,
        metadata={
            "name": "CompositeSurface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    polygon: Optional[Polygon] = field(
        default=None,
        metadata={
            "name": "Polygon",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    opengis_net_gml_surface: Optional[Surface2] = field(
        default=None,
        metadata={
            "name": "_Surface",
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
class PolygonProperty(PolygonPropertyType):
    """Deprecated with GML 3.0 and included only for backwards compatibility
    with GML 2.0.

    Use "surfaceProperty" instead. This property element either
    references a polygon via the XLink-attributes or contains the
    polygon element.
    """
    class Meta:
        name = "polygonProperty"
        namespace = "http://www.opengis.net/gml"


@dataclass
class SurfaceArrayProperty(SurfaceArrayPropertyType):
    class Meta:
        name = "surfaceArrayProperty"
        namespace = "http://www.opengis.net/gml"


@dataclass
class SurfaceProperty(SurfacePropertyType):
    """This property element either references a surface via the XLink-
    attributes or contains the surface element.

    surfaceProperty is the predefined property which can be used by GML
    Application Schemas whenever a GML Feature has a property with a
    value that is substitutable for _Surface.
    """
    class Meta:
        name = "surfaceProperty"
        namespace = "http://www.opengis.net/gml"
