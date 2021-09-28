from dataclasses import dataclass, field
from typing import List, Optional
from bindings.wfs.after import After
from bindings.wfs.any_interacts import AnyInteracts
from bindings.wfs.bbox import Bbox
from bindings.wfs.before import Before
from bindings.wfs.begins import Begins
from bindings.wfs.begun_by import BegunBy
from bindings.wfs.beyond import Beyond
from bindings.wfs.comparison_ops import ComparisonOps
from bindings.wfs.contains import Contains
from bindings.wfs.crosses import Crosses
from bindings.wfs.disjoint import Disjoint
from bindings.wfs.during import During
from bindings.wfs.dwithin import Dwithin
from bindings.wfs.ended_by import EndedBy
from bindings.wfs.ends import Ends
from bindings.wfs.equals import Equals
from bindings.wfs.extension_ops import ExtensionOps
from bindings.wfs.function_type import Function
from bindings.wfs.id import Id
from bindings.wfs.intersects import Intersects
from bindings.wfs.logic_ops import LogicOps
from bindings.wfs.logic_ops_type import LogicOpsType
from bindings.wfs.meets import Meets
from bindings.wfs.met_by import MetBy
from bindings.wfs.overlapped_by import OverlappedBy
from bindings.wfs.overlaps import Overlaps
from bindings.wfs.property_is_between import PropertyIsBetween
from bindings.wfs.property_is_equal_to import PropertyIsEqualTo
from bindings.wfs.property_is_greater_than import PropertyIsGreaterThan
from bindings.wfs.property_is_greater_than_or_equal_to import PropertyIsGreaterThanOrEqualTo
from bindings.wfs.property_is_less_than import PropertyIsLessThan
from bindings.wfs.property_is_less_than_or_equal_to import PropertyIsLessThanOrEqualTo
from bindings.wfs.property_is_like import PropertyIsLike
from bindings.wfs.property_is_nil import PropertyIsNil
from bindings.wfs.property_is_not_equal_to import PropertyIsNotEqualTo
from bindings.wfs.property_is_null import PropertyIsNull
from bindings.wfs.resource_id import ResourceId
from bindings.wfs.spatial_ops import SpatialOps
from bindings.wfs.tcontains import Tcontains
from bindings.wfs.temporal_ops import TemporalOps
from bindings.wfs.tequals import Tequals
from bindings.wfs.touches import Touches
from bindings.wfs.toverlaps import Toverlaps
from bindings.wfs.within import Within

__NAMESPACE__ = "http://www.opengis.net/fes/2.0"


