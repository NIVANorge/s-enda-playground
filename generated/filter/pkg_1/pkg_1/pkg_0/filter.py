from dataclasses import dataclass, field
from typing import List, Optional
from generated.filter.pkg_1.pkg_1.pkg_0.expr import (
    Add,
    Div,
    Function,
    Literal,
    Mul,
    PropertyName,
    Sub,
    Expression,
)
from generated.gml.pkg_3.pkg_1.pkg_1.base.feature import EnvelopeWithTimePeriod
from generated.gml.pkg_3.pkg_1.pkg_1.base.geometry_aggregates import (
    MultiCurve,
    MultiGeometry,
    MultiLineString,
    MultiPoint,
    MultiPolygon,
    MultiSolid,
    MultiSurface,
    GeometricAggregate,
)
from generated.gml.pkg_3.pkg_1.pkg_1.base.geometry_basic0d1d import (
    Envelope,
    LineString,
    Point,
    Curve2,
    GeometricPrimitive,
    Geometry,
)
from generated.gml.pkg_3.pkg_1.pkg_1.base.geometry_basic2d import (
    LinearRing,
    Polygon,
    Ring2,
    Surface2,
)
from generated.gml.pkg_3.pkg_1.pkg_1.base.geometry_complexes import (
    CompositeCurve,
    CompositeSolid,
    CompositeSurface,
    GeometricComplex,
)
from generated.gml.pkg_3.pkg_1.pkg_1.base.geometry_primitives import (
    Curve1,
    OrientableCurve,
    OrientableSurface,
    PolyhedralSurface,
    Ring1,
    Solid1,
    Surface1,
    Tin,
    TriangulatedSurface,
    Solid2,
)
from generated.gml.pkg_3.pkg_1.pkg_1.base.grids import (
    Grid,
    RectifiedGrid,
    ImplicitGeometry,
)

__NAMESPACE__ = "http://www.opengis.net/ogc"


@dataclass
class AbstractIdType:
    pass


@dataclass
class ComparisonOpsType:
    pass


@dataclass
class DistanceType:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    units: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class LogicOpsType:
    pass


@dataclass
class SpatialOpsType:
    pass


