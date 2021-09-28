from dataclasses import dataclass, field
from typing import List, Optional
from bindings.wfs.abstract_selection_clause_type import AbstractSelectionClauseType
from bindings.wfs.after import After
from bindings.wfs.any_interacts import AnyInteracts
from bindings.wfs.bbox import Bbox
from bindings.wfs.before import Before
from bindings.wfs.begins import Begins
from bindings.wfs.begun_by import BegunBy
from bindings.wfs.beyond import Beyond
from bindings.wfs.binary_logic_op_type import (
    And,
    Not,
    Or,
)
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
class FilterType(AbstractSelectionClauseType):
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
    not_value: Optional[Not] = field(
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
