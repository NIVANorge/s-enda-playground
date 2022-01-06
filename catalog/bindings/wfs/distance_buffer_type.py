from dataclasses import dataclass, field
from typing import List, Optional
from bindings.wfs.expression import Expression
from bindings.wfs.function_type import Function
from bindings.wfs.literal import Literal
from bindings.wfs.measure_type import MeasureType
from bindings.wfs.spatial_ops_type import SpatialOpsType

__NAMESPACE__ = "http://www.opengis.net/fes/2.0"


@dataclass
class DistanceBufferType(SpatialOpsType):
    literal: List[Literal] = field(
        default_factory=list,
        metadata={
            "name": "Literal",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
            "max_occurs": 2,
            "sequential": True,
        },
    )
    function: List[Function] = field(
        default_factory=list,
        metadata={
            "name": "Function",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
            "max_occurs": 2,
            "sequential": True,
        },
    )
    value_reference: List[str] = field(
        default_factory=list,
        metadata={
            "name": "ValueReference",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
            "max_occurs": 2,
            "sequential": True,
        },
    )
    expression: List[Expression] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
            "max_occurs": 2,
            "sequential": True,
        },
    )
    other_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
            "max_occurs": 2,
            "sequential": True,
        },
    )
    distance: Optional[MeasureType] = field(
        default=None,
        metadata={
            "name": "Distance",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
            "required": True,
        },
    )
