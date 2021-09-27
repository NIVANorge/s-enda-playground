from dataclasses import dataclass, field
from typing import List, Optional
from bindings.gmd.abstract_geometry_type import AbstractGeometryType
from bindings.gmd.aggregation_type import AggregationType
from bindings.gmd.geometric_primitive_property_type import GeometricPrimitivePropertyType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class GeometricComplexType(AbstractGeometryType):
    element: List[GeometricPrimitivePropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "min_occurs": 1,
        }
    )
    aggregation_type: Optional[AggregationType] = field(
        default=None,
        metadata={
            "name": "aggregationType",
            "type": "Attribute",
        }
    )
