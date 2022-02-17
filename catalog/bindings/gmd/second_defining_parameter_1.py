from dataclasses import dataclass, field
from typing import Optional
from bindings.gmd.length_type import LengthType
from bindings.gmd.measure_type import MeasureType
from bindings.gmd.second_defining_parameter_is_sphere import (
    SecondDefiningParameterIsSphere,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class SecondDefiningParameter1:
    class Meta:
        name = "SecondDefiningParameter"
        namespace = "http://www.opengis.net/gml"

    inverse_flattening: Optional[MeasureType] = field(
        default=None,
        metadata={
            "name": "inverseFlattening",
            "type": "Element",
        },
    )
    semi_minor_axis: Optional[LengthType] = field(
        default=None,
        metadata={
            "name": "semiMinorAxis",
            "type": "Element",
        },
    )
    is_sphere: Optional[SecondDefiningParameterIsSphere] = field(
        default=None,
        metadata={
            "name": "isSphere",
            "type": "Element",
        },
    )