@dataclass
class Bboxtype(SpatialOpsType):
    class Meta:
        name = "BBOXType"

    property_name: Optional[PropertyName] = field(
        default=None,
        metadata={
            "name": "PropertyName",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        }
    )
    envelope_with_time_period: Optional[EnvelopeWithTimePeriod] = field(
        default=None,
        metadata={
            "name": "EnvelopeWithTimePeriod",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    envelope: Optional[Envelope] = field(
        default=None,
        metadata={
            "name": "Envelope",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )


@dataclass
class BinaryComparisonOpType(ComparisonOpsType):
    literal: List[Literal] = field(
        default_factory=list,
        metadata={
            "name": "Literal",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
            "max_occurs": 2,
        }
    )
    function: List[Function] = field(
        default_factory=list,
        metadata={
            "name": "Function",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
            "max_occurs": 2,
        }
    )
    property_name: List[PropertyName] = field(
        default_factory=list,
        metadata={
            "name": "PropertyName",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
            "max_occurs": 2,
        }
    )
    div: List[Div] = field(
        default_factory=list,
        metadata={
            "name": "Div",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
            "max_occurs": 2,
        }
    )
    mul: List[Mul] = field(
        default_factory=list,
        metadata={
            "name": "Mul",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
            "max_occurs": 2,
        }
    )
    sub: List[Sub] = field(
        default_factory=list,
        metadata={
            "name": "Sub",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
            "max_occurs": 2,
        }
    )
    add: List[Add] = field(
        default_factory=list,
        metadata={
            "name": "Add",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
            "max_occurs": 2,
        }
    )
    expression: List[Expression] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
            "max_occurs": 2,
        }
    )
    match_case: bool = field(
        default=True,
        metadata={
            "name": "matchCase",
            "type": "Attribute",
        }
    )


@dataclass
class BinarySpatialOpType(SpatialOpsType):
    property_name: List[PropertyName] = field(
        default_factory=list,
        metadata={
            "name": "PropertyName",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
            "max_occurs": 2,
        }
    )
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
    envelope_with_time_period: Optional[EnvelopeWithTimePeriod] = field(
        default=None,
        metadata={
            "name": "EnvelopeWithTimePeriod",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    envelope: Optional[Envelope] = field(
        default=None,
        metadata={
            "name": "Envelope",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )


@dataclass
class DistanceBufferType(SpatialOpsType):
    property_name: Optional[PropertyName] = field(
        default=None,
        metadata={
            "name": "PropertyName",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
            "required": True,
        }
    )
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
    distance: Optional[DistanceType] = field(
        default=None,
        metadata={
            "name": "Distance",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
            "required": True,
        }
    )


@dataclass
class FeatureIdType(AbstractIdType):
    fid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class GmlObjectIdType(AbstractIdType):
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )


@dataclass
class LowerBoundaryType:
    literal: Optional[Literal] = field(
        default=None,
        metadata={
            "name": "Literal",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        }
    )
    function: Optional[Function] = field(
        default=None,
        metadata={
            "name": "Function",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        }
    )
    property_name: Optional[PropertyName] = field(
        default=None,
        metadata={
            "name": "PropertyName",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        }
    )
    div: Optional[Div] = field(
        default=None,
        metadata={
            "name": "Div",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        }
    )
    mul: Optional[Mul] = field(
        default=None,
        metadata={
            "name": "Mul",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        }
    )
    sub: Optional[Sub] = field(
        default=None,
        metadata={
            "name": "Sub",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        }
    )
    add: Optional[Add] = field(
        default=None,
        metadata={
            "name": "Add",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        }
    )
    expression: Optional[Expression] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        }
    )


@dataclass
class PropertyIsLikeType(ComparisonOpsType):
    property_name: Optional[PropertyName] = field(
        default=None,
        metadata={
            "name": "PropertyName",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
            "required": True,
        }
    )
    literal: Optional[Literal] = field(
        default=None,
        metadata={
            "name": "Literal",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
            "required": True,
        }
    )
    wild_card: Optional[str] = field(
        default=None,
        metadata={
            "name": "wildCard",
            "type": "Attribute",
            "required": True,
        }
    )
    single_char: Optional[str] = field(
        default=None,
        metadata={
            "name": "singleChar",
            "type": "Attribute",
            "required": True,
        }
    )
    escape_char: Optional[str] = field(
        default=None,
        metadata={
            "name": "escapeChar",
            "type": "Attribute",
            "required": True,
        }
    )
    match_case: bool = field(
        default=True,
        metadata={
            "name": "matchCase",
            "type": "Attribute",
        }
    )


@dataclass
class PropertyIsNullType(ComparisonOpsType):
    property_name: Optional[PropertyName] = field(
        default=None,
        metadata={
            "name": "PropertyName",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
            "required": True,
        }
    )


@dataclass
class UpperBoundaryType:
    literal: Optional[Literal] = field(
        default=None,
        metadata={
            "name": "Literal",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        }
    )
    function: Optional[Function] = field(
        default=None,
        metadata={
            "name": "Function",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        }
    )
    property_name: Optional[PropertyName] = field(
        default=None,
        metadata={
            "name": "PropertyName",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        }
    )
    div: Optional[Div] = field(
        default=None,
        metadata={
            "name": "Div",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        }
    )
    mul: Optional[Mul] = field(
        default=None,
        metadata={
            "name": "Mul",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        }
    )
    sub: Optional[Sub] = field(
        default=None,
        metadata={
            "name": "Sub",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        }
    )
    add: Optional[Add] = field(
        default=None,
        metadata={
            "name": "Add",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        }
    )
    expression: Optional[Expression] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        }
    )


@dataclass
class Id(AbstractIdType):
    class Meta:
        name = "_Id"
        namespace = "http://www.opengis.net/ogc"


@dataclass
class ComparisonOps(ComparisonOpsType):
    class Meta:
        name = "comparisonOps"
        namespace = "http://www.opengis.net/ogc"


@dataclass
class LogicOps(LogicOpsType):
    class Meta:
        name = "logicOps"
        namespace = "http://www.opengis.net/ogc"


