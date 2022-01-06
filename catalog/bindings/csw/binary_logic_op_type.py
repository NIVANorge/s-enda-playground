from dataclasses import dataclass, field
from typing import List, Optional
from bindings.csw.bbox import Bbox
from bindings.csw.beyond import Beyond
from bindings.csw.comparison_ops import ComparisonOps
from bindings.csw.contains import Contains
from bindings.csw.crosses import Crosses
from bindings.csw.disjoint import Disjoint
from bindings.csw.dwithin import Dwithin
from bindings.csw.equals import Equals
from bindings.csw.function_type import Function
from bindings.csw.intersects import Intersects
from bindings.csw.logic_ops import LogicOps
from bindings.csw.logic_ops_type import LogicOpsType
from bindings.csw.overlaps import Overlaps
from bindings.csw.property_is_between import PropertyIsBetween
from bindings.csw.property_is_equal_to import PropertyIsEqualTo
from bindings.csw.property_is_greater_than import PropertyIsGreaterThan
from bindings.csw.property_is_greater_than_or_equal_to import (
    PropertyIsGreaterThanOrEqualTo,
)
from bindings.csw.property_is_less_than import PropertyIsLessThan
from bindings.csw.property_is_less_than_or_equal_to import PropertyIsLessThanOrEqualTo
from bindings.csw.property_is_like import PropertyIsLike
from bindings.csw.property_is_not_equal_to import PropertyIsNotEqualTo
from bindings.csw.property_is_null import PropertyIsNull
from bindings.csw.spatial_ops import SpatialOps
from bindings.csw.touches import Touches
from bindings.csw.within import Within

__NAMESPACE__ = "http://www.opengis.net/ogc"


