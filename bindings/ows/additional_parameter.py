from dataclasses import dataclass, field
from typing import List, Optional
from bindings.ows.code_type import CodeType

__NAMESPACE__ = "http://www.opengis.net/ows/2.0"


@dataclass
class AdditionalParameter:
    """
    One additional metadata parameter.

    :ivar name: Name or identifier of this AdditionalParameter, unique
        for this OGC Web Service.
    :ivar value: Unordered list of one or more values of this
        AdditionalParameter.
    """
    class Meta:
        namespace = "http://www.opengis.net/ows/2.0"

    name: Optional[CodeType] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "required": True,
        }
    )
    value: List[object] = field(
        default_factory=list,
        metadata={
            "name": "Value",
            "type": "Element",
            "min_occurs": 1,
        }
    )