@dataclass
class BinaryLogicOpType(LogicOpsType):
    property_is_between: List[PropertyIsBetween] = field(
        default_factory=list,
        metadata={
            "name": "PropertyIsBetween",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
            "min_occurs": 2,
        }
    )
    property_is_nil: List[PropertyIsNil] = field(
        default_factory=list,
        metadata={
            "name": "PropertyIsNil",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
            "min_occurs": 2,
        }
    )
    property_is_null: List[PropertyIsNull] = field(
        default_factory=list,
        metadata={
            "name": "PropertyIsNull",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
            "min_occurs": 2,
        }
    )
    property_is_like: List[PropertyIsLike] = field(
        default_factory=list,
        metadata={
            "name": "PropertyIsLike",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
            "min_occurs": 2,
        }
    )
    property_is_greater_than_or_equal_to: List[PropertyIsGreaterThanOrEqualTo] = field(
        default_factory=list,
        metadata={
            "name": "PropertyIsGreaterThanOrEqualTo",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
            "min_occurs": 2,
        }
    )
    property_is_less_than_or_equal_to: List[PropertyIsLessThanOrEqualTo] = field(
        default_factory=list,
        metadata={
            "name": "PropertyIsLessThanOrEqualTo",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
            "min_occurs": 2,
        }
    )
    property_is_greater_than: List[PropertyIsGreaterThan] = field(
        default_factory=list,
        metadata={
            "name": "PropertyIsGreaterThan",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
            "min_occurs": 2,
        }
    )
    property_is_less_than: List[PropertyIsLessThan] = field(
        default_factory=list,
        metadata={
            "name": "PropertyIsLessThan",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
            "min_occurs": 2,
        }
    )
    property_is_not_equal_to: List[PropertyIsNotEqualTo] = field(
        default_factory=list,
        metadata={
            "name": "PropertyIsNotEqualTo",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
            "min_occurs": 2,
        }
    )
    property_is_equal_to: List[PropertyIsEqualTo] = field(
        default_factory=list,
        metadata={
            "name": "PropertyIsEqualTo",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
            "min_occurs": 2,
        }
    )
    comparison_ops: List[ComparisonOps] = field(
        default_factory=list,
        metadata={
            "name": "comparisonOps",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
            "min_occurs": 2,
        }
    )
    bbox: List[Bbox] = field(
        default_factory=list,
        metadata={
            "name": "BBOX",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
            "min_occurs": 2,
        }
    )
    beyond: List[Beyond] = field(
        default_factory=list,
        metadata={
            "name": "Beyond",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
            "min_occurs": 2,
        }
    )
    dwithin: List[Dwithin] = field(
        default_factory=list,
        metadata={
            "name": "DWithin",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
            "min_occurs": 2,
        }
    )
    contains: List[Contains] = field(
        default_factory=list,
        metadata={
            "name": "Contains",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
            "min_occurs": 2,
        }
    )
    intersects: List[Intersects] = field(
        default_factory=list,
        metadata={
            "name": "Intersects",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
            "min_occurs": 2,
        }
    )
    crosses: List[Crosses] = field(
        default_factory=list,
        metadata={
            "name": "Crosses",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
            "min_occurs": 2,
        }
    )
    overlaps: List[Overlaps] = field(
        default_factory=list,
        metadata={
            "name": "Overlaps",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
            "min_occurs": 2,
        }
    )
    within: List[Within] = field(
        default_factory=list,
        metadata={
            "name": "Within",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
            "min_occurs": 2,
        }
    )
    touches: List[Touches] = field(
        default_factory=list,
        metadata={
            "name": "Touches",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
            "min_occurs": 2,
        }
    )
    disjoint: List[Disjoint] = field(
        default_factory=list,
        metadata={
            "name": "Disjoint",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
            "min_occurs": 2,
        }
    )
    equals: List[Equals] = field(
        default_factory=list,
        metadata={
            "name": "Equals",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
            "min_occurs": 2,
        }
    )
    spatial_ops: List[SpatialOps] = field(
        default_factory=list,
        metadata={
            "name": "spatialOps",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
            "min_occurs": 2,
        }
    )
    any_interacts: List[AnyInteracts] = field(
        default_factory=list,
        metadata={
            "name": "AnyInteracts",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
            "min_occurs": 2,
        }
    )
    overlapped_by: List[OverlappedBy] = field(
        default_factory=list,
        metadata={
            "name": "OverlappedBy",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
            "min_occurs": 2,
        }
    )
    toverlaps: List[Toverlaps] = field(
        default_factory=list,
        metadata={
            "name": "TOverlaps",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
            "min_occurs": 2,
        }
    )
    met_by: List[MetBy] = field(
        default_factory=list,
        metadata={
            "name": "MetBy",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
            "min_occurs": 2,
        }
    )
    meets: List[Meets] = field(
        default_factory=list,
        metadata={
            "name": "Meets",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
            "min_occurs": 2,
        }
    )
    tequals: List[Tequals] = field(
        default_factory=list,
        metadata={
            "name": "TEquals",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
            "min_occurs": 2,
        }
    )
    ends: List[Ends] = field(
        default_factory=list,
        metadata={
            "name": "Ends",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
            "min_occurs": 2,
        }
    )
    ended_by: List[EndedBy] = field(
        default_factory=list,
        metadata={
            "name": "EndedBy",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
            "min_occurs": 2,
        }
    )
    during: List[During] = field(
        default_factory=list,
        metadata={
            "name": "During",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
            "min_occurs": 2,
        }
    )
    tcontains: List[Tcontains] = field(
        default_factory=list,
        metadata={
            "name": "TContains",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
            "min_occurs": 2,
        }
    )
    begun_by: List[BegunBy] = field(
        default_factory=list,
        metadata={
            "name": "BegunBy",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
            "min_occurs": 2,
        }
    )
    begins: List[Begins] = field(
        default_factory=list,
        metadata={
            "name": "Begins",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
            "min_occurs": 2,
        }
    )
    before: List[Before] = field(
        default_factory=list,
        metadata={
            "name": "Before",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
            "min_occurs": 2,
        }
    )
    after: List[After] = field(
        default_factory=list,
        metadata={
            "name": "After",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
            "min_occurs": 2,
        }
    )
    temporal_ops: List[TemporalOps] = field(
        default_factory=list,
        metadata={
            "name": "temporalOps",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
            "min_occurs": 2,
        }
    )
    not_value: List["Not"] = field(
        default_factory=list,
        metadata={
            "name": "Not",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
            "min_occurs": 2,
        }
    )
    or_value: List["Or"] = field(
        default_factory=list,
        metadata={
            "name": "Or",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
            "min_occurs": 2,
        }
    )
    and_value: List["And"] = field(
        default_factory=list,
        metadata={
            "name": "And",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
            "min_occurs": 2,
        }
    )
    logic_ops: List[LogicOps] = field(
        default_factory=list,
        metadata={
            "name": "logicOps",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
            "min_occurs": 2,
        }
    )
    extension_ops: List[ExtensionOps] = field(
        default_factory=list,
        metadata={
            "name": "extensionOps",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
            "min_occurs": 2,
        }
    )
    function: List[Function] = field(
        default_factory=list,
        metadata={
            "name": "Function",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
            "min_occurs": 2,
        }
    )
    resource_id: List[ResourceId] = field(
        default_factory=list,
        metadata={
            "name": "ResourceId",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
            "min_occurs": 2,
        }
    )
    id: List[Id] = field(
        default_factory=list,
        metadata={
            "name": "_Id",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
            "min_occurs": 2,
        }
    )


