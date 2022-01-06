from dataclasses import dataclass, field
from typing import List, Optional
from bindings.csw.abstract_geometric_aggregate_type import (
    AbstractGeometricAggregateType,
)
from bindings.csw.composite_solid_type import SolidMember
from bindings.csw.solid_members import SolidMembers

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class MultiSolidType(AbstractGeometricAggregateType):
    """
    A MultiSolid is defined by one or more Solids, referenced through
    solidMember elements.
    """

    solid_member: List[SolidMember] = field(
        default_factory=list,
        metadata={
            "name": "solidMember",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    solid_members: Optional[SolidMembers] = field(
        default=None,
        metadata={
            "name": "solidMembers",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
