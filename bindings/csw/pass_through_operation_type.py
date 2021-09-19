from dataclasses import dataclass, field
from typing import List, Optional
from bindings.csw.general_conversion_ref_type import AbstractCoordinateOperationType
from bindings.csw.uses_operation import UsesOperation

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class PassThroughOperationType(AbstractCoordinateOperationType):
    """
    A pass-through operation specifies that a subset of a coordinate tuple is
    subject to a specific coordinate operation.

    :ivar modified_coordinate: Ordered sequence of positive integers
        defining the positions in a coordinate tuple of the coordinates
        affected by this pass-through operation.
    :ivar uses_operation:
    """
    modified_coordinate: List[int] = field(
        default_factory=list,
        metadata={
            "name": "modifiedCoordinate",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "min_occurs": 1,
        }
    )
    uses_operation: Optional[UsesOperation] = field(
        default=None,
        metadata={
            "name": "usesOperation",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )
