from dataclasses import dataclass, field
from typing import List
from bindings.csw.abstract_geometry_type import AbstractGeometryType
from bindings.csw.geometric_primitive_property_type import (
    GeometricPrimitivePropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class GeometricComplexType(AbstractGeometryType):
    """
    A geometric complex.
    """

    element: List[GeometricPrimitivePropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "min_occurs": 1,
        },
    )
