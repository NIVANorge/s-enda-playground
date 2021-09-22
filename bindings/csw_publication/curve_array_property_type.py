from dataclasses import dataclass, field
from typing import List
from bindings.csw_publication.composite_curve_type import (
    CompositeCurve,
    Curve1,
    OrientableCurve,
)
from bindings.csw_publication.curve_2 import Curve2
from bindings.csw_publication.line_string import LineString

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class CurveArrayPropertyType:
    """A container for an array of curves.

    The elements are always contained in the array property, referencing
    geometry elements or arrays of geometry elements is not supported.
    """
    orientable_curve: List[OrientableCurve] = field(
        default_factory=list,
        metadata={
            "name": "OrientableCurve",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    curve: List[Curve1] = field(
        default_factory=list,
        metadata={
            "name": "Curve",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    composite_curve: List[CompositeCurve] = field(
        default_factory=list,
        metadata={
            "name": "CompositeCurve",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    line_string: List[LineString] = field(
        default_factory=list,
        metadata={
            "name": "LineString",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    opengis_net_gml_curve: List[Curve2] = field(
        default_factory=list,
        metadata={
            "name": "_Curve",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
