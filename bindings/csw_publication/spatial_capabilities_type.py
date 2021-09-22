from dataclasses import dataclass, field
from typing import Optional
from bindings.csw_publication.geometry_operands_type import GeometryOperandsType
from bindings.csw_publication.spatial_operators_type import SpatialOperatorsType

__NAMESPACE__ = "http://www.opengis.net/ogc"


@dataclass
class SpatialCapabilitiesType:
    class Meta:
        name = "Spatial_CapabilitiesType"

    geometry_operands: Optional[GeometryOperandsType] = field(
        default=None,
        metadata={
            "name": "GeometryOperands",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
            "required": True,
        }
    )
    spatial_operators: Optional[SpatialOperatorsType] = field(
        default=None,
        metadata={
            "name": "SpatialOperators",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
            "required": True,
        }
    )
