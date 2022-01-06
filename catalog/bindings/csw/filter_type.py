from dataclasses import dataclass, field
from typing import List, Optional
from bindings.csw.bbox import Bbox
from bindings.csw.beyond import Beyond
from bindings.csw.binary_logic_op_type import (
    And,
    Not,
    Or,
)
from bindings.csw.comparison_ops import ComparisonOps
from bindings.csw.contains import Contains
from bindings.csw.crosses import Crosses
from bindings.csw.disjoint import Disjoint
from bindings.csw.dwithin import Dwithin
from bindings.csw.equals import Equals
from bindings.csw.feature_id import FeatureId
from bindings.csw.gml_object_id import GmlObjectId
from bindings.csw.id import Id
from bindings.csw.intersects import Intersects
from bindings.csw.logic_ops import LogicOps
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
class FilterType:
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
    not_value: Optional[Not] = field(
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
    gml_object_id: List[GmlObjectId] = field(
        default_factory=list,
        metadata={
            "name": "GmlObjectId",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        },
    )
    feature_id: List[FeatureId] = field(
        default_factory=list,
        metadata={
            "name": "FeatureId",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        },
    )
    id: List[Id] = field(
        default_factory=list,
        metadata={
            "name": "_Id",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        },
    )