@dataclass
class SpatialOps(SpatialOpsType):
    class Meta:
        name = "spatialOps"
        namespace = "http://www.opengis.net/ogc"


@dataclass
class Bbox(Bboxtype):
    class Meta:
        name = "BBOX"
        namespace = "http://www.opengis.net/ogc"


@dataclass
class Beyond(DistanceBufferType):
    class Meta:
        namespace = "http://www.opengis.net/ogc"


@dataclass
class Contains(BinarySpatialOpType):
    class Meta:
        namespace = "http://www.opengis.net/ogc"


@dataclass
class Crosses(BinarySpatialOpType):
    class Meta:
        namespace = "http://www.opengis.net/ogc"


@dataclass
class Dwithin(DistanceBufferType):
    class Meta:
        name = "DWithin"
        namespace = "http://www.opengis.net/ogc"


@dataclass
class Disjoint(BinarySpatialOpType):
    class Meta:
        namespace = "http://www.opengis.net/ogc"


@dataclass
class Equals(BinarySpatialOpType):
    class Meta:
        namespace = "http://www.opengis.net/ogc"


@dataclass
class FeatureId(FeatureIdType):
    class Meta:
        namespace = "http://www.opengis.net/ogc"


@dataclass
class GmlObjectId(GmlObjectIdType):
    class Meta:
        namespace = "http://www.opengis.net/ogc"


@dataclass
class Intersects(BinarySpatialOpType):
    class Meta:
        namespace = "http://www.opengis.net/ogc"


@dataclass
class Overlaps(BinarySpatialOpType):
    class Meta:
        namespace = "http://www.opengis.net/ogc"


@dataclass
class PropertyIsBetweenType(ComparisonOpsType):
    literal: Optional[Literal] = field(
        default=None,
        metadata={
            "name": "Literal",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        }
    )
    function: Optional[Function] = field(
        default=None,
        metadata={
            "name": "Function",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        }
    )
    property_name: Optional[PropertyName] = field(
        default=None,
        metadata={
            "name": "PropertyName",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        }
    )
    div: Optional[Div] = field(
        default=None,
        metadata={
            "name": "Div",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        }
    )
    mul: Optional[Mul] = field(
        default=None,
        metadata={
            "name": "Mul",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        }
    )
    sub: Optional[Sub] = field(
        default=None,
        metadata={
            "name": "Sub",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        }
    )
    add: Optional[Add] = field(
        default=None,
        metadata={
            "name": "Add",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        }
    )
    expression: Optional[Expression] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        }
    )
    lower_boundary: Optional[LowerBoundaryType] = field(
        default=None,
        metadata={
            "name": "LowerBoundary",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
            "required": True,
        }
    )
    upper_boundary: Optional[UpperBoundaryType] = field(
        default=None,
        metadata={
            "name": "UpperBoundary",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
            "required": True,
        }
    )


@dataclass
class PropertyIsEqualTo(BinaryComparisonOpType):
    class Meta:
        namespace = "http://www.opengis.net/ogc"


@dataclass
class PropertyIsGreaterThan(BinaryComparisonOpType):
    class Meta:
        namespace = "http://www.opengis.net/ogc"


@dataclass
class PropertyIsGreaterThanOrEqualTo(BinaryComparisonOpType):
    class Meta:
        namespace = "http://www.opengis.net/ogc"


@dataclass
class PropertyIsLessThan(BinaryComparisonOpType):
    class Meta:
        namespace = "http://www.opengis.net/ogc"


@dataclass
class PropertyIsLessThanOrEqualTo(BinaryComparisonOpType):
    class Meta:
        namespace = "http://www.opengis.net/ogc"


@dataclass
class PropertyIsLike(PropertyIsLikeType):
    class Meta:
        namespace = "http://www.opengis.net/ogc"


@dataclass
class PropertyIsNotEqualTo(BinaryComparisonOpType):
    class Meta:
        namespace = "http://www.opengis.net/ogc"


@dataclass
class PropertyIsNull(PropertyIsNullType):
    class Meta:
        namespace = "http://www.opengis.net/ogc"


