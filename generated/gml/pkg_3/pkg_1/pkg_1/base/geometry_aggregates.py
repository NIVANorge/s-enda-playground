from dataclasses import dataclass, field
from typing import List, Optional
from generated.gml.pkg_3.pkg_1.pkg_1.base.geometry_basic0d1d import (
    AbstractGeometryType,
    CurveArrayPropertyType,
    GeometryArrayPropertyType,
    GeometryPropertyType,
    LineStringPropertyType,
    PointArrayPropertyType,
    PointPropertyType,
)
from generated.gml.pkg_3.pkg_1.pkg_1.base.geometry_basic2d import (
    PolygonPropertyType,
    SurfaceArrayPropertyType,
    SurfacePropertyType,
)
from generated.gml.pkg_3.pkg_1.pkg_1.base.geometry_primitives import (
    SolidArrayPropertyType,
    SolidPropertyType,
    CurveMember,
)
from generated.xlink import (
    ActuateType,
    ShowType,
    TypeType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class AbstractGeometricAggregateType(AbstractGeometryType):
    """
    This is the abstract root type of the geometric aggregates.
    """


@dataclass
class CurveMembers(CurveArrayPropertyType):
    """This property element contains a list of curves.

    The order of the elements is significant and shall be preserved when
    processing the array.
    """
    class Meta:
        name = "curveMembers"
        namespace = "http://www.opengis.net/gml"


@dataclass
class GeometryMember(GeometryPropertyType):
    """
    This property element either references a geometry element via the XLink-
    attributes or contains the geometry element.
    """
    class Meta:
        name = "geometryMember"
        namespace = "http://www.opengis.net/gml"


@dataclass
class GeometryMembers(GeometryArrayPropertyType):
    """This property element contains a list of geometry elements.

    The order of the elements is significant and shall be preserved when
    processing the array.
    """
    class Meta:
        name = "geometryMembers"
        namespace = "http://www.opengis.net/gml"


@dataclass
class LineStringMember(LineStringPropertyType):
    """Deprecated with GML 3.0 and included only for backwards compatibility
    with GML 2.0.

    Use "curveMember" instead. This property element either references a
    line string via the XLink-attributes or contains the line string
    element.
    """
    class Meta:
        name = "lineStringMember"
        namespace = "http://www.opengis.net/gml"


@dataclass
class PointMember(PointPropertyType):
    """
    This property element either references a Point via the XLink-attributes or
    contains the Point element.
    """
    class Meta:
        name = "pointMember"
        namespace = "http://www.opengis.net/gml"


@dataclass
class PointMembers(PointArrayPropertyType):
    """This property element contains a list of points.

    The order of the elements is significant and shall be preserved when
    processing the array.
    """
    class Meta:
        name = "pointMembers"
        namespace = "http://www.opengis.net/gml"


@dataclass
class PolygonMember(PolygonPropertyType):
    """Deprecated with GML 3.0 and included only for backwards compatibility
    with GML 2.0.

    Use "surfaceMember" instead. This property element either references
    a polygon via the XLink-attributes or contains the polygon element.
    """
    class Meta:
        name = "polygonMember"
        namespace = "http://www.opengis.net/gml"


@dataclass
class SolidMember(SolidPropertyType):
    """This property element either references a solid via the XLink-attributes
    or contains the solid element.

    A solid element is any element which is substitutable for "_Solid".
    """
    class Meta:
        name = "solidMember"
        namespace = "http://www.opengis.net/gml"


@dataclass
class SolidMembers(SolidArrayPropertyType):
    """This property element contains a list of solids.

    The order of the elements is significant and shall be preserved when
    processing the array.
    """
    class Meta:
        name = "solidMembers"
        namespace = "http://www.opengis.net/gml"


@dataclass
class SurfaceMember(SurfacePropertyType):
    """This property element either references a surface via the XLink-
    attributes or contains the surface element.

    A surface element is any element which is substitutable for
    "_Surface".
    """
    class Meta:
        name = "surfaceMember"
        namespace = "http://www.opengis.net/gml"


@dataclass
class SurfaceMembers(SurfaceArrayPropertyType):
    """This property element contains a list of surfaces.

    The order of the elements is significant and shall be preserved when
    processing the array.
    """
    class Meta:
        name = "surfaceMembers"
        namespace = "http://www.opengis.net/gml"


@dataclass
class MultiCurveType(AbstractGeometricAggregateType):
    """
    A MultiCurve is defined by one or more Curves, referenced through
    curveMember elements.
    """
    curve_member: List[CurveMember] = field(
        default_factory=list,
        metadata={
            "name": "curveMember",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    curve_members: Optional[CurveMembers] = field(
        default=None,
        metadata={
            "name": "curveMembers",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )


@dataclass
class MultiGeometryType(AbstractGeometricAggregateType):
    """
    A geometry collection must include one or more geometries, referenced
    through geometryMember elements.
    """
    geometry_member: List[GeometryMember] = field(
        default_factory=list,
        metadata={
            "name": "geometryMember",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    geometry_members: Optional[GeometryMembers] = field(
        default=None,
        metadata={
            "name": "geometryMembers",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )


@dataclass
class MultiLineStringType(AbstractGeometricAggregateType):
    """A MultiLineString is defined by one or more LineStrings, referenced
    through lineStringMember elements.

    Deprecated with GML version 3.0. Use MultiCurveType instead.
    """
    line_string_member: List[LineStringMember] = field(
        default_factory=list,
        metadata={
            "name": "lineStringMember",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )


@dataclass
class MultiPointType(AbstractGeometricAggregateType):
    """
    A MultiPoint is defined by one or more Points, referenced through
    pointMember elements.
    """
    point_member: List[PointMember] = field(
        default_factory=list,
        metadata={
            "name": "pointMember",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    point_members: Optional[PointMembers] = field(
        default=None,
        metadata={
            "name": "pointMembers",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )


@dataclass
class MultiPolygonType(AbstractGeometricAggregateType):
    """A MultiPolygon is defined by one or more Polygons, referenced through
    polygonMember elements.

    Deprecated with GML version 3.0. Use MultiSurfaceType instead.
    """
    polygon_member: List[PolygonMember] = field(
        default_factory=list,
        metadata={
            "name": "polygonMember",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )


@dataclass
class MultiSolidType(AbstractGeometricAggregateType):
    """
    A MultiSolid is defined by one or more Solids, referenced through
    solidMember elements.
    """
    solid_member: List[SolidMember] = field(
        default_factory=list,
        metadata={
            "name": "solidMember",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    solid_members: Optional[SolidMembers] = field(
        default=None,
        metadata={
            "name": "solidMembers",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )


@dataclass
class MultiSurfaceType(AbstractGeometricAggregateType):
    """
    A MultiSurface is defined by one or more Surfaces, referenced through
    surfaceMember elements.
    """
    surface_member: List[SurfaceMember] = field(
        default_factory=list,
        metadata={
            "name": "surfaceMember",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    surface_members: Optional[SurfaceMembers] = field(
        default=None,
        metadata={
            "name": "surfaceMembers",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )


@dataclass
class GeometricAggregate(AbstractGeometricAggregateType):
    """
    The "_GeometricAggregate" element is the abstract head of the substituition
    group for all geometric aggremates.
    """
    class Meta:
        name = "_GeometricAggregate"
        namespace = "http://www.opengis.net/gml"


@dataclass
class MultiCurve(MultiCurveType):
    class Meta:
        namespace = "http://www.opengis.net/gml"


@dataclass
class MultiGeometry(MultiGeometryType):
    class Meta:
        namespace = "http://www.opengis.net/gml"


@dataclass
class MultiLineString(MultiLineStringType):
    """Deprecated with GML 3.0 and included for backwards compatibility with
    GML 2.

    Use the "MultiCurve" element instead.
    """
    class Meta:
        namespace = "http://www.opengis.net/gml"


@dataclass
class MultiPoint(MultiPointType):
    class Meta:
        namespace = "http://www.opengis.net/gml"


@dataclass
class MultiPolygon(MultiPolygonType):
    """Deprecated with GML 3.0 and included for backwards compatibility with
    GML 2.

    Use the "MultiSurface" element instead.
    """
    class Meta:
        namespace = "http://www.opengis.net/gml"


@dataclass
class MultiSolid(MultiSolidType):
    class Meta:
        namespace = "http://www.opengis.net/gml"


@dataclass
class MultiSurface(MultiSurfaceType):
    class Meta:
        namespace = "http://www.opengis.net/gml"


@dataclass
class MultiCurvePropertyType:
    """A property that has a collection of curves as its value domain can
    either be an appropriate geometry element encapsulated in an element of
    this type or an XLink reference to a remote geometry element (where remote
    includes geometry elements located elsewhere in the same document).

    Either the reference or the contained element must be given, but
    neither both nor none.
    """
    multi_curve: Optional[MultiCurve] = field(
        default=None,
        metadata={
            "name": "MultiCurve",
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
class MultiGeometryPropertyType:
    """A property that has a geometric aggregate as its value domain can either
    be an appropriate geometry element encapsulated in an element of this type
    or an XLink reference to a remote geometry element (where remote includes
    geometry elements located elsewhere in the same document).

    Either the reference or the contained element must be given, but
    neither both nor none.
    """
    multi_line_string: Optional[MultiLineString] = field(
        default=None,
        metadata={
            "name": "MultiLineString",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    multi_polygon: Optional[MultiPolygon] = field(
        default=None,
        metadata={
            "name": "MultiPolygon",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    multi_solid: Optional[MultiSolid] = field(
        default=None,
        metadata={
            "name": "MultiSolid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    multi_surface: Optional[MultiSurface] = field(
        default=None,
        metadata={
            "name": "MultiSurface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    multi_curve: Optional[MultiCurve] = field(
        default=None,
        metadata={
            "name": "MultiCurve",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    multi_point: Optional[MultiPoint] = field(
        default=None,
        metadata={
            "name": "MultiPoint",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    multi_geometry: Optional[MultiGeometry] = field(
        default=None,
        metadata={
            "name": "MultiGeometry",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    geometric_aggregate: Optional[GeometricAggregate] = field(
        default=None,
        metadata={
            "name": "_GeometricAggregate",
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
class MultiLineStringPropertyType:
    """This type is deprecated with GML 3 and shall not be used.

    It is included for backwards compatibility with GML 2. Use
    MultiCurvePropertyType instead. A property that has a collection of
    line strings as its value domain can either be an appropriate
    geometry element encapsulated in an element of this type or an XLink
    reference to a remote geometry element (where remote includes
    geometry elements located elsewhere in the same document). Either
    the reference or the contained element must be given, but neither
    both nor none.
    """
    multi_line_string: Optional[MultiLineString] = field(
        default=None,
        metadata={
            "name": "MultiLineString",
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
class MultiPointPropertyType:
    """A property that has a collection of points as its value domain can
    either be an appropriate geometry element encapsulated in an element of
    this type or an XLink reference to a remote geometry element (where remote
    includes geometry elements located elsewhere in the same document).

    Either the reference or the contained element must be given, but
    neither both nor none.
    """
    multi_point: Optional[MultiPoint] = field(
        default=None,
        metadata={
            "name": "MultiPoint",
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
class MultiPolygonPropertyType:
    """This type is deprecated with GML 3 and shall not be used.

    It is included for backwards compatibility with GML 2. Use
    MultiSurfacePropertyType instead. A property that has a collection
    of polygons as its value domain can either be an appropriate
    geometry element encapsulated in an element of this type or an XLink
    reference to a remote geometry element (where remote includes
    geometry elements located elsewhere in the same document). Either
    the reference or the contained element must be given, but neither
    both nor none.
    """
    multi_polygon: Optional[MultiPolygon] = field(
        default=None,
        metadata={
            "name": "MultiPolygon",
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
class MultiSolidPropertyType:
    """A property that has a collection of solids as its value domain can
    either be an appropriate geometry element encapsulated in an element of
    this type or an XLink reference to a remote geometry element (where remote
    includes geometry elements located elsewhere in the same document).

    Either the reference or the contained element must be given, but
    neither both nor none.
    """
    multi_solid: Optional[MultiSolid] = field(
        default=None,
        metadata={
            "name": "MultiSolid",
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
class MultiSurfacePropertyType:
    """A property that has a collection of surfaces as its value domain can
    either be an appropriate geometry element encapsulated in an element of
    this type or an XLink reference to a remote geometry element (where remote
    includes geometry elements located elsewhere in the same document).

    Either the reference or the contained element must be given, but
    neither both nor none.
    """
    multi_surface: Optional[MultiSurface] = field(
        default=None,
        metadata={
            "name": "MultiSurface",
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
class MultiCenterLineOf(MultiCurvePropertyType):
    class Meta:
        name = "multiCenterLineOf"
        namespace = "http://www.opengis.net/gml"


@dataclass
class MultiCenterOf(MultiPointPropertyType):
    class Meta:
        name = "multiCenterOf"
        namespace = "http://www.opengis.net/gml"


@dataclass
class MultiCoverage(MultiSurfacePropertyType):
    class Meta:
        name = "multiCoverage"
        namespace = "http://www.opengis.net/gml"


@dataclass
class MultiCurveProperty(MultiCurvePropertyType):
    """This property element either references a curve aggregate via the XLink-
    attributes or contains the "multi curve" element.

    multiCurveProperty is the predefined property which can be used by
    GML Application Schemas whenever a GML Feature has a property with a
    value that is substitutable for MultiCurve.
    """
    class Meta:
        name = "multiCurveProperty"
        namespace = "http://www.opengis.net/gml"


@dataclass
class MultiEdgeOf(MultiCurvePropertyType):
    class Meta:
        name = "multiEdgeOf"
        namespace = "http://www.opengis.net/gml"


@dataclass
class MultiExtentOf(MultiSurfacePropertyType):
    class Meta:
        name = "multiExtentOf"
        namespace = "http://www.opengis.net/gml"


@dataclass
class MultiGeometryProperty(MultiGeometryPropertyType):
    """This property element either references a geometric aggregate via the
    XLink-attributes or contains the "multi geometry" element.

    multiGeometryProperty is the predefined property which can be used
    by GML Application Schemas whenever a GML Feature has a property
    with a value that is substitutable for _GeometricAggregate.
    """
    class Meta:
        name = "multiGeometryProperty"
        namespace = "http://www.opengis.net/gml"


@dataclass
class MultiLocation(MultiPointPropertyType):
    """Deprecated with GML 3.0 and included only for backwards compatibility
    with GML 2.0.

    Use "curveMember" instead. This property element either references a
    line string via the XLink-attributes or contains the line string
    element.
    """
    class Meta:
        name = "multiLocation"
        namespace = "http://www.opengis.net/gml"


@dataclass
class MultiPointProperty(MultiPointPropertyType):
    """This property element either references a point aggregate via the XLink-
    attributes or contains the "multi point" element.

    multiPointProperty is the predefined property which can be used by
    GML Application Schemas whenever a GML Feature has a property with a
    value that is substitutable for MultiPoint.
    """
    class Meta:
        name = "multiPointProperty"
        namespace = "http://www.opengis.net/gml"


@dataclass
class MultiPosition(MultiPointPropertyType):
    class Meta:
        name = "multiPosition"
        namespace = "http://www.opengis.net/gml"


@dataclass
class MultiSolidProperty(MultiSolidPropertyType):
    """This property element either references a solid aggregate via the XLink-
    attributes or contains the "multi solid" element.

    multiSolidProperty is the predefined property which can be used by
    GML Application Schemas whenever a GML Feature has a property with a
    value that is substitutable for MultiSolid.
    """
    class Meta:
        name = "multiSolidProperty"
        namespace = "http://www.opengis.net/gml"


@dataclass
class MultiSurfaceProperty(MultiSurfacePropertyType):
    """This property element either references a surface aggregate via the
    XLink-attributes or contains the "multi surface" element.

    multiSurfaceProperty is the predefined property which can be used by
    GML Application Schemas whenever a GML Feature has a property with a
    value that is substitutable for MultiSurface.
    """
    class Meta:
        name = "multiSurfaceProperty"
        namespace = "http://www.opengis.net/gml"
