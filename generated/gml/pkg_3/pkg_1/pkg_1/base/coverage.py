from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional, Union
from generated.gml.pkg_3.pkg_1.pkg_1.base.basic_types import (
    CoordinatesType,
    NullEnumerationValue,
)
from generated.gml.pkg_3.pkg_1.pkg_1.base.feature import AbstractFeatureType
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
from generated.gml.pkg_3.pkg_1.pkg_1.base.gml_base import StringOrRefType
from generated.gml.pkg_3.pkg_1.pkg_1.base.grids import (
    Grid,
    RectifiedGrid,
    ImplicitGeometry,
)
from generated.gml.pkg_3.pkg_1.pkg_1.base.temporal import (
    TimeInstant,
    TimePeriod,
    TimeComplex,
    TimeGeometricPrimitive,
    TimeObject,
    TimePrimitive,
)
from generated.gml.pkg_3.pkg_1.pkg_1.base.temporal_topology import (
    TimeEdge,
    TimeNode,
    TimeTopologyComplex,
    TimeTopologyPrimitive,
)
from generated.gml.pkg_3.pkg_1.pkg_1.base.value_objects import (
    Category,
    CategoryExtent,
    CategoryList,
    CompositeValue,
    Quantity,
    QuantityExtent,
    QuantityList,
    ValueArray,
)
from generated.xlink import (
    ActuateType,
    ShowType,
    TypeType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


class FileValueModelType(Enum):
    """
    List of codes that identifies the file structure model for records stored
    in files.
    """
    RECORD_INTERLEAVED = "Record Interleaved"


class IncrementOrder(Enum):
    """The enumeration value here indicates the incrementation order  to be
    used on the first 2 axes, i.e. "+x-y" means that the points on the first
    axis are to be traversed from lowest to highest and  the points on the
    second axis are to be traversed from highest to lowest.

    The points on all other axes (if any) beyond the first 2 are assumed
    to increment from lowest to highest.
    """
    X_Y = "+x+y"
    Y_X = "+y+x"
    X_Y_1 = "+x-y"
    X_Y_2 = "-x-y"


class SequenceRuleNames(Enum):
    """
    List of codes (adopted from ISO 19123 Annex C) that identifies the rule for
    traversing a grid to correspond with the sequence of members of the
    rangeSet.
    """
    LINEAR = "Linear"
    BOUSTROPHEDONIC = "Boustrophedonic"
    CANTOR_DIAGONAL = "Cantor-diagonal"
    SPIRAL = "Spiral"
    MORTON = "Morton"
    HILBERT = "Hilbert"


@dataclass
class DomainSetType:
    """The spatiotemporal domain of a coverage. Typically.

    * a geometry collection,
    * an implicit geometry (e.g. a grid),
    * an explicit or implicit collection of time instances or periods, or
    N.B. Temporal geometric complexes and temporal grids are not yet implemented in GML.
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
    time_topology_complex: Optional[TimeTopologyComplex] = field(
        default=None,
        metadata={
            "name": "TimeTopologyComplex",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    time_complex: Optional[TimeComplex] = field(
        default=None,
        metadata={
            "name": "_TimeComplex",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
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
    time_period: Optional[TimePeriod] = field(
        default=None,
        metadata={
            "name": "TimePeriod",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    time_instant: Optional[TimeInstant] = field(
        default=None,
        metadata={
            "name": "TimeInstant",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    time_geometric_primitive: Optional[TimeGeometricPrimitive] = field(
        default=None,
        metadata={
            "name": "_TimeGeometricPrimitive",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    time_primitive: Optional[TimePrimitive] = field(
        default=None,
        metadata={
            "name": "_TimePrimitive",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    time_object: Optional[TimeObject] = field(
        default=None,
        metadata={
            "name": "_TimeObject",
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
class MappingRule(StringOrRefType):
    """
    Description of a rule for associating members from the domainSet with
    members of the rangeSet.
    """
    class Meta:
        namespace = "http://www.opengis.net/gml"


@dataclass
class RangeParametersType:
    """Metadata about the rangeSet.

    Definition of record structure. This is required if the rangeSet is
    encoded in a DataBlock. We use a gml:_Value with empty values as a
    map of the composite value structure.
    """
    boolean: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Boolean",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    category: Optional[Category] = field(
        default=None,
        metadata={
            "name": "Category",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    quantity: Optional[Quantity] = field(
        default=None,
        metadata={
            "name": "Quantity",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    count: Optional[int] = field(
        default=None,
        metadata={
            "name": "Count",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    boolean_list: List[Union[str, NullEnumerationValue]] = field(
        default_factory=list,
        metadata={
            "name": "BooleanList",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "pattern": r"other:\w{2,}",
            "tokens": True,
        }
    )
    category_list: Optional[CategoryList] = field(
        default=None,
        metadata={
            "name": "CategoryList",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    quantity_list: Optional[QuantityList] = field(
        default=None,
        metadata={
            "name": "QuantityList",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    count_list: List[Union[str, NullEnumerationValue]] = field(
        default_factory=list,
        metadata={
            "name": "CountList",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "pattern": r"other:\w{2,}",
            "tokens": True,
        }
    )
    category_extent: Optional[CategoryExtent] = field(
        default=None,
        metadata={
            "name": "CategoryExtent",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    quantity_extent: Optional[QuantityExtent] = field(
        default=None,
        metadata={
            "name": "QuantityExtent",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    count_extent: List[Union[str, NullEnumerationValue]] = field(
        default_factory=list,
        metadata={
            "name": "CountExtent",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "length": 2,
            "pattern": r"other:\w{2,}",
            "tokens": True,
        }
    )
    value_array: Optional[ValueArray] = field(
        default=None,
        metadata={
            "name": "ValueArray",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    composite_value: Optional[CompositeValue] = field(
        default=None,
        metadata={
            "name": "CompositeValue",
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
class SequenceRuleType:
    value: Optional[SequenceRuleNames] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    order: Optional[IncrementOrder] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class DoubleOrNullTupleList:
    class Meta:
        name = "doubleOrNullTupleList"
        namespace = "http://www.opengis.net/gml"

    value: List[Union[str, NullEnumerationValue]] = field(
        default_factory=list,
        metadata={
            "pattern": r"other:\w{2,}",
            "tokens": True,
        }
    )


@dataclass
class TupleList(CoordinatesType):
    class Meta:
        name = "tupleList"
        namespace = "http://www.opengis.net/gml"


@dataclass
class GridDomainType(DomainSetType):
    pass


@dataclass
class GridFunctionType:
    """Defines how values in the domain are mapped to the range set.

    The start point and the sequencing rule are specified here.

    :ivar sequence_rule: If absent, the implied value is "Linear".
    :ivar start_point: Index position of the first grid post, which must
        lie somwhere in the GridEnvelope.  If absent, the startPoint is
        equal to the value of gridEnvelope::low from the grid
        definition.
    """
    sequence_rule: Optional[SequenceRuleType] = field(
        default=None,
        metadata={
            "name": "sequenceRule",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    start_point: List[int] = field(
        default_factory=list,
        metadata={
            "name": "startPoint",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "tokens": True,
        }
    )


@dataclass
class MultiCurveDomainType(DomainSetType):
    pass


@dataclass
class MultiPointDomainType(DomainSetType):
    pass


@dataclass
class MultiSolidDomainType(DomainSetType):
    pass


@dataclass
class MultiSurfaceDomainType(DomainSetType):
    pass


@dataclass
class RectifiedGridDomainType(DomainSetType):
    pass


@dataclass
class DomainSet(DomainSetType):
    class Meta:
        name = "domainSet"
        namespace = "http://www.opengis.net/gml"


@dataclass
class RangeParameters(RangeParametersType):
    class Meta:
        name = "rangeParameters"
        namespace = "http://www.opengis.net/gml"


@dataclass
class DataBlockType:
    range_parameters: Optional[RangeParameters] = field(
        default=None,
        metadata={
            "name": "rangeParameters",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )
    tuple_list: Optional[TupleList] = field(
        default=None,
        metadata={
            "name": "tupleList",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    double_or_null_tuple_list: List[Union[str, NullEnumerationValue]] = field(
        default_factory=list,
        metadata={
            "name": "doubleOrNullTupleList",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "pattern": r"other:\w{2,}",
            "tokens": True,
        }
    )


@dataclass
class FileType:
    range_parameters: Optional[RangeParameters] = field(
        default=None,
        metadata={
            "name": "rangeParameters",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )
    file_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "fileName",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )
    file_structure: Optional[FileValueModelType] = field(
        default=None,
        metadata={
            "name": "fileStructure",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )
    mime_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "mimeType",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    compression: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )


@dataclass
class GridFunction(GridFunctionType):
    class Meta:
        namespace = "http://www.opengis.net/gml"


@dataclass
class IndexMapType(GridFunctionType):
    """Exends GridFunctionType with a lookUpTable.

    This contains a list of indexes of members within the rangeSet
    corresponding with the members of the domainSet.  The domainSet is
    traversed in list order if it is enumerated explicitly, or in the
    order specified by a SequenceRule if the domain is an implicit set.
    The length of the lookUpTable corresponds with the length of the
    subset of the domainSet for which the coverage is defined.
    """
    look_up_table: List[int] = field(
        default_factory=list,
        metadata={
            "name": "lookUpTable",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
            "tokens": True,
        }
    )


@dataclass
class GridDomain(GridDomainType):
    class Meta:
        name = "gridDomain"
        namespace = "http://www.opengis.net/gml"


@dataclass
class MultiCurveDomain(MultiCurveDomainType):
    class Meta:
        name = "multiCurveDomain"
        namespace = "http://www.opengis.net/gml"


@dataclass
class MultiPointDomain(MultiPointDomainType):
    class Meta:
        name = "multiPointDomain"
        namespace = "http://www.opengis.net/gml"


@dataclass
class MultiSolidDomain(MultiSolidDomainType):
    class Meta:
        name = "multiSolidDomain"
        namespace = "http://www.opengis.net/gml"


@dataclass
class MultiSurfaceDomain(MultiSurfaceDomainType):
    class Meta:
        name = "multiSurfaceDomain"
        namespace = "http://www.opengis.net/gml"


@dataclass
class RectifiedGridDomain(RectifiedGridDomainType):
    class Meta:
        name = "rectifiedGridDomain"
        namespace = "http://www.opengis.net/gml"


@dataclass
class DataBlock(DataBlockType):
    class Meta:
        namespace = "http://www.opengis.net/gml"


@dataclass
class File(FileType):
    class Meta:
        namespace = "http://www.opengis.net/gml"


@dataclass
class IndexMap(IndexMapType):
    class Meta:
        namespace = "http://www.opengis.net/gml"


@dataclass
class CoverageFunctionType:
    """The function or rule which defines the map from members of the domainSet
    to the range.

    More functions will be added to this list
    """
    mapping_rule: Optional[MappingRule] = field(
        default=None,
        metadata={
            "name": "MappingRule",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    index_map: Optional[IndexMap] = field(
        default=None,
        metadata={
            "name": "IndexMap",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    grid_function: Optional[GridFunction] = field(
        default=None,
        metadata={
            "name": "GridFunction",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )


@dataclass
class RangeSetType:
    """
    :ivar value_array: each member _Value holds a tuple or "row" from
        the equivalent table
    :ivar boolean_list:
    :ivar category_list:
    :ivar quantity_list:
    :ivar count_list:
    :ivar data_block: Its tuple list holds the values as space-separated
        tuples each of which contains comma-separated components, and
        the tuple structure is specified using the rangeParameters
        property.
    :ivar file: a reference to an external source for the data, together
        with a description of how that external source is structured
    """
    value_array: List[ValueArray] = field(
        default_factory=list,
        metadata={
            "name": "ValueArray",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    boolean_list: List[List[Union[str, NullEnumerationValue]]] = field(
        default_factory=list,
        metadata={
            "name": "BooleanList",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "pattern": r"other:\w{2,}",
            "tokens": True,
        }
    )
    category_list: List[CategoryList] = field(
        default_factory=list,
        metadata={
            "name": "CategoryList",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    quantity_list: List[QuantityList] = field(
        default_factory=list,
        metadata={
            "name": "QuantityList",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    count_list: List[List[Union[str, NullEnumerationValue]]] = field(
        default_factory=list,
        metadata={
            "name": "CountList",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "pattern": r"other:\w{2,}",
            "tokens": True,
        }
    )
    data_block: Optional[DataBlock] = field(
        default=None,
        metadata={
            "name": "DataBlock",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    file: Optional[File] = field(
        default=None,
        metadata={
            "name": "File",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )


@dataclass
class CoverageFunction(CoverageFunctionType):
    class Meta:
        name = "coverageFunction"
        namespace = "http://www.opengis.net/gml"


@dataclass
class RangeSet(RangeSetType):
    class Meta:
        name = "rangeSet"
        namespace = "http://www.opengis.net/gml"


@dataclass
class AbstractCoverageType(AbstractFeatureType):
    """Abstract element which acts as the head of a substitution group for
    coverages.

    Note that a coverage is a GML feature.
    """
    rectified_grid_domain: Optional[RectifiedGridDomain] = field(
        default=None,
        metadata={
            "name": "rectifiedGridDomain",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    grid_domain: Optional[GridDomain] = field(
        default=None,
        metadata={
            "name": "gridDomain",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    multi_solid_domain: Optional[MultiSolidDomain] = field(
        default=None,
        metadata={
            "name": "multiSolidDomain",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    multi_surface_domain: Optional[MultiSurfaceDomain] = field(
        default=None,
        metadata={
            "name": "multiSurfaceDomain",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    multi_curve_domain: Optional[MultiCurveDomain] = field(
        default=None,
        metadata={
            "name": "multiCurveDomain",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    multi_point_domain: Optional[MultiPointDomain] = field(
        default=None,
        metadata={
            "name": "multiPointDomain",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    domain_set: Optional[DomainSet] = field(
        default=None,
        metadata={
            "name": "domainSet",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    range_set: Optional[RangeSet] = field(
        default=None,
        metadata={
            "name": "rangeSet",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )
    dimension: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class AbstractContinuousCoverageType(AbstractCoverageType):
    """
    A continuous coverage as defined in ISO 19123 is a coverage that can return
    different values for the same feature attribute at different direct
    positions within a single spatiotemporal object in its spatiotemporal
    domain.
    """
    coverage_function: Optional[CoverageFunction] = field(
        default=None,
        metadata={
            "name": "coverageFunction",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )


@dataclass
class AbstractDiscreteCoverageType(AbstractCoverageType):
    """A discrete coverage consists of a domain set, range set and optionally a
    coverage function.

    The domain set consists of either geometry or temporal objects,
    finite in number. The range set is comprised of a finite number of
    attribute values each of which is associated to every direct
    position within any single spatiotemporal object in the domain. In
    other words, the range values are constant on each spatiotemporal
    object in the domain. This coverage function maps each element from
    the coverage domain to an element in its range. This definition
    conforms to ISO 19123.
    """
    coverage_function: Optional[CoverageFunction] = field(
        default=None,
        metadata={
            "name": "coverageFunction",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )


@dataclass
class Coverage(AbstractCoverageType):
    class Meta:
        name = "_Coverage"
        namespace = "http://www.opengis.net/gml"


@dataclass
class GridCoverageType(AbstractDiscreteCoverageType):
    pass


@dataclass
class MultiCurveCoverageType(AbstractDiscreteCoverageType):
    """
    A discrete coverage type whose domain is defined by a collection of curves.
    """


@dataclass
class MultiPointCoverageType(AbstractDiscreteCoverageType):
    """
    A discrete coverage type whose domain is defined by a collection of point.
    """


@dataclass
class MultiSolidCoverageType(AbstractDiscreteCoverageType):
    """
    A discrete coverage type whose domain is defined by a collection of Solids.
    """


@dataclass
class MultiSurfaceCoverageType(AbstractDiscreteCoverageType):
    """
    A discrete coverage type whose domain is defined by a collection of surface
    patches (includes polygons, triangles, rectangles, etc).
    """


@dataclass
class RectifiedGridCoverageType(AbstractDiscreteCoverageType):
    pass


@dataclass
class ContinuousCoverage(AbstractContinuousCoverageType):
    class Meta:
        name = "_ContinuousCoverage"
        namespace = "http://www.opengis.net/gml"


@dataclass
class DiscreteCoverage(AbstractDiscreteCoverageType):
    class Meta:
        name = "_DiscreteCoverage"
        namespace = "http://www.opengis.net/gml"


@dataclass
class GridCoverage(GridCoverageType):
    class Meta:
        namespace = "http://www.opengis.net/gml"


@dataclass
class MultiCurveCoverage(MultiCurveCoverageType):
    class Meta:
        namespace = "http://www.opengis.net/gml"


@dataclass
class MultiPointCoverage(MultiPointCoverageType):
    class Meta:
        namespace = "http://www.opengis.net/gml"


@dataclass
class MultiSolidCoverage(MultiSolidCoverageType):
    class Meta:
        namespace = "http://www.opengis.net/gml"


@dataclass
class MultiSurfaceCoverage(MultiSurfaceCoverageType):
    class Meta:
        namespace = "http://www.opengis.net/gml"


@dataclass
class RectifiedGridCoverage(RectifiedGridCoverageType):
    class Meta:
        namespace = "http://www.opengis.net/gml"