@dataclass
class Touches(BinarySpatialOpType):
    class Meta:
        namespace = "http://www.opengis.net/ogc"


@dataclass
class Within(BinarySpatialOpType):
    class Meta:
        namespace = "http://www.opengis.net/ogc"


@dataclass
class PropertyIsBetween(PropertyIsBetweenType):
    class Meta:
        namespace = "http://www.opengis.net/ogc"


@dataclass
class BinaryLogicOpType(LogicOpsType):
    property_is_between: List[PropertyIsBetween] = field(
        default_factory=list,
        metadata={
            "name": "PropertyIsBetween",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        }
    )
    property_is_null: List[PropertyIsNull] = field(
        default_factory=list,
        metadata={
            "name": "PropertyIsNull",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        }
    )
    property_is_like: List[PropertyIsLike] = field(
        default_factory=list,
        metadata={
            "name": "PropertyIsLike",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        }
    )
    property_is_greater_than_or_equal_to: List[PropertyIsGreaterThanOrEqualTo] = field(
        default_factory=list,
        metadata={
            "name": "PropertyIsGreaterThanOrEqualTo",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        }
    )
    property_is_less_than_or_equal_to: List[PropertyIsLessThanOrEqualTo] = field(
        default_factory=list,
        metadata={
            "name": "PropertyIsLessThanOrEqualTo",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        }
    )
    property_is_greater_than: List[PropertyIsGreaterThan] = field(
        default_factory=list,
        metadata={
            "name": "PropertyIsGreaterThan",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        }
    )
    property_is_less_than: List[PropertyIsLessThan] = field(
        default_factory=list,
        metadata={
            "name": "PropertyIsLessThan",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        }
    )
    property_is_not_equal_to: List[PropertyIsNotEqualTo] = field(
        default_factory=list,
        metadata={
            "name": "PropertyIsNotEqualTo",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        }
    )
    property_is_equal_to: List[PropertyIsEqualTo] = field(
        default_factory=list,
        metadata={
            "name": "PropertyIsEqualTo",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        }
    )
    comparison_ops: List[ComparisonOps] = field(
        default_factory=list,
        metadata={
            "name": "comparisonOps",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        }
    )
    bbox: List[Bbox] = field(
        default_factory=list,
        metadata={
            "name": "BBOX",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        }
    )
    beyond: List[Beyond] = field(
        default_factory=list,
        metadata={
            "name": "Beyond",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        }
    )
    dwithin: List[Dwithin] = field(
        default_factory=list,
        metadata={
            "name": "DWithin",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        }
    )
    contains: List[Contains] = field(
        default_factory=list,
        metadata={
            "name": "Contains",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        }
    )
    intersects: List[Intersects] = field(
        default_factory=list,
        metadata={
            "name": "Intersects",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        }
    )
    crosses: List[Crosses] = field(
        default_factory=list,
        metadata={
            "name": "Crosses",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        }
    )
    overlaps: List[Overlaps] = field(
        default_factory=list,
        metadata={
            "name": "Overlaps",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        }
    )
    within: List[Within] = field(
        default_factory=list,
        metadata={
            "name": "Within",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        }
    )
    touches: List[Touches] = field(
        default_factory=list,
        metadata={
            "name": "Touches",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        }
    )
    disjoint: List[Disjoint] = field(
        default_factory=list,
        metadata={
            "name": "Disjoint",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        }
    )
    equals: List[Equals] = field(
        default_factory=list,
        metadata={
            "name": "Equals",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        }
    )
    spatial_ops: List[SpatialOps] = field(
        default_factory=list,
        metadata={
            "name": "spatialOps",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        }
    )
    not_value: List["Not"] = field(
        default_factory=list,
        metadata={
            "name": "Not",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        }
    )
    or_value: List["Or"] = field(
        default_factory=list,
        metadata={
            "name": "Or",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        }
    )
    and_value: List["And"] = field(
        default_factory=list,
        metadata={
            "name": "And",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        }
    )
    logic_ops: List[LogicOps] = field(
        default_factory=list,
        metadata={
            "name": "logicOps",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        }
    )
    function: List[Function] = field(
        default_factory=list,
        metadata={
            "name": "Function",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
            "min_occurs": 2,
        }
    )


