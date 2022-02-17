from dataclasses import dataclass, field
from typing import List, Optional
from bindings.gmd.abstract_ring_type import AbstractRingType
from bindings.gmd.aggregation_type import AggregationType
from bindings.gmd.composite_curve_type import CurveMember

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class RingType(AbstractRingType):
    curve_member: List[CurveMember] = field(
        default_factory=list,
        metadata={
            "name": "curveMember",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "min_occurs": 1,
        },
    )
    aggregation_type: Optional[AggregationType] = field(
        default=None,
        metadata={
            "name": "aggregationType",
            "type": "Attribute",
        },
    )
