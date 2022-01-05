from dataclasses import dataclass, field
from typing import Optional
from bindings.wfs.geometry_operands_type import GeometryOperandsType
from bindings.wfs.spatial_operators_type import SpatialOperatorsType

__NAMESPACE__ = "http://www.opengis.net/fes/2.0"


@dataclass
class SpatialCapabilitiesType:
    class Meta:
        name = "Spatial_CapabilitiesType"

    geometry_operands: Optional[GeometryOperandsType] = field(
        default=None,
        metadata={
            "name": "GeometryOperands",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
            "required": True,
        }
    )
    spatial_operators: Optional[SpatialOperatorsType] = field(
        default=None,
        metadata={
            "name": "SpatialOperators",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
            "required": True,
        }
    )