@dataclass
class And(BinaryLogicOpType):
    class Meta:
        namespace = "http://www.opengis.net/ogc"


@dataclass
class Or(BinaryLogicOpType):
    class Meta:
        namespace = "http://www.opengis.net/ogc"


@dataclass
class UnaryLogicOpType(LogicOpsType):
    property_is_between: Optional[PropertyIsBetween] = field(
        default=None,
        metadata={
            "name": "PropertyIsBetween",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        }
    )
    property_is_null: Optional[PropertyIsNull] = field(
        default=None,
        metadata={
            "name": "PropertyIsNull",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        }
    )
    property_is_like: Optional[PropertyIsLike] = field(
        default=None,
        metadata={
            "name": "PropertyIsLike",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        }
    )
    property_is_greater_than_or_equal_to: Optional[PropertyIsGreaterThanOrEqualTo] = field(
        default=None,
        metadata={
            "name": "PropertyIsGreaterThanOrEqualTo",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        }
    )
    property_is_less_than_or_equal_to: Optional[PropertyIsLessThanOrEqualTo] = field(
        default=None,
        metadata={
            "name": "PropertyIsLessThanOrEqualTo",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        }
    )
    property_is_greater_than: Optional[PropertyIsGreaterThan] = field(
        default=None,
        metadata={
            "name": "PropertyIsGreaterThan",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        }
    )
    property_is_less_than: Optional[PropertyIsLessThan] = field(
        default=None,
        metadata={
            "name": "PropertyIsLessThan",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        }
    )
    property_is_not_equal_to: Optional[PropertyIsNotEqualTo] = field(
        default=None,
        metadata={
            "name": "PropertyIsNotEqualTo",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        }
    )
    property_is_equal_to: Optional[PropertyIsEqualTo] = field(
        default=None,
        metadata={
            "name": "PropertyIsEqualTo",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        }
    )
    comparison_ops: Optional[ComparisonOps] = field(
        default=None,
        metadata={
            "name": "comparisonOps",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        }
    )
    bbox: Optional[Bbox] = field(
        default=None,
        metadata={
            "name": "BBOX",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        }
    )
    beyond: Optional[Beyond] = field(
        default=None,
        metadata={
            "name": "Beyond",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        }
    )
    dwithin: Optional[Dwithin] = field(
        default=None,
        metadata={
            "name": "DWithin",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        }
    )
    contains: Optional[Contains] = field(
        default=None,
        metadata={
            "name": "Contains",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        }
    )
    intersects: Optional[Intersects] = field(
        default=None,
        metadata={
            "name": "Intersects",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        }
    )
    crosses: Optional[Crosses] = field(
        default=None,
        metadata={
            "name": "Crosses",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        }
    )
    overlaps: Optional[Overlaps] = field(
        default=None,
        metadata={
            "name": "Overlaps",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        }
    )
    within: Optional[Within] = field(
        default=None,
        metadata={
            "name": "Within",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        }
    )
    touches: Optional[Touches] = field(
        default=None,
        metadata={
            "name": "Touches",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        }
    )
    disjoint: Optional[Disjoint] = field(
        default=None,
        metadata={
            "name": "Disjoint",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        }
    )
    equals: Optional[Equals] = field(
        default=None,
        metadata={
            "name": "Equals",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        }
    )
    spatial_ops: Optional[SpatialOps] = field(
        default=None,
        metadata={
            "name": "spatialOps",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        }
    )
    not_value: Optional["Not"] = field(
        default=None,
        metadata={
            "name": "Not",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        }
    )
    or_value: Optional[Or] = field(
        default=None,
        metadata={
            "name": "Or",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        }
    )
    and_value: Optional[And] = field(
        default=None,
        metadata={
            "name": "And",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        }
    )
    logic_ops: Optional[LogicOps] = field(
        default=None,
        metadata={
            "name": "logicOps",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        }
    )
    function: Optional[Function] = field(
        default=None,
        metadata={
            "name": "Function",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        }
    )


@dataclass
class Not(UnaryLogicOpType):
    class Meta:
        namespace = "http://www.opengis.net/ogc"


