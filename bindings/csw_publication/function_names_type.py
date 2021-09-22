from dataclasses import dataclass, field
from typing import List
from bindings.csw_publication.function_name_type import FunctionNameType

__NAMESPACE__ = "http://www.opengis.net/ogc"


@dataclass
class FunctionNamesType:
    function_name: List[FunctionNameType] = field(
        default_factory=list,
        metadata={
            "name": "FunctionName",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
            "min_occurs": 1,
        }
    )
