from dataclasses import dataclass, field
from typing import Optional
from bindings.csw_publication.geometry_operands_type import GeometryOperandsType
from bindings.csw_publication.spatial_operator_name_type import SpatialOperatorNameType

__NAMESPACE__ = "http://www.opengis.net/ogc"


@dataclass
class SpatialOperatorType:
    geometry_operands: Optional[GeometryOperandsType] = field(
        default=None,
        metadata={
            "name": "GeometryOperands",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        }
    )
    name: Optional[SpatialOperatorNameType] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
