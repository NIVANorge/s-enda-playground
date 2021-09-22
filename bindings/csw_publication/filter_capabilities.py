from dataclasses import dataclass, field
from typing import Optional
from bindings.csw_publication.id_capabilities_type import IdCapabilitiesType
from bindings.csw_publication.scalar_capabilities_type import ScalarCapabilitiesType
from bindings.csw_publication.spatial_capabilities_type import SpatialCapabilitiesType

__NAMESPACE__ = "http://www.opengis.net/ogc"


@dataclass
class FilterCapabilities:
    class Meta:
        name = "Filter_Capabilities"
        namespace = "http://www.opengis.net/ogc"

    spatial_capabilities: Optional[SpatialCapabilitiesType] = field(
        default=None,
        metadata={
            "name": "Spatial_Capabilities",
            "type": "Element",
            "required": True,
        }
    )
    scalar_capabilities: Optional[ScalarCapabilitiesType] = field(
        default=None,
        metadata={
            "name": "Scalar_Capabilities",
            "type": "Element",
            "required": True,
        }
    )
    id_capabilities: Optional[IdCapabilitiesType] = field(
        default=None,
        metadata={
            "name": "Id_Capabilities",
            "type": "Element",
            "required": True,
        }
    )
