from dataclasses import dataclass, field
from typing import Optional
from bindings.gmd.abstract_surface_patch_type import AbstractSurfacePatchType
from bindings.gmd.aggregation_type import AggregationType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class AbstractParametricCurveSurfaceType(AbstractSurfacePatchType):
    aggregation_type: Optional[AggregationType] = field(
        default=None,
        metadata={
            "name": "aggregationType",
            "type": "Attribute",
        }
    )
