from dataclasses import dataclass, field
from typing import List
from bindings.wfs.value_2 import Value2

__NAMESPACE__ = "http://www.opengis.net/wfs/2.0"


@dataclass
class ValueListType:
    value: List[Value2] = field(
        default_factory=list,
        metadata={
            "name": "Value",
            "type": "Element",
            "namespace": "http://www.opengis.net/wfs/2.0",
            "min_occurs": 1,
        }
    )
