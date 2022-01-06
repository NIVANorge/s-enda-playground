from dataclasses import dataclass, field
from typing import List, Optional
from bindings.gmd.abstract_geometric_aggregate_type import (
    AbstractGeometricAggregateType,
)
from bindings.gmd.point_member import PointMember
from bindings.gmd.point_members import PointMembers

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class MultiPointType(AbstractGeometricAggregateType):
    point_member: List[PointMember] = field(
        default_factory=list,
        metadata={
            "name": "pointMember",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    point_members: Optional[PointMembers] = field(
        default=None,
        metadata={
            "name": "pointMembers",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
