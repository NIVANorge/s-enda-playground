from dataclasses import dataclass, field
from typing import List
from bindings.csw.functions_type import FunctionsType
from bindings.csw.simple_arithmetic import SimpleArithmetic

__NAMESPACE__ = "http://www.opengis.net/ogc"


@dataclass
class ArithmeticOperatorsType:
    simple_arithmetic: List[SimpleArithmetic] = field(
        default_factory=list,
        metadata={
            "name": "SimpleArithmetic",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        }
    )
    functions: List[FunctionsType] = field(
        default_factory=list,
        metadata={
            "name": "Functions",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        }
    )
