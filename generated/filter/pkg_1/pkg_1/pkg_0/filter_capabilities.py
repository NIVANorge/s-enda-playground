from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional
from xml.etree.ElementTree import QName

__NAMESPACE__ = "http://www.opengis.net/ogc"


class ComparisonOperatorType(Enum):
    LESS_THAN = "LessThan"
    GREATER_THAN = "GreaterThan"
    LESS_THAN_EQUAL_TO = "LessThanEqualTo"
    GREATER_THAN_EQUAL_TO = "GreaterThanEqualTo"
    EQUAL_TO = "EqualTo"
    NOT_EQUAL_TO = "NotEqualTo"
    LIKE = "Like"
    BETWEEN = "Between"
    NULL_CHECK = "NullCheck"


@dataclass
class Eid:
    class Meta:
        name = "EID"
        namespace = "http://www.opengis.net/ogc"


@dataclass
class Fid:
    class Meta:
        name = "FID"
        namespace = "http://www.opengis.net/ogc"


@dataclass
class FunctionNameType:
    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    n_args: Optional[str] = field(
        default=None,
        metadata={
            "name": "nArgs",
            "type": "Attribute",
            "required": True,
        }
    )


class GeometryOperandType(Enum):
    GML_ENVELOPE = QName("{http://www.opengis.net/gml}Envelope")
    GML_POINT = QName("{http://www.opengis.net/gml}Point")
    GML_LINE_STRING = QName("{http://www.opengis.net/gml}LineString")
    GML_POLYGON = QName("{http://www.opengis.net/gml}Polygon")
    GML_ARC_BY_CENTER_POINT = QName("{http://www.opengis.net/gml}ArcByCenterPoint")
    GML_CIRCLE_BY_CENTER_POINT = QName("{http://www.opengis.net/gml}CircleByCenterPoint")
    GML_ARC = QName("{http://www.opengis.net/gml}Arc")
    GML_CIRCLE = QName("{http://www.opengis.net/gml}Circle")
    GML_ARC_BY_BULGE = QName("{http://www.opengis.net/gml}ArcByBulge")
    GML_BEZIER = QName("{http://www.opengis.net/gml}Bezier")
    GML_CLOTHOID = QName("{http://www.opengis.net/gml}Clothoid")
    GML_CUBIC_SPLINE = QName("{http://www.opengis.net/gml}CubicSpline")
    GML_GEODESIC = QName("{http://www.opengis.net/gml}Geodesic")
    GML_OFFSET_CURVE = QName("{http://www.opengis.net/gml}OffsetCurve")
    GML_TRIANGLE = QName("{http://www.opengis.net/gml}Triangle")
    GML_POLYHEDRAL_SURFACE = QName("{http://www.opengis.net/gml}PolyhedralSurface")
    GML_TRIANGULATED_SURFACE = QName("{http://www.opengis.net/gml}TriangulatedSurface")
    GML_TIN = QName("{http://www.opengis.net/gml}Tin")
    GML_SOLID = QName("{http://www.opengis.net/gml}Solid")


@dataclass
class LogicalOperators:
    class Meta:
        namespace = "http://www.opengis.net/ogc"


@dataclass
class SimpleArithmetic:
    class Meta:
        namespace = "http://www.opengis.net/ogc"


class SpatialOperatorNameType(Enum):
    BBOX = "BBOX"
    EQUALS = "Equals"
    DISJOINT = "Disjoint"
    INTERSECTS = "Intersects"
    TOUCHES = "Touches"
    CROSSES = "Crosses"
    WITHIN = "Within"
    CONTAINS = "Contains"
    OVERLAPS = "Overlaps"
    BEYOND = "Beyond"
    DWITHIN = "DWithin"


@dataclass
class ComparisonOperatorsType:
    comparison_operator: List[ComparisonOperatorType] = field(
        default_factory=list,
        metadata={
            "name": "ComparisonOperator",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
            "min_occurs": 1,
        }
    )


@dataclass
class FunctionNamesType:
    function_name: List[FunctionNameType] = field(
        default_factory=list,
        metadata={
            "name": "FunctionName",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
            "min_occurs": 1,
        }
    )


@dataclass
class GeometryOperandsType:
    geometry_operand: List[GeometryOperandType] = field(
        default_factory=list,
        metadata={
            "name": "GeometryOperand",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
            "min_occurs": 1,
        }
    )


@dataclass
class IdCapabilitiesType:
    class Meta:
        name = "Id_CapabilitiesType"

    eid: List[Eid] = field(
        default_factory=list,
        metadata={
            "name": "EID",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        }
    )
    fid: List[Fid] = field(
        default_factory=list,
        metadata={
            "name": "FID",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        }
    )


@dataclass
class FunctionsType:
    function_names: Optional[FunctionNamesType] = field(
        default=None,
        metadata={
            "name": "FunctionNames",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
            "required": True,
        }
    )


@dataclass
class SpatialOperatorType:
    geometry_operands: Optional[GeometryOperandsType] = field(
        default=None,
        metadata={
            "name": "GeometryOperands",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        }
    )
    name: Optional[SpatialOperatorNameType] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class ArithmeticOperatorsType:
    simple_arithmetic: List[SimpleArithmetic] = field(
        default_factory=list,
        metadata={
            "name": "SimpleArithmetic",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        }
    )
    functions: List[FunctionsType] = field(
        default_factory=list,
        metadata={
            "name": "Functions",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        }
    )


@dataclass
class SpatialOperatorsType:
    spatial_operator: List[SpatialOperatorType] = field(
        default_factory=list,
        metadata={
            "name": "SpatialOperator",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
            "min_occurs": 1,
        }
    )


@dataclass
class ScalarCapabilitiesType:
    class Meta:
        name = "Scalar_CapabilitiesType"

    logical_operators: Optional[LogicalOperators] = field(
        default=None,
        metadata={
            "name": "LogicalOperators",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        }
    )
    comparison_operators: Optional[ComparisonOperatorsType] = field(
        default=None,
        metadata={
            "name": "ComparisonOperators",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        }
    )
    arithmetic_operators: Optional[ArithmeticOperatorsType] = field(
        default=None,
        metadata={
            "name": "ArithmeticOperators",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        }
    )


@dataclass
class SpatialCapabilitiesType:
    class Meta:
        name = "Spatial_CapabilitiesType"

    geometry_operands: Optional[GeometryOperandsType] = field(
        default=None,
        metadata={
            "name": "GeometryOperands",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
            "required": True,
        }
    )
    spatial_operators: Optional[SpatialOperatorsType] = field(
        default=None,
        metadata={
            "name": "SpatialOperators",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
            "required": True,
        }
    )


@dataclass
class FilterCapabilities:
    class Meta:
        name = "Filter_Capabilities"
        namespace = "http://www.opengis.net/ogc"

    spatial_capabilities: Optional[SpatialCapabilitiesType] = field(
        default=None,
        metadata={
            "name": "Spatial_Capabilities",
            "type": "Element",
            "required": True,
        }
    )
    scalar_capabilities: Optional[ScalarCapabilitiesType] = field(
        default=None,
        metadata={
            "name": "Scalar_Capabilities",
            "type": "Element",
            "required": True,
        }
    )
    id_capabilities: Optional[IdCapabilitiesType] = field(
        default=None,
        metadata={
            "name": "Id_Capabilities",
            "type": "Element",
            "required": True,
        }
    )