@dataclass
class FilterType:
    bbox: Optional[Bbox] = field(
        default=None,
        metadata={
            "name": "BBOX",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        }
    )
    beyond: Optional[Beyond] = field(
        default=None,
        metadata={
            "name": "Beyond",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        }
    )
    dwithin: Optional[Dwithin] = field(
        default=None,
        metadata={
            "name": "DWithin",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        }
    )
    contains: Optional[Contains] = field(
        default=None,
        metadata={
            "name": "Contains",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        }
    )
    intersects: Optional[Intersects] = field(
        default=None,
        metadata={
            "name": "Intersects",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        }
    )
    crosses: Optional[Crosses] = field(
        default=None,
        metadata={
            "name": "Crosses",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        }
    )
    overlaps: Optional[Overlaps] = field(
        default=None,
        metadata={
            "name": "Overlaps",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        }
    )
    within: Optional[Within] = field(
        default=None,
        metadata={
            "name": "Within",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        }
    )
    touches: Optional[Touches] = field(
        default=None,
        metadata={
            "name": "Touches",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        }
    )
    disjoint: Optional[Disjoint] = field(
        default=None,
        metadata={
            "name": "Disjoint",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        }
    )
    equals: Optional[Equals] = field(
        default=None,
        metadata={
            "name": "Equals",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        }
    )
    spatial_ops: Optional[SpatialOps] = field(
        default=None,
        metadata={
            "name": "spatialOps",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        }
    )
    property_is_between: Optional[PropertyIsBetween] = field(
        default=None,
        metadata={
            "name": "PropertyIsBetween",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        }
    )
    property_is_null: Optional[PropertyIsNull] = field(
        default=None,
        metadata={
            "name": "PropertyIsNull",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        }
    )
    property_is_like: Optional[PropertyIsLike] = field(
        default=None,
        metadata={
            "name": "PropertyIsLike",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        }
    )
    property_is_greater_than_or_equal_to: Optional[PropertyIsGreaterThanOrEqualTo] = field(
        default=None,
        metadata={
            "name": "PropertyIsGreaterThanOrEqualTo",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        }
    )
    property_is_less_than_or_equal_to: Optional[PropertyIsLessThanOrEqualTo] = field(
        default=None,
        metadata={
            "name": "PropertyIsLessThanOrEqualTo",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        }
    )
    property_is_greater_than: Optional[PropertyIsGreaterThan] = field(
        default=None,
        metadata={
            "name": "PropertyIsGreaterThan",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        }
    )
    property_is_less_than: Optional[PropertyIsLessThan] = field(
        default=None,
        metadata={
            "name": "PropertyIsLessThan",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        }
    )
    property_is_not_equal_to: Optional[PropertyIsNotEqualTo] = field(
        default=None,
        metadata={
            "name": "PropertyIsNotEqualTo",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        }
    )
    property_is_equal_to: Optional[PropertyIsEqualTo] = field(
        default=None,
        metadata={
            "name": "PropertyIsEqualTo",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        }
    )
    comparison_ops: Optional[ComparisonOps] = field(
        default=None,
        metadata={
            "name": "comparisonOps",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        }
    )
    not_value: Optional[Not] = field(
        default=None,
        metadata={
            "name": "Not",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        }
    )
    or_value: Optional[Or] = field(
        default=None,
        metadata={
            "name": "Or",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        }
    )
    and_value: Optional[And] = field(
        default=None,
        metadata={
            "name": "And",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        }
    )
    logic_ops: Optional[LogicOps] = field(
        default=None,
        metadata={
            "name": "logicOps",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        }
    )
    gml_object_id: List[GmlObjectId] = field(
        default_factory=list,
        metadata={
            "name": "GmlObjectId",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        }
    )
    feature_id: List[FeatureId] = field(
        default_factory=list,
        metadata={
            "name": "FeatureId",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        }
    )
    id: List[Id] = field(
        default_factory=list,
        metadata={
            "name": "_Id",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        }
    )


@dataclass
class Filter(FilterType):
    class Meta:
        namespace = "http://www.opengis.net/ogc"
