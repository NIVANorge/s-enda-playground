from dataclasses import dataclass, field
from typing import List, Optional, Union
from bindings.csw_publication.null_enumeration_value import NullEnumerationValue

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class MeasureOrNullListType:
    """List of numbers with a uniform scale.

    A member of the list may be a typed null. The value of uom (Units Of
    Measure) attribute is a reference to a Reference System for the
    amount, either a ratio or position scale.
    """
    value: List[Union[str, NullEnumerationValue]] = field(
        default_factory=list,
        metadata={
            "pattern": r"other:\w{2,}",
            "tokens": True,
        }
    )
    uom: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
