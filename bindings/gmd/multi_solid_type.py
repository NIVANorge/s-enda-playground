from dataclasses import dataclass, field
from typing import List, Optional
from bindings.gmd.abstract_geometric_aggregate_type import AbstractGeometricAggregateType
from bindings.gmd.solid_members import SolidMembers
from bindings.gmd.solid_property_type import SolidMember

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class MultiSolidType(AbstractGeometricAggregateType):
    solid_member: List[SolidMember] = field(
        default_factory=list,
        metadata={
            "name": "solidMember",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    solid_members: Optional[SolidMembers] = field(
        default=None,
        metadata={
            "name": "solidMembers",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