@dataclass
class And(BinaryLogicOpType):
    class Meta:
        namespace = "http://www.opengis.net/fes/2.0"


@dataclass
class Or(BinaryLogicOpType):
    class Meta:
        namespace = "http://www.opengis.net/fes/2.0"


@dataclass
class UnaryLogicOpType(LogicOpsType):
    property_is_between: Optional[PropertyIsBetween] = field(
        default=None,
        metadata={
            "name": "PropertyIsBetween",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
        }
    )
    property_is_nil: Optional[PropertyIsNil] = field(
        default=None,
        metadata={
            "name": "PropertyIsNil",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
        }
    )
    property_is_null: Optional[PropertyIsNull] = field(
        default=None,
        metadata={
            "name": "PropertyIsNull",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
        }
    )
    property_is_like: Optional[PropertyIsLike] = field(
        default=None,
        metadata={
            "name": "PropertyIsLike",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
        }
    )
    property_is_greater_than_or_equal_to: Optional[PropertyIsGreaterThanOrEqualTo] = field(
        default=None,
        metadata={
            "name": "PropertyIsGreaterThanOrEqualTo",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
        }
    )
    property_is_less_than_or_equal_to: Optional[PropertyIsLessThanOrEqualTo] = field(
        default=None,
        metadata={
            "name": "PropertyIsLessThanOrEqualTo",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
        }
    )
    property_is_greater_than: Optional[PropertyIsGreaterThan] = field(
        default=None,
        metadata={
            "name": "PropertyIsGreaterThan",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
        }
    )
    property_is_less_than: Optional[PropertyIsLessThan] = field(
        default=None,
        metadata={
            "name": "PropertyIsLessThan",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
        }
    )
    property_is_not_equal_to: Optional[PropertyIsNotEqualTo] = field(
        default=None,
        metadata={
            "name": "PropertyIsNotEqualTo",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
        }
    )
    property_is_equal_to: Optional[PropertyIsEqualTo] = field(
        default=None,
        metadata={
            "name": "PropertyIsEqualTo",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
        }
    )
    comparison_ops: Optional[ComparisonOps] = field(
        default=None,
        metadata={
            "name": "comparisonOps",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
        }
    )
    bbox: Optional[Bbox] = field(
        default=None,
        metadata={
            "name": "BBOX",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
        }
    )
    beyond: Optional[Beyond] = field(
        default=None,
        metadata={
            "name": "Beyond",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
        }
    )
    dwithin: Optional[Dwithin] = field(
        default=None,
        metadata={
            "name": "DWithin",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
        }
    )
    contains: Optional[Contains] = field(
        default=None,
        metadata={
            "name": "Contains",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
        }
    )
    intersects: Optional[Intersects] = field(
        default=None,
        metadata={
            "name": "Intersects",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
        }
    )
    crosses: Optional[Crosses] = field(
        default=None,
        metadata={
            "name": "Crosses",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
        }
    )
    overlaps: Optional[Overlaps] = field(
        default=None,
        metadata={
            "name": "Overlaps",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
        }
    )
    within: Optional[Within] = field(
        default=None,
        metadata={
            "name": "Within",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
        }
    )
    touches: Optional[Touches] = field(
        default=None,
        metadata={
            "name": "Touches",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
        }
    )
    disjoint: Optional[Disjoint] = field(
        default=None,
        metadata={
            "name": "Disjoint",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
        }
    )
    equals: Optional[Equals] = field(
        default=None,
        metadata={
            "name": "Equals",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
        }
    )
    spatial_ops: Optional[SpatialOps] = field(
        default=None,
        metadata={
            "name": "spatialOps",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
        }
    )
    any_interacts: Optional[AnyInteracts] = field(
        default=None,
        metadata={
            "name": "AnyInteracts",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
        }
    )
    overlapped_by: Optional[OverlappedBy] = field(
        default=None,
        metadata={
            "name": "OverlappedBy",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
        }
    )
    toverlaps: Optional[Toverlaps] = field(
        default=None,
        metadata={
            "name": "TOverlaps",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
        }
    )
    met_by: Optional[MetBy] = field(
        default=None,
        metadata={
            "name": "MetBy",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
        }
    )
    meets: Optional[Meets] = field(
        default=None,
        metadata={
            "name": "Meets",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
        }
    )
    tequals: Optional[Tequals] = field(
        default=None,
        metadata={
            "name": "TEquals",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
        }
    )
    ends: Optional[Ends] = field(
        default=None,
        metadata={
            "name": "Ends",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
        }
    )
    ended_by: Optional[EndedBy] = field(
        default=None,
        metadata={
            "name": "EndedBy",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
        }
    )
    during: Optional[During] = field(
        default=None,
        metadata={
            "name": "During",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
        }
    )
    tcontains: Optional[Tcontains] = field(
        default=None,
        metadata={
            "name": "TContains",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
        }
    )
    begun_by: Optional[BegunBy] = field(
        default=None,
        metadata={
            "name": "BegunBy",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
        }
    )
    begins: Optional[Begins] = field(
        default=None,
        metadata={
            "name": "Begins",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
        }
    )
    before: Optional[Before] = field(
        default=None,
        metadata={
            "name": "Before",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
        }
    )
    after: Optional[After] = field(
        default=None,
        metadata={
            "name": "After",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
        }
    )
    temporal_ops: Optional[TemporalOps] = field(
        default=None,
        metadata={
            "name": "temporalOps",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
        }
    )
    not_value: Optional["Not"] = field(
        default=None,
        metadata={
            "name": "Not",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
        }
    )
    or_value: Optional[Or] = field(
        default=None,
        metadata={
            "name": "Or",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
        }
    )
    and_value: Optional[And] = field(
        default=None,
        metadata={
            "name": "And",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
        }
    )
    logic_ops: Optional[LogicOps] = field(
        default=None,
        metadata={
            "name": "logicOps",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
        }
    )
    extension_ops: Optional[ExtensionOps] = field(
        default=None,
        metadata={
            "name": "extensionOps",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
        }
    )
    function: Optional[Function] = field(
        default=None,
        metadata={
            "name": "Function",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
        }
    )
    resource_id: List[ResourceId] = field(
        default_factory=list,
        metadata={
            "name": "ResourceId",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
        }
    )
    id: List[Id] = field(
        default_factory=list,
        metadata={
            "name": "_Id",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
        }
    )


@dataclass
class Not(UnaryLogicOpType):
    class Meta:
        namespace = "http://www.opengis.net/fes/2.0"
