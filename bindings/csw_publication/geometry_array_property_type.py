from dataclasses import dataclass, field
from typing import List, Optional
from bindings.csw_publication.abstract_geometric_aggregate_type import AbstractGeometricAggregateType
from bindings.csw_publication.actuate_type import ActuateType
from bindings.csw_publication.composite_curve_type import (
    CompositeCurve,
    Curve1,
    OrientableCurve,
)
from bindings.csw_publication.composite_solid_type import CompositeSolid
from bindings.csw_publication.composite_surface_type import (
    CompositeSurface,
    OrientableSurface,
)
from bindings.csw_publication.curve_2 import Curve2
from bindings.csw_publication.geometric_aggregate import GeometricAggregate
from bindings.csw_publication.geometric_complex import GeometricComplex
from bindings.csw_publication.geometric_primitive import GeometricPrimitive
from bindings.csw_publication.geometry import Geometry
from bindings.csw_publication.grid import Grid
from bindings.csw_publication.implicit_geometry import ImplicitGeometry
from bindings.csw_publication.line_string import LineString
from bindings.csw_publication.linear_ring import LinearRing
from bindings.csw_publication.multi_curve import MultiCurve
from bindings.csw_publication.multi_line_string import MultiLineString
from bindings.csw_publication.multi_point import MultiPoint
from bindings.csw_publication.multi_polygon import MultiPolygon
from bindings.csw_publication.multi_solid import MultiSolid
from bindings.csw_publication.multi_surface import MultiSurface
from bindings.csw_publication.point import Point
from bindings.csw_publication.polygon import Polygon
from bindings.csw_publication.polyhedral_surface import PolyhedralSurface
from bindings.csw_publication.rectified_grid import RectifiedGrid
from bindings.csw_publication.ring_1 import Ring1
from bindings.csw_publication.ring_2 import Ring2
from bindings.csw_publication.show_type import ShowType
from bindings.csw_publication.solid_1 import Solid1
from bindings.csw_publication.solid_2 import Solid2
from bindings.csw_publication.surface_1 import Surface1
from bindings.csw_publication.surface_2 import Surface2
from bindings.csw_publication.tin import Tin
from bindings.csw_publication.triangulated_surface import TriangulatedSurface
from bindings.csw_publication.type_type import TypeType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class GeometryArrayPropertyType:
    """A container for an array of geometry elements.

    The elements are always contained in the array property, referencing
    geometry elements or arrays of geometry elements is not supported.
    """
    multi_line_string: List[MultiLineString] = field(
        default_factory=list,
        metadata={
            "name": "MultiLineString",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    multi_polygon: List[MultiPolygon] = field(
        default_factory=list,
        metadata={
            "name": "MultiPolygon",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    multi_solid: List[MultiSolid] = field(
        default_factory=list,
        metadata={
            "name": "MultiSolid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    multi_surface: List[MultiSurface] = field(
        default_factory=list,
        metadata={
            "name": "MultiSurface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    multi_curve: List[MultiCurve] = field(
        default_factory=list,
        metadata={
            "name": "MultiCurve",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    multi_point: List[MultiPoint] = field(
        default_factory=list,
        metadata={
            "name": "MultiPoint",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    multi_geometry: List["MultiGeometry"] = field(
        default_factory=list,
        metadata={
            "name": "MultiGeometry",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    geometric_aggregate: List[GeometricAggregate] = field(
        default_factory=list,
        metadata={
            "name": "_GeometricAggregate",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    rectified_grid: List[RectifiedGrid] = field(
        default_factory=list,
        metadata={
            "name": "RectifiedGrid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    grid: List[Grid] = field(
        default_factory=list,
        metadata={
            "name": "Grid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    implicit_geometry: List[ImplicitGeometry] = field(
        default_factory=list,
        metadata={
            "name": "_ImplicitGeometry",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    geometric_complex: List[GeometricComplex] = field(
        default_factory=list,
        metadata={
            "name": "GeometricComplex",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    ring: List[Ring1] = field(
        default_factory=list,
        metadata={
            "name": "Ring",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    linear_ring: List[LinearRing] = field(
        default_factory=list,
        metadata={
            "name": "LinearRing",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    opengis_net_gml_ring: List[Ring2] = field(
        default_factory=list,
        metadata={
            "name": "_Ring",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    solid: List[Solid1] = field(
        default_factory=list,
        metadata={
            "name": "Solid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    composite_solid: List[CompositeSolid] = field(
        default_factory=list,
        metadata={
            "name": "CompositeSolid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    opengis_net_gml_solid: List[Solid2] = field(
        default_factory=list,
        metadata={
            "name": "_Solid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
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
    orientable_curve: List[OrientableCurve] = field(
        default_factory=list,
        metadata={
            "name": "OrientableCurve",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    curve: List[Curve1] = field(
        default_factory=list,
        metadata={
            "name": "Curve",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    composite_curve: List[CompositeCurve] = field(
        default_factory=list,
        metadata={
            "name": "CompositeCurve",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    line_string: List[LineString] = field(
        default_factory=list,
        metadata={
            "name": "LineString",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    opengis_net_gml_curve: List[Curve2] = field(
        default_factory=list,
        metadata={
            "name": "_Curve",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    point: List[Point] = field(
        default_factory=list,
        metadata={
            "name": "Point",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    geometric_primitive: List[GeometricPrimitive] = field(
        default_factory=list,
        metadata={
            "name": "_GeometricPrimitive",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    geometry: List[Geometry] = field(
        default_factory=list,
        metadata={
            "name": "_Geometry",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )


@dataclass
class GeometryPropertyType:
    """A geometric property can either be any geometry element encapsulated in
    an element of this type or an XLink reference to a remote geometry element
    (where remote includes geometry elements located elsewhere in the same
    document).

    Note that either the reference or the contained element must be
    given, but not both or none.
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
    multi_geometry: Optional["MultiGeometry"] = field(
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
    rectified_grid: Optional[RectifiedGrid] = field(
        default=None,
        metadata={
            "name": "RectifiedGrid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    grid: Optional[Grid] = field(
        default=None,
        metadata={
            "name": "Grid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    implicit_geometry: Optional[ImplicitGeometry] = field(
        default=None,
        metadata={
            "name": "_ImplicitGeometry",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    geometric_complex: Optional[GeometricComplex] = field(
        default=None,
        metadata={
            "name": "GeometricComplex",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
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
    solid: Optional[Solid1] = field(
        default=None,
        metadata={
            "name": "Solid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    composite_solid: Optional[CompositeSolid] = field(
        default=None,
        metadata={
            "name": "CompositeSolid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    opengis_net_gml_solid: Optional[Solid2] = field(
        default=None,
        metadata={
            "name": "_Solid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
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
    orientable_curve: Optional[OrientableCurve] = field(
        default=None,
        metadata={
            "name": "OrientableCurve",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    curve: Optional[Curve1] = field(
        default=None,
        metadata={
            "name": "Curve",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    composite_curve: Optional[CompositeCurve] = field(
        default=None,
        metadata={
            "name": "CompositeCurve",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    line_string: Optional[LineString] = field(
        default=None,
        metadata={
            "name": "LineString",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    opengis_net_gml_curve: Optional[Curve2] = field(
        default=None,
        metadata={
            "name": "_Curve",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    point: Optional[Point] = field(
        default=None,
        metadata={
            "name": "Point",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    geometric_primitive: Optional[GeometricPrimitive] = field(
        default=None,
        metadata={
            "name": "_GeometricPrimitive",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    geometry: Optional[Geometry] = field(
        default=None,
        metadata={
            "name": "_Geometry",
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
class MultiGeometry(MultiGeometryType):
    class Meta:
        namespace = "http://www.opengis.net/gml"
