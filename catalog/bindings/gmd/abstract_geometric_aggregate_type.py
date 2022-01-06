from dataclasses import dataclass, field
from typing import Optional
from bindings.gmd.abstract_geometry_type import AbstractGeometryType
from bindings.gmd.aggregation_type import AggregationType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class AbstractGeometricAggregateType(AbstractGeometryType):
    aggregation_type: Optional[AggregationType] = field(
        default=None,
        metadata={
            "name": "aggregationType",
            "type": "Attribute",
        },
    )
