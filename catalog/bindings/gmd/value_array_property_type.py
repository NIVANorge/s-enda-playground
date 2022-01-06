from dataclasses import dataclass, field
from typing import List, Optional, Union
from bindings.gmd.abstract_curve import AbstractCurve
from bindings.gmd.abstract_geometric_aggregate import AbstractGeometricAggregate
from bindings.gmd.abstract_geometric_primitive import AbstractGeometricPrimitive
from bindings.gmd.abstract_geometry import AbstractGeometry
from bindings.gmd.abstract_gmltype import AbstractGmltype
from bindings.gmd.abstract_implicit_geometry import AbstractImplicitGeometry
from bindings.gmd.abstract_scalar_value import AbstractScalarValue
from bindings.gmd.abstract_scalar_value_list import AbstractScalarValueList
from bindings.gmd.abstract_solid import AbstractSolid
from bindings.gmd.abstract_surface import AbstractSurface
from bindings.gmd.abstract_time_complex import AbstractTimeComplex
from bindings.gmd.abstract_time_object import AbstractTimeObject
from bindings.gmd.abstract_value import AbstractValue
from bindings.gmd.actuate_value import ActuateValue
from bindings.gmd.aggregation_type import AggregationType
from bindings.gmd.boolean_1 import Boolean1
from bindings.gmd.category import Category
from bindings.gmd.category_extent import CategoryExtent
from bindings.gmd.category_list import CategoryList
from bindings.gmd.composite_curve_type import (
    CompositeCurve,
    Curve,
    OrientableCurve,
)
from bindings.gmd.composite_surface_type import (
    CompositeSurface,
    OrientableSurface,
)
from bindings.gmd.count import Count
from bindings.gmd.geometric_complex import GeometricComplex
from bindings.gmd.geometry_array_property_type import MultiGeometry
from bindings.gmd.grid import Grid
from bindings.gmd.line_string import LineString
from bindings.gmd.multi_curve import MultiCurve
from bindings.gmd.multi_point import MultiPoint
from bindings.gmd.multi_solid import MultiSolid
from bindings.gmd.multi_surface import MultiSurface
from bindings.gmd.nil_reason_enumeration_value import NilReasonEnumerationValue
from bindings.gmd.point import Point
from bindings.gmd.polygon import Polygon
from bindings.gmd.polyhedral_surface import PolyhedralSurface
from bindings.gmd.quantity import Quantity
from bindings.gmd.quantity_extent import QuantityExtent
from bindings.gmd.quantity_list import QuantityList
from bindings.gmd.rectified_grid import RectifiedGrid
from bindings.gmd.show_value import ShowValue
from bindings.gmd.solid import Solid
from bindings.gmd.solid_property_type import CompositeSolid
from bindings.gmd.surface import Surface
from bindings.gmd.time_edge_property_type import (
    AbstractTimeGeometricPrimitive,
    AbstractTimePrimitive,
    AbstractTimeTopologyPrimitive,
    TimeEdge,
    TimeInstant,
    TimeNode,
    TimePeriod,
)
from bindings.gmd.time_topology_complex import TimeTopologyComplex
from bindings.gmd.tin import Tin
from bindings.gmd.triangulated_surface import TriangulatedSurface

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class ValueArrayPropertyType:
    quantity_extent: List[QuantityExtent] = field(
        default_factory=list,
        metadata={
            "name": "QuantityExtent",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "sequential": True,
        },
    )
    count_extent: List[List[Union[str, NilReasonEnumerationValue]]] = field(
        default_factory=list,
        metadata={
            "name": "CountExtent",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "length": 2,
            "pattern": r"other:\w{2,}",
            "sequential": True,
            "tokens": True,
        },
    )
    category_extent: List[CategoryExtent] = field(
        default_factory=list,
        metadata={
            "name": "CategoryExtent",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "sequential": True,
        },
    )
    value_array: List["ValueArray"] = field(
        default_factory=list,
        metadata={
            "name": "ValueArray",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "sequential": True,
        },
    )
    composite_value: List["CompositeValue"] = field(
        default_factory=list,
        metadata={
            "name": "CompositeValue",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "sequential": True,
        },
    )
    quantity_list: List[QuantityList] = field(
        default_factory=list,
        metadata={
            "name": "QuantityList",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "sequential": True,
        },
    )
    count_list: List[List[Union[str, NilReasonEnumerationValue]]] = field(
        default_factory=list,
        metadata={
            "name": "CountList",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "pattern": r"other:\w{2,}",
            "sequential": True,
            "tokens": True,
        },
    )
    category_list: List[CategoryList] = field(
        default_factory=list,
        metadata={
            "name": "CategoryList",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "sequential": True,
        },
    )
    boolean_list: List[List[Union[str, NilReasonEnumerationValue]]] = field(
        default_factory=list,
        metadata={
            "name": "BooleanList",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "pattern": r"other:\w{2,}",
            "sequential": True,
            "tokens": True,
        },
    )
    abstract_scalar_value_list: List[AbstractScalarValueList] = field(
        default_factory=list,
        metadata={
            "name": "AbstractScalarValueList",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "sequential": True,
        },
    )
    quantity: List[Quantity] = field(
        default_factory=list,
        metadata={
            "name": "Quantity",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "nillable": True,
            "sequential": True,
        },
    )
    count: List[Count] = field(
        default_factory=list,
        metadata={
            "name": "Count",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "nillable": True,
            "sequential": True,
        },
    )
    category: List[Category] = field(
        default_factory=list,
        metadata={
            "name": "Category",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "nillable": True,
            "sequential": True,
        },
    )
    boolean: List[Boolean1] = field(
        default_factory=list,
        metadata={
            "name": "Boolean",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "nillable": True,
            "sequential": True,
        },
    )
    abstract_scalar_value: List[AbstractScalarValue] = field(
        default_factory=list,
        metadata={
            "name": "AbstractScalarValue",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "sequential": True,
        },
    )
    abstract_value: List[AbstractValue] = field(
        default_factory=list,
        metadata={
            "name": "AbstractValue",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "sequential": True,
        },
    )
    rectified_grid: List[RectifiedGrid] = field(
        default_factory=list,
        metadata={
            "name": "RectifiedGrid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "sequential": True,
        },
    )
    grid: List[Grid] = field(
        default_factory=list,
        metadata={
            "name": "Grid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "sequential": True,
        },
    )
    abstract_implicit_geometry: List[AbstractImplicitGeometry] = field(
        default_factory=list,
        metadata={
            "name": "AbstractImplicitGeometry",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "sequential": True,
        },
    )
    geometric_complex: List[GeometricComplex] = field(
        default_factory=list,
        metadata={
            "name": "GeometricComplex",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "sequential": True,
        },
    )
    multi_solid: List[MultiSolid] = field(
        default_factory=list,
        metadata={
            "name": "MultiSolid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "sequential": True,
        },
    )
    multi_surface: List[MultiSurface] = field(
        default_factory=list,
        metadata={
            "name": "MultiSurface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "sequential": True,
        },
    )
    multi_curve: List[MultiCurve] = field(
        default_factory=list,
        metadata={
            "name": "MultiCurve",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "sequential": True,
        },
    )
    multi_point: List[MultiPoint] = field(
        default_factory=list,
        metadata={
            "name": "MultiPoint",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "sequential": True,
        },
    )
    multi_geometry: List[MultiGeometry] = field(
        default_factory=list,
        metadata={
            "name": "MultiGeometry",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "sequential": True,
        },
    )
    abstract_geometric_aggregate: List[AbstractGeometricAggregate] = field(
        default_factory=list,
        metadata={
            "name": "AbstractGeometricAggregate",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "sequential": True,
        },
    )
    composite_solid: List[CompositeSolid] = field(
        default_factory=list,
        metadata={
            "name": "CompositeSolid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "sequential": True,
        },
    )
    solid: List[Solid] = field(
        default_factory=list,
        metadata={
            "name": "Solid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "sequential": True,
        },
    )
    abstract_solid: List[AbstractSolid] = field(
        default_factory=list,
        metadata={
            "name": "AbstractSolid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "sequential": True,
        },
    )
    composite_surface: List[CompositeSurface] = field(
        default_factory=list,
        metadata={
            "name": "CompositeSurface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "sequential": True,
        },
    )
    orientable_surface: List[OrientableSurface] = field(
        default_factory=list,
        metadata={
            "name": "OrientableSurface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "sequential": True,
        },
    )
    tin: List[Tin] = field(
        default_factory=list,
        metadata={
            "name": "Tin",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "sequential": True,
        },
    )
    triangulated_surface: List[TriangulatedSurface] = field(
        default_factory=list,
        metadata={
            "name": "TriangulatedSurface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "sequential": True,
        },
    )
    polyhedral_surface: List[PolyhedralSurface] = field(
        default_factory=list,
        metadata={
            "name": "PolyhedralSurface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "sequential": True,
        },
    )
    surface: List[Surface] = field(
        default_factory=list,
        metadata={
            "name": "Surface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "sequential": True,
        },
    )
    polygon: List[Polygon] = field(
        default_factory=list,
        metadata={
            "name": "Polygon",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "sequential": True,
        },
    )
    abstract_surface: List[AbstractSurface] = field(
        default_factory=list,
        metadata={
            "name": "AbstractSurface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "sequential": True,
        },
    )
    composite_curve: List[CompositeCurve] = field(
        default_factory=list,
        metadata={
            "name": "CompositeCurve",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "sequential": True,
        },
    )
    orientable_curve: List[OrientableCurve] = field(
        default_factory=list,
        metadata={
            "name": "OrientableCurve",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "sequential": True,
        },
    )
    curve: List[Curve] = field(
        default_factory=list,
        metadata={
            "name": "Curve",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "sequential": True,
        },
    )
    line_string: List[LineString] = field(
        default_factory=list,
        metadata={
            "name": "LineString",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "sequential": True,
        },
    )
    abstract_curve: List[AbstractCurve] = field(
        default_factory=list,
        metadata={
            "name": "AbstractCurve",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "sequential": True,
        },
    )
    point: List[Point] = field(
        default_factory=list,
        metadata={
            "name": "Point",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "sequential": True,
        },
    )
    abstract_geometric_primitive: List[AbstractGeometricPrimitive] = field(
        default_factory=list,
        metadata={
            "name": "AbstractGeometricPrimitive",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "sequential": True,
        },
    )
    abstract_geometry: List[AbstractGeometry] = field(
        default_factory=list,
        metadata={
            "name": "AbstractGeometry",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "sequential": True,
        },
    )
    time_topology_complex: List[TimeTopologyComplex] = field(
        default_factory=list,
        metadata={
            "name": "TimeTopologyComplex",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "sequential": True,
        },
    )
    abstract_time_complex: List[AbstractTimeComplex] = field(
        default_factory=list,
        metadata={
            "name": "AbstractTimeComplex",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "sequential": True,
        },
    )
    time_edge: List[TimeEdge] = field(
        default_factory=list,
        metadata={
            "name": "TimeEdge",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "sequential": True,
        },
    )
    time_node: List[TimeNode] = field(
        default_factory=list,
        metadata={
            "name": "TimeNode",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "sequential": True,
        },
    )
    abstract_time_topology_primitive: List[AbstractTimeTopologyPrimitive] = field(
        default_factory=list,
        metadata={
            "name": "AbstractTimeTopologyPrimitive",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "sequential": True,
        },
    )
    time_period: List[TimePeriod] = field(
        default_factory=list,
        metadata={
            "name": "TimePeriod",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "sequential": True,
        },
    )
    time_instant: List[TimeInstant] = field(
        default_factory=list,
        metadata={
            "name": "TimeInstant",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "sequential": True,
        },
    )
    abstract_time_geometric_primitive: List[AbstractTimeGeometricPrimitive] = field(
        default_factory=list,
        metadata={
            "name": "AbstractTimeGeometricPrimitive",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "sequential": True,
        },
    )
    abstract_time_primitive: List[AbstractTimePrimitive] = field(
        default_factory=list,
        metadata={
            "name": "AbstractTimePrimitive",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "sequential": True,
        },
    )
    abstract_time_object: List[AbstractTimeObject] = field(
        default_factory=list,
        metadata={
            "name": "AbstractTimeObject",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "sequential": True,
        },
    )
    null: List[Union[str, NilReasonEnumerationValue]] = field(
        default_factory=list,
        metadata={
            "name": "Null",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "pattern": r"other:\w{2,}",
            "sequential": True,
        },
    )
    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class ValuePropertyType:
    quantity_extent: Optional[QuantityExtent] = field(
        default=None,
        metadata={
            "name": "QuantityExtent",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    count_extent: List[Union[str, NilReasonEnumerationValue]] = field(
        default_factory=list,
        metadata={
            "name": "CountExtent",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "length": 2,
            "pattern": r"other:\w{2,}",
            "tokens": True,
        },
    )
    category_extent: Optional[CategoryExtent] = field(
        default=None,
        metadata={
            "name": "CategoryExtent",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    value_array: Optional["ValueArray"] = field(
        default=None,
        metadata={
            "name": "ValueArray",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    composite_value: Optional["CompositeValue"] = field(
        default=None,
        metadata={
            "name": "CompositeValue",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    quantity_list: Optional[QuantityList] = field(
        default=None,
        metadata={
            "name": "QuantityList",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    count_list: List[Union[str, NilReasonEnumerationValue]] = field(
        default_factory=list,
        metadata={
            "name": "CountList",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "pattern": r"other:\w{2,}",
            "tokens": True,
        },
    )
    category_list: Optional[CategoryList] = field(
        default=None,
        metadata={
            "name": "CategoryList",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    boolean_list: List[Union[str, NilReasonEnumerationValue]] = field(
        default_factory=list,
        metadata={
            "name": "BooleanList",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "pattern": r"other:\w{2,}",
            "tokens": True,
        },
    )
    abstract_scalar_value_list: Optional[AbstractScalarValueList] = field(
        default=None,
        metadata={
            "name": "AbstractScalarValueList",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    quantity: Optional[Quantity] = field(
        default=None,
        metadata={
            "name": "Quantity",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "nillable": True,
        },
    )
    count: Optional[Count] = field(
        default=None,
        metadata={
            "name": "Count",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "nillable": True,
        },
    )
    category: Optional[Category] = field(
        default=None,
        metadata={
            "name": "Category",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "nillable": True,
        },
    )
    boolean: Optional[Boolean1] = field(
        default=None,
        metadata={
            "name": "Boolean",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "nillable": True,
        },
    )
    abstract_scalar_value: Optional[AbstractScalarValue] = field(
        default=None,
        metadata={
            "name": "AbstractScalarValue",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    abstract_value: Optional[AbstractValue] = field(
        default=None,
        metadata={
            "name": "AbstractValue",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    rectified_grid: Optional[RectifiedGrid] = field(
        default=None,
        metadata={
            "name": "RectifiedGrid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    grid: Optional[Grid] = field(
        default=None,
        metadata={
            "name": "Grid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    abstract_implicit_geometry: Optional[AbstractImplicitGeometry] = field(
        default=None,
        metadata={
            "name": "AbstractImplicitGeometry",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    geometric_complex: Optional[GeometricComplex] = field(
        default=None,
        metadata={
            "name": "GeometricComplex",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    multi_solid: Optional[MultiSolid] = field(
        default=None,
        metadata={
            "name": "MultiSolid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    multi_surface: Optional[MultiSurface] = field(
        default=None,
        metadata={
            "name": "MultiSurface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    multi_curve: Optional[MultiCurve] = field(
        default=None,
        metadata={
            "name": "MultiCurve",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    multi_point: Optional[MultiPoint] = field(
        default=None,
        metadata={
            "name": "MultiPoint",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    multi_geometry: Optional[MultiGeometry] = field(
        default=None,
        metadata={
            "name": "MultiGeometry",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    abstract_geometric_aggregate: Optional[AbstractGeometricAggregate] = field(
        default=None,
        metadata={
            "name": "AbstractGeometricAggregate",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    composite_solid: Optional[CompositeSolid] = field(
        default=None,
        metadata={
            "name": "CompositeSolid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    solid: Optional[Solid] = field(
        default=None,
        metadata={
            "name": "Solid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    abstract_solid: Optional[AbstractSolid] = field(
        default=None,
        metadata={
            "name": "AbstractSolid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    composite_surface: Optional[CompositeSurface] = field(
        default=None,
        metadata={
            "name": "CompositeSurface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    orientable_surface: Optional[OrientableSurface] = field(
        default=None,
        metadata={
            "name": "OrientableSurface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    tin: Optional[Tin] = field(
        default=None,
        metadata={
            "name": "Tin",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    triangulated_surface: Optional[TriangulatedSurface] = field(
        default=None,
        metadata={
            "name": "TriangulatedSurface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    polyhedral_surface: Optional[PolyhedralSurface] = field(
        default=None,
        metadata={
            "name": "PolyhedralSurface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    surface: Optional[Surface] = field(
        default=None,
        metadata={
            "name": "Surface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    polygon: Optional[Polygon] = field(
        default=None,
        metadata={
            "name": "Polygon",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    abstract_surface: Optional[AbstractSurface] = field(
        default=None,
        metadata={
            "name": "AbstractSurface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    composite_curve: Optional[CompositeCurve] = field(
        default=None,
        metadata={
            "name": "CompositeCurve",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    orientable_curve: Optional[OrientableCurve] = field(
        default=None,
        metadata={
            "name": "OrientableCurve",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    curve: Optional[Curve] = field(
        default=None,
        metadata={
            "name": "Curve",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    line_string: Optional[LineString] = field(
        default=None,
        metadata={
            "name": "LineString",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    abstract_curve: Optional[AbstractCurve] = field(
        default=None,
        metadata={
            "name": "AbstractCurve",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    point: Optional[Point] = field(
        default=None,
        metadata={
            "name": "Point",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    abstract_geometric_primitive: Optional[AbstractGeometricPrimitive] = field(
        default=None,
        metadata={
            "name": "AbstractGeometricPrimitive",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    abstract_geometry: Optional[AbstractGeometry] = field(
        default=None,
        metadata={
            "name": "AbstractGeometry",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    time_topology_complex: Optional[TimeTopologyComplex] = field(
        default=None,
        metadata={
            "name": "TimeTopologyComplex",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    abstract_time_complex: Optional[AbstractTimeComplex] = field(
        default=None,
        metadata={
            "name": "AbstractTimeComplex",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
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
    abstract_time_topology_primitive: Optional[AbstractTimeTopologyPrimitive] = field(
        default=None,
        metadata={
            "name": "AbstractTimeTopologyPrimitive",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    time_period: Optional[TimePeriod] = field(
        default=None,
        metadata={
            "name": "TimePeriod",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    time_instant: Optional[TimeInstant] = field(
        default=None,
        metadata={
            "name": "TimeInstant",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    abstract_time_geometric_primitive: Optional[AbstractTimeGeometricPrimitive] = field(
        default=None,
        metadata={
            "name": "AbstractTimeGeometricPrimitive",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    abstract_time_primitive: Optional[AbstractTimePrimitive] = field(
        default=None,
        metadata={
            "name": "AbstractTimePrimitive",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    abstract_time_object: Optional[AbstractTimeObject] = field(
        default=None,
        metadata={
            "name": "AbstractTimeObject",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    null: Optional[Union[str, NilReasonEnumerationValue]] = field(
        default=None,
        metadata={
            "name": "Null",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "pattern": r"other:\w{2,}",
        },
    )
    type: str = field(
        init=False,
        default="simple",
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
        },
    )
    arcrole: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    show: Optional[ShowValue] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    actuate: Optional[ActuateValue] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    nil_reason: Optional[Union[str, NilReasonEnumerationValue]] = field(
        default=None,
        metadata={
            "name": "nilReason",
            "type": "Attribute",
            "pattern": r"other:\w{2,}",
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
    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class ValueComponent(ValuePropertyType):
    """
    Property that refers to, or contains, a Value.
    """

    class Meta:
        name = "valueComponent"
        namespace = "http://www.opengis.net/gml"


@dataclass
class ValueComponents(ValueArrayPropertyType):
    """
    Property that contains Values.
    """

    class Meta:
        name = "valueComponents"
        namespace = "http://www.opengis.net/gml"


@dataclass
class CompositeValueType(AbstractGmltype):
    value_component: List[ValueComponent] = field(
        default_factory=list,
        metadata={
            "name": "valueComponent",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    value_components: Optional[ValueComponents] = field(
        default=None,
        metadata={
            "name": "valueComponents",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    aggregation_type: Optional[AggregationType] = field(
        default=None,
        metadata={
            "name": "aggregationType",
            "type": "Attribute",
        },
    )


@dataclass
class CompositeValue(CompositeValueType):
    """gml:CompositeValue is an aggregate value built from other values .

    It contains zero or an arbitrary number of gml:valueComponent
    elements, and zero or one gml:valueComponents property elements.  It
    may be used for strongly coupled aggregates (vectors, tensors) or
    for arbitrary collections of values.
    """

    class Meta:
        namespace = "http://www.opengis.net/gml"


@dataclass
class ValueArrayType(CompositeValueType):
    code_space: Optional[str] = field(
        default=None,
        metadata={
            "name": "codeSpace",
            "type": "Attribute",
        },
    )
    uom: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[^: \n\r\t]+",
        },
    )


@dataclass
class ValueArray(ValueArrayType):
    """A Value Array is used for homogeneous arrays of primitive and aggregate
    values.

    The member values may be scalars, composites, arrays or lists.
    ValueArray has the same content model as CompositeValue, but the
    member values shall be homogeneous.  The element declaration
    contains a Schematron constraint which expresses this restriction
    precisely.  Since the members are homogeneous, the
    gml:referenceSystem (uom, codeSpace) may be specified on the
    gml:ValueArray itself and inherited by all the members if desired.
    """

    class Meta:
        namespace = "http://www.opengis.net/gml"