@dataclass
class BinaryLogicOpType(LogicOpsType):
    property_is_between: List[PropertyIsBetween] = field(
        default_factory=list,
        metadata={
            "name": "PropertyIsBetween",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        },
    )
    property_is_null: List[PropertyIsNull] = field(
        default_factory=list,
        metadata={
            "name": "PropertyIsNull",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        },
    )
    property_is_like: List[PropertyIsLike] = field(
        default_factory=list,
        metadata={
            "name": "PropertyIsLike",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        },
    )
    property_is_greater_than_or_equal_to: List[PropertyIsGreaterThanOrEqualTo] = field(
        default_factory=list,
        metadata={
            "name": "PropertyIsGreaterThanOrEqualTo",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        },
    )
    property_is_less_than_or_equal_to: List[PropertyIsLessThanOrEqualTo] = field(
        default_factory=list,
        metadata={
            "name": "PropertyIsLessThanOrEqualTo",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        },
    )
    property_is_greater_than: List[PropertyIsGreaterThan] = field(
        default_factory=list,
        metadata={
            "name": "PropertyIsGreaterThan",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        },
    )
    property_is_less_than: List[PropertyIsLessThan] = field(
        default_factory=list,
        metadata={
            "name": "PropertyIsLessThan",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        },
    )
    property_is_not_equal_to: List[PropertyIsNotEqualTo] = field(
        default_factory=list,
        metadata={
            "name": "PropertyIsNotEqualTo",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        },
    )
    property_is_equal_to: List[PropertyIsEqualTo] = field(
        default_factory=list,
        metadata={
            "name": "PropertyIsEqualTo",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        },
    )
    comparison_ops: List[ComparisonOps] = field(
        default_factory=list,
        metadata={
            "name": "comparisonOps",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        },
    )
    bbox: List[Bbox] = field(
        default_factory=list,
        metadata={
            "name": "BBOX",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        },
    )
    beyond: List[Beyond] = field(
        default_factory=list,
        metadata={
            "name": "Beyond",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        },
    )
    dwithin: List[Dwithin] = field(
        default_factory=list,
        metadata={
            "name": "DWithin",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        },
    )
    contains: List[Contains] = field(
        default_factory=list,
        metadata={
            "name": "Contains",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        },
    )
    intersects: List[Intersects] = field(
        default_factory=list,
        metadata={
            "name": "Intersects",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        },
    )
    crosses: List[Crosses] = field(
        default_factory=list,
        metadata={
            "name": "Crosses",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        },
    )
    overlaps: List[Overlaps] = field(
        default_factory=list,
        metadata={
            "name": "Overlaps",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        },
    )
    within: List[Within] = field(
        default_factory=list,
        metadata={
            "name": "Within",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        },
    )
    touches: List[Touches] = field(
        default_factory=list,
        metadata={
            "name": "Touches",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        },
    )
    disjoint: List[Disjoint] = field(
        default_factory=list,
        metadata={
            "name": "Disjoint",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        },
    )
    equals: List[Equals] = field(
        default_factory=list,
        metadata={
            "name": "Equals",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        },
    )
    spatial_ops: List[SpatialOps] = field(
        default_factory=list,
        metadata={
            "name": "spatialOps",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        },
    )
    not_value: List["Not"] = field(
        default_factory=list,
        metadata={
            "name": "Not",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        },
    )
    or_value: List["Or"] = field(
        default_factory=list,
        metadata={
            "name": "Or",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        },
    )
    and_value: List["And"] = field(
        default_factory=list,
        metadata={
            "name": "And",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        },
    )
    logic_ops: List[LogicOps] = field(
        default_factory=list,
        metadata={
            "name": "logicOps",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        },
    )
    function: List[Function] = field(
        default_factory=list,
        metadata={
            "name": "Function",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
            "min_occurs": 2,
        },
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
        },
    )
    property_is_null: Optional[PropertyIsNull] = field(
        default=None,
        metadata={
            "name": "PropertyIsNull",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        },
    )
    property_is_like: Optional[PropertyIsLike] = field(
        default=None,
        metadata={
            "name": "PropertyIsLike",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        },
    )
    property_is_greater_than_or_equal_to: Optional[
        PropertyIsGreaterThanOrEqualTo
    ] = field(
        default=None,
        metadata={
            "name": "PropertyIsGreaterThanOrEqualTo",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        },
    )
    property_is_less_than_or_equal_to: Optional[PropertyIsLessThanOrEqualTo] = field(
        default=None,
        metadata={
            "name": "PropertyIsLessThanOrEqualTo",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        },
    )
    property_is_greater_than: Optional[PropertyIsGreaterThan] = field(
        default=None,
        metadata={
            "name": "PropertyIsGreaterThan",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        },
    )
    property_is_less_than: Optional[PropertyIsLessThan] = field(
        default=None,
        metadata={
            "name": "PropertyIsLessThan",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        },
    )
    property_is_not_equal_to: Optional[PropertyIsNotEqualTo] = field(
        default=None,
        metadata={
            "name": "PropertyIsNotEqualTo",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        },
    )
    property_is_equal_to: Optional[PropertyIsEqualTo] = field(
        default=None,
        metadata={
            "name": "PropertyIsEqualTo",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        },
    )
    comparison_ops: Optional[ComparisonOps] = field(
        default=None,
        metadata={
            "name": "comparisonOps",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        },
    )
    bbox: Optional[Bbox] = field(
        default=None,
        metadata={
            "name": "BBOX",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        },
    )
    beyond: Optional[Beyond] = field(
        default=None,
        metadata={
            "name": "Beyond",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        },
    )
    dwithin: Optional[Dwithin] = field(
        default=None,
        metadata={
            "name": "DWithin",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        },
    )
    contains: Optional[Contains] = field(
        default=None,
        metadata={
            "name": "Contains",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        },
    )
    intersects: Optional[Intersects] = field(
        default=None,
        metadata={
            "name": "Intersects",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        },
    )
    crosses: Optional[Crosses] = field(
        default=None,
        metadata={
            "name": "Crosses",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        },
    )
    overlaps: Optional[Overlaps] = field(
        default=None,
        metadata={
            "name": "Overlaps",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        },
    )
    within: Optional[Within] = field(
        default=None,
        metadata={
            "name": "Within",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        },
    )
    touches: Optional[Touches] = field(
        default=None,
        metadata={
            "name": "Touches",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        },
    )
    disjoint: Optional[Disjoint] = field(
        default=None,
        metadata={
            "name": "Disjoint",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        },
    )
    equals: Optional[Equals] = field(
        default=None,
        metadata={
            "name": "Equals",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        },
    )
    spatial_ops: Optional[SpatialOps] = field(
        default=None,
        metadata={
            "name": "spatialOps",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        },
    )
    not_value: Optional["Not"] = field(
        default=None,
        metadata={
            "name": "Not",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        },
    )
    or_value: Optional[Or] = field(
        default=None,
        metadata={
            "name": "Or",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        },
    )
    and_value: Optional[And] = field(
        default=None,
        metadata={
            "name": "And",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        },
    )
    logic_ops: Optional[LogicOps] = field(
        default=None,
        metadata={
            "name": "logicOps",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        },
    )
    function: Optional[Function] = field(
        default=None,
        metadata={
            "name": "Function",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        },
    )


@dataclass
class Not(UnaryLogicOpType):
    class Meta:
        namespace = "http://www.opengis.net/ogc"
