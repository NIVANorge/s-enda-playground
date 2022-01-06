from dataclasses import dataclass, field
from typing import List
from bindings.wfs.argument_type import ArgumentType

__NAMESPACE__ = "http://www.opengis.net/fes/2.0"


@dataclass
class ArgumentsType:
    argument: List[ArgumentType] = field(
        default_factory=list,
        metadata={
            "name": "Argument",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
            "min_occurs": 1,
        },
    )
