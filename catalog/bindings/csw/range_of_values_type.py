from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.opengis.net/cat/csw/2.0.2"


@dataclass
class RangeOfValuesType:
    min_value: Optional[object] = field(
        default=None,
        metadata={
            "name": "MinValue",
            "type": "Element",
            "namespace": "http://www.opengis.net/cat/csw/2.0.2",
        },
    )
    max_value: Optional[object] = field(
        default=None,
        metadata={
            "name": "MaxValue",
            "type": "Element",
            "namespace": "http://www.opengis.net/cat/csw/2.0.2",
        },
    )
