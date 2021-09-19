from dataclasses import dataclass, field
from typing import Optional
from bindings.csw.abstract_positional_accuracy_type import AbstractPositionalAccuracyType
from bindings.csw.result import Result

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class AbsoluteExternalPositionalAccuracyType(AbstractPositionalAccuracyType):
    """
    Closeness of reported coordinate values to values accepted as or being
    true.
    """
    result: Optional[Result] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )
