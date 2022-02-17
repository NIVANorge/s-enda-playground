from dataclasses import dataclass, field
from typing import Optional
from bindings.wfs.available_functions_type import AvailableFunctionsType
from bindings.wfs.conformance_type import ConformanceType
from bindings.wfs.extended_capabilities_type import ExtendedCapabilitiesType
from bindings.wfs.id_capabilities_type import IdCapabilitiesType
from bindings.wfs.scalar_capabilities_type import ScalarCapabilitiesType
from bindings.wfs.spatial_capabilities_type import SpatialCapabilitiesType
from bindings.wfs.temporal_capabilities_type import TemporalCapabilitiesType

__NAMESPACE__ = "http://www.opengis.net/fes/2.0"


@dataclass
class FilterCapabilities:
    class Meta:
        name = "Filter_Capabilities"
        namespace = "http://www.opengis.net/fes/2.0"

    conformance: Optional[ConformanceType] = field(
        default=None,
        metadata={
            "name": "Conformance",
            "type": "Element",
            "required": True,
        },
    )
    id_capabilities: Optional[IdCapabilitiesType] = field(
        default=None,
        metadata={
            "name": "Id_Capabilities",
            "type": "Element",
        },
    )
    scalar_capabilities: Optional[ScalarCapabilitiesType] = field(
        default=None,
        metadata={
            "name": "Scalar_Capabilities",
            "type": "Element",
        },
    )
    spatial_capabilities: Optional[SpatialCapabilitiesType] = field(
        default=None,
        metadata={
            "name": "Spatial_Capabilities",
            "type": "Element",
        },
    )
    temporal_capabilities: Optional[TemporalCapabilitiesType] = field(
        default=None,
        metadata={
            "name": "Temporal_Capabilities",
            "type": "Element",
        },
    )
    functions: Optional[AvailableFunctionsType] = field(
        default=None,
        metadata={
            "name": "Functions",
            "type": "Element",
        },
    )
    extended_capabilities: Optional[ExtendedCapabilitiesType] = field(
        default=None,
        metadata={
            "name": "Extended_Capabilities",
            "type": "Element",
        },
    )
