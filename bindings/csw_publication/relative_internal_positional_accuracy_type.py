from dataclasses import dataclass, field
from typing import Optional
from bindings.csw_publication.abstract_positional_accuracy_type import AbstractPositionalAccuracyType
from bindings.csw_publication.result import Result

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class RelativeInternalPositionalAccuracyType(AbstractPositionalAccuracyType):
    """
    Closeness of the relative positions of two or more positions to their
    respective relative positions accepted as or being true.
    """
    result: Optional[Result] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )
