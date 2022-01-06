from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "http://www.opengis.net/cat/csw/2.0.2"


@dataclass
class ListOfValuesType:
    value: List[object] = field(
        default_factory=list,
        metadata={
            "name": "Value",
            "type": "Element",
            "namespace": "http://www.opengis.net/cat/csw/2.0.2",
            "min_occurs": 1,
        },
    )
